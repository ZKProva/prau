# -*- coding: utf-8 -*-
"""
Генератор партнёрских страниц Prau.

Вход:  gen/partners.csv  (slug,name,lang,code_annual,code_monthly,code_lifetime)
       lang — язык по умолчанию: превью в мессенджерах и запасной вариант,
       если язык телефона не из списка. Сама страница содержит все языки из LANGS
       и показывает язык телефона; вверху — переключатель.
Выход: go/<slug>/index.html          — страница партнёра с тремя кнопками
       go/<slug>/annual/index.html   — переход на оффер Annual (Cloudflare считает заходы)
       go/<slug>/monthly/index.html  — переход на оффер Monthly
       go/<slug>/lifetime/index.html — переход на оффер Lifetime
       go/<slug>/qr.png              — QR на страницу партнёра (нужен pip3 install qrcode pillow)

Запуск из корня репо сайта:  python3 gen/build_partners.py
Совместим с Python 3.9 (без f-строк с бэкслэшем, без match).
Страницы /go/ не попадают в sitemap и закрыты от поисковиков (noindex).
"""
import csv
import html
import os
import re

APP_ID = "6801931802"
SITE = "https://getprau.com"
OG_IMAGE = SITE + "/img/demo-poster.jpg"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "gen", "partners.csv")
OUT_DIR = os.path.join(ROOT, "go")

PLANS = ("annual", "monthly", "lifetime")

# Порядок = порядок в переключателе. Добавить язык: новый ключ в T + код сюда.
LANGS = ("ru", "uk", "en", "nl", "fr", "de")
LABELS = {"ru": "RU", "uk": "UA", "en": "EN", "nl": "NL", "fr": "FR", "de": "DE"}

