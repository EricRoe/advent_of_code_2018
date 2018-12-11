import re

def pos(p):
    return (p[0] + t * p[2], p[1] + t * p[3]) # x,y

with open('./input.txt') as f:
    d = [list(map(int, re.findall(r'[-\d]+', line))) for line in f]

# Tweak to find solution. 
# Bump t to help zero in on the solution
# Size controls the bounding box. Print grid only when it fits inside
t = 0
size = 120
log_interval = 1000

while True:
    gridpts = [pos(p) for p in d]

    minx = min(p[0] for p in gridpts)
    maxx = max(p[0] for p in gridpts)
    miny = min(p[1] for p in gridpts)
    maxy = max(p[1] for p in gridpts)

    if not t % log_interval:
        print(t)
        print([minx, maxx, miny, maxy])

    if maxx - minx < size and maxy - miny < size:
        print(t)
        grid = []
        for y in range(miny, maxy+1):
            row = []
            for x in range(minx, maxx+1):
                if (x,y) in gridpts:
                    row.append('#')
                else:
                    row.append('.')
            grid.append(row)
                
        for row in grid:
            print(''.join(row))
        input()

    t += 1

