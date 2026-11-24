"""Voice-over reel generator. python3 reelgen.py <spec.json>  (or import make)."""
import json, subprocess, sys, os, glob, re
F='/tmp/claude-0/-home-claude/2d74f7b3-642a-5c39-a7ec-8eada70396a8/scratchpad/flow/'
S='/tmp/claude-0/-home-claude/2d74f7b3-642a-5c39-a7ec-8eada70396a8/scratchpad/site5/assets/shots/'
MUS='/tmp/claude-0/-home-claude/2d74f7b3-642a-5c39-a7ec-8eada70396a8/scratchpad/reel/'
LOGO='file:///tmp/claude-0/-home-claude/2d74f7b3-642a-5c39-a7ec-8eada70396a8/scratchpad/book/img/logo-mark.png'
BASE=open(F+'reel-hr.html').read()
def sh(c): subprocess.run(c,shell=True,check=True)
def slideshow(shots, w, h, per, out, trans='slideleft'):
    """shots: list of files -> webm of w×h with xfade transitions, `per` seconds each"""
    n=len(shots); ins=' '.join(f'-loop 1 -t {per} -i "{s}"' for s in shots)
    fc=''.join(f'[{i}]scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h}:0:0,fps=30[v{i}];' for i in range(n))
    prev='v0'; off=per-0.35
    for i in range(1,n):
        fc+=f'[{prev}][v{i}]xfade=transition={trans}:duration=0.35:offset={off:.2f}[x{i}];'; prev=f'x{i}'; off+=per-0.35
    fc=fc.rstrip(';')+f';[{prev}]format=yuv420p[o]' if n>1 else fc+f'[v0]format=yuv420p[o]'
    sh(f'ffmpeg -y -loglevel error {ins} -filter_complex "{fc}" -map "[o]" -c:v libvpx-vp9 -b:v 0 -crf 22 -an "{out}"')
def make(sp):
    name=sp['name']; T=sp['t']  # [t1,t2,t3,t4] scene starts for s1..s4
    ph=F+f'rec/{name}-phone.webm'; lp=F+f'rec/{name}-laptop.webm'
    slideshow(sp['phone'],600,1298,(T[2]-T[1])/len(sp['phone'])+0.35,ph)
    slideshow(sp['laptop'],1000,625,(T[3]-T[2])/len(sp['laptop'])+0.35,lp,'slideup')
    h=BASE
    rep=[
     ('src="s1-monthend.jpg"',f'src="{sp["bg0"]}"'),('src="adc-stairs-uec.jpg"',f'src="{sp["bg1"]}"'),
     ('HR · PAYROLL',sp['tag']),
     ('<span>Still running HR &amp; payroll</span><br><span class="y">on spreadsheets?</span>',sp['h0']),
     ('Month-end at 11 pm. Again.',sp['sub0']),
     ('Your company.<br><em>Its own portal.</em>',sp['h1']),
     ('<div><b>50–650</b><small>employees</small></div><div><b>EN · AR</b><small>both languages</small></div><div><b>WPS</b><small>bank file</small></div>',sp['kv']),
     ('Everything in<br><em>one place.</em>',sp['h2']),
     ('src="rec/hr-phone-hd.webm"',f'src="rec/{name}-phone.webm"'),
     ('<span class="chip ok pop d3" style="left:40px;top:700px">✓ Attendance</span><span class="chip ok pop d4" style="right:40px;top:860px">✓ Leave</span><span class="chip ok pop d5" style="left:40px;top:1080px">✓ Payslips</span><span class="chip ok pop d6" style="right:40px;top:1260px">✓ WPS file</span><span class="chip pop d7" style="left:40px;top:1480px">English · عربي</span>',
      ''.join(f'<span class="chip {"ok" if i<4 else ""} pop d{i+3}" style="{["left:40px;top:700px","right:40px;top:860px","left:40px;top:1080px","right:40px;top:1260px","left:40px;top:1480px"][i]}">{c}</span>' for i,c in enumerate(sp['chips']))),
     ('We set it up.<br><em>You just log in.</em>',sp['h3']),
     ('src="rec/hr-laptop-hd.webm"',f'src="rec/{name}-laptop.webm"'),
     ('Payroll run · payslips · WPS file — in minutes, not evenings.',sp['sub3']),
     ('Try the<br><em>live demo.</em>',sp['h4']),
     ('<div class="url up d3">demo.global-link.ae</div>',f'<div class="url up d3" style="font-size:{sp.get("urlsize",64)}px">{sp.get("url","demo.global-link.ae")}</div>'),
     ('Sample data · five roles · resets nightly',sp.get('sub4','Sample data · five roles · resets nightly')),
     ("const T=[[0,'s0'],[3.6,'s1'],[7.4,'s2'],[13.0,'s3'],[17.2,'s4']];",f"const T=[[0,'s0'],[{T[0]},'s1'],[{T[1]},'s2'],[{T[2]},'s3'],[{T[3]},'s4']];"),
     ("width 4.6s linear",f"width {sp['dur']-T[3]-0.4:.1f}s linear"),
    ]
    for a,b in rep:
        assert a in h, a[:60]
        h=h.replace(a,b)
    if sp.get('ar'):
        h=h.replace('</style>','@font-face{font-family:A;font-weight:700;src:url(file:///tmp/claude-0/-home-claude/2d74f7b3-642a-5c39-a7ec-8eada70396a8/scratchpad/brand/node_modules/@fontsource/ibm-plex-sans-arabic/files/ibm-plex-sans-arabic-arabic-700-normal.woff2)}body{font-family:A,M;direction:rtl}.h{font-size:84px!important;line-height:1.15!important}.brand{left:auto;right:60px;flex-direction:row-reverse}.tag{right:auto;left:60px}.kv{direction:rtl}</style>')
    open(F+f'reel-{name}.html','w').write(h)
    dur=sp['dur']
    # deterministic frame-by-frame render (smooth), then mux VO + music
    fr=F+f'det/{name}-frames'; sh(f'rm -rf "{fr}"')
    for k,v in (('ph',ph),('lp',lp)):
        d=F+f'det/{name}-{k}'; sh(f'rm -rf "{d}" && mkdir -p "{d}" && ffmpeg -loglevel error -i "{v}" -vf fps=30 -q:v 2 "{d}/%05d.jpg"')
    sh(f'cd {F} && node render_det.js reel-{name}.html "{fr}" {dur} det/{name}-ph det/{name}-lp')
    out=F+f'out/{name}.mp4'
    sh(f'ffmpeg -y -loglevel error -framerate 30 -i "{fr}/%05d.jpg" -i "{F}{sp["vo"]}" -i "{MUS}{sp["music"]}/music.wav" -filter_complex "[2:a]atrim=0:{dur},volume={sp.get("mvol",0.12)},afade=t=out:st={dur-2.2:.2f}:d=2.2[m];[1:a]adelay=300:all=1[vo];[vo][m]amix=inputs=2:duration=longest:normalize=0,atrim=0:{dur}[a]" -map 0:v -map "[a]" -t {dur} -c:v libx264 -preset medium -crf 19 -pix_fmt yuv420p -r 30 -c:a aac -b:a 192k -movflags +faststart "{out}"')
    off=0
    print('built',out,'offset',off)
if __name__=='__main__':
    for f in sys.argv[1:]: make(json.load(open(f)))
