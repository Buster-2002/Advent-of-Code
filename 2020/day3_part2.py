#!/usr/bin/env python3
"""
Author: Buster
Link: https://adventofcode.com/2020/day/3#part2
Question: What do you get if you multiply together the number of trees encountered on each of the listed slopes?
Answer: 3584591857
"""
from typing import Sequence, Generator, Any


INPUT = open('day3_input.txt', encoding='utf-8').read()
GRID = [(list(line) * 73) for line in INPUT.splitlines()]
COMBOS = (1, 1), (3, 1), (5, 1), (7, 1), (1, 2)

def enumerate2(iterator: Sequence, start: int, step: int) -> Generator[int, Any]:
    for item in iterator:
        yield (start, item)
        start += step

def main() -> int:
    product = 1
    for r, d in COMBOS:
        hit = 0
        for i, line in enumerate2(GRID[0::d], 0, r):
            if line[i] == '#':
                hit += 1

        product = hit * product
    
    return product

if __name__ == '__main__':
    result = main()
    print(f'Answer day 3, part 2: {result}')
