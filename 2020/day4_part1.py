"""
Author: Buster
Link: https://adventofcode.com/2020/day/4#part1
"""
INPUT = open('day4_input.txt', 'r', encoding='utf-8').read()
PASSPORTS = [dict([tuple(i.split(':', maxsplit=1)) for i in l]) for l in list(map(lambda x: x.split(), INPUT.split('\n\n')))]
KEYWORDS = 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'

def main():
    valid = 0

    for passport in PASSPORTS:
        if all(kw in passport.keys() for kw in KEYWORDS):
            valid += 1

    print(f'Answer day 4, part 1: {valid}')

if __name__ == '__main__':
    main()