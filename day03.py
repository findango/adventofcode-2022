#!/usr/bin/env python3
"""
Day 3: Rucksack Reorganization
see https://adventofcode.com/2022/day/3
"""
from utils import *
from more_itertools import chunked, divide

def shared_value(lists):
    common = set.intersection(*map(set, lists))
    return common.pop()    # only ever one common value

def score(values):
    points = "0abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return sum(points.index(v) for v in values)

def two_parts(xs):
    return divide(2, xs)

def solve1(lines):
    shared = [shared_value(pair) for pair in map(two_parts, lines)]
    return score(shared)

def solve2(lines):
    shared = [shared_value(group) for group in chunked(lines, 3)]
    return score(shared)

example = read_input("./inputs/example03.txt")
assert solve1(example) == 157
assert solve2(example) == 70

input = read_input("inputs/input03.txt")

p1 = solve1(input)
print("part 1:", p1)
assert p1 == 7428

p2 = solve2(input)
print("part 2:", p2)
assert p2 == 2650
