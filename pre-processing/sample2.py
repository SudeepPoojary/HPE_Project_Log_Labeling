import re
import pandas as pd


logfile = open("datasets\logfile.log","r")

date_time = r'(?P<date>\d{4}-\d{2}-\d{2})\s(?P<time>\d{2}:\d{2}:\d{2})'

dates = []
times = []

for log in logfile:
    match = re.match(date_time,log)
    if match:
        date = match.group('date')
        time = match.group('time')
        dates.append(date)
        times.append(time)
    

print(dates)
print(times)
dict = {'Date':dates, 'Time' : times}
df = pd.DataFrame(dict)
df.to_csv('output2.csv', index=False)