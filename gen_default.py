#!/usr/bin/env python3
"""Generates folders and files for Advent of Code years
"""

from pathlib import Path
from textwrap import dedent


def generate_files(year: str):
    for day in range(4, 26):
        # Create folder for day
        day_path = Path(f'{year}/day{day}')
        day_path.mkdir(parents=True, exist_ok=True)

        for part_number in range(1, 3):
            part_path = Path(day_path, f'part_{part_number}').with_suffix('.py')
            text_path = Path(day_path, 'input').with_suffix('.txt')

            # Create text file
            open(text_path, 'w+', encoding='utf-8')

            # Create python files
            with open(part_path, 'w+', encoding='utf-8') as file:
                content = dedent(f"""
                    #!/usr/bin/env python3

                    \"\"\"
                    Author: Buster
                    Link: https://adventofcode.com/{year}/day/{day}#part{part_number}
                    Question: 
                    My answer: 
                    \"\"\"
                    INPUT = open('input.txt', encoding='utf-8').read()


                    class Evaluate:

                        def execute(self) -> int:
                            pass


                    if __name__ == '__main__':
                        evaluator = Evaluate()
                        print(f'Answer {year}.{str(day).zfill(2)}.{str(part_number).zfill(2)}: {{evaluator.execute()}}')
                    """
                )
                file.write(content)
                print('Created:', part_path, text_path, sep='\n')


if __name__ == '__main__':
    year = input('Year of AOC? > ')
    generate_files(year)
