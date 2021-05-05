#!/usr/bin/env python3
"""
Author: Buster
Link: https://adventofcode.com/2020/day/4#part1
Question: Count the number of valid passports - those that have all required fields. Treat cid as optional. In your batch file, how many passports are valid?
Answer: 190
"""
INPUT = open('day4_input.txt', encoding='utf-8').read()
PASSPORTS = [
    dict([tuple(i.split(':', maxsplit=1)) for i in l])
    for l in list(map(lambda x: x.split(), INPUT.split('\n\n')))
]
KEYWORDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}

print(sum(all(k in p.keys()for k in('byr','iyr','eyr','hgt','hcl','ecl','pid'))for p in[dict(tuple(i.split(':',maxsplit=1))for i in l)for l in map(str.split,open('day4_input.txt').read().split('\n\n'))])) # golf

def main() -> int:
    valid = 0
    for passport in PASSPORTS:
        if all(kw in passport.keys() for kw in KEYWORDS):
            valid += 1

    return valid

if __name__ == '__main__':
    result = main()
    print(f'Answer day 4, part 1: {result}')
