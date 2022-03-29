n=int(input())
som=0
i=1
while True:
    if n-i**2 >=0:
        n=n-i**2
        som+=1
    else:
        break
    i+=2

print(som)