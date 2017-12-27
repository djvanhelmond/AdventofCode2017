#!/usr/local/bin/python3

class Cpu():
    def __init__(self, components):
        self.components = [ tuple([int(x) for x in component.strip().split("/")]) for component in components ]
        self.validBridges = self.__generateValidBridges(0, self.components)

    def __generateValidBridges(self, port, components, bridge=None):
        if not bridge:
            bridge = []
        validBridges = []
        matchingComponents = [ x for x in components if (x[0] == port or x[1] == port) ]
        if len(matchingComponents) != 0:
            for component in matchingComponents:
                newbridge = bridge + [tuple(component)]
                validBridges.append(newbridge)
                if component[0] != port:
                    newport = component[0]
                else:
                    newport = component[1]
                remainingComponents = [ m for m in components if m not in [component] ]
                validBridges += self.__generateValidBridges(newport, remainingComponents, newbridge)
        return validBridges

    def __calcStrength(self, bridge):
        return sum([item for sublist in bridge for item in sublist])

    def findStrongest(self, bridges):
        return max([ self.__calcStrength(bridge) for bridge in bridges ])

    def findLongest(self):
        longest = [self.validBridges[0]]
        for bridge in self.validBridges:
            if len(bridge) > len(longest[0]):
                longest = [bridge]
            elif len(bridge) == len(longest[0]):
                longest.append(bridge)
        return longest



with open("./input.txt") as f: INPUT = f.readlines()

bridge = Cpu(INPUT)
print("Star 1: %i" % bridge.findStrongest(bridge.validBridges))
print("Star 2: %i" % bridge.findStrongest(bridge.findLongest()))











#print("Star 2: %i" % tubes.steps)

