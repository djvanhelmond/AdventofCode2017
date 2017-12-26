#!/usr/local/bin/python3

"""
In state A:
  If the current value is 0:
    - Write the value 1.
    - Move one slot to the right.
    - Continue with state B.
  If the current value is 1:
    - Write the value 0.
    - Move one slot to the left.
    - Continue with state B.

state['A'] = {0: (1, 1, 'B'), 1: (0, -1, 'B')}
"""


class TuringMachine():
    def __init__(self, input):
        self.startState, self.diagCheck, self.States = self.__parseInput(input)
        self.state = self.startState
        self.tape = {}
        self.cursor = 0
        for i in xrange(self.diagCheck):
            if i % 10000 == 1: print(float(i)/12317297)
            self.__tick()
        self.__runDiagnosticChecksum()

    def __parseInput(self, input):
        start = input[0].split()[3][0]
        diag = int(input[1].split()[5])
        i = 2
        states = {}
        while i < len(input):
            if "In state" in input[i]:
                stateID = input[i].split()[2][0]
                result = {}
                for x in range(2):
                    write = int(input[i + 2 + 4 * x].split()[4][0])
                    if input[i + 3 + 4 * x].split()[6][0] == "r": step = 1
                    else: step = -1
                    state = input[i + 4 + 4 * x].split()[4][0]
                    result[x] = ((write, step, state))
                states[stateID] = result
            i += 1
        return start, diag, states

    def __runDiagnosticChecksum(self):
        print("Star 1: %i" % sum(self.tape.values()))

    def __runState(self):
        action = self.States[self.state][self.tape[self.cursor]]
        self.tape[self.cursor] = action[0]
        self.cursor += action[1]
        self.state = action[2]

    def __tick(self):
        if not self.cursor in self.tape.keys():
            self.tape[self.cursor] = 0
        self.__runState()


with open("./input.txt") as f:
    INPUT = f.readlines()

tm = TuringMachine(INPUT)







