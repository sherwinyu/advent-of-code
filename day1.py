path = 'day1.input.txt'

def get_elf_group_sums():
    """Return a list of ints, each representing the sum of calories an elf is carrying
    """
    with open(path) as f:
        all_str = f.read()
        return [sum([int(val) for val in elf_str.strip().split('\n')]) for elf_str in all_str.split('\n\n')]

def part1():
    return max(get_elf_group_sums())

def part2():
    return sum(sorted(get_elf_group_sums())[:-4:-1])

print(part1())
print(part2())

