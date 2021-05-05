"""
Author: Buster
Link: https://adventofcode.com/2019/day/2#part1
"""
INPUT = open('day2_input.txt', encoding='utf-8').read()
INTEGERS = list(map(int, INPUT.split(',')))

def main() -> int:
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
            return INTEGERS[0]

if __name__ == '__main__':
    result = main()
    print(f'Answer day 2, part 1: {result}')