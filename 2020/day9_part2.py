#!/usr/bin/env python3
"""
Author: Buster
Link: https://adventofcode.com/2020/day/9#part2
Question: Add together the smallest and largest number in this contiguous range
Answer: 5388976
"""
INPUT = open('day9_input.txt', 'r', encoding='utf-8').read()
NUMBERS = list(map(int, INPUT.splitlines()))

class Evaluate():

    @classmethod
    def check_sum(cls, preamble: list, number: int) -> bool:
        '''Check if a sum exists in :preamble for :number'''
        for i in preamble:
            if (number - i) in preamble and (number - i) != i:
                return False

        return True

    def get_invalid(self) -> int:
        '''Returns the first number that does not have a sum in it's preamble, part 1's answer'''
        numbers = NUMBERS[25:]

        for i in range(len(numbers)):
            preamble = NUMBERS[i:i+25]

            if self.check_sum(preamble, numbers[i]):
                return numbers[i]

        return None

    def execute(self) -> int:
        '''Returns the encryption weakness'''
        part1, line = self.get_invalid(), 0

        for i in range(len(NUMBERS)):
            _sum, _length = 0, 2

            while _sum < part1:
                line = NUMBERS[i:i + _length]
                _sum = sum(line)
                _length += 1

            if _sum == part1:
                return min(line) + max(line)

if __name__ == '__main__':
    evaluator = Evaluate()
    print(f'Answer day 9, part 2: {evaluator.execute()}')
