from collections import *

with open('./input.txt') as f:
    d = [l.strip() for l in f]

print(d[:10])

acres= defaultdict(str)

for y in range(len(d)):
    for x in range(len(d[0])):
        acres[(x,y)] = d[y][x]

next_acres = acres.copy()


def get_adjacent(x,y):
    return [acres[(xx, yy)] for xx in range(x-1, x+2) for yy in range(y-1, y+2) if not (xx == x and yy == y)]


def opn(x,y):
    return '|' if sum(c == '|' for c in get_adjacent(x,y)) >= 3 else '.'


def tree(x,y):
    return '#' if sum(c == '#' for c in get_adjacent(x,y)) >= 3 else '|'


def lumber(x,y):
    return '#' if any(c == '#' for c in get_adjacent(x,y)) and any(c == '|' for c in get_adjacent(x,y)) else '.'


def p():
    for y in range(len(d)):
        for x in range(len(d[0])):
            print(acres[(x,y)], end='')
        print()


funs = {'.': opn, '|': tree, '#': lumber}


for i in range(int(1e9)):
    print(i)
    print(sum(c == '|' for c in acres.values())*sum(c == '#' for c in acres.values()))
    for x in range(len(d[0])):
        for y in range(len(d)):
           next_acres[(x,y)] = funs[acres[(x,y)]](x,y)

    acres = next_acres.copy()

print('final')
p()
print(sum(c == '|' for c in acres.values())*sum(c == '#' for c in acres.values()))
