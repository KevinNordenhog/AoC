START = "start"
END = "end"


def main():
    with open("input12.txt") as file:
        lines = file.read().splitlines()
    map = [line.split('-') for line in lines]
    print("Part one:", partOne(map))
    print("Part two:", partTwo(map))


def partOne(map):
    paths = stepAll(map, [[START]])
    return len(paths)


def partTwo(map):
    paths = stepAll(map, [[START]], True)
    return len(paths)


def stepAll(map: list[list], paths: list[list], p2=False):
    newPaths = []
    for path in paths:
        if path[-1] == END:
            continue
        newPaths += step(map, path, p2)
        paths.remove(path)

    paths.extend(newPaths)
    paths = removeDublicates(paths)

    if any([path[-1] != END for path in paths]):
        paths = stepAll(map, paths, p2)

    return paths


def step(mapp: list[list], path: list, p2: bool):
    newPaths = []
    currentStep = path[-1]
    if currentStep != END:
        nextSteps = [m[m.index(currentStep)-1]
                     for m in mapp if currentStep in m]
        for next in nextSteps:
            if next != START and canAdd(path, next, p2):
                newPaths.append(path + [next])
    return newPaths


def canAdd(path: list[str], step: str, p2: bool):
    p2Ok = False
    if p2:
        p2Ok = step.isupper() or step not in path or not any(
            lc.islower() and path.count(lc) > 1 for lc in path)
    return step.isupper() or step not in path or p2Ok


def removeDublicates(paths: list[list]):
    k = sorted(paths)
    return [k[i] for i in range(len(k)) if i == 0 or k[i] != k[i-1]]


if __name__ == "__main__":
    main()
