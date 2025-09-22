def p(j,A=range):
 c,E,k,W=len(j),len(j[0]),0,0
 for l in A(c):
  for J in A(E):
   if j[l][J]:k,W=l+2,J
 for C in A(E):
  k,a=k-1,7+C%2
  for l in A(k):
   for J in W-C,W+C:
    if 0<=J<E:j[l][J]=a
 return j