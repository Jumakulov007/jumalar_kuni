import os
os.system("cls")
import datetime as d
yil=int(input("Yilni kiriitig: "))
keyingi_yil=yil+1
sana="01.01."+str(yil)
sana=d.datetime.strptime(sana,"%d.%m.%Y")
sch=0
while yil<keyingi_yil:
    if int(sana.strftime("%d"))==13 and sana.strftime("%A")=='Friday':
        sch+=1
        print(f"""{sch}.{sana.strftime("%d %B %Y")}""")
    sana=sana+d.timedelta(days=1)
    yil=int(sana.strftime("%Y"))