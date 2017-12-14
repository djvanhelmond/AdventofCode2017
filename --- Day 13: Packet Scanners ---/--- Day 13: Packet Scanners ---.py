#!/usr/local/bin/python3

class Firewall():
    def __init__(self, recording):
        self.curPos = -1
        self.time = -1
        self.severity = 0
        self.geometry = self.__buildFirewallGeometry([ record.split(": ") for record in recording ])
        self.scannerPosition = self.__initialiseScanners()

    def __buildFirewallGeometry(self, recording):
        geometry = {}
        for layer, depth in recording:
            geometry[int(layer)] = int(depth)
        return geometry

    def __initialiseScanners(self):
        positions = {}
        for layer in self.geometry:
            positions[layer] = 0
        return positions

    def __updateScanners(self):
        for layer in self.geometry:
            if (self.time / (self.geometry[layer] - 1)) % 2 == 0:
                self.scannerPosition[layer] = self.time % (self.geometry[layer] - 1)
            else:
                self.scannerPosition[layer] = (self.geometry[layer] - 1) - (self.time % (self.geometry[layer] - 1))

    def __calcCaught(self):
        if self.curPos in self.scannerPosition:
            if self.scannerPosition[self.curPos] == 0:
                return self.curPos * self.geometry[self.curPos]
            else:
                return 0
        else:
            return 0


    def visOut(self):
        time.sleep(0.2)
        print("---------------------------\n")
        if self.time == -1:
            m = "Initial State:\n"
        else:
            m = "Picosecond " + str(self.time) + ": " + str(self.severity) +"\n"
        layers = max(self.geometry) + 1
        depth = self.geometry[max(self.geometry, key=self.geometry.get)]
        for l in range(layers):
            if l < 10:
                m += " " + str(l) + "  "
            else:
                m += str(l) + "  "
        m += "\n"
        for d in range(depth):
            for l in range(layers):
                if (l in self.geometry) and d < self.geometry[l]:
                    if self.scannerPosition[l] == d:
                        if self.curPos == l and d == 0:
                            m += "(S) "
                        else:
                            m += "[S] "
                    else:
                        if self.curPos == l and d == 0:
                            m += "( ) "
                        else:
                            m += "[ ] "
                else:
                    if d == 0:
                        if self.curPos == l and d == 0:
                            m += "(.) "
                        else:
                            m += "... "
                    else:
                        m += "    "
            m += "\n"
        m += "\n"
        print(m)

    def tick(self):
        self.time += 1
        self.curPos += 1
        self.__updateScanners()
        self.severity += self.__calcCaught()






with open("./input.txt") as f:
    INPUT = f.readlines()

scanner = Firewall(INPUT)
for i in range(max(scanner.geometry) + 1):
    scanner.tick()
print("Star 1: %s" % scanner.severity)


Found = False
delay = 8
print("Star 2 might take up to 3 minutes")
while not Found:
    delay += 6
    scanner = Firewall(INPUT)
    scanner.time += delay
    for i in range(max(scanner.geometry) + 1):
        if scanner.severity == 0:
            scanner.tick()
        else:
            continue
    Found = (scanner.severity == 0)

print("Star 2: %i" % delay)
