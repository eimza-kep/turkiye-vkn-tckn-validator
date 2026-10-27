# -*- coding: utf-8 -*-
"""
Türkiye Vergi Kimlik Numarası (VKN) ve T.C. Kimlik Numarası (TCKN) Doğrulayıcı
"""

__version__ = "1.0.0"
__author__ = "eimza-kep"

from .validator import validate_vkn, validate_tckn, validate_identity, ValidationResult
from .generator import generate_valid_vkn, generate_valid_tckn
from .tax_offices import TAX_OFFICES, search_tax_office

__all__ = [
    "validate_vkn",
    "validate_tckn",
    "validate_identity",
    "ValidationResult",
    "generate_valid_vkn",
    "generate_valid_tckn",
    "TAX_OFFICES",
    "search_tax_office"
]
