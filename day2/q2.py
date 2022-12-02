# A = Rock
# B = Paper
# C = Siccors

# X = lose
# Y = draw
# Z = win

winners = {
    "A": "C",
    "B": "A",
    "C": "B"
}
loses = {
    "A": "B",
    "B": "C",
    "C": "A"
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
        wld = splitLine[1].replace("\n", "") # wld = win, loss, draw
        if wld == "X": # lose
            score += value["loss"]
            score += value[winners[opp]]
        elif wld == "Y": # draw
            score += value["draw"]
            score += value[opp]
        elif wld == "Z": # win
            score += value["win"]
            score += value[loses[opp]]
    print(score)
