import re
from collections import namedtuple

DAY = 1
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
        if line != '':
            INPUT.append(line)

def part1():
    total = 0
    for line in INPUT:
        digits = [int(c) for c in line if c.isdigit()]
        total += 10*digits[0] + digits[-1]
    return total

def part2():
    digit_values = {
        'one': 1,   '1': 1,
        'two': 2,   '2': 2,
        'three': 3, '3': 3,
        'four': 4,  '4': 4,
        'five': 5,  '5': 5,
        'six': 6,   '6': 6,
        'seven': 7, '7': 7,
        'eight': 8, '8': 8,
        'nine': 9,  '9': 9
    }
    SearchResult = namedtuple('SearchResult', ['location', 'value'])

    total = 0
    for line in INPUT:
        matches = []
        for search_string in digit_values.keys():
            for match in re.finditer(search_string, line):
                matches.append(SearchResult(match.start(), digit_values[search_string]))
        
        matches.sort()
        total += 10*matches[0].value + matches[-1].value
    return total

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()
