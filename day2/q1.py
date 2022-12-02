# A = X = Rock
# B = Y = Paper
# C = Z = Siccors

winners = {
    "A": "C",
    "B": "A",
    "C": "B"
}
conversion = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}
value = {
    "win": 6,
    "draw": 3,
    "loss": 0,
    "A": 1,
    "B": 2,
    "C": 3
}

with open("input.txt", "r") as f:
    score = 0
    for line in f.readlines():
        print("line: " + str(line))
        splitLine = line.split(" ")
        opp = splitLine[0]
        me = conversion[splitLine[1].replace("\n", "")]
        choiceScore = value[me] # the points from the choice of rpc
        resultScore = 0
        if me == opp:
            resultScore = value["draw"]
        elif winners[me] == opp:
            resultScore = value["win"]
        score += choiceScore + resultScore
    print(score)
