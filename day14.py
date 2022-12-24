walls = [[[int(c) for c in pair.split(',')] for pair in line.strip().split('->')]
         for line in open('day14.input.txt').read().splitlines()]
max_r = max([pair[1] for wall in walls for pair in wall])
max_c = max([pair[0] for wall in walls for pair in wall])
c_offset = None


def correct_col_offset():
    global max_c, c_offset
    min_c = min([pair[0] for wall in walls for pair in wall])
    print(min_c)
    c_offset = min_c - 10
    max_c -= c_offset
    print(max_c)

    for wall in walls:
        for pair in wall:
            pair[0], pair[1] = pair[1], pair[0]
            pair[1] -= c_offset
correct_col_offset()

grid = [['.'] * max_c] * max_r

def draw_wall(wall):
    cur = wall.pop(0)
    while wall:
        grid[cur[0]][cur[1]] = '#'
        head = wall[0]
        if cur != head:
            if cur[0] != head[0]:
                cur[0] += abs(head[0] - cur[0]) // (head[0] - cur[0])
            if cur[1] != head[1]:
                cur[1] += abs(head[1] - cur[1]) // (head[1] - cur[1])
        else:
            wall.pop(0)



def print_grid(grid):
    def row_str(r):
        return ''.join(map(str, r))

    label100 = [(c + c_offset) // 100 % 10 for c in range(max_c)]
    print(label100)
    label10 = [(c + c_offset) // 10 % 10 for c in range(max_c)]
    label1 = [(c + c_offset) % 10 for c in range(max_c)]
    print(row_str(label100))
    print(row_str(label10))
    print(row_str(label1))
    print('\n'.join([''.join(r) for r in grid]))

for wall in walls:
    print(wall)
    draw_wall(wall)
    print_grid(grid)
