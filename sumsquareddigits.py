def ssd(b,n):
    som=[]
    q=n//b
    while True:
        r=n%b
        n=q
        som.append(r)
        if q==0:
            break
        else:
            q=n//b
    r=0
    for i in som:
        r+=int(i)**2

    return r

n=int(input())
lst=[]
for i in range(n):
    tab=[int(i) for i in input().split(" ")]
    lst.append(tab)

res = []
for tab in lst:
    res.append(ssd(tab[1],tab[2]))
j=1
for i in res:
    print(j,i)
    j+=1