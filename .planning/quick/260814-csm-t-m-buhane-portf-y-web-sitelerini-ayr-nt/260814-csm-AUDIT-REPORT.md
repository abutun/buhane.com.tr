# Buhane portföy web siteleri audit raporu

**Tarih:** 14 Ağustos 2026
**Kapsam:** Kaynak ağacı, yerel üretim/doğrulama sözleşmeleri ve sınırlı canlı HTTP kanıtı. Bu rapor üretime dağıtım yapıldığını göstermez.

## Site özeti

| Web sitesi | Durum | Kısa bulgu ve takip |
|---|---|---|
| Buhane Bilgi Teknolojileri | Kaynak doğrulandı | EN/TR şirket, ürün ve yönlendirme yüzeyi merkez kayıtla uyumlu. |
| ahmet.sh | Kaynak doğrulandı | Kişisel profil ve seçili çalışmalar yüzeyi kanonik kaynak sözleşmesini geçiyor. |
| MoodJot | Kaynak doğrulandı | Sekiz dildeki blog/sözlük rotaları ve kartlı içerik yüzeyi kaynakta mevcut. |
| Vynix | Kaynak doğrulandı | Yerelleştirilmiş dokümantasyon, blog ve sözlük envanteri doğrulandı; mevcut admin çıktısı değiştirilmedi. |
| Swipe Slip | Kaynak doğrulandı | Keşif yüzeyi, mağaza bağlantıları ve oyun bağlamı kaynakta doğrulandı. |
| Glow Spin | Kaynak doğrulandı | Kompakt mağaza CTA’ları ile içerik/metadata yüzeyi kaynak sözleşmesini geçiyor. |
| Hive Due / Site Hesap | Kaynak düzeltmesi yapıldı | Dört `href="#"` mağaza yer tutucusu etkileşimsiz, yerelleştirilmiş “Yakında” içeriğine dönüştürüldü; ortak dağıtım kökü için operatör kontrol listesi netleştirildi. |
| Astral Post | Kaynak düzeltmesi yapıldı | Gizlilik sayfasındaki yedi harici yeni-sekme bağlantısına `noopener noreferrer` eklendi; doğrulayıcı bu güvenlik kuralını koruyor. |
| Gridzle | Kaynak doğrulandı | Beş rotalı oyun keşif yüzeyi sağlam; etkin `.gsd/` çalışması korunarak kapsam dışında bırakıldı. |
| Hoşkin | Kaynak doğrulandı | Çok dilli oyun/içerik üretimi ve kanonik rota envanteri doğrulandı. |
| Lastimo | Kaynak doğrulandı | Yerelleştirilmiş ürün/içerik rotaları ve sınırlı ürün iddiaları kaynakta doğrulandı. |
| The Cosmic Meta | Harici erişim engeli | Yönetilen WordPress/deploy kaynağı sağlanmadan siteye dokunulmadı. |
| U2M URL Shortener | Kaynak doğrulandı | Genel landing, rehber, kullanım senaryosu ve keşif dosyaları kaynak sözleşmesini geçiyor. |

## Kaynak ve dağıtım ayrımı

`Kaynak doğrulandı` ve `Kaynak düzeltmesi yapıldı` ifadeleri yalnızca yerel kaynak ile yerel doğrulama sonuçlarını anlatır. Bunlar, aynı sürümün üretimde çalıştığını kanıtlamaz. Tüm düzenlenebilir sitelerde üretim ortamı için **Dağıtım doğrulaması bekliyor**; yetkili operatörün sürüm, yönlendirme ve ham HTTP kanıtını ayrı release kaydında toplaması gerekir.

Hive Due / Site Hesap için takip operatöre aittir: iki marketing Nginx bloğu tek `/var/www/hivedue/www/current` kökünü kullanmalı; `hivedue.com/` host içinde `/en/` yoluna yönlenmeli; her host kendi `robots.txt` ve `sitemap.xml` karşılığını sunmalıdır. Sunucu/Nginx, GeoIP, sembolik bağlantı, DNS/CDN ve önbellek değişiklikleri bu audit kapsamında yapılmadı.

