from collections import defaultdict, deque

def pos(p):
    return (p[0] + t * p[2], p[1] + t * p[3]) # x,y

with open('./input.txt') as f:
    data = [line for line in f]

d = [(int(l[l.index('<')+1:l.index(',')]), int(l[18:24].strip()), int(l[36:38]), int(l[40:42])) for l in data]
#d = [(int(l[l.index('<')+1:l.index(',')]), int(l[14:16].strip()), int(l[28:30]), int(l[32:34])) for l in data]

t = 10300
while True:
    gridpts = [pos(p) for p in d]
    row = ['.'] * (max(p[0] for p in gridpts) + 1 + abs(min(p[0] for p in gridpts)))
    grid = [row.copy() for i in range(max(p[1] for p in gridpts) + 1 + abs(min(p[1] for p in gridpts)))]

    for p in gridpts:
        grid[p[1]+abs(min(p[1] for p in gridpts))][p[0]+abs(min(p[0] for p in gridpts))] = '#'

    print(t, len(grid), len(grid[0]))
    if 274 > len(grid) > 270:
        for row in grid:
            print(''.join(row[:220]))
        for row in grid:
            print(''.join(row[220:]))
        print()

    t += 1


