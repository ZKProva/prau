#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Генерирует index.html для getprau.com — витрина Prau с реальными экранами, 6 языков.
# Тексты: strings_base.py (прежний сайт) + strings_new.py (новые блоки).
import html, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
exec(open(os.path.join(HERE, "strings_base.py"), encoding="utf-8").read())   # даёт L, APPSTORE, MAIL
from strings_new import X

SITE = "https://getprau.com/"
order = ["en","ru","uk","fr","es","de"]
names = {"en":"English","ru":"Русский","uk":"Українська","fr":"Français","es":"Español","de":"Deutsch"}

def e(s): return html.escape(s, quote=False)

def phone(name, alt, cls=""):
    return (f'<figure class="phone {cls}"><picture>'
            f'<source srcset="img/{name}.webp" type="image/webp">'
            f'<img src="img/{name}.png" alt="{e(alt)}" width="640" height="1288" loading="lazy" decoding="async">'
            f'</picture></figure>')

def bubbles(conv):
    return "".join(f'<div class="bub {"a" if i%2==0 else "b"}"><span class="flag" aria-hidden="true">{f}</span>{e(t)}</div>'
                   for i,(f,t) in enumerate(conv))

def section(code, d, x, active):
    lines = d["hero_h1"].split("\n")
    h1 = e(lines[0]) + "<br><span class=\"g\">" + e(lines[1]) + "</span>"
    demos_json = html.escape(json.dumps(x["demos"], ensure_ascii=False), quote=True)
    how = "".join(f'<li><b>{e(t)}</b><p>{e(p)}</p></li>' for t,p in d["how"])
    f = d["feats"]; a = x["alts"]
    def row(feat, shot, flip):
        ico,t,p = feat
        return (f'<div class="row{" flip" if flip else ""}">'
                f'<div class="rtext"><div class="ico" aria-hidden="true">{ico}</div><h3>{e(t)}</h3><p>{e(p)}</p></div>'
                f'{phone(shot, a[shot])}</div>')
    rows = (row(f[2],"settings",False) + row(f[1],"face",True) +
        row(f[5],"summary",False) + row(f[3],"photo",True))
    def card(feat, badge=None):
        ico,t,p = feat
        b = f'<span class="badge free">{e(badge)}</span>' if badge else ""
        return f'<div class="card"><div class="ico" aria-hidden="true">{ico}</div><h3>{e(t)}{b}</h3><p>{e(p)}</p></div>'
    cards = card(f[0]) + card(f[4], x["free_badge"]) + card(f[6])
    setup = "".join(f'<li><b>{e(t)}</b><p>{e(p)}</p></li>' for t,p in x["setup"])
    stays = "".join(f"<li>{e(s)}</li>" for s in d["stays"])
    leaves = "".join(f"<li>{e(s)}</li>" for s in d["leaves"])
    pbul = "".join(f"<li>{e(s)}</li>" for s in d["priv_bul"])
    pro = ""
    for i,(n,p,t) in enumerate(d["pro"]):
        best = f'<span class="badge best">{e(x["best_badge"])}</span>' if i==1 else ""
        pro += f'<div class="plan{" hi" if i==1 else ""}">{best}<div class="pn">{e(n)}</div><div class="pp">{e(p)}</div><p>{e(t)}</p></div>'
    faq = "".join(f'<details><summary>{e(q)}</summary><p>{e(a_)}</p></details>' for q,a_ in d["faq"])
    return f'''
<section data-lang="{code}"{' class="active"' if active else ''}>
<div class="hero">
  <div class="htext">
    <p class="kicker">{e(d["hero_kicker"])}</p>
    <h1>{h1}</h1>
    <p class="lead">{e(d["hero_lead"])}</p>
    <p class="cta"><a class="btn" href="{APPSTORE}"><span class="apple" aria-hidden="true"></span>{e(d["cta"])}</a><span class="ctan">{e(d["cta_note"])}</span></p>
    <div class="demo" data-demos="{demos_json}" aria-hidden="true">{bubbles(x["demos"][0])}</div>
  </div>
  <div class="hshot">
    {phone("main", a["main"], "hero-phone")}
    <p class="shotnote">{e(x["hero_note2"])}</p>
  </div>
</div>

<h2>{e(d["how_h"])}</h2>
<p class="sub">{e(d["how_sub"])}</p>
<ol class="how">{how}</ol>

<h2>{e(x["see_h"])}</h2>
<p class="sub">{e(x["see_sub"])}</p>
<div class="rows">{rows}</div>
<div class="grid">{cards}</div>

<h2 id="setup-{code}">{e(x["setup_h"])}</h2>
<p class="sub">{e(x["setup_sub"])}</p>
<ol class="how setup">{setup}</ol>
<p class="tip">{e(x["setup_tip"])}</p>

<h2>{e(d["lang_h"])}</h2>
<div class="row langrow">
  <div class="rtext"><p class="big">{e(d["lang_p"])}</p><p class="note">{e(d["lang_note"])}</p></div>
  {phone("picker", a["picker"])}
</div>

<h2 id="privacy-{code}">{e(d["priv_h"])}</h2>
<p class="sub">{e(d["priv_lead"])}</p>
<div class="two">
  <div class="col stays"><h3>{e(d["stays_h"])}</h3><ul>{stays}</ul></div>
  <div class="col leaves"><h3>{e(d["leaves_h"])}</h3><ul>{leaves}</ul></div>
</div>
<ul class="plain">{pbul}</ul>
<p><a href="privacy.html#{code}">{e(d["priv_link"])} →</a></p>

<h2>{e(d["pro_h"])}</h2>
<p class="sub">{e(d["pro_lead"])}</p>
<div class="plans">{pro}</div>
<p class="free">{e(d["pro_free"])}</p>
<p class="note">{e(d["pro_note"])}</p>
<p class="cta cta2"><a class="btn" href="{APPSTORE}"><span class="apple" aria-hidden="true"></span>{e(d["cta"])}</a><span class="ctan">{e(d["cta_note"])}</span></p>

<h2 id="support-{code}">{e(d["faq_h"])}</h2>
<div class="faq">{faq}</div>

<h2>{e(d["contact_h"])}</h2>
<p>{e(d["contact_p"])} <a href="mailto:{MAIL}">{MAIL}</a>. {e(d["contact_note"])}</p>

<footer>
  <a href="privacy.html#{code}">{e(d["footer_privacy"])}</a> ·
  <a href="https://www.apple.com/legal/internet-services/itunes/dev/stdeula/">{e(d["footer_terms"])}</a> ·
  <span>{e(d["footer_rights"])}</span>
</footer>
</section>'''

