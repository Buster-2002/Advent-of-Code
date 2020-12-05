"""
Author: Buster
Link: https://adventofcode.com/2019/day/1#part2
"""
INPUT = open('day1_input.txt', 'r', encoding='utf-8').read()
MASSES = INPUT.splitlines()

def main():
    total = 0

    for mass in MASSES:
        while round((int(mass) // 3) - 2) > 0:
            mass = round((int(mass) // 3) - 2)
            total += mass

    print(f'Answer day 1, part 2: {total}')

if __name__ == '__main__':
    main()