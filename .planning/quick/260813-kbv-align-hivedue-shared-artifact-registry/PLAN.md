# Hive Due paylaşımlı artefakt kaydını eşleştir

## Amaç

Portföy doğrulayıcısının Hive Due / Site Hesap için eski iki-artifact mimarisini istemesini engellemek ve gerçek tek `www/dist/` yayın sözleşmesini kayda geçirmek.

## Kapsam

1. İki yayın varyantının da aynı `dist/` kökünü, geçerli tek build komutunu ve kendi host/locale/canonical keşif sözleşmesini kullanmasını sağla.
2. Aynı kökü iki host görünümü olarak denetleyen fixture'ı güncelle; çapraz host hreflang, sitemap ve ürün kimliği kontrollerini koru.
3. Kayıt, birim testleri ve gerçek Hive Due kaynak denetimini çalıştır; GSD özet/durum kaydını ekle.

## Sınırlar

- Bu görev Nginx, DNS, canlı deployment veya Hive Due içerik kaynağını değiştirmez.
- İki host, tek `www/dist/` ve tek `_astro/` ağacını paylaşmaya devam eder.
