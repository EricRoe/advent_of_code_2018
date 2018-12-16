from collections import *
import re

with open('./input.txt') as f:
    d = f.readlines()

s = re.findall(r'#[#.]*', d.pop(0))[0]
s = list('.'*20 + s + '.'*150)
sn = s.copy()

d.pop(0)

M = {}
for r in d:
    M[r[:5]] = r[9]


diffs = []
for t in range(130):

    for start in range(len(s)-4):
        sn[start+2] = M[''.join(s[start:start+5])]

    s, sn = sn, s
    if t > 120:
        diffs.append((t, sum(i-20 for i,v in enumerate(s) if v == '#')))

        #print(t)
        #print(sum(i-20 for i,v in enumerate(s) if v == '#'))
        #print(''.join(s))


#print(''.join(s))
#print(sum(i-20 for i,v in enumerate(s) if v == '#'))
print('i, t, sum, delta')
for i, v in enumerate(diffs):
    print((i, v[0], v[1], v[1]-diffs[i-1][1]))
print(diffs)

