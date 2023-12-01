with open("input1.txt") as file:
    lines = file.read().splitlines()
    numbers = list(map(int,lines))

    print(sum([numbers[i] < numbers[i+1] for i in range(len(numbers)-1)]))
    print(sum([sum(numbers[i:i+3]) < sum(numbers[i+1:i+4]) for i in range(len(numbers)-1)]))