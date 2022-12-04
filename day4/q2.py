def checkContains(range0, range1): # range = [lowNum: number, highNum: number]
    return range0[0] <= range1[0] and range0[1] >= range1[0]

with open("input.txt", "r") as f:
    total = 0
    containsList = []
    for line in f.readlines():
        line = line.replace("\n", "")
        pairs = line.split(",")
        range0Temp = pairs[0].split("-")
        range0 = [int(range0Temp[0]),int(range0Temp[1])]
        range1Temp = pairs[1].split("-")
        range1 = [int(range1Temp[0]),int(range1Temp[1])]
        if checkContains(range0, range1) or checkContains(range1, range0):
            total += 1
            containsList.append(line)

    print(total)
