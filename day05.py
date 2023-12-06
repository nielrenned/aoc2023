import re
from collections import namedtuple

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

        input_type = output_type
        input_nums = output_nums
    
    return min(output_nums)

class ClosedIntInterval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return f'[{self.start}..{self.end}]'

    def __str__(self):
        return self.__repr__()
    
    def __and__(self, other):
        if not isinstance(other, ClosedIntInterval):
            raise ValueError
        
        a, b = self.start, self.end
        c, d = other.start, other.end

        # Calculate [a, b] \cap [c, d]
        if b < c or d < a:
            return None
        return ClosedIntInterval(max(a, c), min(b, d))
    
    def __add__(self, other):
        if isinstance(other, int):
            return ClosedIntInterval(self.start + other, self.end + other)
        
        raise TypeError(f'Cannot add {self.__class__.__name__} and {other.__class__.__name__}')
    
    def __sub__(self, other):
        if isinstance(other, int):
            return ClosedIntInterval(self.start - other, self.end - other)
        
        if isinstance(other, ClosedIntInterval):
            a, b = self.start, self.end
            c, d = other.start, other.end

            # Calculate [a, b] - [c, d]
            if b < c or d < a: # If [a, b] \cap [c, d] = \emptyset
                return [self]
            
            remaining = []
            if d < b: remaining.append(ClosedIntInterval(d+1, b))
            if a < c: remaining.append(ClosedIntInterval(a, c-1))
            return remaining
        
        raise TypeError(f'Cannot subtract {self.__class__.__name__} and {other.__class__.__name__}')

def apply_shifts(input_intervals, shifts):
    output_intervals = []
    while len(input_intervals) != 0:
        input_interval = input_intervals.pop()

        for shift_interval, shift in shifts:
            if overlap := shift_interval & input_interval:
                output_intervals.append(overlap + shift)
                input_intervals.extend(input_interval - overlap)
                break
        else:
            # No overlap with shift intervals, so maps to self
            output_intervals.append(input_interval)
    
    return output_intervals

def part2():
    seed_nums, maps = INPUT

    intervals = []
    for i in range(0, len(seed_nums), 2):
        start, length = seed_nums[i:i+2]
        intervals.append(ClosedIntInterval(start, start+length-1))
    
    shift_maps = {}
    for input_type, (output_type, map_data) in maps.items():
        shifts = []
        for output_start, input_start, length in map_data:
            input_interval = ClosedIntInterval(input_start, input_start+length-1)
            shift = output_start - input_start
            shifts.append((input_interval, shift))
        
        shift_maps[input_type] = (output_type, shifts)
    
    current_type = 'seed'
    while current_type != 'location':
        current_type, shifts = shift_maps[current_type]
        intervals = apply_shifts(intervals, shifts)
    
    return min(interval.start for interval in intervals)

def main():
    load_input(True)
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()
