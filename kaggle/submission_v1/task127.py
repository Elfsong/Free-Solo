def p(g):
 R,Z=range,[r[:]for r in g]
 for r in R(1,len(g),4):
  for c in R(1,len(g[0]),4):
   for y in R(3):
    for x in R(3):Z[r-1+y][c-1+x]=g[r][c]+5
 return Z