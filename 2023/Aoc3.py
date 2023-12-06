statusGrid = []
def main():
    with open("input3.txt") as file:
        lines = file.read().splitlines()

    print("Part One:", partOne(lines))
    print("Part Two:", partTwo(lines))

def partOne(lines: list[list[str]]):
    fillGrid(lines)
    numbers = []
    for x in range(0, len(lines)):
        for y in range(0, len(lines[0])):
            if(lines[x][y].isdigit() and statusGrid[x][y] and isPartNo(lines, x, y)):
                number, highIndex, lowIndex, _ = getNumber(lines, x, y)
                markAsDone(x, highIndex, lowIndex)
                numbers.append(number)
    return sum(numbers)

def partTwo(lines):
    fillGrid(lines)
    numbers = []
    for x in range(0, len(lines)):
        for y in range(0, len(lines[0])):
            if lines[x][y] == "*":
                numbers.append(getGear(lines, x, y))
    return sum(numbers)

def isPartNo(lines, x, y):
    neighbours = getNeighbours(lines, x, y).keys()
    return not all(char.isdigit() or char == '.' for char in neighbours)

def getGear(lines, x, y):
    numbers = []
    neighbours = getNeighbours(lines, x, y)
    for key in neighbours:
        if key.isdigit():
            for pos in neighbours[key]:
                number = getNumber(lines, pos[0], pos[1])
                numbers.append(number)
    uniqueaValues = set(numbers)
    if len(uniqueaValues) == 2 and statusGrid[x][y]:
        val1 = list(uniqueaValues)[0]
        val2 = list(uniqueaValues)[1]
        markAsDone(val1[3], val1[1], val1[2])
        markAsDone(val2[3], val2[1], val2[2])
        return val1[0] * val2[0]
    return 0

def getNeighbours(lines, x, y):
    neighbours = {}
    height = len(lines)-1
    width = len(lines[0])-1
    if x < height:
        addValue(neighbours, lines[x+1][y], (x+1,y))
    if y < width:
        addValue(neighbours, lines[x][y+1], (x,y+1))
    if x > 0:
        addValue(neighbours, lines[x-1][y], (x-1,y))
    if y > 0:
        addValue(neighbours, lines[x][y-1], (x,y-1))
    if x < height and y < width:
        addValue(neighbours, lines[x+1][y+1], (x+1,y+1))
    if x > 0 and y > 0:
        addValue(neighbours, lines[x-1][y-1], (x-1,y-1))
    if x < height and y > 0:
        addValue(neighbours, lines[x+1][y-1], (x+1,y-1))
    if x > 0 and y < width:
        addValue(neighbours, lines[x-1][y+1], (x-1,y+1))

    return neighbours

def addValue(dictionary, key, val):
    if key in dictionary:
        dictionary[key].append(val)
    else:
        dictionary[key] = [val]

def getNumber(lines: list[list[str]], x, y):
    number = 0
    lowIndex = y
    highIndex = y
    for i in range(y, len(lines[x])):
        if not lines[x][i].isdigit():
            break
        highIndex = i
    for i in range(y, -1, -1):
        if not lines[x][i].isdigit():
            break
        lowIndex = i
    number = lines[x][lowIndex:highIndex+1]
    return (int(number), lowIndex, highIndex, x)

def markAsDone(x, lowIndex, highIndex):
    for i in range(lowIndex, highIndex+1):
        statusGrid[x][i] += -1

def fillGrid(lines):
    global statusGrid
    statusGrid = []
    for line in lines:
        statusGrid.append([1] * len(line))

if __name__ == "__main__":
    main()
