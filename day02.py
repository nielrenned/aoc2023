from collections import namedtuple

DAY = 2
RAW_INPUT = None
INPUT = None

Game = namedtuple('Game', ['id', 'draws'])
Draw = namedtuple('Draw', ['r', 'g', 'b'])

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

        descriptor, draw_str = line.split(': ')
        game_id = int(descriptor.split(' ')[1])
        game = Game(game_id, [])

        draw_strs = draw_str.split('; ')
        for draw in draw_strs:
            cube_counts = draw.split(', ')
            r, g, b = 0, 0, 0
            for cube_count in cube_counts:
                num, color = cube_count.split(' ')
                num = int(num)
                if color == 'red': r = num
                elif color == 'green': g = num
                elif color == 'blue': b = num
            game.draws.append(Draw(r, g, b))
        INPUT.append(game)

def part1():
    r_limit = 12
    g_limit = 13
    b_limit = 14

    id_total = 0
    for game in INPUT:
        for draw in game.draws:
            if not (draw.r <= r_limit and draw.g <= g_limit and draw.b <= b_limit):
                break
        else:
            id_total += game.id
    return id_total

def part2():
    power_total = 0
    for game in INPUT:
        r_min = max(draw.r for draw in game.draws)
        g_min = max(draw.g for draw in game.draws)
        b_min = max(draw.b for draw in game.draws)
        power_total += r_min * g_min * b_min
    return power_total

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()
