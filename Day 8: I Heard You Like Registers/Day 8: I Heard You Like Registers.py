#!/usr/local/bin/python3

class CPU():
    def __init__(self):
        self.registers = {}

    def __eval(self, condition):
        register, operand, value = condition.split()
        value = int(value)
        if register not in self.registers:
            self.registers[register] = 0
        if operand == ">":
            if self.registers[register] > value: return True
        elif operand == "<":
            if self.registers[register] < value: return True
        elif operand == ">=":
            if self.registers[register] >= value: return True
        elif operand == "<=":
            if self.registers[register] <= value: return True
        elif operand == "==":
            if self.registers[register] == value: return True
        elif operand == "!=":
            if self.registers[register] != value: return True
        return False

    def __execute(self, action):
        register, inst, value = action.split()
        value = int(value)
        if register not in self.registers:
            self.registers[register] = 0
        if inst == "inc":
            self.registers[register] += value
        elif inst == "dec":
            self.registers[register] -= value

    def step(self, instruction):
        action, condition = instruction.split("if")
        if self.__eval(condition):
            self.__execute(action)



with open("./input.txt") as f:
    INPUT = f.readlines()

maze = CPU()
highest = 0

for inst in INPUT:
    maze.step(inst)
    if maze.registers[max(maze.registers, key=maze.registers.get)] > highest:
        highest = maze.registers[max(maze.registers, key=maze.registers.get)]

print("Star 1: %i" % maze.registers[max(maze.registers, key=maze.registers.get)])
print("Star 2: %i" % highest)





