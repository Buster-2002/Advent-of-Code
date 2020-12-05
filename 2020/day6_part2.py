"""
Author: Buster
Link: https://adventofcode.com/2020/day/6#part2
"""
INPUT = open('day6_input.txt', 'r', encoding='utf-8').read()


def main():
    for day in range(17, 24):
        for part in range(1, 3): 
            f = open(f'day{day}_part{part}.py', 'w', encoding='utf-8')
            open(f'day{day}_input.txt', 'w', encoding='utf-8')
            DEFAULT = f"""
\"\"\"
Author: Buster
Link: https://adventofcode.com/2020/day/{day}#part{part}
\"\"\"
INPUT = open('day{day}_input.txt', 'r', encoding='utf-8').read()

def main():
    pass

if __name__ == '__main__':
    main()
"""
            f.write(DEFAULT)
            f.close()

if __name__ == '__main__':
    main()