B=enumerate
i=any
F=abs
e=set
d=max
N=len
L=sum
A=range
J=0
I=4
def A9(g):A=L(g,[]);return d(e(A),key=A.count)
def m(g,v):return{(A,D)for(A,C)in B(g)for(D,E)in B(C)if E==v}
def K(g,v,c):
	if not c:return[A[:]for A in g]
	D,E=N(g),N(g[0]);A=[A[:]for A in g]
	for(B,C)in c:
		if 0<=B<D and 0<=C<E:A[B][C]=v
	return A
def c(S):A=[A for(A,B)in S];B=[A for(B,A)in S];return min(A),min(B),d(A),d(B)
def n(a,b):
	E,F,G,H=c(a);I,J,K,L=c(b);A,B=(E+G)//2,(F+H)//2;C,D=(I+K)//2,(J+L)//2
	if A==C:return 0,1 if B<D else-1
	if B==D:return 1 if A<C else-1,0
	if A<C:return 1,1 if B<D else-1
	if A>C:return-1,1 if B<D else-1
	return 0,0
def o(p):A,B=p;return{(A-1,B),(A+1,B),(A,B-1),(A,B+1)}
def AA(a,b):
	B,C=a;D,E=b
	if B==D:G,H=(C,E)if C<=E else(E,C);return{(B,A)for A in A(G,H+1)}
	if C==E:G,H=(B,D)if B<=D else(D,B);return{(A,C)for A in A(G,H+1)}
	I,J=D-B,E-C
	if F(I)==F(J):K=1 if I>0 else-1;L=1 if J>0 else-1;M=F(I);return{(B+A*K,C+A*L)for A in A(M+1)}
	return e()
def p(G):
	p='t';q='b'
	if not G or not G[0]:return[A[:]for A in G]
	O,P=N(G),N(G[0]);M=A9(G);W={(B,C)for B in A(O)for C in A(P)if G[B][C]!=M}
	if not W:return[A[:]for A in G]
	F,C,B,D=c(W);AB={(A,C)for A in A(F,B+1)}|{(A,D)for A in A(F,B+1)}|{(F,A)for A in A(C,D+1)}|{(B,A)for A in A(C,D+1)};X=AB-W;AC={(B,E)for B in A(F,B+1)for E in A(C,D+1)};U=AC-W;j=n(U,X);r=n(X,U);AD={p:L(G[F][A]==M for A in A(C,D+1)),q:L(G[B][A]==M for A in A(C,D+1)),'l':L(G[A][C]==M for A in A(F,B+1)),'r':L(G[A][D]==M for A in A(F,B+1))};AE={p:(-1,0),q:(1,0),'l':(0,-1),'r':(0,1)};Q=None;E=sorted(AD.items(),key=lambda x:x[1],reverse=True)
	if E and(N(E)==1 or E[0][1]>E[1][1]):Q=AE[E[0][0]]
	s=L(G[B][D]==J for B in A(O)for D in A(C));t=L(G[B][C]==J for B in A(O)for C in A(D+1,P));u=L(G[B][C]==J for B in A(F)for C in A(P));Y=L(G[B][C]==J for B in A(B+1,O)for C in A(P));R=1 if t>s else-1 if s>t else 0;S=1 if Y>u else-1 if u>Y else 0
	def v(dv):
		B,C=dv;A=0
		if R and C==R:A+=1
		if S and B==S:A+=1
		return A
	T=Q
	if T is None:
		if j==r:T=(S,0)if not R and S else(0,R)if not S and R else j
		else:
			T=d((j,r),key=v)
			if v(T)==0 and(S or R):T=S or 0,R or 0
	f,g=T;k=e()
	for w in A(9):
		AF,AG=f*w,g*w
		for(AH,AI)in X:k.add((AH+AF,AI+AG))
	V=K(G,I,U);x=m(G,J);V=K(V,I,k&x)
	if X:y,z,A0,A1=c(X);A2={(y,z),(y,A1),(A0,z),(A0,A1)}
	else:A2={(F,C),(F,D),(B,C),(B,D)}
	Z=m(V,J);f,g=T
	if g==0 and f:Z={A for A in Z if C<=A[1]<=D}
	elif f==0 and g:Z={A for A in Z if F<=A[0]<=B}
	AJ=not(S or R);AK=G if AJ else V
	def AL(p):
		D,E=p;A=0
		for(B,C)in o(p):
			if 0<=B<O and 0<=C<P and AK[B][C]==J:A+=1
		return A==2
	def A3(S,p):return i((A,B)in S for(A,B)in o(p))
	AM=[A for A in Z if AL(A)and A3(W,A)and A3(k,A)];A4=e()
	for a in A2:
		for A5 in AM:Y=A5[0]-a[0],A5[1]-a[1];l=a[0]+42*Y[0],a[1]+42*Y[1];A4|=AA(a,l)
	H=K(V,I,A4&x)
	if Q and U:
		b={A for(B,A)in U};A6={A for(A,B)in U}
		if Q==(-1,0)and F>0:
			E={(F-1,A)for A in b if 0<=A<P and G[F-1][A]==M}
			if E:H=K(H,I,E)
		elif Q==(1,0)and B+1<O:
			E={(B+1,A)for A in b if 0<=A<P and G[B+1][A]==M}
			if E:H=K(H,I,E)
		elif Q==(0,-1)and C>0:
			E={(A,C-1)for A in A6 if 0<=A<O and G[A][C-1]==M}
			if E:H=K(H,I,E)
		elif Q==(0,1)and D+1<P:
			E={(A,D+1)for A in A6 if 0<=A<O and G[A][D+1]==M}
			if E:H=K(H,I,E)
	if Q==(1,0):
		AN=i(B not in(J,I)for A in G for B in A);h=B+1
		if AN or 0<=h==N(G)-1:
			A7=False
			if 0<=h<N(G):
				AO=A(C+1,D)
				def AP(j):return i(C+1<=A<D and V[B][A]==I for A in(j-1,j,j+1))
				b=tuple(A for A in AO if G[h][A]==J and AP(A))
				if b:H=K(H,I,{(h,A)for A in b});A7=True
			if A7:
				l=N(G[0]);A8={(B,A)for A in A(l)if(A<C or A>D)and H[B][A]==I}
				if A8:H=K(H,J,A8)
	return H