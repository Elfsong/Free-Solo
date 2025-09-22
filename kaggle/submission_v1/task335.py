def p(j,A=range):
	c=lambda E:next((l,W.index(E))for(l,W)in enumerate(j)if E in W);k,W=c(8);l,J=c(2)
	s=(k<l)*2-1
	for a in A(k+s,l+s,s):j[a][W]=4
	for a in A(W,J)if W<J else A(J+1,W):j[l][a]=4
	return j