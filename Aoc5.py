def main():
    with open("input5.txt") as file:
        lines = file.read().splitlines()
    vals = [line.split(' -> ') for line in lines]
    print(partOne(vals))
    print(partTwo(vals))


def partOne(vals):
    return vals


def partTwo(vals):
    return 0


if __name__ == "__main__":
    main()
