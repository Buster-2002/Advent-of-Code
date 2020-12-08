#!/usr/bin/env python3
"""
Author: Buster
Link: https://adventofcode.com/2020/day/7#part1
Question: How many bag colors can eventually contain at least one shiny gold bag?
Answer: 126
"""
INPUT = open('day7_input.txt', 'r', encoding='utf-8').read()
# this might be the stupidest way to do this but ok
BAGS = {bag[0]: bag[1:] for bag in list(list(map(str.strip, l)) for l in map(lambda x: x.split(','), INPUT.replace('bags contain', ',').replace('bags', '').replace('bag', '').replace('.', '').translate(str.maketrans('', '', '0123456789')).splitlines()))}

class Evaluate():

    def get_amount(self, bag: (str, [list])) -> int:
        '''Returns the amount of shiny gold bags a bag can eventually hold'''
        if 'no other' in BAGS[bag]:
            return False

        if 'shiny gold' in BAGS[bag]:
            return True

        return any(self.get_amount(b) for b in BAGS[bag])

    def execute(self) -> int:
        '''Prints the sum of bag colours that can eventually hold at least 1 shiny gold bag'''
        total = []

        for bag in BAGS:
            total.append(self.get_amount(bag))

        return sum(total)

if __name__ == '__main__':
    evaluator = Evaluate()
    print(f'Answer day 7, part 1: {evaluator.execute()}')
