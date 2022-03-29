pred=input()
chr=pred[-1]
n=int(input())
lst=[]
for i in range(n):
    lst.append(input())

r=""
print(f"mon pred {chr}")
j=0
for i in lst:
    if i[0]==chr:
        j=i
        r=i
        break


if r=='' :
    print("?")
else:
    print(i)