#!/usr/local/bin/python3

class PipeSystem():
    def __init__(self, programlist):
        self.Graph = self.__buildGraph([ program.split("<->") for program in programlist ])

    def __buildGraph(self, programlist):
        Nodes = {}
        for program in programlist:
            Nodes[int(program[0])] = [ int(x) for x in program[1].split(",") ]
        return Nodes

    def depthFirstSearch(self, start, graph, visited=None):
        if not visited:
            visited = set()
        visited.add(start)
        for next in set(graph[start]) - visited:
            self.depthFirstSearch(next, graph, visited)
        return list(visited)

    def countGroups(self):
        count = 0
        allPrograms = list(self.Graph)
        while len(allPrograms) != 0:
            count += 1
            group = self.depthFirstSearch(allPrograms[0], self.Graph)
            allPrograms = [ program for program in allPrograms if program not in group ]
        return count


with open("./input.txt") as f:
    INPUT = f.readlines()

system = PipeSystem(INPUT)
print("Star 1: %s" % len(system.depthFirstSearch(0, system.Graph)))
print("Star 2: %s" % system.countGroups())

