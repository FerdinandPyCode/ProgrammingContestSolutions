n=int(input())
tab=[int(i) for i in input().split(" ")]
tab.sort()
result=[]
i=0
while i<n:
    go=False
    if(i<n-2):
        if(tab[i]==tab[i+1]-1==tab[i+2]-2):
            go=True
            lst=[tab[i]]
            j=i
        else:
            result.append(tab[i])
    else:
        result.append(tab[i])

    while go:

        if(j!=n-1 and tab[j]==tab[j+1]-1):
            lst.append(tab[j+1])
        else:
            result.append(f"{str(lst[0])}-{str(lst[-1])}")
            go=False
            i=j
        j+=1
    i+=1
j=0
for i in result:
    if(j==int(len(result))-1):
        print(i,end="")
    else:
        print(i,end=" ")
    j+=1