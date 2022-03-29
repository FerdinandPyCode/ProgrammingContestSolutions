x=input()
y=input()
lst=[i for i in x]
cot = 10
res=''
for i in y:
    if i in lst:
        try:
            while True:
                lst.remove(i)
        except ValueError:
            pass
    else:
        cot-=1
    
    if(len(lst)==0):
        res="WIN"
        break
    elif cot==0:
        res="LOSE"
        break
print(res)