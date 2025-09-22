def p(c):
 M=max(map(max,c));z=[0]*(len(c[0])+2);P=[z]+[[0]+r+[0]for r in c]+[z]
 return[[0if v==M and sum(sum(P[i+x][j:j+3])for x in range(3))==M else v for j,v in enumerate(r)]for i,r in enumerate(c)]