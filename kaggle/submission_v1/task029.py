def p(g,E=enumerate):
	for B in{*sum(g,[])}:
		D,F=zip(*[(d,r)for r,R in E(g)for d,v in E(R)if v==B])
		A=[R[min(D)+1:max(D)]for R in g[min(F):max(F)]]
		if A[0].count(B)==len(A[0]):return A[1:]
	return g