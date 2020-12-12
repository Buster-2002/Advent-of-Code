#!/usr/bin/env python3
"""
Author: Buster
Link: https://adventofcode.com/2020/day/10#part1
Question: What is the number of 1-jolt differences multiplied by the number of 3-jolt differences?
Answer: 2040
"""
INPUT = open('day10_input.txt', 'r', encoding='utf-8').read()
ADAPTERS = sorted(map(int, INPUT.splitlines()))

class Evaluate():

    @classmethod
    def get_adapter(cls, _index) -> int:
        '''Safely returns an adapter'''
        try:
            return ADAPTERS[_index]

        except IndexError:
            return 0

    def execute(self) -> int:
        '''Returns the product of the amount of 1 joltage and 3 joltage differences'''
        diff_1, diff_3 = 1, 1 # Start with one, because of built-in adapter being valid

        for i, adapter in enumerate(ADAPTERS):
            diff = abs(adapter - self.get_adapter(i+1))

            if diff == 1:
                diff_1 += 1

            elif diff == 3:
                diff_3 += 1

        return diff_1 * diff_3

if __name__ == '__main__':
    evaluator = Evaluate()
    print(f'Answer day 10, part 1: {evaluator.execute()}')
