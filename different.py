import sys
lst=[]
for line in sys.stdin:
    line=line[:-1]
    n=[int(i) for i in line.split(" ")]
    lst.append(abs(n[0]-n[1]))
for i in lst:
    print(i)