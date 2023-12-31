import sys
import os

template = """DAY = {day}
RAW_INPUT = None
INPUT = None

def load_input(use_test_input=False):
    global RAW_INPUT
    path = f'inputs/day{{DAY:02}}.txt'
    if use_test_input:
        path = f'inputs/day{{DAY:02}}_test.txt'
    with open(path) as f:
        RAW_INPUT = f.read()

def parse_input():
    global INPUT
    INPUT = []
    for line in RAW_INPUT.split('\\n'):
        if line == '': continue
        INPUT.append(line)

def part1():
    pass

def part2():
    pass

def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    # print('PART 2:', part2())

if __name__ == "__main__":
    main()
"""

def main():
    if len(sys.argv) != 2:
        print('Usage: python newday.py <day_num>')
        return
    
    try:
        day_num = int(sys.argv[1])
    except ValueError:
        print(f'Error: {sys.argv[1]} is not an integer.')
        return
    
    file_name = f'day{day_num:02}.py'
    if os.path.exists(file_name):
        print(f'Error: {file_name} already exists.')
        return
    
    with open(file_name, 'w') as f:
        f.write(template.format(day=day_num))

if __name__ == "__main__":
    main()