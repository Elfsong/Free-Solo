def p(g,R=range,L=len):
	for _ in R(4):
		g=[*map(list,zip(*g[::-1]))]
		for i,r in enumerate(g):
			if L(set(r))>2:B=[*filter(bool,r)];g[i]=(B[-(r.index(B[0])%L(B)):]+B*20)[:L(g[0])]
	return g