CSS = """
  :root{--bg:#0B0C0E;--panel:#161B21;--panel2:#1B222A;--stroke:#262D36;--muted:#8A94A0;--gold:#EABE7A;--gold2:#F3D9A9;--text:#F2F4F7;--soft:#C9D0D8;--green:#7ED9A0;
        --serif:"New York","Iowan Old Style",ui-serif,Georgia,"Times New Roman",serif;
        --sans:-apple-system,BlinkMacSystemFont,"SF Pro Text",Inter,"Segoe UI",Roboto,sans-serif}
  *{box-sizing:border-box}
  html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
  body{margin:0;background:var(--bg);color:var(--text);font:17px/1.6 var(--sans)}
  main{max-width:1060px;margin:0 auto;padding:22px 24px 72px}
  header{display:flex;flex-wrap:wrap;gap:12px 18px;align-items:center;justify-content:space-between;margin-bottom:6px}
  header .home{display:flex;align-items:center;gap:10px;color:var(--text);text-decoration:none;font-weight:700;font-size:20px;letter-spacing:.01em}
  header .home img{width:34px;height:34px;border-radius:9px}
  nav{display:flex;flex-wrap:wrap;gap:6px}
  nav button{background:transparent;border:1px solid var(--stroke);color:var(--muted);border-radius:999px;padding:6px 12px;font:14px var(--sans);cursor:pointer}
  nav button[aria-pressed="true"]{background:var(--gold);color:#000;border-color:var(--gold)}
  nav button:focus-visible,a:focus-visible,summary:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
  .navcta{display:none;font-size:14px;color:var(--gold);text-decoration:none;border:1px solid #4A3E29;border-radius:999px;padding:6px 12px}
  @media (min-width:760px){.navcta{display:inline-block}}
  section[data-lang]{display:none}
  section[data-lang].active{display:block}

  .hero{display:grid;grid-template-columns:1.15fr .85fr;gap:36px;align-items:center;padding:36px 0 18px}
  .kicker{display:inline-flex;align-items:center;gap:10px;color:#e8c48a;background:rgba(232,196,138,.10);border:1px solid rgba(232,196,138,.35);border-radius:999px;padding:8px 16px;text-transform:uppercase;letter-spacing:.14em;font-size:12.5px;font-weight:600;margin:0 0 22px}.kicker::before{content:"";width:8px;height:8px;border-radius:50%;background:#e8c48a;box-shadow:0 0 12px #e8c48a}
  h1{font-family:var(--serif);font-weight:600;font-size:clamp(38px,5.4vw,66px);line-height:1.02;letter-spacing:-.015em;margin:0 0 20px}
  h1 .g{color:var(--gold)}
  .lead{font-size:19px;color:var(--soft);margin:0 0 26px;max-width:560px}
  .cta{display:flex;align-items:center;gap:16px;flex-wrap:wrap;margin:0 0 30px}
  .btn{display:inline-flex;align-items:center;gap:10px;background:var(--gold);color:#000;font-weight:700;text-decoration:none;padding:14px 22px;border-radius:14px;transition:transform .15s,filter .15s}
  .btn:hover{filter:brightness(1.05);transform:translateY(-1px)}
  .apple{width:16px;height:19px;background:currentColor;-webkit-mask:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 814 1000'><path d='M788 341c-6 5-109 62-109 190 0 148 130 200 134 202-1 3-21 71-69 141-42 62-87 123-155 123s-86-40-165-40c-77 0-104 41-167 41s-106-57-155-127C46 790 0 668 0 552c0-186 121-285 240-285 63 0 116 42 155 42 38 0 97-44 169-44 27 0 126 2 224 76zM554 174c31-37 53-89 53-141 0-7-1-14-2-20-51 2-111 34-147 76-29 33-56 85-56 137 0 8 1 16 2 19 3 1 8 1 13 1 45 0 102-30 137-72z'/></svg>") center/contain no-repeat;mask:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 814 1000'><path d='M788 341c-6 5-109 62-109 190 0 148 130 200 134 202-1 3-21 71-69 141-42 62-87 123-155 123s-86-40-165-40c-77 0-104 41-167 41s-106-57-155-127C46 790 0 668 0 552c0-186 121-285 240-285 63 0 116 42 155 42 38 0 97-44 169-44 27 0 126 2 224 76zM554 174c31-37 53-89 53-141 0-7-1-14-2-20-51 2-111 34-147 76-29 33-56 85-56 137 0 8 1 16 2 19 3 1 8 1 13 1 45 0 102-30 137-72z'/></svg>") center/contain no-repeat}
  .ctan{color:var(--muted);font-size:14px}
  .demo{display:flex;flex-direction:column;gap:8px;max-width:500px;min-height:200px}
  .bub{background:var(--panel2);border:1px solid var(--stroke);border-radius:16px;padding:10px 14px;max-width:86%;font-size:16px;opacity:0;transform:translateY(6px);animation:pop .45s ease forwards}
  .bub:nth-child(1){animation-delay:.05s}.bub:nth-child(2){animation-delay:.55s}.bub:nth-child(3){animation-delay:1.25s}.bub:nth-child(4){animation-delay:1.75s}
  @keyframes pop{to{opacity:1;transform:none}}
  .bub.a{align-self:flex-start;border-bottom-left-radius:4px}
  .bub.b{align-self:flex-end;border-bottom-right-radius:4px;background:#26211A;border-color:#4A3E29}
  .bub .flag{margin-right:8px}
  .hshot{display:flex;flex-direction:column;align-items:center;gap:12px}
  .shotnote{margin:0;color:var(--muted);font-size:13px;text-align:center}

  .phone{margin:0;width:100%;max-width:300px;background:#0F1114;border:1px solid #2A313A;border-radius:44px;padding:11px;box-shadow:0 30px 60px -30px rgba(0,0,0,.9),0 0 0 1px rgba(234,190,122,.06) inset}
  .phone img{display:block;width:100%;height:auto;border-radius:34px;background:#000}
  .hero-phone{max-width:320px}

  h2{font-family:var(--serif);font-weight:600;font-size:clamp(28px,3.4vw,40px);line-height:1.1;letter-spacing:-.01em;margin:64px 0 8px;color:var(--gold)}
  h3{font-size:19px;margin:0 0 6px;font-weight:700}
  .sub{color:var(--muted);margin:0 0 20px;font-size:17px;max-width:680px}
  p,li{color:#D8DDE3}
  a{color:var(--gold)}
  .how{counter-reset:s;list-style:none;padding:0;margin:0}
  .how li{position:relative;padding:0 0 22px 56px}
  .how li:before{counter-increment:s;content:counter(s);position:absolute;left:0;top:0;width:38px;height:38px;border-radius:50%;background:var(--gold);color:#000;font:700 17px var(--sans);display:flex;align-items:center;justify-content:center}
  .how li:not(:last-child):after{content:"";position:absolute;left:18px;top:44px;bottom:0;width:2px;background:var(--stroke)}
  .how b{display:block;font-size:19px;margin-bottom:3px}
  .how p{margin:0;max-width:720px}
  .setup li:before{background:var(--panel2);color:var(--gold);border:1px solid #4A3E29}
  .tip{background:#152219;border:1px solid #25402D;border-radius:14px;padding:12px 16px;color:var(--green);margin:6px 0 0;max-width:720px;font-size:15.5px}

  .rows{display:flex;flex-direction:column;gap:22px}
  .row{display:grid;grid-template-columns:1fr auto;gap:36px;align-items:center;background:var(--panel);border:1px solid var(--stroke);border-radius:26px;padding:30px 34px}
  .row.flip{grid-template-columns:auto 1fr}
  .row.flip .rtext{order:2}
  .row .phone{max-width:250px}
  .rtext .ico{font-size:28px;margin-bottom:10px}
  .rtext p{margin:0;font-size:17px;color:var(--soft);max-width:520px}
  .rtext .big{font-size:18px;color:var(--text)}
  .langrow{margin-top:8px}
  .grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:14px;margin-top:22px}
  .card{background:var(--panel);border:1px solid var(--stroke);border-radius:20px;padding:20px 22px}
  .card .ico{font-size:26px;margin-bottom:8px}
  .card p{margin:0;font-size:15.5px;color:var(--soft)}
  .badge{display:inline-block;font:600 11px/1 var(--sans);letter-spacing:.08em;text-transform:uppercase;border-radius:999px;padding:5px 9px;vertical-align:middle;margin-left:8px}
  .badge.free{background:#152219;color:var(--green);border:1px solid #25402D}
  .badge.best{background:#26211A;color:var(--gold);border:1px solid #4A3E29;position:absolute;top:-12px;right:16px;margin:0}
  .note{color:var(--muted);font-size:15px}
  .two{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:0 0 14px}
  .col{border-radius:20px;padding:18px 20px;border:1px solid var(--stroke)}
  .col ul{margin:0;padding-left:20px}
  .col li{margin:4px 0;font-size:15.5px}
  .stays{background:#152219;border-color:#25402D}
  .stays h3{color:var(--green)}
  .leaves{background:var(--panel)}
  .leaves h3{color:var(--gold)}
  .plain{padding-left:20px}
  .plans{display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:14px;margin-top:6px}
  .plan{position:relative;background:var(--panel);border:1px solid var(--stroke);border-radius:20px;padding:20px 22px}
  .plan.hi{border-color:#4A3E29;background:#1A1712}
  .pn{font-weight:700;font-size:18px}
  .pp{font-family:var(--serif);color:var(--gold);font-size:30px;margin:4px 0 8px;letter-spacing:-.01em}
  .plan p{margin:0;color:var(--muted);font-size:15px}
  .free{margin-top:16px;font-weight:600}
  .cta2{margin-top:22px}
  .faq details{border-bottom:1px solid var(--stroke);padding:12px 0}
  .faq summary{cursor:pointer;font-weight:600;list-style:none;display:flex;justify-content:space-between;gap:12px}
  .faq summary::-webkit-details-marker{display:none}
  .faq summary:after{content:"+";color:var(--gold);font-size:22px;line-height:1}
  .faq details[open] summary:after{content:"–"}
  .faq p{margin:10px 0 0;color:var(--soft);font-size:15.5px;max-width:760px}
  footer{margin-top:56px;color:var(--muted);font-size:14px}

  @media (max-width:860px){
    .hero{grid-template-columns:1fr;gap:26px;padding-top:22px}
    .hero-phone{max-width:240px}
    .demo{min-height:0}
    .row,.row.flip{grid-template-columns:1fr;gap:20px;padding:22px}
    .row.flip .rtext{order:0}
    .row .phone{max-width:210px;justify-self:center}
  }
  @media (max-width:560px){.two{grid-template-columns:1fr}main{padding:16px 16px 56px}}
  @media (prefers-reduced-motion:reduce){html{scroll-behavior:auto}.bub{animation:none;opacity:1;transform:none}.btn{transition:none}}
"""

