def p(g):
 R=range
 for o in R(81):
  j,i,c,r=o%3,o//3%3,o//9%3,o//27
  if g[4*r+i][4*c+j]==4:
   return[[5if X%4==3 or Y%4==3 else g[4*r+X-4*i][4*c+Y-4*j]if X//4==i and Y//4==j else 0for Y in R(11)]for X in R(11)]