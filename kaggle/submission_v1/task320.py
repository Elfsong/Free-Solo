def p(j,R=range):
 P=[*map(list,j)]
 for k in R(len(j[0])):
  W=[r for r in R(len(j))if j[r][k]]
  for r in R(len(W)//2):P[W[~r]][k]=8
 return P