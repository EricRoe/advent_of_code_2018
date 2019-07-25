from collections import *

rocky = 0
wet = 1
narrow = 2

nothing = 0
climb = 1
torch = 2
cg_t = climb & torch


d = 5913
tx = 8
ty = 701

debug = False
if debug:
    d = 510
    tx = 10
    ty = 10


def can_move(region, equip):
    if region == rocky:
        return equip != nothing
    if region == wet:
        return equip & torch != torch
    if region == narrow:
        return equip & climb != climb


t = [[0 for i in range(tx+1)] for j in range(ty+1)]
el = [[0 for i in range(tx+1)] for j in range(ty+1)]
gi = [[0 for i in range(tx+1)] for j in range(ty+1)]

for y in range(ty+1):
    for x in range(tx+1):
        if x==0 or y==0:
            gi[y][x] = x*16807+y*48271
            el[y][x] = (d+gi[y][x])%20183
            t[y][x] = el[y][x] % 3

gi[ty][tx] = 0
el[ty][tx] = 0
t[ty][tx] = 0

for y in range(1,ty+1):
    for x in range(1,tx+1):
        gi[y][x] = el[y][x-1]*el[y-1][x]
        el[y][x] = (d+gi[y][x])%20183
        t[y][x] = el[y][x] % 3

t[ty][tx] = 0
if debug:
    for l in t:
        print(l)

print(sum(sum(i for i in row) for row in t))

times = defaultdict(int)

