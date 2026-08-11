from __future__ import annotations

import copy
import email.message
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch
import urllib.error

from scripts.validate_portfolio import (
    APPROVED_COMMAND_CONTRACTS,
    APPROVED_SOURCE_ROOTS,
    FetchResult,
    PortfolioValidator,
    RequestBoundaryError,
    build_parser,
    is_https_origin,
    normalized_origin,
    normalized_url,
    run,
)


ORGANIZATION_ID = "https://buhane.com.tr/#organization"


class PortfolioValidatorTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.repo_root = Path(__file__).resolve().parents[2]
        cls.manifest_path = cls.repo_root / ".planning" / "portfolio-sites.json"
        cls.base_manifest = json.loads(cls.manifest_path.read_text(encoding="utf-8"))

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.root = Path(self.temp_dir.name)

    def manifest(self) -> dict:
        return copy.deepcopy(self.base_manifest)

    def configure_site(
        self,
        manifest: dict,
        site_id: str = "moodjot",
        *,
        canonical_routes: list[str] | None = None,
    ) -> dict:
        record = manifest["products"][site_id]
        record["source_root"] = str(self.root)
        record["public_root"] = str(self.root)
        record["validation_commands"] = []
        record["dirty_path_exclusions"] = []
        record["pending_source_rules"] = []
        record["canonical_routes"] = canonical_routes or ["/", "/guide/"]
        return record

    @staticmethod
    def product_schema(record: dict, product_id: str | None = None) -> dict:
        return {
            "@context": "https://schema.org",
            "@type": record["schema_type"],
            "@id": product_id or record["product_entity_id"],
            "name": record["display_name"],
            "url": record["preferred_origin"],
            "publisher": {"@id": ORGANIZATION_ID},
        }

    @staticmethod
    def editorial_schema(record: dict, product_id: str | None = None) -> dict:
        return {
            "@context": "https://schema.org",
            "@type": "Article",
            "@id": f"{record['preferred_origin']}guide/#article",
            "headline": f"{record['display_name']} Guide",
            "about": {"@id": product_id or record["product_entity_id"]},
            "publisher": {"@id": ORGANIZATION_ID},
        }

    @staticmethod
    def html_page(
        *,
        title: str,
        description: str,
        canonical: str,
        schema: dict | str,
        body: str,
        alternates: dict[str, str] | None = None,
        extra_head: str = "",
    ) -> str:
        schema_text = schema if isinstance(schema, str) else json.dumps(schema)
        alternate_markup = "".join(
            f'<link rel="alternate" hreflang="{locale}" href="{href}">'
            for locale, href in (alternates or {}).items()
        )
        return f"""<!doctype html>
<html lang="en"><head>
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
{alternate_markup}
<meta property="og:url" content="{canonical}">
<script type="application/ld+json">{schema_text}</script>
{extra_head}
</head><body><h1>{title}</h1>{body}</body></html>
"""

    def write_passing_site(self, record: dict, root: Path | None = None) -> None:
        root = root or self.root
        root.mkdir(parents=True, exist_ok=True)
        origin = record["preferred_origin"]
        (root / "guide").mkdir(parents=True, exist_ok=True)
        (root / "index.html").write_text(
            self.html_page(
                title=f"{record['display_name']} Home",
                description=f"Official {record['display_name']} product overview and getting started information.",
                canonical=origin,
                schema=self.product_schema(record),
                body=(
                    '<p>Use the current released product for its documented purpose.</p>'
                    '<a href="/guide/">Read the guide</a>'
                    '<a href="https://buhane.com.tr/">A product by Buhane Information Technologies</a>'
                ),
            ),
            encoding="utf-8",
        )
        (root / "guide" / "index.html").write_text(
            self.html_page(
                title=f"{record['display_name']} Guide",
                description=f"A factual guide to using {record['display_name']} in its current release.",
                canonical=f"{origin}guide/",
                schema=self.editorial_schema(record),
                body='<p>Follow the documented workflow.</p><a href="/">Product overview</a>',
            ),
            encoding="utf-8",
        )
        sitemap_name = Path(record["sitemap_url"].split("/", 3)[-1]).name
        (root / sitemap_name).write_text(
            """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>{origin}</loc></url>
  <url><loc>{origin}guide/</loc></url>
</urlset>
""".format(origin=origin),
            encoding="utf-8",
        )
        robots_name = Path(record["robots_url"].split("/", 3)[-1]).name
        (root / robots_name).write_text(
            f"User-agent: *\nAllow: /\n\nSitemap: {record['sitemap_url']}\n",
            encoding="utf-8",
        )

    def write_route_locale_scope_site(self, record: dict) -> None:
        origin = record["preferred_origin"]
        alternates = {
            "en": f"{origin}en/",
            "tr": f"{origin}tr/",
            "x-default": f"{origin}en/",
        }
        pages = {
            "en": self.html_page(
                title="Lastimo English Home",
                description="The English Lastimo overview for six preset elapsed-time reminders.",
                canonical=f"{origin}en/",
                schema=self.product_schema(record),
                body='<p>Use six released presets.</p><a href="https://buhane.com.tr/">A product by Buhane</a>',
                alternates=alternates,
            ),
            "tr": self.html_page(
                title="Lastimo Turkish Home",
                description="Lastimo altı hazır alan için sakin geçen süre yanıtları sunar.",
                canonical=f"{origin}tr/",
                schema=self.product_schema(record),
                body='<p>Altı hazır alanı kullanın.</p><a href="https://buhane.com.tr/tr/">Buhane ürünü</a>',
                alternates=alternates,
            ),
            "en/blog": self.html_page(
                title="Lastimo English Blog",
                description="English-only Lastimo guidance for the current released workflow.",
                canonical=f"{origin}en/blog/",
                schema=self.editorial_schema(record),
                body='<p>Follow the current released workflow.</p><a href="https://buhane.com.tr/">A product by Buhane</a>',
            ),
        }
        for route, markup in pages.items():
            output = self.root / route / "index.html"
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(markup, encoding="utf-8")
        (self.root / "sitemap.xml").write_text(
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
            f'<url><loc>{origin}en/</loc></url>'
            f'<url><loc>{origin}tr/</loc></url>'
            f'<url><loc>{origin}en/blog/</loc></url>'
            "</urlset>",
            encoding="utf-8",
        )
        (self.root / "robots.txt").write_text(
            f"User-agent: *\nAllow: /\nSitemap: {record['sitemap_url']}\n",
            encoding="utf-8",
        )

    def write_astral_locale_scope_site(self, record: dict) -> None:
        origin = record["preferred_origin"]
        alternates = {
            "en": f"{origin}glossary/",
            "tr": f"{origin}sozluk/",
            "x-default": f"{origin}glossary/",
        }
        pages = {
            "": self.html_page(
                title="Astral Post Home",
                description="Astral Post offers a personal message ritual and symbolic reflections.",
                canonical=origin,
                schema=self.product_schema(record),
                body='<p>Use the released reflection workflow.</p><a href="https://buhane.com.tr/">A product by Buhane</a>',
            ),
            "glossary": self.html_page(
                title="Astral Post Glossary",
                description="English definitions for the Astral Post reflection experience.",
                canonical=f"{origin}glossary/",
                schema=self.editorial_schema(record),
                body='<p>Read the English definitions.</p><a href="https://buhane.com.tr/">A product by Buhane</a>',
                alternates=alternates,
            ),
            "sozluk": self.html_page(
                title="Astral Post Sözlük",
                description="Astral Post düşünme deneyimi için Türkçe tanımlar.",
                canonical=f"{origin}sozluk/",
                schema=self.editorial_schema(record),
                body='<p>Türkçe tanımları okuyun.</p><a href="https://buhane.com.tr/tr/">Buhane ürünü</a>',
                alternates=alternates,
            ),
        }
        for route, markup in pages.items():
            output = self.root / route / "index.html" if route else self.root / "index.html"
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(markup, encoding="utf-8")
        (self.root / "sitemap.xml").write_text(
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
            f"<url><loc>{origin}</loc></url>"
            f"<url><loc>{origin}glossary/</loc></url>"
            f"<url><loc>{origin}sozluk/</loc></url>"
            "</urlset>",
            encoding="utf-8",
        )
        (self.root / "robots.txt").write_text(
            f"User-agent: *\nAllow: /\nSitemap: {record['sitemap_url']}\n",
            encoding="utf-8",
        )

    def validate(
        self,
        manifest: dict,
        mode: str = "source",
        site: str = "moodjot",
        *,
        allow_pending: bool = False,
        fetcher=None,
        resolver=None,
    ) -> dict:
        if fetcher is not None and resolver is None:
            resolver = lambda _hostname, _port: ("93.184.216.34",)
        return PortfolioValidator(
            manifest,
            self.manifest_path,
            mode,
            selected_sites=[site],
            timeout=1,
            allow_pending=allow_pending,
            fetcher=fetcher,
            resolver=resolver,
        ).validate()

    @staticmethod
    def rules(report: dict) -> set[str]:
        return {finding["rule_id"] for finding in report["findings"]}

    def test_help_lists_all_cli_options(self) -> None:
        help_text = build_parser().format_help()
        for option in (
            "--help",
            "--manifest",
            "--mode",
            "--site",
            "--timeout",
            "--report",
            "--allow-pending",
        ):
            self.assertIn(option, help_text)

    def test_registry_manifest_passes_and_report_path_is_exact(self) -> None:
        report_path = self.root / "chosen" / "registry.json"
        stdout = io.StringIO()
        with redirect_stdout(stdout):
            exit_code = run(
                [
                    "--manifest",
                    str(self.manifest_path),
                    "--mode",
                    "registry",
                    "--report",
                    str(report_path),
                ]
            )
        self.assertEqual(0, exit_code, stdout.getvalue())
        self.assertTrue(report_path.is_file())
        report = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertEqual(0, report["exit_status"])
        self.assertEqual({}, report["skipped_pending_rules"])

    def test_registry_high_finding_exits_nonzero(self) -> None:
        manifest = self.manifest()
        manifest["products"]["vynix"]["preferred_origin"] = "http://vynix.app/"
        report = self.validate(manifest, mode="registry")
        self.assertEqual(1, report["exit_status"])
        self.assertIn("REG.PREFERRED_HTTPS", self.rules(report))

    def test_url_normalization_is_total_and_rejects_unsafe_authorities(self) -> None:
        invalid_urls = (
            "https://example.com:not-a-port/",
            "https://example.com:70000/",
            "https://example.com:/",
            "https://[2001:db8::1/",
            "https://user@example.com/",
            "https://user:secret@example.com/",
        )
        for url in invalid_urls:
            with self.subTest(url=url):
                self.assertEqual("", normalized_origin(url))
                self.assertEqual("", normalized_url(url))
                self.assertFalse(is_https_origin(url))

    def test_url_normalization_preserves_valid_ipv6_authority(self) -> None:
        url = "https://[2606:4700:4700::1111]/path?q=1#fragment"
        self.assertEqual("https://[2606:4700:4700::1111]", normalized_origin(url))
        self.assertEqual(
            "https://[2606:4700:4700::1111]/path?q=1",
            normalized_url(url),
        )

    def test_registry_rejects_legacy_and_malformed_command_specs(self) -> None:
        invalid_commands = (
            "cd www && node scripts/build-seo-content.mjs --check",
            {"argv": "node", "cwd": "www"},
            {"argv": [], "cwd": "www"},
            {"argv": ["node", "scripts/build-seo-content.mjs", "--check"], "cwd": "www", "shell": True},
        )
        for command in invalid_commands:
            with self.subTest(command=command):
                manifest = self.manifest()
                manifest["products"]["vynix"]["validation_commands"] = [command]
                report = self.validate(manifest, mode="registry", site="vynix")
                self.assertIn("REG.COMMAND_SPEC", self.rules(report))
                self.assertEqual(1, report["exit_status"])

    def test_registry_rejects_command_metacharacters_and_path_escape(self) -> None:
        invalid_commands = (
            {
                "argv": ["node", "scripts/build-seo-content.mjs;touch", "--check"],
                "cwd": "www",
            },
            {
                "argv": ["node", "scripts/build-seo-content.mjs", "--check"],
                "cwd": "../Vynix",
            },
        )
        for command in invalid_commands:
            with self.subTest(command=command):
                manifest = self.manifest()
                manifest["products"]["vynix"]["validation_commands"] = [command]
                report = self.validate(manifest, mode="registry", site="vynix")
                self.assertIn("REG.COMMAND_SPEC", self.rules(report))
                self.assertEqual(1, report["exit_status"])

    def test_source_rejects_unapproved_command_without_spawning_process(self) -> None:
        manifest = self.manifest()
        record = self.configure_site(manifest, "vynix")
        self.write_passing_site(record)
        record["validation_commands"] = [
            {"argv": ["node", "-e", "process.exit(0)"], "cwd": "."}
        ]
        with patch("scripts.validate_portfolio.subprocess.Popen") as popen_mock:
            report = self.validate(manifest, site="vynix")

        self.assertIn("GEN.COMMAND_REJECTED", self.rules(report))
        popen_mock.assert_not_called()
        self.assertEqual(1, report["exit_status"])

    def test_native_command_timeout_emits_report_and_nonzero_exit(self) -> None:
        manifest = self.manifest()
        record = self.configure_site(manifest)
        self.write_passing_site(record)
        command = {"argv": ["sleep", "5"], "cwd": "."}
        record["validation_commands"] = [command]
        manifest_path = self.root / "manifest.json"
        report_path = self.root / "timeout-report.json"
        manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

        with (
            patch.dict(APPROVED_SOURCE_ROOTS, {"moodjot": self.root}),
            patch.dict(
                APPROVED_COMMAND_CONTRACTS,
                {"moodjot": {(".", ("sleep", "5"))}},
            ),
        ):
            exit_code = run(
                [
                    "--manifest",
                    str(manifest_path),
                    "--mode",
                    "source",
                    "--site",
                    "moodjot",
                    "--timeout",
                    "0.1",
                    "--report",
                    str(report_path),
                ]
            )

        self.assertEqual(1, exit_code)
        report = json.loads(report_path.read_text(encoding="utf-8"))
        self.assertIn("GEN.COMMAND_TIMEOUT", self.rules(report))
        timeout_finding = next(
            finding for finding in report["findings"] if finding["rule_id"] == "GEN.COMMAND_TIMEOUT"
        )
        self.assertEqual(0.1, timeout_finding["evidence"]["timeout_seconds"])

    def test_passing_static_site_reuses_one_product_identity(self) -> None:
        manifest = self.manifest()
        record = self.configure_site(manifest)
        self.write_passing_site(record)
        report = self.validate(manifest)
        self.assertEqual(0, report["exit_status"], report["findings"])
        self.assertEqual(record["product_entity_id"], report["sites"]["moodjot"]["product_entity_id"])

    def test_buhane_source_contract_derives_all_product_detail_pairs(self) -> None:
        manifest = self.manifest()
        validator = PortfolioValidator(
            manifest,
            self.manifest_path,
            "source",
            selected_sites=["buhane"],
            timeout=1,
        )
        contract = validator._source_contract("buhane", manifest["properties"]["buhane"])

        self.assertEqual(26, len(contract["canonical_routes"]))
        self.assertEqual("https://buhane.com.tr/robots.txt", contract["robots_url"])
        self.assertEqual("https://buhane.com.tr/sitemap.xml", contract["sitemap_url"])
        self.assertEqual(22, len(contract["product_detail_routes"]))
        self.assertEqual(
            set(record["product_entity_id"] for record in manifest["products"].values()),
            set(contract["product_detail_routes"].values()),
        )
        self.assertEqual(
            list(manifest["products"]),
            contract["approved_contextual_links"],
        )

    def test_ahmet_selected_work_rejects_unapproved_seventh_product(self) -> None:
        manifest = self.manifest()
        manifest["properties"]["ahmet-sh"]["approved_contextual_links"].append("astral-post")

        report = self.validate(manifest, mode="registry", site="ahmet-sh")

        self.assertIn("REG.PROPERTY_CONTEXTUAL_LINK_CONTRACT", self.rules(report))
        self.assertEqual(1, report["exit_status"])

    def test_unexpected_property_is_reported_without_contract_lookup_failure(self) -> None:
        manifest = self.manifest()
        manifest["properties"]["unexpected"] = copy.deepcopy(manifest["properties"]["ahmet-sh"])

        report = self.validate(manifest, mode="registry", site="ahmet-sh")

        self.assertIn("REG.PROPERTY_SET", self.rules(report))
        self.assertEqual(1, report["exit_status"])

    def test_gridzle_registry_rejects_stale_html_route_shapes(self) -> None:
        manifest = self.manifest()
        record = manifest["products"]["gridzle"]
        record["canonical_routes"] = [
            "/",
            "/support.html",
            "/privacy.html",
            "/terms.html",
            "/guides/how-to-play/",
        ]
        record["support_url"] = "https://gridzle.app/support.html"

        report = self.validate(manifest, mode="registry", site="gridzle")

        self.assertIn("REG.PRODUCT_PUBLIC_ROUTE_CONTRACT", self.rules(report))
        self.assertEqual(1, report["exit_status"])

    def test_u2m_registry_rejects_source_tree_as_public_output(self) -> None:
        manifest = self.manifest()
        record = manifest["products"]["u2m"]
        record["public_root"] = str(Path(record["source_root"]) / "frontend")

        report = self.validate(manifest, mode="registry", site="u2m")

        self.assertIn("REG.PRODUCT_PUBLIC_ROUTE_CONTRACT", self.rules(report))
        self.assertEqual(1, report["exit_status"])

    def test_u2m_registry_rejects_legacy_aliases_as_canonical_routes(self) -> None:
        for legacy_route in ("/api-docs", "/privacy"):
            with self.subTest(legacy_route=legacy_route):
                manifest = self.manifest()
                manifest["products"]["u2m"]["canonical_routes"].append(legacy_route)

                report = self.validate(manifest, mode="registry", site="u2m")

                self.assertIn("REG.PRODUCT_PUBLIC_ROUTE_CONTRACT", self.rules(report))
                self.assertEqual(1, report["exit_status"])

    def test_u2m_registry_declares_www_as_legacy_origin_only(self) -> None:
        manifest = self.manifest()
        record = manifest["products"]["u2m"]
        self.assertEqual(["https://www.u2m.io/"], record["legacy_origins"])
        self.assertEqual("https://u2m.io/", record["preferred_origin"])
        report = self.validate(manifest, mode="registry", site="u2m")
        self.assertEqual(0, report["exit_status"], report["findings"])

    def test_u2m_registry_rejects_private_or_noindex_canonical_routes(self) -> None:
        forbidden_routes = (
            "/login",
            "/register",
            "/forgot-password",
            "/reset-password",
            "/dashboard",
            "/dashboard/stats-token",
            "/app/dashboard",
            "/profile",
            "/stats",
            "/tokens",
            "/frontend/",
            "/frontend/profile",
        )
        for forbidden_route in forbidden_routes:
            with self.subTest(forbidden_route=forbidden_route):
                manifest = self.manifest()
                manifest["products"]["u2m"]["canonical_routes"].append(forbidden_route)

                report = self.validate(manifest, mode="registry", site="u2m")

                self.assertIn("REG.PRODUCT_PUBLIC_ROUTE_CONTRACT", self.rules(report))
                self.assertEqual(1, report["exit_status"])

    def test_legacy_canonical_has_stable_rule_and_high_exit(self) -> None:
        manifest = self.manifest()
        record = self.configure_site(manifest)
        self.write_passing_site(record)
        home = (self.root / "index.html").read_text(encoding="utf-8")
        home = home.replace("https://moodjot.app/", "https://moodjot.com/", 2)
        (self.root / "index.html").write_text(home, encoding="utf-8")
        report = self.validate(manifest)
        self.assertIn("CANON.LEGACY_ORIGIN", self.rules(report))
        self.assertEqual(1, report["exit_status"])

    def test_invalid_json_ld_has_stable_schema_rule(self) -> None:
        manifest = self.manifest()
        record = self.configure_site(manifest)
        self.write_passing_site(record)
        home = (self.root / "index.html").read_text(encoding="utf-8")
        start = home.index('<script type="application/ld+json">')
        end = home.index("</script>", start)
        home = home[:start] + '<script type="application/ld+json">{"bad":</script>' + home[end + 9 :]
        (self.root / "index.html").write_text(home, encoding="utf-8")
        report = self.validate(manifest)
        self.assertIn("SCHEMA.INVALID_JSON", self.rules(report))

    def test_sitemap_auth_leakage_is_fatal(self) -> None:
        manifest = self.manifest()
        record = self.configure_site(manifest)
        self.write_passing_site(record)
        sitemap = self.root / "sitemap.xml"
        text = sitemap.read_text(encoding="utf-8").replace(
            "</urlset>", "<url><loc>https://moodjot.app/login/</loc></url></urlset>"
        )
        sitemap.write_text(text, encoding="utf-8")
        report = self.validate(manifest)
        self.assertIn("SITEMAP.PRIVATE_ROUTE", self.rules(report))
        self.assertEqual(1, report["exit_status"])

    def test_sitemap_route_outside_declared_canonical_contract_is_fatal(self) -> None:
        manifest = self.manifest()
        record = self.configure_site(manifest)
        self.write_passing_site(record)
        (self.root / "stats").mkdir()
        (self.root / "stats" / "index.html").write_text(
            self.html_page(
                title="MoodJot Operational Statistics",
                description="Operational statistics that are intentionally outside the public discovery contract.",
                canonical="https://moodjot.app/stats/",
                schema=self.editorial_schema(record),
                body='<p>Operational data.</p><a href="/">Product overview</a>',
            ),
            encoding="utf-8",
        )
        sitemap = self.root / "sitemap.xml"
        sitemap.write_text(
            sitemap.read_text(encoding="utf-8").replace(
                "</urlset>",
                "<url><loc>https://moodjot.app/stats/</loc></url></urlset>",
            ),
            encoding="utf-8",
        )

        report = self.validate(manifest)

        self.assertIn("SITEMAP.UNDECLARED_ROUTE", self.rules(report))
        self.assertEqual(1, report["exit_status"])

    def test_incomplete_hreflang_is_fatal(self) -> None:
        manifest = self.manifest()
        record = self.configure_site(manifest)
        record["indexable_locales"] = ["en", "tr"]
        self.write_passing_site(record)
        home = (self.root / "index.html").read_text(encoding="utf-8").replace(
            '<meta property="og:url"',
            '<link rel="alternate" hreflang="en" href="https://moodjot.app/">\n<meta property="og:url"',
        )
        (self.root / "index.html").write_text(home, encoding="utf-8")
        report = self.validate(manifest)
        self.assertIn("LOCALE.HREFLANG_INCOMPLETE", self.rules(report))

    def test_route_locale_scope_allows_english_only_editorial_pages(self) -> None:
        manifest = self.manifest()
        record = self.configure_site(
            manifest,
            "lastimo",
            canonical_routes=["/en/", "/tr/", "/en/blog/"],
        )
        record["indexable_locales"] = ["en", "tr"]
        record["route_locale_scopes"] = [
            {"routes": ["/en/blog/"], "indexable_locales": ["en"]}
        ]
        self.write_route_locale_scope_site(record)

        report = self.validate(manifest, site="lastimo")

        self.assertEqual(0, report["exit_status"], report["findings"])

    def test_route_locale_scope_rejects_fabricated_editorial_alternate(self) -> None:
        manifest = self.manifest()
        record = self.configure_site(
            manifest,
            "lastimo",
            canonical_routes=["/en/", "/tr/", "/en/blog/"],
        )
        record["indexable_locales"] = ["en", "tr"]
        record["route_locale_scopes"] = [
            {"routes": ["/en/blog/"], "indexable_locales": ["en"]}
        ]
        self.write_route_locale_scope_site(record)
        blog = self.root / "en" / "blog" / "index.html"
        blog.write_text(
            blog.read_text(encoding="utf-8").replace(
                '<meta property="og:url"',
                '<link rel="alternate" hreflang="tr" href="https://lastimo.app/tr/blog/">'
                '<meta property="og:url"',
            ),
            encoding="utf-8",
        )

        report = self.validate(manifest, site="lastimo")

        self.assertIn("LOCALE.NONADDRESSABLE_HREFLANG", self.rules(report))
        self.assertEqual(1, report["exit_status"])

    def test_route_locale_scope_does_not_weaken_translated_routes(self) -> None:
        manifest = self.manifest()
        record = self.configure_site(
            manifest,
            "lastimo",
            canonical_routes=["/en/", "/tr/", "/en/blog/"],
        )
        record["indexable_locales"] = ["en", "tr"]
        record["route_locale_scopes"] = [
            {"routes": ["/en/blog/"], "indexable_locales": ["en"]}
        ]
        self.write_route_locale_scope_site(record)
        english_home = self.root / "en" / "index.html"
        english_home.write_text(
            english_home.read_text(encoding="utf-8").replace(
                '<link rel="alternate" hreflang="tr" href="https://lastimo.app/tr/">',
                "",
            ),
            encoding="utf-8",
        )

        report = self.validate(manifest, site="lastimo")

        self.assertIn("LOCALE.HREFLANG_INCOMPLETE", self.rules(report))
        self.assertEqual(1, report["exit_status"])

    def test_route_locale_scope_registry_rejects_overlap_and_unknown_locale(self) -> None:
        manifest = self.manifest()
        manifest["products"]["lastimo"]["route_locale_scopes"] = [
            {"routes": ["/en/blog/"], "indexable_locales": ["en"]},
            {"routes": ["/en/blog/"], "indexable_locales": ["xx"]},
        ]

        report = self.validate(manifest, mode="registry", site="lastimo")

        self.assertIn("REG.ROUTE_LOCALE_SCOPE", self.rules(report))
        self.assertEqual(1, report["exit_status"])

    def test_astral_route_scope_keeps_only_glossary_pair_addressable(self) -> None:
        manifest = self.manifest()
        record = self.configure_site(
            manifest,
            "astral-post",
            canonical_routes=["/", "/glossary/", "/sozluk/"],
        )
        record["route_locale_scopes"] = [
            {"routes": ["/"], "indexable_locales": ["en"]}
        ]
        self.write_astral_locale_scope_site(record)

        report = self.validate(manifest, site="astral-post")

        self.assertEqual(0, report["exit_status"], report["findings"])

    def test_astral_glossary_pair_still_requires_reciprocal_alternates(self) -> None:
        manifest = self.manifest()
        record = self.configure_site(
            manifest,
            "astral-post",
            canonical_routes=["/", "/glossary/", "/sozluk/"],
        )
        record["route_locale_scopes"] = [
            {"routes": ["/"], "indexable_locales": ["en"]}
        ]
        self.write_astral_locale_scope_site(record)
        glossary = self.root / "glossary" / "index.html"
        glossary.write_text(
            glossary.read_text(encoding="utf-8").replace(
                '<link rel="alternate" hreflang="tr" href="https://astralpost.app/sozluk/">',
                "",
            ),
            encoding="utf-8",
        )

        report = self.validate(manifest, site="astral-post")

        self.assertIn("LOCALE.HREFLANG_INCOMPLETE", self.rules(report))
        self.assertIn("LOCALE.HREFLANG_RECIPROCAL", self.rules(report))
        self.assertEqual(1, report["exit_status"])

    def test_unapproved_sibling_footer_link_is_fatal(self) -> None:
        manifest = self.manifest()
        record = self.configure_site(manifest)
        record["approved_contextual_links"] = []
        self.write_passing_site(record)
        home = (self.root / "index.html").read_text(encoding="utf-8").replace(
            "</body>", '<footer><a href="https://vynix.app/">Try Vynix</a></footer></body>'
        )
        (self.root / "index.html").write_text(home, encoding="utf-8")
        report = self.validate(manifest)
        self.assertIn("LINK.SIBLING_NOT_ALLOWED", self.rules(report))

    def test_private_registry_exposure_is_fatal(self) -> None:
        manifest = self.manifest()
        record = self.configure_site(manifest)
        self.write_passing_site(record)
        home = (self.root / "index.html").read_text(encoding="utf-8").replace(
            "</body>", '<a href="/.planning/portfolio-sites.json">Registry</a></body>'
        )
        (self.root / "index.html").write_text(home, encoding="utf-8")
        report = self.validate(manifest)
        self.assertIn("SEC.PRIVATE_REGISTRY_EXPOSED", self.rules(report))

    def test_lastimo_excluded_claim_is_fatal(self) -> None:
        manifest = self.manifest()
        record = self.configure_site(manifest, "lastimo", canonical_routes=["/"])
        record["indexable_locales"] = ["en"]
        self.root.mkdir(parents=True, exist_ok=True)
        (self.root / "index.html").write_text(
            self.html_page(
                title="Lastimo Home",
                description="Remember the last time you completed one of six preset activities.",
                canonical="https://lastimo.app/",
                schema=self.product_schema(record),
                body=(
                    "<p>Review your history after each update.</p>"
                    '<a href="https://buhane.com.tr/">A product by Buhane</a>'
                ),
            ),
            encoding="utf-8",
        )
        (self.root / "sitemap.xml").write_text(
            '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://lastimo.app/</loc></url></urlset>',
            encoding="utf-8",
        )
        (self.root / "robots.txt").write_text(
            "User-agent: *\nAllow: /\nSitemap: https://lastimo.app/sitemap.xml\n",
            encoding="utf-8",
        )
        report = self.validate(manifest, site="lastimo")
        self.assertIn("CLAIM.EXCLUDED", self.rules(report))

    def test_home_product_id_mismatch_is_fatal(self) -> None:
        manifest = self.manifest()
        record = self.configure_site(manifest)
        self.write_passing_site(record)
        home = (self.root / "index.html").read_text(encoding="utf-8").replace(
            record["product_entity_id"], "https://moodjot.app/home/#product", 1
        )
        (self.root / "index.html").write_text(home, encoding="utf-8")
        report = self.validate(manifest)
        self.assertIn("ENTITY.PRODUCT_ID_MISMATCH", self.rules(report))

    def test_editorial_route_local_product_id_is_fatal(self) -> None:
        manifest = self.manifest()
        record = self.configure_site(manifest)
        self.write_passing_site(record)
        guide = (self.root / "guide" / "index.html").read_text(encoding="utf-8").replace(
            record["product_entity_id"], "https://moodjot.app/guide/#product", 1
        )
        (self.root / "guide" / "index.html").write_text(guide, encoding="utf-8")
        report = self.validate(manifest)
        self.assertIn("ENTITY.EDITORIAL_PRODUCT_REFERENCE", self.rules(report))

    def configure_hive(self, manifest: dict) -> dict:
        record = manifest["products"]["hive-due"]
        record["source_root"] = str(self.root)
        record["public_root"] = str(self.root)
        record["validation_commands"] = []
        command = {"argv": ["python3", "-c", "pass"], "cwd": "."}
        source_patch = patch.dict(APPROVED_SOURCE_ROOTS, {"hive-due": self.root})
        command_patch = patch.dict(
            APPROVED_COMMAND_CONTRACTS,
            {"hive-due": {(".", ("python3", "-c", "pass"))}},
        )
        source_patch.start()
        command_patch.start()
        self.addCleanup(source_patch.stop)
        self.addCleanup(command_patch.stop)
        for variant in record["publication_variants"]:
            variant["build_command"] = command
            variant["canonical_routes"] = [
                "/en/" if variant["id"] == "hivedue" else "/"
            ]
        return record

    def write_hive_variants(self, record: dict) -> None:
        alternates = {
            "tr": "https://sitehesap.com/",
            "en": "https://hivedue.com/en/",
            "x-default": "https://hivedue.com/en/",
        }
        for variant in record["publication_variants"]:
            variant_root = self.root / variant["output_root"]
            variant_root.mkdir(parents=True, exist_ok=True)
            (variant_root / "en").mkdir(parents=True, exist_ok=True)
            canonical_locale = variant["indexable_locales"][0]
            for locale, route, canonical in (
                ("tr", "/", "https://sitehesap.com/"),
                ("en", "/en/", "https://hivedue.com/en/"),
            ):
                indexable = locale == canonical_locale
                page_canonical = canonical
                if variant["id"] == "hivedue" and locale == "tr":
                    page_canonical = "https://hivedue.com/en/"
                markup = self.html_page(
                    title=f'{variant["id"]} {locale} Home',
                    description=f'{variant["id"]} {locale} regional product overview and workflow.',
                    canonical=page_canonical,
                    schema=self.product_schema(record),
                    body='<p>Use the released invoice workflow.</p><a href="https://buhane.com.tr/">A product by Buhane</a>',
                    alternates=alternates if indexable else None,
                    extra_head='' if indexable else '<meta name="robots" content="noindex,follow">',
                )
                output = variant_root / route.lstrip("/") / "index.html"
                if route == "/":
                    output = variant_root / "index.html"
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_text(markup, encoding="utf-8")
            canonical_url = (
                "https://hivedue.com/en/"
                if variant["id"] == "hivedue"
                else "https://sitehesap.com/"
            )
            (variant_root / "sitemap.xml").write_text(
                '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                f"<url><loc>{canonical_url}</loc></url></urlset>",
                encoding="utf-8",
            )
            (variant_root / "robots.txt").write_text(
                f"User-agent: *\nAllow: /\nSitemap: {variant['sitemap_url']}\n",
                encoding="utf-8",
            )

    def test_passing_two_host_hive_reuses_one_product_id(self) -> None:
        manifest = self.manifest()
        record = self.configure_hive(manifest)
        self.write_hive_variants(record)
        report = self.validate(manifest, site="hive-due")
        self.assertEqual(0, report["exit_status"], report["findings"])
        variants = report["sites"]["hive-due"]["publication_variants"]
        self.assertEqual({"hivedue", "sitehesap"}, set(variants))
        self.assertEqual(
            {"https://hivedue.com/#product"},
            {item["product_entity_id"] for item in variants.values()},
        )

    def test_hive_crossed_origin_robots_sitemap_and_product_id_fail(self) -> None:
        manifest = self.manifest()
        record = self.configure_hive(manifest)
        self.write_hive_variants(record)
        sitehesap = self.root / "dist" / "sitehesap"
        home = (sitehesap / "index.html").read_text(encoding="utf-8")
        home = home.replace("https://sitehesap.com/", "https://hivedue.com/", 2)
        home = home.replace(record["product_entity_id"], "https://sitehesap.com/#product", 1)
        (sitehesap / "index.html").write_text(home, encoding="utf-8")
        (sitehesap / "robots.txt").write_text(
            "User-agent: *\nAllow: /\nSitemap: https://hivedue.com/sitemap.xml\n",
            encoding="utf-8",
        )
        report = self.validate(manifest, site="hive-due")
        rules = self.rules(report)
        self.assertIn("CANON.PREFERRED_ORIGIN", rules)
        self.assertIn("ROBOTS.SITEMAP_MISMATCH", rules)
        self.assertIn("ENTITY.PRODUCT_ID_MISMATCH", rules)

    def test_incomplete_publication_variant_is_fatal(self) -> None:
        manifest = self.manifest()
        del manifest["products"]["hive-due"]["publication_variants"][1]["sitemap_url"]
        report = self.validate(manifest, mode="registry", site="hive-due")
        self.assertIn("REG.VARIANT_INCOMPLETE", self.rules(report))

    def test_cross_publication_hreflang_missing_peer_is_fatal(self) -> None:
        manifest = self.manifest()
        record = self.configure_hive(manifest)
        self.write_hive_variants(record)
        hivedue_home = self.root / "dist" / "hivedue" / "en" / "index.html"
        hivedue_home.write_text(
            hivedue_home.read_text(encoding="utf-8").replace(
                '<link rel="alternate" hreflang="tr" href="https://sitehesap.com/">',
                "",
            ),
            encoding="utf-8",
        )

        report = self.validate(manifest, site="hive-due")

        rules = self.rules(report)
        self.assertIn("LOCALE.CROSS_PUBLICATION_HREFLANG", rules)
        self.assertIn("LOCALE.CROSS_PUBLICATION_RECIPROCAL", rules)
        self.assertEqual(1, report["exit_status"])

    def test_cross_publication_noncanonical_copy_must_stay_noindex(self) -> None:
        manifest = self.manifest()
        record = self.configure_hive(manifest)
        self.write_hive_variants(record)
        sitehesap_english = self.root / "dist" / "sitehesap" / "en" / "index.html"
        sitehesap_english.write_text(
            sitehesap_english.read_text(encoding="utf-8").replace(
                '<meta name="robots" content="noindex,follow">',
                "",
            ),
            encoding="utf-8",
        )

        report = self.validate(manifest, site="hive-due")

        self.assertIn("LOCALE.CROSS_PUBLICATION_COPY_INDEXABLE", self.rules(report))
        self.assertEqual(1, report["exit_status"])

    def test_cross_publication_noncanonical_copy_requires_canonical_peer(self) -> None:
        manifest = self.manifest()
        record = self.configure_hive(manifest)
        self.write_hive_variants(record)
        sitehesap_english = self.root / "dist" / "sitehesap" / "en" / "index.html"
        sitehesap_english.write_text(
            sitehesap_english.read_text(encoding="utf-8").replace(
                '<link rel="canonical" href="https://hivedue.com/en/">',
                '<link rel="canonical" href="https://hivedue.com/missing/">',
            ),
            encoding="utf-8",
        )

        report = self.validate(manifest, site="hive-due")

        self.assertIn("LOCALE.CROSS_PUBLICATION_COPY_TARGET", self.rules(report))
        self.assertEqual(1, report["exit_status"])

    def test_cross_publication_registry_rejects_unknown_variant_and_default(self) -> None:
        manifest = self.manifest()
        contract = manifest["products"]["hive-due"]["cross_publication_hreflang"]
        contract["locale_variants"]["en"]["publication_variant"] = "missing"
        contract["x_default"] = "de"

        report = self.validate(manifest, mode="registry", site="hive-due")

        self.assertIn("REG.CROSS_PUBLICATION_HREFLANG", self.rules(report))
        self.assertEqual(1, report["exit_status"])

    def test_allow_pending_skips_only_declared_discovery_rules(self) -> None:
        manifest = self.manifest()
        record = self.configure_site(manifest)
        record["pending_source_rules"] = ["SRC.MISSING_SITEMAP"]
        self.write_passing_site(record)
        (self.root / "sitemap.xml").unlink()
        report = self.validate(manifest, allow_pending=True)
        self.assertEqual(0, report["exit_status"], report["findings"])
        self.assertEqual(["SRC.MISSING_SITEMAP"], report["skipped_pending_rules"]["moodjot"])

        home = (self.root / "index.html").read_text(encoding="utf-8").replace(
            json.dumps(self.product_schema(record)), '{"@context":'
        )
        (self.root / "index.html").write_text(home, encoding="utf-8")
        fatal_report = self.validate(manifest, allow_pending=True)
        self.assertIn("SCHEMA.INVALID_JSON", self.rules(fatal_report))
        self.assertEqual(1, fatal_report["exit_status"])

    @staticmethod
    def fake_live_fetcher(calls: list[str], overflow: bool = False):
        def fetch(url: str, allowed: set[str], timeout: float, user_agent: str) -> FetchResult:
            calls.append(url)
            if url.endswith("robots.txt"):
                return FetchResult(url, url, 200, "text/plain", b"User-agent: *\nAllow: /", 0)
            if url.endswith("sitemap.xml") or url.endswith("sitemap_index.xml"):
                return FetchResult(
                    url,
                    url,
                    200,
                    "application/xml",
                    b'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"/>',
                    0,
                )
            final_url = "https://moodjot.app/" if "moodjot.com" in url else url
            redirects = 4 if overflow and url == "https://moodjot.app/" else (1 if final_url != url else 0)
            body = (
                f'<html><head><link rel="canonical" href="{final_url}"></head><body>OK</body></html>'
            ).encode()
            return FetchResult(
                url,
                final_url,
                200,
                "text/html",
                body,
                redirects,
                (301,) if final_url != url else (),
            )

        return fetch

    def test_live_redirect_overflow_is_fatal(self) -> None:
        manifest = self.manifest()
        calls: list[str] = []
        report = self.validate(
            manifest,
            mode="live",
            fetcher=self.fake_live_fetcher(calls, overflow=True),
        )
        self.assertIn("LIVE.REDIRECT_OVERFLOW", self.rules(report))
        self.assertEqual(1, report["exit_status"])

    def test_live_legacy_redirect_must_be_permanent(self) -> None:
        manifest = self.manifest()
        calls: list[str] = []
        normal_fetch = self.fake_live_fetcher(calls)

        def temporary_legacy_fetch(url: str, allowed: set[str], timeout: float, user_agent: str):
            if url == "https://moodjot.com/":
                return FetchResult(
                    url,
                    "https://moodjot.app/",
                    200,
                    "text/html",
                    b'<html><head><link rel="canonical" href="https://moodjot.app/"></head></html>',
                    1,
                    (302,),
                )
            return normal_fetch(url, allowed, timeout, user_agent)

        report = self.validate(manifest, mode="live", fetcher=temporary_legacy_fetch)
        self.assertIn("LIVE.LEGACY_REDIRECT", self.rules(report))
        self.assertEqual(1, report["exit_status"])

    def test_live_refuses_arbitrary_host_before_network_open(self) -> None:
        manifest = self.manifest()
        manifest["products"]["moodjot"]["sitemap_url"] = "https://evil.example/sitemap.xml"
        calls: list[str] = []
        report = self.validate(
            manifest,
            mode="live",
            fetcher=self.fake_live_fetcher(calls),
            resolver=lambda _hostname, _port: ("93.184.216.34",),
        )
        self.assertIn("LIVE.REQUEST_BOUNDARY", self.rules(report))
        self.assertNotIn("https://evil.example/sitemap.xml", calls)
        self.assertEqual(1, report["exit_status"])

    def test_live_origin_contract_rejects_manifest_selected_public_host(self) -> None:
        manifest = self.manifest()
        manifest["products"]["moodjot"]["preferred_origin"] = "https://attacker.example/"
        calls: list[str] = []
        report = self.validate(
            manifest,
            mode="live",
            fetcher=self.fake_live_fetcher(calls),
            resolver=lambda _hostname, _port: ("93.184.216.34",),
        )
        self.assertIn("REG.ORIGIN_CONTRACT", self.rules(report))
        self.assertIn("LIVE.REQUEST_BOUNDARY", self.rules(report))
        self.assertNotIn("https://attacker.example/", calls)

    def test_request_boundary_rejects_local_and_non_global_literal_ips(self) -> None:
        validator = PortfolioValidator(
            self.manifest(),
            self.manifest_path,
            "live",
            selected_sites=["moodjot"],
            resolver=lambda _hostname, _port: ("93.184.216.34",),
        )
        urls = (
            "https://127.0.0.1/",
            "https://10.0.0.1/",
            "https://169.254.169.254/",
            "https://224.0.0.1/",
            "https://0.0.0.0/",
            "https://[::1]/",
            "https://[fe80::1]/",
            "https://[ff02::1]/",
        )
        for url in urls:
            with self.subTest(url=url):
                with self.assertRaises(RequestBoundaryError):
                    validator._validate_request_target(url, {normalized_origin(url)})

    def test_request_boundary_rejects_userinfo_and_private_dns_answers(self) -> None:
        validator = PortfolioValidator(
            self.manifest(),
            self.manifest_path,
            "live",
            selected_sites=["moodjot"],
            resolver=lambda _hostname, _port: ("192.168.1.10",),
        )
        with self.assertRaises(RequestBoundaryError):
            validator._validate_request_target(
                "https://user:secret@moodjot.app/",
                {"https://moodjot.app"},
            )
        with self.assertRaises(RequestBoundaryError):
            validator._validate_request_target(
                "https://moodjot.app/",
                {"https://moodjot.app"},
            )

    def test_redirect_target_is_dns_checked_before_second_open(self) -> None:
        manifest = self.manifest()

        def resolver(hostname: str, _port: int) -> tuple[str, ...]:
            if hostname == "moodjot.com":
                return ("127.0.0.1",)
            return ("93.184.216.34",)

        class RedirectingOpener:
            def __init__(self) -> None:
                self.calls: list[str] = []

            def open(self, request, timeout):
                self.calls.append(request.full_url)
                headers = email.message.Message()
                headers["Location"] = "https://moodjot.com/"
                raise urllib.error.HTTPError(
                    request.full_url,
                    301,
                    "Moved Permanently",
                    headers,
                    io.BytesIO(),
                )

        opener = RedirectingOpener()
        validator = PortfolioValidator(
            manifest,
            self.manifest_path,
            "live",
            selected_sites=["moodjot"],
            resolver=resolver,
        )
        allowed = validator._allowed_origins("moodjot", manifest["products"]["moodjot"])
        with patch("scripts.validate_portfolio.urllib.request.build_opener", return_value=opener):
            with self.assertRaises(RequestBoundaryError):
                validator._safe_fetch("https://moodjot.app/", allowed, "test-agent")
        self.assertEqual(["https://moodjot.app/"], opener.calls)

    def test_findings_have_complete_unique_schema(self) -> None:
        manifest = self.manifest()
        record = self.configure_site(manifest)
        self.write_passing_site(record)
        (self.root / "sitemap.xml").write_text("<bad", encoding="utf-8")
        report = self.validate(manifest)
        required = {
            "finding_id",
            "rule_id",
            "property_id",
            "publication_variant",
            "severity",
            "message",
            "evidence",
        }
        self.assertTrue(report["findings"])
        self.assertTrue(all(set(finding) == required for finding in report["findings"]))
        ids = [finding["finding_id"] for finding in report["findings"]]
        self.assertEqual(len(ids), len(set(ids)))


if __name__ == "__main__":
    unittest.main()
