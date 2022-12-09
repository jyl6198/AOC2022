class Directory:
    def __init__(self, data=None, parent=None, children=None, files=None):
        if children is None:
            children = []
        self.data = data
        self.parent = parent
        self.children = children
        self.size = 0
        if files is None:
            files = {}
        self.files = files


def getTotalSize(curr_node, size):
    max_size = 100000
    if curr_node.size <= max_size:
        size += curr_node.size
    for child in curr_node.children:
        size = getTotalSize(child, size)
    return size


def part_1(root):
    totalSize = 0
    for child in root.children:
        totalSize += getTotalSize(child, 0)
    return totalSize


def smallestSize(curr_node, directories, space):
    if curr_node.size >= space:
        directories.append(curr_node.size)
    for child in curr_node.children:
        smallestSize(child, directories, space)


def part_2(root):
    totalDiskAvail = 70000000
    unusedSpace = 30000000
    currentFreeSpace = totalDiskAvail-root.size
    neededSpace = unusedSpace-currentFreeSpace

    directories = []
    smallestSize(root, directories, neededSpace)
    return sorted(directories)[0]


def main():
    with open("input.txt", "r") as file:
        root = Directory(data='/')
        curr_dir = root
        for line in file.readlines():
            curr_line = line.split()
            if "cd" in curr_line:
                if curr_line[2] == '..':
                    curr_dir = curr_dir.parent
                else:
                    for child in curr_dir.children:
                        if child.data == curr_line[2]:
                            curr_dir = child
                            break
            elif 'dir' in curr_line:
                curr_dir.children.append(Directory(curr_line[1], curr_dir))
                for child in curr_dir.children:
                    child.parent = curr_dir
            elif 'ls' in curr_line:
                #print("lol ls does nothing blah blah")
                continue
            else:
                file_name, file_size = curr_line[1], int(curr_line[0])
                if file_name not in curr_dir.files:
                    curr_dir.files[file_name] = file_size
                curr_dir.size += file_size
                # this is probably my worst coding of a re-traversal omg OMO
                parent = curr_dir.parent
                while parent:
                    parent.size += file_size
                    parent = parent.parent
    print('Part 1:', part_1(root))
    print('Part 2:', part_2(root))


if __name__ == "__main__":
    main()
