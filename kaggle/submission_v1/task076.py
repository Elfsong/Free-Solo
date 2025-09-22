H=True
D=max
E=range
B=min
C=len
F=False
from collections import Counter as I
def R(g):
	if not g or not g[0]:return 0
	A=I(B for A in g for B in A);E=D(A.values());C=[A for(A,B)in A.items()if B==E];return 0 if 0 in C else B(C)
def P(g,u=F,d=F,w=H):
	if not g or not g[0]:return[]
	J,K=C(g),C(g[0]);L=R(g)if w else None;F=[[0]*K for A in E(J)];P=[];S=[(1,0),(-1,0),(0,1),(0,-1)]+[(1,1),(1,-1),(-1,1),(-1,-1)]*d
	for G in E(J):
		for H in E(K):
			D=g[G][H]
			if F[G][H]or w and D==L:continue
			Q=D if u else None;I=[(G,H)];F[G][H]=1;M=[]
			while I:
				N,O=I.pop();D=g[N][O]
				if u and D!=Q or not u and w and D==L:continue
				M.append((D,(N,O)))
				for(T,U)in S:
					A,B=N+T,O+U
					if 0<=A<J and 0<=B<K and not F[A][B]:
						if u:
							if g[A][B]==Q:F[A][B]=1;I.append((A,B))
						elif not(w and g[A][B]==L):F[A][B]=1;I.append((A,B))
			if M:P.append(M)
	return P
def A(o):G=iter(o);J,(H,I)=next(G);A=C=H;E=F=I;[((A:=B(A,G)),(C:=D(C,G)),(E:=B(E,H)),(F:=D(F,H)))for(I,(G,H))in G];return A,E,C,F
def J(o):return o if not o else(lambda mi,mj,ma,mj2:[(A,(B-mi,C-mj))for(A,(B,C))in o])(*A(o))
def K(o,d):A,B=d;return[(C,(D+A,E+B))for(C,(D,E))in o]
def G(o):return o if not o else(lambda mi,mj,ma,mj2:[(A,(B,mj+mj2-C))for(A,(B,C))in o])(*A(o))
def Q(o):return o if not o else(lambda mi,mj,mi2,mj2:[(A,(mi+mi2-B,C))for(A,(B,C))in o])(*A(o))
def L(o):return o if not o else(lambda mi,mj,ma,mj2:[(A,(C-mj+mi,B-mi+mj))for(A,(B,C))in o])(*A(o))
def S(o):return G(L(G(o)))
def T(g,o):
	if not g or not g[0]:return g
	E,F=C(g),C(g[0]);A=[list(A)for A in g]
	for(G,(B,D))in o:
		if 0<=B<E and 0<=D<F:A[B][D]=G
	return A
def U(g,o):
	if not g or not g[0]:return set()
	D,F=C(g),C(g[0]);B=J(o)
	if not B:return set()
	G,H,I,L=A(B);M,N=I-G+1,L-H+1;return{(A,C)for A in E(D-M+1)for C in E(F-N+1)if all(g[B][C]==A for(A,(B,C))in K(B,(A,C)))}
def p(I):
	if not I or not I[0]:return I
	M=P(I,u=F,d=H,w=H)
	if not M:return I
	R=D(M,key=lambda o:C({A for(A,B)in o}));E=[S,L,Q,G];V=E+[lambda x,a=A,b=B:a(b(x))for A in E for B in E];N=[]
	for W in V:
		X=W(R);O=J(X);A=[(A,(B,C))for(A,(B,C))in O if A in{2,4}]
		if not A:continue
		Y,Z=B(B for(A,(B,A))in A),B(B for(A,(A,B))in A)
		for(a,b)in U(I,A):N.append(K(O,(a-Y,b-Z)))
	return T(I,{B for A in N for B in A})