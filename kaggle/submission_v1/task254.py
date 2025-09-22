def p(j):
 k=[sum(x>0 for x in c)for c in zip(*j)]
 for r in j:r[:]=[0]*len(j[0])
 for v,C in[(min(filter(None,k)),2),(max(k),1)]:
  w=k.index(v)
  for l in range(v):j[~l][w]=C
 return j