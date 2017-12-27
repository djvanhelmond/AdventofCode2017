#!/usr/local/bin/python3

class CPU():
    def __init__(self, instruction_list, version):
        self.version = version
        self.halt = False
        self.program_counter = 0
        self.instruction_list = map(int,[ instruction for instruction in instruction_list ])
        self.__instr_set = {
            'jmp1': self.__jmp1,
            'jmp2': self.__jmp2,
        }

    def __jmp1(self, x):
        self.instruction_list[self.program_counter] += 1
        self.program_counter += x

    def __jmp2(self, x):
        if x >= 3:
            self.instruction_list[self.program_counter] -= 1
        else:
            self.instruction_list[self.program_counter] += 1
        self.program_counter += x

    def __checkExit(self):
        if self.program_counter > len(self.instruction_list) - 1:
            self.halt = True

    def __execute(self):
        instruction_register = self.instruction_list[self.program_counter]
        self.__instr_set[self.version](instruction_register)
        self.__checkExit()

    def step(self):
        self.__execute()




with open("./input.txt") as f:
    INPUT = f.readlines()

star1_maze = CPU(INPUT,'jmp1')
star1_steps = 0
while not star1_maze.halt:
    star1_steps += 1
    star1_maze.step()

star2_maze = CPU(INPUT, 'jmp2')
star2_steps = 0
while not star2_maze.halt:
    star2_steps += 1
    star2_maze.step()

print("Star 1: %i" % star1_steps)
print("Star 2: %i" % star2_steps)



