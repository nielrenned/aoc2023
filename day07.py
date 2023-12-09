from collections import namedtuple, Counter
from functools import cmp_to_key

DAY = 7
RAW_INPUT = None
INPUT = None

def load_input(use_test_input=False):
    global RAW_INPUT
    path = f'inputs/day{DAY:02}.txt'
    if use_test_input:
        path = f'inputs/day{DAY:02}_test.txt'
    with open(path) as f:
        RAW_INPUT = f.read()

Hand = namedtuple('Hand', ['cards', 'bid'])

def parse_input():
    global INPUT
    INPUT = []
    for line in RAW_INPUT.split('\n'):
        if line == '': continue
        cards, bid_str = line.split()
        INPUT.append(Hand(cards, int(bid_str)))

def hand_type(cards):
    counter = Counter(cards)
    uniques = counter.keys()
    values = counter.values()

    if len(uniques) == 1:   return 6 # Five of a kind
    elif len(uniques) == 2:
        if 4 in values:     return 5 # Four of a kind
        else:               return 4 # Full house
    elif len(uniques) == 3:
        if 3 in values:     return 3 # Three of a kind
        else:               return 2 # Two pair
    elif len(uniques) == 4: return 1 # One pair
    else:                   return 0 # High card

def part1():
    CARD_VALUES = {
        **{str(i): i for i in range(2, 10)},
        'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14
    }

    def hand_value(hand):
        card_values = tuple(CARD_VALUES[card] for card in hand.cards)
        return (hand_type(hand.cards),) + card_values

    sorted_hands = sorted(INPUT, key=hand_value)
    return sum((i+1)*hand.bid for i, hand in enumerate(sorted_hands))

def part2():
    CARD_VALUES = {
        'J': 1,
        **{str(i): i for i in range(2, 10)},
        'T': 10, 'Q': 12, 'K': 13, 'A': 14
    }

    def hand_value(hand):
        type = 0
        for new_card in CARD_VALUES.keys():
            type = max(type, hand_type(hand.cards.replace('J', new_card)))
        card_values = tuple(CARD_VALUES[card] for card in hand.cards)
        return (type,) + card_values
    
    sorted_hands = sorted(INPUT, key=hand_value)
    return sum((i+1)*hand.bid for i, hand in enumerate(sorted_hands))

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()
