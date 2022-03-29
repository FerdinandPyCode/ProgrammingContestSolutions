n=input()
s1=0
s2=0
s3=0
s4=0
for i in n:
    if 97<=ord(i)<=122:
        s1+=1

    elif 65<=ord(i)<=90:
        s2+=1
    
    elif ord(i)==95:
        s3+=1
    
    else:
        s4+=1
k=int(len(n))
print(s3/k)
print(s1/k)
print(s2/k)
print(s4/k)