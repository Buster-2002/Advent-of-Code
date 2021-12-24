#!/usr/bin/env python3

from dataclasses import dataclass
from enum import Enum
from typing import List

"""
Author: Buster
Link: https://adventofcode.com/2021/day/2#part1
Question: What do you get if you multiply your final horizontal position by your final depth?
My answer 2102357
"""
INPUT = open('input.txt', encoding='utf-8').read()


class CommandType(Enum):
    forward = 0 # increases the horizontal position by X units
    down    = 1 # increases the depth by X units
    up      = 2 # decreases the depth by X units


@dataclass
class Command:
    command_type: CommandType
    value: int


class Evaluate:
    def __init__(self):
        self.horizontal_position = 0
        self.depth = 0
        self.commands: List[Command] = list(map(
            self.split_command_from_value,
            INPUT.splitlines()
        ))


    def split_command_from_value(self, line: str) -> Command:
        command_string, value = line.split()
        return Command(CommandType[command_string], int(value))


    def execute(self) -> int:
        for command in self.commands:
            if command.command_type is CommandType.forward:
                self.horizontal_position += command.value
            elif command.command_type is CommandType.down:
                self.depth += command.value
            elif command.command_type is CommandType.up:
                self.depth -= command.value

        return self.horizontal_position * self.depth


if __name__ == '__main__':
    evaluator = Evaluate()
    print(f'Answer 2021.02.01: {evaluator.execute()}')
