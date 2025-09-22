def p(g,R=range):
 g=g[0];S=5*len({e for e in g if e>0})
 return[([0]*(S-1-r)+g[:5]+[0]*S)[:S]for r in R(S)]