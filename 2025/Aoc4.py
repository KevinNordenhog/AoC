# --- Day 4: Printing Department ---
# You ride the escalator down to the printing department. They're clearly getting ready for Christmas; they have lots of large rolls of paper everywhere, and there's even a massive printer in the corner (to handle the really big print jobs).
#
# Decorating here will be easy: they can make their own decorations. What you really need is a way to get further into the North Pole base while the elevators are offline.
#
# "Actually, maybe we can help with that," one of the Elves replies when you ask for help. "We're pretty sure there's a cafeteria on the other side of the back wall. If we could break through the wall, you'd be able to keep moving. It's too bad all of our forklifts are so busy moving those big rolls of paper around."
#
# If you can optimize the work the forklifts are doing, maybe they would have time to spare to break through the wall.
#
# The rolls of paper (@) are arranged on a large grid; the Elves even have a helpful diagram (your puzzle input) indicating where everything is located.
#
# For example:
#
# ..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.
# The forklifts can only access a roll of paper if there are fewer than four rolls of paper in the eight adjacent positions. If you can figure out which rolls of paper the forklifts can access, they'll spend less time looking and more time breaking down the wall to the cafeteria.
#
# In this example, there are 13 rolls of paper that can be accessed by a forklift (marked with x):
#
# ..xx.xx@x.
# x@@.@.@.@@
# @@@@@.x.@@
# @.@@@@..@.
# x@.@@@@.@x
# .@@@@@@@.@
# .@.@.@.@@@
# x.@@@.@@@@
# .@@@@@@@@.
# x.x.@@@.x.
# Consider your complete diagram of the paper roll locations. How many rolls of paper can be accessed by a forklift?
#
# --- Part Two ---
# Now, the Elves just need help accessing as much of the paper as they can.
#
# Once a roll of paper can be accessed by a forklift, it can be removed. Once a roll of paper is removed, the forklifts might be able to access more rolls of paper, which they might also be able to remove. How many total rolls of paper could the Elves remove if they keep repeating this process?
#
# Starting with the same example as above, here is one way you could remove as many rolls of paper as possible, using highlighted @ to indicate that a roll of paper is about to be removed, and using x to indicate that a roll of paper was just removed:
#
# Initial state:
# ..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# @.@@@@..@.
# @@.@@@@.@@
# .@@@@@@@.@
# .@.@.@.@@@
# @.@@@.@@@@
# .@@@@@@@@.
# @.@.@@@.@.
#
# Remove 13 rolls of paper:
# ..xx.xx@x.
# x@@.@.@.@@
# @@@@@.x.@@
# @.@@@@..@.
# x@.@@@@.@x
# .@@@@@@@.@
# .@.@.@.@@@
# x.@@@.@@@@
# .@@@@@@@@.
# x.x.@@@.x.
#
# Remove 12 rolls of paper:
# .......x..
# .@@.x.x.@x
# x@@@@...@@
# x.@@@@..x.
# .@.@@@@.x.
# .x@@@@@@.x
# .x.@.@.@@@
# ..@@@.@@@@
# .x@@@@@@@.
# ....@@@...
#
# Remove 7 rolls of paper:
# ..........
# .x@.....x.
# .@@@@...xx
# ..@@@@....
# .x.@@@@...
# ..@@@@@@..
# ...@.@.@@x
# ..@@@.@@@@
# ..x@@@@@@.
# ....@@@...
#
# Remove 5 rolls of paper:
# ..........
# ..x.......
# .x@@@.....
# ..@@@@....
# ...@@@@...
# ..x@@@@@..
# ...@.@.@@.
# ..x@@.@@@x
# ...@@@@@@.
# ....@@@...
#
# Remove 2 rolls of paper:
# ..........
# ..........
# ..x@@.....
# ..@@@@....
# ...@@@@...
# ...@@@@@..
# ...@.@.@@.
# ...@@.@@@.
# ...@@@@@x.
# ....@@@...
#
# Remove 1 roll of paper:
# ..........
# ..........
# ...@@.....
# ..x@@@....
# ...@@@@...
# ...@@@@@..
# ...@.@.@@.
# ...@@.@@@.
# ...@@@@@..
# ....@@@...
#
# Remove 1 roll of paper:
# ..........
# ..........
# ...x@.....
# ...@@@....
# ...@@@@...
# ...@@@@@..
# ...@.@.@@.
# ...@@.@@@.
# ...@@@@@..
# ....@@@...
#
# Remove 1 roll of paper:
# ..........
# ..........
# ....x.....
# ...@@@....
# ...@@@@...
# ...@@@@@..
# ...@.@.@@.
# ...@@.@@@.
# ...@@@@@..
# ....@@@...
#
# Remove 1 roll of paper:
# ..........
# ..........
# ..........
# ...x@@....
# ...@@@@...
# ...@@@@@..
# ...@.@.@@.
# ...@@.@@@.
# ...@@@@@..
# ....@@@...
# Stop once no more rolls of paper are accessible by a forklift. In this example, a total of 43 rolls of paper can be removed.
#
# Start with your original diagram. How many rolls of paper in total can be removed by the Elves and their forklifts?

def partOne(lines):
    copyoflines = lines.copy()
    xMax = len(lines[0])
    yMax = len(lines)
    count = 0
    for y in range(0,yMax):
        for x in range(0, xMax):
            if (lines[y][x] == "."):
                continue
            neighbors = numberOfNeighbors(lines, x, y, xMax, yMax)
            if (neighbors < 4):
                count += 1
                copyoflines[y] = copyoflines[y][:x] + "x" + copyoflines[y][x+1:]

    return count

def partTwo(lines):
    xMax = len(lines[0])
    yMax = len(lines)
    count = 0
    done = False
    while (not done):
        done = True
        for y in range(0,yMax):
            for x in range(0, xMax):
                if (lines[y][x] == "."):
                    continue
                neighbors = numberOfNeighbors(lines, x, y, xMax, yMax)
                if (neighbors < 4):
                    count += 1
                    lines[y] = lines[y][:x] + "." + lines[y][x+1:]
                    done = False

    return count

def numberOfNeighbors(lines: list[str], x: int, y: int, xMax: int, yMax: int):
    neigh = 0
    for i in range(y-1, y+2):
        for j in range(x-1, x+2):
            if (i < 0 or j < 0 or i >= yMax or j >= xMax or (i == y and j == x)):
                continue
            if (lines[i][j] == "@"):
                neigh += 1
    return neigh

def runTest():
    testValuesPartOne = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

    testlines = testValuesPartOne.splitlines()
    partOneResult = partOne(testlines)
    assert partOneResult == 13, "got result: {}".format(partOneResult)

    partTwoResult = partTwo(testlines)
    assert partTwoResult == 43, "got result: {}".format(partTwoResult)
