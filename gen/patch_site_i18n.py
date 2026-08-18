TAIL = r'''PAGES_BY_LANG = True   # маркер применённого патча

def href_for(code):
    """Адрес языковой страницы. Английский живёт в корне сайта."""
    return "/" if code == "en" else "/" + code + "/"


def nav_for(active):
    out = []
    for c in order:
        cur = ' aria-current="true"' if c == active else ''
        out.append('<a class="lang" href="' + href_for(c) + '"' + cur + '>' + names[c] + '</a>')
    return "".join(out)


def alternates(active):
    """hreflang на все языковые версии, x-default — на английскую."""
    rows = []
    for c in order:
        rows.append('<link rel="alternate" hreflang="' + c + '" href="' + SITE.rstrip("/") + href_for(c) + '">')
    rows.append('<link rel="alternate" hreflang="x-default" href="' + SITE + '">')
    return "\n".join(rows)


def page(code):
    d = L[code]
    x = X[code]
    canon = SITE.rstrip("/") + href_for(code)
    alts = alternates(code)
    nav = nav_for(code)
    body = section(code, d, x, True)
    return f"""<!doctype html>
<html lang="{code}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(d["title"])}</title>
<meta name="description" content="{e(d["meta"])}">
<link rel="canonical" href="{canon}">
{alts}
<meta property="og:type" content="website">
<meta property="og:url" content="{canon}">
<meta property="og:locale" content="{code}">
<meta property="og:title" content="{e(d["title"])}">
<meta property="og:description" content="{e(d["meta"])}">
<meta property="og:image" content="{SITE}og.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(d["title"])}">
<meta name="twitter:description" content="{e(d["meta"])}">
<meta name="twitter:image" content="{SITE}og.png">
<meta name="apple-itunes-app" content="app-id=6801931802">
<meta name="theme-color" content="#0B0C0E">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="/icon-192.png">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<script>if(/\\.github\\.io$/.test(location.hostname)){{location.replace("{SITE}"+location.search+location.hash);}}</script>
<style>{CSS}</style>
</head>
<body>
<main>
<header>
  <a class="home" href="/"><img src="/icon-64.png" alt="" width="34" height="34">Prau</a>
  <nav id="langs" aria-label="Language">{nav}</nav>
  <a class="navcta" href="{APPSTORE}">{e(x["nav_cta"])}</a>
</header>
{body}
</main>
<script>
(function(){{
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  function esc(s){{return s.replace(/[&<>]/g,function(c){{return {{'&':'&amp;','<':'&lt;','>':'&gt;'}}[c];}});}}
  function render(box,conv){{
    box.innerHTML=conv.map(function(m,i){{return '<div class="bub '+(i%2?'b':'a')+'"><span class="flag" aria-hidden="true">'+m[0]+'</span>'+esc(m[1])+'</div>';}}).join('');
  }}
  var box=document.querySelector('.demo');
  if(box){{
    var demos=JSON.parse(box.getAttribute('data-demos')); var i=0;
    render(box,demos[0]);
    if(!reduce&&demos.length>1){{
      setInterval(function(){{ if(document.hidden) return; i=(i+1)%demos.length; render(box,demos[i]); }},6500);
    }}
  }}
}})();
</script>
</body>
</html>
"""


import datetime
OUT = os.path.dirname(HERE)   # пишем сразу в корень репозитория, без ручного cp
total = 0
for code in order:
    html_out = page(code)
    if code == "en":
        path = os.path.join(OUT, "index.html")
    else:
        folder = os.path.join(OUT, code)
        if not os.path.isdir(folder):
            os.makedirs(folder)
        path = os.path.join(folder, "index.html")
    open(path, "w", encoding="utf-8").write(html_out)
    total += len(html_out)
    print(code, len(html_out), "bytes")

today = datetime.date.today().isoformat()
rows = []
for code in order:
    rows.append("  <url>\n    <loc>" + SITE.rstrip("/") + href_for(code) +
                "</loc>\n    <lastmod>" + today +
                "</lastmod>\n    <changefreq>weekly</changefreq>\n    <priority>" +
                ("1.0" if code == "en" else "0.8") + "</priority>\n  </url>")
rows.append("  <url>\n    <loc>" + SITE + "privacy.html</loc>\n    <lastmod>" + today +
            "</lastmod>\n    <changefreq>monthly</changefreq>\n    <priority>0.3</priority>\n  </url>")
sm = ('<?xml version="1.0" encoding="UTF-8"?>\n'
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
      + "\n".join(rows) + "\n</urlset>\n")
open(os.path.join(OUT, "sitemap.xml"), "w", encoding="utf-8").write(sm)
print("sitemap.xml:", len(order) + 1, "URL")
print("ИТОГО", total, "bytes")
'''

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Патч gen/build_site.py: одна страница на язык вместо шести секций в одном файле.

  /index.html   английский (корень)   /ru/  /uk/  /fr/  /es/  /de/
  на каждой: свой lang, title, description, canonical, взаимные hreflang.
  Переключатель языков — обычные ссылки. Заодно пересобирается sitemap.xml.

ЗАПУСК из папки gen/:  python3 patch_site_i18n.py
Резервная копия: build_site.py.bak
"""
import io, os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "build_site.py")
if not os.path.exists(SRC):
    sys.exit("build_site.py не найден — запускайте из папки gen/")

src = io.open(SRC, encoding="utf-8").read()
if "PAGES_BY_LANG" in src:
    sys.exit("Патч уже применён.")
shutil.copyfile(SRC, SRC + ".bak")

# 1. Внутренние пути делаем корневыми: из /ru/ относительные ломаются
for a, b in [
    ('srcset="img/{name}.webp"',    'srcset="/img/{name}.webp"'),
    ('src="img/{name}.png"',        'src="/img/{name}.png"'),
    ('href="privacy.html#{code}"',  'href="/privacy.html#{code}"'),
]:
    if a not in src:
        sys.exit("Фрагмент не найден, генератор изменился: " + a)
    src = src.replace(a, b)

# 2. Секция на своей странице всегда видима
old = "  section[data-lang]{display:none}\n  section[data-lang].active{display:block}"
if old not in src:
    sys.exit("Не найдены правила section[data-lang] в CSS")
src = src.replace(old, "  section[data-lang]{display:block}")

# 3. Переключатель языков: кнопки -> ссылки
src = src.replace("  nav button{background:transparent;",
                  "  nav a.lang{text-decoration:none;background:transparent;")
src = src.replace('  nav button[aria-pressed="true"]{',
                  '  nav a.lang[aria-current="true"]{')
src = src.replace("  nav button:focus-visible,", "  nav a.lang:focus-visible,")

# 4. Новый хвост вместо сборки одного файла
cut = src.index("PRESSED = ' aria-pressed=" + chr(34) + "true" + chr(34) + "'")
io.open(SRC, "w", encoding="utf-8").write(src[:cut] + TAIL)
print("build_site.py пропатчен. Копия: build_site.py.bak")
