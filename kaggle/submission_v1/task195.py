def p(g):
 y=min(i for i,r in enumerate(g)if 5 in r)
 x=min(r.index(5)for r in g if 5 in r)
 V=lambda r,c:g[y+3*r][x+3*c]
 R=range(9)
 return[[V(r//3,c//3)and V(r%3,c%3)for c in R]for r in R]