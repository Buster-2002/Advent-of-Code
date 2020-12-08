#!/usr/bin/env python3
"""
Author: Buster
Link: https://adventofcode.com/2020/day/7#part2
Question: How many individual bags are required inside your single shiny gold bag?
Answer: 58175
"""
import re

INPUT = open('day7_input.txt', 'r', encoding='utf-8').read()
BAGS = {line[0]: {part[1]: int(part[0]) for part in line[1]} for line in [(re.match(r'(\w+ \w+) bags contain', line)[1], re.findall(r'(\d) (\w+ \w+) bag', line)) for line in INPUT.splitlines()]}

def main():
    def count_bags(bag):
        return sum(count_bags(bag) * amt for bag, amt in BAGS[bag].items()) + 1

    return count_bags('shiny gold') - 1

if __name__ == '__main__':
    print(f"Answer day 7, part 2: {main()}")
