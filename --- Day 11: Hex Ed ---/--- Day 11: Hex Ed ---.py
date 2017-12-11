#!/usr/local/bin/python3

class HexGrid():
    def __init__(self, path):
        self.coor = [float(0), float(0)]
        self.furthest = 0
        self.__parsePath(path.split(","))

    def __parsePath(self, path):
        for step in path:
            if step == "n":
                self.coor[0] += -1
                self.coor[1] += 0
            elif step == "nw":
                self.coor[0] += -0.5
                self.coor[1] += -1
            elif step == "ne":
                self.coor[0] += -0.5
                self.coor[1] += 1
            elif step == "s":
                self.coor[0] += 1
                self.coor[1] += 0
            elif step == "sw":
                self.coor[0] += 0.5
                self.coor[1] += -1
            elif step == "se":
                self.coor[0] += 0.5
                self.coor[1] += 1
            distance = self.calcSteps(list(self.coor))
            if distance > self.furthest:
                self.furthest = distance

    def calcSteps(self, coor):
        steps = 0
        while coor != [0, 0]:
#            print(coor)
            steps += 1
            if (coor[0] > 0) and (coor[1] == 0):
                coor[0] += -1
                coor[1] += 0
            elif (coor[0] < 0) and (coor[1] == 0):
                coor[0] += 1
                coor[1] += 0
            elif (coor[0] == 0) and (coor[1] < 0):
                coor[0] += -0.5
                coor[1] += 1
            elif (coor[0] == 0) and (coor[1] > 0):
                coor[0] += -0.5
                coor[1] += -1
            elif (coor[0] < 0) and (coor[1] < 0):
                coor[0] += 0.5
                coor[1] += 1
            elif (coor[0] > 0) and (coor[1] < 0):
                coor[0] += -0.5
                coor[1] += 1
            elif (coor[0] < 0) and (coor[1] > 0):
                coor[0] += 0.5
                coor[1] += -1
            elif (coor[0] > 0) and (coor[1] > 0):
                coor[0] += -0.5
                coor[1] += -1
        return steps


with open("./input.txt") as f:
    INPUT = f.readlines()

for i in INPUT:
    path = HexGrid(i)
    print("Star 1: %i" % path.calcSteps(list(path.coor)))
    print("Star 2: %i" % path.furthest)


