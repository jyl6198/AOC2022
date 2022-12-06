def part_1(stack, move_list):
    for move in move_list:
        # adjust index
        num_of_crates_moved, move[1], move[2] = move[0], move[1]-1, move[2]-1
        for _ in range(num_of_crates_moved):
            # check if stack is empty or has a crate
            if stack[move[1]]:
                crate = stack[move[1]].pop()
                stack[move[2]].append(crate)
    return ''.join([crate[-1] for crate in stack])


def part_2(stack, move_list):
    for move in move_list:
        num_of_crates_moved, move[1], move[2] = move[0], move[1]-1, move[2]-1
        if stack[move[1]]:
            crates_moved = stack[move[1]][-num_of_crates_moved:]
            stack[move[1]] = stack[move[1]][:-num_of_crates_moved]
            stack[move[2]] += crates_moved
    return ''.join([crate[-1] for crate in stack])


def main():
    with open("input.txt", "r") as file:
        data = file.read().splitlines()
        crates, moves = data[:8], data[10:]
        stack = [[] for _ in range(len(crates)+1)]
        for crate in crates:
            # every 4 is a crate w/ a character inside
            for i in range(0, len(crate), 4):
                crate_num = i // 4
                container = crate[i:i+4]
                if container[1] != ' ':
                    stack[crate_num].append(container[1])
        # pop in way we want stack to pop
        stack = [crate[::-1] for crate in stack]

        move_list = []
        for move in moves:
            nums = [int(num) for num in move.split() if num.isdigit()]
            move_list.append(nums)
        #print(part_1(stack, move_list))
        print(part_2(stack, move_list))


if __name__ == "__main__":
    main()
