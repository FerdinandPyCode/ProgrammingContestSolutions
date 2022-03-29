from math import *
tab=[int(i) for i in input().split(' ')]
r=tab[0]/sin(tab[1]/(180/pi))
if(r==int(r)):
    print(r)
else:
    print(int(r)+1)




#1rad × 180/π = 57,296