def findEndBracket(string, start):
    openings = 1 # assuming that we start after the first open brackets
    i = start
    while i < len(string):
        if string[i] == "[":
            openings += 1
        elif string[i] == "]":
            openings -= 1
            if openings == 0:
                return i
        i += 1
    return -1

def makeArr(string):
    endArr = []
    index = 1
    while index < len(string):
        s = string[index]
        if s == "[":
            endIndex = findEndBracket(string, index + 1)
            bracketString = string[index: endIndex]
            endArr.append(makeArr(bracketString))
            index = endIndex
        elif s != "," and s != "]":
            endArr.append(s)
        index += 1
    return endArr

def compareArrays(left, right):
    for index, l in enumerate(left):
        if len(right) - 1 >= index:
            r = right[index]
            if type(l) == list or type(r) == list:
                res = runCheck(l, r)
                if res != None:
                    return res
            elif int(l) < int(r):
                # print("- Left side is smaller, so inputs are in the right order")
                return True
            elif int(l) > int(r):
                # print("- Right side is smaller, so inputs are not in the right order")
                return False
        else:
            # print("right ran out of items so not in right order")
            return False

def runCheck(left, right): # left and right can be str or list
    leftArr = []
    if type(left) == str:
        if left[0] != "[":
            left = "[" + left + "]"
        leftArr = makeArr(left)
    elif type(left) == list:
        leftArr = left
    if type(right) == str:
        if right[0] != "[":
            right = "[" + right + "]"
        rightArr = makeArr(right)
    elif type(right) == list:
        rightArr = right
    return compareArrays(leftArr, rightArr)

with open("input.txt", "r") as f:
    left = ""
    right = ""
    index = 1
    total = 0
    for line in f.readlines():
        line = line.replace("\n", "")
        if len(left) == 0:
            left = line
        elif len(right) == 0:
            right = line
        elif line == "":
            print("left: " + str(left))
            print("right: " + str(right))
            res = runCheck(left, right)
            if res == None or res == True:
                print(str(index) + ". IS right order")
                total += index
            else:
                print(str(index) + ". IS NOT right order")
            left = ""
            right = ""
            index += 1

    res = runCheck(left, right)
    if res == None or res == True:
        print(str(index) + ". IS right order")
        total += index
    else:
        print(str(index) + ". IS NOT right order")

    print("answer: " + str(total))
