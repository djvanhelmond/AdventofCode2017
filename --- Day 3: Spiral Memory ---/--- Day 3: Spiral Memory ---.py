#!/usr/local/bin/python3

INPUT = 289326

################################################################################################
import math
c = math.floor(math.sqrt(INPUT))
if math.pow(c,2) == INPUT:
    print ("Star 1: %i" % int(math.floor(c/2)*2))
else:
    ring = int(math.ceil(c/2))
    rest = (INPUT - (math.pow(c,2))) % (c + 1)
    print ("Star 1: %i\n\n" % int(ring + abs(ring - rest)))

### I tried to solve this in a non-compute and memory intensive way, but have given up for 3.2.
################################################################################################


class spiralMemory():
    def __init__(self):
        self.nrSteps = 1
        self.coor = [0, 0]
        self.dir = "r"
        self.values = {(0, 0): 1}
        self.highest = 1

    def step(self):
        self.movePos()
        self.calcVal()
        self.updateDir()
        self.nrSteps += 1

    def movePos(self):
        moves = {"u": [0, -1], "l": [-1, 0], "r": [1, 0], "d": [0, 1] }
        self.coor = [sum(x) for x in zip(self.coor, moves[self.dir])]

    def updateDir(self):
        if self.coor[0] > abs(self.coor[1]):
            self.dir = "u"
        if abs(self.coor[1]) == self.coor[0] and self.coor[0] != self.coor[1]:
            self.dir = "l"
        if self.coor[0] == self.coor[1] and self.coor[0] < 0:
            self.dir = "d"
        if abs(self.coor[0]) == self.coor[1] and self.coor[0] != self.coor[1]:
            self.dir = "r"

    def calcVal(self):
        totalValue = 0
        windDirections = [ [-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1] ]
        for direction in windDirections:
            if tuple([sum(x) for x in zip(self.coor, direction)]) in self.values:
                totalValue += (self.values[tuple([sum(x) for x in zip(self.coor, direction)])])
        self.values[tuple(self.coor)] = totalValue
        if totalValue > self.highest:
            self.highest = totalValue



star1 = spiralMemory()
while star1.nrSteps < INPUT:
    star1.step()
print("Star 1: Step: %i,  Coordinate: %s,  MHLength: %i" % (star1.nrSteps, star1.coor, abs(star1.coor[0]) + abs(star1.coor[1])))

star2 = spiralMemory()
while star2.highest < INPUT:
    star2.step()
print("Star 2: Step: %i,      Coordinate: %s,       Value: %i" % (star2.nrSteps, star2.coor, star2.values[tuple(star2.coor)]))



