import functools
def cmp(a, b):
    if type(a) == int and type(b) == int:
        return a - b
    if type(a) == int and type(b) == list:
        return cmp([a], b)
    if type(a) == list and type(b) == int:
        return cmp(a, [b])
    if type(a) == list and type(b) == list:
        minl = min(len(a), len(b))
        for aa, bb in zip(a, b):
            if (val := cmp(aa, bb)):
                return val
        return len(a) - len(b)


def part1():
    ans = 0
    for i, example in enumerate(open('day13.input.txt').read().split('\n\n')):
        left, right = [eval(l) for l in example.splitlines()]
        if cmp(left, right) < 0:
            ans += i + 1
    print(ans)

def part2():
    START = [[2]]
    END = [[6]]
    els = [eval(line) for line in open('day13.input.txt').read().splitlines() if line]
    els +=  [START, END]
    els = sorted(els, key=functools.cmp_to_key(cmp))
    ans = (els.index(START) + 1) * (els.index(END) + 1)
    print(ans)

part1()
part2()
