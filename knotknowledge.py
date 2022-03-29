n=int(input())
tab=[int(i) for i in input().split(" ")]
tab1=[int(i) for i in input().split(" ")]
for i in tab:
    if i not in tab1:
        print(i)