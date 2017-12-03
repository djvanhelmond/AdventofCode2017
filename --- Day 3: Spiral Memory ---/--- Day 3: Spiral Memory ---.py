#!/usr/local/bin/python3

import math

INPUT = 289326

brCorner = math.floor(math.sqrt(INPUT))

if brCorner*brCorner == INPUT:
    print ("Star 1: %i" % int(math.floor(brCorner/2)*2))
else:
    ring = int(math.ceil(brCorner/2))
    rest = (INPUT - (brCorner*brCorner)) % (brCorner + 1)
    print ("Star 1: %i" % int(ring + abs(ring - rest)))


### I tried to solve this in a non-memory intensive way, but have given up for 3.2.
