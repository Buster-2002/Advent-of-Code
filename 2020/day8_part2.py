#!/usr/bin/env python3
"""
Author: Buster
Link: https://adventofcode.com/2020/day/8#part2
Question: Fix the program so that it terminates normally by changing exactly one jmp (to nop) or nop (to jmp). What is the value of the accumulator after the program terminates?
Answer: 797
"""
from typing import Tuple, List


INPUT = open('day8_input.txt', encoding='utf-8').read()
DEFAULT_CODE = [
    {'opcode': l[0], 'value': int(l[1])}
    for l in map(str.split, INPUT.splitlines())
]


class Evaluate():

    @staticmethod
    def run(code: list) -> Tuple[int, List[int]]:
        '''Returns the value of the accumulator'''
        acc, step, instructs = 0, 0, []
        while True:
            if step not in instructs and step < len(code):
                instructs.append(step)
                c = code[step]
                if c['opcode'] == 'acc':
                    acc += c['value']
                if c['opcode'] == 'jmp':
                    step += c['value']
                else:
                    step += 1
            else:
                instructs.append(step)
                return acc, instructs

    @staticmethod
    def opposite(opcode: str) -> str:
        '''Returns the opposite of :opcode'''
        if opcode == 'jmp':
            return 'nop'
        if opcode == 'nop':
            return 'jmp'
        return opcode

    def find_fault(self, instructions: list) -> int:
        '''Finds what acc should be a jmp, or what jmp should be a acc'''
        new_code = DEFAULT_CODE.copy()
        for l in instructions:
            opcode = new_code[l]['opcode']
            if opcode == 'jmp':
                opcode = self.opposite(opcode)
                new_code[l].update({
                    'opcode': opcode
                })
                acc, instructs = self.run(new_code)
                if instructs[-1] == len(DEFAULT_CODE):
                    return acc
                new_code[l].update({
                    'opcode': self.opposite(opcode)
                })

        return None

    def execute(self) -> int:
        '''Finds the fault in the code, and returns correct accumulator'''
        instructions = self.run(DEFAULT_CODE)[1]
        return self.find_fault(instructions)

if __name__ == '__main__':
    evaluator = Evaluate()
    result = evaluator.execute()
    print(f'Answer day 8, part 2: {result}')
