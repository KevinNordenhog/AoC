def main():
    with open("input4.txt") as file:
        lines = file.read().splitlines()
    seq = lines[0].split(',')
    boards = getBoards(lines[1:])
    print(partOne(seq, boards))
    print(partTwo(seq, boards))


def partOne(seq, boards):
    for num in seq:
        for board in boards:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if num == board[i][j]:
                        board[i][j] = board[i][j] + "+"
                        if checkBoard(board):
                            return calcBoard(board, num)


def partTwo(seq, boards):
    maxSeqIndex = 0
    lastBoard = []
    for board in boards:
        boardDone = False
        for num in seq:
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if num == board[i][j]:
                        board[i][j] = board[i][j] + "+"
                        if checkBoard(board):
                            boardDone = True
                            if seq.index(num) > maxSeqIndex:
                                maxSeqIndex = seq.index(num)
                                lastBoard = board
            if boardDone:
                break
    return calcBoard(lastBoard, seq[maxSeqIndex])


def checkBoard(board):
    cols = [([row[i] for row in board]) for i in range(len(board[0]))]
    return any([all([x.endswith('+') for x in col]) for col in cols]
               ) or any([all([x.endswith('+') for x in row])for row in board])


def calcBoard(board, num):
    numbers = [int(x) for row in board for x in row if not x.endswith('+')]
    return sum(numbers)*int(num)


def getBoards(lines):
    boards = [[]]
    i = 0
    for line in lines[1:]:
        if line == '':
            i += 1
            boards.append([])
            continue
        boards[i].append(line.split())
    return boards


if __name__ == "__main__":
    main()
