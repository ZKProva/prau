#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ПАТЧ gen/build_site.py: кнопка «Скоро в App Store» вместо мёртвой ссылки.

Ссылка https://apps.apple.com/app/id6801931802 отдаёт 404 — приложение
ещё на ревью. Пока LIVE = False:
  * кнопка загрузки — некликабельный элемент (никаких 404)
  * подпись под ней переписана на «скоро», требование iOS сохранено
  * кнопка App Store в шапке скрыта
  * снят Smart App Banner (apple-itunes-app) — вести некуда

ПОСЛЕ ОДОБРЕНИЯ APPLE: в gen/build_site.py поменять LIVE = False на True,
пересобрать (python3 gen/build_site.py) и запушить. Больше ничего.

ЗАПУСК из папки gen/:  python3 patch_cta_soon.py
"""

BLOCK = 'LIVE = False   # False = приложение ещё не в App Store: кнопка «скоро», без ссылки.\n               # После одобрения Apple поставить True, пересобрать, запушить.\n\nSOON = {\n "en": ("Coming to the App Store", "Launching soon \\u00b7 iOS 18 or later"),\n "ru": ("\\u0421\\u043a\\u043e\\u0440\\u043e \\u0432 App Store", "\\u0417\\u0430\\u043f\\u0443\\u0441\\u043a \\u0441\\u043e\\u0432\\u0441\\u0435\\u043c \\u0441\\u043a\\u043e\\u0440\\u043e \\u00b7 iOS 18 \\u0438 \\u043d\\u043e\\u0432\\u0435\\u0435"),\n "uk": ("\\u041d\\u0435\\u0437\\u0430\\u0431\\u0430\\u0440\\u043e\\u043c \\u0432 App Store", "\\u0417\\u0430\\u043f\\u0443\\u0441\\u043a \\u043d\\u0435\\u0432\\u0434\\u043e\\u0432\\u0437\\u0456 \\u00b7 iOS 18 \\u0456 \\u043d\\u043e\\u0432\\u0456\\u0448\\u0435"),\n "fr": ("Bient\\u00f4t sur l\'App Store", "Lancement imminent \\u00b7 iOS 18 ou ult\\u00e9rieur"),\n "es": ("Pr\\u00f3ximamente en el App Store", "Lanzamiento muy pronto \\u00b7 iOS 18 o posterior"),\n "de": ("Bald im App Store", "Start in K\\u00fcrze \\u00b7 iOS 18 oder neuer"),\n}\n\n\ndef cta_block(code, d, extra=""):\n    """Кнопка загрузки. До релиза — некликабельный элемент, чтобы не вести в 404."""\n    cls = "cta cta2" if extra else "cta"\n    if LIVE:\n        btn = (\'<a class="btn" href="\' + APPSTORE + \'">\'\n               \'<span class="apple" aria-hidden="true"></span>\' + e(d["cta"]) + \'</a>\')\n        note = e(d["cta_note"])\n    else:\n        label, note_txt = SOON.get(code, SOON["en"])\n        btn = (\'<span class="btn soon" aria-disabled="true">\'\n               \'<span class="apple" aria-hidden="true"></span>\' + e(label) + \'</span>\')\n        note = e(note_txt)\n    return \'<p class="\' + cls + \'">\' + btn + \'<span class="ctan">\' + note + \'</span></p>\'\n\n'

import io, os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "build_site.py")
if not os.path.exists(SRC):
    sys.exit("build_site.py не найден — запускайте из папки gen/")

s = io.open(SRC, encoding="utf-8").read()
if "PAGES_BY_LANG" not in s:
    sys.exit("Сначала нужен патч i18n (patch_site_i18n.py).")
if "LIVE = False" in s or "LIVE = True" in s:
    sys.exit("Патч уже применён — в build_site.py есть флаг LIVE.")
shutil.copyfile(SRC, SRC + ".cta.bak")

REPL = [
 ("PAGES_BY_LANG = True", BLOCK + "PAGES_BY_LANG = True"),
 ('    <p class="cta"><a class="btn" href="{APPSTORE}"><span class="apple" aria-hidden="true"></span>{e(d["cta"])}</a><span class="ctan">{e(d["cta_note"])}</span></p>',
  "    {cta_block(code, d)}"),
 ('<p class="cta cta2"><a class="btn" href="{APPSTORE}"><span class="apple" aria-hidden="true"></span>{e(d["cta"])}</a><span class="ctan">{e(d["cta_note"])}</span></p>',
  '{cta_block(code, d, "2")}'),
 ("  .ctan{color:var(--muted);font-size:14px}",
  "  .ctan{color:var(--muted);font-size:14px}\n  .btn.soon{background:transparent;color:var(--gold);border:1px solid #4A3E29;cursor:default}\n  .btn.soon:hover{transform:none;filter:none}"),
 ('<meta name="apple-itunes-app" content="app-id=6801931802">', "{smart_banner}"),
 ('  <a class="navcta" href="{APPSTORE}">{e(x["nav_cta"])}</a>', "{navcta}"),
 ("    body = section(code, d, x, True)",
  '    body = section(code, d, x, True)\n'
  '    smart_banner = \'<meta name="apple-itunes-app" content="app-id=6801931802">\' if LIVE else ""\n'
  '    navcta = (\'  <a class="navcta" href="\' + APPSTORE + \'">\' + e(x["nav_cta"]) + \'</a>\') if LIVE else ""'),
]

for a, b in REPL:
    if a not in s:
        sys.exit("Фрагмент не найден: " + a[:60])
    s = s.replace(a, b)

io.open(SRC, "w", encoding="utf-8").write(s)
print("build_site.py пропатчен. Копия: build_site.py.cta.bak")
print("Дальше из корня репозитория: python3 gen/build_site.py")
