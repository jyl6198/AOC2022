def part_1(x1, x2, y1, y2):
    count = 0
    if (y1 >= x1 and y2 <= x2) or (x1 >= y1 and x2 <= y2):
        count += 1
    return count


def part_2(x1, x2, y1, y2):
    count = 0
    if (y1 <= x1 <= y2) or (x1 <= y1 <= x2):
        count += 1
    return count


def main():
    with open("day4_input.txt", "r") as file:
        containing_pairs, overlapping_pairs = 0, 0
        for line in file.readlines():
            first_pair, second_pair = line.strip().split(',')
            x1, x2 = [int(x) for x in first_pair.split('-')]
            y1, y2 = [int(y) for y in second_pair.split('-')]
            containing_pairs += part_1(x1, x2, y1, y2)
            overlapping_pairs += part_2(x1, x2, y1, y2)
        print('Part 1:', containing_pairs, 'Part 2:', overlapping_pairs)


if __name__ == "__main__":
    main()
