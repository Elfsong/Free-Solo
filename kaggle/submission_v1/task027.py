L=len;R=range
def p(g):
 H,W=L(g),L(g[0]);r=[*map(list,g)];k={(x,a)for x in R(H)for a in R(W)if g[x][a]};B=lambda Y,X:0<=Y<H and 0<=X<W
 if not k:return r
 for o in R(2):
  l={(X,A)for x,a in k for X,A in[(5-x+o,a-5),(5-a+o,4-x+o),(x-5,a-4)]if-5<=X<=5 and-5<=A<=5}
  P=[(x,a)for x,a in l if B(c:=5-x+o,d:=5+a)and(c,d)in k and(not B(e:=4-a+o,f:=5-x+o)or(e,f)in k)and(not B(d,m:=4+x)or(d,m)in k)]
  if k=={(Y,X)for y,x in P for Y,X in[(5-y+o,5+x),(4-x+o,5-y+o),(5+x,4+y)]if B(Y,X)}:
   for x,a in P:
    if B(Y:=4+x,X:=4-a+o)and not r[Y][X]:r[Y][X]=2
   return r
 return r