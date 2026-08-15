from __future__ import annotations

import struct
import unittest
from html.parser import HTMLParser
from pathlib import Path


PRODUCT_IDS = (
    "moodjot",
    "vynix",
    "swipe-slip",
    "glow-spin",
    "hive-due",
    "astral-post",
    "gridzle",
    "hoskin",
    "lastimo",
    "the-cosmic-meta",
    "u2m",
)

LOGO_PRODUCTS = {
    "moodjot": "MoodJot",
    "vynix": "Vynix",
    "swipe-slip": "Swipe Slip",
    "glow-spin": "Glow Spin",
    "hive-due": "Hive Due / Site Hesap",
    "astral-post": "Astral Post",
    "gridzle": "Gridzle",
    "hoskin": "Hoşkin",
    "lastimo": "Lastimo",
    "u2m": "U2M URL Shortener",
}


class ProductCardParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.cards: list[dict] = []
        self.current_card: dict | None = None
        self.unavailable_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attributes = dict(attrs)
        classes = set((attributes.get("class") or "").split())

        if tag == "article" and "product-card" in classes:
            self.current_card = {
                "product_id": attributes.get("data-product-id"),
                "images": [],
                "unavailable": [],
                "monograms": [],
            }
            return

        if self.current_card is None:
            return

        if "product-monogram" in classes:
            self.current_card["monograms"].append(attributes)
        if tag == "img" and "product-logo" in classes:
            self.current_card["images"].append(attributes)
        if tag == "div" and "product-logo--unavailable" in classes:
            self.current_card["unavailable"].append({"attrs": attributes, "text": []})
            self.unavailable_depth += 1

    def handle_data(self, data: str) -> None:
        if self.current_card is not None and self.unavailable_depth:
            self.current_card["unavailable"][-1]["text"].append(data)

    def handle_endtag(self, tag: str) -> None:
        if self.current_card is None:
            return
        if tag == "div" and self.unavailable_depth:
            self.unavailable_depth -= 1
        if tag == "article":
            self.cards.append(self.current_card)
            self.current_card = None
            self.unavailable_depth = 0


class ProductCardLogoTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root = Path(__file__).resolve().parents[2]
        cls.pages = {
            "en": cls.root / "index.html",
            "tr": cls.root / "tr" / "index.html",
        }

    def parse_cards(self, locale: str) -> list[dict]:
        parser = ProductCardParser()
        parser.feed(self.pages[locale].read_text(encoding="utf-8"))
        parser.close()
        return parser.cards

    def test_localized_product_cards_use_verified_local_logos(self) -> None:
        for locale in ("en", "tr"):
            with self.subTest(locale=locale):
                cards = self.parse_cards(locale)
                self.assertEqual(PRODUCT_IDS, tuple(card["product_id"] for card in cards))

                cards_by_id = {card["product_id"]: card for card in cards}
                for product_id, name in LOGO_PRODUCTS.items():
                    with self.subTest(locale=locale, product_id=product_id):
                        card = cards_by_id[product_id]
                        self.assertEqual([], card["monograms"])
                        self.assertEqual([], card["unavailable"])
                        self.assertEqual(1, len(card["images"]))
                        image = card["images"][0]
                        expected_src = f"images/products/{product_id}.png"
                        if locale == "tr":
                            expected_src = f"/{expected_src}"
                        self.assertEqual(expected_src, image.get("src"))
                        self.assertFalse((image.get("src") or "").startswith(("http://", "https://")))
                        expected_alt = f"{name} logo" if locale == "en" else f"{name} logosu"
                        self.assertEqual(expected_alt, image.get("alt"))
                        self.assertEqual("56", image.get("width"))
                        self.assertEqual("56", image.get("height"))
                        self.assert_png_dimensions(product_id)

                cosmic = cards_by_id["the-cosmic-meta"]
                self.assertEqual([], cosmic["monograms"])
                self.assertEqual([], cosmic["images"])
                self.assertEqual(1, len(cosmic["unavailable"]))
                fallback = cosmic["unavailable"][0]
                self.assertEqual("true", fallback["attrs"].get("aria-hidden"))
                self.assertNotIn("src", fallback["attrs"])
                self.assertEqual("", "".join(fallback["text"]).strip())

    def test_no_product_monograms_remain(self) -> None:
        for path in (*self.pages.values(), self.root / "styles.css"):
            with self.subTest(path=path):
                self.assertNotIn("product-monogram", path.read_text(encoding="utf-8"))

    def assert_png_dimensions(self, product_id: str) -> None:
        path = self.root / "images" / "products" / f"{product_id}.png"
        data = path.read_bytes()
        self.assertGreaterEqual(len(data), 24, path)
        self.assertEqual(b"\x89PNG\r\n\x1a\n", data[:8], path)
        self.assertEqual(b"IHDR", data[12:16], path)
        width, height = struct.unpack(">II", data[16:24])
        self.assertGreaterEqual(width, 56, path)
        self.assertGreaterEqual(height, 56, path)


if __name__ == "__main__":
    unittest.main()
