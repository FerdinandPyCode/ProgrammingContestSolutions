import datetime
tab1=[int(i) for i in input().split(":")]
tab2=[int(i) for i in input().split(":")]

time_1 = datetime.timedelta(hours= tab1[0], minutes=tab1[1], seconds=tab1[2])
time_2 = datetime.timedelta(hours=tab2[0], minutes=tab2[1], seconds=tab2[2])

tt=str(time_2 - time_1)
print('mm'+tt)
ttr=tt[-8:]
print('mm'+ttr)
if(ttr[0]==' ' or len(ttr)<9):
    ttr='0'+ttr[1:]

print('mm'+ttr)



#08:00:00