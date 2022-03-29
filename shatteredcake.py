n=int(input())
t=int(input())
som=0
for i in range(t):
    tab=[int(i) for i in input().split(' ')]
    som+=tab[0]*tab[1]

print(int(som/n))