n=float(input())
n1=int(input())
som=0
for i in range(n1):
    tab=[float(i) for i in input().split(" ")]
    som+=tab[0]*tab[1]

print(som*n)