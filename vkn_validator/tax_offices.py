# -*- coding: utf-8 -*-
"""
Türkiye Vergi Dairesi Kodları ve Sorgulama Modülü
"""

from typing import List, Dict, Optional

# Popüler ve İl Bazlı Vergi Dairesi Kod Listesi
TAX_OFFICES = {
    "006205": {"city": "Ankara", "name": "Çankaya Vergi Dairesi Müdürlüğü"},
    "006206": {"city": "Ankara", "name": "Kavaklıdere Vergi Dairesi Müdürlüğü"},
    "006207": {"city": "Ankara", "name": "Ulus Vergi Dairesi Müdürlüğü"},
    "006208": {"city": "Ankara", "name": "Yenimahalle Vergi Dairesi Müdürlüğü"},
    "006209": {"city": "Ankara", "name": "Ostim Vergi Dairesi Müdürlüğü"},
    "034251": {"city": "İstanbul", "name": "Boğaziçi Kurumlar Vergi Dairesi"},
    "034252": {"city": "İstanbul", "name": "Marmara Kurumlar Vergi Dairesi"},
    "034253": {"city": "İstanbul", "name": "Büyük Mükellefler Vergi Dairesi"},
    "034255": {"city": "İstanbul", "name": "Maslak Vergi Dairesi Müdürlüğü"},
    "034256": {"city": "İstanbul", "name": "Beşiktaş Vergi Dairesi Müdürlüğü"},
    "034257": {"city": "İstanbul", "name": "Beyoğlu Vergi Dairesi Müdürlüğü"},
    "034258": {"city": "İstanbul", "name": "Şişli Vergi Dairesi Müdürlüğü"},
    "034260": {"city": "İstanbul", "name": "Kadıköy Vergi Dairesi Müdürlüğü"},
    "034262": {"city": "İstanbul", "name": "Üsküdar Vergi Dairesi Müdürlüğü"},
    "034265": {"city": "İstanbul", "name": "Bakırköy Vergi Dairesi Müdürlüğü"},
    "034268": {"city": "İstanbul", "name": "İkitelli Vergi Dairesi Müdürlüğü"},
    "035251": {"city": "İzmir", "name": "Konak Vergi Dairesi Müdürlüğü"},
    "035252": {"city": "İzmir", "name": "Bornova Vergi Dairesi Müdürlüğü"},
    "035253": {"city": "İzmir", "name": "Karşıyaka Vergi Dairesi Müdürlüğü"},
    "016251": {"city": "Bursa", "name": "Osmangazi Vergi Dairesi Müdürlüğü"},
    "016252": {"city": "Bursa", "name": "Nilüfer Vergi Dairesi Müdürlüğü"},
    "007251": {"city": "Antalya", "name": "Muratpaşa Vergi Dairesi Müdürlüğü"},
    "041251": {"city": "Kocaeli", "name": "İzmit Vergi Dairesi Müdürlüğü"},
    "041252": {"city": "Kocaeli", "name": "Gebze Vergi Dairesi Müdürlüğü"}
}

def search_tax_office(query: str) -> List[Dict[str, str]]:
    """
    Vergi dairesi adı veya koduna göre arama yapar.
    """
    q = query.lower().strip()
    results = []
    for code, info in TAX_OFFICES.items():
        if q in code or q in info["name"].lower() or q in info["city"].lower():
            results.append({"code": code, "city": info["city"], "name": info["name"]})
    return results
