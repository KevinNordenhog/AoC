def main():
    with open("input6.txt") as file:
        vals = list(map(int, file.read().split(',')))
    print(partTwo(vals))
    print(partOne(vals))

def partOne(vals):
    for _ in range(80):
        zeroCnt = vals.count(0)
        for j in range(len(vals)):
            vals[j] = vals[j]-1 if vals[j] > 0 else 6
        vals.extend([8 for _ in range(zeroCnt)])
    return len(vals)

def partTwo(vals):
    numberCnt = [ vals.count(i) for i in range(7)]
    new = [0,0]
    print(sum(numberCnt))
    for i in range(256):
        add = numberCnt[0]
        numberCnt = numberCnt[1:] + numberCnt[:1]
        numberCnt[-1] = numberCnt[-1] + new[0]
        new[0] = new[1]
        new[1] = add

    return sum(numberCnt+new)

if __name__ == "__main__":
    main()