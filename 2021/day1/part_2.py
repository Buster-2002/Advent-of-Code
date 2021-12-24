#!/usr/bin/env python3

"""
Author: Buster
Link: https://adventofcode.com/2021/day/1#part2
Question: Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?
My answer
"""
INPUT = open('input.txt', encoding='utf-8').read()


class Evaluate:

    def execute(self) -> int:
        numbers = list(map(int, INPUT.splitlines()))
        measurement_groups = []

        for position in range(len(numbers)):
            window = numbers[position:][:3]
            measurement_groups.append(window)

        previous_measurement_sum = float('inf')
        increased_counter = 0

        for measurement_group in measurement_groups:
            measurement_sum = sum(measurement_group)
            if measurement_sum > previous_measurement_sum:
                increased_counter += 1

            previous_measurement_sum = measurement_sum

        return increased_counter


if __name__ == '__main__':
    evaluator = Evaluate()
    print(f'Answer 2021.01.02: {evaluator.execute()}')
