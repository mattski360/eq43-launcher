from PIL import Image,ImageDraw,ImageFont,ImageFilter
src=Image.open('/cursor/stores/store-86d33eb8-fdd3-49ef-a1a2-c3f34f1b7422/grok-bot/agents/0acc6b6f-6690-469e-a900-f111d7afb7eb/attachments/01M6M2FXZSBV7HHZDFGRKJ462H.jpg').convert('RGB')
c=src.crop((0,95,554,430)); g=c.convert('L').point(lambda v:255 if v<200 else 0); c=c.crop(g.getbbox())
S=1024; W=int(S*.82); H=round(c.height*W/c.width)
t=c.resize((W,H),Image.LANCZOS).filter(ImageFilter.UnsharpMask(2,80,2))
col=(0x4a,0x4a,0x4a)
f=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',190)
im=Image.new('RGB',(S,S),'white');d=ImageDraw.Draw(im)
tb=d.textbbox((0,0),'EQ43',font=f);th=tb[3]-tb[1];gap=40
y0=(S-(H+gap+th))//2
im.paste(t,((S-W)//2,y0))
d.text(((S-(tb[2]-tb[0]))//2-tb[0],y0+H+gap-tb[1]),'EQ43',font=f,fill=col)
im.save('icon-1024.png')
for n,s in [('apple-touch-icon.png',180),('icon-192.png',192),('icon-512.png',512),('favicon-32.png',32),('icon-preview.png',512)]:
  im.resize((s,s),Image.LANCZOS).save(n)
im.resize((180,180),Image.LANCZOS).save('/tmp/p180.png');im.resize((60,60),Image.LANCZOS).save('/tmp/p60.png')
print(W,H,y0,th)
