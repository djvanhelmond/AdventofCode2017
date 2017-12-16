#!/usr/local/bin/python3

class LineDance():
    def __init__(self, length):
        self.line = [ chr(x) for x in range(97,97+length) ]

    def __moveSpin(self, places):
        self.line = self.line[-places:] + self.line[:-places]

    def __moveExchange(self, pos):
        self.line[pos[0]], self.line[pos[1]] = self.line[pos[1]], self.line[pos[0]]

    def __movePartner(self, chars):
        self.__moveExchange([self.line.index(chars[0]),self.line.index(chars[1])])

    def executeMove(self, move):
        if move[0] in "sxp":
            if move[0] == "s":
                self.__moveSpin(int(move[1:]))
            elif move[0] == "x":
                self.__moveExchange(map(int,move[1:].split('/')))
            elif move[0] == "p":
                self.__movePartner(move[1:].split('/'))



with open("./input.txt") as f:
    INPUT = f.readlines()[0].split(",")

seen = []
dancers = LineDance(16)
while "".join(dancers.line) not in seen:
    seen.append("".join(dancers.line))
    for move in INPUT:
        dancers.executeMove(move)
print("Star 1: %s" % seen[1 % len(seen)])
print("Star 2: %s" % seen[1000000000 % len(seen)])
