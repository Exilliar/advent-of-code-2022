class Marker:
    arr = []
    markerLen = 14
    def __init__(self) -> None:
        pass

    def add(self, value): # adds to the current marker and returns whether the new marker is a proper marker
        isMarker = True
        if len(self.arr) < self.markerLen:
            self.arr.append(value)
            return False
        else:
            for i in range(0, len(self.arr)-1):
                self.arr[i] = self.arr[i+1]
            self.arr[self.markerLen - 1] = value

        tempArr = []
        for i in self.arr:
            if i in tempArr:
                return False
            else:
                tempArr.append(i)
        return True


with open("input.txt", "r") as f:
    line = f.readlines()[0]
    marker = Marker()
    index = 1
    isMarker = False
    while not isMarker:
        isMarker = marker.add(line[index - 1])
        if not isMarker:
            index += 1
    print(index)
