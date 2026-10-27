# -*- coding: utf-8 -*-
"""
Test ve Sandbox İçin Matematiksel Olarak Geçerli VKN ve TCKN Üreticisi
"""

import random
from .validator import validate_vkn, validate_tckn

def generate_valid_vkn() -> str:
    """
    Test sistemlerinde kullanılmak üzere geçerli 10 haneli VKN üretir.
    """
    while True:
        # Rastgele 9 hane üret
        digits = [random.randint(0, 9) for _ in range(9)]
        v_sum = 0
        for i in range(9):
            v1 = (digits[i] + (9 - i)) % 10
            if v1 != 0:
                v2 = (v1 * (2 ** (9 - i))) % 9
                v_sum += 9 if v2 == 0 else v2
            else:
                v_sum += 0

        check_digit = (10 - (v_sum % 10)) % 10
        digits.append(check_digit)
        vkn = "".join(str(d) for d in digits)
        if validate_vkn(vkn):
            return vkn

def generate_valid_tckn() -> str:
    """
    Test sistemlerinde kullanılmak üzere geçerli 11 haneli TCKN üretir.
    """
    while True:
        digits = [random.randint(1, 9)]  # İlk hane 0 olamaz
        digits.extend([random.randint(0, 9) for _ in range(8)])

        odd_sum = digits[0] + digits[2] + digits[4] + digits[6] + digits[8]
        even_sum = digits[1] + digits[3] + digits[5] + digits[7]

        d10 = ((odd_sum * 7) - even_sum) % 10
        digits.append(d10)

        d11 = sum(digits[:10]) % 10
        digits.append(d11)

        tckn = "".join(str(d) for d in digits)
        if validate_tckn(tckn):
            return tckn
