# Prompt kartları — Repo keşfi (1. Gün)

**Amaç:** Agentic loop'u gözlemlemek: bağlam topla → tool kullan → sonuçları yorumla → kanıtı raporla.  
**Kural:** Bu bölüm **salt okunur**dur. Mümkün olan yerde Claude Code'un planlama / salt okunur modunda çalış, istenen izinleri incele, düzenlemeye ya da yıkıcı komutlara izin verme. Prompt tek başına erişim kısıtı uygulamaz.

## Prompt 01 — Kod tabanının haritasını çıkar (09:30–10:45 demo)

```text
OpsDesk reposunu hiçbir dosyayı düzenlemeden incele.
1. Projenin amacını ve ana klasörlerini açıkla.
2. Incident ve Task modellerini ve alanlarını bul.
3. GET /incidents endpoint'ini bul ve şu anki davranışını izle.
4. Mevcut API davranışını koruyan testleri belirle.
5. Her iddia için tam dosya yolunu ve ilgili fonksiyon adını ver.
6. Doğrulanmış gözlemleri varsayımlardan ayır.
Şunları yapma: bağımlılık kurmak, dosya düzenlemek, commit ya da push etmek.
```

**Gözlemle:** hangi dosyalar okundu; agent okumadan önce arama yaptı mı; iddialar gerçek dosya yollarına dayanıyor mu; herhangi bir düzenleme istendi mi. Yalnızca son metni değil, tool işlemlerini kaydet.

## Prompt 02 — Bilinçli test hatalarını açıkla

Önce komutları repo kökünden kendin çalıştır:

```bash
pytest -q -m 'not ops101'
pytest -q -m ops101
```

Sonra **gerçek komut çıktısını** ver ya da agent'tan, onaylanmamış komut çalıştırmadan mevcut test kodunu incelemesini iste.

```text
tests/test_ops101.py dosyasını GET /incidents endpoint'iyle birlikte analiz et.
Her OPS-101 kabul testi için şunları belirle:
- amaçlanan davranış,
- şu an gözlemlenen ya da koddan statik olarak çıkarılan davranış,
- hatanın olası nedeni,
- bundan sonra incelenecek kaynak dosya(lar).
Hiçbir dosyayı değiştirme, testleri gevşetme.
Benim verdiğim test çıktısını, kaynaktan çıkardığın sonuçlardan ayır.
```

**Dokunulmamış başlangıçta beklenen:** 7 baseline testi geçer. OPS-101'de 4 test kalır (critical, high, eşleşme yok, geçersiz severity), 1 test geçer (filtre yok).

## Prompt 03 — Uygulama değil, etki analizi (11:00–12:30)

```text
docs/OPS-101.md dosyasını oku ve ilgili endpoint'i, modelleri, şemaları
ve testleri incele. Bütün kabul kriterlerini karşılayan en küçük
uygulama planını öner.
Planlanan her değişiklik için şunları yaz:
- tam dosya / fonksiyon,
- gereken davranış,
- neden gerekli olduğu,
- mevcut sözleşmelere riski,
- nasıl doğrulanacağı.
Kaynak ve test dosyalarını değiştirme. Planı onaya sunduktan sonra dur.
```

**İnceleme soruları:** Plan desteklenen severity değerlerini doğruluyor mu? Filtresiz listelemeyi koruyor mu? Desteklenmeyen değerler için 422 döndürüyor mu? Filtreyi sorguda mı uyguluyor? Sıralamayı koruyor mu? Testlere dokunmuyor mu?

## Eğitmen eşliğinde karşılaştırma

Muğlak bir prompt ("Endpoint'i düzelt") ile yukarıdaki yapılandırılmış prompt'un çıktıları yan yana gösterilir. Tartışılacak soru hangi cevabın daha emin konuştuğu değil, hangisinin daha iyi **doğrulanabilir kanıt** ürettiğidir.

## Kaydedilecek kanıt

- Agent'ın kullandığı tool'ların listesi (arayüzden ya da oturum kaydından).
- İncelenen dosya yolları.
- En az bir hatalı varsayım ya da belirsizlik ve nasıl çözüldüğü.
- Önerilen değişiklik listesi; bu etkinlikte kaynak dosyalar **değiştirilmez**.
- Dokunulmamış bir daldan başlandıysa temiz çalışma kopyası için `git diff --exit-code`.
