SIZE = 1000


def main():
    with open("input6.txt") as file:
        vals = list(map(int, file.read().split(',')))
    print(partOne(vals))
    print(partTwo(vals))


def partOne(vals):
    for _ in range(80):
        zeroCnt = vals.count(0)
        for j in range(len(vals)):
            vals[j] = vals[j]-1 if vals[j] > 0 else 6
            # if vals[j] == 0:
            #     vals[j] = 6
            # else:
            #     vals[j] -= 1
        vals.extend([8 for _ in range(zeroCnt)])
    return len(vals)


def partTwo(vals):
    return 0


if __name__ == "__main__":
    main()

# P1 376194
