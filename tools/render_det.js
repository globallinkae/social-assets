// Deterministic frame-by-frame render of a reel HTML (no real-time recording).
// node render_det.js <reel.html> <outdir> <durSec> <phoneFramesDir> <lapFramesDir>
const {chromium}=require('playwright');const path=require('path');const fs=require('fs');
(async()=>{
 const [html,out,durS,phDir,lpDir]=process.argv.slice(2);const FPS=30;const N=Math.round(parseFloat(durS)*FPS);
 fs.mkdirSync(out,{recursive:true});
 const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});
 await p.goto('file://'+path.resolve(__dirname,html));await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(500);
 const ph=fs.readdirSync(phDir).filter(f=>f.endsWith('.jpg')).sort().map(f=>'file://'+path.resolve(phDir,f));
 const lp=fs.readdirSync(lpDir).filter(f=>f.endsWith('.jpg')).sort().map(f=>'file://'+path.resolve(lpDir,f));
 await p.evaluate(({ph,lp})=>{
   window.setTimeout=()=>0; // go() uses setTimeout only for the progress bar; we drive it ourselves
   const st=document.createElement('style');st.textContent='.phone img.vf{width:100%;height:100%;object-fit:cover;object-position:top;display:block}.lap img.vf{width:100%;display:block}';document.head.appendChild(st);
   for(const id of ['v1','v2']){const v=document.getElementById(id);const im=document.createElement('img');im.id=id;im.className='vf';im.play=()=>{};im.src=(id==='v1'?ph:lp)[0];v.replaceWith(im);}
   window.__ph=ph;window.__lp=lp;
   const src=document.querySelector('script:not([src])').textContent;
   window.__T=eval(src.match(/const T=(\[[^;]*\]);/)[1]);
   window.__bar=parseFloat(src.match(/width ([0-9.]+)s linear/)[1]);
   window.__k=-1;
 },{ph,lp});
 for(let n=0;n<N;n++){
   const t=n/FPS;
   await p.evaluate(async(t)=>{
     const T=window.__T;let k=0;for(let i=0;i<T.length;i++) if(t>=T[i][0]-1e-6) k=i;
     if(k!==window.__k){window.__k=k;go(T[k][1]);}
     const Tk=T[k][0];
     for(const a of document.getAnimations()){
       a.pause();
       const nm=a.animationName||'';
       if(nm==='float'||nm==='glow') a.currentTime=t*1000;
       else if(nm==='flash' && k===0) a.currentTime=1000;
       else a.currentTime=Math.max(0,(t-Tk)*1000);
     }
     const bar=document.getElementById('bar');
     if(bar){bar.style.transition='none';bar.style.width=(k===T.length-1?Math.min(1,Math.max(0,(t-Tk-0.3)/window.__bar))*100:0)+'%';}
     const setF=(id,arr,ts)=>{const im=document.getElementById(id);const i=Math.min(arr.length-1,Math.max(0,Math.floor(ts*30)));const s=arr[i];if(im.src!==s){im.src=s;}return im;};
     const ims=[];
     if(k>=2) ims.push(setF('v1',window.__ph,t-T[2][0]));
     if(k>=3) ims.push(setF('v2',window.__lp,t-T[3][0]));
     await Promise.all(ims.map(im=>im.decode().catch(()=>{})));
   },t);
   await p.screenshot({path:path.join(out,String(n).padStart(5,'0')+'.jpg'),type:'jpeg',quality:94});
 }
 await b.close();console.log('frames',N);
})();
