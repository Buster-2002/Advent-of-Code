"""
Author: Buster
Link: https://adventofcode.com/2020/day/6#part2
"""
INPUT = open('day6_input.txt', 'r', encoding='utf-8').read()
GROUPS = list(map(lambda x: x.split('\n'), INPUT.strip().split('\n\n')))

print(sum(len(set.intersection(*map(set,g)))for g in map(str.split,open('day6_input.txt').read().split('\n\n')))) # golf

class Evaluate():

    @classmethod
    def get_unique(cls, group: list) -> int:
        '''Returns the amount of unique items in a string'''
        return len(set.intersection(*[set(member) for member in group]))

    def execute(self) -> int:
        '''Prints the sum of the amount of unique yes answers for each group'''
        total = 0

        for group in GROUPS:
            total += self.get_unique(group)

        print(f'Answer day 6, part 2: {total}')

if __name__ == '__main__':
    evaluator = Evaluate()
    evaluator.execute()
