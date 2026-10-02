from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
import unittest


class InventoryParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.cards = {}
        self.map_links = []
        self.hero_totals = []
        self.about_totals = []
        self.capture = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        classes = set(attrs.get("class", "").split())
        if "product-card" in classes:
            self.cards[attrs["data-product-id"]] = attrs["data-product-category"]
        if "map-product" in classes:
            self.map_links.append(attrs["href"])
        if tag == "dt":
            self.capture = ("dt", self.hero_totals)
        elif "stat-number" in classes:
            self.capture = (tag, self.about_totals)

    def handle_data(self, data):
        if self.capture and data.strip():
            self.capture[1].append(int(data.strip()))

    def handle_endtag(self, tag):
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


if __name__ == "__main__":
    unittest.main()
