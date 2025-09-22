def p(j):
	c=len(j);E=c//2-2;R=range(2,c-2)
	return[[(j[l][a],j[[0,-1][(l-2)//E]][[0,-1][(a-2)//E]])[j[l][a]==8]for a in R]for l in R]