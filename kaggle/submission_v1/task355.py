E=enumerate
def p(g):
 f=sum(g,[])
 Z=sorted(set(f),key=f.count)
 def M(C):
  x,y=zip(*((i,j)for j,r in E(g)for i,c in E(r)if c==C))
  return sum(r[min(x):max(x)+1].count(Z[0])for r in g[min(y):max(y)+1])
 return[[max(Z[1:],key=M)]]