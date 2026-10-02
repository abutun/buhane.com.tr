from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import unittest
from urllib.parse import parse_qs, urlsplit


class InventoryParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cards = {}
        self.map_links = []
        self.map_labels = {}
        self.stylesheets = []
        self.hero_totals = []
        self.about_totals = []
        self.capture = None
        self.current_map = None
        self.map_label = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = set(attrs.get("class", "").split())
        if "product-card" in classes:
            self.cards[attrs["data-product-id"]] = attrs["data-product-category"]
        if "map-product" in classes:
            self.map_links.append(attrs["href"])
            self.current_map = attrs["href"]
            self.map_labels[self.current_map] = {}
        if self.current_map and tag == "span":
            for label in ("map-product-name", "map-product-type"):
                if label in classes:
                    self.map_label = label
                    self.map_labels[self.current_map][label] = ""
        if tag == "link" and attrs.get("rel") == "stylesheet":
            self.stylesheets.append(attrs["href"])
        if tag == "dt":
            self.capture = ("dt", self.hero_totals)
        elif "stat-number" in classes:
            self.capture = (tag, self.about_totals)

    def handle_data(self, data):
        if self.current_map and self.map_label:
            self.map_labels[self.current_map][self.map_label] += data
        if self.capture and data.strip():
            self.capture[1].append(int(data.strip()))

    def handle_endtag(self, tag):
        if tag == "span":
            self.map_label = None
        elif tag == "a":
            self.current_map = None
        if self.capture and self.capture[0] == tag:
            self.capture = None


class PortfolioInventoryTests(unittest.TestCase):
    def test_bilingual_totals_and_product_categories_are_synchronized(self):
        root = Path(__file__).resolve().parents[2]
        for locale, page, base in (
            ("en", "index.html", "/products/"),
            ("tr", "tr/index.html", "/tr/urunler/"),
        ):
            with self.subTest(locale=locale):
                parser = InventoryParser()
                parser.feed((root / page).read_text(encoding="utf-8"))
                self.assertEqual(14, len(parser.cards))
                self.assertEqual(
                    Counter(app=5, game=5, saas=3, publication=1),
                    Counter(parser.cards.values()),
                )
                self.assertEqual("saas", parser.cards["mintropolis"])
                self.assertEqual("app", parser.cards["leaselore"])
                self.assertEqual([14, 5, 5, 4], parser.hero_totals)
                self.assertEqual(parser.hero_totals, parser.about_totals)
                self.assertEqual(14, len(parser.map_links))
                self.assertEqual(14, len(set(parser.map_links)))
                self.assertIn(base + "mintropolis/", parser.map_links)
                self.assertIn(base + "leaselore/", parser.map_links)

    def test_leaselore_map_tile_has_localized_name_and_app_label(self):
        root = Path(__file__).resolve().parents[2]
        for page, href, category in (
            ("index.html", "/products/leaselore/", "App"),
            ("tr/index.html", "/tr/urunler/leaselore/", "Uygulama"),
        ):
            with self.subTest(page=page):
                parser = InventoryParser()
                parser.feed((root / page).read_text(encoding="utf-8"))
                self.assertEqual(
                    {"map-product-name": "LeaseLore", "map-product-type": category},
                    parser.map_labels[href],
                )

    def test_homepages_use_the_same_versioned_shared_stylesheet(self):
        root = Path(__file__).resolve().parents[2]
        versions = []
        for page in ("index.html", "tr/index.html"):
            with self.subTest(page=page):
                parser = InventoryParser()
                parser.feed((root / page).read_text(encoding="utf-8"))
                stylesheets = [
                    urlsplit(href) for href in parser.stylesheets
                    if urlsplit(href).path.lstrip("/") == "styles.css"
                ]
                self.assertEqual(1, len(stylesheets))
                version = parse_qs(stylesheets[0].query).get("v")
                self.assertTrue(version, "Refresh the CSS URL when the product-map layout changes")
                versions.append(version)
        self.assertEqual(versions[0], versions[1])


if __name__ == "__main__":
    unittest.main()
