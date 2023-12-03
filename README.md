# Advent of Code 2023

My solutions to and thoughts about the problems of [AoC2023](https://adventofcode.com/2023).

WARNING: There *will* be spoilers below. Watch out!

I'm going to document this here to make myself accountable for next year: I want to create my own programming language and use it to solve AoC2024.

## Code Structure

I've given each file a template that includes empty methods for Part 1 and Part 2 of each problem, along with boilerplate code to load the raw input. The input for each problem is stored as the global `INPUT`.

In a lot of problems, code can be shared between Parts 1 and 2, but there's no way to know that ahead of time. So I'll probably end up with some copypasta. I'm okay with that for two reasons: firstly, this is just for fun, and secondly, I would like Parts 1 and 2 to be able to run independently.

## Thoughts

- [Day 1](#day-1)
- [Day 2](#day-2)
- [Day 3](#day-3)

### Day 1

[Problem Page](https://adventofcode.com/2023/day/1)

Part 1 was very straightforward: Add all the digits you find to a list, then use the first and last index of the list to create the value for each line. Even if the line contains only one digit, this strategy works.

Part 2, however, was quite sneaky! I thought I had a clean solution using the regular expression `\d|one|two|...|nine` and then doing the same as part one. However, this fails in a couple specific cases. For example, consider a line that looks like `1kljtwone`. Using the regex from above, this line is valued at `12`, which is wrong. It should be `11`. This happens because `one` and `two` overlap. Instead, what we need to do is find all locations for *each* digit string, then sort the matches by their starting location. So we would have a match for `two` at index `4` and a match for `one` at index `6`. My solution uses a `namedtuple` for code readability and for quick sorting.

This was a nice little twist, as usually Day 1 is nearly trivial.

### Day 2

[Problem Page](https://adventofcode.com/2023/day/2)

This problem was more of an exercise in parsing, rather than an exercise in problem solving. I did get to use a couple nice Python constructs though. In Part 1, I took advantage of Python's [`for-else` statement](https://book.pythontips.com/en/latest/for_-_else.html) to add the game's `id` to the total only if we *didn't* break out of the loop. In Part 2, I used [list comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions), a Python classic, to make determining the minimum number of cubes short-and-sweet.

### Day 3

[Problem Page](https://adventofcode.com/2023/day/3)

This one took me a few iterations to get right. I got stuck for quite a while on an off-by-one error when searching the file for numbers. There's probably a better way to do it. But once the parsing was figured out, solving the actual problem was relatively quick. I think the "trick" is to avoid counting numbers more than once, but we can use Python's `set` to make sure we don't count duplicates. Also, there were some pretty clean comprehensions that made the code short. Python is crazy.