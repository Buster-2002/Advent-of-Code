#!/usr/bin/env python3
"""
Author: Buster
Link: https://adventofcode.com/2020/day/10#part2
Question: What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?
Answer: 28346956187648
"""
INPUT = open('day10_input.txt', 'r', encoding='utf-8').read()
ADAPTERS = sorted(map(int, INPUT.splitlines()))

def main():
    cache = {0: 1}

    for adapter in ADAPTERS:
        routes = 0

        for i in range(1, 4):
            routes += cache.get(adapter - i, 0)
        
        cache[adapter] = routes

    return cache[max(ADAPTERS)]

if __name__ == '__main__':
    print(f'Answer day 10, part 2: {main()}')
