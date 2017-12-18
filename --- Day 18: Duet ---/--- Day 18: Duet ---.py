#!/usr/local/bin/python3

class Duet():
    def __init__(self, instruction_list):
        self.instruction_list = [ instruction.split() for instruction in instruction_list ]
        self.program_counter = 0
        self.registers = {}
        self.played = None
        self.nonZeroPlayed = False
        self.__instr_set = {
            'set': self.__set,
            'add': self.__add,
            'mul': self.__mul,
            'mod': self.__mod,
            'snd': self.__snd,
            'rcv': self.__rcv,
            'jgz': self.__jgz,
        }

    def __set(self, x, y):
        if y.isalpha(): y = self.registers[y]
        self.registers[x] = int(y)

    def __add(self, x, y):
        if y.isalpha(): y = self.registers[y]
        self.registers[x] += int(y)

    def __mul(self, x, y):
        if y.isalpha(): y = self.registers[y]
        self.registers[x] *= int(y)

    def __mod(self, x, y):
        if y.isalpha(): y = self.registers[y]
        self.registers[x] %= int(y)

    def __snd(self, x):
        self.played = self.registers[x]

    def __rcv(self, x):
        if self.registers[x] != 0:
            self.nonZeroPlayed = True

    def __jgz(self, x, y):
        if self.registers[x] > 0:
            self.program_counter += int(y) - 1


    def __exitCriteria(self):
        if self.nonZeroPlayed:
            return True
        if self.program_counter >= len(self.instruction_list):
            return True
        return False

    def __execute(self):
        instruction = self.instruction_list[self.program_counter]
        self.program_counter += 1
        if instruction[1] not in self.registers:
            self.registers[instruction[1]] = 0
        self.__instr_set[instruction[0]](*instruction[1:])

    def run(self):
        while not self.__exitCriteria():
            self.__execute()


with open("./input.txt") as f:
    INPUT = f.readlines()

duet = Duet(INPUT)
duet.run()
print("Star 1: %s" % duet.played)

