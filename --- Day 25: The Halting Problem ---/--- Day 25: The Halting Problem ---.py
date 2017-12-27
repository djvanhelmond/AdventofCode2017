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
        self.state, self.diagCheck, self.States = self.__parseInput(input)
        self.tape = {0: 0}
        self.cursor = 0
        self.currange = [0, 0]

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

    def runDiagnosticChecksum(self):
        print("Star 1: %i" % sum(self.tape.values()))

    def tick(self):
        if not self.currange[0] <= self.cursor <= self.currange[1]:
            self.tape[self.cursor] = 0
            self.currange = [ min(self.currange[0], self.cursor), max(self.currange[1], self.cursor) ]
        action = self.States[self.state][self.tape[self.cursor]]
        self.tape[self.cursor] = action[0]
        self.cursor += action[1]
        self.state = action[2]


with open("./input.txt") as f:
    INPUT = f.readlines()

tm = TuringMachine(INPUT)
for i in xrange(tm.diagCheck):
    if i % 1000000 == 317296: print("Calculating: %i%%" % int((float(i) / 123172)))
    tm.tick()
tm.runDiagnosticChecksum()







