"""
Author: Buster
Link: https://adventofcode.com/2020/day/5#part1
"""
INPUT = open('day5_input.txt', 'r', encoding='utf-8').read()
PASSES = INPUT.splitlines()

class Evaluate():

    @classmethod
    def get_row(cls, bd_pass: str) -> int:
        '''Calculates what row a boarding pass is for.'''
        row1, row2 = (0, 127)

        for i in range(7):
            if bd_pass[i] == 'F':
                row2 = (row1 + row2) // 2

            else:
                row1 = round((row1 + row2) / 2)

        return min((row1, row2))

    @classmethod
    def get_column(cls, bd_pass: str) -> int:
        '''Calculates what column a boarding pass is for.'''
        col1, col2 = (0, 7)

        for i in range(7, 10):
            if bd_pass[i] == 'L':
                col2 = (col1 + col2) // 2

            else:
                col1 = round((col1 + col2) / 2)

        return max((col1, col2))

    def get_id(self, bd_pass: str) -> int:
        '''Calculates the unique seat ID.'''
        return (self.get_row(bd_pass) * 8) + self.get_column(bd_pass)

    def execute(self) -> int:
        '''Calculates what the highest seat ID of the input is.'''
        bd_pass_ids = [self.get_id(bd_pass) for bd_pass in PASSES]
        print(f'Answer day 5, part 1: {max(bd_pass_ids)}')

if __name__ == '__main__':
    evaluator = Evaluate()
    evaluator.execute()
