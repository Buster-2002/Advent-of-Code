"""
Author: Buster
Link: https://adventofcode.com/2020/day/2#part1
"""
INPUT = open('day2_input.txt', 'r', encoding='utf-8').read()

def main():
    correct = 0
    for combo in INPUT.splitlines():
        combo = combo.split()
        _range = list(map(int, combo[0].replace('-', ' ').split()[0:2]))
        letter = combo[1].replace(':', '')
        password = combo[2]

        if _range[0] <= password.count(letter) <= _range[1]:
            correct += 1

    print(f'Answer day 2, part 1: {correct}')

if __name__ == '__main__':
    main()
