def main():
    with open("input6.txt") as file:
        vals = list(map(int, file.read().split(',')))
    print("Part one:", fishCount(vals, 80))
    print("Part two:", fishCount(vals, 256))


def fishCount(vals, days):
    numberCnt = [vals.count(i) for i in range(9)]
    for i in range(days):
        add = numberCnt[0]
        numberCnt = numberCnt[1:7] + numberCnt[:1] + numberCnt[-2:]
        numberCnt[6] += numberCnt[7]
        numberCnt[7] = numberCnt[8]
        numberCnt[8] = add
    return sum(numberCnt)


if __name__ == "__main__":
    main()
