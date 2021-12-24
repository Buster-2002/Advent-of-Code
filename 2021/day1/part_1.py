#!/usr/bin/env python3

"""
Author: Buster
Link: https://adventofcode.com/2021/day/1#part1
Question: How many measurements are larger than the previous measurement?
My answer 1581
"""
INPUT = open('input.txt', encoding='utf-8').read()


class Evaluate:

    def execute(self) -> int:
        numbers = map(int, INPUT.splitlines())
        previous_number = float('inf')
        increased_counter = 0

        for number in numbers:
            if number > previous_number:
                increased_counter += 1
            
            previous_number = number

        return increased_counter


if __name__ == '__main__':
    evaluator = Evaluate()
    print(f'Answer 2021.01.01: {evaluator.execute()}')
