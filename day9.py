deltas = {
    'U': 1j,
    "D": -1j,
    "L": -1,
    "R": 1,
}

def distance(a, b):
    delta = (a - b)
    return abs(delta.imag) + abs(delta.real)

def snap_to_diagonal_delta(c):
    return complex(c.real / abs(c.real), c.imag / abs(c.imag))

def is_adjacent(a, b):
    c = a - b
    return abs(c.imag) <= 1 and abs(c.real) <= 1

knots = None

def compute_new_pos(head, tail):
    if is_adjacent(head, tail):
        return tail
    d = distance(head, tail)
    if d == 2:
        tail += (head - tail) / 2
    if d >= 3:
        tail += snap_to_diagonal_delta((head - tail))
    return tail

def reconcile_knot(i):
    head = knots[i - 1]
    tail = knots[i]
    knots[i] = compute_new_pos(head, tail)


def process(n):
    global knots
    knots = [0] * n
    visited = set()

    for line in open('day9.input.txt').readlines():
        direction, dist = line.strip(' ').split()
        visited.add(knots[-1])

        for i in range(int(dist)):
            knots[0] += deltas[direction]

            for i in range(1, len(knots)):
                reconcile_knot(i)
            visited.add(knots[-1])

    return len(visited)

def part1():
    print(process(2))
def part2():
    print(process(10))
part1()
part2()

