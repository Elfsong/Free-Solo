def p(j,A=enumerate):
 for r,R in A(j):
  for c,C in A(R):
   if C==5:
    for y in-1,0,1:
     for x in-1,0,1:j[r+y][c+x]=1
    j[r][c]=5
 return j