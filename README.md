# Advent of Code 2023

My solutions to and thoughts about the problems of [AoC2023](https://adventofcode.com/2023).

WARNING: There *will* be spoilers below. Watch out!

I'm going to document this here to make myself accountable for next year: I want to create my own programming language and use it to solve AoC2024.

## Code Structure

I've given each file a template that includes empty methods for Part 1 and Part 2 of each problem, along with boilerplate code to load the raw input. The input for each problem is stored as the global `INPUT`.

In a lot of problems, code can be shared between Parts 1 and 2, but there's no way to know that ahead of time. So I'll probably end up with some copypasta. I'm okay with that for two reasons: firstly, this is just for fun, and secondly, I would like Parts 1 and 2 to be able to run independently.

## Thoughts

|S|M|T|W|T|F|S|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| | | | | | [1](#day-1) | [2](#day-2) |
| [3](#day-3) | [4](#day-4) | [5](#day-5) | [6](#day-6) | 7 | 8 | 9 |
| 10 | 11 | 12 | 13 | 14 | 15 | 16 |
| 17 | 18 | 19 | 20 | 21 | 22 | 23 |
| 24 | 25 | | | | | | 

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

### Day 4

[Problem Page](https://adventofcode.com/2023/day/4)

Today felt like one of the easiest days so far. Using `set`s made Part 1 very simple, as we can simply get the length of the intersection. I expected Part 2 to have some sort of combinatorial explosion, but I think you can do it in a pretty naive way and still get the right answer. Not much else to say about Day 4.

### Day 5

[Problem Page](https://adventofcode.com/2023/day/5)

Part 1 was relatively straightforward. We just need to trace the seed numbers through their paths. Part 2, however, required a little more cleverness. You can still, in theory, use the exact same method as Part 1. However, the numbers involved are pretty big, so this takes wayyy too long to calculate. However, we can note that the maps are essentially integer intervals being shifted around. Consider the first example:

```
seed-to-soil map:
50 98 2
52 50 48
```

This tells us that the interval $[98, 99]$ maps to $[50, 51]$, the interval $[50, 97]$ maps to $[52, 99]$, and every other interval maps to itself. Put another way: If $s\in[98,99]$, return $s - 48$; if $s\in[50,51]$, return $s + 2$; otherwise return $s$. We can take advantage of this to map entire intervals! (All intervals here are integer intervals). Suppose we're trying to map the interval $[45, 60]$ using the above map. Then we really have two pieces: $[45, 49]$ and $[50, 60]$. The former maps to itself, and the latter needs to be shifted up $2$, which gives the new set of intervals: $\{[45, 49], [52, 62] \}$. Instead of $15$ operations, we only did $4$. These savings get even more significant with the size of the intervals in the real data. Then we simply repeat the process for the next map with each of the new intervals until we're done.

These interval calculations could have been done somewhat manually, but I decided to implement a class called `ClosedIntInterval` to make things a little easier. It implements addition of integers, subtraction of integers and other intervals, and intersection of intervals. That's all that's needed to perform the algorithm above! Some sort of interval-based math is an Advent of Code classic.

### Day 6

[Problem Page](https://adventofcode.com/2023/day/6)

Woah, a math problem! I think the idea here was to make you think you could do this just by iterating through the options and checking each one, and then pull the rug out from under you in Part 2. But since I'm math-oriented already, I went that direction first and got rewarded. 

Consider the first example where $\text{time} = 7$ and $\text{distance} = 9$. Let $k$ be the number of milliseconds we hold down the button. Then the speed of the the boat is $k$ mm/ms and the remaining time is $7-k$ ms, so the distance the boat travels is $k(7-k)$ mm. So we want to know for what integer values of $k$ is $k(7-k)$ greater than $9$, i.e., we're solving the inequality $7k - k^2 > 9 \Leftrightarrow k^2 - 7k + 9 < 0$. The equation on the left-hand side can be visualized as a parabola opening upward. So if we solve $k^2 - 7k + 9 = 0$, this will give two values of $k$ (not necessarily integers) and then our answer will be all integer values *between* those, as that's the bit at the bottom of the parabola which will be under the $x$-axis (or really the $k$-axis in our case). Applying the quadratic formula, our two answers are approximately $1.697$ and $5.302$, which means choosing any $k\in\{2,3,4,5\}$ will ensure we beat the record. 

We can apply this process generally and it quickly gives the answers in both parts. Nice! :)