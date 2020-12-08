#!/usr/bin/env python3 
"""
Author: Buster
Link: https://adventofcode.com/2020/day/2#part2
Question: How many passwords are valid according to the new interpretation of the policies?
Answer: 673
"""
INPUT = open('day2_input.txt', 'r', encoding='utf-8').read()

def main():
    correct = 0

    for combo in INPUT.splitlines():
        combo = combo.split()
        _range = list(map(int, combo[0].replace('-', ' ').split()[0:2]))
        letter = combo[1].replace(':', '')
        password = combo[2]

        if password[(_range[0] - 1)] == letter and not password[(_range[1] - 1)] == letter:
            correct += 1

        elif password[(_range[1] - 1)] == letter and not password[(_range[0] - 1)] == letter:
            correct += 1

    print(f'Answer day 2, part 2: {correct}')

if __name__ == '__main__':
    main()
    