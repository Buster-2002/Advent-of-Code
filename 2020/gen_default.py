for day in range(1, 26):
    open(f'day{day}_input.txt', 'w', encoding='utf-8')
    for part in range(1, 3):
        f = open(f'day{day}_part{part}.py', 'w', encoding='utf-8')
        content = f"""#!/usr/bin/env python3
\"\"\"
Author: Buster
Link: https://adventofcode.com/2020/day/{day}#part{part}
Question: 
Answer: 
\"\"\"
INPUT = open('day{day}_input.txt', 'r', encoding='utf-8').read()

class Evaluate():

    def execute(self):
        pass

if __name__ == '__main__':
    evaluator = Evaluate()
    print(f'Answer day {day}, part {part}: {{evaluator.execute()}}')
"""
        f.write(content)
