#!/usr/bin/env python3
"""
Day 5: Supply Stacks
see https://adventofcode.com/2022/day/5
"""
from utils import *
from more_itertools import split_at

def extract_numbers(s):
    # 'move 1 from 2 to 1' -> (1, 2, 1)
    return mapt(int, re.findall(r'\d+', s))

def non_empty(s):
    return len(s.strip()) > 0

def parse_stacks(lines):
    rows = [re.findall(r'.(.)..?', s) for s in lines]
    cols = [filterl(non_empty, c) for c in map(reversed, transpose(rows))]
    return cols

def parse_input(input):
    stacks, moves = split_at(input, lambda x: len(x) == 0)
    stacks = parse_stacks(stacks[:-1])    # discard the line with numbers
    moves = [extract_numbers(m) for m in moves]
    return stacks, moves

def tops_of(stacks):
    return ''.join([s[-1] for s in stacks])

def solve(input, move_multiple=False):
    stacks, moves = parse_input(input)
    for count, src, dest in moves:
        moving = stacks[src - 1][-count:]
        stacks[src - 1] = stacks[src - 1][:-count]
        stacks[dest - 1].extend(moving if move_multiple else reversed(moving))
    return tops_of(stacks)

example = read_input("inputs/example05.txt")
assert solve(example) == 'CMZ'
assert solve(example, move_multiple=True) == 'MCD'

input = read_input("inputs/input05.txt")

p1 = solve(input)
print('part1:', p1)
assert p1 == 'WCZTHTMPS'

p2 = solve(input, move_multiple=True)
print('part1:', p2)
assert p2 == 'BLSGJSDTS'
