import cairosvg
from PIL import Image
from temple import temple
def svg(bg, tf, win, tc, mor, stroke=''):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
<defs>{bg[0]}</defs><rect width="512" height="512" fill="{bg[1]}"/>
{temple(tf,win,mor)}
<text x="256" y="468" text-anchor="middle" font-family="DejaVu Sans" font-weight="bold" font-size="112" letter-spacing="4" fill="{tc}" {stroke}>EQ43</text></svg>'''
A=svg(('<linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1f4e8c"/><stop offset="1" stop-color="#0a1f44"/></linearGradient>','url(#g)'),'#d9dde3','#163a6e','#e8c35a','#e8c35a')
B=svg(('<linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f3d77f"/><stop offset="1" stop-color="#b8892a"/></linearGradient>','url(#g)'),'#eef0f3','#8a6a22','#0a1f44','#0a1f44')
for n,s in (('a',A),('b',B)):
    open(f'icon-{n}.svg','w').write(s)
    for sz,name in ((180,'apple-touch-icon'),(192,'icon-192'),(512,'icon-512'),(32,'favicon-32')):
        cairosvg.svg2png(bytestring=s.encode(),write_to=f'{name}-{n}.png',output_width=sz,output_height=sz)
    cairosvg.svg2png(bytestring=s.encode(),write_to=f'big-{n}.png',output_width=600,output_height=600)
p=Image.new('RGB',(1300,700),'#ddd')
for i,n in enumerate('ab'):
    p.paste(Image.open(f'big-{n}.png'),(40+i*640,50))
    p.paste(Image.open(f'apple-touch-icon-{n}.png').resize((60,60)),(40+i*640+620-80,0)) if False else None
p.save('preview.png')
import shutil
for f in ('apple-touch-icon','icon-192','icon-512','favicon-32'): shutil.copy(f'{f}-a.png',f'{f}.png')
