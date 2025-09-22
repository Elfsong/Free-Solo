R=range
def p(I):
 B=[c for r in I for c in r];g=max(set(B),key=B.count);L,M=len(I),len(I[0]);d,h=set(),[]
 for i,j in ((k//M,k%M) for k in R(L*M)):
  if(i,j)in d or I[i][j]==g:continue
  E=I[i][j];J,F=set(),{(i,j)}
  while F:J|=F;d|=F;F={(a,b)for y,x in F for a,b in((y+1,x),(y-1,x),(y,x+1),(y,x-1))if 0<=a<L and 0<=b<M and I[a][b]==E}-d
  h.append({(E,c)for c in J})
 P=[[(c,(y,x))for y,r in enumerate(I)for x,c in enumerate(r)if c==C]for C in{*B}-{g}]
 def kf(a):
  c=a[0][0];O=[o for o in h if o and next(iter(o))[0]==c]
  if not O:return 0
  W=max(max(x for _,(_,x)in o)-min(x for _,(_,x)in o)+1 for o in O);s={abs(y-Y)+abs(x-X)for i,o in enumerate(O)for p in O[i+1:]for _,(y,x)in o for _,(Y,X)in p};m=min(s,default=0)
  return -(2*W+(m-1 if m else-2))
 S=sorted(P,key=kf)
 def K(p):
  if not p:return p
  def T(q):
   if not q:return()
   ps={c for _,c in q};y,x=zip(*ps);return tuple(sorted((a-min(y),b-min(x))for a,b in ps))
  ps=[];q=p
  for _ in R(2):
   r=q
   for _ in R(4):
    ps.append(r);c,xy=zip(*r);y,x=zip(*xy);X=min(x)+max(x);ps.append(list(zip(c,[(y,X-x)for y,x in xy])));c,xy=zip(*r);y,x=zip(*xy);Y=max(y)+min(y);r=list(zip(c,[(x,Y-y)for y,x in xy]))
   c,xy=zip(*q);y,x=zip(*xy);Y=max(y)+min(y);q=list(zip(c,[(Y-y,x)for y,x in xy]))
  return min(ps,key=T)
 M=[K(s)for s in S];N=[]
 for p in M:c,ps=zip(*p);y,x=zip(*ps);uy,ux=min(y),min(x);N.append([(c,(y-uy,x-ux))for c,(y,x)in p])
 C=len(P);D=C if any(len(a)==1 for a in P)else C+1;E=[]
 for p,(dy,dx)in zip(N,[(i,i)for i in R(D)]):E.extend(sorted([(c,(y+dy,x+dx))for c,(y,x)in p],key=lambda t:t[1][1]))
 F=2*D-1;A=[[g]*F for _ in R(F)]
 for _ in R(4):
  for c,(y,x)in E:A[y][x]=c
  A=[[*r]for r in zip(*A[::-1])]
 return A