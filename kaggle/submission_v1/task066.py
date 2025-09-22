F=enumerate
W=abs
C=int
Q=range
P=sorted
K=sum
I=round
O=set
J=min
B=len
A=None
from typing import List as D,Tuple,Optional
from copy import deepcopy as R
d=Tuple[C,C]
e=D[D[C]]
E,M,G=3,2,0
def N(g,r,c):return 0<=r<B(g)and 0<=c<B(g[0])
def S(r,c):return[(r+1,c),(r-1,c),(r,c+1),(r,c-1)]
def T(a,b):return a[0]+b[0],a[1]+b[1]
def X(a,b):return a[0]-b[0],a[1]-b[1]
def Y(d):return 0 if d[0]==0 else 1 if d[0]>0 else-1,0 if d[1]==0 else 1 if d[1]>0 else-1
def f(d):return-d[1],d[0]
def h(d):return d[1],-d[0]
def U(a,b):return W(a[0]-b[0])+W(a[1]-b[1])
def H(g,val):return[(A,C)for(A,B)in F(g)for(C,D)in F(B)if D==val]
def Z(g,positions):
	A=O(positions);E=[]
	while A:
		F=A.pop();D=[F];G=[F]
		while D:
			H,I=D.pop()
			for(B,C)in S(H,I):
				if(B,C)in A:A.remove((B,C));D.append((B,C));G.append((B,C))
		E.append(G)
	return E
def L(goals,p):A=goals;return J(U(p,A)for A in A)if A else 10**9
def V(val):return val==G or val==E
def g(g,greens,reds):
	H=greens
	if not H or not reds:return
	V=Z(g,H);G=J(V,key=lambda comp:(B(comp),L(reds,(I(K(A for(A,B)in comp)/B(comp)),I(K(A for(B,A)in comp)/B(comp))))));D=A;W=O(G)
	for(M,N)in G:
		for(P,Q)in S(M,N):
			if(P,Q)in W:D=(M,N),(P,Q);break
		if D:break
	if D is A:
		R=A;T=-1
		for E in G:
			for F in G:
				C=U(E,F)
				if C>T:R=E,F;T=C
		D=R
	E,F=D;C=Y(X(F,E));a=[(F,C),(E,(-C[0],-C[1]))];return J(a,key=score)
class i:
	__slots__='pred','path','steps','dmin','dend','bounces','start','start_dir'
	def __init__(A,pred,path,steps,dmin,dend,bounces,start,start_dir):A.pred=pred;A.path=path;A.steps=steps;A.dmin=dmin;A.dend=dend;A.bounces=bounces;A.start=start;A.start_dir=start_dir
def a(g,start,d,reds):
	X=start;S=reds;j,k=B(g),B(g[0]);D=R(g);K=O();U=0;A=X;F=d;Y=[A];P=L(S,A);Z=P;W=0
	while U<j*k*10:
		U+=1;I=T(A,F)
		if N(g,*I)and D[I[0]][I[1]]==M:break
		l=not N(g,*I)or not V(D[I[0]][I[1]])
		if not l:
			A=I
			if D[A[0]][A[1]]==G:D[A[0]][A[1]]=E
			H=A,F
			if H in K:break
			K.add(H)
		else:
			a,m=f(F),h(F);Q=[]
			for b in(a,m):
				C=T(A,b)
				if N(g,*C)and V(D[C[0]][C[1]]):Q.append((L(S,C),b,C))
			if Q:
				Q.sort(key=lambda x:(x[0],0 if x[1]==a else 1));o,n,C=Q[0];F=n;A=C
				if D[A[0]][A[1]]==G:D[A[0]][A[1]]=E
				H=A,F
				if H in K:break
				K.add(H);W+=1
			else:
				c=-F[0],-F[1];C=T(A,c)
				if N(g,*C)and V(D[C[0]][C[1]]):
					F=c;A=C
					if D[A[0]][A[1]]==G:D[A[0]][A[1]]=E
					H=A,F
					if H in K:break
					K.add(H);W+=1
				else:break
		Y.append(A);e=L(S,A);P=J(P,e);Z=e
	return i(D,Y,U,P,Z,W,X,d)
def b(g):
	G=H(g,M);Q=H(g,E)
	if not G or not Q:return R(g)
	h=Z(g,Q);N=J(h,key=lambda comp:(B(comp),L(G,(I(K(A for(A,B)in comp)/B(comp)),I(K(A for(B,A)in comp)/B(comp))))));C=A;i=O(N)
	for(T,V)in N:
		for(W,b)in S(T,V):
			if(W,b)in i:C=(T,V),(W,b);break
		if C:break
	if C is A:
		c=A;d=-1
		for D in N:
			for F in N:
				e=U(D,F)
				if e>d:c=D,F;d=e
		C=c
	D,F=C;P=Y(X(F,D));f=[a(g,F,P,G),a(g,D,(-P[0],-P[1]),G)];f.sort(key=lambda r:(r.dend,r.bounces,r.dmin,r.steps));return f[0].pred
def c(g):
	I=H(g,M);K=H(g,E)
	if B(I)!=2 or B(K)!=2:return
	def O(ps):(A,B),(C,D)=P(ps);return B==D and W(A-C)==1
	if not(O(I)and O(K)):return
	(S,L),(T,a)=P(K);(U,N),(V,a)=P(I)
	if{S,T}!={U,V}:return
	X,Y=P([L,N]);F=A
	for C in Q(0,J(S,U)+1):
		if all(g[C][A]in(G,E,M)for A in Q(X,Y+1)):F=C;break
	if F is A or F==0:return
	D=R(g);b=max(T,V)
	for C in Q(F,b+1):
		if D[C][L]==G:D[C][L]=E
		if D[C][N]==G:D[C][N]=E
	for Z in Q(X,Y+1):
		if D[F][Z]==G:D[F][Z]=E
	return D
def p(grid):
	B=c(grid)
	if B is not A:return B
	return b(grid)