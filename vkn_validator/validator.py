# -*- coding: utf-8 -*-
"""
VKN (10 hane) ve TCKN (11 hane) Algoritmik Doğrulama Motoru
"""

from dataclasses import dataclass
from typing import Optional

@dataclass
class ValidationResult:
    is_valid: bool
    identity_type: str  # 'VKN', 'TCKN', 'INVALID'
    value: str
    error_message: Optional[str] = None


def validate_vkn(vkn_str: str) -> bool:
    """
    Türkiye Vergi Kimlik Numarası (VKN) Doğrulama Algoritması:
    - 10 hanelidir.
    - Sadece rakamlardan oluşur.
    - İlk 9 hane üzerinde katsayı ve modül 9/10 fonksiyonu uygulanarak 10. kontrol hanesi teyit edilir.
    """
    vkn = str(vkn_str).strip()
    if len(vkn) != 10 or not vkn.isdigit():
        return False

    digits = [int(ch) for ch in vkn]
    v_sum = 0

    for i in range(9):
        # 1. Adım: (Hane + (9 - i)) mod 10
        v1 = (digits[i] + (9 - i)) % 10
        if v1 != 0:
            # 2. Adım: (v1 * 2^(9-i)) mod 9 (eğer sonuç 0 ise 9 alınır)
            v2 = (v1 * (2 ** (9 - i))) % 9
            v_sum += 9 if v2 == 0 else v2
        else:
            v_sum += 0

    # 3. Adım: Kontrol hanesi hesabı: (10 - (toplam mod 10)) mod 10
    check_digit = (10 - (v_sum % 10)) % 10
    return check_digit == digits[9]


def validate_tckn(tckn_str: str) -> bool:
    """
    Türkiye Cumhuriyeti Kimlik Numarası (TCKN) Doğrulama Algoritması:
    - 11 hanelidir.
    - Sadece rakamlardan oluşur ve ilk hane '0' olamaz.
    - 10. hane: ((1, 3, 5, 7, 9. hanelerin toplamı * 7) - (2, 4, 6, 8. hanelerin toplamı)) mod 10
    - 11. hane: İlk 10 hanenin toplamının mod 10'u
    """
    tckn = str(tckn_str).strip()
    if len(tckn) != 11 or not tckn.isdigit():
        return False

    if tckn[0] == "0":
        return False

    digits = [int(ch) for ch in tckn]

    odd_sum = digits[0] + digits[2] + digits[4] + digits[6] + digits[8]
    even_sum = digits[1] + digits[3] + digits[5] + digits[7]

    digit_10 = ((odd_sum * 7) - even_sum) % 10
    if digit_10 != digits[9]:
        return False

    total_10_sum = sum(digits[:10])
    digit_11 = total_10_sum % 10
    if digit_11 != digits[10]:
        return False

    return True


def validate_identity(ident_str: str) -> ValidationResult:
    """
    Verilen kimlik numarasını otomatik olarak VKN veya TCKN tespit ederek doğrular.
    """
    val = str(ident_str).strip()
    if len(val) == 10:
        is_ok = validate_vkn(val)
        return ValidationResult(
            is_valid=is_ok,
            identity_type="VKN",
            value=val,
            error_message=None if is_ok else "Geçersiz Vergi Kimlik Numarası (Algoritma kontrol hanesi uyuşmuyor)."
        )
    elif len(val) == 11:
        is_ok = validate_tckn(val)
        return ValidationResult(
            is_valid=is_ok,
            identity_type="TCKN",
            value=val,
            error_message=None if is_ok else "Geçersiz T.C. Kimlik Numarası (Nüfus algoritma kurallarına uymuyor)."
        )
    else:
        return ValidationResult(
            is_valid=False,
            identity_type="INVALID",
            value=val,
            error_message=f"Numara 10 hane (VKN) veya 11 hane (TCKN) olmalıdır. Girilen uzunluk: {len(val)}"
        )
