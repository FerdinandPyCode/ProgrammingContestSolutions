n=int(input())
a=0
lst=[]
for i in range(n):
    tab=[float(i) for i in input().split(" ")]
    if i==0:
        pass
    else:
        a+=((tab[1]+lst[i-1][1])*(tab[0]-lst[i-1][0]))/2000
    lst.append(tab)

print(a)