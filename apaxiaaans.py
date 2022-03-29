n=input()
lst=[n[0]]
l=int(len(n))
for i in range(1,l):
    if n[i]==n[i-1]:
        lst.pop(-1)
        lst.append(n[i])
    else:
        lst.append(n[i])

print(''.join(lst))