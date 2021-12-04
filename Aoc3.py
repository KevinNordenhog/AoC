def main():
    with open("input3.txt") as file:
        lines = file.read().splitlines()
    partOne(lines)
    partTwo(lines)


def partOne(lines):
    bits = "".join(
        [
            ("1" if [line[i] for line in lines].count("1") > 500 else "0")
            for i in range(len(lines[0]))
        ]
    )
    inv = "".join("1" if b == "0" else "0" for b in bits)
    print(int(bits, 2) * int(inv, 2))


def partTwo(lines):
    ograte = ogRate(lines)
    co2 = co2Rate(lines)
    print(int(ograte, 2) * int(co2, 2))


def ogRate(lines):
    for i in range(len(lines[0])):
        ones = []
        zeros = []
        for line in lines:
            if line[i] == "1":
                ones.append(line)
            else:
                zeros.append(line)
        lines = ones if len(ones) >= len(zeros) else zeros
        if len(lines) == 1:
            break
    return lines[0]


def co2Rate(lines):
    for i in range(len(lines[0])):
        ones = []
        zeros = []
        for line in lines:
            if line[i] == "1":
                ones.append(line)
            else:
                zeros.append(line)
        lines = ones if len(ones) < len(zeros) else zeros
        if len(lines) == 1:
            break
    return lines[0]


if __name__ == "__main__":
    main()
