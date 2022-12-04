def checkContains(range0, range1): # range = [lowNum: number, highNum: number]
    return int(range0[0]) <= int(range1[0]) and int(range0[1]) >= int(range1[1])

with open("input.txt", "r") as f:
    total = 0
    containsList = []
    for line in f.readlines():
        line = line.replace("\n", "")
        pairs = line.split(",")
        range0 = pairs[0].split("-")
        range1 = pairs[1].split("-")
        if checkContains(range0, range1) or checkContains(range1, range0):
            total += 1
            containsList.append(line)

    print(total)
