tab=[int(i) for i in input().split(" ")]
f=tab[0]
s=tab[1]
g=tab[2]
u=tab[3]
d=tab[4]

total=0
re=g-s
if (re>0):
    if(u==0):
        print("use the stairs")
    else:
        reste=re%u
        if(u*int((re/u)+1)+s>f):
            print("use the stairs")
        else:
            if(reste==0):
                total=re/u

            elif(reste/d==int(reste/d)):
                total=int(re/u)+reste/d+1
            else:
                print("use the stairs")
else:
    if(d==0):
        print("use the stairs")
    else:
        re=-1*re
        reste=re%d
        if(s-d*int((re/d)+1)<0):
            print("use the stairs")
        else:
            if(reste==0):
                total=re/d

            elif(reste/u==int(reste/u)):
                total=int(re/d)+reste/u+1
            else:
                print("use the stairs")

if total!=0:
    print(int(total))