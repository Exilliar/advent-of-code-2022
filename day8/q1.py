with open("input.txt", "r") as f:
    visible = 0
    lines = f.readlines()
    for lIndex, line in enumerate(lines):
        line = line.replace("\n", "")
        if lIndex == 0 or lIndex == len(lines) - 1:
            visible += len(line)
        else:
            trees = line
            for tIndex, tree in enumerate(trees):
                if tIndex == 0 or tIndex == len(trees) - 1:
                    visible += 1
                else:
                    if int(tree) != 0:
                        visibleHeight = int(tree) - 1
                        isVisible = True
                        # look right
                        visibleRight = True
                        for i in range(tIndex+1, len(trees)):
                            if int(trees[i]) > visibleHeight:
                                visibleRight = False
                        # look left
                        visibleLeft = True
                        for i in range(0, tIndex):
                            if int(trees[i]) > visibleHeight:
                                visibleLeft = False
                        # look top
                        visibleTop = True
                        for i in range(0, lIndex):
                            if int(lines[i][tIndex]) > visibleHeight:
                                visibleTop = False
                        # look bottom
                        visibleBottom = True
                        for i in range(lIndex+1, len(lines)):
                            if int(lines[i][tIndex]) > visibleHeight:
                                visibleBottom = False
                        if visibleRight == True or visibleLeft == True or visibleTop == True or visibleBottom:
                            visible += 1
    print("visible: " + str(visible))
