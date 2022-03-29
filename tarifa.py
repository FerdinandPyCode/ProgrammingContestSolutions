n=int(input())
t=int(input())
som=n*t
for i in range(t):
    som-=int(input())

print(som+n)