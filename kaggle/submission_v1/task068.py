def p(j):
 s=sum(j,[])
 r,c=divmod(s.index(W:=next(x for x in s if s.count(x)<2and x)),10)
 return[[W if(R,C)==(r,c)else 2if max(abs(R-r),abs(C-c))<2else 0for C in range(10)]for R in range(10)]