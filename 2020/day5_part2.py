#!/usr/bin/env python3
"""
Author: Buster
Link: https://adventofcode.com/2020/day/5#part2
Question: What is the ID of your seat?
Answer: 699
"""
INPUT = open('day5_input.txt', encoding='utf-8').read()
PASSES = INPUT.splitlines()


class Evaluate():

    @staticmethod
    def get_row(bd_pass: str) -> int:
        '''Calculates what row a boarding pass is for.'''
        return int(bd_pass[:7].replace('F', '0').replace('B', '1'), 2)

    @staticmethod
    def get_column(bd_pass: str) -> int:
        '''Calculates what column a boarding pass is for.'''
        return int(bd_pass[7:].replace('L', '0').replace('R', '1'), 2)

    @staticmethod
    def get_seat(lst: list) -> int:
        '''Calculates your seat ID'''
        return [i for i in range(min(lst), max(lst)) if i not in lst][0]

    def get_id(self, bd_pass: str) -> int:
        '''Calculates the unique seat ID.'''
        return (self.get_row(bd_pass) * 8) + self.get_column(bd_pass)

    def execute(self) -> int:
        '''Calculates what the highest seat ID of the input is.'''
        bd_pass_ids = []
        for bd_pass in PASSES:
            bd_pass_ids.append(self.get_id(bd_pass))

        return self.get_seat(bd_pass_ids)

if __name__ == '__main__':
    evaluator = Evaluate()
    result = evaluator.execute()
    print(f'Answer day 5, part 2: {result}')