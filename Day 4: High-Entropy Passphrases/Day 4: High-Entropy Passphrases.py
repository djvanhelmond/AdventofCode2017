#!/usr/local/bin/python3


with open("./input.txt") as f:
    INPUT = f.readlines()

print("Star 1: %i" % [ max([ line.split().count(element) for element in line.split() ]) for line in INPUT ].count(1))



from itertools import permutations
validPasswords = 0
for line in INPUT:
    lineValid = True
    if max([ line.split().count(element) for element in line.split() ]) != 1:
        lineValid = False
    for element in line.split():
        for perms in [''.join(p) for p in permutations(element)]:
            if (perms != element and perms in line.split()):
                lineValid = False
    if lineValid:
        validPasswords += 1

print("Star 2: %i" % validPasswords)









