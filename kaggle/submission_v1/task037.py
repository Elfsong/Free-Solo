def p(j,A=range):
 k,W={},[r[:]for r in j]
 [k.setdefault(a,[]).append((y,x))for y,r in enumerate(j)for x,a in enumerate(r)if a]
 for a in k:
  (C,e),(K,w)=k[a]
  for d in A(abs(K-C)+1):W[C+d*(2*(K>C)-1)][e+d*(2*(w>e)-1)]=a
 return W