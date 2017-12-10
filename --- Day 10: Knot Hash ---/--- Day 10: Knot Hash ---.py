#!/usr/local/bin/python3

class KnotHash():
    def __init__(self, length):
        self.string = [ x for x in range(length)]
        self.currentPos = 0
        self.skipSize = 0


    def hash(self, lengthSeq, rounds):
        for _ in range(rounds):
            for length in lengthSeq:
                self.__reverseOrder(length)
                self.currentPos = (self.currentPos + length + self.skipSize) % len(self.string)
                self.skipSize += 1


    def __reverseOrder(self, length):
        self.string = self.string[-(len(self.string) - self.currentPos):] + self.string[:-(len(self.string) - self.currentPos)]
        newstring = []
        for i in range(len(self.string)):
            if i < length:
                newstring.append(self.string[length - i - 1])
            else:
                newstring.append(self.string[i])
        self.string = newstring[-self.currentPos:] + newstring[:-self.currentPos]


    def denseHash(self):
        hash = ""
        for i in range(16):
            dense = 0
            for m in range(16):
                dense ^= self.string[16 * i + m]
            hash += "{:02x}".format(dense)
        return hash




INPUT = "106,16,254,226,55,2,1,166,177,247,93,0,255,228,60,36"

knot = KnotHash(256)
knot.hash([ int(x) for x in INPUT.split(",") ], 1)
print("Star 1: %i" % (knot.string[0] * knot.string[1]))

knot = KnotHash(256)
knot.hash([ (ord(i)) for i in INPUT ] + [17, 31, 73, 47, 23], 64)
print("Star 2: %s" % (knot.denseHash()))


