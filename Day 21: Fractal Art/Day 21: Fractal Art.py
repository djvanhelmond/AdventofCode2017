#!/usr/local/bin/python3
import math

class artGenerator():
    def __init__(self, rules):
        self.art = [".#.", "..#", "###" ]
        self.enhanceRules = self.__augmentEnhancementRules(rules)

    def __flipPattern(self, inPattern):
        return "/".join([ element[::-1] for element in inPattern.split("/") ])

    def __rotatePattern(self, inPattern):
        rotatedPatterns = []
        for _ in range(3):
            pat = [ element[::-1] for element in inPattern.split("/") ]
            inPattern = "/".join([ "".join([ pat[j][i] for j in range(len(pat)) ]) for i in range(len(pat)) ])
            rotatedPatterns.append(inPattern)
        return rotatedPatterns

    def __augmentEnhancementRules(self, rules):
        rulebase = {}
        for rule in rules:
            inPattern, outPattern = rule.strip("\n").split(" => ")
            rulebase[inPattern] = outPattern
            rulebase[self.__flipPattern(inPattern)] = outPattern
            for rotPattern in self.__rotatePattern(inPattern) + self.__rotatePattern(self.__flipPattern(inPattern)):
                rulebase[rotPattern] = outPattern
        return rulebase

    def __cutArtinSquares(self, art):
        if (len(self.art) % 2 == 0): size = 2
        else: size = 3
        squares = []
        for i in range(0, len(art), size):
            for j in range(0, len(art[i]), size):
                squares.append( "/".join([ art[k][j:j + size] for k in range(i, i + size) ]))
        return squares

    def __recombineSquares(self, squares):
        artSize = int(math.sqrt(len(squares)))
        squares = [ square.split("/") for square in squares ]
        newArt = []
        for i in range(artSize):
            for j in range(len(squares[i])):
                newArt.append("".join([ squares[(i*artSize)+k][j] for k in range(artSize) ]))
        return newArt

    def iterate(self):
        self.art = self.__recombineSquares([self.enhanceRules[square] for square in self.__cutArtinSquares(self.art)])

    def countOn(self):
        return sum([ i.count("#") for i in self.art ])


with open("./input.txt") as f: INPUT = f.readlines()
art = artGenerator(INPUT)
for i in range(18):
    if i == 5: print("Star 1: %i" % art.countOn())
    art.iterate()
print("Star 2: %i" % art.countOn())