openMap = {")": "(", "]": "[", "}": "{", ">": "<"}
closingMap = {"(": ")", "[": "]", "{": "}", "<": ">"}
charValues = {")": 3, "]": 57, "}": 1197, ">": 25137}
charValues2 = {")": 1, "]": 2, "}": 3, ">": 4}


def main():
    with open("input10.txt") as file:
        lines = file.read().splitlines()
    missingChars, illegalChars = getIllegalAndMissingCharacters(lines)
    print("Part one:", sum([charValues[char] for char in illegalChars]))
    print("Part two:", getMiddleScore(missingChars))


def getIllegalAndMissingCharacters(lines):
    illegalChars = []
    missingChars = []
    for line in lines:
        corrupted = False
        chars = []
        for c in line:
            if c in ("(", "[", "{", "<"):
                chars.append(c)
            elif openMap[c] == chars[-1]:
                chars.pop()
            else:
                illegalChars.append(c)
                corrupted = True
                break
        if not corrupted:
            missingChars.append([closingMap[c] for c in chars[::-1]])
    return missingChars, illegalChars


def getMiddleScore(missingChars):
    scores = []
    for chars in missingChars:
        score = 0
        for c in chars:
            score = score * 5 + charValues2[c]
        scores.append(score)
    scores.sort()
    return scores[int(len(scores)/2)]


if __name__ == "__main__":
    main()
