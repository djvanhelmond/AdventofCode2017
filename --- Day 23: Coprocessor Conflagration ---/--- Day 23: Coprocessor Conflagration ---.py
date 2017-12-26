#!/usr/local/bin/python3

class CoCpu():
    def __init__(self, instruction_list):
        self.instruction_list = [ instruction.split() for instruction in instruction_list ]
        self.program_counter = 0
        self.registers = {}
        self.muls = 0
        self.__instr_set = {
            'set': self.__set,
            'sub': self.__sub,
            'mul': self.__mul,
            'jnz': self.__jnz,
        }

    def __set(self, x, y):
        if y.isalpha(): y = self.registers[y]
        self.registers[x] = int(y)

    def __sub(self, x, y):
        if y.isalpha(): y = self.registers[y]
        self.registers[x] -= int(y)

    def __mul(self, x, y):
        self.muls += 1
        if y.isalpha(): y = self.registers[y]
        self.registers[x] *= int(y)

    def __jnz(self, x, y):
        if x.isalpha(): x = self.registers[x]
        if y.isalpha(): y = self.registers[y]
        if x != 0:
            self.program_counter += int(y) - 1


    def __exitCriteria(self):
        if self.program_counter >= len(self.instruction_list):
            return True
        return False

    def __execute(self):
        instruction = self.instruction_list[self.program_counter]
        self.program_counter += 1
        self.__instr_set[instruction[0]](*instruction[1:])

    def run(self):
        while not self.__exitCriteria():
            self.__execute()


with open("./input.txt") as f:
    INPUT = f.readlines()

cpu = CoCpu(INPUT)
cpu.registers['a'] = 0
cpu.registers['b'] = 0
cpu.registers['c'] = 0
cpu.registers['d'] = 0
cpu.registers['e'] = 0
cpu.registers['f'] = 0
cpu.registers['g'] = 0
cpu.registers['h'] = 0
cpu.run()
print("Star 1: %i" % cpu.muls)
