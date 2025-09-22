R=range
def p(g):
	B=sum(g,[]);A=B.count(0)
	return[[max(B)*(g[r%3][c%3]and(r//3)*A+c//3<9-A)for c in R(A*3)]for r in R(A*3)]