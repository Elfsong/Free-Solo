def p(g,a=3):
 l=len(g)//2
 for i in range(l+1):
  if g[-2][l-i]<1:g[-a][l-i]=g[-a][l+i]=g[-1][l];a+=1
 return g