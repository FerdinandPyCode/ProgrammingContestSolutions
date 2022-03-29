tab=[int(i) for i in input().split(" ")]
lst=set()
res=0
l=[]
for i in range(tab[1]):
    l.append(input())
    
for j,i in enumerate(l):
    lst.add(i)
    if len(lst)==tab[0]:
        res=j+1
        break
if len(lst)<tab[0]:
    print("paradox avoided")
else:
    print(res)