T = {
    "ru": {
        "share": "Покажите этот код другу — он наведёт камеру iPhone и получит тот же бонус.",
        "chem": "Химия вашей приватности.", "pr": "приватность", "au": "золото",
        "title": "Prau — офлайн-переводчик голоса",
        "from": "Рекомендует: {name}",
        "lead": "Ваш голос и ваши разговоры — не для чужих серверов. Prau переводит на 19 языков прямо на iPhone, без интернета: ни одно слово не покидает телефон.",
        "bonus_h": "Ваш бонус по этой ссылке",
        "bonus": ["7 дней бесплатно вместо 3 — на месяц и год", "−10% на «Навсегда»"],
        "feat": ["19 языков без интернета", "Разговор в любые наушники", "Лицом к лицу на одном телефоне", "Перевод фото и PDF"],
        "rare": ["История разговоров: переименование свайпом вправо, кнопка «Продолжить» добавляет новые фразы в тот же разговор",
                 "AI-саммари разговора в одно касание (с Apple Intelligence)",
                 "Siri и кнопка действия: перевод в одно касание (кнопка — на iPhone 15 Pro и новее)"],
        "annual": "Год", "annual_b": "7 дней вместо 3",
        "monthly": "Месяц", "monthly_b": "7 дней вместо 3",
        "lifetime": "Навсегда", "lifetime_b": "−10%",
        "best": "Выгоднее всего",
        "note": "Бонус действует только при покупке по кнопке на этой странице. Цена в вашей валюте — в App Store.",
        "iphone": "Prau работает только на iPhone. Откройте эту ссылку на iPhone или наведите камеру на код:",
        "fallback": "Если App Store не открылся — нажмите сюда",
    },
    "uk": {
        "share": "Покажіть цей код другові — він наведе камеру iPhone і отримає той самий бонус.",
        "chem": "Хімія вашої приватності.", "pr": "приватність", "au": "золото",
        "title": "Prau — офлайн-перекладач голосу",
        "from": "Рекомендує: {name}",
        "lead": "Ваш голос і ваші розмови — не для чужих серверів. Prau перекладає 19 мовами просто на iPhone, без інтернету: жодне слово не залишає телефон.",
        "bonus_h": "Ваш бонус за цим посиланням",
        "bonus": ["7 днів безкоштовно замість 3 — на місяць і рік", "−10% на «Назавжди»"],
        "feat": ["19 мов без інтернету", "Розмова в будь-які навушники", "Обличчям до обличчя на одному телефоні", "Переклад фото і PDF"],
        "rare": ["Історія розмов: перейменування свайпом праворуч, кнопка «Продовжити» додає нові фрази в ту саму розмову",
                 "AI-підсумок розмови в один дотик (з Apple Intelligence)",
                 "Siri і кнопка дії: переклад в один дотик (кнопка — на iPhone 15 Pro і новіших)"],
        "annual": "Рік", "annual_b": "7 днів замість 3",
        "monthly": "Місяць", "monthly_b": "7 днів замість 3",
        "lifetime": "Назавжди", "lifetime_b": "−10%",
        "best": "Найвигідніше",
        "note": "Бонус діє лише при покупці за кнопкою на цій сторінці. Ціна у вашій валюті — в App Store.",
        "iphone": "Prau працює лише на iPhone. Відкрийте це посилання на iPhone або наведіть камеру на код:",
        "fallback": "Якщо App Store не відкрився — натисніть сюди",
    },
    "en": {
        "share": "Show this code to a friend — they point their iPhone camera at it and get the same bonus.",
        "chem": "The chemistry of your privacy.", "pr": "privacy", "au": "gold",
        "title": "Prau — offline voice translator",
        "from": "Recommended by {name}",
        "lead": "Your voice and your conversations don't belong on someone else's servers. Prau translates 19 languages right on your iPhone, offline — not a single word leaves your phone.",
        "bonus_h": "Your bonus with this link",
        "bonus": ["7 days free instead of 3 — on Month and Year", "−10% on Lifetime"],
        "feat": ["19 languages, no internet", "Talk through any headphones", "Face to face on one phone", "Translate photos and PDFs"],
        "rare": ["Conversation history: swipe right to rename, tap Continue to add new phrases to the same conversation",
                 "One-tap AI summary of a conversation (with Apple Intelligence)",
                 "Siri and the Action Button: translate in one tap (Action Button on iPhone 15 Pro and later)"],
        "annual": "Year", "annual_b": "7 days instead of 3",
        "monthly": "Month", "monthly_b": "7 days instead of 3",
        "lifetime": "Lifetime", "lifetime_b": "−10%",
        "best": "Best value",
        "note": "The bonus applies only when you buy with a button on this page. Your local price is shown in the App Store.",
        "iphone": "Prau runs on iPhone only. Open this link on your iPhone or scan the code:",
        "fallback": "If the App Store did not open, tap here",
    },
    "nl": {
        "share": "Laat deze code aan een vriend zien — hij richt zijn iPhone-camera erop en krijgt dezelfde bonus.",
        "chem": "De chemie van je privacy.", "pr": "privacy", "au": "goud",
        "title": "Prau — offline spraakvertaler",
        "from": "Aanbevolen door {name}",
        "lead": "Je stem en je gesprekken horen niet op andermans servers. Prau vertaalt 19 talen direct op je iPhone, offline — geen enkel woord verlaat je telefoon.",
        "bonus_h": "Jouw bonus via deze link",
        "bonus": ["7 dagen gratis in plaats van 3 — bij Maand en Jaar", "−10% op Levenslang"],
        "feat": ["19 talen zonder internet", "Praten via elke koptelefoon of oortjes", "Tegenover elkaar op één telefoon", "Foto's en pdf's vertalen"],
        "rare": ["Gespreksgeschiedenis: veeg naar rechts om te hernoemen, tik op Doorgaan om nieuwe zinnen aan hetzelfde gesprek toe te voegen",
                 "AI-samenvatting van een gesprek met één tik (met Apple Intelligence)",
                 "Siri en de actieknop: vertalen met één tik (actieknop op iPhone 15 Pro en nieuwer)"],
        "annual": "Jaar", "annual_b": "7 dagen i.p.v. 3",
        "monthly": "Maand", "monthly_b": "7 dagen i.p.v. 3",
        "lifetime": "Levenslang", "lifetime_b": "−10%",
        "best": "Voordeligst",
        "note": "De bonus geldt alleen bij aankoop via een knop op deze pagina. De prijs in jouw valuta zie je in de App Store.",
        "iphone": "Prau werkt alleen op iPhone. Open deze link op je iPhone of scan de code:",
        "fallback": "Opent de App Store niet? Tik hier",
    },
    "fr": {
        "share": "Montrez ce code à un ami : il le scanne avec l'appareil photo de son iPhone et reçoit le même bonus.",
        "chem": "La chimie de votre vie privée.", "pr": "confidentialité", "au": "or",
        "title": "Prau — traducteur vocal hors ligne",
        "from": "Recommandé par {name}",
        "lead": "Votre voix et vos conversations n'ont rien à faire sur les serveurs des autres. Prau traduit 19 langues directement sur votre iPhone, hors ligne : pas un mot ne quitte votre téléphone.",
        "bonus_h": "Votre bonus avec ce lien",
        "bonus": ["7 jours gratuits au lieu de 3 — sur Un mois et Un an", "−10 % sur À vie"],
        "feat": ["19 langues sans internet", "Conversation dans n'importe quels écouteurs", "Face à face sur un seul téléphone", "Traduction de photos et de PDF"],
        "rare": ["Historique des conversations : balayez vers la droite pour renommer, touchez Continuer pour ajouter de nouvelles phrases à la même conversation",
                 "Résumé IA d'une conversation en un geste (avec Apple Intelligence)",
                 "Siri et le bouton Action : traduire en un geste (bouton Action sur iPhone 15 Pro et ultérieurs)"],
        "annual": "Un an", "annual_b": "7 jours au lieu de 3",
        "monthly": "Un mois", "monthly_b": "7 jours au lieu de 3",
        "lifetime": "À vie", "lifetime_b": "−10 %",
        "best": "Le plus avantageux",
        "note": "Le bonus s'applique uniquement à l'achat via un bouton de cette page. Le prix dans votre devise s'affiche dans l'App Store.",
        "iphone": "Prau fonctionne uniquement sur iPhone. Ouvrez ce lien sur votre iPhone ou scannez le code :",
        "fallback": "Si l'App Store ne s'est pas ouvert, touchez ici",
    },
    "de": {
        "share": "Zeig diesen Code einem Freund – er scannt ihn mit der iPhone-Kamera und bekommt denselben Bonus.",
        "chem": "Die Chemie deiner Privatsphäre.", "pr": "Privatsphäre", "au": "Gold",
        "title": "Prau — Offline-Sprachübersetzer",
        "from": "Empfohlen von {name}",
        "lead": "Deine Stimme und deine Gespräche gehören nicht auf fremde Server. Prau übersetzt 19 Sprachen direkt auf deinem iPhone, offline — kein einziges Wort verlässt dein Handy.",
        "bonus_h": "Dein Bonus über diesen Link",
        "bonus": ["7 Tage gratis statt 3 — bei Monat und Jahr", "−10 % auf Für immer"],
        "feat": ["19 Sprachen ohne Internet", "Gespräch über beliebige Kopfhörer", "Von Angesicht zu Angesicht auf einem Handy", "Fotos und PDFs übersetzen"],
        "rare": ["Gesprächsverlauf: nach rechts wischen zum Umbenennen, „Fortsetzen“ fügt neue Sätze zum selben Gespräch hinzu",
                 "KI-Zusammenfassung eines Gesprächs mit einem Tipp (mit Apple Intelligence)",
                 "Siri und Aktionstaste: übersetzen mit einem Tipp (Aktionstaste ab iPhone 15 Pro)"],
        "annual": "Jahr", "annual_b": "7 statt 3 Tage",
        "monthly": "Monat", "monthly_b": "7 statt 3 Tage",
        "lifetime": "Für immer", "lifetime_b": "−10 %",
        "best": "Bestes Angebot",
        "note": "Der Bonus gilt nur beim Kauf über einen Button auf dieser Seite. Den Preis in deiner Währung zeigt der App Store.",
        "iphone": "Prau läuft nur auf dem iPhone. Öffne diesen Link auf deinem iPhone oder scanne den Code:",
        "fallback": "Falls sich der App Store nicht geöffnet hat, hier tippen",
    },
}

