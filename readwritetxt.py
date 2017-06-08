import datetime
d1 = datetime.datetime.now()
f = open('C:\webserviceTest\shpdaoluzhongxinxian.txt', 'w')
for line in open('C:\webserviceTest\shpdaoluzhongxinxian.xyz'):
    str=line.split()
    lat=str[0].split('.')
    lon=str[1].split('.')
    strlat1=lat[1][0:len(lat[1])-1]
    strlon1 = lon[1][0:len(lon[1]) - 1]
    strlat=float(lat[0])*100+(float(strlat1)*60)/100000
    strlon=float(lon[0])*100+(float(strlon1)*60)/100000
    flat1=("%.4f" % strlat)
    flon1=("%.4f" % strlon)
    d1 = d1 + datetime.timedelta(seconds=2)
    time1=d1.strftime("%H%M%S")+'.00'
    f.write('$GPGGA'+','+time1+','+flat1+',N,'+flon1+',E,'+'0,,,'+'058.3,'+'M,'+'-5.9,'+'M,,'+'*53'+'\n')
f.close()
kk=1