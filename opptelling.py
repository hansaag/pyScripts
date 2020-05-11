import csv
import sys
import os
from datetime import datetime 
from collections import defaultdict


innFil1 = "GETTY.csv"
innFil2 = "ISTOCK.csv"
innFil3 = "NTB1.csv"
innFil4 = "NTB2.csv"
utFil = "opptellinger.csv"
kolonneNavn = "Download notes"
innfiler = ["GETTY.csv", "ISTOCK.csv", "NTB1.csv", "NTB2.csv"]

lastUpdate = datetime(2019,5,23)

tot= 0
innfil : str
x = 0
e = 1
count = defaultdict(list)
for e in range(2):
    fields = []
    rows = []
    telleIndeks : int
    innfil = innfiler[e]
    with open(innfil, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter = ',')

        fields = next(csvreader)
        i = 0
        for v in fields:
        
            if v == kolonneNavn:
                print(v)
                telleIndeks = i
                break
            i += 1
        print(telleIndeks)
        
        for row in csvreader:
            name = row[telleIndeks]
            tot+=1
            if count.get(name) == None:
                count[name] = [0,0,0,0,0]             # 0-GETTY 1-GETTY_DUP 2-ISTOCK 3-ISTOCK_DUP 4NTB
            
            if row[telleIndeks + 1] == 'Duplicate download':
                count[name][1+x] += 1
            else:
                count[name][0+x] += 1

    csvfile.close()
    x+=2
    

sortedCount = sorted(count.keys(), key=lambda x:x.lower())



if os.path.exists(utFil):
    mode = 'a'
else:
    mode = 'w'


with open(utFil, mode) as output:
    print ("Prosjekt, Getty,Getty Duplikat,Istock,Istock Duplikat, TOTALT: {}".format(str(tot)), file=output)
    for d in sortedCount:
        values = count[d]
        print ("{},{},{},{},{}".format(d, values[0],values[1], values[2],values[3]), file=output)
    print("\n\nhentet: ", datetime.now(), file=output)