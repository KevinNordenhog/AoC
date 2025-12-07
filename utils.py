from collections import defaultdict
from typing import Type


def createGrid(lines: list[str], type: Type):
    grid = defaultdict(type)
    numbers = [list(map(type, line.split())) for line in lines]
    gridRowCount = len(numbers)
    gridColCount = len(numbers[0])
    for i in range(gridRowCount):
        for j in range(gridColCount):
            grid[(i, j)] = numbers[i][j]
    return grid


def println(lines: list[str]):
    print("\n".join(lines))


def replace_char(s: str, index: int, new_char: str) -> str:
    return s[:index] + new_char + s[index + 1 :]
