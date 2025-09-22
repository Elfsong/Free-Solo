from collections import*
def p(j):
 j=[k for k in j if(c:=[t for t in Counter(sum(j,[])).most_common(3)if t[0]>0][-1][0])in k]
 E=[i for k in j for i,x in enumerate(k)if x==c]
 return[k[min(E):max(E)+1]for k in j]