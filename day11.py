from collections import namedtuple
from math import prod

Monkey = namedtuple('Monkey', ['idx', 'items', 'op', 'test', 'true_dest', 'false_dest'])

def get_suffix(lines, splitter):
    return lines.pop(0).split(splitter).strip()[-1].strip()

monkeys = []

def get_op_func(s):
    print(s)
    a, op, b = s.strip().split(' ')
    def op_func = (x):

    if op == '+':
        if a == 'old' and b != 'old':
            return lambda x: x + int(b)
        if a != 'old' and b == 'old':
            return lambda x: x + int(a)
        if a == 'old' and b == 'old':
            return lambda x: x + x
    if op == '*':
        if a == 'old' and b != 'old':
            return lambda x: x * int(b)
        if a != 'old' and b == 'old':
            return lambda x: x * int(a)
        if a == 'old' and b == 'old':
            return lambda x: x * x
    raise Exception()


for idx, raw in enumerate(open('day11.input.txt').read().split('\n\n')):
    lines = raw.split("\n")
    assert 'Monkey' in lines.pop(0)
    items = [int(s.strip()) for s in get_suffix(lines, 'items: ').split(', ')]
    op = get_op_func(get_suffix(lines, 'new ='))
    test = int(get_suffix(lines, 'divisible by'))
    true_dest = int(get_suffix(lines, 'monkey'))
    false_dest = int(get_suffix(lines, 'monkey'))
    m = Monkey(idx, items, op, test,  true_dest, false_dest)
    monkeys.append(m)

for m in monkeys:
    print(m)
monkey_cts = [0] * len(monkeys)


def part1():
    for r in range(20):
        print('round', r + 1)
        for m in monkeys:
            print(f'monkey {m.idx}', m.items)
            monkey_cts[m.idx] += len(m.items)
            while m.items:
                item = m.items.pop(0)
                item = m.op(item)
                item //= 3
                dest = m.true_dest if item % m.test == 0 else m.false_dest
                monkeys[dest].items.append(item)
                print(f'.. sending {item} to {dest}')
    print(prod(sorted(monkey_cts)[-2:]))

def part2():
    big_mod = prod(m.test for m in monkeys)
    for r in range(10000):
        if r%100 == 0:
            print('round', r + 1)
        for m in monkeys:
            monkey_cts[m.idx] += len(m.items)
            while m.items:
                item = m.items.pop(0)
                item = m.op(item)
                item %= big_mod
                dest = m.true_dest if item % m.test == 0 else m.false_dest
                monkeys[dest].items.append(item)
    print(prod(sorted(monkey_cts)[-2:]))

part1()
part2()

