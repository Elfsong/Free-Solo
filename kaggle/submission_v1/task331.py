def p(j):
 for a,C in[(E,W)for E,k in enumerate(j)for W,l in enumerate(k)if l==1]:
  if a:j[a-1][C]=2
  if a<9:j[a+1][C]=8
  if C:j[a][C-1]=7
  if C<9:j[a][C+1]=6
 return j