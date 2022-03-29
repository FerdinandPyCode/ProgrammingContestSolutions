tab=[int(i) for i in input().split(" ")]
n1=tab[1]-tab[0]-1
n2=tab[2]-tab[1]-1

if n1>=n2:
    print(n1)
else:
    print(n2)