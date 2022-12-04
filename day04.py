#!/usr/bin/env python3
"""
Day 4: Camp Cleanup
see https://adventofcode.com/2022/day/4
"""
from utils import *
from more_itertools import collapse

def parse(line):
    points = [pair.split('-') for pair in line.split(',')]
    return mapt(int, collapse(points))

def fully_overlap(points):
    a1, a2, b1, b2 = points
    return (a1 <= b1 and a2 >= b2) or (b1 <= a1 and b2 >= a2)

def overlap(points):
    a1, a2, b1, b2 = points
    return (a1 <= b1 and a2 >= b1) or (b1 <= a1 and b2 >= a1)

def part1(lines):
    points = [parse(l) for l in lines]
    overlapping = filterl(fully_overlap, points)
    return len(overlapping)

def part2(lines):
    points = [parse(l) for l in lines]
    overlapping = filterl(overlap, points)
    return len(overlapping)

example = read_input("./inputs/example04.txt")
input = read_input("inputs/input04.txt")

ex1 = part1(example)
assert ex1 == 2
ex2 = part2(example)
assert ex2 == 4

p1 = part1(input)
print("part 1:", p1)
assert p1 == 456

p2 = part2(input)
print("part 2:", p2)
assert p2 == 808
