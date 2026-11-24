import json
exec(open('gen_ads.py').read().split('ADS=[')[0])   # CSS, dev(), LOGO, S, P
exec(open('batch3.py').read())
man=[]
# Instagram: device ads on gradient art
for n,bgp,cls,kind,shot,small,big,sub,pl,pb,cta,cap in IG:
    pill=f'<div class="pill">{pl} <b>{pb}</b></div>' if pl else f'<div class="pill"><b>{pb}</b></div>'
    site='global-link.ae' if ('website' in sub or 'school' in sub or 'private' in sub or 'website' in cap) else 'demo.global-link.ae'
    html=f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head><body class="{cls}"><img class="bg" src="bg3/{n}.jpg"><div class="gt"></div><div class="gb"></div><div class="stage">{dev(kind,shot)}</div><div class="h"><small>{small}</small>{big}</div><div class="s">{sub}</div>{pill}<div class="cta">{cta}</div><div class="brand"><img src="{LOGO}">Global Link</div><div class="site">{site}</div></body></html>'
    open(n+'.html','w').write(html); man.append([n,1080,1350])
# LinkedIn: typographic insight cards
LCSS='''*{box-sizing:border-box;margin:0}body{width:1080px;height:1350px;background:#0b1020;font-family:Inter,'Noto Naskh Arabic',sans-serif;color:#eef2ff;position:relative;overflow:hidden}
.g1{position:absolute;width:900px;height:900px;border-radius:50%;background:radial-gradient(circle,rgba(124,92,255,.38),transparent 65%);top:-300px;right:-300px}
.g2{position:absolute;width:800px;height:800px;border-radius:50%;background:radial-gradient(circle,rgba(56,189,248,.2),transparent 65%);bottom:-260px;left:-250px}
.m{position:absolute;top:100px;left:90px;right:90px}
.k{font-size:26px;letter-spacing:.18em;text-transform:uppercase;color:#a5b4fc;font-weight:700;display:flex;align-items:center;gap:18px}
.k:before{content:"";width:46px;height:4px;background:#7c5cff}
.h{margin-top:34px;font-size:70px;line-height:1.08;font-weight:800;letter-spacing:-.02em}
.b{margin-top:36px;font-size:32px;line-height:1.45;color:#c7d2fe;max-width:820px}
.st{position:absolute;left:90px;bottom:180px}.st b{display:block;font-size:104px;font-weight:800;color:#fbbf24;letter-spacing:-.03em;line-height:1}.st small{display:block;margin-top:10px;font-size:26px;color:#a5b4fc}
.sh{position:absolute;right:-30px;bottom:150px;width:560px;border-radius:18px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.55);border:6px solid #1e2440;transform:rotate(-4deg)}
.sh img{width:100%;display:block}
.ft{position:absolute;left:90px;right:90px;bottom:60px;display:flex;justify-content:space-between;align-items:center;font-size:24px;color:#a5b4fc;border-top:1px solid rgba(165,180,252,.25);padding-top:26px}
.ft span{display:flex;align-items:center;gap:14px;color:#eef2ff;font-weight:700}.ft img{width:40px;height:40px;border-radius:10px}
body.ar .m{direction:rtl;text-align:right;font-family:'Noto Naskh Arabic',sans-serif}body.ar .h{font-size:66px;line-height:1.35;letter-spacing:0}body.ar .k{letter-spacing:0;font-size:30px}
body.ar .st{left:auto;right:90px;text-align:right}body.ar .sh{right:auto;left:-30px;transform:rotate(4deg)}
'''
for n,kick,head,body,sb,ss,shot,cap in LI:
    ar=' class="ar"' if any('؀'<=c<='ۿ' for c in head) else ''
    html=f'<!doctype html><html><head><meta charset="utf-8"><style>{LCSS}</style></head><body{ar}><div class="g1"></div><div class="g2"></div><div class="m"><div class="k">{kick}</div><div class="h">{head}</div><div class="b">{body}</div></div><div class="st"><b>{sb}</b><small>{ss}</small></div><div class="sh"><img src="{shot}"></div><div class="ft"><span><img src="{LOGO}">Global Link International</span>{"demo.global-link.ae" if "demo." in cap else "global-link.ae"}</div></body></html>'
    open(n+'.html','w').write(html); man.append([n,1080,1350])
json.dump(man,open('manifest-b3.json','w')); print(len(man))