PRESSED = ' aria-pressed="true"'

btns = "".join(f'<button data-set="{c}"{PRESSED if c=="en" else ""}>{names[c]}</button>' for c in order)
sections = "".join(section(c, L[c], X[c], c=="en") for c in order)
en = L["en"]

out = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{e(en["title"])}</title>
<meta name="description" content="{e(en["meta"])}">
<link rel="canonical" href="{SITE}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}">
<meta property="og:title" content="{e(en["title"])}">
<meta property="og:description" content="{e(en["meta"])}">
<meta property="og:image" content="{SITE}og.png">
<meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(en["title"])}">
<meta name="twitter:description" content="{e(en["meta"])}">
<meta name="twitter:image" content="{SITE}og.png">
<meta name="apple-itunes-app" content="app-id=6801931802">
<meta name="theme-color" content="#0B0C0E">
<link rel="icon" type="image/png" sizes="32x32" href="favicon-32.png">
<link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<script>if(/\\.github\\.io$/.test(location.hostname)){{location.replace("{SITE}"+location.search+location.hash);}}</script>
<style>{CSS}</style>
</head>
<body>
<main>
<header>
  <a class="home" href="./"><img src="icon-64.png" alt="" width="34" height="34">Prau</a>
  <nav id="langs" aria-label="Language">{btns}</nav>
  <a class="navcta" href="{APPSTORE}" data-i18n="nav_cta">App Store</a>
