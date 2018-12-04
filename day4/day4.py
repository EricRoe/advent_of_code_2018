from datetime import datetime

with open('./input.txt') as f:
    data = [line for line in f]

date = [datetime(1518, int(d[d.index('-')+1:d.index('-')+3]), int(d[d.index('-')+4:d.index('-')+6]), int(d[d.index(' ')+1:d.index(':')]), int(d[d.index(':')+1:d.index(']')])) for d in data]

day = [int(d[9:11]) for d in data]
m = [int(d[15:17]) for d in data]

g1 = dict((k, int(v[v.index('#')+1:v.index('b')-1])) for k, v in enumerate(data) if 'Guard' in v)
g = []
for i in range(len(day)):
    if i in g1:
        g.append(g1[i])
    else:
        g.append(g[-1])

s = ['falls' in d for d in data]

d = list(zip(data, day, m, g, s, date))
d.sort(key = lambda t: t[5])

guards = {}
for i in g:
    guards[i] = [0 for i in range(60)]

curg = d[0][3]
curm = 0
sleep = False
for t in d:
    if 'Guard' in t[0]:
        for m in range(curm, 60):
            guards[curg][m] += 1 if sleep else 0

        curg = t[3]
        curm = t[2]
        sleep = False
        continue

    for m in range(curm, t[2]):
        guards[curg][m] += 1 if sleep else 0

    curm = t[2]
    sleep = t[4]



x = max(sum(g) for g in guards.values())
y = [(k,v) for k,v in guards.items() if sum(v) == x][0]
print(y[0]*y[1].index(max(y[1])))

x = max(max(g) for g in guards.values())
y = [(k,v) for k,v in guards.items() if max(v) == x][0]
print(y[0]*y[1].index(max(y[1])))
