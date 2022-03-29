n=int(input())
lst=[]
for i in range(n):
    k=input()
    if(i%2==0):
        lst.append(k)
for i in lst:
    print(i)