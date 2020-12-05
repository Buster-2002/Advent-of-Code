"""
Author: Buster
Link: https://adventofcode.com/2020/day/3#part2
"""
INPUT = open('day3_input.txt', 'r', encoding='utf-8').read()
GRID = [(list(line) * 73) for line in INPUT.splitlines()]
COMBOS = (1, 1), (3, 1), (5, 1), (7, 1), (1, 2)

def enumerate2(iterator, start, step):
    for item in iterator:
        yield (start, item)
        start += step

def main():
    product = 1

    for r, d in COMBOS:
        hit = 0
        for i, line in enumerate2(GRID[0::d], 0, r):
            if line[i] == '#':
                hit += 1

        product = hit * product

    print(f'Answer day 3, part 2: {product}')

if __name__ == '__main__':
    main()
