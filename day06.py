from collections import namedtuple
from math import sqrt, ceil, floor

DAY = 6
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
    INPUT = []
    for line in RAW_INPUT.split('\n'):
        if line == '': continue
        INPUT.append(list(map(int, line.split()[1:])))

def part1():
    total = 1
    times = INPUT[0]
    dists = INPUT[1]
    for t, d in zip(times, dists):
        lower = ceil((t - sqrt(t*t - 4*d))/2)
        upper = floor((t + sqrt(t*t - 4*d))/2)
        num_options = upper - lower + 1
        total *= num_options
    return total

def part2():
    t = int(''.join(map(str, INPUT[0])))
    d = int(''.join(map(str, INPUT[1])))
    lower = ceil((t - sqrt(t*t - 4*d))/2)
    upper = floor((t + sqrt(t*t - 4*d))/2)
    return upper - lower + 1

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()
