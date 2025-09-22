def p(a):
    o,d=len(a),len(a[0])
    e=[(x,y)for x in(-4,0,4)for y in(-4,0,4)if x|y]
    q=[d]*10;u=[o]*10;j=[-1]*10;b=[-1]*10
    for i,r in enumerate(a):
        for h,m in enumerate(r):
            q[m]=min(q[m],h);u[m]=min(u[m],i);j[m]=max(j[m],h);b[m]=max(b[m],i)
    m=next(m for m in range(1,10)if j[m]-q[m]==2 and b[m]-u[m]==2);c,i=q[m],u[m]
    r=[[0]*d for _ in a]
    for x in 0,1,2:r[i+x][c:c+3]=a[i+x][c:c+3]
    z=[(s,t)for t in(0,1,2)for s in(0,1,2)if a[i+t][c+s]]
    for f,g in e:
        h=c+f;s=i+g;m=0
        for k in 0,1,2:
            for y in 0,1,2:
                v,l=h+y,s+k
                if 0<=v<d<=v+99 and 0<=l<o<=l+99 and a[l][v]:m=a[l][v];break
            if m:break
        if not m:continue
        h=c;s=i
        while 1:
            h+=f;s+=g
            if not(-3<h<d and-3<s<o):break
            for y,k in z:
                v,l=h+y,s+k
                if 0<=v<d<=v+99 and 0<=l<o<=l+99:r[l][v]=m
    return r