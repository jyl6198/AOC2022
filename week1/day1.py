def part_1():
    with open("day1_input.txt", "r") as file:
        max_cal = 0
        curr_max = 0
        for line in file.readlines():
            curr_line = line.strip()
            if curr_line != '':
                curr_max += int(curr_line)
            else:
                if curr_max > max_cal:
                    max_cal = curr_max
                curr_max = 0
        return max_cal

def part_2():
    with open("day1_input.txt", "r") as file:
        cals = []
        curr_cals = 0
        for line in file.readlines():
            curr_line = line.strip()
            if curr_line != '':
                curr_cals += int(curr_line)
            else:
                cals.append(curr_cals)
                curr_cals = 0
        cals.sort(reverse=True)
    return sum(cals[:3])

def main():
    print(part_1())
    print(part_2())

if __name__ == "__main__":
    main()