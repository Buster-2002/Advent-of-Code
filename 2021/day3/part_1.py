#!/usr/bin/env python3

"""
Author: Buster
Link: https://adventofcode.com/2021/day/3#part1
Question: What is the power consumption of the submarine?
My answer 2003336
"""
INPUT = open('input.txt', encoding='utf-8').read()


class Evaluate:
    def __init__(self):
        self.gamma_rate = ''
        self.epsilon_rate = ''
        self.diagnostics = [
            list(map(int, list(line)))
            for line in INPUT.splitlines()
        ]


    def execute(self) -> int:
        for position in range(12): # Each number has a length of 12 bits
            zero_counter = 0
            one_counter = 0

            for bit_list in self.diagnostics:
                if bit_list[position] == 0:
                    zero_counter += 1
                elif bit_list[position] == 1:
                    one_counter += 1

            result = zero_counter > one_counter
            self.gamma_rate += str(int(result))
            self.epsilon_rate += str(int(not result))
    
            # if zero_counter > one_counter:
            #     self.gamma_rate += '0'
            #     self.epsilon_rate += '1'
            # else:
            #     self.gamma_rate += '1'
            #     self.epsilon_rate += '0'

        gamma_rate_decimal = int(self.gamma_rate, 2)
        epsilon_rate_decimal = int(self.epsilon_rate, 2)
        return gamma_rate_decimal * epsilon_rate_decimal


if __name__ == '__main__':
    evaluator = Evaluate()
    print(f'Answer 2021.03.01: {evaluator.execute()}')
