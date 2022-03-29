tab=[]
for i in range(5):
    if "FBI" in input():
        tab.append(i+1)

if len(tab)==0:
    print("HE GOT AWAY!")
else:
    j=0
    for i in tab:
        if(j==int(len(tab)-1)):
            print(i)
        else:
            print(i,end=' ')