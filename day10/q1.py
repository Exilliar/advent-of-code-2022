class CPU:
    cycle = 0
    cycleValues = []
    X = 1
    cycleInstructions = {} # dictionary containing the values to add or subtract from X and when to do that
    currInstruction = ""

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
        if str(self.cycle) in self.cycleInstructions:
            self.X += self.cycleInstructions[str(self.cycle)]
        self.cycleValues.append((self.currInstruction, self.X))
        self.cycle += 1



with open("input.txt", "r") as f:
    cpu = CPU()
    for line in f.readlines():
        splitted = line.replace("\n", "").split(" ")
        if splitted[0] == "addx":
            cpu.addx(int(splitted[1]))
        elif splitted[0] == "noop":
            cpu.noop()
    x = 18
    totalStrengths = 0
    while x < 220:
        val = cpu.cycleValues[x][1]
        curr = x+2 # no idea why +2, it just works
        print(str(curr) + "th: " + str(val) + ", strength: " + str(val * (curr)))
        totalStrengths += val * (curr)
        x += 40
    print("totalStrengths: " + str(totalStrengths))