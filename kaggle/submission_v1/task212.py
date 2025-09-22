def p(g,L=len,R=range):
	E,D=L(g),0
	while 5 not in g[D]:D+=1
	for A in R(E):
		for B in R(L(g[0])):
			v=g[A][B]
			if v in(1,2)and A-D:
				P=[[(A,E,1),(A,-1,-1)],[(D+1,A,1),(A,D,1)]][v-1][A<D]
				for C in R(*P):g[C][B]=v
	return g