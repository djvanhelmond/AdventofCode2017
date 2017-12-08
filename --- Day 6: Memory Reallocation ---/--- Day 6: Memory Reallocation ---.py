#!/usr/local/bin/python3

#INPUT = [ 0, 2, 7, 0 ]
INPUT = [ 0, 5, 10, 0, 11, 14, 13, 4, 11, 8, 8, 7, 1, 4, 12, 11 ]

class Memory():
    def __init__(self, configuration):
        self.cycles = 1
        self.looplength = 0
        self.banks = {}
        self.seen = {}
        for i in range(len(configuration)):
            self.banks[i] = configuration[i]

    def __findMostBlocks(self):
        highest = 0
        for i in self.banks.keys():
            if self.banks[i] > self.banks[highest]:
                highest = i
        return highest

    def __redistributeBlocks(self, bankId):
        blocks = self.banks[bankId]
        self.banks[bankId] = 0
        for i in range(1, blocks + 1):
            self.banks[(bankId + i) % len(self.banks)] = self.banks[(bankId + i) % len(self.banks)] + 1

    def cycle(self):
        while not list(self.banks.values()) in self.seen.values():
            self.seen[self.cycles] = list(self.banks.values())
            self.__redistributeBlocks(self.__findMostBlocks())
            self.cycles += 1
        for key, value in self.seen.iteritems():
            if value == list(self.banks.values()):
                self.looplength = self.cycles - key


mem = Memory(INPUT)
mem.cycle()
print("Star 1: %i" % len(mem.seen))
print("Star 2: %i" % mem.looplength)
