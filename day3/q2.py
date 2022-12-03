import string
def calcScore(dup):
    s = string.ascii_lowercase.index(dup.lower()) + 1
    if dup.isupper():
        s += 26
    return s

with open("input.txt", "r") as f:
    total = 0
    lines = []
    for index, line in enumerate(f.readlines()):
        line = line.replace("\n", "")
        if (index + 1) % 3 == 0:
            lines.append(line)
            dup = ""
            for l1 in lines[0]:
                for l2 in lines[1]:
                    if l1 == l2:
                        for l3 in lines[2]:
                            if (l3 == l1):
                                dup = l1
            score = calcScore(dup)
            total += score
            lines = []
        else:
            lines.append(line)

    print(total)
