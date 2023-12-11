from itertools import combinations

DAY = 11
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

    star_map = list(filter(lambda s: len(s) > 0, RAW_INPUT.split('\n')))

    galaxies = []
    empty_rows = set(range(len(star_map)))
    empty_cols = set(range(len(star_map[0])))
    for y, line in enumerate(star_map):
        for x, c in enumerate(line):
            if c == '#':
                galaxies.append((x, y))
                empty_cols.discard(x)
                empty_rows.discard(y)
    
    INPUT = (galaxies, empty_rows, empty_cols)

def part1():
    galaxies, empty_rows, empty_cols = INPUT
    
    total = 0
    for (x1, y1), (x2, y2) in combinations(galaxies, 2):
        min_x, max_x, min_y, max_y = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)

        x_length = max_x - min_x + sum(1 for c in empty_cols if min_x <= c <= max_x)
        y_length = max_y - min_y + sum(1 for r in empty_rows if min_y <= r <= max_y)

        total += x_length + y_length
    return total

def part2():
    galaxies, empty_rows, empty_cols = INPUT
    
    total = 0
    for (x1, y1), (x2, y2) in combinations(galaxies, 2):
        min_x, max_x, min_y, max_y = min(x1, x2), max(x1, x2), min(y1, y2), max(y1, y2)

        x_length = max_x - min_x + sum(1_000_000 - 1 for c in empty_cols if min_x <= c <= max_x)
        y_length = max_y - min_y + sum(1_000_000 - 1 for r in empty_rows if min_y <= r <= max_y)

        total += x_length + y_length
    return total

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()
