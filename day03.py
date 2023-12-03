import re

from collections import namedtuple

DAY = 3
RAW_INPUT = None
INPUT = None

def load_input(use_test_input=False):
    global RAW_INPUT
    path = f'inputs/day{DAY:02}.txt'
    if use_test_input:
        path = f'inputs/day{DAY:02}_test.txt'
    with open(path) as f:
        RAW_INPUT = f.read()

DELTAS = [(-1,0), (1,0), (0,-1), (0,1), (1,-1), (1,1), (-1,-1), (-1,1)]

Number = namedtuple('PartNumber', ['value', 'span'])
Part = namedtuple('Part', ['symbol', 'location'])

def parse_input():
    global INPUT
    
    parts = []
    numbers = []
    for y, line in enumerate(RAW_INPUT.split('\n')):
        if line == '': continue
        
        for match in re.finditer('\d+', line):
            value = int(match.group())
            span = frozenset((x,y) for x in range(match.start(), match.end()))
            numbers.append(Number(value, span))
        
        for match in re.finditer('[^\d.]', line):
            symbol = match.group()
            location = (match.start(), y)
            parts.append(Part(symbol, location))
    
    INPUT = (parts, numbers)

def part1():
    parts, numbers = INPUT

    part_numbers = set()
    for _, (x,y) in parts:
        adjacent_locations = {(x + dx, y + dy) for dx, dy in DELTAS}
        adjacent_numbers = {number for number in numbers if len(number.span & adjacent_locations) > 0}
        part_numbers |= adjacent_numbers

    return sum(number.value for number in part_numbers)

def part2():
    parts, numbers = INPUT

    total = 0
    for symbol, (x,y) in parts:
        if symbol != '*': continue
        adjacent_locations = {(x + dx, y + dy) for dx, dy in DELTAS}
        adjacent_numbers = {number for number in numbers if len(number.span & adjacent_locations) > 0}
        if len(adjacent_numbers) == 2:
            total += adjacent_numbers.pop().value * adjacent_numbers.pop().value
    
    return total

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()
