import os, pathlib
from playwright.sync_api import sync_playwright

D = pathlib.Path(__file__).parent
BG = D / "bg"
OUT = D
G, IV, GOLD, RED, INK = "#0e4d35", "#f4f1e8", "#d4ad57", "#b3122b", "#1c2321"

CSS = f"""
*{{box-sizing:border-box;margin:0}}
body{{width:1080px;height:1350px;font-family:'Inter Display','Inter',sans-serif;}}
.c{{position:relative;width:1080px;height:1350px;overflow:hidden;color:{IV};background:{INK}}}
.bg{{position:absolute;inset:0;background-size:cover;background-position:center}}
.ov{{position:absolute;inset:0}}
.in{{position:absolute;inset:0;padding:84px 84px 76px;display:flex;flex-direction:column;justify-content:space-between}}
.top{{display:flex;justify-content:space-between;font-size:26px;letter-spacing:.16em;text-transform:uppercase;font-weight:500;opacity:.92}}
.big{{font-size:420px;line-height:.82;font-weight:700;letter-spacing:-.04em;color:{GOLD}}}
.rule{{width:150px;height:5px;background:{RED};margin:34px 0 30px}}
.h{{font-size:64px;line-height:1.1;font-weight:600;max-width:880px}}
.ar{{font-family:'Noto Naskh Arabic',serif;direction:rtl;font-size:58px;font-weight:700;line-height:1.5;margin-top:14px}}
.sub{{font-size:34px;line-height:1.4;max-width:860px;opacity:.95;margin-top:18px}}
.foot{{display:flex;justify-content:space-between;align-items:flex-end;font-size:26px;font-weight:500;gap:30px}}
.pill{{background:{GOLD};color:{INK};font-weight:700;border-radius:999px;padding:18px 40px;font-size:38px;white-space:nowrap}}
.brand{{text-align:right;line-height:1.35;opacity:.95}}
.brand b{{font-weight:700;letter-spacing:.04em}}
"""

def brand(sub="demo.global-link.ae"):
    return f'<div class="brand"><b>GLOBAL LINK INTERNATIONAL</b><br>{sub}</div>'

def page(bg, overlay, body):
    bgdiv = f'<div class="bg" style="background-image:url(file://{BG/bg})"></div>' if bg else ''
    return f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="c">{bgdiv}<div class="ov" style="background:{overlay}"></div><div class="in">{body}</div></div></body></html>'

