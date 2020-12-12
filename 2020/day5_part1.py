#!/usr/bin/env python3
"""
Author: Buster
Link: https://adventofcode.com/2020/day/5#part1
Question: As a sanity check, look through your list of boarding passes. What is the highest seat ID on a boarding pass?
Answer: 915
"""
INPUT = open('day5_input.txt', 'r', encoding='utf-8').read()
PASSES = INPUT.splitlines()

print(*[r*8+c for r,c in[max((int(p[:7].replace('F','0').replace('B','1'),2),int(p[7:].replace('L','0').replace('R','1'),2))for p in open('day5_input.txt').readlines())]]) # golf

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
        bd_pass_ids = []
        
        for bd_pass in PASSES:
            bd_pass_ids.append(self.get_id(bd_pass))

        return max(bd_pass_ids)

if __name__ == '__main__':
    evaluator = Evaluate()
    print(f'Answer day 5, part 1: {evaluator.execute()}')
