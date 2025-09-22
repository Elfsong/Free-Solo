from collections import*
def p(j):
 c=Counter(sum(j,[])).most_common(9)
 return[*map(list,zip(*([e]*n+[0]*(c[0][1]-n)for e,n in c)))]