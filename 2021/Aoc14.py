import collections
from itertools import count
from tempfile import tempdir


def main():
    with open("input14.txt") as file:
        lines = file.read().splitlines()
    seq = lines[0]
    charMap = toDict([line.split(' -> ') for line in lines[2:]])
    print("Part One:", partOne(charMap, seq))
    seq = lines[0]
    print("Part Two:", partTwo(charMap, seq))


def partOne(charMap, seq):
    for i in range(10):
        seq = applyTemplate(charMap, seq)
    mostCommon = collections.Counter(seq).most_common()[0]
    leastCommon = collections.Counter(seq).most_common()[-1]
    print("MC", mostCommon)
    print("LC", leastCommon)
    return mostCommon[1] - leastCommon[1]


def partTwo(charMap: dict, seq: str):
    print(seq)
    counts = getCounts(charMap, seq)

    seqCounts = getCharCountDictFromString(seq)

    for i in range(40):
        counts, seqCounts = countOccurence(charMap, counts, seqCounts)

    print(seqCounts)

    indvCounts = getCharCountDict(seqCounts)
    mostCommon = max(indvCounts, key=indvCounts.get)
    leastCommon = min(indvCounts, key=indvCounts.get)
    print("MC", mostCommon)
    print("LC", leastCommon)
    return indvCounts[mostCommon] - indvCounts[leastCommon]


def applyTemplate(charMap: dict, seq: str):
    temp = seq
    roof = len(seq)
    addedValues = 0
    for i in range(1, roof):
        val = temp[i-1] + temp[i]
        if val in charMap:
            seq = seq[:(i+addedValues)] + charMap[val] + seq[(i+addedValues):]
            addedValues += 1
    return seq


def countOccurence(charMap: dict, counts: dict, seqCounts: dict()):
    added = dict()
    removed = dict()
    for key in counts:
        if key in charMap:
            left = key[0] + charMap[key]
            right = charMap[key] + key[1]
            added[left] = added.get(
                left, 0) + counts[key]
            added[right] = added.get(
                right, 0) + counts[key]
            seqCounts[charMap[key]] = seqCounts.get(
                charMap[key], 0) + counts[key]
            removed[key] = removed.get(
                key, 0) + counts[key]
    # print("SeqCounts", seqCounts)
    # print("Counts: ", counts)
    # print("Added: ", added)
    # print("Removed: ", removed)
    # print()

    for key in added:
        counts[key] = counts.get(key, 0) + added.get(key, 0)
    for key in removed:
        counts[key] = counts.get(key, 0) - removed.get(key, 0)

    return counts, seqCounts


def toDict(charMap: list[list[str]]):
    charDict = dict()
    for chars in charMap:
        charDict[chars[0]] = chars[1]
    return charDict


def getCounts(charMap: dict, seq: str):
    counts = dict()

    for i in range(len(seq)-1):
        counts[seq[i:i+2]] = counts.get(seq[i:i+2], 0) + 1

    for pair in charMap:
        counts[pair] = counts.get(pair, 0)
    return counts


def getCharCountDict(counts: dict):
    indvCounts = dict()
    for charPair in counts:
        for char in charPair:
            indvCounts[char] = indvCounts.get(char, 0) + counts[charPair]
    return indvCounts


def getCharCountDictFromString(seq: str):
    counts = dict()
    for char in seq:
        counts[char] = counts.get(char, 0) + 1
    return counts


if __name__ == "__main__":
    main()
