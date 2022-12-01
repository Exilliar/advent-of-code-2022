with open("input.txt", "r") as f:
    highest = 0
    curr = 0
    for line in f.readlines():
        if line == '' or line == "\n":
            if curr > highest:
                highest = curr
                curr = 0
            else:
                curr = 0
        else:
            curr += int(line)
    print(highest)