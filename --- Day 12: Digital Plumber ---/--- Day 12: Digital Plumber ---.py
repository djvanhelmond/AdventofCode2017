#!/usr/local/bin/python3

class PipeSystem():
    def __init__(self, programlist):
        self.Programs = self.__loadPrograms([ program.split("<->") for program in programlist ])
        self.Graph = self.__buildGraph()

    def __loadPrograms(self, programlist):
        Nodes = {}
        for program in programlist:
            Nodes[int(program[0])] = [ int(x) for x in program[1].split(",") ]
        return Nodes

    def __buildGraph(self):
        G = {}
        for source in self.Programs:
            G[source] = {}
            for destination in self.Programs[source]:
                G[source][destination] = 1
        return G

    def depthFirstSearch(self, start, graph, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        for next in set(graph[start]) - visited:
            self.depthFirstSearch(next, graph, visited)
        return list(visited)

    def countGroups(self):
        groups = []
        for source in self.Programs:
            group = sorted(self.depthFirstSearch(source, system.Graph))
            if not group in groups:
                groups.append(group)
        return len(groups)


with open("./input.txt") as f:
    INPUT = f.readlines()

system = PipeSystem(INPUT)
print("Star 1: %s" % len(system.depthFirstSearch(0, system.Graph)))
print("Star 2: %s" % system.countGroups())

