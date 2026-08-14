# Buhane Portföyü — Arama ve Yapay Zekâ Keşif Runbook'u

**Tarih:** 2026-08-14
**Kapsam:** Buhane, kişisel site ve kayıtlı tüm ürünler için kaynakta doğrulanmış arama/yanıt-motoru görünürlüğü, içerik bakımı ve yayın devri.
**Sınır:** Bu belge hesap, CDN/WAF, DNS, Nginx, GeoIP, arama konsolu, analiz veya canlı yayını değiştirmez.

## Yönetici özeti

Google AI Overviews ve AI Mode, ayrı bir “AI SEO” formatı değil; normal Google Arama'nın taranabilirlik, indekslenebilirlik ve faydalı/insan odaklı içerik ilkelerine dayanır. ChatGPT Search için ilgili tarama erişimi `OAI-SearchBot`'tur. Kayıtlı düzenlenebilir kaynaklarda `User-agent: *` ve `Allow: /` zaten bu botu kaynak seviyesinde engellemez.

Bu nedenle portföye topluca `llms.txt`, AI'ya özel şema, gizli AI metni, zorunlu parçalara ayırma veya sorgu varyantı makaleleri eklenmemelidir. Bunlar Google görünürlüğü için gereklilik ya da kanıtlanmış sıralama/alıntılanma kaldıracı değildir; ChatGPT için de görünür ve doğru HTML, erişilebilirlik, doğru kanonik URL, robots ve sitemap'ın yerini tutmaz. En acil gerçek bulgu yalnızca Hive Due / Site Hesap'ın canlı `robots.txt` ve `sitemap.xml` eşlemesidir.

### Birincil kaynaklar

