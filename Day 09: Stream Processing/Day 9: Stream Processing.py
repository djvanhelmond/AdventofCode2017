#!/usr/local/bin/python3

class GarbageCollector():
    def __init__(self, stream):
        self.stack = []
        self.pointer = 0
        self.score = 0
        self.garbageRemoved = 0
        self.garbageMode = False
        self.stream = stream
        self.__parseStream()

    def __parseStream(self):
        while self.pointer < len(self.stream):
            self.__parseChar()
            self.pointer += 1

    def __parseChar(self):
        if self.stream[self.pointer] == "!":
            self.pointer += 1
        elif self.stream[self.pointer] == ">":
            self.garbageMode = False
        elif self.garbageMode:
            self.garbageRemoved += 1
        else:
            if self.stream[self.pointer] == "<":
                self.garbageMode = True
            if self.stream[self.pointer] == "{":
                self.stack.append(self.pointer)
            if self.stream[self.pointer] == "}":
                group = [self.stack.pop(), self.pointer]
                self.score += len(self.stack) + 1


with open("./input.txt") as f:
    INPUT = f.readlines()

stream = GarbageCollector(INPUT[0])
print("Star 1: %i" % stream.score)
print("Star 2: %i" % stream.garbageRemoved)


