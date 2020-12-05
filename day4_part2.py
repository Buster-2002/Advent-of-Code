"""
Author: Buster
Link: https://adventofcode.com/2020/day/4#part2
"""
INPUT = open('day4_input.txt', 'r', encoding='utf-8').read()

class Evaluate():

    def __init__(self):
        self.passports = [dict([tuple(i.split(':', maxsplit=1)) for i in l]) for l in list(map(lambda x: x.split(), INPUT.split('\n\n')))]
        self.chars = ('a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
        self.eye_colours = ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')

    @classmethod
    def check_byr(cls, byr: str) -> bool:
        '''Checks if four digits; at least 1920 and at most 2002'''
        return len(byr) == 4 and 1920 <= int(byr) <= 2002

    @classmethod
    def check_iyr(cls, iyr: str) -> bool:
        '''Checks if four digits; at least 2010 and at most 2020.'''
        return len(iyr) == 4 and 2010 <= int(iyr) <= 2020

    @classmethod
    def check_eyr(cls, eyr: str) -> bool:
        '''Checks if four digits; at least 2020 and at most 2030.'''
        return len(eyr) == 4 and 2020 <= int(eyr) <= 2030

    @classmethod
    def check_hgt(cls, hgt: str) -> bool:
        '''Checks if a number followed by either cm or in:
            If cm, the number must be at least 150 and at most 193.
            If in, the number must be at least 59 and at most 76.
        '''
        return hgt.endswith('cm') and 150 <= int(hgt[:-2]) <= 193 or hgt.endswith('in') and 59 <= int(hgt[:-2]) <= 76

    def check_hcl(self, hcl: str) -> bool:
        '''Checks if a # followed by exactly six characters 0-9 or a-f.'''
        return hcl.startswith('#') and len(hcl[1:]) == 6 and all([char in self.chars for char in hcl[1:]])

    def check_ecl(self, ecl: str) -> bool:
        '''Checks if exactly one of: amb blu brn gry grn hzl oth.'''
        return ecl in self.eye_colours

    @classmethod
    def check_cid(cls, _: str) -> bool:
        return True

    @classmethod
    def check_pid(cls, pid: str) -> bool:
        '''Checks if a nine-digit number, including leading zeroes.'''
        return len(pid) == 9 and pid.isdigit()

    def dispatch(self, key: str, value: str):
        '''Dispatches a corresponding function based on the passports key.'''
        method = getattr(self, ('check_' + key))
        method(value)

    def execute(self):
        '''Will calculate how many passports meet the requirements.'''
        valid = 0

        for passport in self.passports:
            if all(self.dispatch(k, v) for k, v in passport.items()):
                valid += 1

        print(f'Answer day 4, part 2: {valid}')

if __name__ == '__main__':
    evaluator = Evaluate()
    evaluator.execute()
