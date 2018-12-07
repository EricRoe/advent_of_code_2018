from collections import defaultdict

with open('./input.txt') as f:
    data = [line.split(', ') for line in f]
    data = [(int(t[0]), int(t[1]), i) for i, t in enumerate(data)]


def dist(p, x, y):
    return abs(p[0]-x) + abs(p[1]-y)

def closest(x,y):
    close = (1e5, -1) # distance, id
    for p in data:
        if dist(p, x, y) < close[0]:
            close= (dist(p, x, y), p[2])
        elif dist(p,x,y) == close[0]:
            return -1
    return close[1]


c = defaultdict(int)
pts = dict()
xmin = min(d[0] for d in data)
xmax = max(d[0] for d in data)
ymin = min(d[1] for d in data)
ymax = max(d[1] for d in data)


for x in range(xmin, xmax+1):
    for y in range(ymin, ymax+1):
        close = closest(x,y) 
        c[close] += 1
#        pts[(x,y)] = close

inf_pts = {-1}
for x in range(xmin, xmax+1):
    for y in [ymin, ymax+1]:
        inf_pts.add(closest(x,y))

for y in range(ymin, ymax+1):
    for x in [xmin, xmax+1]:
        inf_pts.add(closest(x,y))

print(max((i for i in c.items() if i[0] not in inf_pts), key = lambda t: t[1])[1])


