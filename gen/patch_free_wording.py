#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Патч: уточнение по бесплатности в блоке «Один разговор на человека».

ЧТО НЕ ТАК. Абзац описывает и «Продолжить этот разговор» (новые переводы,
а они после триала требуют Pro), и бесплатные вещи. Финальное «Всё это
бесплатно, всегда» плюс зелёный бейдж читались как «приложение бесплатное» —
обещание, которого продукт не держит.

ЧТО ДЕЛАЕТ:
  * убирает зелёный бейдж у этого ряда
  * заменяет последнюю фразу на перечисление поимённо, на 6 языках

ЗАПУСК из папки gen/:  python3 patch_free_wording.py
"""

REPL = {'en': ('All of this is free, always.', 'Translation history, searching it, exporting and copying never require a subscription — not now, not later.'), 'ru': ('Всё это бесплатно, всегда.', 'История переводов, поиск по ней, экспорт и копирование не требуют подписки — ни сейчас, ни потом.'), 'uk': ('Усе це безкоштовно, завжди.', 'Історія перекладів, пошук по ній, експорт і копіювання не потребують підписки — ні зараз, ні потім.'), 'fr': ('Tout cela est gratuit, toujours.', "L'historique des traductions, la recherche, l'export et la copie ne nécessitent jamais d'abonnement — ni maintenant, ni plus tard."), 'es': ('Todo esto es gratis, siempre.', 'El historial de traducciones, su búsqueda, la exportación y la copia nunca requieren suscripción: ni ahora, ni después.'), 'de': ('All das ist kostenlos, immer.', 'Der Übersetzungsverlauf, die Suche darin, Export und Kopieren erfordern nie ein Abo — weder jetzt noch später.')}

import io, os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(HERE, "strings_base.py")
BS = os.path.join(HERE, "build_site.py")
for p in (SB, BS):
    if not os.path.exists(p):
        sys.exit("не найден " + os.path.basename(p) + " — запускайте из gen/")

sb = io.open(SB, encoding="utf-8").read()
bs = io.open(BS, encoding="utf-8").read()
if "HISTORY_ROW" not in bs:
    sys.exit("Сначала нужен patch_history_feature.py")
if 'row(f[4],"history",False)' in bs:
    sys.exit("Патч уже применён.")

shutil.copyfile(SB, SB + ".free.bak")
shutil.copyfile(BS, BS + ".free.bak")

missing = []
for code, (old, new) in REPL.items():
    if old not in sb:
        missing.append(code)
        continue
    sb = sb.replace(old, new, 1)
if missing:
    sys.exit("не нашёл старую фразу для: " + ", ".join(missing))
io.open(SB, "w", encoding="utf-8").write(sb)

# бейдж у ряда истории убираем
old_row = 'row(f[4],"history",False,x["free_badge"])'
new_row = 'row(f[4],"history",False)'
if old_row not in bs:
    sys.exit("не нашёл вызов row() для истории")
bs = bs.replace(old_row, new_row, 1)
io.open(BS, "w", encoding="utf-8").write(bs)

print("готово. Копии: *.free.bak")
print("Дальше из корня: python3 gen/build_site.py")
