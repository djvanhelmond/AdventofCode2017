#!/usr/local/bin/python3

class Tubes():
    def __init__(self, routingdiagram):
        self.rd = self.__parseRouteDiagram(routingdiagram)
        self.height = len(self.rd)
        self.width = len(self.rd[0])
        self.coor = [0, self.rd[0].index("|")]
        self.dir = "d"
        self.finished = False
        self.letters = []
        self.steps = 0

    def __parseRouteDiagram(self, rd):
        width = max([len(line) for line in rd]) - 1
        return [ [ line[i] if i < len(line) - 1 else " " for i in range(width) ] for line in rd ]

    def __movePos(self):
        self.steps += 1
        moves = {"u": [-1, 0], "l": [0, -1], "r": [0, 1], "d": [1, 0] }
        self.coor = [sum(x) for x in zip(self.coor, moves[self.dir])]

    def __findDirection(self):
        if self.dir == "u" or self.dir == "d":
            if self.coor[1] - 1 >= 0:
                if self.rd[self.coor[0]][self.coor[1] - 1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ-+":
                    self.dir = "l"
            if self.coor[1] + 1 < self.width:
                if self.rd[self.coor[0]][self.coor[1] + 1] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ-+":
                    self.dir = "r"
        elif self.dir == "l" or self.dir == "r":
            if self.coor[0] - 1 >= 0:
                if self.rd[self.coor[0] - 1][self.coor[1]] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ|+":
                    self.dir = "u"
            if self.coor[0] + 1 < self.height:
                if self.rd[self.coor[0] + 1][self.coor[1]] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ|+":
                    self.dir = "d"

    def __evalPos(self):
        if self.rd[self.coor[0]][self.coor[1]] == " ":
            self.finished = True
        elif self.rd[self.coor[0]][self.coor[1]] == "+":
            self.__findDirection()
        elif self.rd[self.coor[0]][self.coor[1]] in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            self.letters.append(self.rd[self.coor[0]][self.coor[1]])

    def stepForward(self):
        self.__movePos()
        self.__evalPos()



with open("./input.txt") as f: INPUT = f.readlines()
tubes = Tubes(INPUT)
while not tubes.finished:
    tubes.stepForward()

print("Star 1: %s" % "".join(tubes.letters))
print("Star 2: %i" % tubes.steps)

