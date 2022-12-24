def part1_execute_move(num_to_move, source, dest):
    for i in range(num_to_move):
        dest.insert(0, source.pop(0))

def part2_execute_move(num_to_move, source, dest):
    dest[0:0] = source[0:num_to_move]
    source[0:num_to_move] = []

def process(execute_move):
    all_str = open('day5.input.txt').read()
    init_str, instructions_str = all_str.split('\n\n')
    init = init_str.split('\n')

    num_stacks = (len(init[-1]) + 2) // 4
    stacks = [[] for i in range(num_stacks)]

    for stack_str in init[:-1]:
        parsed = stack_str[1::4].ljust(num_stacks, ' ')
        for i, c in enumerate(parsed):
            if c.isupper():
                stacks[i].append(c)

    for instr in instructions_str.split('\n')[:-1]:
        import re
        num_to_move, source, dest = [int(token) for token in re.split('\D+', instr) if token]
        execute_move(num_to_move, stacks[source - 1], stacks[dest - 1])

    return(''.join(stack[0] for stack in stacks))

def part1():
    print(process(part1_execute_move))

def part2():
    print(process(part2_execute_move))

part1()
part2()
