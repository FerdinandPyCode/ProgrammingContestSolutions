n=int(input())
lst=[]
for i in range(n):
    try:
        tab=[int(i) for i in input().split('+')]
        lst.append(tab[0]+tab[1])
    except:
        lst.append('skipped')

for i in lst:
    print(i)