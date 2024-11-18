import pandas as pd
import csv

FILEPATH = 'diode.DAT'
df = pd.read_table(FILEPATH)

data_list = []
for index, segment in zip(range(len(df)), df['X,"ID"']):
    data_list.append(segment.split(','))
    data_list[index][0] = float(data_list[index][0])
    data_list[index][1] = float(data_list[index][1])

# print(data_list)
with open(FILEPATH, 'w', newline='') as f:
    write = csv.writer(f)
    write.writerows(data_list)