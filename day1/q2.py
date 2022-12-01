with open("input.txt", "r") as f:
    highest = [0,0,0]
    curr = 0
    for line in f.readlines():
        if line == '' or line == "\n":
            if curr > highest[0]:
                highest[0] = curr
            elif curr > highest[1]:
                highest[1] = curr
            elif curr > highest[2]:
                highest[2] = curr
            curr = 0
        else:
            curr += int(line)
    print(sum(highest))