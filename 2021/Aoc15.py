import heapq
import copy


def main():
    with open("input15.txt") as file:
        lines = file.read().splitlines()
    grid = [list(map(int, line)) for line in lines]

    print("Part One:", partOne(grid))
    print("Part Two:", partTwo(grid))


def partOne(grid: list[list[int]]):
    global height, width
    height = len(grid)
    width = len(grid[1])
    path = aStar(grid, (0, 0), (height-1, width-1))
    print(path)
    numbers = [grid[indices[0]][indices[1]]for indices in path]
    print(numbers)
    return sum(numbers)-grid[0][0]


def partTwo(grid: list[list[int]]):
    fullMap = getFullMap(grid)
    global height, width
    height = len(fullMap)
    width = len(fullMap[1])
    path = aStar(fullMap, (0, 0), (height-1, width-1))
    numbers = [fullMap[indices[0]][indices[1]]for indices in path]
    return sum(numbers)-fullMap[0][0]


def getFullMap(grid: list[list[int]]):
    fullMap = copy.deepcopy(grid)
    # Columns
    for i in range(1, 5):
        for r in range(len(grid[0])):
            # Får inte vara 0, 9 ska wrappa till 1
            fullMap[r] += [(val + i + 1) % 10 if (val + i) >
                           9 else (val + i) % 10 for val in grid[r]]
    # rows
    for i in range(1, 5):
        for r in range(len(grid)):
            # Får inte vara 0, 9 ska wrappa till 1
            fullMap.append([(val + i + 1) % 10 if (val + i) > 9 else (val + i) %
                            10 for val in fullMap[r]])

    return fullMap


def getCopy(grid: list[list[int]]):
    return [val for val in grid]


def aStar(grid, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    path = []

    while not frontier.empty():
        current = frontier.get()
        if current == goal:
            break
        for node in neighbours(grid, current):
            new_cost = cost_so_far[current] + grid[node[0]][node[1]]
            if node not in cost_so_far or new_cost < cost_so_far[node]:
                cost_so_far[node] = new_cost
                prio = new_cost + heuristic(goal, node)
                frontier.put(node, prio)
                came_from[node] = current

    temp = current
    while (temp in came_from):
        path.append(temp)
        temp = came_from[temp]
    return path


def neighbours(grid, node):
    neigh = []
    if ((0 <= (node[0]+1) < width) and (0 <= (node[1]) < height)):
        neigh.append(((node[0]+1), (node[1])))
    if ((0 <= (node[0]-1) < width) and (0 <= (node[1]) < height)):
        neigh.append(((node[0]-1), (node[1])))
    if ((0 <= (node[0]) < width) and (0 <= (node[1]+1) < height)):
        neigh.append(((node[0]), (node[1]+1)))
    if ((0 <= (node[0]) < width) and (0 <= (node[1]-1) < height)):
        neigh.append(((node[0]), (node[1]-1)))

    return neigh


def heuristic(goal, node):
    (x1, y1) = goal
    (x2, y2) = node
    return abs(x1-x2) + abs(y1-y2)


class PriorityQueue:
    def __init__(self):
        self.elements = []

    def empty(self):
        return len(self.elements) == 0

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]


if __name__ == "__main__":
    main()
