import collections
import queue

grid = [[c for c in line.strip()] for line in open('day12.input.txt').readlines()]
ROWS = range(len(grid))
COLS = range(len(grid[0]))

for r in ROWS:
    for c in COLS:
        if grid[r][c] == 'S':
            start = (r, c)
            grid[r][c] = 'a'
        elif grid[r][c] == 'E':
            end = (r, c)
            grid[r][c] = 'z'
        grid[r][c] = ord(grid[r][c]) - ord('a')


# print(grid)
# print(start, end)
# print(grid)

adjacent_positions = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
print(adjacent_positions)

queue = []
queue.append((start, 0))
visited = set(start)

def part1():
    while len(queue):
        ((r, c), d) = queue.pop(0)
        print(r, c, d)
        if (r, c) == end:
            print(d)
            break

        new_pos = [(r + dr, c + dc) for dr, dc in adjacent_positions]
        for (new_r, new_c) in new_pos:
            if not (new_r in ROWS and new_c in COLS):
                continue
            if grid[r][c] + 1 < grid[new_r][new_c]:
                continue
            if (new_r, new_c) in visited:
                continue
            queue.append(((new_r, new_c), d + 1))
            visited.add((new_r, new_c))

def part2():
    queue = []
    queue.append((end, 0))
    visited = set(end)
    distances = {}
    distances[end] = 0
    while len(queue):
        ((r, c), d) = queue.pop(0)
        print(r, c, d)
        # if (r, c) == end:
        #     print(d)
        #     break

        new_pos = [(r + dr, c + dc) for dr, dc in adjacent_positions]
        for (new_r, new_c) in new_pos:
            if not (new_r in ROWS and new_c in COLS):
                continue
            if grid[new_r][new_c] + 1 < grid[r][c]:
                continue
            if (new_r, new_c) in visited:
                continue
            queue.append(((new_r, new_c), d + 1))
            distances[(new_r, new_c)] = d + 1
            visited.add((new_r, new_c))

    print(distances)
    print('missing distances')
    for r in ROWS:
        for c in COLS:
            if (r, c) not in distances:
                print(r, c, grid[r][c])
    import ipdb; ipdb.set_trace()
    ans = sorted([distances[(r, c)] for r in ROWS for c in COLS if grid[r][c] == 0 and (r, c) in distances])[0]
    print(ans)

part2()
# def part2():
#     nodes = queue.PriorityQueue()
#     dists = {}
#     nodes.put((0, end))
#     while True:
#         d, (r, c) = nodes.get()
#         dists


#         for (new_r, new_c) in [(r + dr, c + dc) for dr, dc in adjacent_positions]:
#             if not (new_r in ROWS and new_c in COLS):
#                 continue
#             if grid[new_r][new_c] + 1 < grid[r][c]:
#                 continue
#             nodes.put((d + 1, (new_r, new_c)))

#             # if (new_r, new_c) in visited:
#             #     continue






# # returns the length of the shortest path from (r, c) to END
# def recur(r, c, visited, d=0):
#     if (r, c) in memo:
#         return memo[(r, c)]
#     print(r, c, d, memo[(r, c)])
#     if (r, c) == end:
#         return 0

#     results = [9999]

#     # new_pos = sorted([(r + dr, c + dc) for dr, dc in adjacent_positions], key=dist)
#     new_pos = [(r + dr, c + dc) for dr, dc in adjacent_positions]
#     for (new_r, new_c) in new_pos:
#         if not (new_r in ROWS and new_c in COLS):
#             continue
#         if grid[r][c] + 1 < grid[new_r][new_c]:
#             continue
#         if (new_r, new_c) in visited:
#             continue
#         results.append(1 + recur(new_r, new_c, visited | {(r, c)}, d + 1 ))
#     print('res', (r, c), results)
#     result = min(results)
#     print('solved:', (r, c, result))
#     memo[(r, c)] = result
#     return result

# ans = recur(*start, set())
# print('ans', ans)




