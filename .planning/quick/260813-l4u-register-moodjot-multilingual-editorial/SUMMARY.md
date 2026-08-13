---
quick_id: 260813-l4u
slug: register-moodjot-multilingual-editorial
status: complete
code_commit: 210c6f6
---

# MoodJot çok dilli editorial yayın sözleşmesini kaydet

## Sonuç

Merkez portföy kaydı MoodJot’un sekiz gerçek editorial dilini ve 99 canonical URL’sini tanıyor. İngilizce ana sayfa, gizlilik ve koşullar tek URL olarak kalırken blog, makaleler ve sözlük sekiz dilde karşılıklı hreflang sözleşmesiyle doğrulanıyor.

## Teslim edilenler

- MoodJot için `en`, `tr`, `es`, `de`, `fr`, `pt-BR`, `ru` ve `zh-Hans` indexable locale kaydı.
- Ana ve legal URL'ler için tek-dilli locale kapsamı; tüm editorial URL'ler için çok dilli kapsam.
- Deterministik MoodJot üretici/doğrulayıcı komutları için onaylı no-shell kaynak komut sözleşmesi.
- Test fixture'larında varsayılan tek-dilli örnek mimarinin açıkça korunması.

## Doğrulama

- `python3 -m unittest discover -s scripts/tests -p 'test_*.py'` — 55 test geçti.
- Registry doğrulaması — sıfır bulgu.
- MoodJot kaynak doğrulaması, her iki native editorial denetimini çalıştırarak — sıfır bulgu.
