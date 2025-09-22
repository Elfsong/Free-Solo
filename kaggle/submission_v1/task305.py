def p(j):
	A=len(j)
	E=sorted({e for r in j for e in r if e})
	return E and[[E[(r+c)%len(E)]for c in range(A)]for r in range(A)]or j