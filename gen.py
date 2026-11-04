import cairosvg
from PIL import Image
def temple(fill, win):
    return f'''<g fill="{fill}">
<rect x="226" y="198" width="60" height="64"/>
<rect x="234" y="150" width="44" height="50"/>
<polygon points="234,150 256,128 278,150"/>
<polygon points="244,132 256,62 268,132"/>
<circle cx="256" cy="52" r="6"/><rect x="254" y="57" width="4" height="12"/><rect x="249" y="44" width="14" height="2.5" transform="rotate(-20 256 45)"/>
<rect x="140" y="256" width="232" height="96"/>
<rect x="132" y="226" width="40" height="34"/><polygon points="132,226 152,200 172,226"/>
<rect x="340" y="226" width="40" height="34"/><polygon points="340,226 360,200 380,226"/>
<rect x="114" y="350" width="284" height="12" rx="2"/>
</g>
<g fill="{win}">
<path d="M248 186v-14a8 8 0 0 1 16 0v14z"/>
<path d="M246 250v-24a10 10 0 0 1 20 0v24z"/>
''' + ''.join(f'<path d="M{x} 334v-36a9 9 0 0 1 18 0v36z"/>' for x in (163,203,291,331)) + '''
<path d="M243 352v-46a13 13 0 0 1 26 0v46z"/>
</g>'''
def svg(bg, tf, win, tc, stroke=''):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
<defs>{bg[0]}</defs><rect width="512" height="512" fill="{bg[1]}"/>
{temple(tf,win)}
<text x="256" y="468" text-anchor="middle" font-family="DejaVu Sans" font-weight="bold" font-size="112" letter-spacing="4" fill="{tc}" {stroke}>EQ43</text></svg>'''
A=svg(('<linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1f4e8c"/><stop offset="1" stop-color="#0a1f44"/></linearGradient>','url(#g)'),'#ffffff','#163a6e','#e8c35a')
B=svg(('<linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#f3d77f"/><stop offset="1" stop-color="#b8892a"/></linearGradient>','url(#g)'),'#ffffff','#c99a3a','#0a1f44')
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
