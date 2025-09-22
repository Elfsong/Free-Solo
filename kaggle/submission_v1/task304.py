def p(j,A=range(9)):
 E=max(f:=sum(j,[]),key=f.count)
 return[[j[R%3][C%3]if j[R//3][C//3]==E else 0for C in A]for R in A]