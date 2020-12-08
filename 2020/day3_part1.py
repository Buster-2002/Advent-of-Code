#!/usr/bin/env python3
"""
Author: Buster
Link: https://adventofcode.com/2020/day/3#part1
Question: Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
Answer: 211
"""
INPUT = open('day3_input.txt', 'r', encoding='utf-8').read()
GRID = [(list(line) * 32) for line in INPUT.splitlines()]

def enumerate2(iterator, start, step):
    for item in iterator:
        yield (start, item)
        start += step

def main():
    hit = 0

    for i, line in enumerate2(GRID, 0, 3):
        if line[i] == '#':
            hit += 1

    print(f'Answer day 3, part 1: {hit}')

if __name__ == '__main__':
    main()
