def p(j,A=range):
 c=len(j)
 for E in A(1,c-1):
  k=W=0
  for l in A(c):
   J=j[E][l]
   if J>1and k<1:k=1
   elif J<1and k==1:k=2;W=W or l
   elif J>1and k>1:j[E][W:l]=[9]*(l-W);k=1;W=0
 return j