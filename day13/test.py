test = "[0,0,[1,2,[3]]]"


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

print(str(makeArr(test)))
