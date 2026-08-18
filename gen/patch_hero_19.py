#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Патч: «19 языков» в первый абзац первого экрана.

ПОЧЕМУ. Число 19 появлялось только после долгой прокрутки, а первый
экран о количестве языков молчал. Переключатель вверху показывает
6 языков — языков САЙТА, — и человек может решить, что это и есть
весь список. Главный аргумент был спрятан.

ЧТО ДЕЛАЕТ: добавляет «на 19 языках» в hero_lead на 6 языках.

ЗАПУСК из папки gen/:  python3 patch_hero_19.py
"""

REPL = {'en': ('Prau recognizes, translates and speaks — entirely on your iPhone.', 'Prau recognizes, translates and speaks in 19 languages — entirely on your iPhone.'), 'ru': ('Prau распознаёт, переводит и озвучивает — целиком на вашем iPhone.', 'Prau распознаёт, переводит и озвучивает на 19 языках — целиком на вашем iPhone.'), 'uk': ('Prau розпізнає, перекладає й озвучує — повністю на вашому iPhone.', 'Prau розпізнає, перекладає й озвучує 19 мовами — повністю на вашому iPhone.'), 'fr': ('Prau reconnaît, traduit et parle — entièrement sur votre iPhone.', 'Prau reconnaît, traduit et parle en 19 langues — entièrement sur votre iPhone.'), 'es': ('Prau reconoce, traduce y habla, por completo en tu iPhone.', 'Prau reconoce, traduce y habla en 19 idiomas, por completo en tu iPhone.'), 'de': ('Prau erkennt, übersetzt und spricht – vollständig auf deinem iPhone.', 'Prau erkennt, übersetzt und spricht in 19 Sprachen – vollständig auf deinem iPhone.')}

import io, os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(HERE, "strings_base.py")
if not os.path.exists(SB):
    sys.exit("strings_base.py не найден — запускайте из gen/")

sb = io.open(SB, encoding="utf-8").read()

done = [c for c, (o, n) in REPL.items() if n in sb]
if done:
    sys.exit("Патч уже применён для: " + ", ".join(done))

shutil.copyfile(SB, SB + ".hero19.bak")

missing = []
for code, (old, new) in REPL.items():
    if old not in sb:
        missing.append(code)
        continue
    sb = sb.replace(old, new, 1)
if missing:
    sys.exit("не нашёл hero_lead для: " + ", ".join(missing))

io.open(SB, "w", encoding="utf-8").write(sb)
print("готово. Копия: strings_base.py.hero19.bak")
print("Дальше из корня: python3 gen/build_site.py")
