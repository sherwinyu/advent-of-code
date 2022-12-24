import math

f = open('day8.input.txt')
grid = [[int(c) for c in line.strip()] for line in f.readlines()]

SIZE = len(grid)

marked_visible = set()

def pos_and_idx_to_coord(pos, idx):
    interior = range(len(grid))

    if pos.imag in interior:
        const = pos.real
    else:
        assert pos.real in interior
        const = pos.imag

    var = idx if const == -1 else SIZE - idx - 1

    if pos.imag in interior:
        return  complex(var, pos.imag)
    else:
        return complex(pos.real, var)

def check_visible(seq, pos):
    print( 'CHECKING SEQ', seq, pos)
    count = 0
    highest = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > highest:
            highest = seq[i]
            print(f'hit: seq[{i}] = {seq[i]}', seq)
            coord = pos_and_idx_to_coord(pos, i)
            print(coord)
            marked_visible.add(coord)

print('checking rows')
for r in range(SIZE):
    seq = grid[r]
    print(seq)
    check_visible(seq, complex(-1, r))
    check_visible(seq[::-1], complex(SIZE, r))
    marked_visible.add(complex(0, r))
    marked_visible.add(complex(SIZE - 1, r))

print('checking cols')
for c in range(SIZE):
    seq = [row[c] for row in grid]
    print(seq)
    check_visible(seq, complex(c, -1))
    check_visible(seq[::-1], complex(c, SIZE))
    marked_visible.add(complex(c, 0))
    marked_visible.add(complex(c, SIZE - 1))

print(marked_visible)

for r in range(SIZE):
    for c in range(SIZE):
        if (complex(c, r) in marked_visible):
            print(' # ', end = '')
        else:
            print(' - ', end = '')
    print('')

print(len(marked_visible))

def compute_score(r, c):
    row = grid[r]
    col = [row[c] for row in grid]
    seqs = [
        row[0:c:][::-1],
        row[c+1:],
        col[0:r][::-1],
        col[r+1:]
    ]
    viss = [find_visibility(seq, grid[r][c]) for seq in seqs]
    return math.prod(viss)

def find_visibility(seq, height):
    return next((idx for idx, h in enumerate(seq) if h >= height), len(seq) - 1) + 1


coords = [(r, c) for r in range(SIZE) for c in range(SIZE)]
print(coords)
print('part 2', max([compute_score(*coord) for coord in coords]))

cv = 0
ccoord = None
for coord in coords:
    v = compute_score(*coord)
    if v > cv:
        cv = v
        ccoord = coord

print(ccoord, cv)



# for c in SIZE:

    # check_visible(grid[r], )
# check_visible(grid[1][::-1], 5 + 1j)
# for i in range(len(grid)):
#     pos = complex()

