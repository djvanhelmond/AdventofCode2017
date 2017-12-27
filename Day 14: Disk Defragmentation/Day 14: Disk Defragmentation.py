#!/usr/local/bin/python3

class KnotHash():
    def __init__(self, lengthSeq):
        self.string = [ x for x in range(256)]
        self.currentPos = 0
        self.skipSize = 0
        self.hash(lengthSeq)

    def hash(self, lengthSeq):
        for _ in range(64):
            for length in [ (ord(x)) for x in lengthSeq ]  + [17, 31, 73, 47, 23]:
                self.__reverseOrder(length)
                self.currentPos = (self.currentPos + length + self.skipSize) % len(self.string)
                self.skipSize += 1

    def __reverseOrder(self, length):
        self.string = self.string[-(len(self.string) - self.currentPos):] + self.string[:-(len(self.string) - self.currentPos)]
        newstring = []
        for i in range(len(self.string)):
            if i < length:
                newstring.append(self.string[length - i - 1])
            else:
                newstring.append(self.string[i])
        self.string = newstring[-self.currentPos:] + newstring[:-self.currentPos]

    def denseHash(self):
        hash = ""
        for i in range(16):
            dense = 0
            for m in range(16):
                dense ^= self.string[16 * i + m]
            hash += "{:02x}".format(dense)
        return hash



class Disk():
    def __init__(self, keyString):
        self.width = 128
        self.height = 128
        self.diskLayout = self.__generateLayout(keyString)
        self.Graph = self.__build_graph()

    def __generateLayout(self, keyString):
        layout = {}
        for i in range(self.height):
            knot = KnotHash(keyString + "-" + str(i))
            hash = knot.denseHash()
            layout[i] = ""
            for hexChar in hash:
                layout[i] += bin(int(hexChar, 16))[2:].zfill(4)
        return layout

    def __build_graph(self):
        G = {}
        for i in range(self.height):
            for j in range(self.width):
                if self.diskLayout[i][j] == "1":
                    G[str(i)+","+str(j)] = {}
                    if (i-1 >= 0):
                        if self.diskLayout[i-1][j] == "1":
                            G[str(i)+","+str(j)][str(i - 1)+","+str(j)] = 1
                    if (i+1 < self.height):
                        if self.diskLayout[i+1][j] == "1":
                            G[str(i)+","+str(j)][str(i + 1) + "," + str(j)] = 1
                    if (j-1 >= 0):
                        if self.diskLayout[i][j-1] == "1":
                            G[str(i)+","+str(j)][str(i) + "," + str(j - 1)] = 1
                    if (j+1 < self.width):
                        if self.diskLayout[i][j+1] == "1":
                            G[str(i)+","+str(j)][str(i) + "," + str(j + 1)] = 1
        return G

    def __depthFirstSearch(self, start, graph, visited=None):
        if not visited:
            visited = set()
        visited.add(start)
        for next in set(graph[start]) - visited:
            self.__depthFirstSearch(next, graph, visited)
        return list(visited)

    def calcUsedSquares(self):
        return (sum( [ self.diskLayout[x].count("1") for x in range(self.height) ] ))

    def countRegions(self):
        count = 0
        allSquares = list(self.Graph)
        while len(allSquares) != 0:
            count += 1
            group = self.__depthFirstSearch(allSquares[0], self.Graph)
            allSquares = [ program for program in allSquares if program not in group ]
        return count




INPUT = "jxqlasbh"

disk = Disk(INPUT)
print("Star 1: %i" % disk.calcUsedSquares())
print("Star 2: %i" % disk.countRegions())




