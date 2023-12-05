import re
numbers = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def aoc():
    with open("input1.txt") as file:
        lines = file.read().splitlines()
        nums = []
        nums2 = []
        for line in lines:
            num = ''.join(char for char in line if char.isdigit())
            nums.append(int(num[0]+num[-1]))
            nums2.append(findDigits(line))
        print(sum(nums))
        print(sum(nums2))

def findDigits(string):
    numbersInString = [(string[i], i) for i in range(0, len(string)) if string[i].isdigit()]
    for number in numbers:
        if number in string:
            numbersInString.extend([(number, m.start()) for m in re.finditer(number, string)])
    highestNumber = ('',-1)
    lowestNumber = ('',999)
    for number in numbersInString:
        i = number[1]
        if i < lowestNumber[1]:
            lowestNumber = number
        if i > highestNumber[1]:
            highestNumber = number
    return getSum(lowestNumber, highestNumber)

def getSum(firstNumber: tuple[str, int], secondNumber: tuple[str, int]):
    return int(getNumber(firstNumber[0]) + getNumber(secondNumber[0]))

def getNumber(string):
    if string.isdigit():
        return string
    else:
        return str(numbers.index(string))

aoc()
#P1 54990
#P2 54473