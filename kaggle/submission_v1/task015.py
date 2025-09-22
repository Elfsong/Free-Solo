def p(g,r=range(9)):
 for i in r:
  for j in r:
   if 0<(v:=g[i][j])<3:
    for a in-1,0,1:
     for b in-1,0,1:
      if a|b and(a*b!=0)==(v-1):g[i+a][j+b]=7-3*(v-1)
 return g