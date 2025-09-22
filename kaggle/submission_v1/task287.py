def p(g):
 C=range(len(g))
 def A(D):
  for r in C:
   for c in C:
    if g[r][c]==4:g[r][c]=D[r][c]
 A(g[::-1])
 A([r[::-1]for r in g])
 return g