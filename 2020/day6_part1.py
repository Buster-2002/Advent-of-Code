#!/usr/bin/env python3
"""
Author: Buster
Link: https://adventofcode.com/2020/day/6#part1
Question: For each group, count the number of questions to which anyone answered "yes". What is the sum of those counts?
Answer: 6310
"""
INPUT = open('day6_input.txt', encoding='utf-8').read()
GROUPS = list(map(lambda x: x.replace('\n', ''), INPUT.strip().split('\n\n')))

print(sum(len(set(g))for g in map(lambda x:x.replace('\n',''),open('day6_input.txt').read().split('\n\n')))) # golf


class Evaluate():

    @staticmethod
    def get_unique(group: str) -> int:
        '''Returns the amount of unique items in a string'''
        return len(set(group))

    def execute(self) -> int:
        '''Prints the sum of the amount of unique yes answers for each group'''
        total = 0
        for group in GROUPS:
            total += self.get_unique(group)

        return total

if __name__ == '__main__':
    evaluator = Evaluate()
    result = evaluator.execute()
    print(f'Answer day 6, part 1: {result}')
