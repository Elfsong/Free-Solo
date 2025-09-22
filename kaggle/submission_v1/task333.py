def p(g):
 for _ in[0]*4:
  g=list(map(list,zip(*g[::-1])))
  for r in g:
   if 3 in r:
    x=r.index(3)
    if(C:=max(r[:x]or[0]))>0:y=r.index(C);r[y:x]=[C]*(x-y)
 return g