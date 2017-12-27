#!/usr/local/bin/python3

class SpinLock():
    def __init__(self, step):
        self.stepSize = step
        self.index = 0
        self.buffer = [ 0 ]

    def __updateIndex(self):
        self.index =  1 + (self.index + self.stepSize) % len(self.buffer)

    def addValue(self, value):
        self.__updateIndex()
        self.buffer.insert(self.index, value)


STEP = 329
lock = SpinLock(STEP)
for i in range(1, 2018):
    lock.addValue(i)
print("Star 1: %i" % lock.buffer[lock.buffer.index(2017)+1])

