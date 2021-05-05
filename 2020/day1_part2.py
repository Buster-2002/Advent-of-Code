#!/usr/bin/env python3
"""
Author: Buster
Link: https://adventofcode.com/2020/day/1#part2
Question: In your expense report, what is the product of the three entries that sum to 2020?
Answer: 92643264
"""
INPUT = open('day1_input.txt', encoding='utf-8').read()
NUMBERS = list(map(int, INPUT.splitlines()))

def main() -> int:
    for num1 in NUMBERS:
        for num2 in NUMBERS:
            for num3 in NUMBERS:
                if sum((num1, num2, num3)) == 2020:
                    return num1 * num2 * num3


if __name__ == '__main__':
    result = main()
    print(f'Answer day 1, part 2: {result}')
