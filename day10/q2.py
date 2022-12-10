class CPU:
    cycle = 0
    cycleValues = []
    X = 1
    cycleInstructions = {} # dictionary containing the values to add or subtract from X and when to do that
    currInstruction = ""
    screen = []
    screenXPos = 0
    screenYPos = 0

    def addx(self, x):
        self.currInstruction = "addx " + str(x)
        timeToDo = self.cycle + 1
        self.cycleInstructions[str(timeToDo)] = x
        oldX = self.X
        while self.X != oldX + x:
            self.incCycle()

    def noop(self):
        self.currInstruction = "noop"
        self.incCycle()

    def incCycle(self):
        self.draw()
        if str(self.cycle) in self.cycleInstructions:
            self.X += self.cycleInstructions[str(self.cycle)]
        self.cycleValues.append((self.currInstruction, self.X))
        self.cycle += 1

    def draw(self):
        if self.screenXPos == 0:
            self.screen.append("")
        if self.screenXPos >= self.X-1 and self.screenXPos <= self.X+1:
            self.screen[self.screenYPos] += "#"
        else:
            self.screen[self.screenYPos] += "."
        self.screenXPos += 1
        if self.screenXPos > 39:
            self.screenXPos = 0
            self.screenYPos += 1

    def printScreen(self):
        for line in self.screen:
            print(line)



with open("input.txt", "r") as f:
    cpu = CPU()
    for line in f.readlines():
        splitted = line.replace("\n", "").split(" ")
        if splitted[0] == "addx":
            cpu.addx(int(splitted[1]))
        elif splitted[0] == "noop":
            cpu.noop()
    cpu.printScreen()