import math

sign = lambda x: math.copysign(1, x)

class Knot:
    head = [0,0]
    history = {"0,0": 1}
    tail = None
    name = ""
    def __init__(self, tail = None, name = ""):
        self.tail = tail
        self.name = name
        self.history = {"0,0": 1}
        self.head = [0,0]

    def moveHead(self, directions):
        print("move " + self.name)
        if directions[0] == "R":
            self.head[0] += 1
        elif directions[0] == "L":
            self.head[0] -= 1
        elif directions[1] == "U":
            self.head[1] += 1
        elif directions[1] == "D":
            self.head[1] -= 1
        self.history[str(self.head[0]) + "," + str(self.head[1])] = 1

        if self.tail != None and self.tail.head[0] >= self.head[0] - 1 and self.tail.head[0] <= self.head[0] + 1 and self.tail.head[1] >= self.head[1] - 1 and self.tail.head[1] <= self.head[1] + 1:
            return
        elif self.tail != None:
            moveDirs = ["",""]
            if self.head[0] != self.tail.head[0]:
                moveDir = sign(self.head[0] - self.tail.head[0])
                if moveDir == 1:
                    # print(self.name + ", move tail")
                    # self.tail.moveHead("R")
                    moveDirs[0] = "R"
                else:
                    # print(self.name + ", move tail")
                    # self.tail.moveHead("L")
                    moveDirs[0] = "L"
                # self.tail[0] += int(moveDir)
            if self.head[1] != self.tail.head[1]:
                moveDir = sign(self.head[1] - self.tail.head[1])
                if moveDir == 1:
                    moveDirs[1] = "U"
                    # print(self.name + ", move tail")
                    # self.tail.moveHead("U")
                else:
                    # print(self.name + ", move tail")
                    # self.tail.moveHead("D")
                    moveDirs[1] = "D"
                # self.tail.head[1] += int(moveDir)
            if moveDirs[0] != "" or moveDirs[1] != "":
                print(self.name + ", move tail")
                self.tail.moveHead(moveDirs)
            self.history[str(self.head[0]) + "," + str(self.head[1])] = 1

# class Knot:
#     head = [0,0] # (x,y)
#     tail = [0,0] # (x,y)

#     tailHistory = {"0,0": 1}

#     def moveHead(self, direction):
#         if direction == "R":
#             self.head[0] += 1
#         elif direction == "L":
#             self.head[0] -= 1
#         elif direction == "U":
#             self.head[1] += 1
#         elif direction == "D":
#             self.head[1] -= 1

#         if self.tail[0] >= self.head[0] - 1 and self.tail[0] <= self.head[0] + 1 and self.tail[1] >= self.head[1] - 1 and self.tail[1] <= self.head[1] + 1:
#             return
#         else:
#             if self.head[0] != self.tail[0]:
#                 moveDir = sign(self.head[0] - self.tail[0])
#                 self.tail[0] += int(moveDir)
#             if self.head[1] != self.tail[1]:
#                 moveDir = sign(self.head[1] - self.tail[1])
#                 self.tail[1] += int(moveDir)
#             self.tailHistory[str(self.tail[0]) + "," + str(self.tail[1])] = 1

with open("input.txt", "r") as f:
    # rope = Rope()
    nine = Knot(name="nine")
    eight = Knot(nine,name="eight")
    seven = Knot(eight,name="seven")
    six = Knot(seven,name="six")
    five = Knot(six,name="five")
    four = Knot(five,name="four")
    three = Knot(four,name="three")
    two = Knot(three,name="two")
    one = Knot(two,name="one")
    head = Knot(one,name="head")
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        splitted = line.split(" ")
        for i in range(0, int(splitted[1])):
            print("\nmove")
            # head.moveHead(splitted[0])
            dir = splitted[0]
            if dir == "R" or dir == "L":
                head.moveHead([dir,""])
            elif dir == "U" or dir == "D":
                head.moveHead(["",dir])
    print("count: " + str(len(nine.history)))
