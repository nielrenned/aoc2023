import math
import copy
from itertools import product

DAY = 10
RAW_INPUT = None
INPUT = None

def load_input(use_test_input=False):
    global RAW_INPUT
    path = f'inputs/day{DAY:02}.txt'
    if use_test_input:
        path = f'inputs/day{DAY:02}_test.txt'
    with open(path) as f:
        RAW_INPUT = f.read()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __neg__(self):
        return Point(-self.x, -self.y)
    
    def __iter__(self):
        return iter((self.x, self.y))
    
    def __hash__(self):
        return hash((self.x, self.y))
    
    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)
    
    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return f'({self.x}, {self.y})'

NORTH = Point(0, -1)
SOUTH = Point(0, 1)
WEST  = Point(-1, 0)
EAST  = Point(1, 0)

DIRECTIONS = {NORTH, SOUTH, EAST, WEST}

PIPE_CONNECTIONS = {
    '|': {NORTH, SOUTH},
    '-': {EAST, WEST},
    'L': {NORTH, EAST},
    'J': {NORTH, WEST},
    '7': {SOUTH, WEST},
    'F': {SOUTH, EAST}
}

def parse_input():
    global INPUT
    pipe_map = []
    starting_location = None
    for y, line in enumerate(RAW_INPUT.split('\n')):
        if line == '': continue
        if (x := line.find('S')) != -1:
            starting_location = Point(x, y)
        pipe_map.append(list(line))
    INPUT = (starting_location, pipe_map)

def is_connected(pipe, dir):
    if pipe not in PIPE_CONNECTIONS:
        return False
    return (dir in PIPE_CONNECTIONS[pipe])

def pipe_at(pipe_map, pos):
    x, y = pos
    if 0 <= x < len(pipe_map[0]) and 0 <= y < len(pipe_map):
        return pipe_map[y][x]
    return '#'  # Need some way to indicate we reached the edge

def get_flow_direction(pipe, from_dir):
    connections = PIPE_CONNECTIONS[pipe]
    return (connections - {from_dir}).pop()

STARTING_PIPE = None
LOOP_TILES = set()

def part1():
    global LOOP_TILES, STARTING_PIPE
    start, pipe_map = INPUT
    LOOP_TILES.add(start)
    
    # Determine connections to starting point
    connected_directions = set()
    for dir in DIRECTIONS:
        if is_connected(pipe_at(pipe_map, start + dir), -dir):
            connected_directions.add(dir)
    
    for pipe, connections in PIPE_CONNECTIONS.items():
        if connections == connected_directions:
            STARTING_PIPE = pipe
            break

    # Trace the path
    flow_direction = connected_directions.pop()
    pos = start + flow_direction
    steps = 1
    while (pipe := pipe_at(pipe_map, pos)) != 'S':
        LOOP_TILES.add(pos)
        flow_direction = get_flow_direction(pipe, -flow_direction)
        pos += flow_direction
        steps += 1
    
    return math.ceil(steps / 2)


def part2():
    start, pipe_map_orig = INPUT
    pipe_map = copy.deepcopy(pipe_map_orig)
    pipe_map[start.y][start.x] = STARTING_PIPE

    inside_count = 0
    for x, y in product(range(len(pipe_map[0])), range(len(pipe_map))):
        pos = Point(x, y)
        if pos in LOOP_TILES: continue

        num_crossings = 0
        while pipe_at(pipe_map, pos) != '#':
            pos += NORTH
            if pos not in LOOP_TILES: continue # Keep taking steps until we hit the main loop
            
            first_pipe = pipe_at(pipe_map, pos) # This pipe must be on the main loop

            # Since we're stepping north, '-' will always count as crossing the main loop
            if first_pipe == '-':
                num_crossings += 1
                continue
            
            # At this point, we must've hit a corner pipe that isn't connected to the south,
            # i.e. either an 'L' or a 'J' bend. From here, we keep taking steps north until
            # we leave the main loop
            assert(first_pipe == 'L' or first_pipe == 'J')
            while is_connected(pipe_at(pipe_map, pos), NORTH):
                pos += NORTH
            
            # The line we just followed north looks like
            #
            #    F        7      /                     7        F  \
            #    |   or   |      | with mirror images  |   or   |  |
            #    L        L      \                     J        J  /
            #
            # In the first case, we didn't  cross the main loop, we kind of skirted along it.
            # In the second case , we *did* cross the main loop, so we need to count that crossing.
            if ((first_pipe == 'L' and pipe_at(pipe_map, pos) == '7') or
                (first_pipe == 'J' and pipe_at(pipe_map, pos) == 'F')):
                num_crossings += 1
        
        # Every time we cross the loop, we change which side we're on. Since we know we end up on
        # the outside, crossing the loop an odd number of times means we started on the inside.
        if num_crossings % 2 == 1:
            inside_count += 1

    return inside_count


def main():
    load_input()
    parse_input()
    print('PART 1:', part1())
    print('PART 2:', part2())

if __name__ == "__main__":
    main()
