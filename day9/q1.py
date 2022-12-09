import math

sign = lambda x: math.copysign(1, x)

class Rope:
    head = [0,0] # (x,y)
    tail = [0,0] # (x,y)

    tailHistory = {"0,0": 1}

    def moveHead(self, direction):
        if direction == "R":
            self.head[0] += 1
        elif direction == "L":
            self.head[0] -= 1
        elif direction == "U":
            self.head[1] += 1
        elif direction == "D":
            self.head[1] -= 1

        if self.tail[0] >= self.head[0] - 1 and self.tail[0] <= self.head[0] + 1 and self.tail[1] >= self.head[1] - 1 and self.tail[1] <= self.head[1] + 1:
            return
        else:
            if self.head[0] != self.tail[0]:
                moveDir = sign(self.head[0] - self.tail[0])
                self.tail[0] += int(moveDir)
            if self.head[1] != self.tail[1]:
                moveDir = sign(self.head[1] - self.tail[1])
                self.tail[1] += int(moveDir)
            self.tailHistory[str(self.tail[0]) + "," + str(self.tail[1])] = 1

with open("input.txt", "r") as f:
    rope = Rope()
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        splitted = line.split(" ")
        for i in range(0, int(splitted[1])):
            rope.moveHead(splitted[0])
    print("count: " + str(len(rope.tailHistory)))
