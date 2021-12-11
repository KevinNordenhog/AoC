from operator import itemgetter


def main():
    with open("input8.txt") as file:
        lines = file.read().splitlines()
    vals = [line.split(' | ') for line in lines]
    print("Part one:", partOne(vals))
    print("Part two:", PartTwo(vals))


def partOne(vals):
    cnt = 0
    for val in vals:
        cnt += sum(1 for exp in val[1].split() if len(exp) in (2, 4, 3, 7))
    return cnt


def PartTwo(vals):
    output = 0
    for val in vals:
        cipher = ["" for _ in range(7)]
        mapping = getCharacterCntMapping(val[0].split())
        cipher[0] = getIndex0(mapping)
        cipher[1] = getIndex1(mapping)
        cipher[2] = getIndex2(mapping)
        cipher[3] = getIndex3(mapping)
        cipher[4] = getIndex4(mapping)
        cipher[5] = getIndex5(mapping)
        cipher[6] = getIndex6(mapping)
        output += getNumber(val[1], cipher)
    return output


def getNumber(val, cipher):
    number = ""
    zero = ''.join(c for c in cipher if cipher.index(c) in [0, 1, 2, 4, 5, 6])
    one = ''.join(c for c in cipher if cipher.index(c) in [2, 5])
    two = ''.join(c for c in cipher if cipher.index(c) in [0, 2, 3, 4, 6])
    three = ''.join(c for c in cipher if cipher.index(c) in [0, 2, 3, 5, 6])
    four = ''.join(c for c in cipher if cipher.index(c) in [1, 2, 3, 5])
    five = ''.join(c for c in cipher if cipher.index(c) in [0, 1, 3, 5, 6])
    six = ''.join(c for c in cipher if cipher.index(c) in [0, 1, 3, 4, 5, 6])
    seven = ''.join(c for c in cipher if cipher.index(c) in [0, 2, 5])
    eight = ''.join(c for c in cipher)
    nine = ''.join(c for c in cipher if cipher.index(c) in [0, 1, 2, 3, 5, 6])
    for entry in val.split():
        if sameScrambledString(entry, zero):
            number += "0"
        elif sameScrambledString(entry, one):
            number += "1"
        elif sameScrambledString(entry, two):
            number += "2"
        elif sameScrambledString(entry, three):
            number += "3"
        elif sameScrambledString(entry, four):
            number += "4"
        elif sameScrambledString(entry, five):
            number += "5"
        elif sameScrambledString(entry, six):
            number += "6"
        elif sameScrambledString(entry, seven):
            number += "7"
        elif sameScrambledString(entry, eight):
            number += "8"
        elif sameScrambledString(entry, nine):
            number += "9"
    return int(number)


def mapIndexValues(a, b):
    out = map(a.__getitem__, list(b))
    return ''.join(list(out))


def getIndex0(mapping):
    # 1&7 ger oss aaaa
    one = mapping.get(2)[0]
    seven = mapping.get(3)[0]
    return stringDiff(one, seven)


def getIndex1(mapping):
    # 1&3&4 ger oss bb och ddd
    one = mapping.get(2)[0]
    three = "".join(word for word in mapping.get(5)
                    if containsAll(word, one))
    four = mapping.get(4)[0]
    return stringDiff(three, four+getIndex0(mapping)+getIndex6(mapping))


def getIndex2(mapping):
    # 9&6&0&1 (det som saknas i sexan) ger oss cc och ff
    one = mapping.get(2)[0]
    six = "".join(word for word in mapping.get(6)
                  if not containsAll(word, one))
    eight = mapping.get(7)[0]
    return stringDiff(six, eight)


def getIndex3(mapping):
    one = mapping.get(2)[0]
    four = mapping.get(4)[0]
    return stringDiff(one+getIndex1(mapping), four)


def getIndex4(mapping):
    # 9&8 ger oss eee
    four = mapping.get(4)[0]
    nine = "".join(word for word in mapping.get(6) if containsAll(word, four))
    eight = mapping.get(7)[0]
    return stringDiff(nine, eight)


def getIndex5(mapping):
    # Index2 och ett löser ff
    one = mapping.get(2)[0]
    return stringDiff(one, getIndex2(mapping))


def getIndex6(mapping):
    # 4&9 (bara 9:an delar med 4:an) ger oss gggg (har redan aaa, cipher[0])
    four = mapping.get(4)[0]
    nine = "".join(word for word in mapping.get(6) if containsAll(word, four))
    return stringDiff(four+getIndex0(mapping), nine)


def getCharacterCntMapping(words):
    mapping = {}
    for word in words:
        mapping.setdefault(len(word), []).append(word)
    return mapping


def stringDiff(s1, s2):
    return "".join(set(s2).symmetric_difference(set(s1)))


def containsAny(str, set):
    for c in set:
        if c in str:
            return 1
    return 0


def containsAll(str, set):
    for c in set:
        if c not in str:
            return 0
    return 1


def sameScrambledString(str1, str2):
    return sorted(str1) == sorted(str2)


if __name__ == "__main__":
    main()
