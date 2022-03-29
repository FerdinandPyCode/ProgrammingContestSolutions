n=input()
n1=input()

som= 1
for i in range(4):
    if(n[i]==n1[i]):
        som*=1
    else:
        som*=2
print(som)