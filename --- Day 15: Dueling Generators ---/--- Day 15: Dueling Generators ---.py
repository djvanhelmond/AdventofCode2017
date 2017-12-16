#!/usr/local/bin/python3

class Generator():
    def __init__(self, init, factor, modulo, multiple):
        self.value = init
        self.factor = factor
        self.modulo = modulo
        self.multiple = multiple

    def getNext(self):
        self.value = (self.value * self.factor) % self.modulo
        while (self.value % self.multiple) != 0:
            self.value = (self.value * self.factor) % self.modulo
        return self.value

class Judge():
    def __init__(self, genA, genB):
        self.generatorA = genA
        self.generatorB = genB
        self.count = 0

    def evalNext(self):
        if self.generatorA.getNext()&0xffff == self.generatorB.getNext()&0xffff:
            self.count += 1


FACTOR_GEN_A = 16807
FACTOR_GEN_B = 48271
MODULO = 2147483647
START_VALUE_GEN_A = 512
START_VALUE_GEN_B = 191


generatorA = Generator(START_VALUE_GEN_A, FACTOR_GEN_A, MODULO, 1)
generatorB = Generator(START_VALUE_GEN_B, FACTOR_GEN_B, MODULO, 1)
judge = Judge(generatorA, generatorB)
for i in xrange(40000000):
    judge.evalNext()
print("Star 1: %i" % judge.count)

generatorA = Generator(START_VALUE_GEN_A, FACTOR_GEN_A, MODULO, 4)
generatorB = Generator(START_VALUE_GEN_B, FACTOR_GEN_B, MODULO, 8)
judge = Judge(generatorA, generatorB)
for i in xrange(5000000):
    judge.evalNext()
print("Star 2: %i" % judge.count)
