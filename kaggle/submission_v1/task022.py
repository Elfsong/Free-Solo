def p(g):
 F=[(r,c)for r,R in enumerate(g)for c,v in enumerate(R)if v==5]
 return[[([v for r,c in F if min(r+i,c+j)>=0 and(v:=g[r+i][c+j])]or[0])[-1]for j in[-1,0,1]]for i in[-1,0,1]]