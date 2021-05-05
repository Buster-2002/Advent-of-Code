#!/usr/bin/env python3
"""
Author: Buster
Link: https://adventofcode.com/2020/day/4#part2
Question: Count the number of valid passports - those that have all required fields and valid values. Continue to treat cid as optional. In your batch file, how many passports are valid?
Answer: 121
"""
INPUT = open('day4_input.txt', encoding='utf-8').read()
CHARS = {'a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
REQUIRED = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}


class Evaluate():

    def __init__(self):
        self._passports = [dict(
            [tuple(i.split(':', maxsplit=1)) for i in l])
            for l in list(map(lambda x: x.split(), INPUT.split('\n\n'))
        )]

    @staticmethod
    def check_byr(byr: str) -> bool:
        '''Checks if four digits; at least 1920 and at most 2002'''
        return len(byr) == 4 and 1920 <= int(byr) <= 2002

    @staticmethod
    def check_iyr(iyr: str) -> bool:
        '''Checks if four digits; at least 2010 and at most 2020.'''
        return len(iyr) == 4 and 2010 <= int(iyr) <= 2020

    @staticmethod
    def check_eyr(eyr: str) -> bool:
        '''Checks if four digits; at least 2020 and at most 2030.'''
        return len(eyr) == 4 and 2020 <= int(eyr) <= 2030

    @staticmethod
    def check_hgt(hgt: str) -> bool:
        '''Checks if a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76.
        '''
        return (
            hgt.endswith('cm')
            and 150 <= int(hgt[:-2]) <= 193 or hgt.endswith('in')
            and 59 <= int(hgt[:-2]) <= 76
        )

    @staticmethod
    def check_hcl(hcl: str) -> bool:
        '''Checks if a # followed by exactly six characters 0-9 or a-f.'''
        return hcl.startswith('#') and len(hcl[1:]) == 6 and all(char in CHARS for char in hcl[1:])

    @staticmethod
    def check_ecl(ecl: str) -> bool:
        '''Checks if exactly one of: amb blu brn gry grn hzl oth.'''
        return ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

    @staticmethod
    def check_pid(pid: str) -> bool:
        '''Checks if a nine-digit number, including leading zeroes.'''
        return len(pid) == 9 and pid.isdigit() # digit check not necessary

    def dispatch(self, key: str, value: str) -> bool:
        '''Dispatches a corresponding function based on the passports key.'''
        return getattr(self, ('check_' + key), lambda _: True)(value)

    def execute(self) -> int:
        '''Will calculate how many passports meet the requirements.'''
        valid = 0
        for passport in self._passports:
            if all(key in passport.keys() for key in REQUIRED):
                if all(self.dispatch(k, v) for k, v in passport.items()):
                    valid += 1

        return valid

if __name__ == '__main__':
    evaluator = Evaluate()
    result = evaluator.execute()
    print(f'Answer day 4, part 2: {result}')
