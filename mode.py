# Collector OP
from collections import Counter
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

count = Counter(dataList)


# Please don't look down onto from line 24 to 45 if you want a peaceful moment just feel free to type "python mode.py" in the terminal



# separting things by their occurence
mode = {"75-85":0, "85-95":0, "95-105":0, "105-115":0, "115-125":0, "125-135":0, "135-145":0, "145-155":0, "155-165":0, "165-175":0}
for weight,occurence in count.items() :
    if 75 < float(weight) < 85 : 
        mode["75-85"]+=occurence
    elif 85 < float(weight) < 95 :
        mode["85-95"]+=occurence 
    elif 95 < float(weight) < 105 :
        mode["95-105"]+=occurence
    elif 105 < float(weight) < 115 :
        mode["105-115"]+=occurence 
    elif 115 < float(weight) < 125 :
        mode["115-125"]+=occurence
    elif 125 < float(weight) < 135 :
        mode["125-135"]+=occurence
    elif 135 < float(weight) < 145 :
        mode["135-145"]+=occurence
    elif 145 < float(weight) < 155 :
        mode["145-155"]+=occurence 
    elif 155 < float(weight) < 165 :
        mode["155-165"]+=occurence
    elif 165 < float(weight) < 175 :
        mode["165-175"]+=occurence

modeRange,modeOccurence = 0, 0
for range, occurence in mode.items() :
    if occurence > modeOccurence :
        modeRange, modeOccurence = [int(range.split("-")[0]), int(range.split("-")[1])], occurence

mode = float((modeRange[0]+modeRange[1])/2)
print(mode)
