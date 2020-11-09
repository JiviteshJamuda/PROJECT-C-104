import csv

with open("SOCR-HeightWeight.csv", newline="") as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
newData = []
newData2 = []
for i in range(len(fileData)):
    num = fileData[i][2]
    num2 = fileData[i][1]
    newData.append(float(num))
    newData2.append(float(num2))

# finding mean
n = len(newData)
n2 = len(newData2)
total = 0
total2 = 0
for x in newData :
    total+=x
for y in newData2 :
    total2 += y

mean = total/n
mean2 = total2/n2
print("mean for weight : " + str(mean))
print("mean for height : " + str(mean2))