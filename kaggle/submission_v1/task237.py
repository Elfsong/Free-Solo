def p(g):
 for r in g[::-1]:
  s=0
  for i,c in enumerate(r):r[i]=s=c or s
 s=0
 for r in g:r[-1]=s=r[-1]or s
 return g