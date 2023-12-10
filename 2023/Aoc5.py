cards = {}


def main():
    with open("input5.txt") as file:
        lines = file.read().splitlines()
    maps = getMapValues(lines)
    print("Part One:", partOne(maps))
    print("Part Two:", partTwo())


def partOne(maps):
    return maps


def partTwo():
    return 0


def getMapValues(lines):
    maps = {}
    current_map = None
    for line in lines:
        if ":" in line:
            mapping = line.split(":")
            current_map = mapping[0]
            if mapping[1] != "":
                maps[current_map] = [int(val) for val in mapping[1].split()]

        elif current_map and line != '':
            values = [int(val) for val in line.split()]
            addValue(maps, current_map, values)
    return maps


def addValue(dictionary, key, val):
    if key in dictionary:
        dictionary[key].append(val)
    else:
        dictionary[key] = [val]


if __name__ == "__main__":
    main()
