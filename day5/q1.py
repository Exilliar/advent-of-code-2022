class Boxes:
    def __init__(self, length):
        self.arr = [[] for l in range(0,int(length/4) + 1)]

    def addToStart(self, value, stackNum):
        if value != " ":
            index = stackNum - 1
            arr = self.arr[index]
            arr.append("")
            for i in range(len(arr) - 1, -1, -1):
                if i != 0:
                    arr[i] = arr[i-1]
                else:
                    arr[i] = value

    def add(self, value, stackNum):
        index = stackNum - 1
        self.arr[index].append(value)

    def remove(self, stackNum):
        index = int(stackNum - 1)
        if len(self.arr[index]) != 0:
            return self.arr[index].pop()
        return ""

    def move(self, _from, to):
        value = self.remove(_from)
        self.add(value, to)

    def printAnswer(self):
        ans = ""
        for a in self.arr:
            if (len(a) == 0):
                ans += " "
            else:
                ans += a[len(a)-1]
        return ans

with open("input.txt", "r") as f:
    lines = f.readlines()
    boxes = Boxes(len(lines[0])-4)
    instructionsIndex = 0
    for index, line in enumerate(lines):
        if line[1] != "1":
            for i in range(1, len(line), 4):
                stack = int(((i-1) / 4) + 1)
                boxes.addToStart(line[i], stack)
        else:
            instructionsIndex = index + 2
            break

    for i in range(instructionsIndex, len(lines)):
        line = lines[i].split(" ")
        move = int(line[1])
        _from = int(line[3])
        to = int(line[5].replace("\n", ""))
        for m in range(0, int(move)):
            boxes.move(_from, to)

    print(boxes.printAnswer())

