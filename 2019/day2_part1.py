"""
Author: Buster
Link: https://adventofcode.com/2019/day/2#part1
"""
INPUT = open('day2_input.txt', encoding='utf-8').read()
INTEGERS = list(map(int, INPUT.split(',')))

def main():
    INTEGERS[1] = 12
    INTEGERS[2] = 2

    for p, i in enumerate(INTEGERS):
        if i == 1:
            workspace = INTEGERS[p:(p + 4)]
            workspace[3] = INTEGERS[workspace[1]] + INTEGERS[workspace[2]]

        elif i == 2:
            workspace = INTEGERS[p:(p + 4)]
            workspace[3] = INTEGERS[workspace[1]] * INTEGERS[workspace[2]]

        elif i == 99:
            print(f'Answer day 2, part 1: {INTEGERS[0]}')
            break

if __name__ == '__main__':
    main()