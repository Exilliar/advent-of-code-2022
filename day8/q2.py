with open("input.txt", "r") as f:
    visible = 0
    lines = f.readlines()
    highest = 0
    for yIndex, line in enumerate(lines):
        line = line.replace("\n", "")
        for xIndex, tree in enumerate(line):
            scores = {
                "right": 0,
                "left": 0,
                "top": 0,
                "bottom": 0,
            }
            stopHeight = int(tree)
            # right
            i = xIndex+1
            rightStop = False
            while i < len(line) and rightStop == False:
                scores["right"] += 1
                if int(line[i]) >= stopHeight:
                    rightStop = True
                i += 1

            # left
            i = xIndex - 1
            leftStop = False
            while i >= 0 and leftStop == False:
                scores["left"] += 1
                if int(line[i]) >= stopHeight:
                    leftStop = True
                i -= 1

            # top
            i = yIndex - 1
            topStop = False
            while i >= 0 and topStop == False:
                scores["top"] += 1
                if int(lines[i][xIndex]) >= stopHeight:
                    topStop = True
                i -= 1

            # bottom
            i = yIndex + 1
            bottomStop = False
            while i < len(lines) and bottomStop == False:
                scores["bottom"] += 1
                if int(lines[i][xIndex]) >= stopHeight:
                    bottomStop = True
                i += 1

            # calc score
            score = scores["right"] * scores["left"] * scores["top"] * scores["bottom"]
            if score > highest:
                highest = score

    print("highest: " + str(highest))
