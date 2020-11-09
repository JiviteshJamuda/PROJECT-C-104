import csv 

# reading the csv file and storing values in variable
with open("SOCR-HeightWeight.csv", newline="") as f:
    reader = csv.reader(f)
    data = list(reader)

data.pop(0)
dataList = []

for i in range(len(data)):
    num = data[i][2]
    dataList.append(num)

n = len(dataList)
dataList.sort()

if n%2 == 0 :
    # hastag triplets
    median1 = float(dataList[n//2])
    median2 = float(dataList[n//2 - 1])
    median = (median1 + median2)/2
else:
    median = dataList[n//2]
    
print(median)