from collections import*
from itertools import*
R=range
M=min
def p(g):
	if not g or not g[0]:return[*map(list,g)]
	h,w=len(g),len(g[0]);MM=lambda e:(l:=sum(e,[]),max(set(l),key=l.count))[1];Q=lambda p:p and isinstance(next(iter(p))[1],tuple);T=lambda p:{c for _,c in p}if Q(p)else p;u=lambda p:M((a for a,b in T(p)),default=0);l=lambda p:M((b for a,b in T(p)),default=0);r=lambda p:max((b for a,b in T(p)),default=0);U=lambda p:(i:=T(p),(M(a for a,b in i),M(b for a,b in i)))[1]if i else(0,0);L=lambda p:(i:=T(p),(max(a for a,b in i),max(b for a,b in i)))[1]if i else(0,0);S=lambda p,d:{(c,(y+d[0],x+d[1]))for c,(y,x)in p}if Q(p)else{(y+d[0],x+d[1])for y,x in p} if p else p;Z=lambda p:S(p,(-u(p),-l(p)))if p else p;RT=lambda g:[*map(list,zip(*g[::-1]))];PT=lambda g,o:(b:=[*map(list,g)],[b[y].__setitem__(x,c) for c,(y,x) in o or[] if 0<=y<len(b)and 0<=x<len(b[0])],b)[2];H=lambda p:(c:=U(p)[0]+L(p)[0],{(a,(c-y,x))for a,(y,x)in p}if Q(p)else{(c-y,x)for y,x in p})[1]if p else p;V=lambda p:(c:=U(p)[1]+L(p)[1],{(a,(y,c-x))for a,(y,x)in p}if Q(p)else{(y,c-x)for y,x in p})[1]if p else p;D=lambda p:(u_:=U(p),{(a,(x-u_[1]+u_[0],y-u_[0]+u_[1]))for a,(y,x)in p}if Q(p)else{(x-u_[1]+u_[0],y-u_[0]+u_[1])for y,x in p})[1]if p else p;b=MM(g);o=[];s=set()
	for y,x in product(R(h),R(w)):
		if(y,x)in s:continue
		c=g[y][x]
		if c==b:continue
		j,f_={(c,(y,x))},{(y,x)}
		while f_:
			k=set()
			for R,C in f_:
				j.add((c,(R,C)));s.add((R,C))
				for dy,dx in[(0,1),(0,-1),(1,0),(-1,0)]:Y,X=R+dy,C+dx;k.add((Y,X))if 0<=Y<h and 0<=X<w else 0
			f_=k-s
		o.append(j)
	m=lambda a,b:(i:=T(a),j:=T(b),M(abs(y1-y2)+abs(x1-x2)for y1,x1 in i for y2,x2 in j)if i and j else 0)[2]
	def J(a):
		d=next(iter(a))[0];A=[x for x in o if next(iter(x))[0]==d];B=max((r(x)-l(x)+1 for x in A),default=0);e={m(C,b)for b in A for C in A};c=M((x for x in e if x),default=0);return-(2*B+(c-1 if c>0 else-2))
	f=sorted([{(a,(R,C))for R,row in enumerate(g)for C,a in enumerate(row)if a==b}for b in{c for r in g for c in r}-{b}],key=J);K=lambda p:M((V(p),D(p),V(D(V(p))),H(p)),key=lambda p:tuple(sorted(T(Z(p)))))if p else p;n=tuple(Z(K(a))for a in f);C=len(f);d=C+1-any(len(A)==1 for A in f);E=tuple(C for(A,B)in zip(n,tuple((i,i)for i in R(d)))for C in sorted(S(A,B),key=lambda t:t[1]));F=2*d-1;A=[[b]*F for _ in R(F)]
	for _ in R(3):A=PT(A,E);A=RT(A)
	return PT(A,E)