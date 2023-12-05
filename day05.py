import re

DAY = 5
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

    lines = list(filter(lambda l: l != '', RAW_INPUT.split('\n')))

    seed_nums = list(map(int, lines[0].split(': ')[1].split()))

    maps = {}
    map_input = None
    map_output = None
    map_data = []
    for line in lines[1:]:
        if match := re.match('(\w+)-to-(\w+) map:', line):
            if map_input is not None:
                maps[map_input] = (map_output, map_data)
                map_input = map_output = None
                map_data = []
            
            map_input = match[1]
            map_output = match[2]
        else:
            map_data.append(tuple(map(int, line.split())))
    
    maps[map_input] = (map_output, map_data) # Don't forget the last one!

    INPUT = (seed_nums, maps)

def part1():
    seed_nums, maps = INPUT

    input_type = 'seed'
    input_nums = seed_nums[:]

    # debug_lines = [f'Seed {i}, ' for i in seed_nums]
    
    while input_type != 'location':
        output_type, map_data = maps[input_type]
        output_nums = []
        for input_num in input_nums:
            for output_start, input_start, length in map_data:
                delta = input_num - input_start
                if 0 <= delta < length:
                    output_nums.append(output_start + delta)
                    break
            else:
                output_nums.append(input_num)
        
        # for i in range(len(debug_lines)):
        #     debug_lines[i] += f'{output_type} {output_nums[i]}, '

        input_type = output_type
        input_nums = output_nums
    
    # for line in debug_lines:
    #     print(line)
    
    return min(output_nums)


def part2():
    pass

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    # print('PART 2:', part2())

if __name__ == "__main__":
    main()
