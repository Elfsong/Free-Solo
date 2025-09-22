from itertools import*
def p(g,L=len,R=range):
 C=max(([k for k,_ in groupby(r)]for r in g),key=L)
 g=[C*1 for _ in C]
 for r in R(L(g)//2):
  for c in R(r,L(g)-r-1):g[r][c]=g[~r][c]=C[r]
 return g