</header>
{sections}
</main>
<script>
(function(){{
  var titles={json.dumps({c:L[c]["title"] for c in order}, ensure_ascii=False)};
  var navcta={json.dumps({c:X[c]["nav_cta"] for c in order}, ensure_ascii=False)};
  var metas={json.dumps({c:L[c]["meta"] for c in order}, ensure_ascii=False)};
  var sections=document.querySelectorAll('section[data-lang]');
  var buttons=document.querySelectorAll('#langs button');
  var reduce=window.matchMedia&&window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var timer=null;
  function esc(s){{return s.replace(/[&<>]/g,function(c){{return {{'&':'&amp;','<':'&lt;','>':'&gt;'}}[c];}});}}
  function render(box,conv){{
    box.innerHTML=conv.map(function(m,i){{return '<div class="bub '+(i%2?'b':'a')+'"><span class="flag" aria-hidden="true">'+m[0]+'</span>'+esc(m[1])+'</div>';}}).join('');
  }}
  function startDemo(sec){{
    if(timer){{clearInterval(timer);timer=null;}}
    var box=sec.querySelector('.demo'); if(!box) return;
    var demos=JSON.parse(box.getAttribute('data-demos')); var i=0;
    render(box,demos[0]);
    if(reduce||demos.length<2) return;
    timer=setInterval(function(){{ if(document.hidden) return; i=(i+1)%demos.length; render(box,demos[i]); }},6500);
  }}
  function show(l){{
    var cur=null;
    sections.forEach(function(s){{var on=s.dataset.lang===l; s.classList.toggle('active',on); if(on) cur=s;}});
    buttons.forEach(function(b){{b.setAttribute('aria-pressed',b.dataset.set===l?'true':'false');}});
    document.documentElement.lang=l;
    document.title=titles[l]||titles.en;
    var m=document.querySelector('meta[name="description"]'); if(m) m.setAttribute('content',metas[l]||metas.en);
    var nc=document.querySelector('.navcta'); if(nc) nc.textContent=navcta[l]||'App Store';
    try{{history.replaceState(null,'','#'+l);}}catch(e){{}}
    if(cur) startDemo(cur);
  }}
  buttons.forEach(function(b){{b.addEventListener('click',function(){{show(b.dataset.set);}});}});
  var known={json.dumps(order)};
  var fromHash=location.hash.replace('#','').split('-')[0];
  var fromNav=(navigator.language||'en').slice(0,2).toLowerCase();
  show(known.indexOf(fromHash)>=0?fromHash:(known.indexOf(fromNav)>=0?fromNav:'en'));
}})();
</script>
</body>
</html>
'''
open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(out)
print(len(out), "bytes")
