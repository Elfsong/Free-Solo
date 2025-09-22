def p(j):
 A=min(len(j),len(j[0]));p,c=[r[:A]for r in j[:A]],[r[-A:]for r in j[-A:]]
 if 8 in map(max,p):p,c=c,p
 R=range(A*A)
 return[[p[y//A][x//A]*c[y%A][x%A]//8 for x in R]for y in R]