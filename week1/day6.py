def part_1():
    with open("input.txt", "r") as file:
        datastream = file.readline()
        for i in range(4, len(datastream)):
            s = set(datastream[(i-4):i])
            if len(s) == 4:
                print('answer:', datastream[i-4:i], i)
                return i


def part_2():
    with open("input.txt", "r") as file:
        datastream = file.readline()
        for i in range(14, len(datastream)):
            s = set(datastream[(i-14):i])
            if len(s) == 14:
                print('answer:', datastream[i-14:i], i)
                return i


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
