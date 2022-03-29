n=int(input())
lst=[]
for i in range(n):
    tab=[int(i) for i in input().split(" ")]
    lst.append(tab)

lst.reverse()
maxe=0
for i in range(n-1):
    for j in range(n):
        tmp=
