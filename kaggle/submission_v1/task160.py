Z=[0,2,0];T=[2]*3
def p(g):
 for r in range(len(g)-2):
  for c in range(len(g[0])-2):
   if g[r][c]==1 and sum(sum(i[c:c+3])for i in g[r:r+3])==8:g[r][c:c+3]=Z;g[r+1][c:c+3]=T;g[r+2][c:c+3]=Z
 return g