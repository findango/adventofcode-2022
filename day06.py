#!/usr/bin/env python3
"""
Day 6: Tuning Trouble
see https://adventofcode.com/2022/day/6
"""
from utils import *
from more_itertools import all_unique, sliding_window

def part1(input):
    return mapl(all_unique, sliding_window(input, 4)).index(True) + 4

def part2(input):
    return mapl(all_unique, sliding_window(input, 14)).index(True) + 14

assert part1('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 7
assert part2('mjqjpqmgbljsphdztnvjfqwrcgsmlb') == 19

assert part1('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 11
assert part2('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw') == 26

input = read_input('inputs/input06.txt')[0]

p1 = part1(input)
print('part1:', p1)
assert p1 == 1155

p2 = part2(input)
print('part2:', p2)
assert p2 == 2789
