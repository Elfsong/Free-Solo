def p(j):
 A=range;c=[[0]*9 for i in A(9)];E=[(r,C,j[r][C])for r in A(9)for C in A(9)if j[r][C]]
 for k,W,l in E:
  for i in A(9):c[k][i]=c[i][W]=l
 a,b=E[:2];c[a[0]][b[1]]=c[b[0]][a[1]]=2
 return c