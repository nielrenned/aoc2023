import re
import operator
from collections.abc import Iterable
from functools import reduce

DAY = 8
RAW_INPUT = None
INPUT = None

def load_input(use_test_input=False):
    global RAW_INPUT
    path = f'inputs/day{DAY:02}.txt'
    if use_test_input:
        path = f'inputs/day{DAY:02}_test.txt'
    with open(path) as f:
        RAW_INPUT = f.read()

def parse_input():
    global INPUT
    instrs = tuple(0 if c == 'L' else 1 for c in RAW_INPUT.split('\n')[0])
    regex = re.compile(r'(\w{3}) = \((\w{3}), (\w{3})\)')
    nodes = {}
    for line in RAW_INPUT.split('\n')[2:]:
        if line == '': continue
        match = regex.match(line)
        start, left, right = match.groups()
        nodes[start] = (left, right)
    INPUT = (instrs, nodes)

def gcd(a: int | Iterable[int], b: int = None):
    if b is not None:
        while b != 0:
            a, b = b, a%b
        return a
    else:
        return reduce(gcd, a)

def lcm(a: int | Iterable[int], b: int = None):
    if b is not None:
        return a*b // gcd(a, b)
    elif len(a) == 2:
        return lcm(a[0], a[1])
    else:
        return lcm(a[0], lcm(a[1:]))

def part1():
    instrs, nodes = INPUT

    current = 'AAA'
    count = 0
    while current != 'ZZZ':
        for instr in instrs:
            current = nodes[current][instr]
            count += 1
            if current == 'ZZZ': break
    
    return count

def part2():
    instrs, nodes = INPUT

    starting_nodes = [node for node in nodes if node[-1] == 'A']
    lengths = []
    for starting_node in starting_nodes:
        current = starting_node
        count = 0
        while current[-1] != 'Z':
            for instr in instrs:
                current = nodes[current][instr]
                count += 1
                if current[-1] == 'Z': break
        lengths.append(count)

    return lcm(lengths)

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()
