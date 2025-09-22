def p(j,r=range):
 c=len(j)
 for E in r(c):
  for k in r(1,c-E,2):
   if j[0][E]:j[k][k+E]=4
   if j[E][0]:j[k+E][k]=4
 return j