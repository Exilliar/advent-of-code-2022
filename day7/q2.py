class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __str__(self):
        return "- " + self.name + " (file, size=" + str(self.size) + ")"

class Folder:
    folders = [] # the sub folders this folder contains
    files = [] # the files this folder contains
    size = 0
    def __init__(self, name, parent = None):
        self.folders = []
        self.files = []
        self.size = 0
        self.name = name
        self.parent = parent

    def addFolder(self, name):
        if self.moveDown(name) != None:
            return None
        self.folders.append(Folder(name, self))

    def addFile(self, name, size):
        self.files.append(File(name, size))

    def moveDown(self, name):
        for folder in self.folders:
            if folder.name == name:
                return folder
        return None

    def __str__(self) -> str:
        out = "- " + self.name + " (dir, size=" + str(self.size) + ")\n"
        tabs = 0
        curr = self
        while curr != None:
            curr = curr.parent
            tabs += 1
        tabsStr = "".join(["\t" for i in range(0, tabs)])
        for file in self.files:
            out += tabsStr + str(file) + "\n"
        for folder in self.folders:
            out += tabsStr + str(folder) + "\n"
        return out

    def calcSize(self):
        totalSize = 0
        for file in self.files:
            totalSize += int(file.size)
        for folder in self.folders:
            folder.calcSize()
            totalSize += int(folder.size)
        self.size = totalSize

    def getValid(self, limit, validFolders):
        if self.size == 0:
            self.calcSize()
        if self.size <= limit:
            validFolders.append(self)
        for folder in self.folders:
            folder.getValid(limit, validFolders)


with open("input.txt", "r") as f:
    currentFolder = None
    for line in f.readlines():
        line = line.replace("\n", "")
        parts = line.split(" ")
        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "..":
                    currentFolder = currentFolder.parent
                elif currentFolder == None:
                    currentFolder = Folder(parts[2])
                else:
                    currentFolder = currentFolder.moveDown(parts[2])
        elif parts[0] == "dir":
            currentFolder.addFolder(parts[1])
        else:
            currentFolder.addFile(parts[1], parts[0])

    while currentFolder.parent != None:
        currentFolder = currentFolder.parent
    currentFolder.calcSize()
    validFolders = []
    currentFolder.getValid(70000000, validFolders)
    totalSize = 0
    for folder in validFolders:
        totalSize += int(folder.size)
    maxSize = 70000000
    updateSize = 30000000
    currentSize = currentFolder.size
    spaceOver = maxSize - currentSize
    spaceRequired = updateSize - spaceOver

    currentChoice = None
    for folder in validFolders:
        if currentChoice == None:
            currentChoice = folder
        elif folder.size >= spaceRequired and folder.size < currentChoice.size:
            currentChoice = folder
    print("currentChoice name: " + str(currentChoice.name) + ", size: " + str(currentChoice.size))
