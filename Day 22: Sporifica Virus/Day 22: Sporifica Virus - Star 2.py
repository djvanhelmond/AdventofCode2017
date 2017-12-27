#!/usr/local/bin/python3

class ComputeGrid():
    def __init__(self, givenMap):
        self.gotInfected = 0
        self.coor = [0, 0]
        self.dir = "u"
        self.infected = self.__listInfected(givenMap)
        #self.visOut()

    def __listInfected(self, givenMap):
        mid = len(givenMap) / 2
        outermap = {}
        for line in range(len(givenMap)):
            for char in range(len(givenMap[line].strip())):
                if givenMap[line][char] == "#":
                    outermap[((line - mid), (char - mid))] = givenMap[line][char]
        return outermap

    def __movePos(self):
        moves = {"u": [-1, 0], "l": [0, -1], "r": [0, 1], "d": [1, 0] }
        self.coor = [sum(x) for x in zip(self.coor, moves[self.dir])]

    def __updateDir(self):
        if tuple(self.coor) not in self.infected.keys():
            if self.dir == "u": self.dir = "l"
            elif self.dir == "r": self.dir = "u"
            elif self.dir == "d": self.dir = "r"
            elif self.dir == "l": self.dir = "d"
        else:
            if self.infected[tuple(self.coor)] == "W":
                pass
            elif self.infected[tuple(self.coor)] == "#":
                if self.dir == "u": self.dir = "r"
                elif self.dir == "r": self.dir = "d"
                elif self.dir == "d": self.dir = "l"
                elif self.dir == "l": self.dir = "u"
            elif self.infected[tuple(self.coor)] == "F":
                if self.dir == "u": self.dir = "d"
                elif self.dir == "r": self.dir = "l"
                elif self.dir == "d": self.dir = "u"
                elif self.dir == "l": self.dir = "r"

    def __infect(self):
        if tuple(self.coor) in self.infected.keys():
            if self.infected[tuple(self.coor)] == "W":
                self.infected[tuple(self.coor)] = "#"
                self.gotInfected += 1
            elif self.infected[tuple(self.coor)] == "#":
                self.infected[tuple(self.coor)] = "F"
            elif self.infected[tuple(self.coor)] == "F":
                del self.infected[tuple(self.coor)]
        else:
            self.infected[tuple(self.coor)] = "W"

    def burstWork(self):
        self.__updateDir()
        self.__infect()
        self.__movePos()
        #self.visOut()


    def visOut(self):
        print("---")
        u = min([ x[0] for x in self.infected.keys() ])
        d = max([ x[0] for x in self.infected.keys() ]) + 1
        l = min([ x[1] for x in self.infected.keys() ])
        r = max([ x[1] for x in self.infected.keys() ]) + 1
        for i in xrange(u, d):
            out = ""
            for j in xrange(l, r):
                if tuple(self.coor) == (i, j):
                    if (i, j) in self.infected.keys():
                        out = out + "[" + self.infected[(i, j)] + "]"
                    else:
                        out = out + "[.]"
                elif (i, j) in self.infected.keys():
                    out = out + " " + self.infected[(i, j)] + " "
                else:
                    out = out + " . "
            print(out)
        print(self.gotInfected)


with open("./input.txt") as f:
    INPUT = f.readlines()

gcc = ComputeGrid(INPUT)
for i in xrange(0,10000000):
    if i % 10000 == 0: print("complete: %f%%" % float(float(i) / 100000))
    gcc.burstWork()
print(gcc.gotInfected)