- Google: [Üretken yapay zekâ arama deneyimleri için optimizasyon](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
- Google: [AI özellikleri ve web siteleri / tarayıcı kontrolleri](https://developers.google.com/search/docs/appearance/ai-features)
- Google: [Teknik gereksinimler](https://developers.google.com/search/docs/essentials/technical) ve [teknik SEO başlangıcı](https://developers.google.com/search/docs/fundamentals/get-started)
- Google: [Organization yapılandırılmış verisi](https://developers.google.com/search/docs/appearance/structured-data/organization)
- OpenAI: [Publishers and Developers FAQ](https://help.openai.com/en/articles/12627856-publishers-and-developers-faq) ve [tarayıcı belgeleri](https://developers.openai.com/api/docs/bots)

Bu kaynaklar uygunluğun indeksleme, sıralama veya alıntılanma garantisi olmadığını da açıkça gerektirir.

## Portföy durumu ve güvenli içerik bakımı

Her yeni sayfa veya güncelleme aşağıdaki dört koşulu birlikte sağlamalıdır: (1) mevcutta yayınlanmış/kanıtlanmış bir yetenek, (2) gerçek arama sorgusu, kullanıcı sorusu, destek talebi ya da dönüşüm kanıtı, (3) kullanıcıyı ilerleten anlamlı bir sonraki bağlantı ve (4) gerçekten sürdürülebilecek bir yerelleştirilmiş sürüm. Desteklenmeyen özellik, mağaza, tıbbi/wellness sonucu, tarih veya kullanım iddiası eklenmez. Hesap verisi `not_verified` ise sıfır olarak raporlanmaz.

| Kayıtlı mülk | Doğrulanmış kaynak / içerik yüzeyi | Güvenli bakım ölçütü | Bu task için deploy sınıfı | Canlı / harici yeterlilik notu |
|---|---|---|---|---|
| **Buhane Bilgi Teknolojileri** | 26 EN/TR şirket, portföy ve ürün-detay rotası; Organization şeması ve onaylı ürün bağları | Doğrulanmış hizmet/ürün sorusunu EN ve TR'de açıklayan, doğru ürün veya iletişim bağlantılı sayfa | **Bu task için yeni kaynak deploy'u yok** | Phase 05 kaynağı `deployment_pending`; daha önce commit edilmiş kaynağın canlı revizyonu kanıtlanmadı |
| **ahmet.sh** | Tek, gerçekçi Person/Organization sayfası ve seçilmiş çalışmalar | Gerçek portföy/iletişim sorusu; var olmayan dil rotası veya biyografi iddiası ekleme | **Bu task için yeni kaynak deploy'u yok** | `deployment_pending`; canlı revizyon eşlemesi kanıtlanmadı |
| **MoodJot** | 8 dilde adreslenebilir editoryal/glossary rotaları ve doğrulanmış yerelleştirilmiş içerik üreticisi | Yayınlanmış mood/journal özelliği + gerçek kullanıcı sorusu; tıbbi tanı/tedavi iddiası yok | **Bu task için yeni kaynak deploy'u yok** | `deployment_pending`; mevcut yerel kaynak ChatGPT erişimi için wildcard ile engel koymuyor |
| **Vynix** | 5 dilde rehber, glossary ve docs; deterministik içerik üreticisi | Yayınlanmış AI içerik üretim yeteneği + gerçek görev/sorgu; sürüm kanıtı olmadan özellik ekleme yok | **Bu task için yeni kaynak deploy'u yok** | `deployment_pending`; mevcut `www/admin/dist/index.html` kirliliği bu çalışmanın dışındadır |
| **Swipe Slip** | 10 oyun rehberi, glossary, FAQ ve VideoGame şeması | Gerçek oyuncu/mağaza destek sorusu + ilgili rehber/indirme bağlantısı | **Bu task için yeni kaynak deploy'u yok** | `deployment_pending`; kaynak kontratı geçmiştir |
| **Glow Spin** | 10 rehber, glossary ve oyun şeması | Gerçek oyuncu sorusu veya yayınlanmış oyun davranışı + ilgili sonraki bağlantı | **Bu task için yeni kaynak deploy'u yok** | `deployment_pending`; kaynak kontratı geçmiştir |
| **Hive Due / Site Hesap** | Tek ürün kimliğiyle EN/TR kaynaklar, resources/blog/guides/docs ve iki hosta ait üretilen keşif dosyaları | Yayınlanmış topluluk finansı iş akışı + gerçek yönetici/sakin sorusu; ikinci bölgesel build yok | **Acil deploy / canlı düzeltme** | Canlı `robots.txt`/`sitemap.xml` HTML fallback veriyor; aşağıdaki tek paylaşımlı artifact işlemi gerekir |
| **Astral Post** | Yansıtma rehberleri, glossary ve desteklenen EN/TR rota kontratı | Yayınlanmış reflection iş akışı + gerçek kullanıcı sorusu; wellness/tedavi sonucu uydurma yok | **Bu task için yeni kaynak deploy'u yok** | Phase 05 ve önceki denetimden commit edilmiş kaynak için canlı revizyon hâlâ kanıtlanmadı |
| **Gridzle** | HowTo/FAQ, beş kanonik rota ve oyun şeması | Gerçek oynanış/release kanıtı + ilgili oyun rehberi bağlantısı | **Bu task için yeni kaynak deploy'u yok** | Phase 05 ve önceki denetimden commit edilmiş kaynak için canlı revizyon hâlâ kanıtlanmadı; mevcut Android/.gsd kirliliğine dokunulmaz |
| **Hoşkin** | Beş adreslenebilir dilde kurallar rehberi, glossary ve feed | Gerçek kural/oynanış sorusu + sürdürülebilir aynı-dil içeriği; mağaza bağlantısı ancak doğrulanınca | **Bu task için yeni kaynak deploy'u yok** | `deployment_pending`; kaynak kontratı geçmiştir |
| **Lastimo** | 12 yerelleştirilmiş herkese açık set, rehberler ve sıkı ürün-doğruluk sınırları | Yayınlanmış yetenek + gerçek kullanıcı sorusu; geçmiş, analiz, özel tracker veya tıbbi iddia yok | **Bu task için yeni kaynak deploy'u yok** | `deployment_pending`; kaynak kontratı geçmiştir |
| **The Cosmic Meta** | Yerel düzenlenebilir kaynak yok; yalnızca Buhane ürün ayrıntısı doğrulanabilir | Kaynak/WordPress sahibi doğrulanmadan içerik ya da discovery dosyası düzenlenmez | **Harici erişim engeli** | “No verified local source, repository, build, deploy pipeline, or WordPress administration path has been shown to own `https://thecosmicmeta.com/`.” |
| **U2M URL Shortener** | Herkese açık docs, use case, API sayfaları; token/özel rotalar hariç | Yayınlanmış API/web özelliği + gerçek geliştirici sorusu; kısaltılmış hedef URL veya kullanıcı verisi kullanma | **Bu task için yeni kaynak deploy'u yok** | `deployment_pending`; dağıtımda public statik rotalar ile uygulama rotaları ayrı doğrulanmalı |

**Yeniden deploy kararı:** Bu task'ta yeni kaynak değişikliği yalnızca planlama dokümanıdır; bu yüzden diğer on bir düzenlenebilir mülk için “bu task nedeniyle” deploy yoktur. Bununla birlikte yukarıdaki `deployment_pending` kayıtları, önceki doğrulanmış Phase 05 kaynak revizyonlarının canlıda izlenebilir biçimde kanıtlanmadığını ifade eder; canlıyı güncelleme/kanıtlama kararı yayın sahibindedir. Buhane Bilgi Teknolojileri, Astral Post ve Gridzle için önceden commit edilmiş fakat canlı revizyonu kanıtlanmamış kaynak notu ayrıca korunur.

## Tarayıcı politikası: sahip onayı şablonu

Her public origin için aşağıdaki kayıt ayrı ayrı tutulmalıdır. Bu çalışma hiçbir robots kuralını değiştirmez.

| Alan | Kaydedilecek karar / kanıt |
|---|---|
| Origin ve kapsam | Tercih edilen origin, hangi public yolların taranabilir olduğu, sorumlu yayın sahibi |
| Normal arama erişimi | Varsayılan: mevcut `User-agent: *` / `Allow: /` korunur. Bu, kaynak seviyesinde `OAI-SearchBot` erişimini zaten kapsar; ayrıca tekrarlı bot satırı gerekmez. |
| `OAI-SearchBot` | Arama/ChatGPT Search için durum: wildcard üzerinden erişilebilir. Yayın sonrası ham yanıt ve CDN/WAF katmanının da bu erişimi engellemediği kanıtlanır. |
| `GPTBot` | Hukuk/ürün/gizlilik sahibi ayrı **allow** veya **block** seçer; karar sahibi ve tarih zorunludur. |
| `ClaudeBot` | Hukuk/ürün/gizlilik sahibi ayrı **allow** veya **block** seçer; karar sahibi ve tarih zorunludur. |
| `Google-Extended` | Hukuk/ürün/gizlilik sahibi ayrı **allow** veya **block** seçer. Googlebot'tan ayrıdır; normal Google Search/AI Overview uygunluğunu açıp kapatan bir anahtar değildir. |
| Değişiklik öncesi kanıt | Karar sahibi+tarih; kaynak robots dosyası; CDN/WAF kuralıyla uyum; ham deploy edilmiş yanıt; rollback noktası. |
| Değişiklik sonrası kanıt | Tercih edilen origin üzerinde HTTP 200, `text/plain`, doğru dosya gövdesi; CDN/WAF/redirect yeniden kontrolü; geri alma sorumlusu. |

Reklam tarayıcısı kuralı, reklam satın alımı, Search Console/Bing ayarı, IndexNow, DNS/CDN/WAF veya analiz hesap değişikliği bu runbook'un kapsamı dışındadır.

## Acil canlı düzeltme: Hive Due / Site Hesap

Sorun kaynak kodu değil, yayın/configuration drift'idir. `apps/HiveDue/www/dist/` zaten **one shared** artifact köküdür; `robots-hivedue.txt`, `robots-sitehesap.txt`, `sitemap-hivedue.xml` ve `sitemap-sitehesap.xml` aynı artifact içinde bulunur. Bu artifact yalnızca **bir kez** yapılandırılmış current release köküne yayınlanır. İkinci bölgesel build, ikinci dist klasörü veya uygulama yeniden yazımı yapılmaz.

Operatör, `apps/HiveDue/deployment/nginx-hivedue-sitehesap.conf.example` içindeki mevcut kesin alias'ları etkinleştirmelidir:

| Host | Kesin yol | Alias | Beklenen içerik türü |
|---|---|---|---|
| `hivedue.com` | `/robots.txt` | `robots-hivedue.txt` | `text/plain` |
| `hivedue.com` | `/sitemap.xml` | `sitemap-hivedue.xml` | `application/xml` |
| `sitehesap.com` | `/robots.txt` | `robots-sitehesap.txt` | `text/plain` |
| `sitehesap.com` | `/sitemap.xml` | `sitemap-sitehesap.xml` | `application/xml` |

Yayın sonrasında `https://hivedue.com/robots.txt` ve `https://hivedue.com/sitemap.xml` bir **Türkiye dışı egress** üzerinden; `https://sitehesap.com/robots.txt` ve `https://sitehesap.com/sitemap.xml` ise **Türkiye egress** üzerinden test edilmelidir. Her yanıtta final hostname, dil/bölge davranışı, HTTP 200, yukarıdaki content type ve doğru kanonik host kontrol edilir. Bu doğrulama yalnızca canlı yapılandırmanın kaynak kontratıyla eşleştiğini gösterir; yeni bir ürün varyantı oluşturmaz.

## Yayın sonrası kontrol listesi

### Day 0 — deploy gününde

1. Her tercih edilen origin için ham HTTP ile ana sayfa, robots, sitemap ve örnek kanonik route: final HTTP 200, doğru `Content-Type`, self-canonical, indeksleme kuralı ve sitemap URL'sini doğrula.
2. Her sitemap'tan temsilî URL'leri, dil alternatifi olan sayfalarda alternatif/canonical ilişkisinin kaynaktaki kapsamla uyumunu ve görünür Organization/Product/WebSite yapılandırılmış verisini örnekle.
3. Google Search Console ve Bing Webmaster mülk sahipliği ile canonical sitemap gönderim/okuma durumunu kaydet; hesabın doğrulanmadığı yerde `not_verified` yaz, sıfır yazma.
4. Uygun olduğunda Rich Results/URL Inspection sonucunu temsilî sayfa, zaman ve sorunla kaydet. Bu raporlar sıralama garantisi değildir.
5. Onaylı ölçüm şeması dışında veri gönderme: yalnızca altı event adı (`portfolio_product_click`, `store_click`, `support_click`, `contact_start`, `contact_submit`, `signup_start`) ve beş özellik (`product_id`, `source_site`, `source_page_type`, `destination_type`, `locale`) kullanılabilir. Kullanıcı içeriği, günlük/mood notu, hedef kısaltılmış URL, fatura, token veya kimlik verisi kaydedilmez.

### Day 28 — kanıta dayalı ilk bakım turu

1. Search Console/Bing doğrulaması, sitemap read/fetch durumu, temsilî indekslenmiş kanonikler, hariç/duplicate URL'ler ve canonical-selection sorunlarını karşılaştır.
2. Sunuluyorsa impressions, clicks, CTR, sorgu grubu, ülke ve locale'i toplulaştırılmış olarak incele; Bing AI alıntı görünürlüğünü sunulduğunda kaydet.
3. Varsa toplulaştırılmış `utm_source=chatgpt.com` referral oturumları ve landing page türlerini, kullanıcı veya ürün verisi olmadan değerlendir.
4. Bir veya iki yeni içerik adayını yalnızca yukarıdaki dört bakım ölçütü ile seç; kanıt yoksa içerik ekleme.

### Day 90 — kalite ve yön kararı

1. Day 0/28 ile indeksleme, sitemap, şema uyarıları, sorgu/referral ve gerçek dönüşüm sonuçlarını karşılaştır; sezonluk veya ürün iddiası değişimlerini not et.
2. Hâlâ `deployment_pending` olan originlerde yayın revision, rollback noktası ve ham canlı kanıtı kapatılmadan başarı iddiasında bulunma.
3. İnce/tekrarlı veya artık doğru olmayan içerik için güncelleme, birleştirme, noindex ya da kaldırma kararını gerçek kaynak/sahip onayıyla al; yapay anahtar kelime genişletmesi yapma.

## Kaynak ve sözleşme doğrulaması

Doğrulamalar **2026-08-14** tarihinde, yalnızca yerel kaynak üzerinde çalıştırıldı. Hiçbiri canlı revision'ın yayınlandığını kanıtlamaz.

| Kontrol | Kesin sonuç |
|---|---|
| `PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode registry` | `PASS [registry] no findings`; high/medium/low/info `0/0/0/0`, çıkış `0` |
| `PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_portfolio.py --manifest .planning/portfolio-sites.json --mode source --timeout 180 --report /tmp/260814-igz-source.json` | `PASS [source] no findings`; high/medium/low/info `0/0/0/0`, çıkış `0` |
| `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s scripts/tests -p 'test_*.py'` | `55` test, `OK`, çıkış `0`. Test fixture'ları timeout hata yolunu kasıtlı olarak sınadığı için stdout'ta iki `GEN.COMMAND_TIMEOUT moodjot` satırı göründü; bunlar testin beklediği sentetik sonuçlardır, merkezi kaynak validator bulgusu değildir. |
| Hive artifact/Nginx denetimi | `PASS [hive-artifact-nginx] one dist root, four discovery files, and both host aliases present` |
| Kaynak robots ve `llms.txt` envanteri | 12 düzenlenebilir public yayın `User-agent: *` + `Allow: /` sözleşmesini koruyor; `OAI-SearchBot` kaynakta engellenmiyor. 12 public kaynak/output kökünde `llms.txt` bulunmuyor ve bu strateji için gerekli değildir. |

Hive doğrulamasında `www/dist/` altında dört dosya (`robots-hivedue.txt`, `robots-sitehesap.txt`, `sitemap-hivedue.xml`, `sitemap-sitehesap.xml`) bulundu. Aynı Nginx örneğinde iki host için hem kesin `location = /robots.txt` hem `location = /sitemap.xml` blokları ve ilgili alias adları bulundu.

## Sonuç

**Bu çalışmada kaynak değişikliği yapılmadı.** Bu, tüm canlı deploy'ların doğrulandığı anlamına gelmez; mevcut kaynak kontratı ve içerik yüzeyinin zaten yeterli olduğuna ilişkin kanıta dayalı, kasıtlı bir sınırlamadır. Tek acil operasyon, var olan Hive Due / Site Hesap ortak artifact'ının canlıya doğru alias'larla yayınlanmasıdır. The Cosmic Meta'nın canlıdaki eski `llms.txt` çıktısı ise yalnızca doğrulanmış WordPress/hosting sahipliği üzerinden düzeltilebilir veya kaldırılabilir.
