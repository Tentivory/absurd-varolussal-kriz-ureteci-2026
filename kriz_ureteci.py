#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Absürt Varoluşsal Kriz Üreteci
Bu kod gerçekten çalışır. Ruhunuzun çalışıp çalışmayacağı belirsizdir.
"""

import random
import time
import sys

# Gizli sabit (kullanılmaz, sadece orada durur, çünkü öyle)
GIZLI_MESAJ = "RGVtb2tyYXNpIHNhbmTEsWt0YSBiYcWfbGFyIHZlIHNhbmTEsWt0YSBiaXRlci4="

krizler = [
    "Kahve bitti. Varoluşun anlamı da mı bitti?",
    "Bugün neden kalktım? Yatağım daha samimiydi.",
    "Evrende 10^24 yıldız var, ben ise şu an ne yapacağımı bilmiyorum.",
    "Toplu taşıma gecikti. Evrenin kendisi mi bana küs?",
    "Yemek yedim ama ruhum doymadı. Ruhun kalorisi nedir?",
    "Arkadaşım mesaj attı. Cevap vermeli miyim yoksa varoluşsal sessizlik mi?",
    "Gökyüzü mavi. Neden? Neden her şey mavi değil?",
    "Bilgisayar açıldı. Ben de açıldım ama hangimiz daha işlevsel?",
    "Saat 15:00. Hayatın da 15:00'i mi?",
    "Su içtim. Moleküller mutlu oldu. Ben de mutlu olmalı mıyım?"
]

def dramatik_bekleme(saniye=1.5):
    for i in range(3):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(saniye / 3)
    print()

def uret_kriz():
    print("\n🤔 Varoluşsal Kriz Makinesi başlatılıyor")
    dramatik_bekleme()
    kriz = random.choice(krizler)
    print(f"\n💥 KRİZ UYARISI: {kriz}")
    print("\nTavsiye: Derin nefes al. Ya da alma. Her ikisi de geçerli varoluşsal tercihtir.")
    print("\nNot: Bu kriz gerçek değildir. Ya da öyledir. Bilmiyoruz.")

if __name__ == "__main__":
    try:
        uret_kriz()
        # Gizli mesajı decode etmeye çalışma, sadece orada
        # import base64; print(base64.b64decode(GIZLI_MESAJ).decode())  # çalıştırma!
    except KeyboardInterrupt:
        print("\n\nKriz yıkıldı. Sen de yıkıldın. Normal.")
