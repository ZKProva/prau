#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Патч: возвращает на сайт фичу «Один разговор на человека».

ЧТО СЛУЧИЛОСЬ. Правку внесли прямо в index.html, минуя генератор,
поэтому следующая сборка из strings_base.py её стёрла. Этот патч
кладёт тексты в strings_base.py и переносит историю из карточки
в полноценный ряд с картинкой — так она переживёт любую пересборку.

ПЕРЕД ЗАПУСКОМ положите img/history.png и img/history.webp из архива
prau_site_update.zip в папку prau/img/ — без них картинка не появится.

ЗАПУСК из папки gen/:  python3 patch_history_feature.py
"""
import io, os, shutil, sys

DATA = {'en': {'title': 'One conversation per person — voice, photos and PDFs together', 'badge': 'Free, always', 'text': 'Every conversation is saved on your iPhone. Swipe a conversation right to rename it — “Hotel in Lisbon”, “Landlord”. Open it and tap “Continue this conversation”: new speech, photos and PDF pages land in the same thread, so one counterpart means one record, one summary, one export. Search across everything, export any conversation to TXT or PDF. And in any card, press and hold to select and copy a single word or phrase. All of this is free, always.', 'alt': 'History: a conversation with the Rename action revealed by a right swipe'}, 'ru': {'title': 'Один разговор на человека — речь, фото и PDF вместе', 'badge': 'Бесплатно, всегда', 'text': 'Каждый разговор хранится на вашем iPhone. Свайп вправо по разговору — переименовать: «Отель в Лиссабоне», «Арендодатель». Откройте его и нажмите «Продолжить этот разговор» — новая речь, фото и страницы PDF лягут в ту же ветку: один контрагент — одна запись, одно краткое содержание, один экспорт. Поиск по всему, экспорт любого разговора в TXT или PDF. А в любой карточке — зажмите палец, чтобы выделить и скопировать отдельное слово или фразу. Всё это бесплатно, всегда.', 'alt': 'История: разговор с кнопкой «Переименовать», открытой свайпом вправо'}, 'uk': {'title': 'Одна розмова на людину — мовлення, фото та PDF разом', 'badge': 'Безкоштовно, завжди', 'text': 'Кожна розмова зберігається на вашому iPhone. Свайп праворуч по розмові — перейменувати: «Готель у Лісабоні», «Орендодавець». Відкрийте її та натисніть «Продовжити цю розмову» — нове мовлення, фото та сторінки PDF ляжуть у ту саму гілку: один контрагент — один запис, один короткий зміст, один експорт. Пошук по всьому, експорт будь-якої розмови в TXT або PDF. А в будь-якій картці — затисніть палець, щоб виділити й скопіювати окреме слово чи фразу. Усе це безкоштовно, завжди.', 'alt': 'Історія: розмова з кнопкою «Перейменувати», відкритою свайпом праворуч'}, 'fr': {'title': 'Une conversation par personne — voix, photos et PDF ensemble', 'badge': 'Gratuit, toujours', 'text': "Chaque conversation est conservée sur votre iPhone. Glissez une conversation vers la droite pour la renommer — « Hôtel à Lisbonne », « Propriétaire ». Ouvrez-la et touchez « Continuer cette conversation » : nouvelle parole, photos et pages PDF s'ajoutent au même fil — un interlocuteur, un dossier, un résumé, un export. Recherche dans tout, export de n'importe quelle conversation en TXT ou PDF. Et dans toute carte, appui long pour sélectionner et copier un mot ou une phrase. Tout cela est gratuit, toujours.", 'alt': "Historique : une conversation avec l'action Renommer révélée par un glissement vers la droite"}, 'es': {'title': 'Una conversación por persona: voz, fotos y PDF juntos', 'badge': 'Gratis, siempre', 'text': 'Cada conversación se guarda en tu iPhone. Desliza una conversación a la derecha para renombrarla: «Hotel en Lisboa», «Casero». Ábrela y toca «Continuar esta conversación»: la nueva voz, las fotos y las páginas PDF caen en el mismo hilo; un interlocutor, un registro, un resumen, una exportación. Busca en todo, exporta cualquier conversación a TXT o PDF. Y en cualquier tarjeta, mantén pulsado para seleccionar y copiar una sola palabra o frase. Todo esto es gratis, siempre.', 'alt': 'Historial: una conversación con la acción Renombrar mostrada al deslizar a la derecha'}, 'de': {'title': 'Ein Gespräch pro Person – Sprache, Fotos und PDFs zusammen', 'badge': 'Kostenlos, immer', 'text': 'Jedes Gespräch bleibt auf deinem iPhone. Wische ein Gespräch nach rechts, um es umzubenennen – „Hotel in Lissabon“, „Vermieter“. Öffne es und tippe auf „Dieses Gespräch fortsetzen“: neue Sprache, Fotos und PDF-Seiten landen im selben Faden – ein Gegenüber, ein Eintrag, eine Zusammenfassung, ein Export. Suche über alles, Export jedes Gesprächs als TXT oder PDF. Und in jeder Karte: gedrückt halten, um ein einzelnes Wort oder einen Satz zu markieren und zu kopieren. All das ist kostenlos, immer.', 'alt': 'Verlauf: ein Gespräch mit der durch Rechtswisch eingeblendeten Aktion „Umbenennen“'}}

HERE = os.path.dirname(os.path.abspath(__file__))
SB = os.path.join(HERE, "strings_base.py")
SN = os.path.join(HERE, "strings_new.py")
BS = os.path.join(HERE, "build_site.py")
for p in (SB, SN, BS):
    if not os.path.exists(p):
        sys.exit("не найден " + os.path.basename(p) + " — запускайте из gen/")

img = os.path.join(os.path.dirname(HERE), "img", "history.webp")
if not os.path.exists(img):
    sys.exit("нет img/history.webp — сначала распакуйте картинки из архива")

sb = io.open(SB, encoding="utf-8").read()
sn = io.open(SN, encoding="utf-8").read()
bs = io.open(BS, encoding="utf-8").read()
if "HISTORY_ROW" in bs:
    sys.exit("патч уже применён")
for p, t in ((SB, sb), (SN, sn), (BS, bs)):
    shutil.copyfile(p, p + ".hist.bak")

# 1. Тексты фичи f[4] — заменяем короткие на развёрнутые
import re
ns = {}
exec(sb, ns)
miss = []
for code, v in DATA.items():
    old_t = ns["L"][code]["feats"][4][1]
    old_p = ns["L"][code]["feats"][4][2]
    if old_t not in sb or old_p not in sb:
        miss.append(code)
        continue
    sb = sb.replace(repr(old_t), repr(v["title"]), 1) if repr(old_t) in sb else sb.replace(old_t, v["title"], 1)
    sb = sb.replace(repr(old_p), repr(v["text"]), 1) if repr(old_p) in sb else sb.replace(old_p, v["text"], 1)
if miss:
    sys.exit("не нашёл тексты f[4] для: " + ", ".join(miss))
io.open(SB, "w", encoding="utf-8").write(sb)

# 2. alt для картинки истории (alts объявлен как dict(main=..., ...))
ns2 = {}
exec(sn, ns2)
for code, v in DATA.items():
    if "history" in ns2["X"][code]["alts"]:
        continue
    main_val = ns2["X"][code]["alts"]["main"]
    anchor = None
    for quote in ('"', "'"):
        cand = "alts=dict(main=" + quote + main_val + quote
        if cand in sn:
            anchor = cand
            break
    if anchor is None:
        sys.exit("не нашёл alts=dict(main=...) для " + code)
    sn = sn.replace(anchor, "alts=dict(history=\"" + v["alt"] + "\", main=" + anchor[len("alts=dict(main="):], 1)
io.open(SN, "w", encoding="utf-8").write(sn)

# 3. История: из карточки в ряд
old_rows = '    rows = (row(f[2],"settings",False) + row(f[1],"face",True) +\n        row(f[5],"summary",False) + row(f[3],"photo",True))'
new_rows = '    # HISTORY_ROW: история — полноценный ряд, а не карточка\n' + \
           '    rows = (row(f[2],"settings",False) + row(f[1],"face",True) +\n' + \
           '        row(f[5],"summary",False) + row(f[3],"photo",True) +\n' + \
           '        row(f[4],"history",False,x["free_badge"]))'
if old_rows not in bs:
    sys.exit("не нашёл блок rows в build_site.py")
bs = bs.replace(old_rows, new_rows)

old_row_def = '    def row(feat, shot, flip):\n        ico,t,p = feat\n        return (f\'<div class="row{" flip" if flip else ""}">\'\n                f\'<div class="rtext"><div class="ico" aria-hidden="true">{ico}</div><h3>{e(t)}</h3><p>{e(p)}</p></div>\''
new_row_def = '    def row(feat, shot, flip, badge=None):\n        ico,t,p = feat\n        b = f\'<span class="badge free">{e(badge)}</span>\' if badge else ""\n        return (f\'<div class="row{" flip" if flip else ""}">\'\n                f\'<div class="rtext"><div class="ico" aria-hidden="true">{ico}</div><h3>{e(t)}{b}</h3><p>{e(p)}</p></div>\''
if old_row_def not in bs:
    sys.exit("не нашёл определение row() в build_site.py")
bs = bs.replace(old_row_def, new_row_def)

old_cards = '    cards = card(f[0]) + card(f[4], x["free_badge"]) + card(f[6])'
new_cards = '    cards = card(f[0]) + card(f[6])'
if old_cards not in bs:
    sys.exit("не нашёл блок cards в build_site.py")
bs = bs.replace(old_cards, new_cards)

io.open(BS, "w", encoding="utf-8").write(bs)
print("готово. Копии: *.hist.bak")
print("Дальше из корня: python3 gen/build_site.py")