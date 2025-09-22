def p(j):
 E=len(j[0])
 for r in j:
  if sum(r)==0:r[:]=[2]*E
 for W in range(E):
  if not{c[W]for c in j}-{0,2}:
   for r in j:r[W]=2
 return j