#!/usr/bin/env python3
"""
Author: Buster
Link: https://adventofcode.com/2020/day/8#part1
Question: Run your copy of the boot code. Immediately before any instruction is executed a second time, what value is in the accumulator?
Answer: 1782
"""
INPUT = open('day8_input.txt', 'r', encoding='utf-8').read()
CODE = [{'opcode': l[0], 'value': int(l[1])} for l in map(str.split, INPUT.splitlines())]

def main() -> int:
    '''Returns the value of the accumulator'''
    acc, step, instructs = 0, 0, []
    
    while True:
        if step not in instructs and step < len(CODE):
            instructs.append(step)
            c = CODE[step]

            if c['opcode'] == 'acc':
                acc += c['value']

            if c['opcode'] == 'jmp':
                step += c['value']

            else:
                step += 1

        else:
            return acc, instructs

if __name__ == '__main__':
    var, var1 = main()
    print(f'Answer day 8, part 1: {main()}')
