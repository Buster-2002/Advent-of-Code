"""
Author: Buster
Link: https://adventofcode.com/2020/day/5#part1
"""
INPUT = open('day5_input.txt', 'r', encoding='utf-8').read()
PASSES = INPUT.splitlines()

print(*(map(lambda r,c:r*8+c,*zip(max((int(p[:7].replace('F','0').replace('B','1'), 2),int(p[7:].replace('L','0').replace('R','1'), 2))for p in open('day5_input.txt').readlines()))))) # golf

class Evaluate():

    @classmethod
    def get_row(cls, bd_pass: str) -> int:
        '''Calculates what row a boarding pass is for.'''
        return int(bd_pass[:7].replace('F', '0').replace('B', '1'), 2)

    @classmethod
    def get_column(cls, bd_pass: str) -> int:
        '''Calculates what column a boarding pass is for.'''
        return int(bd_pass[7:].replace('L', '0').replace('R', '1'), 2)

    def get_id(self, bd_pass: str) -> int:
        '''Calculates the unique seat ID.'''
        return self.get_row(bd_pass) * 8 + self.get_column(bd_pass)

    def execute(self) -> int:
        '''Calculates what the highest seat ID of the input is.'''
        bd_pass_ids = [self.get_id(bd_pass) for bd_pass in PASSES]
        print(f'Answer day 5, part 1: {max(bd_pass_ids)}')

if __name__ == '__main__':
    evaluator = Evaluate()
    evaluator.execute()
