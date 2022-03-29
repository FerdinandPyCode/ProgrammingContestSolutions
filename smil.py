s =input()
lst = []

for pos,char in enumerate(s):
    if(char == ':' or char == ';'):
        try:
            if(s[pos+1] == ')' or (s[pos+1] == '-' and s[pos+2] == ')')):
                lst.append(pos)
        except:
            pass
for i in lst:
    print(i)