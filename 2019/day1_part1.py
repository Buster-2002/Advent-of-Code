"""
Author: Buster
Link: https://adventofcode.com/2019/day/1#part1
"""
INPUT = open('day1_input.txt', encoding='utf-8').read()
MASSES = INPUT.splitlines()

def main() -> int:
    total = 0
    for mass in MASSES:
        total += round((int(mass) // 3) - 2)

    return total

if __name__ == '__main__':
    result = main()
    print(f'Answer day 1, part 1: {result}')
