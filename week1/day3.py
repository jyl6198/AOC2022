def calc_priority(shared):
    sum_prio = 0
    for char in shared:
        sum_prio += ord(char) - 96 if char.islower() else ord(char) - 38
    return sum_prio


def part_1():
    # print(ord("a")-96, ord('z')-96, ord("A")-38, ord("Z")-38)
    with open("day3_input.txt", "r") as file:
        sum_prio = 0
        for line in file.readlines():
            shared_types = []
            first_half = line[:len(line) // 2].strip()
            sec_half = line[len(line) // 2:].strip()
            chars = {}
            for char in first_half:
                chars[char] = chars[char]+1 if char in chars else 1
            for char in sec_half:
                if char in chars and char not in shared_types:
                    shared_types.append(char)
            sum_prio += calc_priority(shared_types)
    return sum_prio


def part_2():
    with open("day3_input.txt", "r") as file:
        shared_types = []
        counter = 1
        chars = {}
        for line in file.readlines():
            for char in line.strip():
                if chars.get(char, 0) == 0 and counter == 1:
                    chars[char] = 1
                else:
                    if chars.get(char, 0) == counter-1:
                        chars[char] += 1
                    if chars.get(char, 0) == 3:
                        shared_types.append(char)
                        counter = 0
                        chars = {}
                        break
            counter += 1
        sum_prio = calc_priority(shared_types)
    return sum_prio


def main():
    print(part_1())
    print(part_2())


if __name__ == "__main__":
    main()
