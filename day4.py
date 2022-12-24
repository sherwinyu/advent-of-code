import re

def readlines(f):
    return [l.strip() for l in open(f).readlines()]

def process(check_ftn):
    count = 0
    for l in readlines("day4.input.txt"):
        [a1, a2, b1, b2] = map(int, re.split(',|-', l))
        a = set(range(a1, a2 + 1))
        b = set(range(b1, b2 + 1))
        if check_ftn(a, b):
            count += 1
    return count

def part1():
    print(process(check1))

def part2():
    print(process(check2))

def check1(a, b):
    return len(a & b) == min(len(a), len(b))

def check2(a, b):
    return a & b

part1()
part2()
