DAY = 9
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
        INPUT.append(list(map(int, line.split())))

def predict_next(seq):
    if all(seq[0] == seq[i] for i in range(1, len(seq))):
        return seq[0]
    
    differences = [seq[i] - seq[i-1] for i in range(1, len(seq))]
    next_diff = predict_next(differences)
    return seq[-1] + next_diff

def part1():
    return sum(predict_next(seq) for seq in INPUT)

def part2():
    return sum(predict_next(seq[::-1]) for seq in INPUT)

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()
