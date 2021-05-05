#!/usr/bin/env python3
"""
Author: Buster
Link: https://adventofcode.com/2020/day/2#part1
Question: How many passwords are valid according to their policies?
Answer: 655
"""
INPUT = open('day2_input.txt', encoding='utf-8').read()

def main() -> int:
    correct = 0
    for combo in INPUT.splitlines():
        combo = combo.split()
        _range = list(map(int, combo[0].replace('-', ' ').split()[0:2]))
        letter, password = combo[1].replace(':', ''), combo[2]
        if _range[0] <= password.count(letter) <= _range[1]:
            correct += 1

    return correct

if __name__ == '__main__':
    result = main()
    print(f'Answer day 2, part 1: {result}')
    