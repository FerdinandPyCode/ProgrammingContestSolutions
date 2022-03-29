tab=[int(i) for i in input().split(" ")]
dico={}
for i in range(1,tab[0]+1):
    for j in range(1,tab[1]+1):
        k=i+j
        if k in dico.keys():
            dico[k]+=1
        else:
            dico[k]=1

listofTuples = sorted(dico.items() , reverse=True, key=lambda x: x[1])
maxe=listofTuples[0][1]
for item in dico.items():
    if item[1]==maxe:
        print(item[0])