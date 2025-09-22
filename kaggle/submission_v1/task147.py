def p(j):
 c,E=len(j),len(j[0]);G=lambda r,C:j[r][C]if c>r>=0 and E>C>=0 else 0
 return[[(j[k][W],8)[j[k][W]==3 and 3 in(G(k+l,W+J)for l,J in zip([0,1,0,-1],[1,0,-1,0]))]for W in range(E)]for k in range(c)]