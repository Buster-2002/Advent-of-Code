"""
Author: Buster
Link: https://adventofcode.com/2020/day/1#part1
"""
import sys

INPUT = open('day1_input.txt', 'r', encoding='utf-8').read()
NUMBERS = list(map(int, INPUT.splitlines()))

def main():
    for num1 in NUMBERS:
        for num2 in NUMBERS:
            if sum((num1, num2)) == 2020:
                print(f'Answer day 1, part 1: {num1*num2}')
                sys.exit()

if __name__ == '__main__':
    main()
