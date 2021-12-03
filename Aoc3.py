def main():
    with open("input3.txt") as file:
        lines = file.read().splitlines()
    partOne(lines)

def partOne(lines):
    bits = ''.join([('1' if [line[i] for line in lines].count('1') > 500 else '0') for i in range(len(lines[0]))])
    inv = ''.join('1' if b == '0' else '0' for b in bits)
    print(int(bits,2)*int(inv,2))

if __name__ == "__main__":
    main()