CSS = """
:root{--bg:#0a0b0d;--card:#141619;--line:#2a2d33;--text:#f4f2ee;--muted:#9b9da3;--gold:#e3c18b;--gold-ink:#1a1408}
*{box-sizing:border-box}
[hidden]{display:none!important}
html{background:var(--bg)}
body{margin:0;background:var(--bg);color:var(--text);font:16px/1.5 -apple-system,BlinkMacSystemFont,"SF Pro Text",system-ui,sans-serif;-webkit-font-smoothing:antialiased}
main{max-width:440px;margin:0 auto;padding:16px 16px 40px}
nav{display:flex;justify-content:center;flex-wrap:wrap;gap:4px;margin:0 0 28px}
nav button{font:inherit;font-size:13px;font-weight:600;color:var(--muted);background:none;border:1px solid transparent;border-radius:8px;padding:4px 9px;cursor:pointer}
nav button.on{color:var(--text);border-color:var(--line)}
.tiles{display:flex;justify-content:center;margin:0 0 14px}
.tile{width:118px;height:118px;border-radius:16px;position:relative;display:flex;flex-direction:column;align-items:center;justify-content:center}
.tile .n{position:absolute;top:8px;left:12px;font-size:13px}
.tile .s{font-size:44px;font-weight:700;line-height:1;letter-spacing:-.02em}
.tile .w{position:absolute;bottom:8px;font-size:12px}
.tile.pr{border:2px solid var(--gold);color:var(--text)}
.tile.pr .n,.tile.pr .w{color:var(--muted)}
.tile.au{background:var(--gold);color:var(--gold-ink)}
.word{text-align:center;font-size:40px;font-weight:700;letter-spacing:-.02em;margin:0 0 14px}
.word span{color:var(--gold)}
.from{display:table;margin:0 auto 18px;padding:4px 12px;border-radius:99px;border:1px solid rgba(227,193,139,.4);color:var(--gold);font-weight:600;font-size:14px}
h1{font-size:28px;line-height:1.15;text-align:center;margin:0 0 10px;letter-spacing:-.01em}
.lead{color:var(--muted);text-align:center;margin:0 0 22px}
ul{list-style:none;padding:0;margin:0 0 24px;display:grid;gap:8px}
li{padding-left:24px;position:relative}
li:before{content:"✓";position:absolute;left:0;color:var(--gold);font-weight:700}
.bonus{border:2px solid var(--gold);border-radius:16px;padding:12px 16px;margin:0 0 22px}
.bonus b{display:block;color:var(--gold);font-size:12px;text-transform:uppercase;letter-spacing:.06em;margin-bottom:4px}
.bonus ul{margin:0;gap:2px}
.bonus li{font-weight:600}
.bonus li:before{content:"★"}
.plans{display:grid;gap:10px}
a.plan{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:16px 18px;border-radius:18px;background:var(--card);border:1px solid var(--line);color:var(--text);text-decoration:none;font-weight:600;font-size:18px}
a.plan.main{background:var(--gold);border-color:var(--gold);color:var(--gold-ink)}
a.plan:active{transform:scale(.98)}
.badge{font-size:14px;font-weight:700;color:var(--gold-ink);background:var(--gold);padding:4px 10px;border-radius:99px;white-space:nowrap}
a.plan.main .badge{background:var(--gold-ink);color:var(--gold)}
.best{display:block;font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.06em;opacity:.7}
.note{color:var(--muted);font-size:13px;text-align:center;margin:18px 0 0}
.qr{text-align:center;margin-top:28px;padding-top:22px;border-top:1px solid var(--line)}
.qr img{width:200px;height:200px;background:#fff;padding:10px;border-radius:14px;display:block;margin:0 auto 10px}
.qr p{color:var(--muted);font-size:13px;margin:0 auto;max-width:300px}
.desk{display:none;text-align:center;margin:18px 0 0}
body.notios .plans{display:none}
body.notios .desk{display:block}
body.notios .qr p.sh{display:none}
.foot{text-align:center;margin-top:28px;font-size:13px}
.foot a{color:var(--muted)}
"""

