---
quick_id: 260813-kbv
slug: align-hivedue-shared-artifact-registry
status: complete
code_commit: a4a78c6
---

# Hive Due paylaşımlı artefakt kaydını eşleştir

## Sonuç

Merkez portföy kaydı ve doğrulayıcısı, Hive Due / Site Hesap'ın gerçek tek `www/dist/` yayın modelini denetler. İki host aynı statik dosyaları paylaşır; bununla birlikte her host yalnız kendi canonical rota, sitemap ve robots görünümüyle doğrulanır.

## Teslim edilenler

- Her iki yayın varyantı için `npm run build` ve ortak `dist/` output sözleşmesi.
- Nginx'in dışarıda `/robots.txt` ve `/sitemap.xml` olarak yayımladığı host-özel `robots-*.txt` ve `sitemap-*.xml` kaynak eşlemesi.
- Ortak output kökünde declared canonical rota kapsamını ayrı denetleyen doğrulayıcı davranışı.
- Ortak artefaktta bulunmayan noindex locale kopyalarını zorunlu tutmayan, karşılıklı canonical hreflang denetimini koruyan kayıt sözleşmesi.
- Ortak-artifact Hive fixture'ı ve hata senaryoları için güncellenmiş birim testleri.

## Doğrulama

- `python3 -m unittest discover -s scripts/tests -p 'test_*.py'` — 55 test geçti.
- `python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode registry --site hive-due` — sıfır bulgu.
- `python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode source --site hive-due` — sıfır bulgu.

## Dağıtım notu

Bu değişiklik yalnız portföy kaydı/doğrulama sözleşmesidir. Nginx, DNS ve canlı artifact geçişi değiştirilmedi.
