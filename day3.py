def readlines(f):
    return [l.strip() for l in open(f).readlines()]

def sacks_to_priority(sacks):
    item = next(iter(set.intersection(*(set(sack) for sack in sacks))))
    return (ord(item.lower()) - ord('a') + 1) + (26 if item.isupper() else 0)

def chunk(arr, n):
    for i in range(0, len(arr), 3):
        yield arr[i:i+3]

def part2():
    lines = readlines('day3.input.txt')
    print(sum([sacks_to_priority(sacks) for sacks in chunk(lines, 3)]))


def part1():
    score = 0
    for line in readlines('day3.input.txt'):
        a = line[0:len(line)//2]
        b = line[len(line)//2:]
        sacks = [a,b]
        score += sacks_to_priority(sacks)
    print(score)

part1()
part2()
