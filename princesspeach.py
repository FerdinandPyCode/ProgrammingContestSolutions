tab=[int(i) for i in input().split(" ")]
lst=[]
for i in range(tab[1]):
    lst.append(int(input()))

for i in range(tab[0]):
    if(i not in lst):
        print(i)
j=set(lst)
print(f"Mario got {int(len(j))} of the dangerous obstacles.")