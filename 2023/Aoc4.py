cards = {}


def main():
    with open("input4.txt") as file:
        lines = file.read().splitlines()
    splitLines = [line.replace(" | ", ": ").split(": ") for line in lines]
    for card in splitLines:
        cards[int(card[0][4:])] = (card[1].split(), card[2].split())
    print("Part One:", partOne())
    print("Part Two:", partTwo())


def partOne():
    points = 0
    for game in cards:
        winningNumberCount = getWinningNumberCount(game)
        if winningNumberCount > 2:
            points += 2 ** (winningNumberCount-1)
        else:
            points += winningNumberCount
    return points


def partTwo():
    counts = {}
    for game in cards:
        addValue(counts, game, 1)
        gamePoints = getWinningNumberCount(game)
        for i in range(1, gamePoints+1):
            addValue(counts, game+i, 1*counts[game])
    return sum([val for val in counts.values()])


def getWinningNumberCount(game):
    winningNumberCount = 0
    for number in cards[game][0]:
        if number in cards[game][1]:
            winningNumberCount += 1
    return winningNumberCount


def addValue(dictionary, key: int, val):
    if key in dictionary:
        dictionary[key] += val
    else:
        dictionary[key] = val


if __name__ == "__main__":
    main()
