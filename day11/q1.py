import math

class Monkey:
    def __init__(self, name, startingItems, operation, operationVal, test, trueVal, falseVal, inspected = 0):
        self.name = name
        self.items = startingItems
        self.operation = operation
        self.operationVal = operationVal
        self.test = test
        self.trueVal = trueVal
        self.falseVal = falseVal
        self.inspected = inspected

    def removeItem(self, item):
        newItems = []
        for i in self.items:
            if i != item:
                newItems.append(i)
        self.items = newItems

    def __str__(self):
        out = ""
        out += "name: " + str(self.name) + "\n"
        out += "items: " + str(self.items) + "\n"
        out += "operation: " + str(self.operation) + "\n"
        out += "operationVal: " + str(self.operationVal) + "\n"
        out += "test: " + str(self.test) + "\n"
        out += "trueVal: " + str(self.trueVal) + "\n"
        out += "falseVal: " + str(self.falseVal)
        return out

def makeOperation(operation, val):
    def square(old, _):
        return old * old
    def mult(old, val):
        return old * val
    def add(old, val):
        return old + val

    if operation == "*":
        if val == "old":
            return ("multiplied by itself", square)
        else:
            return ("is multiplied by", mult)
    elif operation == "+":
        return ("increases by", add)

with open("input.txt", "r") as f:
    # make the monkeys
    tempMonkey = {}
    monkeys = {}
    for line in f.readlines():
        line = line.replace("\n", "")
        splitted = line.split(" ")
        if len(splitted) == 1:
            monkeys[tempMonkey["name"]] = Monkey(tempMonkey["name"], tempMonkey["items"], tempMonkey["operation"], tempMonkey["operationVal"], tempMonkey["test"], tempMonkey["trueMonkey"], tempMonkey["falseMonkey"])
        elif splitted[0] == "Monkey":
            tempMonkey["name"] = splitted[1].replace(":", "")
        elif splitted[2] == "Starting":
            tempItems = line.split(":")[1].replace(" ", "").split(",")
            items = []
            for item in tempItems:
                items.append(int(item))
            tempMonkey["items"] = items
        elif splitted[2] == "Operation:":
            strOp = line.split(":")[1].split(" ")
            operation = makeOperation(strOp[4],strOp[5])
            tempMonkey["operation"] = operation
            if strOp[5] == "old":
                tempMonkey["operationVal"] = -1
            else:
                tempMonkey["operationVal"] = strOp[5]
        elif splitted[2] == "Test:":
            tempMonkey["test"] = splitted[5]
        elif splitted[4] == "If" and splitted[5] == "true:":
            tempMonkey["trueMonkey"] = splitted[9]
        elif splitted[4] == "If" and splitted[5] == "false:":
            tempMonkey["falseMonkey"] = splitted[9]
    monkeys[tempMonkey["name"]] = Monkey(tempMonkey["name"], tempMonkey["items"], tempMonkey["operation"], tempMonkey["operationVal"], tempMonkey["test"], tempMonkey["trueMonkey"], tempMonkey["falseMonkey"])

    for monkey in monkeys:
        print("\nmonkey: " + str(monkeys[monkey]))

    # do the rounds
    rounds = 20
    for round in range(0, rounds):
        for key in monkeys:
            monkey = monkeys[key]
            print("Monkey " + str(monkey.name) + ":")
            for item in monkey.items:
                monkey.inspected += 1
                print("\tMonkey inspects an item with a worry level of " + str(item) + ".")
                newVal = monkey.operation[1](int(item), int(monkey.operationVal))
                print("\t\tWorry level " + monkey.operation[0] + " " + str(monkey.operationVal) + " to " + str(newVal) + ".")
                divided = math.trunc(newVal / 3)
                print("\t\tMonkey gets bored with item. Worry level is divided by 3 to " + str(divided) + ".")
                sendTo = ""
                if divided % int(monkey.test) == 0:
                    sendTo = monkey.trueVal
                else:
                    sendTo = monkey.falseVal
                print("\t\tItem with worry level " + str(divided) + " is thrown to monkey " + str(sendTo) + ".")
                monkeys[sendTo].items.append(divided)
                monkey.removeItem(item)

    # print some stuff
    for key in monkeys:
        print("Monkey " + key + ": " + str(monkeys[key].items))

    for key in monkeys:
        print("Monkey " + key + " inspected items " + str(monkeys[key].inspected) + " times.")

    # find monkey business
    # find two highest
    highest = [0,0]
    for key in monkeys:
        monkey = monkeys[key]
        if monkey.inspected > highest[0]:
            highest[1] = highest[0]
            highest[0] = monkey.inspected
        elif monkey.inspected > highest[1]:
            highest[1] = monkey.inspected
    monkeyBusiness = highest[0] * highest[1]
    print("Monkey business: " + str(monkeyBusiness))
