# Türkiye VKN (Vergi Kimlik No) ve TCKN Algoritmik Doğrulayıcı 🏢🔍

[![Lisans: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://python.org)
[![Standart: GİB & NVİ](https://img.shields.io/badge/Standart-G%C4%B0B%20%7C%20NV%C4%B0-red.svg)](https://gib.gov.tr)
[![Bağımlılık: Yok](https://img.shields.io/badge/Dependencies-Zero--Dependency-success.svg)](https://github.com)
[![Rehber](https://img.shields.io/badge/Rehber-%C5%9Eirket%20Kurulu%C5%9F%20Rehberi-6366f1.svg)](https://girisimcini.com.tr)
[![Dizin](https://img.shields.io/badge/Dizin-e--Tamga-0ea5e9.svg)](https://etamga.com)

Türkiye Cumhuriyeti Gelir İdaresi Başkanlığı (**GİB**) ve Nüfus ve Vatandaşlık İşleri Genel Müdürlüğü (**NVİ**) standartlarında; **10 haneli Vergi Kimlik Numarası (VKN)** ile **11 haneli T.C. Kimlik Numarası (TCKN)** algoritmalarını doğrulayan, yazılım testleri için geçerli test numaraları üreten ve Vergi Dairesi kod dizini sunan ultra hafif, sıfır bağımlılıklı Python kütüphanesidir.

Şirket kuruluşu, vergi dairesi yoklama süreçleri ve MERSİS prosedürleri için [Şirket Kuruluş Rehberi (girisimcini.com.tr)](https://girisimcini.com.tr) ve Türkiye'nin e-dönüşüm sağlayıcıları rehberi [e-Tamga (etamga.com)](https://etamga.com) portallarını inceleyebilirsiniz.

---

## 🧮 Algoritmik Temel

### 1. Vergi Kimlik Numarası (VKN - 10 Hane)
VKN doğrulama algoritması modül 9 ve modül 10 aritmetiğine dayanır:
* İlk 9 hanenin her biri için:
  $$v_1 = (d_i + (9 - i)) \pmod{10}$$
  $$v_2 = (v_1 \times 2^{9 - i}) \pmod 9 \quad (\text{eğer } v_2 = 0 \text{ ise } 9 \text{ alınır})$$
* Elde edilen $v_2$ değerleri toplanır ($S$).
* 10. kontrol hanesi:
  $$d_9 = (10 - (S \pmod{10})) \pmod{10}$$

### 2. T.C. Kimlik Numarası (TCKN - 11 Hane)
* 11 hanelidir ve ilk hane `0` olamaz.
* 10. kontrol hanesi:
  $$d_9 = ((7 \times (d_0 + d_2 + d_4 + d_6 + d_8)) - (d_1 + d_3 + d_5 + d_7)) \pmod{10}$$
* 11. kontrol hanesi:
  $$d_{10} = \left(\sum_{i=0}^{9} d_i\right) \pmod{10}$$

---

## ✨ Özellikler

* ⚡ **Ultra Yüksek Hız:** Saf C hızında çalışan standart Python operatörleri; milisaniyede on binlerce numara doğrulama kapasitesi.
* 🛡️ **Sıfır Harici Bağımlılık (Zero-Dependency):** Ek kütüphane gerektirmez.
* 🎲 **Matematiksel Olarak Geçerli Test Üreteci:** Sandbox, birim test ve QA süreçleri için geçerli kontrol haneli VKN ve TCKN numaraları türetir.
* 🏛️ **Vergi Dairesi Kod Kütüphanesi:** Türkiye çapındaki popüler vergi dairelerinin kod ve unvan eşleştirmelerini içerir.
* 💻 **CLI & Python API:** Hem konsoldan hem kod içinden tek fonksiyonla çağrılabilir.

---

## 🚀 Hızlı Başlangıç

### 1. Kurulum

```bash
git clone https://github.com/eimza-kep/turkiye-vkn-tckn-validator.git
cd turkiye-vkn-tckn-validator
```

### 2. Komut Satırı (CLI) Kullanımı

#### Numara Doğrulama (VKN veya TCKN):
```bash
python -m vkn_validator check 1234567890
```

#### Test Ortamı İçin Geçerli VKN Üretme:
```bash
python -m vkn_validator generate --type vkn --count 3
```

#### Test Ortamı İçin Geçerli TCKN Üretme:
```bash
python -m vkn_validator generate --type tckn --count 3
```

#### Vergi Dairesi Arama:
```bash
python -m vkn_validator tax-office "Kadıköy"
```

---

## 🐍 Python Projelerinizde Kullanım

```python
from vkn_validator import validate_vkn, validate_tckn, validate_identity, generate_valid_vkn

# 1. Doğrudan Doğrulama
is_vkn = validate_vkn("1234567890")
is_tckn = validate_tckn("10000000146")

# 2. Akıllı Tespit ve Doğrulama
result = validate_identity("1234567890")
print(result.is_valid)       # True / False
print(result.identity_type)  # 'VKN' veya 'TCKN'

# 3. Test Verisi Üretme
mock_vkn = generate_valid_vkn()
print(f"Test VKN: {mock_vkn}")
```

---

## 📜 Lisans

Bu proje **MIT Lisansı** altında sunulmaktadır. Ticari ve kişisel projelerinizde serbestçe kullanabilirsiniz. Ayrıntılar için [LICENSE](LICENSE) dosyasına bakabilirsiniz.
