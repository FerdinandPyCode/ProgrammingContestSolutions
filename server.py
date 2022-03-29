n,t=input().split(" ")
n=int(n)
t=int(t)
tasks=[int(i) for i in input().split(" ")]
som=0
j=0
for i in range(n):
    som+=tasks[i]
    if(som>t):
        j=i
        break
    else:
        j=i+1
print(j)
