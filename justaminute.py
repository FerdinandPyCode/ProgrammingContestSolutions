n=int(input())
som=0
for i in range(n):
    tab1=[int(i) for i in input().split(' ')]
    som+=tab1[1]/(tab1[0]*60)

print(som/n)