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
    subparsers = parser.add_subparsers(dest="command", help="Komutlar: check, generate, tax-office, batch")

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

    # Batch verification
    batch_parser = subparsers.add_parser("batch", help="Dosyadan toplu VKN/TCKN doğrular")
    batch_parser.add_argument("file", help="İçinde her satırda bir numara olan txt/csv dosya yolu")
    batch_parser.add_argument("--output", "-o", help="Doğrulama sonuçlarını CSV olarak kaydetme yolu")

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

    if args.command == "batch":
        import csv
        try:
            with open(args.file, "r", encoding="utf-8", errors="ignore") as f:
                lines = [line.strip().strip('"\',') for line in f if line.strip()]
        except Exception as e:
            print(f"❌ Dosya okunamadı: {e}")
            sys.exit(1)

        print("\n" + "=" * 60)
        print(f"📋 TOPLU VKN / TCKN DOĞRULAMA ({len(lines)} kayıt)")
        print("=" * 60)
        valid_cnt, invalid_cnt = 0, 0
        records = []
        for idx, line in enumerate(lines, 1):
            val = line.split(",")[0].strip().split(";")[0].strip()
            res = validate_identity(val)
            if res.is_valid:
                valid_cnt += 1
                status = f"✅ {res.identity_type} Geçerli"
            else:
                invalid_cnt += 1
                status = f"❌ Geçersiz: {res.error_message or 'Hatalı'}"
            records.append((val, res.identity_type or "Bilinmeyen", res.is_valid, res.error_message or ""))
            if idx <= 15 or not res.is_valid:
                print(f"  [{idx:3}] {val:15} -> {status}")
        if len(lines) > 15:
            print(f"  ... ve {len(lines) - 15} kayıt daha doğrulandı.")

        print("-" * 60)
        print(f"ÖZET: Toplam {len(lines)} | ✅ Geçerli: {valid_cnt} | ❌ Geçersiz: {invalid_cnt}")
        print("=" * 60)

        if args.output:
            try:
                with open(args.output, "w", encoding="utf-8", newline="") as out_f:
                    writer = csv.writer(out_f)
                    writer.writerow(["Numara", "Tur", "GecerliMi", "HataMesaji"])
                    for r in records:
                        writer.writerow([r[0], r[1], "Evet" if r[2] else "Hayir", r[3]])
                print(f"💾 Sonuçlar kaydedildi: {args.output}")
            except Exception as e:
                print(f"❌ CSV kaydetme hatası: {e}")
        return

    parser.print_help()

if __name__ == "__main__":
    main()
