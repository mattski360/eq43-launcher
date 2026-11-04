def cren(x1,x2,y,n,h=8):
    w=(x2-x1)/(2*n-1); return ''.join(f'<rect x="{x1+i*2*w:.1f}" y="{y-h}" width="{w:.1f}" height="{h+1}"/>' for i in range(n))
def pin(x,y,h=22,w=7): return f'<polygon points="{x-w/2},{y} {x},{y-h} {x+w/2},{y}"/>'
def tower(x1,x2,top,spire,n=3):
    s=f'<rect x="{x1}" y="{top}" width="{x2-x1}" height="{362-top}"/>'+cren(x1,x2,top,n)
    s+=pin(x1+3,top-6)+pin(x2-3,top-6)
    if spire: c=(x1+x2)/2; s+=f'<polygon points="{c-10},{top-6} {c},{top-spire} {c+10},{top-6}"/>'
    return s
def temple(fill,win,mor):
    g=f'<g fill="{fill}">'
    g+='<rect x="190" y="236" width="132" height="126"/>'+cren(190,322,236,7)
    for cx,ct,st,sp in ((148,150,206,40),(364,118,190,56)):
        g+=tower(cx-46,cx-22,st,0,2)+tower(cx+22,cx+46,st,0,2)+tower(cx-22,cx+22,ct,sp)
    g+='<rect x="92" y="360" width="328" height="14" rx="2"/></g>'
    w=f'<g fill="{win}">'
    for x in (212,248,284):w+=f'<path d="M{x} 340v-62a8 8 0 0 1 16 0v62z"/>'
    for cx,ct,st in ((148,150,206),(364,118,190)):
        for x in (cx-38,cx+30): w+=f'<path d="M{x} 340v-{340-st-30}a4 4 0 0 1 8 0v{340-st-30}z"/>'
        w+=f'<path d="M{cx-7} 340v-{340-ct-30}a7 7 0 0 1 14 0v{340-ct-30}z"/><circle cx="{cx}" cy="{ct+16}" r="6"/>'
    w+='</g>'
    tip=118-56
    m=f'<g fill="{mor}"><rect x="361" y="{tip-14}" width="6" height="16" rx="2"/><circle cx="364" cy="{tip-19}" r="4.5"/><polygon points="366,{tip-12} 382,{tip-24} 383,{tip-21} 367,{tip-8}"/></g>'
    return g+w+m
