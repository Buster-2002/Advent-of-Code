"""
Author: Buster
Link: https://adventofcode.com/2020/day/5#part2
"""
INPUT = open('day5_input.txt', 'r', encoding='utf-8').read()
PASSES = INPUT.splitlines()

class Evaluate():

    @classmethod
    def get_row(cls, bd_pass: str) -> int:
        '''Calculates what row a boarding pass is for.'''
        return int(bd_pass[:7].replace('F', '0').replace('B', '1'), 2)

    @classmethod
    def get_column(cls, bd_pass: str) -> int:
        '''Calculates what column a boarding pass is for.'''
        return int(bd_pass[7:].replace('L', '0').replace('R', '1'), 2)

    @classmethod
    def get_seat(self, lst: list) -> [int, list]:
        '''Calculates your seat ID'''
        return ' '.join(map(str, [i for i in range(min(lst), max(lst)) if i not in lst]))

    def get_id(self, bd_pass: str) -> int:
        '''Calculates the unique seat ID.'''
        return (self.get_row(bd_pass) * 8) + self.get_column(bd_pass)

    def execute(self) -> int:
        '''Calculates what the highest seat ID of the input is.'''
        bd_pass_ids = [self.get_id(bd_pass) for bd_pass in PASSES]
        print(f'Answer day 5, part 2: {self.get_seat(bd_pass_ids)}')

if __name__ == '__main__':
    evaluator = Evaluate()
    evaluator.execute()