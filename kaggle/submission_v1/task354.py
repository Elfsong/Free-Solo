def p(j):
 c=[x[:]for x in j]
 def d(E,k,W):
  if 0<=E<10>k>=0 and c[E][k]==5:c[E][k]=W;[d(E+a,k+b,W)for a,b in zip([-1,1,0,0],[0,0,-1,1])]
 [d(i%9+1,i//9,j[0][i//9])for i in range(90)if j[0][i//9]]
 return c