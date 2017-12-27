#!/usr/local/bin/python3

class messageQueue():
    def __init__(self):
        self.queues = {}

    def register(self, ID):
        self.queues[ID] = []

    def sndValue(self, ID, value):
        self.queues[ID].append(value)

    def rcvValue(self, ID):
        if len(self.queues[ID]) == 0:
            return None
        else:
            return self.queues[ID].pop(0)



class Duet():
    def __init__(self, (id, peer), instruction_list, mq):
        self.id = id
        self.peer = peer
        self.mq = mq
        self.mq.register(id)
        self.instruction_list = [ instruction.split() for instruction in instruction_list ]
        self.program_counter = 0
        self.registers = {}
        self.registers["p"] = self.id
        self.rxLock = False
        self.valSent = 0
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
        if x.isalpha(): x = self.registers[x]
        self.valSent = self.valSent + 1
        self.mq.sndValue(self.peer, int(x))

    def __rcv(self, x):
        self.rxLock = True
        rxBuffer = self.mq.rcvValue(self.id)
        if rxBuffer:
            self.registers[x] = rxBuffer
            self.rxLock = False

    def __jgz(self, x, y):
        if x.isalpha(): x = self.registers[x]
        if y.isalpha(): y = self.registers[y]
        if int(x) > 0:
            self.program_counter += (int(y) - 1)


    def __exitCriteria(self):
        if self.program_counter >= len(self.instruction_list):
            return True
        return False

    def __execute(self):
        instruction = self.instruction_list[self.program_counter]
        if instruction[1].isalpha():
            if instruction[1] not in self.registers:
                self.registers[instruction[1]] = 0
        self.__instr_set[instruction[0]](*instruction[1:])
        if not self.rxLock:
            self.program_counter += 1

    def tick(self):
        if not self.__exitCriteria():
            self.__execute()


with open("./input.txt") as f:
    INPUT = f.readlines()

mq = messageQueue()
programZero = Duet((0, 1), INPUT, mq)
programOne = Duet((1, 0), INPUT, mq)

while not (programOne.rxLock and programZero.rxLock):
    programZero.tick()
    programOne.tick()

print("Star 2: %i" % programOne.valSent)

