#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Патч: «Один разговор на человека» поднимается сразу под «Лицом к лицу».

БЫЛО:  наушники -> лицом к лицу -> саммари -> фото/PDF -> история
СТАЛО: наушники -> лицом к лицу -> история -> саммари -> фото/PDF

Смысл: после разговора лицом к лицу логично сразу показать, что он
сохранился в ту же ветку. Чередование сторон (flip) пересчитано,
иначе два скриншота встали бы подряд с одной стороны.

ЗАПУСК из папки gen/:  python3 patch_rows_order.py
"""
import io, os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "build_site.py")
if not os.path.exists(SRC):
    sys.exit("build_site.py не найден — запускайте из gen/")

s = io.open(SRC, encoding="utf-8").read()
if "HISTORY_ROW" not in s:
    sys.exit("Сначала нужен patch_history_feature.py")

OLD = ('    rows = (row(f[2],"settings",False) + row(f[1],"face",True) +\n'
       '        row(f[5],"summary",False) + row(f[3],"photo",True) +\n'
       '        row(f[4],"history",False,x["free_badge"]))')

NEW = ('    rows = (row(f[2],"settings",False) + row(f[1],"face",True) +\n'
       '        row(f[4],"history",False,x["free_badge"]) +\n'
       '        row(f[5],"summary",True) + row(f[3],"photo",False))')

if OLD not in s:
    if NEW in s:
        sys.exit("Патч уже применён.")
    sys.exit("Не нашёл блок rows — генератор изменился.")

shutil.copyfile(SRC, SRC + ".order.bak")
io.open(SRC, "w", encoding="utf-8").write(s.replace(OLD, NEW))
print("порядок рядов изменён. Копия: build_site.py.order.bak")
print("Дальше из корня: python3 gen/build_site.py")
