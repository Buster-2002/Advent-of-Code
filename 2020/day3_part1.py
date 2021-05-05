#!/usr/bin/env python3
"""
Author: Buster
Link: https://adventofcode.com/2020/day/3#part1
Question: Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
Answer: 211
"""
from typing import Sequence, Generator, Any


INPUT = open('day3_input.txt', encoding='utf-8').read()
GRID = [(list(line) * 32) for line in INPUT.splitlines()]

def enumerate2(iterator: Sequence, start: int, step: int) -> Generator[int, Any]:
    for item in iterator:
        yield (start, item)
        start += step

def main() -> int:
    hit = 0
    for i, line in enumerate2(GRID, 0, 3):
        if line[i] == '#':
            hit += 1

    return hit

if __name__ == '__main__':
    result = main()
    print(f'Answer day 3, part 1: {result}')