PAGE = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="robots" content="noindex,nofollow">
<title>{title}</title>
<meta name="description" content="{lead}">
<meta property="og:title" content="{title} · {from_}">
<meta property="og:description" content="{lead}">
<meta property="og:image" content="{og_image}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico">
<style>{css}</style>
</head>
<body>
<main>
<nav>{nav}</nav>
{sections}
<div class="qr"><img src="qr.png" alt="QR">{qrtext}</div>
<p class="foot"><a href="/">getprau.com</a></p>
</main>
<script>
(function(){{
var u=navigator.userAgent||"";
var ios=/iPhone|iPod/.test(u)||(/Macintosh/.test(u)&&navigator.maxTouchPoints>1);
if(!ios)document.body.className+=" notios";
var have={langs};
function show(l){{
  var s=document.querySelectorAll("section[data-lang]");
  for(var i=0;i<s.length;i++)s[i].hidden=s[i].getAttribute("data-lang")!==l;
  var q=document.querySelectorAll("p.sh");
  for(var x=0;x<q.length;x++)q[x].hidden=q[x].getAttribute("data-l")!==l;
  var b=document.querySelectorAll("nav button");
  for(var j=0;j<b.length;j++)b[j].className=b[j].getAttribute("data-lang")===l?"on":"";
  document.documentElement.lang=l;
}}
var pick=null,list=navigator.languages||[navigator.language||""];
for(var k=0;k<list.length&&!pick;k++){{var c=String(list[k]).slice(0,2).toLowerCase();if(have.indexOf(c)>=0)pick=c;}}
show(pick||"{lang}");
var nb=document.querySelectorAll("nav button");
for(var m=0;m<nb.length;m++)nb[m].onclick=function(){{show(this.getAttribute("data-lang"));}};
}})();
</script>
</body>
</html>
"""

SECTION = """<section data-lang="{code}"{hidden}>
<div class="tiles"><div class="tile pr"><span class="n">59</span><span class="s">Pr</span><span class="w">{pr}</span></div><div class="tile au"><span class="n">79</span><span class="s">Au</span><span class="w">{au}</span></div></div>
<div class="word">Pr<span>au</span></div>
<div class="from">{from_}</div>
<h1>{chem}</h1>
<p class="lead">{lead}</p>
<div class="bonus"><b>{bonus_h}</b><ul>{bonus}</ul></div>
<ul>{feats}</ul>
<div class="plans">
<a class="plan main" href="annual/"><span><span class="best">{best}</span>{annual}</span><span class="badge">{annual_b}</span></a>
<a class="plan" href="monthly/"><span>{monthly}</span><span class="badge">{monthly_b}</span></a>
<a class="plan" href="lifetime/"><span>{lifetime}</span><span class="badge">{lifetime_b}</span></a>
</div>
<p class="note">{note}</p>
<p class="desk">{iphone}</p>
</section>"""

HOP = """<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<meta http-equiv="refresh" content="0;url={target}">
<title>Prau</title>
<style>body{{margin:0;background:#0d0f14;color:#f2f2f5;font:16px/1.5 -apple-system,system-ui,sans-serif;text-align:center;padding:80px 16px}}a{{color:#e8b84a}}</style>
</head>
<body>
<p>App Store…</p>
<p><a href="{target}">{fallback}</a></p>
<script>location.replace("{target}");</script>
</body>
</html>
"""

CODE_RE = re.compile(r"^[A-Za-z0-9]{1,64}$")
SLUG_RE = re.compile(r"^[a-z0-9-]{2,40}$")


def redeem_url(code):
    return "https://apps.apple.com/redeem?ctx=offercodes&id=" + APP_ID + "&code=" + code


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def make_qr(url, path):
    try:
        import qrcode
    except ImportError:
        return False
    img = qrcode.make(url, box_size=10, border=2)
    img.save(path)
    return True


def build_partner(row):
    slug = row["slug"].strip().lower()
    if not SLUG_RE.match(slug):
        raise SystemExit("Плохой slug: " + repr(slug) + " (только a-z, 0-9, дефис)")
    lang = (row.get("lang") or "ru").strip()
    if lang not in T:
        raise SystemExit("Нет текстов для языка " + repr(lang) + " у " + slug)
    name = html.escape(row["name"].strip())
    base = os.path.join(OUT_DIR, slug)
    url = SITE + "/go/" + slug + "/"

    for plan in PLANS:
        code = row["code_" + plan].strip()
        if not CODE_RE.match(code):
            raise SystemExit("Плохой код " + repr(code) + " у " + slug + " (" + plan + "): только буквы и цифры")
        target = redeem_url(code)
        write(os.path.join(base, plan, "index.html"),
              HOP.format(lang=lang, target=target, fallback=T[lang]["fallback"]))

    nav = "".join('<button type="button" data-lang="' + c + '"' + (' class="on"' if c == lang else "") + ">"
                  + LABELS[c] + "</button>" for c in LANGS)
    sections = []
    for c in LANGS:
        t = T[c]
        sections.append(SECTION.format(
            code=c, hidden="" if c == lang else " hidden",
            from_=t["from"].format(name=name), title=t["title"], lead=t["lead"],
            feats="".join("<li>" + html.escape(x) + "</li>" for x in t["feat"] + t["rare"]),
            bonus="".join("<li>" + html.escape(x) + "</li>" for x in t["bonus"]),
            bonus_h=t["bonus_h"], chem=t["chem"], pr=t["pr"], au=t["au"],
            best=t["best"], annual=t["annual"], annual_b=t["annual_b"],
            monthly=t["monthly"], monthly_b=t["monthly_b"],
            lifetime=t["lifetime"], lifetime_b=t["lifetime_b"],
            note=t["note"], iphone=t["iphone"],
        ))
    d = T[lang]
    page = PAGE.format(
        lang=lang, title=d["title"], lead=d["lead"], from_=d["from"].format(name=name),
        og_image=OG_IMAGE, url=url, css=CSS, nav=nav, sections="\n".join(sections),
        langs="[" + ",".join('"' + c + '"' for c in LANGS) + "]",
        qrtext="".join('<p class="sh" data-l="' + c + '"' + ('' if c == lang else ' hidden') + '>' + html.escape(T[c]["share"]) + '</p>' for c in LANGS),
    )
    write(os.path.join(base, "index.html"), page)
    qr_ok = make_qr(url, os.path.join(base, "qr.png"))
    return url, qr_ok


def main():
    for c in LANGS:
        if c not in T:
            raise SystemExit("Язык " + c + " есть в LANGS, но нет текстов в T")
    with open(CSV_PATH, encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if (r.get("slug") or "").strip()]
    seen = set()
    for r in rows:
        for plan in PLANS:
            c = r["code_" + plan].strip().upper()
            if c in seen:
                raise SystemExit("Код повторяется: " + c + " (Apple требует уникальные коды в приложении)")
            seen.add(c)
    for r in rows:
        url, qr_ok = build_partner(r)
        print("OK  " + url + ("" if qr_ok else "   (QR не сделан: pip3 install qrcode pillow)"))
    print("Готово: " + str(len(rows)) + " партн.")


if __name__ == "__main__":
    main()
