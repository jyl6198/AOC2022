def part_1(guide):
    with open("day2_input.txt", "r") as file:
        score = 0
        for line in file.readlines():
            opp, player = line.strip().split(' ')
            score += guide[opp][player] + guide[player]
    return score


def part_2(guide):
    with open("day2_input.txt", "r") as file:
        score = 0
        for line in file.readlines():
            opp, player = line.strip().split(' ')
            score += guide[opp][player] + guide[player]
    return score


def main():
    guide_1 = {
        "A": {
            "X": 3,
            "Y": 6,
            "Z": 0
        },
        "B": {
            "X": 0,
            "Y": 3,
            "Z": 6
        },
        "C": {
            "X": 6,
            "Y": 0,
            "Z": 3
        },
        "X": 1, "Y": 2, "Z": 3
    }
    print(part_1(guide_1))

    guide_2 = {
        "A": {
            "X": 3,
            "Y": 1,
            "Z": 2
        },
        "B": {
            "X": 1,
            "Y": 2,
            "Z": 3
        },
        "C": {
            "X": 2,
            "Y": 3,
            "Z": 1
        },
        "X": 0, "Y": 3, "Z": 6
    }
    print(part_2(guide_2))


if __name__ == "__main__":
    main()
