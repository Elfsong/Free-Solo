L=len;R=range
def p(g):
 r=[*map(list,g)];n=L(g);m=L(g[0]);B=lambda i,j:0<=i<n and 0<=j<m;k={(i,j)for i in R(n)for j in R(m)if g[i][j]==1}
 if not k:return r
 for o in R(2):
  l={(u,v)for x,a in k for u,v in((5-x+o,a-5),(5-a+o,4-x+o),(x-5,a-4))if-5<=u<=5 and-5<=v<=5}
  p=[t for t in l if all((5-x+o,5+a)in k or not B(5-x+o,5+a)for x,a in[t])and all((4-a+o,5-x+o)in k or not B(4-a+o,5-x+o)for x,a in[t])and all((5+a,4+x)in k or not B(5+a,4+x)for x,a in[t])and any(B(5-x+o,5+a)and(5-x+o,5+a)in k for x,a in[t])]
  if p:
   s={(5-x+o,5+a)for x,a in p if B(5-x+o,5+a)}|{(4-a+o,5-x+o)for x,a in p if B(4-a+o,5-x+o)}|{(5+a,4+x)for x,a in p if B(5+a,4+x)}
   if s==k:
    for x,a in p:
     if 0<=4+x<L(r)and 0<=4-a+o<L(r[0])and not r[4+x][4-a+o]:r[4+x][4-a+o]=2
    return r
 return r
