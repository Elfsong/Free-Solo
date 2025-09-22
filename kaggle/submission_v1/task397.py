def p(i,f=range):
 n=[(m,l,len(set(s)))for m in f(len(i)-1)for l in f(len(i[0])-1)if all(s:=i[m][l:l+2]+i[m+1][l:l+2])]
 for m,l,a in n:
  for e in f(m+2,min(len(i),m+2+a)):i[e][l:l+2]=[3,3]
 return i