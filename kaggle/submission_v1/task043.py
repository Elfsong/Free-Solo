def p(j,A=enumerate):
 for k,r in A(j):
  if k and r[~0]==5:
   for l in range(len(j)-1):
    if j[0][l]==5:r[l]=2
 return j