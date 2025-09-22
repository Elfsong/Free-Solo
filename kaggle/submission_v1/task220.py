def p(j,A=enumerate):
 E=[[*W]for W in j]
 for k,W in A(j):
  for l,J in A(W):
   if J:
    for a in-1,0,1:
     for C in-1,0,1:
      try:
       if a or C:E[k+a][l+C]={8:4,2:1,3:6}[J]
      except:0
 return E