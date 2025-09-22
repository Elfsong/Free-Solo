def p(g):
 C=sum(g,[]).count(5);D=next(i for i,r in enumerate(g)if 0 not in r);E=g[D][0]
 return[[E if R==D+C or C==g[0].index(E)-L else 0for L,_ in enumerate(g[0])]for R,_ in enumerate(g)]