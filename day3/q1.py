import string

with open("input.txt", "r") as f:
    total = 0
    for line in f.readlines():
        halfIndex = int(len(line)/2)
        firstHalf = line[0:halfIndex]
        secondHalf = line[halfIndex:len(line)]
        dup = "" # the duplicate letter
        for f in firstHalf:
            for s in secondHalf:
                if f == s:
                    dup = f
        score = string.ascii_lowercase.index(dup.lower()) + 1
        if dup.isupper():
            score += 26
        total += score

    print(total)
