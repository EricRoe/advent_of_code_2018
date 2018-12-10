def pos(p):
    return (p[0] + t * p[2], p[1] + t * p[3]) # x,y

with open('./input.txt') as f:
    data = [line for line in f]

d = [(int(l[l.index('<')+1:l.index(',')]), int(l[18:24].strip()), int(l[36:38]), int(l[40:42])) for l in data]

# uncomment to parse test input.  Needs regex refactoring :P
#d = [(int(l[l.index('<')+1:l.index(',')]), int(l[14:16].strip()), int(l[28:30]), int(l[32:34])) for l in data]

# Tweak to find solution. 
# Bump t to help zero in on the solution
# Size controls the bounding box. Print grid only when it fits inside
t = 0
size = 10
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

    t += 1

