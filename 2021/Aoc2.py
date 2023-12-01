def main():
    with open("input2.txt") as file:
        lines = file.read().splitlines()
    partOneNaive(lines)
    partOneShort(lines)
    partTwo(lines)


def partOneShort(lines):
    print(
        sum([int(line[-1]) for line in lines if line.startswith("forward")])
        *(sum([int(line[-1]) for line in lines if line.startswith("down")])
            -sum([int(line[-1]) for line in lines if line.startswith("up")]))
    )

def partOneNaive(lines):
    depth = 0
    pos = 0
    for line in lines:
        dir,x = line.split()
        if dir == "forward":
            pos += int(x)
        elif dir == "down":
            depth += int(x)
        elif dir == "up":
            depth -= int(x)
    print(depth*pos)

def partTwo(lines):
    depth = 0
    pos = 0
    aim = 0
    for line in lines:
        dir,x = line.split()
        if dir == "forward":
            pos += int(x)
            depth += aim*int(x)
        elif dir == "down":
            aim += int(x)
        elif dir == "up":
            aim -= int(x)
    print(depth*pos)

if __name__ == "__main__":
    main()