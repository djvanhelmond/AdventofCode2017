#!/usr/local/bin/python3

import math


class Particle():
    def __init__(self, position, velocity, acceleration):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.absA = self.__absoluteAccelleration()

    def __absoluteAccelleration(self):
        return math.sqrt(sum([ math.pow(val, 2) for val in self.acceleration ]))

    def update(self):
        for i in range(3):
            self.velocity[i] += self.acceleration[i]
            self.position[i] += self.velocity[i]

class Gpu():
    def __init__(self, particleList):
        self.particles = {}
        for key in range(len(particleList)):
            self.particles[key] = self.__loadParticles(particleList[key])

    def __loadParticles(self, particleData):
        p, v, a = particleData.split(", ")
        _, px, py, pz, _ = p.replace("<", ",").replace(">", ",").split(",")
        _, vx, vy, vz, _ = v.replace("<", ",").replace(">", ",").split(",")
        _, ax, ay, az, _ = a.replace("<", ",").replace(">", ",").split(",")
        return Particle([int(px),int(py),int(pz)], [int(vx),int(vy),int(vz)], [int(ax),int(ay),int(az)])

    def slowestParticle(self):
        slowest = 0
        for key in self.particles:
            if self.particles[key].absA < self.particles[slowest].absA:
                slowest = key
        return slowest

    def __removeCollisions(self):
        allPositions = [ self.particles[key].position for key in self.particles ]
        collisions = [x for n, x in enumerate(allPositions) if x in allPositions[:n]]
        delkeys = [ key for key in self.particles if self.particles[key].position in collisions ]
        for key in delkeys:
            del self.particles[key]

    def tick(self):
        for key in self.particles:
            self.particles[key].update()
        self.__removeCollisions()


with open("./input.txt") as f: INPUT = f.readlines()
canvas = Gpu(INPUT)
print("Star 1: %i" % canvas.slowestParticle())

for i in range(100):
    canvas.tick()
print("Star 2: %i" % len(canvas.particles))
