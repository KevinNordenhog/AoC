def main():
    with open("input2.txt") as file:
        lines = file.read().splitlines()

    print("Part One:", partOne(lines))
    print("Part Two:", partTwo(lines))

def partOne(lines):
    numberOfCubes = {"red": 12, "green": 13, "blue": 14}
    possibleIds = []
    for line in lines:
        (game,cubess) = line.split(": ")
        gameNo = game[4:]
        sets = cubess.split("; ")
        gamePossible = True
        for set in sets:
            cubes = set.split(", ")
            for cube in cubes:
                (amount,color) = cube.split(' ')
                if int(amount) >  numberOfCubes[color]:
                    gamePossible = False
        if gamePossible:
            possibleIds.append(int(gameNo))
    return sum(possibleIds)

def partTwo(lines):
    power = []
    for line in lines:
        numberOfCubes = {"red": 0, "green": 0, "blue": 0}
        (_,cubess) = line.split(": ")
        sets = cubess.split("; ")
        for set in sets:
            cubes = set.split(", ")
            for cube in cubes:
                (amount,color) = cube.split(' ')
                if int(amount) >  numberOfCubes[color]:
                    numberOfCubes[color] = int(amount)
        power.append(multiply(numberOfCubes.values()))
    return sum(power)

def multiply(list):
    result = 1
    for x in list:
        result = result * x
    return result

if __name__ == "__main__":
    main()
