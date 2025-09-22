def p(g):
 a=list(map(list,zip(*g[::-1])))
 for r in a:
  if w:=r[0]:q=sum(r)//w;r[:]=[0]*q+[w]*q+[0]*(15-2*q)
 return list(map(list,zip(*a)))[::-1]