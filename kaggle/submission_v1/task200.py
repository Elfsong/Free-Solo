def p(g):
 for i,a in enumerate(g[-1]):
  if a:
   for r in g:r[i:10:2]=[a]*len(r[i:10:2])
   for j,k in[(0,1),(~0,3)]:g[j][i+k:10:4]=[5]*len(g[j][i+k:10:4])
   return g
 return g