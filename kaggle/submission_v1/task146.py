def p(g):
 for a in g[:3],g[3:6],g[6:]:
  if(*map(tuple,a),)!=(*zip(*a),):return a