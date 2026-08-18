#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Патч: текст в рядах фич выравнивается по верху, а не по центру.

ПОЧЕМУ. У .row стоит align-items:center, поэтому текст центрируется по
высоте всего ряда. Высоту задаёт картинка телефона, а на скриншотах
содержимое собрано вверху и ниже идёт пустая чёрная область — из-за
этого текст оказывается напротив пустоты и выглядит «провалившимся».

ЧТО ДЕЛАЕТ: align-items:center -> align-items:start у .row.
На узких экранах ряд и так одноколоночный, там ничего не меняется.

ЗАПУСК из папки gen/:  python3 patch_row_align.py
"""
import io, os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "build_site.py")
if not os.path.exists(SRC):
    sys.exit("build_site.py не найден — запускайте из gen/")

s = io.open(SRC, encoding="utf-8").read()

OLD = ".row{display:grid;grid-template-columns:1fr auto;gap:36px;align-items:center;"
NEW = ".row{display:grid;grid-template-columns:1fr auto;gap:36px;align-items:start;"

if OLD not in s:
    if NEW in s:
        sys.exit("Патч уже применён.")
    sys.exit("Не нашёл правило .row — генератор изменился.")

shutil.copyfile(SRC, SRC + ".align.bak")
io.open(SRC, "w", encoding="utf-8").write(s.replace(OLD, NEW, 1))
print("выравнивание рядов изменено на верх. Копия: build_site.py.align.bak")
print("Дальше из корня: python3 gen/build_site.py")
