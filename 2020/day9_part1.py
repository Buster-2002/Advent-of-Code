#!/usr/bin/env python3
"""
Author: Buster
Link: https://adventofcode.com/2020/day/9#part1
Question: What is the first number that does not have the sum of 2 of the previous 25 numbers as the next in line?
Answer: 41682220
"""
INPUT = open('day9_input.txt', encoding='utf-8').read()
NUMBERS = list(map(int, INPUT.splitlines()))


class Evaluate():

    @staticmethod
    def check_sum(preamble: list, number: int) -> bool:
        '''Check if a sum exists in :preamble for :number'''
        for i in preamble:
            if (number - i) in preamble and (number - i) != i:
                return False

        return True

    def execute(self) -> int:
        '''Returns the first number that does not have a sum in it's preamble'''
        numbers = NUMBERS[25:]
        for i in range(len(numbers)):
            preamble = NUMBERS[i:i + 25]
            if self.check_sum(preamble, numbers[i]):
                return numbers[i]

        return None

if __name__ == '__main__':
    evaluator = Evaluate()
    result = evaluator.execute()
    print(f'Answer day 9, part 1: {result}')
