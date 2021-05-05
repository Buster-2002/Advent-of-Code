#!/usr/bin/env python3
"""
Author: Buster
Link: https://adventofcode.com/2020/day/1#part1
Question: Find the two entries that sum to 2020; what do you get if you multiply them together?
Answer: 1005459
"""
INPUT = open('day1_input.txt', encoding='utf-8').read()
NUMBERS = list(map(int, INPUT.splitlines()))

def main() -> int:
    for num1 in NUMBERS:
        for num2 in NUMBERS:
            if sum((num1, num2)) == 2020:
                return num1 * num2

if __name__ == '__main__':
    result = main()
    print(f'Answer day 1, part 1: {result}')
    