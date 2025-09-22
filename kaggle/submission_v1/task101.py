from collections import*
def p(g):
 if not g or not g[0]:return g
 h,w=len(g),len(g[0]);b=Counter(c for r in g for c in r).most_common(1)[0][0]
 v,C=set(),[]
 for y in range(h):
  for x in range(w):
   if(y,x)not in v and g[y][x]!=b:
    q=deque([(y,x)]);v.add((y,x));m=[]
    while q:
     Y,X=q.popleft();m+=[(g[Y][X],(Y,X))]
     for oy in-1,0,1:
      for ox in-1,0,1:
       if oy|ox:
        ny,nx=Y+oy,X+ox
        if 0<=ny<h and 0<=nx<w and(ny,nx)not in v and g[ny][nx]!=b:v.add((ny,nx));q.append((ny,nx))
    if m:C.append(m)
 if not C:return g
 k=max(C,key=lambda c:len({a for a,z in c}));y,x=zip(*(c for _,c in k));my,mx=min(y),min(x);T={(c,(cy-my,cx-mx))for c,(cy,cx)in k};U=Counter(a for a,z in k);M=max(U,key=lambda i:(U[i],-i))
 F=[]
 for V in 1,2,3:
  G={(c,(y*V+i,x*V+j))for c,(y,x)in T for i in range(V)for j in range(V)}
  o=set()
  for P in[{(a,z)for a,z in G if a!=M},{(a,z)for a,z in G if a==M}]:
   if o or not P:continue
   z={c for _,c in P};y,x=zip(*z);my,mx,My,Mx=min(y)-1,min(x)-1,max(y)+1,max(x)+1
   J=P|{(0,(i,j))for i in range(my,My+1)for j in(mx,Mx)}|{(0,(i,j))for j in range(mx,Mx+1)for i in(my,My)}
   y,x=zip(*(c for _,c in J));s_y,s_x=min(y),min(x);A={(c,(cy-s_y,cx-s_x))for c,(cy,cx)in J};y,x=zip(*(c for _,c in A));ph,pw=max(y)+1,max(x)+1
   for sy in range(1-ph,h):
    for sx in range(1-pw,w):
     if any(0<=sy+py<h and 0<=sx+px<w for _,(py,px)in A)and all((g[sy+py][sx+px]==c if 0<=sy+py<h and 0<=sx+px<w else c==0) for c,(py,px)in A):o.add((sy,sx))
   if o:
    for Y,Z in o:F.append({(c,(py+Y-s_y,px+Z-s_x))for c,(py,px)in G})
 if not F:return g
 N=[*map(list,g)]
 for(D,(O,P))in set().union(*F):
  if 0<=O<h and 0<=P<w:N[O][P]=D
 return N