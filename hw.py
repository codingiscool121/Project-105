import math
import csv

with open('hw.csv') as f:
    reader=csv.reader(f)
    data=list(reader)
data.pop(0)
def mean(data):
    total=0
    n = len(data)
    print(n)
    for i in data:
        total=total+int(i[1])
    mean=total/n
    return mean
meansquare = []
for i in data:
    temp= int(i[1])-mean(data)
    temp=temp**2
    meansquare.append(temp)
sum=0
for i in meansquare:
    sum=sum+i
result=sum/(len(data)-1)
standarddeviation = math.sqrt(result)
print(standarddeviation)