def p(j,A=enumerate):
 for c,E in A(j):
  for k,W in A(E):
   if W and W^4:
    j[c+1][k]=W
    for r in j[:c+1]:r[k&1::2]=[4]*len(r[k&1::2])
    return j