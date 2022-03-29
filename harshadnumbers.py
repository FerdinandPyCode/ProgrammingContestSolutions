def hard(n):
    som=0
    for i in n:
        som+=int(i)
    if int(n)%som==0:
        return int(n)
    return hard(str(int(n)+1))

n=input()
print(hard(n))
