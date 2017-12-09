#!/usr/local/bin/python3

import collections

class TowerBuilder():
    def __init__(self, programlist):
        self.Programs = self.__loadPrograms([ program.split() for program in programlist ])
        self.Graph = self.__buildGraph()
        self.root = self.__findRoot()

    def __loadPrograms(self, programlist):
        Nodes = {}
        for program in programlist:
            Nodes[program[0]] = [int(program[1].strip('(').strip(')')), ""]
            if len(program) > 2:
                Nodes[program[0]][1] = [ child.strip(",") for child in program[3:] ]
        return Nodes

    def __buildGraph(self):
        G = {}
        for parent in self.Programs:
            if self.Programs[parent][1]:
                for child in self.Programs[parent][1]:
                    G[child] = parent
        return G

    def __findRoot(self):
        for parent in self.Programs:
            if parent not in self.Graph:
                return parent

    def __calcSubTower(self, parent):
        if not self.Programs[parent][1]:
            return self.Programs[parent][0]
        else:
            disc = []
            for child in self.Programs[parent][1]:
                disc.append(self.__calcSubTower(child))
            return self.Programs[parent][0] + sum(disc)

    def __isBalanced(self, parent):
        if not self.Programs[parent][1]:
            return True
        else:
            values = []
            for child in self.Programs[parent][1]:
                values.append(self.__calcSubTower(child))
            for i in values:
                if i != sum(values)/len(values):
                    return False
                else:
                    return True

    def __findUnbalancedDisc(self, parent):
        unBalancedChild = parent
        for child in self.Programs[parent][1]:
            if not self.__isBalanced(child):
                unBalancedChild = self.__findUnbalancedDisc(child)
        return unBalancedChild


    def findUnbalancedProgram(self, parent):
        tower = {}
        for child in self.Programs[self.__findUnbalancedDisc(parent)][1]:
            tower[child] = self.__calcSubTower(child)
        for k, v in tower.items():
            if v == collections.Counter(tower.values()).most_common()[-1][0]:
                items = [ i[0] for i in collections.Counter(tower.values()).most_common()[:-3:-1] ]
                return (k, self.Programs[k][0] - (items[0] - sum(items[1:])))



with open("./input.txt") as f:
    INPUT = f.readlines()

tower = TowerBuilder(INPUT)
print("Star 1: %s" % tower.root)
print("Star 2: Program '%s' should be: %i" % tower.findUnbalancedProgram(tower.root))