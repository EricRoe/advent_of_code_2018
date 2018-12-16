from operator import itemgetter
from collections import *
import re

with open('./input.txt') as f:
    d = [l[:-1] for l in f]

carts = [[c,x,y,0] for y,l in enumerate(d) for x, c in enumerate(l) if c in 'v^<>']

for i,l in enumerate(d):
    d[i] = l.replace('v', '|').replace('^', '|').replace('<', '-').replace('>', '-')

intersection = {'v':'>v<', '^':'<^>', '>':'^>v', '<':'v<^'} # +
corner_fwd = {'v':'<', '^':'>', '>':'^', '<':'v'}           # /
corner_back = {'v':'>', '^':'<', '>':'v', '<':'^'}          # \



def next():
    carts.sort(key=itemgetter(2,1))
    crashed = []
    for cart in carts:
        if cart[0] == 'v':
            cart[2] += 1
        elif cart[0] == '^':
            cart[2] -= 1
        elif cart[0] == '<':
            cart[1] -= 1
        else:
            cart[1] += 1

        track = d[cart[2]][cart[1]]
        if track == '+':
            cart[0] = intersection[cart[0]][cart[3]]
            cart[3] += 1
            cart[3] %= 3
        elif track == '/':
            cart[0] = corner_fwd[cart[0]]
        elif track == '\\':
           cart[0] = corner_back[cart[0]] 

        for c2 in carts:
            if cart != c2 and cart[1] == c2[1] and cart[2] == c2[2]:
                crashed.append(cart)
                crashed.append(c2)
    for cart in crashed:
        carts.remove(cart)




def hit():
    for j, c in enumerate(carts):
        for i, cc in enumerate(carts):
            if i!=j and c[1] == cc[1] and c[2] == cc[2]:
                return (c[1], c[2])
    return False


def hit2():
    for i in range(len(carts)-1):
        for j in range(i+1,len(carts)):
            if carts[i][1] == carts[j][1] and carts[i][2] == carts[j][2]:
                carts.remove(carts[i])
                carts.remove(carts[j-1])
                return True
    return False


def p():
    coords = [(c[1], c[2]) for c in carts]
    for y, r in enumerate(d):
        for x, c in enumerate(r):
            if (x,y) in coords:
                print('c', end='')
            else:
                print(c, end='')
        print()


print('start')
t = 0
while len(carts) > 1:
    print(t)
    t += 1


    next()

print(carts)


