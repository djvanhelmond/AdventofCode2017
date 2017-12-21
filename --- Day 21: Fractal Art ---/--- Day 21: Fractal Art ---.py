#!/usr/local/bin/python3

import math

class artGenerator():
    def __init__(self, rules):
        self.art = [".#.", "..#", "###" ]
        self.enhancementRules = self.__augmentEnhancementRules(rules)

    def __flipPattern(self, inPattern):
        return "/".join([ element[::-1] for element in inPattern.split("/") ])

    def __rotatePattern(self, inPattern):
        newPatterns = []
        new = inPattern
        for _ in range(3):
            pat = [ m[::-1] for m in new.split("/") ]
            new = []
            for i in range(len(pat)):
                for j in range(len(pat)):
                    new.append(pat[j][i])
                new.append("/")
            new = "".join(new)[:-1]
            newPatterns.append(new)
        return newPatterns

    def __augmentEnhancementRules(self, rules):
        rulebase = {}
        for rule in rules:
            inPattern, outPattern = rule.strip("\n").split(" => ")
            rulebase[inPattern] = outPattern
            rulebase[self.__flipPattern(inPattern)] = outPattern
            for rotPattern in self.__rotatePattern(inPattern):
                rulebase[rotPattern] = outPattern
            for rotPattern in self.__rotatePattern(self.__flipPattern(inPattern)):
                rulebase[rotPattern] = outPattern
        return rulebase

    def __cutArtinSquares(self, art, size):
        squares = []
        for i in range(0, len(art), size):
            for j in range(0, len(art[i]), size):
                squares.append("/".join([ art[k][j:j+size] for k in range(i, i+size) ]))
        return squares

    def __recombineSquares(self, squares, size):
        artSize = int(math.sqrt(len(squares)))
        squares = [ square.split("/") for square in squares ]
        newArt = []
        for h in range(1):
            for i in range(0, artSize):
                for j in range(size+1):
                    line = []
                    for k in range(artSize):
                        line.append(squares[(i*artSize)+k][j])
                    newArt.append("".join(line))
        return newArt

    def itterate(self):
        if (len(self.art) % 2 == 0):
            size = 2
        else:
            size = 3
        squares = self.__cutArtinSquares(self.art, size)
        enhancedSquares = []
        for square in squares:
            enhancedSquares.append(self.enhancementRules[square])
        self.art = self.__recombineSquares(enhancedSquares, size)

    def countOn(self):
        return sum([ i.count("#") for i in self.art ])




with open("./input.txt") as f:
    INPUT = f.readlines()

art = artGenerator(INPUT)
for i in range(18):
    if i == 5: print("Star 1: %i" % art.countOn())
    art.itterate()
print("Star 2: %i" % art.countOn())

