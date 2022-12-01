import re
# from itertools import permutations, combinations, chain, cycle, product, islice
from textwrap import dedent

def noop(x):
    return x

def mapl(f, iterable):
    return list(map(f, iterable))

def mapt(f, iterable):
    return tuple(map(f, iterable))

def filterl(f, iterable):
    return list(filter(f, iterable))

def transpose(rows):
    """Pivot rows into columns"""
    return list(zip(*rows))

def read_example(multiline, parser=str):
    """Split a multi-line string example, and parse each line into a record"""
    lines = dedent(multiline).splitlines()
    return list(map(parser, lines))

def read_input(filename, parser=str):
    """Read an input file, and parse each line into a record"""
    f = open(filename).read().splitlines()
    return [parser(line) for line in f]

def read_paragraphs(filename, parser=str):
    """Read a paragraph file --> [[11, 12], [21, 22], ...]"""
    records = open(filename).read().split("\n\n")
    return [[parser(l) for l in r.splitlines()] for r in records]

def grep(pattern, lines):
    for line in lines:
        if re.search(pattern, line):
            print(line)
