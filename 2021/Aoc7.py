def main():
    with open("input7.txt") as file:
        vals = list(map(int, file.read().split(',')))
    print("Part one:", calcTotalFuel(vals, True))
    print("Part two:", calcTotalFuel(vals))


def calcTotalFuel(vals, inc=False):
    lastSum = 99 ** 20
    for align in range(max(vals)):
        fuel = 0
        for val in vals:
            fuel += sum(range(abs(val-align)*inc, abs(val-align)+1))
        if fuel < lastSum:
            lastSum = fuel
        else:
            return lastSum


if __name__ == "__main__":
    main()
