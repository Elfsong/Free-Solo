def p(j):
 c,E=divmod(sum(j,[]).index(2),5);j[c][E]=0
 for r,C,v in(-1,-1,3),(-1,1,6),(1,-1,8),(1,1,7):
  if 0<=c+r<3 and 0<=E+C<5:j[c+r][E+C]=v
 return j