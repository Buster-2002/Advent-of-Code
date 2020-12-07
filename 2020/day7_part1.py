"""
Author: Buster
Link: https://adventofcode.com/2020/day/7#part1
"""
INPUT = open('day7_input.txt', 'r', encoding='utf-8').read()
# this might be the stupidest way to do this but ok
BAGS = {bag[0]: bag[1:] for bag in list(list(map(str.strip, l)) for l in map(lambda x: x.split(','), INPUT.replace('bags contain', ',').replace('bags', '').replace('bag', '').replace('.', '').translate(str.maketrans('', '', '0123456789')).splitlines()))}

class Evaluate():

    def get_amount(self, bag: tuple(str, [list])) -> int:
        '''Returns the amount of shiny gold bags a bag can eventually hold'''
        if bag[0] == 'shiny gold':
            return 1

        return 1 if any(self.get_amount(b) for b in bag[1:]) else 0

    def execute(self) -> int:
        '''Prints the sum of bag colours that can eventually hold at least 1 shiny gold bag'''
        total = 0

        for bag in BAGS.items():
            total += self.get_amount(bag)

        return total

if __name__ == '__main__':
    evaluator = Evaluate()
    print(f'Answer day 7, part 1: {evaluator.execute()}')
