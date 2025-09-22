def p(j):
	c=len(j);E=[[0]*c for _ in' '*c];E[0]=[3]*c;y,x=0,c-1;dy,dx=1,0
	for a in range(c-1,0,-2):
		for _ in'  ':
			for _ in range(a):y+=dy;x+=dx;E[y][x]=3
			dy,dx=dx,-dy
	return E