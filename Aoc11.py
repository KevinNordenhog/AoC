def main():
    with open("input11.txt") as file:
        lines = file.read().splitlines()
    grid = [list(map(int, line)) for line in lines]
    Step(grid)


def Step(grid):
    cnt = 0
    for step in range(1, 1000):
        increaseGrid(grid)
        cnt += flashGrid(grid)
        if step == 100:
            print("Part one:", cnt)
        if allFlashed(grid):
            print("Part two:", step)
            break


def increaseGrid(grid):
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            grid[x][y] = grid[x][y] + \
                (1 if grid[x][y] >= 0 else 2)


def flashGrid(grid):
    cnt = 0
    for x in range(len(grid)):
        for y in range(len(grid[0])):
            cnt += flash(grid, x, y)
    return cnt


def flash(grid, x, y):
    cnt = 0
    if grid[x][y] > 9:
        cnt += 1
        grid[x][y] = -1
        cnt += flashNeighbors(grid, x, y)

    return cnt


def flashNeighbors(grid, x, y):
    cnt = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (i, j) != (0, 0) and isBetween(x+i, -1, len(grid)) and isBetween(y+j, -1, len(grid[0])):
                if grid[x+i][y+j] >= 0 and grid[x+i][y+j] <= 9:
                    grid[x+i][y+j] += 1
                if grid[x+i][y+j] > 9:
                    cnt += flash(grid, x+i, y+j)
    return cnt


def isBetween(val, min, max):
    return val > min and val < max


def allFlashed(grid):
    for row in grid:
        for value in row:
            if value != -1:
                return False
    return True


if __name__ == "__main__":
    main()
