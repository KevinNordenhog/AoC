def main():
    with open("input8.txt") as file:
        lines = file.read().splitlines()
    vals = [line.split(' | ') for line in lines]
    print("Part one:", partOne(vals))
    print("Part two:", PartTwo(vals))


def partOne(vals):
    cnt = 0
    for val in vals:
        cnt += sum(1 for exp in val[1].split() if len(exp) in (2,4,3,7))
    return cnt

def PartTwo(vals):
    sum = 0
    for val in vals:
        cipher = ["" for _ in range(7)]
        test = val[0].split()
        mapping = {len(item): item for item in val[0].split()}
        item = mapping.get(3)
        # 1&7 ger oss aaaa
        # 9&6&0&1 (det som saknas i sexan) ger oss cc och ff
        # 1&3&4 ger oss bb och ddd
        # 3&2&5 ger oss eee
        # 4&9 (bara 9:an delar med 4:an) ger oss gggg (har redan aaa)
        # 9&8 ger oss eee
        # bara ggg kvar
        seq = val[0]

    print(test)
    return mapping


if __name__ == "__main__":
    main()

# 1 = 2, 4 = 4, 7 = 3 8 = 7