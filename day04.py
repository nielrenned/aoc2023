from collections import namedtuple

DAY = 4
RAW_INPUT = None
INPUT = None

def load_input(use_test_input=False):
    global RAW_INPUT
    path = f'inputs/day{DAY:02}.txt'
    if use_test_input:
        path = f'inputs/day{DAY:02}_test.txt'
    with open(path) as f:
        RAW_INPUT = f.read()

Card = namedtuple('Card', ['id', 'winning_numbers', 'numbers_found'])

def parse_input():
    global INPUT
    INPUT = []
    for line in RAW_INPUT.split('\n'):
        if line == '': continue
        card_desc, numbers = line.split(': ')
        card_id = int(card_desc.split()[1])

        winning_list, found_list = numbers.split(' | ')
        winning_numbers = set(map(int, winning_list.split()))
        numbers_found = set(map(int, found_list.split()))

        INPUT.append(Card(card_id, winning_numbers, numbers_found))

def part1():
    total = 0
    for card in INPUT:
        num_matches = len(card.winning_numbers & card.numbers_found)
        if num_matches > 0:
            total += 2**(num_matches-1)
    return total

def part2():
    match_counts = {
        card.id: len(card.winning_numbers & card.numbers_found) for card in INPUT
    }
    
    card_counts = [0] + [1 for _ in INPUT] # cards are 1-indexed
    for card_id in range(1, len(card_counts)):
        for i in range(1, match_counts[card_id] + 1):
            card_counts[card_id + i] += card_counts[card_id]
    
    return sum(card_counts)


def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()
