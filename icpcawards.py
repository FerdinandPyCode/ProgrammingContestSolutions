n=int(input())
lst=[]
l=[]
res=[]
for i in range(n):
    tab=input().split(" ")
    l.append(tab)

for i in l:
    if i[0] not in lst:
        lst.append(i[0])
        res.append(' '.join(i))
    
    if len(res)==12:
        break

for i in res:
    print(i)