POSTS = {
"p1-launch": page("lattice.jpg", "linear-gradient(180deg, rgba(8,35,25,.75) 0%, rgba(8,35,25,0) 14%), radial-gradient(ellipse at 50% 48%, rgba(10,45,32,.6), rgba(10,45,32,.2) 70%)", f"""
 <div class="top"><span>Eid Al Etihad</span><span>26 Nov – 10 Dec</span></div>
 <div style="text-align:center;display:flex;flex-direction:column;align-items:center">
   <div class="big">55</div><div class="rule"></div>
   <div class="h" style="font-size:60px">Our Eid Al Etihad offer<br>for UAE businesses</div>
   <div class="ar">عرض عيد الاتحاد</div>
 </div>
 <div class="foot"><span class="pill">20% OFF</span>{brand("Websites & business portals")}</div>"""),

"p2-family": page("dallah.jpg", "linear-gradient(180deg, rgba(8,30,20,.88) 0%, rgba(8,30,20,.55) 42%, rgba(0,0,0,0) 62%, rgba(0,0,0,.55) 100%)", f"""
 <div><div class="top"><span>Eid Al Etihad</span><span>UAE family businesses</span></div>
   <div class="h" style="margin-top:70px">Many UAE companies began as a family business.</div>
   <div class="rule"></div>
   <div class="sub">We build the systems that help them grow: staff, payroll, invoices and customers, in Arabic and English.</div></div>
 <div class="foot"><span class="pill">20% off until 10 Dec</span>{brand()}</div>"""),

"p3-commemoration": page(None, "linear-gradient(180deg,#1c2321,#141a18)", f"""
 <div class="top" style="color:#c9cfcc"><span>30 November</span><span></span></div>
 <div style="text-align:center;display:flex;flex-direction:column;align-items:center;color:#eef1ef">
   <div class="ar" style="font-size:92px;color:#eef1ef">يوم الشهيد</div>
   <div class="h" style="font-size:72px;font-weight:500;margin-top:10px">Commemoration Day</div>
   <div style="width:90px;height:2px;background:#8f9a95;margin:46px 0"></div>
   <div class="sub" style="text-align:center;max-width:780px">We remember with pride the sons of the UAE who gave their lives for the nation.</div>
   <div class="ar" style="font-size:44px;font-weight:500;margin-top:30px;color:#d9dedb">نستذكر بكل فخر واعتزاز تضحيات شهداء الوطن</div>
 </div>
 <div class="foot" style="justify-content:center;color:#aab3af"><span>Global Link International</span></div>"""),

"p4-eve": page("skyline.jpg", "linear-gradient(180deg, rgba(4,28,32,.65) 0%, rgba(4,28,32,.2) 45%, rgba(0,0,0,0) 60%, rgba(0,0,0,.6) 100%)", f"""
 <div><div class="top"><span>1 December</span><span>Eve of the 55th</span></div>
   <div class="h" style="margin-top:80px;font-size:76px">Tomorrow the UAE celebrates 55 years of the Union.</div>
   <div class="rule"></div>
   <div class="ar">عيد الاتحاد الخامس والخمسون</div></div>
 <div class="foot"><span></span>{brand("Abu Dhabi")}</div>"""),

"p5-greeting": page("dunes.jpg", "linear-gradient(180deg, rgba(40,28,8,.55) 0%, rgba(40,28,8,.45) 50%, rgba(30,20,5,.55) 100%)", f"""
 <div class="top" style="color:#fffaf0"><span>2 December 2026</span><span></span></div>
 <div style="text-align:center;display:flex;flex-direction:column;align-items:center;margin-top:-160px">
   <div class="big" style="color:#fffaf0;text-shadow:0 6px 40px rgba(90,60,10,.35)">55</div><div class="rule"></div>
   <div class="h" style="color:#fffaf0">Happy Eid Al Etihad</div>
   <div class="ar" style="color:#fffaf0">كل عام والإمارات بخير</div>
 </div>
 <div class="foot" style="justify-content:center;color:#fffaf0"><span>From all of us at Global Link International</span></div>"""),

"p6-december": page("dallah.jpg", "linear-gradient(180deg, rgba(8,30,20,.9) 0%, rgba(8,30,20,.6) 40%, rgba(0,0,0,0) 60%, rgba(0,0,0,.6) 100%)", f"""
 <div><div class="top"><span>Eid Al Etihad offer</span><span>Until 10 Dec</span></div>
   <div class="h" style="margin-top:70px;font-size:84px">Start in December.<br>Go live in January.</div>
   <div class="rule"></div>
   <div class="sub">Most portals are ready in 2 to 3 weeks: HR and payroll, operations, ISO 9001, nursery and bilingual websites.</div></div>
 <div class="foot"><span class="pill">20% OFF</span>{brand()}</div>"""),

"p7-4days": page("lattice.jpg", "linear-gradient(180deg, rgba(8,35,25,.75) 0%, rgba(8,35,25,0) 14%), radial-gradient(ellipse at 50% 48%, rgba(10,45,32,.65), rgba(10,45,32,.25) 70%)", f"""
 <div class="top"><span>Eid Al Etihad offer</span><span></span></div>
 <div style="text-align:center;display:flex;flex-direction:column;align-items:center">
   <div class="big" style="font-size:300px">4 days</div><div class="rule"></div>
   <div class="h">left to book with 20% off</div>
   <div class="ar">باقي 4 أيام على انتهاء العرض</div>
 </div>
 <div class="foot"><span class="pill">Ends Thu 10 Dec</span>{brand()}</div>"""),

"p8-lastday": page("skyline.jpg", "linear-gradient(180deg, rgba(4,28,32,.7) 0%, rgba(4,28,32,.25) 45%, rgba(0,0,0,0) 60%, rgba(0,0,0,.65) 100%)", f"""
 <div><div class="top"><span>Eid Al Etihad offer</span><span>10 Dec</span></div>
   <div class="big" style="font-size:230px;margin-top:60px">Last day</div>
   <div class="rule"></div>
   <div class="h">20% off websites and business portals</div>
   <div class="ar">آخر يوم للعرض</div></div>
 <div class="foot"><span class="pill">Book today</span>{brand()}</div>"""),
}

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width":1080,"height":1350})
    for name, html in POSTS.items():
        f = D / f"_{name}.html"; f.write_text(html, encoding="utf-8")
        pg.goto(f"file://{f}"); pg.wait_for_timeout(400)
        pg.screenshot(path=str(OUT/f"{name}.jpg"), type="jpeg", quality=90)
        f.unlink()
    b.close()
print("ok")
