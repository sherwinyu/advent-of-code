import re
from collections import namedtuple

Item = namedtuple('Item', ['name', 'size', 'children'])

def peek_line(f):
    pos = f.tell()
    line = f.readline()
    f.seek(pos)
    return line

def is_cmd(line):
    return line[0] == '$'

def get_cmd_and_arg(line):
    assert is_cmd(line)
    parsed = line.strip().split(' ')[1:]
    cmd = parsed[0]
    if cmd == 'ls':
        return 'ls', None
    else:
        return 'cd', parsed[1]


def parse_input_into_dir_item(f, expected_dir_name):
    """ returns an Item representing the directory
    pre condition: f is pointing to a line that is a `cd` descending into a dir
    i.e., it's not a 'cd ..'
    """
    # Process cd command
    cmd, arg = get_cmd_and_arg(f.readline())
    # print(cmd, arg)
    assert cmd == 'cd' and arg != '..', f'expected cmd to be cd into a dir, got {cmd}'
    assert arg == expected_dir_name, f'expected parse_input to be called with {expected_dir_name}, got {arg}'
    cur_item = Item(name=arg, size='dir', children=[])


    # Process ls command: every cd command that meets our precondition will be followed by an ls
    cmd, arg = get_cmd_and_arg(f.readline())
    assert cmd == 'ls', f'expected cmd to be ls, got {cmd}'

    children_dirs = []
    # Process ls output
    # every line is either a dir or a file
    # if it's a dir, save its name for recursive processing later
    # if it's a file, create the Item with appropriate name and size
    # exit condition is when we're back at a command
    while (line := peek_line(f)) and not is_cmd(line):
        line = f.readline()
        size, name = line.strip().split()
        if size == 'dir':
            children_dirs.append(name)
        else:
            cur_item.children.append(Item(name=name, size=int(size), children=None))

    # Recursively process all child dirs
    for child_dir in children_dirs:
        cur_item.children.append(parse_input_into_dir_item(f, child_dir))

    # Process all 'cd ..' commands as no-ops
    while (l := peek_line(f)) and is_cmd(l) and l.strip() == '$ cd ..':
        line = f.readline()
        # print(line)

    return cur_item


f = open('day7.input.txt')
root = parse_input_into_dir_item(f, '/')

part1_ans = 0
dir_sizes = []
def process_sizes(item):
    """Recursively compute total sizes, save sizes for part 2, and also flag sizes less than 100000
    for part 1"""
    global part1_ans
    if item.size != 'dir':
        return item.size
    else:
        size = sum([process_sizes(child) for child in item.children])
        if size < 100000:
            part1_ans += size
        dir_sizes.append(size)
        return size

space_needed = 30000000 - (70000000 - process_sizes(root))
dir_sizes.sort()

print('part 1', part1_ans)
print('part 2', [s for s in dir_sizes if s > space_needed][0])
