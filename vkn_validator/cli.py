# -*- coding: utf-8 -*-
"""
VKN & TCKN Doğrulayıcı CLI Aracı
"""

import sys
import argparse
from .validator import validate_identity
from .generator import generate_valid_vkn, generate_valid_tckn
from .tax_offices import search_tax_office

def main():
    parser = argparse.ArgumentParser(
        description="Türkiye VKN (Vergi Kimlik No) ve TCKN Algoritmik Doğrulayıcı"
    )
    subparsers = parser.add_subparsers(dest="command", help="Komutlar: check, generate, tax-office")

    # Check
    check_parser = subparsers.add_parser("check", help="VKN veya TCKN doğrular")
    check_parser.add_argument("number", help="Doğrulanacak 10 haneli VKN veya 11 haneli TCKN")

    # Generate
    gen_parser = subparsers.add_parser("generate", help="Test için geçerli numara üretir")
    gen_parser.add_argument("--type", choices=["vkn", "tckn"], default="vkn", help="Numara türü")
    gen_parser.add_argument("--count", type=int, default=1, help="Üretilecek adet")

    # Tax office
    tax_parser = subparsers.add_parser("tax-office", help="Vergi dairesi kodu veya ismi arar")
    tax_parser.add_argument("query", help="Arama terimi (örn: Maslak veya 034255)")

    args = parser.parse_args()

    if args.command == "check":
        res = validate_identity(args.number)
        print("\n" + "=" * 50)
        print("🔍 KİMLİK / VERGİ NUMARASI DOĞRULAMA")
        print("=" * 50)
        print(f"Girdi: {res.value}")
        print(f"Tür: {res.identity_type}")
        print(f"Sonuç: {'✅ GEÇERLİ' if res.is_valid else '❌ GEÇERSİZ'}")
        if res.error_message:
            print(f"Hata: {res.error_message}")
        print("=" * 50)
        sys.exit(0 if res.is_valid else 1)

    if args.command == "generate":
        print(f"\n🎲 Test İçin Üretilen Geçerli {args.type.upper()} Numaraları:")
        for i in range(args.count):
            num = generate_valid_vkn() if args.type == "vkn" else generate_valid_tckn()
            print(f"  [{i+1}] {num}")
        return

    if args.command == "tax-office":
        results = search_tax_office(args.query)
        print(f"\n🏛️ '{args.query}' ile Eşleşen Vergi Daireleri ({len(results)} adet):")
        for r in results:
            print(f"  • Kod: {r['code']} | {r['city']} - {r['name']}")
        return

    parser.print_help()

if __name__ == "__main__":
    main()
