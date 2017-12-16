#!/usr/local/bin/python3

class LineDance():
    def __init__(self, length):
        self.line = [ chr(x) for x in range(97,97+length) ]

    def __moveSpin(self, places):
        self.line = self.line[-places:] + self.line[:-places]

    def __moveExchange(self, pos):
        temp = self.line[pos[0]]
        self.line[pos[0]] = self.line[pos[1]]
        self.line[pos[1]] = temp

    def __movePartner(self, chars):
        firstPos = self.line.index(chars[0])
        secondPos = self.line.index(chars[1])
        self.__moveExchange([firstPos,secondPos])

    def executeMove(self, move):
        if move[0] in "sxp":
            if move[0] == "s":
                self.__moveSpin(int(move[1:]))
            if move[0] == "x":
                self.__moveExchange([ int(x) for x in move[1:].split('/') ])
            if move[0] == "p":
                self.__movePartner(move[1:].split('/'))



with open("./input.txt") as f:
    INPUT = f.readlines()[0].split(",")

dancers = LineDance(16)
for move in INPUT:
    dancers.executeMove(move)
print("Star 1: %s" % "".join(dancers.line))


seen = []
dancers = LineDance(16)
while "".join(dancers.line) not in seen:
    seen.append("".join(dancers.line))
    for move in INPUT:
        dancers.executeMove(move)
for _ in range(1000000000 % len(seen)):
    for move in INPUT:
        dancers.executeMove(move)
print("Star 2: %s" % "".join(dancers.line))


