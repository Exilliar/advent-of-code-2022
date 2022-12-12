import sys
import math

alphabet = list("abcdefghijklmnopqrstuvwxyz")

class Node:
    def __init__(self, id, height, start = False, end = False) -> None:
        self.id = id
        self.height = height
        self.prevNode = None
        self.geoDistTo = None
        self.distTo = sys.maxsize
        self.paths = [] # { node: Node; distance: number }[]
        self.visited = False
        self.start = start
        self.end = end

    def __str__(self):
        # return str(self.id)
        if self.start == False and self.end == False:
            return str(self.id)
        elif self.start == True:
            return "Str"
        elif self.end == True:
            return "End"
        return "err"

class PriorityQueue:
    def __init__(self, init: Node):
        self.queue = [init]

    def add(self, node: Node):
        if any(obj.id == node.id for obj in self.queue):
            return
        updateArr = []
        added = False
        bDist = node.distTo + node.geoDistTo

        for q in self.queue:
            aDist = q.distTo + q.geoDistTo

            if bDist < aDist and added == False:
                updateArr.append(node)
                updateArr.append(q)
                added = True
            else:
                updateArr.append(q)

        if len(updateArr) == len(self.queue):
            updateArr.append(node)

        self.queue = updateArr

    def top(self):
        return self.queue.pop(0)

with open("input.txt", "r") as f:
    # make node objects
    start = None
    end = None
    nodes = []
    for y, line in enumerate(f.readlines()):
        line = line.replace("\n", "")
        nodes.append([])
        for x, node in enumerate(list(line)):
            val = node
            isStart = False
            isEnd = False
            if node == "S":
                val = "a"
                isStart = True
            elif node == "E":
                val = "z"
                isEnd = True
            nodeObj = Node(str(x) + "," + str(y), val, isStart, isEnd)
            nodes[y].append(nodeObj)
            if node == "S":
                start = nodeObj
            elif node == "E":
                end = nodeObj

    for line in nodes:
        lineStr = ""
        for node in line:
            lineStr += str(node) + ", "

    # make paths
    splittedEnd = end.id.split(",")
    endX = int(splittedEnd[0])
    endY = int(splittedEnd[1])
    for y, line in enumerate(nodes):
        for x, node in enumerate(line):
            valPos = alphabet.index(node.height)
            splittedNode = node.id.split(",")
            nodeX = int(splittedNode[0])
            nodeY = int(splittedNode[1])
            node.geoDistTo = math.sqrt((endX - nodeX) ** 2 + (endY - nodeY) ** 2)
            if x != len(line) - 1:
                # right
                rightNode: Node = nodes[y][x+1]
                rightVal = alphabet.index(rightNode.height)
                if rightVal <= valPos + 1:
                    node.paths.append({ "node": rightNode, "distance": 1 })
            if x != 0:
                # left
                leftNode: Node = nodes[y][x-1]
                leftVal = alphabet.index(leftNode.height)
                if leftVal <= valPos + 1:
                    node.paths.append({ "node": leftNode, "distance": 1 })

            if y != 0:
                # up
                upNode: Node = nodes[y-1][x]
                upVal = alphabet.index(upNode.height)
                if upVal <= valPos + 1:
                    node.paths.append({ "node": upNode, "distance": 1 })

            if y != len(nodes) - 1:
                # down
                downNode: Node = nodes[y+1][x]
                downVal = alphabet.index(downNode.height)
                if downVal <= valPos + 1:
                    node.paths.append({ "node": downNode, "distance": 1 })

    # actually run A* to calc the path
    start.distTo = 0
    priorityQueue = PriorityQueue(start)
    current = priorityQueue.top()
    nodesVisited = 0
    while current.id != end.id:
        currentDist = current.distTo

        for path in current.paths:
            dist = currentDist + path["distance"]
            if dist < path["node"].distTo and path["node"].visited == False:
                path["node"].distTo = dist
                path["node"].prevNode = current
                priorityQueue.add(path["node"])

        current = priorityQueue.top()
        nodesVisited += 1

    # go back through the path
    route = [end]
    currentNode = end
    steps = 0
    while current.id != start.id:
        steps += 1
        current = current.prevNode
        route.append(current)
    route.reverse()
    for index, step in enumerate(route):
        print(str(index) + ": " + str(step))

    print("steps: " + str(steps))
