import csv

# reading the csv file and storing values in variable
with open("SOCR-HeightWeight.csv", newline="") as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)

# hastag double troubles starting from here
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

# dont mind the variable names they not for being read just go on and do the "python mean.py" in the terminal
total = 0
total2 = 0

# one for weight
for x in newData :
    total+=x

# another for height
for y in newData2 :
    total2 += y

mean = total/n
mean2 = total2/n2
print("mean for weight : " + str(mean))
print("mean for height : " + str(mean2))