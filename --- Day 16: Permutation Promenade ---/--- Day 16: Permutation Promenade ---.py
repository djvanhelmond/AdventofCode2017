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
#        print(self.line, move)
        if move[0] in "sxp":
            if move[0] == "s":
                self.__moveSpin(int(move[1:]))
            if move[0] == "x":
                self.__moveExchange([ int(x) for x in move[1:].split('/') ])
            if move[0] == "p":
                self.__movePartner(move[1:].split('/'))
#        print(self.line)



with open("./input.txt") as f:
    INPUT = f.readlines()[0].split(",")


dancers = LineDance(16)
for move in INPUT:
    dancers.executeMove(move)
print("Star 1: %s" % "".join(dancers.line))


