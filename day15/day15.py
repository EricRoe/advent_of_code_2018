from operator import attrgetter, itemgetter
from collections import *
import re


class Unit():
    def __init__(self, x,y,t,hp=200):
        self.x = x
        self.y = y
        self.t = t
        self.hp = hp


    def target(self):
        candidates = s([u for u in units if not self.cmp(u) and dist(u,self) == 1 and u.t != self.t])
        if not candidates:
            return candidates
        return sorted(candidates, key=attrgetter('hp', 'y', 'x'))[0]


    def fight(self):
        t = self.target()
        if t:
            t.hp -= 3
            if t.hp <= 0:
                units.remove(t)


    def move(self):
        print('X')
        if self.target():
            return
        if not [u for u in units if u.t != self.t and has_liberties(u.x, u.y)]:
            return

        p = self.path()
        if p:
            self.x = p[0]
            self.y = p[1]
            

    def path(self):
        paths = [pf((self.x, self.y), (u.x, u.y), [], min(dist(self,u)*2, 50)) for u in units if self.t != u.t]
        paths = [p for p in paths if p and len(p) == min(len(p) for p in paths if p)]
        paths = sorted(paths, key=lambda p: p[-2][1]*1000 + p[-2][0])
        if paths:
            return paths[0][0]
        return False


    def cmp(self, u):
        return self.x == u.x and self.y == u.y and self.hp == u.hp and self.t == u.t


def pf(p, t, acc, mxl):
    if len(acc) > mxl:
        return False

    if distp(p,t) == 1:
        acc.append('found')
        return acc

    potential_pts = [(p[0]+1,p[1]),(p[0]-1,p[1]),(p[0],p[1]+1),(p[0],p[1]-1)]
    pts = [pt for pt in potential_pts if pt not in acc and ok(pt[0],pt[1])]

    if len(pts) == 0:
        return False

    results = []
    for pt in pts:
        result = pf(pt, t, acc + [pt], mxl)
        if not result:
            continue
        results.append(result)

    if not results:
        return False

    results = [r for r in results if len(r) == min(len(r) for r in results)]
    if len(results[0]) > 2:
        results = sorted(results, key=lambda r: r[-2][1]*999+r[-2][0])
    results = sorted(results, key=lambda r: r[0][1]*999+r[0][0])
    return results[0]


        

def has_liberties(x,y):
    return ok(x+1,y) or ok(x-1,y) or ok(x,y+1) or ok(x,y-1)


def ok(x,y):
    return grid[y][x] not in '#X' and (x,y) not in [(u.x,u.y) for u in units]


def dist(a,b):
    return abs(a.x - b.x) + abs(a.y - b.y)


def distp(a,b):
    return abs(a[0]-b[0])+abs(a[1]-b[1])


def s(l):
    return sorted(l, key=attrgetter('y','x'))


def p():
    for y,l in enumerate(grid):
        for x,c in enumerate(l):
            if (x,y) in [(u.x,u.y) for u in units]:
                print([u.t for u in units if u.x ==x and u.y == y][0], end='')
            else:
                print(grid[y][x], end='')
        print()


with open('./input.txt') as f:
    grid = [list(l.strip()) for l in f]

units = []

for y,l in enumerate(grid):
    for x,c in enumerate(l):
        if c in 'GE':
            units.append(Unit(x,y,c))
            grid[y][x] = '.'


t = 0
while [u for u in units if u.t == 'E']:
    units = s(units)
    print(t)
    p()
    for u in units:
        u.move()
        u.fight()
    print()
    t += 1

print((t-1)*sum(u.hp for u in units))

