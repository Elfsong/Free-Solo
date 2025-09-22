from collections import*
from itertools import*
R=range
v=len
def a(G,u,d,w,H,I,J=-1):
 Q=Counter(c for r in G for c in r).most_common(1)[0][0]if w and G and G[0]else None;A=[[0]*I for _ in R(H)];RR=[];S=[(1,0),(-1,0),(0,1),(-1,0)]
 if d:S+=[(1,1),(1,-1),(-1,1),(-1,-1)]
 for B in R(H):
  for K in R(I):
   T=G[B][K]
   if(w and T==Q)or A[B][K]:continue
   L,M,A[B][K],V=[],[(B,K)],1,T
   while M:
    N,O=M.pop(J);P=G[N][O]
    if(u and P!=V)or(w and P==Q):continue
    L.append((P,(N,O)))
    for(W,X)in S:
     i,j=N+W,O+X
     if 0<=i<H and 0<=j<I and not A[i][j]:A[i][j]=1;M.append((i,j))
   if L:RR.append(L)
 return RR
def b(p):y,x=zip(*(c for _,c in p));s,r=min(y),min(x);t,A=max(y),max(x);return t-s+1,A-r+1,(s,r)
c=lambda p,d:[(c,(y+d[0],x+d[1]))for c,(y,x)in p]
d=lambda p,f:[(c,(y*f+i,x*f+j))for c,(y,x)in p for i in R(f)for j in R(f)]if f>1 else p
def e(G,obj):B=[r[:]for r in G];[B[y].__setitem__(x,c)for c,(y,x)in obj or[]if 0<=y<v(B)and 0<=x<v(B[0])];return B
def f(patch):
 D={};E,B,C=0,0,0
 for E,(B,C)in patch:
  if E in(0,4):continue
  A=D.setdefault(E,[B,B,C,C]);A[0]=min(A[0],B);A[1]=max(A[1],B);A[2]=min(A[2],C);A[3]=max(A[3],C)
 return D
g=lambda A,b:(A+b-1)//b if b>0 else 0
def k(L,F,I):
 Y=Counter(A for(A,_)in L if A not in(0,4));G=f(L);H=[A for A in G if A in F]
 if not H:return
 J,K,A,M=[],[],[],[]
 for B in H:
  l,Z,m,z=G[B];P,Q,S,T=z-m+1,Z-l+1,F[B][3]-F[B][2]+1,F[B][1]-F[B][0]+1
  if P*Q*S*T<=0:return
  J.append(max(1,g(S,P)));K.append(max(1,g(T,Q)));A.append((l,m,F[B][0],F[B][2]));U=Y.get(B,0);x=I.get(B,0)
  if U>0:
   C=1
   while U*C*C<x:C+=1
   M.append(C)
 D=max(J+K+M)if J+K+M else 0
 if D<=0:return
 V=[C-A*D for(A,B,C,B)in A];W=[C-B*D for(A,B,A,C)in A];e=min(V or[0]);H=min(W or[0]);return D,(e,H),A
i=lambda off,m:max(0,min(off,m))if m>=0 else 0
j=lambda ref,s:(min([c-a*s for a,b,c,b in ref]or[0]),min([c-b*s for a,b,a,c in ref]or[0]))
def p(G):
 if not G or not G[0]:return[*map(list,G)]
 E,F=v(G),v(G[0]);U=[[c if c-4 else 0 for c in r]for r in G];M=a(U,0,1,1,E,F);AB=[(0,(A,B))for A in R(E)for B in R(F)if G[A][B]==4]
 if AB:h,w,(s,r)=b(AB);B=[G[i][r:r+w]for i in R(s,s+h)]
 else:B=G
 H=[[c if c-4 else 0 for c in r]for r in B];V,W=(v(H),v(H[0]))if H and H[0]else(0,0);A=list(dict.fromkeys(chain.from_iterable(a(H,1,0,1,V,W,J=0))));(AG,AF,(AH,AI))=b(A)if A else(0,0,(0,0));AJ=f(A);AL=Counter(c for c,_ in A);X={(y,z):x for x,(y,z)in A};Z,t=None,None;AD=[p for p in M if M and max(c[0]for _,c in p)==max(max(c[0]for _,c in p2)for p2 in M)]or M
 for N in AD:
  if not N:continue
  d_val,c_val,(s,r)=b(N);u=[(C,(y-s,x-r))for C,(y,x)in N];VV=k(u,AJ,AL);O=[]
  if VV:a_val,b_val,I=VV;O.append((a_val,b_val,I));O.append((a_val+1,j(I,a_val+1),I))
  else:O.append((max(1,g(AF,c_val or 1),g(AG,d_val or 1)),(AH,AI),None))
  for P,(AP,AQ),I in O:
   if P<=0:continue
   e_val=d(u,P);w,AR,_=b(e_val);f_val,h_val=v(B)-w,v(B[0])-AR;j_val=R(1,f_val)or[i(1,f_val)];AS=R(h_val+1)or[0];b_val=(i(AP,f_val),i(AQ,h_val));Q={b_val}
   if I is None:Q.update((A,B)for A in j_val for B in AS)
   if not Q:Q.add((0,0))
   for(AT,AU) in Q:
    y=c(e_val,(AT,AU));J={(x,C):D for D,(x,C)in y if 0<=x<v(B)and 0<=C<v(B[0])}
    if not J or any(B[x][C]==4 for x,C in J):continue
    if X:jk,xk=J.keys(),X.keys();I_set=jk&xk;z=sum(1 for p in I_set if J[p]==X[p]);l=7*z-5*v(I_set)-10*v(xk-jk)-v(jk-xk)
    else:l=-v(J)
    if Z is None or l>Z:Z,t=l,y
 return e(B,t)