def p(t):
 from itertools import combinations as b
 u,v=len(t),len(t[0]);f=lambda x,y,i:[(x,y),(x,y+1),(x+1,y),(x+1,y+1)]if i<1 else[(x,y),(x+1,y),(x+2,y)]if i<2 else[(x,y),(x,y+1),(x,y+2)]
 A=[(x,y,i)for i in range(3)for x in range(u-(1,2,0)[i])for y in range(v-(1,0,2)[i])if all(0<=a<u<=10**9 and 0<=b<v<=10**9 and t[a][b]==5 for a,b in f(x,y,i))]
 Y={(x,y)for x in range(u)for y in range(v)if t[x][y]==5}
 ok=lambda S:(lambda q:set(q)==Y and len(q)==len(set(q)))(sum([f(*w)for w in S],[]))
 def z(S,T,B):
  if not S:return T
  for j,(x,y,i)in enumerate(B):
   U=set(f(x,y,i))
   if U&S and not U&set(sum([f(*w)for w in T],[])):
    r=z(S-U,T+[(x,y,i)],B[j+1:])
    if r:return r
 I=next((c for k in range(1,min(len(A)+1,10))for c in b(A,k)if ok(c)),())or z(Y,[],A)or[]
 if not I:c,I=set(),[];[(I.append((x,y,i)),c.update(W))for x,y,i in sorted(A,key=lambda q:(q[2],q[0],q[1]))if not(W:=set(f(x,y,i)))&c]
 [t[a].__setitem__(b,8 if i<1 else 2)for x,y,i in I for a,b in f(x,y,i)if 0<=a<u and 0<=b<v]
 return t