#!/usr/local/bin/python3

class ComputeGrid():
    def __init__(self, givenMap):
        self.gotInfected = 0
        self.coor = [0, 0]
        self.dir = "u"
        self.map = self.__genMap(givenMap)

    def __genMap(self, givenMap):
        mid = len(givenMap) / 2
        outermap = {}
        for line in range(len(givenMap)):
            innermap = {}
            for char in range(len(givenMap[line].strip())):
                innermap[char - mid] = givenMap[line][char]
            outermap[line - mid] = innermap
        return outermap

    def __movePos(self):
        moves = {"u": [-1, 0], "l": [0, -1], "r": [0, 1], "d": [1, 0] }
        self.coor = [sum(x) for x in zip(self.coor, moves[self.dir])]
        if self.coor[0] not in self.map.keys():
            self.map[self.coor[0]] = {}
            self.map[self.coor[0]][self.coor[1]] = "."
        else:
            if self.coor[1] not in self.map[self.coor[0]].keys():
                self.map[self.coor[0]][self.coor[1]] = "."

    def __updateDir(self):
        if self.map[self.coor[0]][self.coor[1]] == "#":
            if self.dir == "u": self.dir = "r"
            elif self.dir == "r": self.dir = "d"
            elif self.dir == "d": self.dir = "l"
            elif self.dir == "l": self.dir = "u"
        else:
            if self.dir == "u": self.dir = "l"
            elif self.dir == "r": self.dir = "u"
            elif self.dir == "d": self.dir = "r"
            elif self.dir == "l": self.dir = "d"

    def __infect(self):
        if self.map[self.coor[0]][self.coor[1]] == "#":
            self.map[self.coor[0]][self.coor[1]] = "."
        else:
            self.map[self.coor[0]][self.coor[1]] = "#"
            self.gotInfected += 1

    def burstWork(self):
        self.__updateDir()
        self.__infect()
        self.__movePos()



with open("./input.txt") as f:
    INPUT = f.readlines()

gcc = ComputeGrid(INPUT)
for i in range(0,10000):
    gcc.burstWork()
print("Star 1: %i" % gcc.gotInfected)










