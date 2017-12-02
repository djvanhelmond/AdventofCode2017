#!/usr/local/bin/python3

with open("./input.txt") as f:
    INPUT = f.readlines()

star1_checksum = 0
star2_checksum = 0

for row in INPUT:
    star1_checksum += max(map(int, row.split('\t'))) - min(map(int, row.split('\t')))

for row in INPUT:
    all = sorted(list(map(int, row.split('\t'))))
    edFound = False
    while not edFound:
        for j in all[::-1]:
            for i in all:
                if  (j != i) and (j % i == 0):
                    edFound = True
                    star2_checksum += (j / i)

print star1_checksum
print star2_checksum

