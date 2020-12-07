"""
Author: Buster
Link: https://adventofcode.com/2020/day/7#part1
"""
INPUT = open('day7_input.txt', 'r', encoding='utf-8').read()
# this might be the stupidest way to do this but ok
BAGS = {bag[0]: bag[1:] for bag in list(list(map(str.strip, l)) for l in map(lambda x: x.split(','), INPUT.replace('bags contain', ',').replace('bags', '').replace('bag', '').replace('.', '').translate(str.maketrans('', '', '0123456789')).splitlines()))}

class Evaluate():

    @classmethod
    def get_amount(cls, bag: str) -> int:
        '''Returns the amount of shiny gold bags a bag can eventually hold'''
        golden = 0

        def recurse(_bag):
            for sub_bag in _bag:
                if sub_bag == 'shiny gold':
                    golden += 1
                    break

                recurse(BAGS.get(sub_bag))

        return golden

    def execute(self) -> int:
        '''Prints the sum of bag colours that can eventually hold at least 1 shiny gold bag'''
        total = 0

        for bag in BAGS:
            total += self.get_amount(bag)

        print(f'Answer day 7, part 1: {total}')
    
if __name__ == '__main__':
    evaluator = Evaluate()
    evaluator.execute()
