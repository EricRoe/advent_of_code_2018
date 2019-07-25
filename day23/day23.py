from collections import *
import re

with open('./input.txt') as f:
    d = [l for l in f]

d = [list(map(int, re.findall('-?\d+', l))) for l in d]
cnt = defaultdict(int)

dist = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]) + abs(p1[2]-p2[2])

for p in d:
    c = 0
    for pp in d:
        if dist(p, pp) <= p[3]:
            c +=1
    cnt[(p[0], p[1], p[2])] = c

it = None
for l in d:
    if it is None or l[3] > it[3]:
        it = l
print(cnt[(it[0], it[1], it[2])])


x = sum(p[0] for p in d)/1000
y = sum(p[1] for p in d)/1000
z = sum(p[2] for p in d)/1000
print(sum(p[0] - x for p in d)/1000)
print(sum(p[1] - y for p in d)/1000)
print(sum(p[2] - z for p in d)/1000)

print(len(d))
