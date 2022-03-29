from math import *
n=int(input())
res=[]
for i in range(n):
    tab=[float(i) for i in input().split(" ")]
    t=tab[2]/(tab[0]*cos(tab[1]*(pi/180)))
    y=tab[0]*t*sin(tab[1]*(pi/180)) - 0.5*9.81*t**2

    if tab[3]+1<=y<=tab[4]-1:
        res.append("Safe")
    else:
        res.append("Not Safe")

for i in res:
    print(i)
