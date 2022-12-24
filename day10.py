cycle = 1
x = 1

def cycle_to_pos():
    return cycle % 40 - 1

def print_tick():
    pos = cycle_to_pos()
    if pos in range(x-1, x+2):
        c = '#'
    else:
        c = '.'
    print(c, end = '')

    if cycle % 40 == 0:
        print()



t = 0
cycle_pts = set(range(20, 221, 40))
for line in open('day10.input.txt').readlines():
    line = line.strip()
    cmd = line[:4]
    # print('cmd', line)
    # print('..cycle', cycle)
    # print('..x', x)
    if cmd == 'addx':
        x_inc = int(line[5:])
        cycle_inc = 2
    else:
        assert cmd == 'noop'
        x_inc = 0
        cycle_inc = 1
    # candidates = set(range(cycle, cycle + cycle_inc))
    # if cycle_pts & candidates:
    #     cycle_hit, = cycle_pts & candidates
    #     # print('..cycle_hit', cycle_hit)
    #     t += cycle_hit * x
    for i in range(cycle_inc):
        print_tick()
        cycle += 1
    x += x_inc

print(t)
