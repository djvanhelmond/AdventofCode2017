#!/usr/local/bin/python3

class SpinLock():
    def __init__(self, step):
        self.stepSize = step
        self.index = 0
        self.bufferlength = 1
        self.valueAfterZero = None

    def addValue(self, value):
        self.index =  1 + (self.index + self.stepSize) % self.bufferlength
        self.bufferlength += 1
        if self.index == 1:
            self.valueAfterZero = value


STEP = 329
lock = SpinLock(STEP)
for i in xrange(1, 50000001):
    lock.addValue(i)

print("Star 2: %i" % lock.valueAfterZero)
