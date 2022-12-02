#!/usr/bin/env python3
"""
Day 1: Calorie Counting
see https://adventofcode.com/2022/day/1
"""
from utils import *

def subtotals(records):
    return mapl(sum, records)

def top_three(l):
    return sorted(l, reverse=True)[:3]

example = read_paragraphs("inputs/example01.txt", int)
input = read_paragraphs("inputs/input01.txt", int)

ex1 = max(subtotals(example))
assert ex1 == 24000

ex2 = sum(top_three(subtotals(example)))
assert ex2 == 45000

most1 = max(subtotals(input))
print("part 1:", most1)
assert most1 == 70613

most2 = sum(top_three(subtotals(input)))
print("part 2:", most2)
assert most2 == 205805
