#!/usr/bin/env python3
"""
Author: Buster
Link: https://adventofcode.com/2020/day/7#part2
Question: How many individual bags are required inside your single shiny gold bag?
Answer: 
"""
INPUT = open('day7_input.txt', 'r', encoding='utf-8').read()
BAGS = {bag[0]: bag[1:] for bag in list(list(map(str.strip, l)) for l in map(lambda x: x.split(','), INPUT.replace('bags contain', ',').replace('bags', '').replace('bag', '').replace('.', '').translate(str.maketrans('', '', '0123456789')).splitlines()))}

class Evaluate():

    def execute(self):
        pass

if __name__ == '__main__':
    evaluator = Evaluate()
    print(f'Answer day 7, part 2: {evaluator.execute()}')
