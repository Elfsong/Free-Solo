def p(j):
 for r in j:
  P=k=0
  for i,a in enumerate(r):
   if a>0:P=a
   if P:r[i]=(P,5)[k%2];k+=1
 return j