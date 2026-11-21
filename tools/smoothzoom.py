"""Smooth Ken Burns TikTok render for Eid stills: sub-pixel zoom (cv2 cubic), clear first frame, fade-out last 0.3 s.
python3 smoothzoom.py <still.jpg> <audio_src.mp4> <out.mp4>"""
import cv2,numpy as np,subprocess,sys
still_p,aud,out=sys.argv[1:4]
still=cv2.imread(still_p).astype(np.float32)
s=1920/1350; bg=cv2.resize(still,(round(1080*s),1920)); x=(bg.shape[1]-1080)//2; bg=bg[:,x:x+1080]
bg=cv2.GaussianBlur(bg,(0,0),30)
hsv=cv2.cvtColor(np.clip(bg,0,255).astype(np.uint8),cv2.COLOR_BGR2HSV).astype(np.float32); hsv[...,1]=np.clip(hsv[...,1]*1.25,0,255)
bg=cv2.cvtColor(hsv.astype(np.uint8),cv2.COLOR_HSV2BGR).astype(np.float32)*0.62
comp=bg.copy(); comp[285:285+1350]=still
dur=float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration','-of','csv=p=0',aud],capture_output=True,text=True).stdout)
N=round(dur*30); p=subprocess.Popen(['ffmpeg','-loglevel','error','-y','-f','rawvideo','-pix_fmt','bgr24','-s','1080x1920','-r','30','-i','-','-i',aud,'-map','0:v','-map','1:a','-c:v','libx264','-preset','medium','-crf','18','-pix_fmt','yuv420p','-c:a','copy','-shortest','-movflags','+faststart',out],stdin=subprocess.PIPE)
for n in range(N):
    S=1+0.108*n/(N-1); M=np.float32([[S,0,540*(1-S)],[0,S,960*(1-S)]])
    f=cv2.warpAffine(comp,M,(1080,1920),flags=cv2.INTER_CUBIC,borderMode=cv2.BORDER_REFLECT)
    k=min(1,(N-1-n)/9)  # fade out over last 0.3 s
    p.stdin.write(np.clip(f*k,0,255).astype(np.uint8).tobytes())
p.stdin.close(); p.wait(); print(out,N)
