def main():
    with open("input9.txt") as file:
        lines = file.read().splitlines()
    matrix = [list(line) for line in lines]
    print("Part one:", partOne(matrix))
    print("Part two:", PartTwo(matrix))


def partOne(matrix):
    sum = 0
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            sum += (int(matrix[x][y])+1) * isLowPoint(matrix, x, y)
    return sum


def PartTwo(matrix):
    basins = [[]]
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            if not any([(x, y) in basin for basin in basins]):
                basins.append(getBasin(matrix, [], x, y))
    sortd = sorted(basins, key=len)
    return len(sortd[-1])*len(sortd[-2])*len(sortd[-3])


def isLowPoint(matrix, x, y):
    point = int(matrix[x][y])
    top = int(matrix[x][y-1]) if y > 0 else 9
    bottom = int(matrix[x][y+1]) if y < len(matrix[0])-1 else 9
    left = int(matrix[x-1][y]) if x > 0 else 9
    right = int(matrix[x+1][y]) if x < len(matrix)-1 else 9
    return min([point, top, bottom, left, right]) == point and point != 9


def getBasin(matrix, basin, x, y):
    if (x, y) in basin or int(matrix[x][y]) == 9:
        return []
    basin.append((x, y))
    if y > 0:
        getBasin(matrix, basin, x, y-1)
    if y < len(matrix[0])-1:
        getBasin(matrix, basin, x, y+1)
    if x > 0:
        getBasin(matrix, basin, x-1, y)
    if x < len(matrix)-1:
        getBasin(matrix, basin, x+1, y)
    return basin


if __name__ == "__main__":
    main()
