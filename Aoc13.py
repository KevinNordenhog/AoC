MAXX = 0
MAXY = 0


def main():
    with open("input13.txt") as file:
        lines = file.read().splitlines()
    mapp = [line.split(',') for line in lines]

    grid = createGrid([list(map(int, point))
                      for point in mapp if len(point) > 1])
    foldDirections = [val[0] for val in mapp if len(val) == 1 and val[0] != '']
    print("Part one:", partOne(grid, foldDirections))
    print("Part two:")
    partTwo(grid, foldDirections)


def partOne(grid, foldDirections):
    foldedGrid = grid
    foldedGrid = fold(foldedGrid, foldDirections[0])

    return sum([sum(row) for row in foldedGrid])


def partTwo(grid, foldDirections):
    foldedGrid = grid
    for direction in foldDirections:
        foldedGrid = fold(foldedGrid, direction)

    return prettfy(foldedGrid)


def fold(grid: list[list], direktion: str):
    temp = direktion.split('=')
    axis = temp[0][-1]
    line = int(temp[1])
    if axis == "x":
        for i in range(1, line+1):
            for y in range(len(grid[0])):
                if line+i <= len(grid):
                    grid[line-i][y] = grid[line+i][y] or grid[line-i][y]
        grid = [grid[i] for i in range(line)]

    elif axis == "y":
        for x in range(len(grid)):
            for i in range(1, line+1):
                if line+i <= len(grid[0]):
                    grid[x][line-i] = grid[x][line+i] or grid[x][line-i]
        grid = [[row[i] for i in range(line)] for row in grid]

    return grid


def prettfy(grid: list[list]):
    prettyGrid = []
    i = 0
    for y in range(len(grid[0])):
        prettyGrid.append([])
        for x in range(len(grid)):
            prettyGrid[i].append("#" if grid[x][y] else ".")
        i += 1
    for row in prettyGrid:
        print(row)


def createGrid(map):
    MAXX = max(point[0] for point in map if len(point) > 1) + 1
    MAXY = max(point[1] for point in map if len(point) > 1) + 1
    grid = [[0 for x in range(MAXY)] for y in range(MAXX)]
    for x, y in map:
        grid[x][y] = 1
    return grid


if __name__ == "__main__":
    main()
