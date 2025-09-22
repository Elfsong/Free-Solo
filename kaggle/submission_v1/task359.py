def p(g,u=len,r=range):
 R=lambda x:list(zip(*x[::-1]))
 m=max(map(g[0].count,r(10)))-1<u(g[0])/2
 if m:g=R(g)
 g=[[max((row.count(l),l)for l in r(10))[1]]*u(g[0])for row in g]
 if m:g=R(R(R(g)))
 return g