S=False
L=isinstance
P=None
C=list
H=len
A=int
G=range
B=True
from collections import deque,Counter as M
from typing import List as E,Tuple as I,Iterable,Union
R=E[E[A]]
T=I[A,I[A,A]]
def g(g):return[C(A)for A in g]
def W(patch):
	A=patch
	if not A:return 0
	if L(A,C)and A and L(A[0],C):B=[B for A in A for B in A]
	else:B=[A for(A,B)in A]
	if not B:return 0
	return M(B).most_common(1)[0][0]
def V(i,j):
	for A in(-1,0,1):
		for B in(-1,0,1):
			if A==0 and B==0:continue
			yield(i+A,j+B)
def h(grid,diagonal=B,without_bg=B):
	F=without_bg;D=grid;I,J=H(D),H(D[0]);O=W(D)if F else P;E=[[S]*J for A in G(I)];T=[];X=V if diagonal else lambda i,j:((i-1,j),(i+1,j),(i,j-1),(i,j+1))
	for K in G(I):
		for L in G(J):
			if E[K][L]:continue
			Y=D[K][L]
			if F and Y==O:E[K][L]=B;continue
			Q=[];R=deque([(K,L)])
			while R:
				A,C=R.popleft()
				if not(0<=A<I and 0<=C<J)or E[A][C]:continue
				U=D[A][C]
				if F and U==O:E[A][C]=B;continue
				E[A][C]=B;Q.append((U,(A,C)))
				for(M,N)in X(A,C):
					if 0<=M<I and 0<=N<J and not E[M][N]:
						if not F or D[M][N]!=O:R.append((M,N))
			if Q:T.append(Q)
	return T
def J(patch):return[A for(B,A)in patch]
def F(indices):A=indices;B=[A for(A,B)in A];C=[A for(B,A)in A];return min(B),min(C),max(B),max(C)
def i(indices):A,B,C,D=F(indices);return C-A+1,D-B+1
def K(indices):A,B,C,D=F(indices);return A+(C-A)//2,B+(D-B)//2
def j(a_idx,b_idx):
	A,B=K(a_idx);C,D=K(b_idx)
	if A==C:return 0,1 if B<D else-1
	if B==D:return 1 if A<C else-1,0
	if A<C:return 1,1 if B<D else-1
	if A>C:return-1,1 if B<D else-1
	return 0,0
def k(loc,others):
	A,C=loc;D=set(others)
	for(E,F)in((A-1,C),(A+1,C),(A,C-1),(A,C+1)):
		if(E,F)in D:return B
	return S
def X(patch):
	A=patch;B=J(A)
	if not B:return[]
	C,G,D,H=F(B);E=C+D;return[(A,(E-B,C))for(A,(B,C))in A]
def Y(patch):
	A=patch;B=J(A)
	if not B:return[]
	G,C,H,D=F(B);E=C+D;return[(A,(B,E-C))for(A,(B,C))in A]
def D(patch,d):A,B=d;return[(C,(D+A,E+B))for(C,(D,E))in patch]
def N(grid,cells):
	A=grid;F,G=H(A),H(A[0]);B=[A[:]for A in A]
	for(C,(D,E))in cells:
		if C!=0 and 0<=D<F and 0<=E<G:B[D][E]=C
	return B
def O(grid,inter):
	C=inter
	for(A,B)in C:
		D=grid[A][B]
		if D!=0:return D
	for(A,B)in C:return grid[A][B]
	return 0
def Q(I):
	H=g(I);l=h(H,diagonal=B,without_bg=B);C=[A[:]for A in H];Q=[];R=[];S=[]
	for A in l:
		if not A:continue
		E=W(A);Z=[A for A in A if A[0]==E];m=[A for A in A if A[0]!=E];J=[A for(B,A)in m];a=[A for(B,A)in Z];K=P
		for T in A:
			if T[0]!=E:continue
			if k(T[1],J):K=T;break
		if K is P:K=Z[0]
		n=J+[K[1]]if J else[K[1]];o,p,q,r=F(n);U={(A,B)for A in G(o,q+1)for B in G(p,r+1)};L,M=j(a,J if J else a);b,c=i([A for(B,A)in A]);s=b*L,0;t=0,c*M;u=b*L,c*M
		def V(v):
			B,C=v
			def A(x):
				x=-x
				if x==0:return 0
				return x+1 if x>0 else x-1
			return A(B),A(C)
		v=V((L,0));w=V((0,M));x=V((L,M));y=[A for A in D(X(A),s)if A[0]==E];z=[A for A in D(Y(A),t)if A[0]==E];A0=[A for A in D(X(Y(A)),u)if A[0]==E];d=D(y,v);e=D(z,w);f=D(A0,x);A1={A for(B,A)in d if A in U};A2={A for(B,A)in e if A in U};A3={A for(B,A)in f if A in U};A4=O(H,A1);A5=O(H,A2);A6=O(H,A3);Q.extend((A4,A)for(B,A)in d);R.extend((A5,A)for(B,A)in e);S.extend((A6,A)for(B,A)in f)
	if Q:C=N(C,Q)
	if R:C=N(C,R)
	if S:C=N(C,S)
	return C
def p(g):return Q(g)