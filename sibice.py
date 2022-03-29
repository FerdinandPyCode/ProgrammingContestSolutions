tab=[int(i) for i in input().split(' ')]
res=[]
h=(tab[1]**2 + tab[2]**2)**0.5
for i in range(tab[0]):
    m=int(input())
    if m<=h:
        res.append("DA")
    else:
        res.append("NE")

for i in res:
    print(i)
