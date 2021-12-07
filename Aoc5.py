SIZE = 1000
def main():
    with open("input5.txt") as file:
        lines = file.read().splitlines()
    vals = [line.split(' -> ') for line in lines]
    print(partOne(vals))
    print(partTwo(vals))


def partOne(vals):
    matrix = createMatrix()
    for val in vals:
        matrix = addValuesToMatrix(val, matrix)

    return sum([sum(row) for row in matrix])

def partTwo(vals):
    return 0

def addValuesToMatrix(val, matrix, diagonal = False):
    x1, y1 = list(map(int, val[0].split(',')))
    x2, y2 = list(map(int, val[1].split(',')))

    if x1 == x2:
        if y1 < y2:
            for i in  range(y1,y2+1):
                matrix[x1][i] = matrix[x1][i]+(matrix[x1][i] < 1) if matrix[x1][i] is not False else 0
                #matrix[x1][i] += 1
        else:
            for i in  range(y1,y2-1,-1):
                matrix[x1][i] = matrix[x1][i]+(matrix[x1][i] < 1) if matrix[x1][i] is not False else 0
                #matrix[x1][i] += 1

    elif y1 == y2:
        if x1 < x2:
            for i in  range(x1,x2+1):
                matrix[i][y1] = matrix[i][y1]+(matrix[i][y1] < 1) if matrix[i][y1] is not False else 0
                #matrix[i][y1] += 1
        else:
            for i in  range(x1,x2-1, -1):
                matrix[i][y1] = matrix[i][y1]+(matrix[i][y1] < 1) if matrix[i][y1] is not False else 0
                #matrix[i][y1] += 1
    # if diagonal and abs(x1-x2) == abs(y1-y2):
    #     for i in range(abs(x1-x2)):
    #         matrix[i][y1] = matrix[i][y1]+(matrix[i][y1] < 1) if matrix[i][y1] is not False else 0
    return matrix

def createMatrix():
    return [[False for _ in range(SIZE) ]for _ in range(SIZE)]
    #return [[0 for _ in range(SIZE) ]for _ in range(SIZE)]

if __name__ == "__main__":
    main()

#P1 8350
