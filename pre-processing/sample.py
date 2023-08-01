import re
import pandas as pd


logfile = open("datasets\logfile.log","r")

date_time = r'\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}'

timestamps = []

for log in logfile:
    timestamp = re.search(date_time,log)
    timestamps.append(timestamp.group())
    

print(timestamps)
dict = {'Timestamp':timestamps}
df = pd.DataFrame(dict)
df.to_csv('output.csv', index=False)