The Cosmic Meta için kesin engel şudur: No verified local source, repository, build, deploy pipeline, or WordPress administration path has been shown to own `https://thecosmicmeta.com/`.

## Audit yöntemi ve kanıt kaynakları

- Merkezi envanter: `.planning/portfolio-sites.json`
- Önceki kaynak/canlı ayrım kanıtı: `05-RELEASE-VALIDATION.md`
- The Cosmic Meta erişim ve sahiplik dosyası: `05-EXTERNAL-BLOCKERS.md`
- Her düzenlenebilir sitenin yerel üretici, test ve doğrulama komutları
- İncelenen başlıklar: kanonik/sitemap/robots uyumu, locale rotaları, yapılandırılmış veri, sahiplik bağları, bağlantı güvenliği, içerik iddiası sınırları, temel erişilebilirlik ve görünür etkileşimler

## Bu görevde çalıştırılan kapılar

| Komut | Sonuç |
|---|---|
| `python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode registry` | Çıkış `0`; bulgu yok. |
| `python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode source --timeout 180 --report /tmp/260814-csm-source.json` | Çıkış `0`; yüksek/orta/düşük/bilgi bulgusu `0/0/0/0`. |
| `python3 -m unittest discover -s scripts/tests -p 'test_*.py'` | Çıkış `0`; 55 test geçti. Testlerin kontrollü timeout senaryoları beklenen `GEN.COMMAND_TIMEOUT` çıktısını üretti. |
| AstralPost: `node scripts/verify-content-hub.mjs` | 9 locale, 90 makale, 135 sözlük terimi ve 112 kanonik URL ile geçti. |
| AstralPost: yedi yeni-sekme bağlantısı için yerel Node kontrolü | 7 güvenli bağlantı, 0 güvensiz bağlantı. |
| Hive Due: `npm run check` | 0 hata, 0 uyarı, 0 ipucu. |
| Hive Due: `npm test` | 5 test dosyası, 26 test geçti; tek ortak `dist/` üretildi. |
| Hive Due: `npm run verify:regional-assets` | 85 HTML ve 26 yerel varlık iki Host başlığıyla doğrulandı; eksik `/_astro/` isteği HTML olmayan 404 döndü. |
| Hive Due: mağaza yer tutucusu kontrolü | İki paylaşılan bileşende `href="#"` kalmadı. |

## Yapılan değişiklikler

- Astral Post gizlilik politikasındaki tüm harici `target="_blank"` bağlantıları opener izolasyonu alacak şekilde düzeltildi; statik içerik doğrulayıcısına gerileme kontrolü eklendi.
- Hive Due / Site Hesap’ta yayınlanmamış App Store ve Google Play yüzeyleri gerçek URL yokken link olmaktan çıkarıldı. Web uygulaması CTA’sı tek gerçek yönlendirilebilir birincil CTA olarak kaldı.
- Hive Due dağıtım notu, ortak artifact kökü, dört host-nitelikli discovery dosyası, Nginx örneğinin doğru göreli yolu ve zorunlu content-type probe’ları ile netleştirildi.

## Kapsam dışı ve sonraki adımlar

- Üretim deploy, Nginx/GeoIP düzenleme, CDN/DNS/TLS, cache purge, analytics, Search Console/Bing/IndexNow veya mağaza listeleme değişikliği yapılmadı.
- The Cosmic Meta için erişim paketi alınmadan WordPress, tema, eklenti, Yoast, robots/sitemap veya canlı içerik değiştirilmedi.
- Vynix’in mevcut admin çıktısı ve Gridzle’ın etkin `.gsd/` durumu korunarak bu görevin dışında bırakıldı.
- Hive Due / Site Hesap operatörü yetkili deploy sonrasında her iki hostun `robots.txt` yanıtında `text/plain`, `sitemap.xml` yanıtında XML content type ve country-dependent yönlendirme kanıtını release kaydına eklemelidir.
