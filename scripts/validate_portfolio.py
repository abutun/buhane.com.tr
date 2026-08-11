#!/usr/bin/env python3
"""Validate Buhane's private portfolio registry and public discovery surfaces.

The implementation intentionally uses only the Python standard library so every
portfolio repository can run it without adopting a shared build system.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Callable, Iterable, Mapping, Sequence


EXPECTED_PRODUCTS = {
    "moodjot": "https://moodjot.app/#product",
    "vynix": "https://vynix.app/#product",
    "swipe-slip": "https://swipeslip.app/#product",
    "glow-spin": "https://glowspin.app/#product",
    "hive-due": "https://hivedue.com/#product",
    "astral-post": "https://astralpost.app/#product",
    "gridzle": "https://gridzle.app/#product",
    "hoskin": "https://hoskin.app/#product",
    "lastimo": "https://lastimo.app/#product",
    "the-cosmic-meta": "https://thecosmicmeta.com/#product",
    "u2m": "https://u2m.io/#product",
}
BUHANE_PRODUCT_SLUGS = tuple(EXPECTED_PRODUCTS)
SOURCE_HTML_EXCLUSIONS = {
    "buhane": {"yandex_abc334285efd6c2e.html"},
}
EXPECTED_PROPERTIES = {"buhane", "ahmet-sh"}
EXPECTED_ENTITIES = {
    "buhane": "https://buhane.com.tr/#organization",
    "ahmet": "https://ahmet.sh/#person",
}
PRODUCT_REQUIRED_FIELDS = {
    "display_name",
    "legal_owner",
    "lifecycle_status",
    "category",
    "schema_type",
    "source_root",
    "public_root",
    "preferred_origin",
    "product_entity_id",
    "legacy_origins",
    "regional_origins",
    "default_locale",
    "indexable_locales",
    "canonical_routes",
    "sitemap_url",
    "robots_url",
    "store_urls",
    "support_url",
    "contact_url",
    "publisher_entity_id",
    "approved_contextual_links",
    "verified_features",
    "excluded_claims",
    "claim_reviewed_at",
    "generation_model",
    "validation_commands",
    "dirty_path_exclusions",
    "pending_source_rules",
    "external_status",
}
PROPERTY_REQUIRED_FIELDS = {
    "display_name",
    "property_type",
    "entity_id",
    "source_root",
    "public_root",
    "preferred_origin",
    "default_locale",
    "indexable_locales",
    "canonical_routes",
    "generation_model",
    "validation_commands",
    "dirty_path_exclusions",
    "pending_source_rules",
    "external_status",
}
VARIANT_REQUIRED_FIELDS = {
    "id",
    "build_command",
    "output_root",
    "preferred_origin",
    "indexable_locales",
    "robots_url",
    "sitemap_url",
}
ALLOWED_LIFECYCLES = {"live", "beta", "coming-soon", "retired"}
ALLOWED_EXTERNAL_STATES = {"local_editable", "external_blocked"}
PENDING_RULES = {
    "SRC.MISSING_DECLARED_ROUTE",
    "SRC.MISSING_ROBOTS",
    "SRC.MISSING_SITEMAP",
}
PRIVATE_ROUTE_RE = re.compile(
    r"/(?:admin|auth|dashboard|login|profile|recover|recovery|register|reset-password|signup)(?:/|$)",
    re.IGNORECASE,
)
PRIVATE_EXPOSURE_RE = re.compile(
    r"(?:^|/)(?:\.planning(?:/|$)|scripts(?:/|$))|portfolio-sites\.json",
    re.IGNORECASE,
)
EDITORIAL_TYPES = {"Article", "BlogPosting", "NewsArticle", "TechArticle", "FAQPage", "HowTo"}
SEARCH_AGENTS = [
    "Googlebot",
    "Bingbot",
    "OAI-SearchBot",
    "Claude-SearchBot",
    "PerplexityBot",
]
SEVERITIES = ("high", "medium", "low", "info")


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def normalized_origin(value: str) -> str:
    parsed = urllib.parse.urlsplit(value)
    if not parsed.scheme or not parsed.hostname:
        return ""
    port = parsed.port
    default_port = (parsed.scheme == "https" and port in (None, 443)) or (
        parsed.scheme == "http" and port in (None, 80)
    )
    authority = parsed.hostname.lower() if default_port else f"{parsed.hostname.lower()}:{port}"
    return f"{parsed.scheme.lower()}://{authority}"


def normalized_url(value: str) -> str:
    parsed = urllib.parse.urlsplit(value)
    path = parsed.path or "/"
    return urllib.parse.urlunsplit(
        (parsed.scheme.lower(), parsed.netloc.lower(), path, parsed.query, "")
    )


def is_https_origin(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    parsed = urllib.parse.urlsplit(value)
    return parsed.scheme == "https" and bool(parsed.hostname) and (parsed.path in ("", "/"))


def is_path_within(child: Path, parent: Path) -> bool:
    try:
        child.resolve().relative_to(parent.resolve())
        return True
    except (OSError, ValueError):
        return False


def ensure_list(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def schema_types(node: Mapping[str, Any]) -> set[str]:
    value = node.get("@type")
    if isinstance(value, str):
        return {value}
    if isinstance(value, list):
        return {item for item in value if isinstance(item, str)}
    return set()


def flatten_schema_nodes(value: Any) -> Iterable[dict[str, Any]]:
    if isinstance(value, dict):
        if "@type" in value or "@id" in value:
            yield value
        graph = value.get("@graph")
        if graph is not None:
            yield from flatten_schema_nodes(graph)
    elif isinstance(value, list):
        for item in value:
            yield from flatten_schema_nodes(item)


def referenced_ids(value: Any) -> set[str]:
    result: set[str] = set()
    if isinstance(value, str):
        result.add(value)
    elif isinstance(value, dict):
        if isinstance(value.get("@id"), str):
            result.add(value["@id"])
        for child in value.values():
            result.update(referenced_ids(child))
    elif isinstance(value, list):
        for child in value:
            result.update(referenced_ids(child))
    return result


@dataclass
class FetchResult:
    requested_url: str
    final_url: str
    status: int
    content_type: str
    body: bytes
    redirects: int
    redirect_statuses: tuple[int, ...] = ()


class RedirectOverflow(Exception):
    pass


class RequestBoundaryError(Exception):
    pass


class NoRedirectHandler(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req: Any, fp: Any, code: int, msg: str, headers: Any, newurl: str) -> None:
        return None


class PageParser(HTMLParser):
    """Small tolerant HTML extractor for metadata, links, text, and JSON-LD."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.titles: list[str] = []
        self.h1s: list[str] = []
        self.descriptions: list[str] = []
        self.canonicals: list[str] = []
        self.og_urls: list[str] = []
        self.robots: list[str] = []
        self.alternates: dict[str, str] = {}
        self.json_ld_raw: list[str] = []
        self.links: list[dict[str, Any]] = []
        self.resources: list[str] = []
        self.visible_text: list[str] = []
        self._title_parts: list[str] | None = None
        self._h1_parts: list[str] | None = None
        self._json_parts: list[str] | None = None
        self._anchor_parts: list[str] | None = None
        self._anchor_href: str | None = None
        self._anchor_in_footer = False
        self._footer_depth = 0
        self._hidden_depth = 0

    @staticmethod
    def _attrs(attrs: Sequence[tuple[str, str | None]]) -> dict[str, str]:
        return {key.lower(): value or "" for key, value in attrs}

    def handle_starttag(self, tag: str, attrs: Sequence[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        values = self._attrs(attrs)
        if tag == "footer":
            self._footer_depth += 1
        if tag in {"script", "style", "noscript", "template"}:
            self._hidden_depth += 1
        if tag == "title":
            self._title_parts = []
        elif tag == "h1":
            self._h1_parts = []
        elif tag == "meta":
            name = values.get("name", "").lower()
            prop = values.get("property", "").lower()
            content = values.get("content", "").strip()
            if name == "description":
                self.descriptions.append(content)
            elif name == "robots":
                self.robots.append(content.lower())
            elif prop == "og:url":
                self.og_urls.append(content)
        elif tag == "link":
            rel = {item.lower() for item in values.get("rel", "").split()}
            href = values.get("href", "").strip()
            if "canonical" in rel:
                self.canonicals.append(href)
            if "alternate" in rel and values.get("hreflang"):
                self.alternates[values["hreflang"]] = href
            if href and rel.intersection({"stylesheet", "icon", "preload", "manifest"}):
                self.resources.append(href)
        elif tag == "script":
            if values.get("type", "").lower() == "application/ld+json":
                self._json_parts = []
            if values.get("src"):
                self.resources.append(values["src"])
        elif tag in {"img", "source", "video", "audio"}:
            for key in ("src", "poster"):
                if values.get(key):
                    self.resources.append(values[key])
        elif tag == "a":
            self._anchor_parts = []
            self._anchor_href = values.get("href", "").strip()
            self._anchor_in_footer = self._footer_depth > 0

    def handle_startendtag(self, tag: str, attrs: Sequence[tuple[str, str | None]]) -> None:
        self.handle_starttag(tag, attrs)
        self.handle_endtag(tag)

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag == "title" and self._title_parts is not None:
            self.titles.append(" ".join("".join(self._title_parts).split()))
            self._title_parts = None
        elif tag == "h1" and self._h1_parts is not None:
            self.h1s.append(" ".join("".join(self._h1_parts).split()))
            self._h1_parts = None
        elif tag == "script" and self._json_parts is not None:
            self.json_ld_raw.append("".join(self._json_parts).strip())
            self._json_parts = None
        elif tag == "a" and self._anchor_parts is not None:
            self.links.append(
                {
                    "href": self._anchor_href or "",
                    "text": " ".join("".join(self._anchor_parts).split()),
                    "in_footer": self._anchor_in_footer,
                }
            )
            self._anchor_parts = None
            self._anchor_href = None
            self._anchor_in_footer = False
        if tag == "footer" and self._footer_depth:
            self._footer_depth -= 1
        if tag in {"script", "style", "noscript", "template"} and self._hidden_depth:
            self._hidden_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._title_parts is not None:
            self._title_parts.append(data)
        if self._h1_parts is not None:
            self._h1_parts.append(data)
        if self._json_parts is not None:
            self._json_parts.append(data)
        if self._anchor_parts is not None:
            self._anchor_parts.append(data)
        if not self._hidden_depth and data.strip():
            self.visible_text.append(data.strip())

    @property
    def text(self) -> str:
        return " ".join(" ".join(self.visible_text).split())


class FindingCollector:
    def __init__(self, allow_pending: bool, records: Mapping[str, Mapping[str, Any]]) -> None:
        self.allow_pending = allow_pending
        self.records = records
        self.findings: list[dict[str, Any]] = []
        self.skipped_pending_rules: dict[str, set[str]] = defaultdict(set)
        self._seen_ids: Counter[str] = Counter()

    def add(
        self,
        rule_id: str,
        property_id: str,
        severity: str,
        message: str,
        evidence: Any,
        *,
        publication_variant: str | None = None,
        route: str | None = None,
        pending_eligible: bool = False,
    ) -> None:
        record = self.records.get(property_id, {})
        declared = set(ensure_list(record.get("pending_source_rules")))
        if (
            self.allow_pending
            and pending_eligible
            and rule_id in PENDING_RULES
            and rule_id in declared
        ):
            self.skipped_pending_rules[property_id].add(rule_id)
            return
        severity = severity if severity in SEVERITIES else "high"
        route_key = route or ""
        raw_key = "\x1f".join(
            [property_id, publication_variant or "", rule_id, route_key]
        )
        digest = hashlib.sha256(raw_key.encode("utf-8")).hexdigest()[:16]
        base_id = f"F-{digest}"
        occurrence = self._seen_ids[base_id]
        self._seen_ids[base_id] += 1
        finding_id = base_id if occurrence == 0 else f"{base_id}-{occurrence + 1}"
        self.findings.append(
            {
                "finding_id": finding_id,
                "rule_id": rule_id,
                "property_id": property_id,
                "publication_variant": publication_variant,
                "severity": severity,
                "message": message,
                "evidence": evidence,
            }
        )


class PortfolioValidator:
    def __init__(
        self,
        manifest: Mapping[str, Any],
        manifest_path: Path,
        mode: str,
        selected_sites: Sequence[str] | None = None,
        timeout: float = 20.0,
        allow_pending: bool = False,
        fetcher: Callable[[str, set[str], float, str], FetchResult] | None = None,
    ) -> None:
        self.manifest = dict(manifest)
        self.manifest_path = manifest_path
        self.mode = mode
        self.timeout = timeout
        self.allow_pending = allow_pending
        self.products: dict[str, dict[str, Any]] = {
            key: dict(value)
            for key, value in (self.manifest.get("products") or {}).items()
            if isinstance(value, dict)
        }
        self.properties: dict[str, dict[str, Any]] = {
            key: dict(value)
            for key, value in (self.manifest.get("properties") or {}).items()
            if isinstance(value, dict)
        }
        self.records: dict[str, dict[str, Any]] = {**self.properties, **self.products}
        self.selected_sites = list(selected_sites or self.records.keys())
        self.collector = FindingCollector(allow_pending, self.records)
        self.fetcher = fetcher or self.fetch_url
        self.started_at = utc_now()
        self.site_results: dict[str, dict[str, Any]] = {}
        self.product_origins = {
            normalized_origin(record.get("preferred_origin", "")): product_id
            for product_id, record in self.products.items()
            if normalized_origin(record.get("preferred_origin", ""))
        }
        for product_id, record in self.products.items():
            for regional in ensure_list(record.get("regional_origins")):
                if isinstance(regional, dict):
                    origin = normalized_origin(regional.get("origin", ""))
                    if origin:
                        self.product_origins[origin] = product_id

    def validate(self) -> dict[str, Any]:
        self.validate_registry()
        if self.mode == "source":
            self.validate_source()
        elif self.mode == "live":
            self.validate_live()
        self._finalize_site_results()
        severity_counts = Counter(item["severity"] for item in self.collector.findings)
        exit_status = 1 if severity_counts["high"] else 0
        return {
            "mode": self.mode,
            "started_at": self.started_at,
            "sites": self.site_results,
            "findings": self.collector.findings,
            "severity_counts": {severity: severity_counts[severity] for severity in SEVERITIES},
            "skipped_pending_rules": {
                site: sorted(rule_ids)
                for site, rule_ids in sorted(self.collector.skipped_pending_rules.items())
            },
            "exit_status": exit_status,
        }

    def _initialize_site_result(self, site_id: str, record: Mapping[str, Any]) -> dict[str, Any]:
        result = self.site_results.setdefault(
            site_id,
            {
                "preferred_origin": record.get("preferred_origin"),
                "product_entity_id": record.get("product_entity_id"),
                "severity_counts": {severity: 0 for severity in SEVERITIES},
            },
        )
        variants = ensure_list(record.get("publication_variants"))
        if variants:
            variant_results = result.setdefault("publication_variants", {})
            for variant in variants:
                if not isinstance(variant, dict) or not isinstance(variant.get("id"), str):
                    continue
                variant_results.setdefault(
                    variant["id"],
                    {
                        "output_root": variant.get("output_root"),
                        "preferred_origin": variant.get("preferred_origin"),
                        "product_entity_id": record.get("product_entity_id"),
                        "severity_counts": {severity: 0 for severity in SEVERITIES},
                    },
                )
        return result

    def _finalize_site_results(self) -> None:
        for site_id in self.selected_sites:
            record = self.records.get(site_id)
            if record:
                self._initialize_site_result(site_id, record)
        for finding in self.collector.findings:
            site_id = finding["property_id"]
            result = self._initialize_site_result(site_id, self.records.get(site_id, {}))
            severity = finding["severity"]
            result["severity_counts"][severity] += 1
            variant_id = finding["publication_variant"]
            if variant_id and "publication_variants" in result:
                variant_result = result["publication_variants"].setdefault(
                    variant_id,
                    {
                        "output_root": None,
                        "preferred_origin": None,
                        "product_entity_id": self.records.get(site_id, {}).get("product_entity_id"),
                        "severity_counts": {item: 0 for item in SEVERITIES},
                    },
                )
                variant_result["severity_counts"][severity] += 1
        for site_id, skipped in self.collector.skipped_pending_rules.items():
            result = self._initialize_site_result(site_id, self.records.get(site_id, {}))
            result["skipped_pending_rules"] = sorted(skipped)

    def validate_registry(self) -> None:
        if self.manifest.get("schema_version") != "1.0":
            self.collector.add(
                "REG.SCHEMA_VERSION",
                "manifest",
                "high",
                "schema_version must be 1.0",
                {"actual": self.manifest.get("schema_version")},
            )
        if set(self.products) != set(EXPECTED_PRODUCTS):
            self.collector.add(
                "REG.PRODUCT_SET",
                "manifest",
                "high",
                "Registry must contain the exact eleven approved product IDs",
                {
                    "missing": sorted(set(EXPECTED_PRODUCTS) - set(self.products)),
                    "unexpected": sorted(set(self.products) - set(EXPECTED_PRODUCTS)),
                },
            )
        if set(self.properties) != EXPECTED_PROPERTIES:
            self.collector.add(
                "REG.PROPERTY_SET",
                "manifest",
                "high",
                "Registry must contain exactly the Buhane and ahmet.sh properties",
                {
                    "missing": sorted(EXPECTED_PROPERTIES - set(self.properties)),
                    "unexpected": sorted(set(self.properties) - EXPECTED_PROPERTIES),
                },
            )
        entities = self.manifest.get("entities") or {}
        for entity_name, expected_id in EXPECTED_ENTITIES.items():
            actual = entities.get(entity_name, {}).get("entity_id") if isinstance(entities, dict) else None
            if actual != expected_id:
                self.collector.add(
                    "REG.ENTITY_ID",
                    "manifest",
                    "high",
                    f"Stable {entity_name} entity ID does not match the contract",
                    {"expected": expected_id, "actual": actual},
                    route=entity_name,
                )
        manifest_allowlist = set(ensure_list(self.manifest.get("pending_source_rule_allowlist")))
        if manifest_allowlist != PENDING_RULES:
            self.collector.add(
                "REG.PENDING_ALLOWLIST",
                "manifest",
                "high",
                "Pending source rule allowlist contains a non-discovery rule or omits an approved one",
                {"expected": sorted(PENDING_RULES), "actual": sorted(manifest_allowlist)},
            )

        seen_origins: dict[str, str] = {}
        for property_id, record in self.properties.items():
            self._initialize_site_result(property_id, record)
            self._validate_required_fields(property_id, record, PROPERTY_REQUIRED_FIELDS)
            expected_entity = EXPECTED_ENTITIES["buhane" if property_id == "buhane" else "ahmet"]
            if record.get("entity_id") != expected_entity:
                self.collector.add(
                    "REG.ENTITY_ID",
                    property_id,
                    "high",
                    "Property entity_id differs from its stable entity contract",
                    {"expected": expected_entity, "actual": record.get("entity_id")},
                )
            self._validate_common_registry_fields(property_id, record, seen_origins)

        for product_id, record in self.products.items():
            self._initialize_site_result(product_id, record)
            self._validate_required_fields(product_id, record, PRODUCT_REQUIRED_FIELDS)
            self._validate_common_registry_fields(product_id, record, seen_origins)
            expected_id = EXPECTED_PRODUCTS.get(product_id)
            if record.get("product_entity_id") != expected_id:
                self.collector.add(
                    "REG.PRODUCT_ENTITY_ID",
                    product_id,
                    "high",
                    "product_entity_id differs from the approved preferred-origin identity",
                    {"expected": expected_id, "actual": record.get("product_entity_id")},
                )
            if record.get("legal_owner") != EXPECTED_ENTITIES["buhane"]:
                self.collector.add(
                    "REG.LEGAL_OWNER",
                    product_id,
                    "high",
                    "Every product must identify Buhane as legal owner",
                    {"actual": record.get("legal_owner")},
                )
            if record.get("publisher_entity_id") != EXPECTED_ENTITIES["buhane"]:
                self.collector.add(
                    "REG.PUBLISHER_ID",
                    product_id,
                    "high",
                    "Every product must reuse the Buhane publisher entity ID",
                    {"actual": record.get("publisher_entity_id")},
                )
            if record.get("lifecycle_status") not in ALLOWED_LIFECYCLES:
                self.collector.add(
                    "REG.LIFECYCLE_STATE",
                    product_id,
                    "high",
                    "lifecycle_status is not an allowed state",
                    {"actual": record.get("lifecycle_status")},
                )
            self._validate_contextual_links(product_id, record)
            self._validate_variants(product_id, record)

        required_lastimo_exclusions = {
            "history",
            "statistics",
            "analytics",
            "past_logs",
            "custom_trackers",
            "past_date_correction",
        }
        lastimo = self.products.get("lastimo", {})
        if not required_lastimo_exclusions.issubset(set(ensure_list(lastimo.get("excluded_claims")))):
            self.collector.add(
                "REG.LASTIMO_TRUTH",
                "lastimo",
                "high",
                "Lastimo excluded_claims omits one or more forbidden v1 capabilities",
                {
                    "missing": sorted(
                        required_lastimo_exclusions - set(ensure_list(lastimo.get("excluded_claims")))
                    )
                },
            )
        cosmic = self.products.get("the-cosmic-meta", {})
        if cosmic.get("external_status") != "external_blocked" or cosmic.get("source_root") is not None:
            self.collector.add(
                "REG.EXTERNAL_BLOCKER",
                "the-cosmic-meta",
                "high",
                "The Cosmic Meta must remain external_blocked with no local source_root",
                {
                    "external_status": cosmic.get("external_status"),
                    "source_root": cosmic.get("source_root"),
                },
            )

        for selected in self.selected_sites:
            if selected not in self.records:
                self.collector.add(
                    "REG.SITE_UNKNOWN",
                    selected,
                    "high",
                    "--site names a property that is not in the manifest",
                    {"site": selected},
                )

    def _validate_required_fields(
        self, property_id: str, record: Mapping[str, Any], required: set[str]
    ) -> None:
        missing = sorted(required - set(record))
        if missing:
            self.collector.add(
                "REG.REQUIRED_FIELD",
                property_id,
                "high",
                "Registry record is incomplete",
                {"missing": missing},
            )

    def _validate_common_registry_fields(
        self, property_id: str, record: Mapping[str, Any], seen_origins: dict[str, str]
    ) -> None:
        preferred = record.get("preferred_origin")
        if not is_https_origin(preferred):
            self.collector.add(
                "REG.PREFERRED_HTTPS",
                property_id,
                "high",
                "preferred_origin must be an absolute HTTPS origin",
                {"actual": preferred},
            )
        origin = normalized_origin(preferred) if isinstance(preferred, str) else ""
        if origin:
            if origin in seen_origins and seen_origins[origin] != property_id:
                self.collector.add(
                    "REG.ORIGIN_UNIQUE",
                    property_id,
                    "high",
                    "preferred_origin is assigned to more than one property",
                    {"origin": origin, "other_property": seen_origins[origin]},
                )
            seen_origins[origin] = property_id
        external_status = record.get("external_status")
        if external_status not in ALLOWED_EXTERNAL_STATES:
            self.collector.add(
                "REG.EXTERNAL_STATE",
                property_id,
                "high",
                "external_status is not an allowed state",
                {"actual": external_status},
            )
        source_root = record.get("source_root")
        public_root = record.get("public_root")
        if external_status == "local_editable":
            if not isinstance(source_root, str) or not Path(source_root).is_absolute():
                self.collector.add(
                    "REG.SOURCE_BOUNDARY",
                    property_id,
                    "high",
                    "Local properties require an absolute source_root",
                    {"source_root": source_root},
                )
            if not isinstance(public_root, str) or not Path(public_root).is_absolute():
                self.collector.add(
                    "REG.SOURCE_BOUNDARY",
                    property_id,
                    "high",
                    "Local properties require an absolute public_root",
                    {"public_root": public_root},
                    route="public_root",
                )
            elif isinstance(source_root, str) and not is_path_within(Path(public_root), Path(source_root)):
                self.collector.add(
                    "REG.SOURCE_BOUNDARY",
                    property_id,
                    "high",
                    "public_root must remain inside source_root",
                    {"source_root": source_root, "public_root": public_root},
                    route="containment",
                )
        pending = set(ensure_list(record.get("pending_source_rules")))
        invalid_pending = pending - PENDING_RULES
        if invalid_pending:
            self.collector.add(
                "REG.PENDING_RULE_UNSAFE",
                property_id,
                "high",
                "pending_source_rules may contain only missing route/discovery rules",
                {"invalid": sorted(invalid_pending)},
            )
        for legacy in ensure_list(record.get("legacy_origins")):
            if not is_https_origin(legacy):
                self.collector.add(
                    "REG.LEGACY_ORIGIN",
                    property_id,
                    "high",
                    "legacy_origins entries must be absolute HTTPS origins",
                    {"actual": legacy},
                    route=str(legacy),
                )
            if normalized_origin(str(legacy)) == origin:
                self.collector.add(
                    "REG.LEGACY_PREFERRED_SEPARATION",
                    property_id,
                    "high",
                    "A preferred origin cannot also be a legacy alias",
                    {"origin": legacy},
                    route=str(legacy),
                )

    def _validate_contextual_links(self, product_id: str, record: Mapping[str, Any]) -> None:
        links = ensure_list(record.get("approved_contextual_links"))
        invalid = sorted(
            link for link in links if not isinstance(link, str) or link not in EXPECTED_PRODUCTS or link == product_id
        )
        if len(links) != len(set(item for item in links if isinstance(item, str))) or invalid:
            self.collector.add(
                "REG.CONTEXTUAL_LINK_ALLOWLIST",
                product_id,
                "high",
                "approved_contextual_links contains an unknown, duplicate, or self link",
                {"invalid": invalid, "links": links},
            )

    def _validate_variants(self, product_id: str, record: Mapping[str, Any]) -> None:
        variants = ensure_list(record.get("publication_variants"))
        seen: set[str] = set()
        for index, variant in enumerate(variants):
            route = str(index)
            if not isinstance(variant, dict):
                self.collector.add(
                    "REG.VARIANT_INCOMPLETE",
                    product_id,
                    "high",
                    "publication_variants entries must be objects",
                    {"index": index},
                    route=route,
                )
                continue
            missing = sorted(VARIANT_REQUIRED_FIELDS - set(variant))
            variant_id = variant.get("id") if isinstance(variant.get("id"), str) else None
            if missing:
                self.collector.add(
                    "REG.VARIANT_INCOMPLETE",
                    product_id,
                    "high",
                    "Publication variant is missing required fields",
                    {"missing": missing},
                    publication_variant=variant_id,
                    route=route,
                )
            if variant_id in seen or not variant_id:
                self.collector.add(
                    "REG.VARIANT_ID",
                    product_id,
                    "high",
                    "Publication variant IDs must be nonempty and unique",
                    {"actual": variant_id},
                    publication_variant=variant_id,
                    route=route,
                )
            if variant_id:
                seen.add(variant_id)
            if "product_entity_id" in variant:
                self.collector.add(
                    "REG.VARIANT_PRODUCT_ID_OVERRIDE",
                    product_id,
                    "high",
                    "A publication variant may not override the product_entity_id",
                    {"actual": variant.get("product_entity_id")},
                    publication_variant=variant_id,
                )
            output_root = variant.get("output_root")
            if not isinstance(output_root, str) or Path(output_root).is_absolute() or ".." in Path(output_root).parts:
                self.collector.add(
                    "REG.VARIANT_OUTPUT_BOUNDARY",
                    product_id,
                    "high",
                    "Variant output_root must be a safe relative path",
                    {"actual": output_root},
                    publication_variant=variant_id,
                )
            for url_field in ("preferred_origin", "robots_url", "sitemap_url"):
                value = variant.get(url_field)
                if url_field == "preferred_origin":
                    valid = is_https_origin(value)
                else:
                    valid = isinstance(value, str) and urllib.parse.urlsplit(value).scheme == "https"
                if not valid:
                    self.collector.add(
                        "REG.VARIANT_URL",
                        product_id,
                        "high",
                        f"Variant {url_field} must be an absolute HTTPS URL",
                        {"field": url_field, "actual": value},
                        publication_variant=variant_id,
                        route=url_field,
                    )

    def validate_source(self) -> None:
        for site_id in self.selected_sites:
            record = self.records.get(site_id)
            if not record:
                continue
            self._initialize_site_result(site_id, record)
            if record.get("external_status") == "external_blocked":
                continue
            public_root_value = record.get("public_root")
            source_root_value = record.get("source_root")
            if not isinstance(public_root_value, str) or not isinstance(source_root_value, str):
                continue
            public_root = Path(public_root_value)
            source_root = Path(source_root_value)
            variants = ensure_list(record.get("publication_variants"))
            if variants:
                for variant in variants:
                    if not isinstance(variant, dict) or not isinstance(variant.get("id"), str):
                        continue
                    variant_id = variant["id"]
                    build_command = variant.get("build_command")
                    if isinstance(build_command, str) and build_command.strip():
                        self._run_command(
                            build_command,
                            public_root,
                            site_id,
                            "GEN.BUILD_FAILED",
                            publication_variant=variant_id,
                        )
                    output_root = public_root / str(variant.get("output_root", ""))
                    variant_contract = dict(record)
                    variant_contract.update(
                        {
                            "preferred_origin": variant.get("preferred_origin"),
                            "indexable_locales": variant.get("indexable_locales"),
                            "robots_url": variant.get("robots_url"),
                            "sitemap_url": variant.get("sitemap_url"),
                            "canonical_routes": variant.get("canonical_routes", ["/"]),
                        }
                    )
                    self._inspect_output(
                        site_id,
                        record,
                        variant_contract,
                        output_root,
                        publication_variant=variant_id,
                    )
            else:
                source_contract = self._source_contract(site_id, record)
                self._inspect_output(site_id, source_contract, source_contract, public_root)
            for command in ensure_list(record.get("validation_commands")):
                if isinstance(command, str) and command.strip():
                    self._run_command(command, source_root, site_id, "GEN.CHECK_FAILED")

    def _source_contract(
        self,
        site_id: str,
        record: Mapping[str, Any],
    ) -> dict[str, Any]:
        """Add source-owned route contracts without publishing them in the private registry."""
        contract = dict(record)
        if site_id != "buhane":
            return contract

        detail_routes = {
            route: EXPECTED_PRODUCTS[slug]
            for slug in BUHANE_PRODUCT_SLUGS
            for route in (f"/products/{slug}/", f"/tr/urunler/{slug}/")
        }
        contract.update(
            {
                "canonical_routes": [
                    "/",
                    "/tr/",
                    "/products/",
                    "/tr/urunler/",
                    *detail_routes,
                ],
                "robots_url": "https://buhane.com.tr/robots.txt",
                "sitemap_url": "https://buhane.com.tr/sitemap.xml",
                "product_detail_routes": detail_routes,
                "approved_contextual_links": list(BUHANE_PRODUCT_SLUGS),
            }
        )
        self._initialize_site_result(site_id, record)["product_detail_entity_ids"] = sorted(
            set(detail_routes.values())
        )
        return contract

    def _run_command(
        self,
        command: str,
        cwd: Path,
        site_id: str,
        rule_id: str,
        *,
        publication_variant: str | None = None,
    ) -> None:
        if not cwd.is_dir():
            self.collector.add(
                "SRC.OUTPUT_ROOT_MISSING",
                site_id,
                "high",
                "Command working directory does not exist",
                {"cwd": str(cwd), "command": command},
                publication_variant=publication_variant,
                route=str(cwd),
            )
            return
        result = subprocess.run(
            command,
            cwd=cwd,
            shell=True,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            timeout=max(30.0, self.timeout),
            check=False,
        )
        if result.returncode != 0:
            self.collector.add(
                rule_id,
                site_id,
                "high",
                "Repository-native build or validation command failed",
                {
                    "command": command,
                    "returncode": result.returncode,
                    "output_tail": result.stdout[-2000:],
                },
                publication_variant=publication_variant,
                route=command,
            )

    def _inspect_output(
        self,
        site_id: str,
        base_record: Mapping[str, Any],
        contract: Mapping[str, Any],
        root: Path,
        *,
        publication_variant: str | None = None,
    ) -> None:
        if not root.is_dir():
            self.collector.add(
                "SRC.OUTPUT_ROOT_MISSING",
                site_id,
                "high",
                "Declared public output root does not exist",
                {"output_root": str(root)},
                publication_variant=publication_variant,
                route=str(root),
            )
            return
        html_files = sorted(
            path
            for path in root.rglob("*.html")
            if not any(part.startswith(".") for part in path.relative_to(root).parts)
            and "node_modules" not in path.parts
            and "admin" not in {part.lower() for part in path.relative_to(root).parts}
            and path.name not in SOURCE_HTML_EXCLUSIONS.get(site_id, set())
        )
        pages: list[dict[str, Any]] = []
        for html_file in html_files:
            try:
                raw = html_file.read_text(encoding="utf-8")
            except (OSError, UnicodeError) as exc:
                self.collector.add(
                    "SRC.HTML_READ",
                    site_id,
                    "high",
                    "HTML file could not be read as UTF-8",
                    {"file": str(html_file), "error": str(exc)},
                    publication_variant=publication_variant,
                    route=str(html_file.relative_to(root)),
                )
                continue
            parser = PageParser()
            try:
                parser.feed(raw)
                parser.close()
            except Exception as exc:  # HTMLParser is tolerant; a failure is meaningful.
                self.collector.add(
                    "SRC.HTML_PARSE",
                    site_id,
                    "high",
                    "HTML parser failed",
                    {"file": str(html_file), "error": str(exc)},
                    publication_variant=publication_variant,
                    route=str(html_file.relative_to(root)),
                )
                continue
            route = self._file_route(html_file, root)
            noindex = any("noindex" in value for value in parser.robots)
            redirect_shell = bool(re.search(r"http-equiv\s*=\s*[\"']?refresh", raw, re.IGNORECASE))
            page = {
                "file": html_file,
                "route": route,
                "parser": parser,
                "raw": raw,
                "noindex": noindex,
                "redirect_shell": redirect_shell,
                "indexable": not noindex and not redirect_shell and not PRIVATE_ROUTE_RE.search(route),
            }
            pages.append(page)
            if page["indexable"]:
                self._validate_page(
                    site_id,
                    base_record,
                    contract,
                    root,
                    page,
                    publication_variant=publication_variant,
                )
            self._validate_links(
                site_id,
                base_record,
                contract,
                root,
                page,
                publication_variant=publication_variant,
            )

        for declared_route in ensure_list(contract.get("canonical_routes")):
            if not isinstance(declared_route, str):
                continue
            expected_file = self._route_file(root, declared_route)
            if not expected_file.is_file():
                self.collector.add(
                    "SRC.MISSING_DECLARED_ROUTE",
                    site_id,
                    "high",
                    "A declared canonical route is missing from the output",
                    {"route": declared_route, "expected_file": str(expected_file)},
                    publication_variant=publication_variant,
                    route=declared_route,
                    pending_eligible=True,
                )

        self._validate_uniqueness(site_id, pages, publication_variant)
        sitemap_urls = self._validate_sitemap(
            site_id,
            contract,
            root,
            pages,
            publication_variant=publication_variant,
        )
        self._validate_robots(
            site_id,
            contract,
            root,
            publication_variant=publication_variant,
        )
        self._validate_hreflang(
            site_id,
            contract,
            pages,
            sitemap_urls,
            publication_variant=publication_variant,
        )
        schema_nodes = [
            node
            for page in pages
            if page["indexable"]
            for raw in page["parser"].json_ld_raw
            for schema in self._parsed_schema_values(raw)
            for node in flatten_schema_nodes(schema)
        ]
        source_evidence = self._initialize_site_result(site_id, base_record).setdefault(
            "source_evidence", {}
        )
        source_evidence.update(
            {
                "indexable_route_count": sum(1 for page in pages if page["indexable"]),
                "sitemap_url_count": len(sitemap_urls),
                "schema_node_count": len(schema_nodes),
                "schema_types": sorted(
                    {schema_type for node in schema_nodes for schema_type in schema_types(node)}
                ),
            }
        )

    @staticmethod
    def _parsed_schema_values(raw: str) -> list[Any]:
        try:
            return [json.loads(raw)]
        except (json.JSONDecodeError, TypeError):
            return []

    @staticmethod
    def _file_route(path: Path, root: Path) -> str:
        relative = path.relative_to(root).as_posix()
        if relative == "index.html":
            return "/"
        if relative.endswith("/index.html"):
            return "/" + relative[: -len("index.html")]
        return "/" + relative

    @staticmethod
    def _route_file(root: Path, route: str) -> Path:
        parsed = urllib.parse.urlsplit(route)
        path = urllib.parse.unquote(parsed.path or "/").lstrip("/")
        if not path or path.endswith("/"):
            return root / path / "index.html"
        candidate = root / path
        if candidate.suffix:
            return candidate
        return candidate / "index.html"

    def _validate_page(
        self,
        site_id: str,
        base_record: Mapping[str, Any],
        contract: Mapping[str, Any],
        root: Path,
        page: Mapping[str, Any],
        *,
        publication_variant: str | None,
    ) -> None:
        parser: PageParser = page["parser"]
        route = str(page["route"])
        required_counts = {
            "META.TITLE": parser.titles,
            "META.H1": parser.h1s,
            "META.DESCRIPTION": parser.descriptions,
            "CANON.COUNT": parser.canonicals,
        }
        for rule_id, values in required_counts.items():
            if len(values) != 1 or not values[0].strip():
                self.collector.add(
                    rule_id,
                    site_id,
                    "high",
                    "Indexable page requires exactly one nonempty value",
                    {"file": str(page["file"]), "count": len(values)},
                    publication_variant=publication_variant,
                    route=route,
                )
        if not parser.canonicals:
            return
        canonical = parser.canonicals[0]
        preferred_origin = normalized_origin(str(contract.get("preferred_origin", "")))
        if urllib.parse.urlsplit(canonical).scheme != "https":
            self.collector.add(
                "CANON.HTTPS",
                site_id,
                "high",
                "Canonical URL must use HTTPS",
                {"canonical": canonical},
                publication_variant=publication_variant,
                route=route,
            )
        canonical_origin = normalized_origin(canonical)
        legacy_origins = {
            normalized_origin(item)
            for item in ensure_list(base_record.get("legacy_origins"))
            if isinstance(item, str)
        }
        if canonical_origin in legacy_origins:
            self.collector.add(
                "CANON.LEGACY_ORIGIN",
                site_id,
                "high",
                "Canonical URL uses a legacy redirect origin",
                {"canonical": canonical},
                publication_variant=publication_variant,
                route=route,
            )
        elif canonical_origin != preferred_origin:
            self.collector.add(
                "CANON.PREFERRED_ORIGIN",
                site_id,
                "high",
                "Canonical URL does not use the publication's preferred origin",
                {"canonical": canonical, "expected_origin": preferred_origin},
                publication_variant=publication_variant,
                route=route,
            )
        if len(parser.og_urls) != 1 or normalized_url(parser.og_urls[0]) != normalized_url(canonical):
            self.collector.add(
                "META.OG_CANONICAL",
                site_id,
                "high",
                "Open Graph URL must appear once and equal the canonical URL",
                {"canonical": canonical, "og_urls": parser.og_urls},
                publication_variant=publication_variant,
                route=route,
            )
        self._validate_schema(
            site_id,
            base_record,
            page,
            canonical,
            publication_variant=publication_variant,
        )
        self._validate_claims(
            site_id,
            base_record,
            parser.text,
            publication_variant=publication_variant,
            route=route,
        )

    def _validate_schema(
        self,
        site_id: str,
        record: Mapping[str, Any],
        page: Mapping[str, Any],
        canonical: str,
        *,
        publication_variant: str | None,
    ) -> None:
        parser: PageParser = page["parser"]
        route = str(page["route"])
        schemas: list[Any] = []
        for index, raw in enumerate(parser.json_ld_raw):
            try:
                schemas.append(json.loads(raw))
            except (json.JSONDecodeError, TypeError) as exc:
                self.collector.add(
                    "SCHEMA.INVALID_JSON",
                    site_id,
                    "high",
                    "JSON-LD block is not valid JSON",
                    {"error": str(exc), "block": index},
                    publication_variant=publication_variant,
                    route=route,
                )
        nodes = [node for schema in schemas for node in flatten_schema_nodes(schema)]
        product_entity_id = record.get("product_entity_id")
        publisher_id = record.get("publisher_entity_id")
        if isinstance(product_entity_id, str):
            primary_type = str(record.get("schema_type", ""))
            primary_nodes = [node for node in nodes if primary_type in schema_types(node)]
            if not primary_nodes and urllib.parse.urlsplit(canonical).path in ("", "/"):
                self.collector.add(
                    "SCHEMA.PRODUCT_ENTITY_MISSING",
                    site_id,
                    "high",
                    "Home/product page is missing its primary product schema",
                    {"expected_type": primary_type, "expected_id": product_entity_id},
                    publication_variant=publication_variant,
                    route=route,
                )
            for node in primary_nodes:
                if node.get("@id") != product_entity_id:
                    self.collector.add(
                        "ENTITY.PRODUCT_ID_MISMATCH",
                        site_id,
                        "high",
                        "Home/product schema must reuse the registry product_entity_id",
                        {"expected": product_entity_id, "actual": node.get("@id")},
                        publication_variant=publication_variant,
                        route=route,
                    )
                publisher_refs = referenced_ids(node.get("publisher"))
                if publisher_id and publisher_id not in publisher_refs:
                    self.collector.add(
                        "SCHEMA.PUBLISHER_ID",
                        site_id,
                        "high",
                        "Product schema must reference the approved Buhane publisher entity",
                        {"expected": publisher_id, "actual": sorted(publisher_refs)},
                        publication_variant=publication_variant,
                        route=route,
                    )
            reference_properties = ensure_list(
                record.get("product_reference_properties")
                or ["about", "mainEntity", "isPartOf"]
            )
            for node in nodes:
                if not schema_types(node).intersection(EDITORIAL_TYPES):
                    continue
                refs: set[str] = set()
                for key in reference_properties:
                    if isinstance(key, str) and key in node:
                        refs.update(referenced_ids(node[key]))
                product_like_refs = {value for value in refs if "#product" in value}
                if product_entity_id not in refs:
                    self.collector.add(
                        "ENTITY.EDITORIAL_PRODUCT_REFERENCE",
                        site_id,
                        "high",
                        "Editorial schema must reference the exact registry product_entity_id",
                        {
                            "expected": product_entity_id,
                            "actual_product_references": sorted(product_like_refs),
                        },
                        publication_variant=publication_variant,
                        route=route,
                    )
                publisher_refs = referenced_ids(node.get("publisher"))
                if publisher_id and publisher_id not in publisher_refs:
                    self.collector.add(
                        "SCHEMA.PUBLISHER_ID",
                        site_id,
                        "high",
                        "Editorial schema must reference the approved Buhane publisher entity",
                        {"expected": publisher_id, "actual": sorted(publisher_refs)},
                        publication_variant=publication_variant,
                        route=f"{route}:editorial",
                    )
        else:
            expected_entity = record.get("entity_id")
            if isinstance(expected_entity, str):
                matching = [node for node in nodes if node.get("@id") == expected_entity]
                if not matching:
                    self.collector.add(
                        "ENTITY.PROPERTY_ID_MISSING",
                        site_id,
                        "high",
                        "Property page is missing its stable entity ID",
                        {"expected": expected_entity},
                        publication_variant=publication_variant,
                        route=route,
                    )

        detail_routes = record.get("product_detail_routes") or {}
        if isinstance(detail_routes, dict) and route in detail_routes:
            expected = detail_routes[route]
            matching_nodes = [node for node in nodes if node.get("@id") == expected]
            if not matching_nodes:
                self.collector.add(
                    "ENTITY.HUB_PRODUCT_ID",
                    site_id,
                    "high",
                    "Buhane product detail page does not reuse the product origin's entity ID",
                    {"expected": expected},
                    publication_variant=publication_variant,
                    route=route,
                )
                return

            product_id = next(
                (key for key, value in EXPECTED_PRODUCTS.items() if value == expected),
                None,
            )
            product_record = self.products.get(product_id or "", {})
            expected_type = product_record.get("schema_type")
            expected_origin = product_record.get("preferred_origin")
            if expected_type and not any(
                expected_type in schema_types(node) for node in matching_nodes
            ):
                self.collector.add(
                    "SCHEMA.HUB_PRODUCT_TYPE",
                    site_id,
                    "Buhane detail page uses the wrong primary product schema type",
                    {"expected_type": expected_type, "product_entity_id": expected},
                    publication_variant=publication_variant,
                    route=route,
                )
            if expected_origin and not any(
                normalized_url(str(node.get("url", ""))) == normalized_url(str(expected_origin))
                for node in matching_nodes
            ):
                self.collector.add(
                    "ENTITY.HUB_PRODUCT_URL",
                    site_id,
                    "Buhane detail product node must keep the preferred product origin URL",
                    {"expected": expected_origin},
                    publication_variant=publication_variant,
                    route=route,
                )
            if not any(
                EXPECTED_ENTITIES["buhane"] in referenced_ids(node.get("publisher"))
                for node in matching_nodes
            ):
                self.collector.add(
                    "SCHEMA.HUB_PRODUCT_PUBLISHER",
                    site_id,
                    "Buhane detail product node must reference the Buhane publisher",
                    {"expected": EXPECTED_ENTITIES["buhane"]},
                    publication_variant=publication_variant,
                    route=route,
                )
            web_page_nodes = [
                node for node in nodes if schema_types(node).intersection({"WebPage", "CollectionPage"})
            ]
            if not any(
                normalized_url(str(node.get("url", ""))) == normalized_url(canonical)
                for node in web_page_nodes
            ):
                self.collector.add(
                    "SCHEMA.WEBPAGE_CANONICAL",
                    site_id,
                    "Detail WebPage URL must equal the page canonical",
                    {"canonical": canonical},
                    publication_variant=publication_variant,
                    route=route,
                )

    def _validate_claims(
        self,
        site_id: str,
        record: Mapping[str, Any],
        text: str,
        *,
        publication_variant: str | None,
        route: str,
    ) -> None:
        normalized_text = re.sub(r"[^a-z0-9]+", " ", text.lower())
        for claim in ensure_list(record.get("excluded_claims")):
            if not isinstance(claim, str):
                continue
            phrase = re.sub(r"[^a-z0-9]+", " ", claim.lower()).strip()
            if phrase and re.search(rf"\b{re.escape(phrase)}\b", normalized_text):
                self.collector.add(
                    "CLAIM.EXCLUDED",
                    site_id,
                    "high",
                    "Visible public copy contains a registry-excluded claim",
                    {"claim": claim},
                    publication_variant=publication_variant,
                    route=route,
                )

    def _validate_links(
        self,
        site_id: str,
        record: Mapping[str, Any],
        contract: Mapping[str, Any],
        root: Path,
        page: Mapping[str, Any],
        *,
        publication_variant: str | None,
    ) -> None:
        parser: PageParser = page["parser"]
        route = str(page["route"])
        canonical_base = parser.canonicals[0] if parser.canonicals else urllib.parse.urljoin(
            str(contract.get("preferred_origin", "")), route.lstrip("/")
        )
        own_origin = normalized_origin(str(contract.get("preferred_origin", "")))
        owner_link_found = site_id not in self.products
        sibling_links: list[tuple[str, bool]] = []
        all_refs: list[str] = [item["href"] for item in parser.links] + parser.resources
        for ref in all_refs:
            if not ref or ref.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
                continue
            absolute = urllib.parse.urljoin(canonical_base, ref)
            parsed = urllib.parse.urlsplit(absolute)
            absolute_origin = normalized_origin(absolute)
            if PRIVATE_EXPOSURE_RE.search(parsed.path):
                self.collector.add(
                    "SEC.PRIVATE_REGISTRY_EXPOSED",
                    site_id,
                    "high",
                    "Public HTML references a private planning, script, or registry path",
                    {"url": absolute},
                    publication_variant=publication_variant,
                    route=route,
                )
            if absolute_origin == own_origin:
                candidate = self._url_to_local_file(root, parsed.path)
                if candidate is not None and not candidate.exists():
                    self.collector.add(
                        "LINK.LOCAL_MISSING",
                        site_id,
                        "high",
                        "Internal link or asset does not resolve inside the output root",
                        {"url": absolute, "expected_file": str(candidate)},
                        publication_variant=publication_variant,
                        route=f"{route}:{parsed.path}",
                    )
        for link in parser.links:
            href = link["href"]
            if not href or href.startswith(("#", "mailto:", "tel:", "javascript:")):
                continue
            absolute = urllib.parse.urljoin(canonical_base, href)
            origin = normalized_origin(absolute)
            if origin == normalized_origin("https://buhane.com.tr/") and link["text"].strip():
                owner_link_found = True
            sibling_id = self.product_origins.get(origin)
            if sibling_id and sibling_id != site_id:
                sibling_links.append((sibling_id, bool(link["in_footer"])))
                if sibling_id not in ensure_list(record.get("approved_contextual_links")):
                    self.collector.add(
                        "LINK.SIBLING_NOT_ALLOWED",
                        site_id,
                        "high",
                        "Sibling-product link is not approved for this property",
                        {"destination_product": sibling_id, "url": absolute},
                        publication_variant=publication_variant,
                        route=f"{route}:{sibling_id}",
                    )
        footer_siblings = {sibling_id for sibling_id, in_footer in sibling_links if in_footer}
        if len(footer_siblings) >= 3:
            self.collector.add(
                "LINK.BLANKET_SIBLING_LIST",
                site_id,
                "high",
                "Footer contains a blanket sibling-product portfolio list",
                {"products": sorted(footer_siblings)},
                publication_variant=publication_variant,
                route=route,
            )
        if site_id in self.products and page["indexable"] and route == "/" and not owner_link_found:
            self.collector.add(
                "LINK.OWNER_MISSING",
                site_id,
                "high",
                "Product home page lacks a visible link to Buhane",
                {"expected_origin": "https://buhane.com.tr/"},
                publication_variant=publication_variant,
                route=route,
            )

    @staticmethod
    def _url_to_local_file(root: Path, path: str) -> Path | None:
        decoded = urllib.parse.unquote(path).lstrip("/")
        candidate = (root / decoded).resolve()
        if not is_path_within(candidate, root):
            return None
        if path.endswith("/") or not Path(decoded).suffix:
            if candidate.is_file():
                return candidate
            return candidate / "index.html"
        return candidate

    def _validate_uniqueness(
        self,
        site_id: str,
        pages: Sequence[Mapping[str, Any]],
        publication_variant: str | None,
    ) -> None:
        values: dict[str, dict[str, list[str]]] = {
            "META.TITLE_UNIQUE": defaultdict(list),
            "META.DESCRIPTION_UNIQUE": defaultdict(list),
            "CANON.UNIQUE": defaultdict(list),
        }
        for page in pages:
            if not page["indexable"]:
                continue
            parser: PageParser = page["parser"]
            route = str(page["route"])
            if len(parser.titles) == 1:
                values["META.TITLE_UNIQUE"][parser.titles[0]].append(route)
            if len(parser.descriptions) == 1:
                values["META.DESCRIPTION_UNIQUE"][parser.descriptions[0]].append(route)
            if len(parser.canonicals) == 1:
                values["CANON.UNIQUE"][normalized_url(parser.canonicals[0])].append(route)
        for rule_id, grouped in values.items():
            for value, routes in grouped.items():
                if len(routes) > 1:
                    self.collector.add(
                        rule_id,
                        site_id,
                        "high",
                        "Indexable pages reuse metadata that must be unique",
                        {"value": value, "routes": routes},
                        publication_variant=publication_variant,
                        route="|".join(sorted(routes)),
                    )

    def _validate_sitemap(
        self,
        site_id: str,
        contract: Mapping[str, Any],
        root: Path,
        pages: Sequence[Mapping[str, Any]],
        *,
        publication_variant: str | None,
    ) -> set[str]:
        sitemap_url = contract.get("sitemap_url")
        if not isinstance(sitemap_url, str):
            return set()
        sitemap_path = self._url_to_local_file(root, urllib.parse.urlsplit(sitemap_url).path)
        if sitemap_path is None or not sitemap_path.is_file():
            self.collector.add(
                "SRC.MISSING_SITEMAP",
                site_id,
                "high",
                "Declared sitemap file is missing",
                {"sitemap_url": sitemap_url, "expected_file": str(sitemap_path)},
                publication_variant=publication_variant,
                route=sitemap_url,
                pending_eligible=True,
            )
            return set()
        urls = self._read_local_sitemap(
            site_id,
            contract,
            root,
            sitemap_path,
            publication_variant=publication_variant,
        )
        preferred_origin = normalized_origin(str(contract.get("preferred_origin", "")))
        canonical_to_page: dict[str, Mapping[str, Any]] = {}
        for page in pages:
            parser: PageParser = page["parser"]
            if page["indexable"] and len(parser.canonicals) == 1:
                canonical_to_page[normalized_url(parser.canonicals[0])] = page
        for url in urls:
            parsed = urllib.parse.urlsplit(url)
            if normalized_origin(url) != preferred_origin:
                self.collector.add(
                    "SITEMAP.NONCANONICAL_ORIGIN",
                    site_id,
                    "high",
                    "Sitemap URL does not use the preferred publication origin",
                    {"url": url, "expected_origin": preferred_origin},
                    publication_variant=publication_variant,
                    route=url,
                )
            if PRIVATE_ROUTE_RE.search(parsed.path):
                self.collector.add(
                    "SITEMAP.PRIVATE_ROUTE",
                    site_id,
                    "high",
                    "Sitemap exposes an auth, admin, recovery, or private route",
                    {"url": url},
                    publication_variant=publication_variant,
                    route=url,
                )
            if PRIVATE_EXPOSURE_RE.search(parsed.path):
                self.collector.add(
                    "SEC.PRIVATE_REGISTRY_EXPOSED",
                    site_id,
                    "high",
                    "Sitemap exposes a private planning, script, or registry path",
                    {"url": url},
                    publication_variant=publication_variant,
                    route=url,
                )
            page = canonical_to_page.get(normalized_url(url))
            if page is None:
                self.collector.add(
                    "SITEMAP.NONCANONICAL_PAGE",
                    site_id,
                    "high",
                    "Sitemap URL does not map to an inspected canonical indexable page",
                    {"url": url},
                    publication_variant=publication_variant,
                    route=url,
                )
        for canonical in sorted(set(canonical_to_page) - {normalized_url(url) for url in urls}):
            self.collector.add(
                "SITEMAP.MISSING_CANONICAL",
                site_id,
                "high",
                "Canonical indexable page is absent from the sitemap",
                {"canonical": canonical},
                publication_variant=publication_variant,
                route=canonical,
            )
        return urls

    def _read_local_sitemap(
        self,
        site_id: str,
        contract: Mapping[str, Any],
        root: Path,
        sitemap_path: Path,
        *,
        publication_variant: str | None,
        seen: set[Path] | None = None,
    ) -> set[str]:
        seen = seen or set()
        if sitemap_path in seen:
            return set()
        seen.add(sitemap_path)
        try:
            tree = ET.parse(sitemap_path)
        except (ET.ParseError, OSError) as exc:
            self.collector.add(
                "SITEMAP.INVALID_XML",
                site_id,
                "high",
                "Sitemap XML could not be parsed",
                {"file": str(sitemap_path), "error": str(exc)},
                publication_variant=publication_variant,
                route=str(sitemap_path),
            )
            return set()
        root_node = tree.getroot()
        local_name = root_node.tag.rsplit("}", 1)[-1]
        locations = {
            (node.text or "").strip()
            for node in root_node.iter()
            if node.tag.rsplit("}", 1)[-1] == "loc" and (node.text or "").strip()
        }
        if len(locations) != sum(
            1
            for node in root_node.iter()
            if node.tag.rsplit("}", 1)[-1] == "loc" and (node.text or "").strip()
        ):
            self.collector.add(
                "SITEMAP.DUPLICATE_URL",
                site_id,
                "high",
                "Sitemap contains duplicate loc values",
                {"file": str(sitemap_path)},
                publication_variant=publication_variant,
                route=str(sitemap_path),
            )
        if local_name == "sitemapindex":
            urls: set[str] = set()
            expected_origin = normalized_origin(str(contract.get("preferred_origin", "")))
            for location in locations:
                if normalized_origin(location) != expected_origin:
                    self.collector.add(
                        "SITEMAP.NONCANONICAL_ORIGIN",
                        site_id,
                        "high",
                        "Sitemap index references a different origin",
                        {"url": location},
                        publication_variant=publication_variant,
                        route=location,
                    )
                    continue
                child = self._url_to_local_file(root, urllib.parse.urlsplit(location).path)
                if child and child.is_file():
                    urls.update(
                        self._read_local_sitemap(
                            site_id,
                            contract,
                            root,
                            child,
                            publication_variant=publication_variant,
                            seen=seen,
                        )
                    )
                else:
                    self.collector.add(
                        "SRC.MISSING_SITEMAP",
                        site_id,
                        "high",
                        "Sitemap index references a missing local sitemap",
                        {"url": location, "expected_file": str(child)},
                        publication_variant=publication_variant,
                        route=location,
                        pending_eligible=True,
                    )
            return urls
        return locations

    def _validate_robots(
        self,
        site_id: str,
        contract: Mapping[str, Any],
        root: Path,
        *,
        publication_variant: str | None,
    ) -> None:
        robots_url = contract.get("robots_url")
        sitemap_url = contract.get("sitemap_url")
        if not isinstance(robots_url, str):
            return
        robots_path = self._url_to_local_file(root, urllib.parse.urlsplit(robots_url).path)
        if robots_path is None or not robots_path.is_file():
            self.collector.add(
                "SRC.MISSING_ROBOTS",
                site_id,
                "high",
                "Declared robots.txt file is missing",
                {"robots_url": robots_url, "expected_file": str(robots_path)},
                publication_variant=publication_variant,
                route=robots_url,
                pending_eligible=True,
            )
            return
        try:
            text = robots_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            self.collector.add(
                "ROBOTS.READ",
                site_id,
                "high",
                "robots.txt could not be read",
                {"file": str(robots_path), "error": str(exc)},
                publication_variant=publication_variant,
                route=robots_url,
            )
            return
        declared_sitemaps = [
            match.group(1).strip()
            for match in re.finditer(r"^\s*Sitemap:\s*(\S+)\s*$", text, re.IGNORECASE | re.MULTILINE)
        ]
        if not isinstance(sitemap_url, str) or declared_sitemaps != [sitemap_url]:
            self.collector.add(
                "ROBOTS.SITEMAP_MISMATCH",
                site_id,
                "high",
                "robots.txt must name exactly the publication's canonical sitemap URL",
                {"expected": sitemap_url, "actual": declared_sitemaps},
                publication_variant=publication_variant,
                route=robots_url,
            )
        if re.search(r"^\s*Disallow:\s*/\s*$", text, re.IGNORECASE | re.MULTILINE):
            self.collector.add(
                "ROBOTS.PUBLIC_BLOCKED",
                site_id,
                "high",
                "robots.txt blocks the whole public site",
                {"file": str(robots_path)},
                publication_variant=publication_variant,
                route=robots_url,
            )

    def _validate_hreflang(
        self,
        site_id: str,
        contract: Mapping[str, Any],
        pages: Sequence[Mapping[str, Any]],
        sitemap_urls: set[str],
        *,
        publication_variant: str | None,
    ) -> None:
        locales = [item for item in ensure_list(contract.get("indexable_locales")) if isinstance(item, str)]
        canonical_map: dict[str, PageParser] = {}
        for page in pages:
            parser: PageParser = page["parser"]
            if page["indexable"] and len(parser.canonicals) == 1:
                canonical_map[normalized_url(parser.canonicals[0])] = parser
        if len(locales) <= 1:
            for canonical, parser in canonical_map.items():
                if parser.alternates:
                    self.collector.add(
                        "LOCALE.NONADDRESSABLE_HREFLANG",
                        site_id,
                        "high",
                        "Single-URL locale architecture must not advertise indexable alternates",
                        {"canonical": canonical, "alternates": parser.alternates},
                        publication_variant=publication_variant,
                        route=canonical,
                    )
            return
        for canonical, parser in canonical_map.items():
            required = set(locales)
            actual = set(parser.alternates)
            missing = sorted(required - actual)
            if missing or canonical not in {normalized_url(url) for url in parser.alternates.values()}:
                self.collector.add(
                    "LOCALE.HREFLANG_INCOMPLETE",
                    site_id,
                    "high",
                    "Localized page lacks a complete self-referential hreflang set",
                    {
                        "canonical": canonical,
                        "missing_locales": missing,
                        "alternates": parser.alternates,
                    },
                    publication_variant=publication_variant,
                    route=canonical,
                )
            for locale, alternate in parser.alternates.items():
                if locale == "x-default":
                    continue
                alternate_key = normalized_url(alternate)
                peer = canonical_map.get(alternate_key)
                if peer is None:
                    self.collector.add(
                        "LOCALE.HREFLANG_TARGET",
                        site_id,
                        "high",
                        "hreflang alternate is not a canonical indexable page in this output",
                        {"canonical": canonical, "locale": locale, "alternate": alternate},
                        publication_variant=publication_variant,
                        route=f"{canonical}:{locale}",
                    )
                elif canonical not in {normalized_url(value) for value in peer.alternates.values()}:
                    self.collector.add(
                        "LOCALE.HREFLANG_RECIPROCAL",
                        site_id,
                        "high",
                        "hreflang relationship is not reciprocal",
                        {"canonical": canonical, "alternate": alternate},
                        publication_variant=publication_variant,
                        route=f"{canonical}:{locale}",
                    )

    def validate_live(self) -> None:
        for site_id in self.selected_sites:
            record = self.records.get(site_id)
            if not record:
                continue
            self._initialize_site_result(site_id, record)
            allowed_origins = self._allowed_origins(record)
            targets = ensure_list(record.get("publication_variants")) or [record]
            for target in targets:
                if not isinstance(target, dict):
                    continue
                variant_id = target.get("id") if target is not record else None
                preferred_origin = target.get("preferred_origin") or record.get("preferred_origin")
                if not isinstance(preferred_origin, str):
                    continue
                try:
                    home = self._safe_fetch(preferred_origin, allowed_origins, "PortfolioValidator/1.0")
                    self._validate_live_home(site_id, preferred_origin, home, variant_id)
                except RequestBoundaryError as exc:
                    self._live_boundary_finding(site_id, preferred_origin, exc, variant_id)
                    continue
                except RedirectOverflow as exc:
                    self.collector.add(
                        "LIVE.REDIRECT_OVERFLOW",
                        site_id,
                        "high",
                        "Preferred origin exceeded the three-redirect cap",
                        {"url": preferred_origin, "error": str(exc)},
                        publication_variant=variant_id,
                        route=preferred_origin,
                    )
                    continue
                except (OSError, urllib.error.URLError) as exc:
                    self.collector.add(
                        "LIVE.REQUEST_FAILED",
                        site_id,
                        "high",
                        "Preferred origin request failed",
                        {"url": preferred_origin, "error": str(exc)},
                        publication_variant=variant_id,
                        route=preferred_origin,
                    )
                    continue
                for field, expected_kind in (("robots_url", "text"), ("sitemap_url", "xml")):
                    url = target.get(field) or record.get(field)
                    if isinstance(url, str):
                        self._validate_live_discovery(
                            site_id,
                            url,
                            expected_kind,
                            allowed_origins,
                            variant_id,
                        )
                for agent in ensure_list(self.manifest.get("search_citation_agents")) or SEARCH_AGENTS:
                    if not isinstance(agent, str):
                        continue
                    try:
                        result = self._safe_fetch(preferred_origin, allowed_origins, agent)
                        if result.status != 200:
                            self.collector.add(
                                "LIVE.SEARCH_AGENT_BLOCKED",
                                site_id,
                                "high",
                                "Configured search/citation agent did not receive HTTP 200",
                                {"agent": agent, "status": result.status},
                                publication_variant=variant_id,
                                route=f"{preferred_origin}:{agent}",
                            )
                    except (RequestBoundaryError, RedirectOverflow, OSError, urllib.error.URLError) as exc:
                        self.collector.add(
                            "LIVE.SEARCH_AGENT_BLOCKED",
                            site_id,
                            "high",
                            "Configured search/citation agent request failed",
                            {"agent": agent, "error": str(exc)},
                            publication_variant=variant_id,
                            route=f"{preferred_origin}:{agent}",
                        )
            preferred_origin = record.get("preferred_origin")
            for legacy in ensure_list(record.get("legacy_origins")):
                if not isinstance(legacy, str) or not isinstance(preferred_origin, str):
                    continue
                try:
                    result = self._safe_fetch(legacy, allowed_origins, "PortfolioValidator/1.0")
                    if (
                        result.status != 200
                        or result.redirects != 1
                        or result.redirect_statuses not in {(301,), (308,)}
                        or normalized_origin(result.final_url) != normalized_origin(preferred_origin)
                    ):
                        self.collector.add(
                            "LIVE.LEGACY_REDIRECT",
                            site_id,
                            "high",
                            "Legacy origin must permanently resolve to the preferred origin in one hop",
                            {
                                "legacy": legacy,
                                "final_url": result.final_url,
                                "status": result.status,
                                "redirects": result.redirects,
                                "redirect_statuses": list(result.redirect_statuses),
                            },
                            route=legacy,
                        )
                except RedirectOverflow as exc:
                    self.collector.add(
                        "LIVE.REDIRECT_OVERFLOW",
                        site_id,
                        "high",
                        "Legacy origin exceeded the three-redirect cap",
                        {"url": legacy, "error": str(exc)},
                        route=legacy,
                    )
                except RequestBoundaryError as exc:
                    self._live_boundary_finding(site_id, legacy, exc, None)
                except (OSError, urllib.error.URLError) as exc:
                    self.collector.add(
                        "LIVE.REQUEST_FAILED",
                        site_id,
                        "high",
                        "Legacy origin request failed",
                        {"url": legacy, "error": str(exc)},
                        route=legacy,
                    )

    def _allowed_origins(self, record: Mapping[str, Any]) -> set[str]:
        values: list[Any] = [record.get("preferred_origin")]
        values.extend(ensure_list(record.get("legacy_origins")))
        for regional in ensure_list(record.get("regional_origins")):
            if isinstance(regional, dict):
                values.append(regional.get("origin"))
        for variant in ensure_list(record.get("publication_variants")):
            if isinstance(variant, dict):
                values.append(variant.get("preferred_origin"))
        return {
            normalized_origin(value)
            for value in values
            if isinstance(value, str) and normalized_origin(value)
        }

    def _safe_fetch(self, url: str, allowed_origins: set[str], user_agent: str) -> FetchResult:
        if normalized_origin(url) not in allowed_origins:
            raise RequestBoundaryError(f"origin {normalized_origin(url)!r} is not manifest-approved")
        return self.fetcher(url, allowed_origins, self.timeout, user_agent)

    def fetch_url(
        self, url: str, allowed_origins: set[str], timeout: float, user_agent: str
    ) -> FetchResult:
        current = url
        redirects = 0
        redirect_statuses: list[int] = []
        opener = urllib.request.build_opener(NoRedirectHandler())
        while True:
            if normalized_origin(current) not in allowed_origins:
                raise RequestBoundaryError(
                    f"redirect target origin {normalized_origin(current)!r} is not manifest-approved"
                )
            request = urllib.request.Request(
                current,
                headers={
                    "User-Agent": user_agent,
                    "Accept": "text/html,application/xml,text/xml,text/plain;q=0.9,*/*;q=0.1",
                },
                method="GET",
            )
            try:
                response = opener.open(request, timeout=timeout)
            except urllib.error.HTTPError as exc:
                if exc.code in {301, 302, 303, 307, 308} and exc.headers.get("Location"):
                    redirects += 1
                    redirect_statuses.append(exc.code)
                    if redirects > 3:
                        raise RedirectOverflow(f"more than 3 redirects while requesting {url}")
                    current = urllib.parse.urljoin(current, exc.headers["Location"])
                    continue
                body = exc.read(2_000_000)
                return FetchResult(
                    requested_url=url,
                    final_url=current,
                    status=exc.code,
                    content_type=exc.headers.get_content_type(),
                    body=body,
                    redirects=redirects,
                    redirect_statuses=tuple(redirect_statuses),
                )
            with response:
                return FetchResult(
                    requested_url=url,
                    final_url=response.geturl(),
                    status=response.getcode(),
                    content_type=response.headers.get_content_type(),
                    body=response.read(2_000_000),
                    redirects=redirects,
                    redirect_statuses=tuple(redirect_statuses),
                )

    def _validate_live_home(
        self,
        site_id: str,
        preferred_origin: str,
        result: FetchResult,
        publication_variant: str | None,
    ) -> None:
        if result.redirects > 3:
            self.collector.add(
                "LIVE.REDIRECT_OVERFLOW",
                site_id,
                "high",
                "Preferred origin exceeded the three-redirect cap",
                {"url": preferred_origin, "redirects": result.redirects},
                publication_variant=publication_variant,
                route=preferred_origin,
            )
        if result.status != 200 or normalized_origin(result.final_url) != normalized_origin(preferred_origin):
            self.collector.add(
                "LIVE.PREFERRED_RESPONSE",
                site_id,
                "high",
                "Preferred origin must end on itself with HTTP 200",
                {
                    "requested": preferred_origin,
                    "final_url": result.final_url,
                    "status": result.status,
                },
                publication_variant=publication_variant,
                route=preferred_origin,
            )
        if "html" not in result.content_type:
            self.collector.add(
                "LIVE.CONTENT_TYPE",
                site_id,
                "high",
                "Preferred page does not return an HTML content type",
                {"content_type": result.content_type},
                publication_variant=publication_variant,
                route=preferred_origin,
            )
            return
        parser = PageParser()
        parser.feed(result.body.decode("utf-8", errors="replace"))
        if len(parser.canonicals) != 1 or normalized_origin(parser.canonicals[0]) != normalized_origin(preferred_origin):
            self.collector.add(
                "LIVE.CANONICAL_MISMATCH",
                site_id,
                "high",
                "Live preferred page canonical does not agree with its preferred origin",
                {"canonical": parser.canonicals, "preferred_origin": preferred_origin},
                publication_variant=publication_variant,
                route=preferred_origin,
            )
        if any("noindex" in value for value in parser.robots):
            self.collector.add(
                "LIVE.NOINDEX",
                site_id,
                "high",
                "Live preferred page is unexpectedly noindex",
                {"robots": parser.robots},
                publication_variant=publication_variant,
                route=preferred_origin,
            )

    def _validate_live_discovery(
        self,
        site_id: str,
        url: str,
        expected_kind: str,
        allowed_origins: set[str],
        publication_variant: str | None,
        depth: int = 0,
    ) -> None:
        try:
            result = self._safe_fetch(url, allowed_origins, "PortfolioValidator/1.0")
        except RequestBoundaryError as exc:
            self._live_boundary_finding(site_id, url, exc, publication_variant)
            return
        except RedirectOverflow as exc:
            self.collector.add(
                "LIVE.REDIRECT_OVERFLOW",
                site_id,
                "high",
                "Discovery URL exceeded the three-redirect cap",
                {"url": url, "error": str(exc)},
                publication_variant=publication_variant,
                route=url,
            )
            return
        except (OSError, urllib.error.URLError) as exc:
            self.collector.add(
                "LIVE.REQUEST_FAILED",
                site_id,
                "high",
                "Discovery URL request failed",
                {"url": url, "error": str(exc)},
                publication_variant=publication_variant,
                route=url,
            )
            return
        content_ok = (
            expected_kind == "text" and ("text" in result.content_type or "plain" in result.content_type)
        ) or (
            expected_kind == "xml" and ("xml" in result.content_type or result.content_type == "text/plain")
        )
        if result.status != 200 or result.redirects or not content_ok:
            self.collector.add(
                "LIVE.DISCOVERY_RESPONSE",
                site_id,
                "high",
                "Discovery file must return HTTP 200 directly with an appropriate content type",
                {
                    "url": url,
                    "status": result.status,
                    "redirects": result.redirects,
                    "content_type": result.content_type,
                },
                publication_variant=publication_variant,
                route=url,
            )
        if expected_kind == "xml" and result.status == 200:
            try:
                xml_root = ET.fromstring(result.body)
            except ET.ParseError as exc:
                self.collector.add(
                    "LIVE.SITEMAP_XML",
                    site_id,
                    "high",
                    "Live sitemap XML is invalid",
                    {"url": url, "error": str(exc)},
                    publication_variant=publication_variant,
                    route=url,
                )
                return
            sitemap_urls = [
                (node.text or "").strip()
                for node in xml_root.iter()
                if node.tag.rsplit("}", 1)[-1] == "loc" and (node.text or "").strip()
            ]
            sitemap_kind = xml_root.tag.rsplit("}", 1)[-1]
            expected_origin = normalized_origin(url)
            for page_url in sitemap_urls:
                if normalized_origin(page_url) != expected_origin:
                    self.collector.add(
                        "LIVE.SITEMAP_ORIGIN",
                        site_id,
                        "high",
                        "Live sitemap contains a URL outside its publication origin",
                        {"sitemap": url, "url": page_url, "expected_origin": expected_origin},
                        publication_variant=publication_variant,
                        route=page_url,
                    )
                    continue
                if normalized_origin(page_url) not in allowed_origins:
                    self._live_boundary_finding(
                        site_id,
                        page_url,
                        RequestBoundaryError("sitemap URL is outside manifest origins"),
                        publication_variant,
                    )
                    continue
                if sitemap_kind == "sitemapindex":
                    if depth >= 3:
                        self.collector.add(
                            "LIVE.SITEMAP_DEPTH",
                            site_id,
                            "high",
                            "Live sitemap index nesting exceeds the validation cap",
                            {"sitemap": url, "child": page_url},
                            publication_variant=publication_variant,
                            route=page_url,
                        )
                    else:
                        self._validate_live_discovery(
                            site_id,
                            page_url,
                            "xml",
                            allowed_origins,
                            publication_variant,
                            depth + 1,
                        )
                else:
                    self._validate_live_sitemap_page(
                        site_id,
                        page_url,
                        allowed_origins,
                        publication_variant,
                    )

    def _validate_live_sitemap_page(
        self,
        site_id: str,
        page_url: str,
        allowed_origins: set[str],
        publication_variant: str | None,
    ) -> None:
        try:
            result = self._safe_fetch(page_url, allowed_origins, "PortfolioValidator/1.0")
        except RequestBoundaryError as exc:
            self._live_boundary_finding(site_id, page_url, exc, publication_variant)
            return
        except RedirectOverflow as exc:
            self.collector.add(
                "LIVE.REDIRECT_OVERFLOW",
                site_id,
                "high",
                "Sitemap page exceeded the three-redirect cap",
                {"url": page_url, "error": str(exc)},
                publication_variant=publication_variant,
                route=page_url,
            )
            return
        except (OSError, urllib.error.URLError) as exc:
            self.collector.add(
                "LIVE.REQUEST_FAILED",
                site_id,
                "high",
                "Sitemap page request failed",
                {"url": page_url, "error": str(exc)},
                publication_variant=publication_variant,
                route=page_url,
            )
            return
        if result.status != 200 or result.redirects or "html" not in result.content_type:
            self.collector.add(
                "LIVE.SITEMAP_PAGE_RESPONSE",
                site_id,
                "high",
                "Sitemap page must return HTML with HTTP 200 and no redirect",
                {
                    "url": page_url,
                    "status": result.status,
                    "redirects": result.redirects,
                    "content_type": result.content_type,
                },
                publication_variant=publication_variant,
                route=page_url,
            )
            return
        parser = PageParser()
        parser.feed(result.body.decode("utf-8", errors="replace"))
        if len(parser.canonicals) != 1 or normalized_url(parser.canonicals[0]) != normalized_url(page_url):
            self.collector.add(
                "LIVE.SITEMAP_PAGE_CANONICAL",
                site_id,
                "high",
                "Sitemap page canonical does not equal the sitemap URL",
                {"url": page_url, "canonical": parser.canonicals},
                publication_variant=publication_variant,
                route=page_url,
            )
        if any("noindex" in value for value in parser.robots):
            self.collector.add(
                "LIVE.SITEMAP_PAGE_NOINDEX",
                site_id,
                "high",
                "Sitemap contains a noindex page",
                {"url": page_url, "robots": parser.robots},
                publication_variant=publication_variant,
                route=page_url,
            )

    def _live_boundary_finding(
        self,
        site_id: str,
        url: str,
        error: Exception,
        publication_variant: str | None,
    ) -> None:
        self.collector.add(
            "LIVE.REQUEST_BOUNDARY",
            site_id,
            "high",
            "Live validator refused a URL outside manifest-approved origins before opening it",
            {"url": url, "error": str(error)},
            publication_variant=publication_variant,
            route=url,
        )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Validate the Buhane portfolio registry and discovery surfaces."
    )
    parser.add_argument("--manifest", required=True, help="Path to the private portfolio JSON manifest")
    parser.add_argument(
        "--mode",
        required=True,
        choices=("registry", "source", "live"),
        help="Validation mode",
    )
    parser.add_argument("--site", action="append", default=[], help="Property ID to validate; repeatable")
    parser.add_argument("--timeout", type=float, default=20.0, help="Per-command/request timeout in seconds")
    parser.add_argument("--report", help="Exact path for the machine-readable JSON report")
    parser.add_argument(
        "--allow-pending",
        action="store_true",
        help="Skip only manifest-declared missing-route/discovery rules for incremental work",
    )
    return parser


def render_human_report(report: Mapping[str, Any]) -> None:
    findings = report.get("findings") or []
    if not findings:
        print(f"PASS [{report.get('mode')}] no findings")
    for finding in findings:
        variant = (
            f"/{finding['publication_variant']}" if finding.get("publication_variant") else ""
        )
        print(
            f"{str(finding['severity']).upper()} {finding['rule_id']} "
            f"{finding['property_id']}{variant} {finding['finding_id']}: {finding['message']}"
        )
    for site_id, rules in sorted((report.get("skipped_pending_rules") or {}).items()):
        print(f"SKIP PENDING {site_id}: {', '.join(rules)}")
    counts = report.get("severity_counts") or {}
    print(
        "SUMMARY "
        + " ".join(f"{severity}={counts.get(severity, 0)}" for severity in SEVERITIES)
        + f" exit_status={report.get('exit_status', 1)}"
    )


def run(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    manifest_path = Path(args.manifest).expanduser().resolve()
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        print(f"ERROR MANIFEST.READ: {exc}", file=sys.stderr)
        return 2
    if not isinstance(manifest, dict):
        print("ERROR MANIFEST.TYPE: root must be a JSON object", file=sys.stderr)
        return 2
    validator = PortfolioValidator(
        manifest,
        manifest_path,
        args.mode,
        selected_sites=args.site or None,
        timeout=max(0.1, args.timeout),
        allow_pending=args.allow_pending,
    )
    report = validator.validate()
    render_human_report(report)
    if args.report:
        report_path = Path(args.report).expanduser().resolve()
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return int(report["exit_status"])


def main() -> None:
    raise SystemExit(run())


if __name__ == "__main__":
    main()
