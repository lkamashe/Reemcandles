import subprocess, sys, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np

SRC="/root/.claude/uploads/6797c805-cfbb-54da-9770-5168982e29fc/3373a5cc-reem_tita_30s_native.mp4"
OUT=sys.argv[1]
W,H=1080,1920; FPS=24
GOLD=(197,160,89); CREAM=(253,251,247)
F_B="fonts/Amiri-Bold.ttf"; F_R="fonts/Amiri-Regular.ttf"
def font(p,s): return ImageFont.truetype(p,s,layout_engine=ImageFont.Layout.RAQM)

def rtl_line(words, gold_idx, f, color_main=CREAM, color_gold=GOLD, pad_x=46, pad_y=20, border=2):
    sp=int(f.size*0.26)
    ws=[f.getlength(w,direction='rtl',language='ar') for w in words]
    tw=sum(ws)+sp*(len(words)-1)
    asc,desc=f.getmetrics()
    w=int(tw+2*pad_x); h=int(asc+desc+2*pad_y)
    img=Image.new('RGBA',(w,h),(0,0,0,0))
    d=ImageDraw.Draw(img)
    d.rounded_rectangle((0,0,w-1,h-1),radius=h//2,fill=(18,20,18,178),outline=GOLD+(255,),width=border)
    x=w-pad_x; base=pad_y+asc
    for i,wd in enumerate(words):
        d.text((x,base),wd,font=f,fill=(color_gold if i in gold_idx else color_main)+(255,),anchor='rs',direction='rtl',language='ar')
        x-=ws[i]+sp
    return img

# (start,end,words,gold index)
SUBS=[
 (2.35,3.65,["هل","هي","حلوى؟"],[2]),
 (9.05,10.25,["هذه","هدية","لك."],[1]),
 (11.20,12.85,["أحب","هذه","الهدايا!"],[2]),
 (14.02,15.15,["أين","الحلوى؟"],[1]),
 (16.42,18.40,["لماذا","هي","بيضاء","هكذا؟"],[2]),
 (18.70,20.20,["هذه","شمعة","يا","تيتا."],[1]),
 (20.90,23.45,["شمعة؟","ظننتها","حلوى!"],[2]),
 (23.70,25.45,["رائحتها","أطيب","من","الحلوى!"],[1]),
 (25.50,27.65,["من","ريم.","عطرها","من","غراس."],[4]),
 (27.55,28.60,["حسناً."],[]),
 (28.95,30.20,["وأين","الحلوى؟"],[1]),
]
fs=font(F_B,60)
sub_imgs=[rtl_line(w,g,fs) for (_,_,w,g) in SUBS]
hook=rtl_line(["تيتا:","هل","هذه","حلوى؟"],[3],font(F_B,80),pad_x=58,pad_y=24,border=3)
HOOK=(0.0,2.35)
SUB_BOTTOM=1545; HOOK_CY=330

def alpha_at(t,a,b,fi=0.12,fo=0.15):
    if t<a or t>b: return 0.0
    return max(0.0,min(1.0,(t-a)/fi,(b-t)/fo)) if True else 1.0

def paste(frame,img,cx,top,alpha):
    if alpha<=0: return
    im=img if alpha>=0.999 else img.copy()
    if alpha<0.999:
        a=im.getchannel('A').point(lambda v:int(v*alpha)); im.putalpha(a)
    frame.alpha_composite(im,(int(cx-im.width/2),int(top)))

def zoom(t):
    z=0.0
    if t>=12.6:
        if t<14.0: z=(t-12.6)/1.4
        elif t<14.9: z=1.0
        elif t<15.4: z=1-(t-14.9)/0.5
    z=z*z*(3-2*z) if 0<z<1 else z
    z2=0.0
    if t>=28.9: z2=min(1.0,(t-28.9)/1.0)
    z2=z2*z2*(3-2*z2)
    return 1.0+0.08*z+0.05*z2

# ---- end card ----
def end_card():
    bg=Image.new('RGB',(W,H),(31,42,30))
    yy,xx=np.mgrid[0:H,0:W]
    r=np.sqrt(((xx-W/2)/(W*0.8))**2+((yy-H*0.42)/(H*0.6))**2)
    g=np.clip(1-r,0,1)[...,None]
    arr=np.array(bg).astype(float)*(1-g)+np.array((52,68,50),float)*g
    card=Image.fromarray(arr.astype('uint8')).convert('RGBA')
    c=Image.open('logo_crop.png').convert('RGB')
    c=c.resize((int(c.width*1.7),int(c.height*1.7)),Image.LANCZOS)
    a=np.array(c).astype(float)
    alpha=np.clip((a[...,0]-a[...,2]-22)/70,0,1)*np.clip((a[...,0]-80)/60,0,1)
    la=Image.fromarray((alpha*255).astype('uint8')).filter(ImageFilter.GaussianBlur(0.4))
    logo=c.convert('RGBA'); logo.putalpha(la)
    s=560/logo.width; logo=logo.resize((560,int(logo.height*s)),Image.LANCZOS)
    card.alpha_composite(logo,(W//2-logo.width//2,560))
    d=ImageDraw.Draw(card)
    d.text((W//2,1215),"قريباً",font=font(F_B,150),fill=GOLD+(255,),anchor='ms',direction='rtl',language='ar')
    d.text((W//2,1345),"آخر تشرين الثاني",font=font(F_R,72),fill=CREAM+(255,),anchor='ms',direction='rtl',language='ar')
    d.text((W//2,1470),"@reemcandles.co",font=font(F_R,56),fill=(225,220,210,255),anchor='ms')
    return card.convert('RGB')

# ---- decode + render ----
SW,SH=768,1344
dec=subprocess.Popen(["ffmpeg","-v","error","-i",SRC,"-f","rawvideo","-pix_fmt","rgb24","-"],stdout=subprocess.PIPE)
DUR_END=2.5
enc=subprocess.Popen(["ffmpeg","-v","error","-y","-f","rawvideo","-pix_fmt","rgb24","-s",f"{W}x{H}","-r",str(FPS),"-i","-","-i",SRC,
  "-filter_complex","[1:a]apad=whole_dur=32.667,atrim=0:32.667[a]","-map","0:v","-map","[a]","-c:v","libx264","-preset","medium","-crf","20","-pix_fmt","yuv420p",
  "-c:a","aac","-b:a","192k","-t","32.667","-movflags","+faststart",OUT],stdin=subprocess.PIPE)
n=0; last=None
base_w=SH*9/16
while True:
    buf=dec.stdout.read(SW*SH*3)
    if len(buf)<SW*SH*3: break
    t=n/FPS
    src=Image.frombytes("RGB",(SW,SH),buf)
    z=zoom(t)
    w=base_w/z; h=SH/z
    fx,fy=(0.47,0.36) if t<20 else (0.45,0.40)
    left=(SW-base_w)/2+(base_w-w)*fx; top=(SH-h)*fy
    fr=src.resize((W,H),Image.LANCZOS,box=(left,top,left+w,top+h)).convert('RGBA')
    paste(fr,hook,W/2,HOOK_CY-hook.height/2,alpha_at(t,*HOOK,fi=0.25,fo=0.3))
    for (a,b,_,_),im in zip(SUBS,sub_imgs):
        al=alpha_at(t,a,b)
        if al>0: paste(fr,im,W/2,SUB_BOTTOM-im.height,al)
    out=fr.convert('RGB'); last=out
    enc.stdin.write(out.tobytes()); n+=1
ec=end_card()
for k in range(int(DUR_END*FPS)):
    m=min(1.0,k/8)
    enc.stdin.write(Image.blend(last,ec,m).tobytes() if m<1 else ec.tobytes())
enc.stdin.close(); enc.wait(); print("frames",n,"+",int(DUR_END*FPS))
