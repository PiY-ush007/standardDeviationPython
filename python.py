import math
import csv
with open('data.csv', newline='') as f:
    reader = csv.reader(f)
    file_data = list(reader)
data = file_data[0]


def mean(data):
    m = len(data)
    total = 0
    for x in data:
        total += int(x)
    mean = total/m
    return mean


squared_list = []
for number in data:
    value = int(number)-mean(data)
    value = value**2
    squared_list.append(value)
sum = 0
for i in squared_list:
    sum = sum+i
result = sum/(len(data)-1)
standardDeviation = math.sqrt(result)

print(standardDeviation)
