#!/usr/bin/env python3
"""
Day 2: Rock Paper Scissors
see https://adventofcode.com/2022/day/2
"""
from utils import *

play = {'A': 'rock', 'B': 'paper', 'C': 'scissors', 'X': 'rock', 'Y': 'paper', 'Z': 'scissors'}
outcomes = {'X': 'lose', 'Y': 'draw', 'Z': 'win'}

win = {'rock': 'paper', 'paper': 'scissors', 'scissors': 'rock'}
lose = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

value = {'rock': 1, 'paper': 2, 'scissors': 3}

def as_plays(line):
    a, b = line.split()
    return (play[a], play[b])

def as_outcomes(line):
    a, b = line.split()
    return (play[a], outcomes[b])

def score(round):
    you, me = round
    if me == you:
        return 3 + value[me]
    elif me == lose[you]:
        return 0 + value[me]
    elif me == win[you]:
        return 6 + value[me]

def choose(round):
    you, outcome = round
    if outcome == 'draw':
        return (you, you)
    elif outcome == 'lose':
        return (you, lose[you])
    elif outcome == 'win':
        return (you, win[you])

example = read_input("inputs/example02.txt", as_plays)
ex1 = sum([score(round) for round in example])
assert ex1 == 15

example2 = read_input("inputs/example02.txt", as_outcomes)
ex2 = sum([score(round) for round in mapl(choose, example2)])
assert ex2 == 12

plays = read_input("inputs/input02.txt", as_plays)
p1 = sum([score(round) for round in plays])
print("part 1:", p1)
assert p1 == 11386

outcomes = read_input("inputs/input02.txt", as_outcomes)
p2 = sum([score(round) for round in mapl(choose, outcomes)])
print("part 2:", p2)
assert p2 == 13600
