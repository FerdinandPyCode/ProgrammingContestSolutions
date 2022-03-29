n=int(input())
som=0
for i in range(n):
    tab=[float(i) for i in input().split(' ')]
    som+=tab[0]*tab[1]

print(som)