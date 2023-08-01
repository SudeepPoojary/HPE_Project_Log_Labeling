import numpy as np
import pandas as pd
import re
import csv
from collections import Counter

regex="\"?\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} - ifinfo.*"
y="datasets\logtable.csv"
with open(y) as f:
    fread=f.read()

    ans=re.findall(regex,fread)
    print(len(ans))
    '''with open("ifinfo.csv",'w') as f:
        fwrit=csv.writer(f)
        fwrit.writerow(["data"])
        for i in ans:
            fwrit.writerow([i])'''
    regex1="\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} - rpd.*"
    rpd=re.findall(regex1,fread)
    with open("rpd2.csv",'w') as f:
        fwrite=csv.writer(f)
        fwrite.writerow(["data"])
        for i in rpd:
            fwrite.writerow([i]+[" "])
        
    #print(len(rpd))
    '''regex2="\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} - /usr/sbin.*"
    usr=re.findall(regex2,fread)
    with open("usr.csv",'w') as f:
        fwrit=csv.writer(f)
        fwrit.writerow(['data'])
        for i in usr:
            fwrit.writerow([i])
    regex3="\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} - chassis.*"
    chassis=re.findall(regex3,fread)
    with open("chassis.csv",'w') as f:
        wir=csv.writer(f)
        wir.writerow(["data"])
        for i in chassis:
            wir.writerow([i])'''
#print((chassis))
                
        





regex3="\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2} - chassis.*"
chassis=re.findall(regex3,fread)
#print((chassis))

#print(len(chassis)+len(ans)+len(rpd)+len(usr))
