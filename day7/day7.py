from collections import defaultdict

with open('./input.txt') as f:
    d = [(line[5], line[36]) for line in f]

a = [i[0] for i in d]
b = [i[1] for i in d]

m = defaultdict(list)
dep = defaultdict(list)

for i in d:
    m[i[0]] += i[1]
    dep[i[1]] += i[0]


order = ''

candidates = sorted(list(set([i for i in a if i not in b])))

while candidates:
    order += candidates.pop(0)    
    for i in m[order[-1]]:
        ok = True
        for j in dep[i]:
            ok = ok and (j in order)
        if ok:
            candidates.append(i)
    candidates.sort()

print(order)


order = ''
clock = 0
candidates = sorted(list(set([i for i in a if i not in b])))
workers = [[None, None] for i in range(5)] # letter, seconds remaining

def free():
    return len([w for w in workers if w[0] is None]) > 0

def getw(ltr):
    for w in workers:
        if w[0] == None:
            w[0] = ltr
            w[1] = ord(ltr) - 4
            return

def tick():
    global order
    global clock

    clock += 1

    for w in workers:
        if w[0] is not None:
            w[1] -= 1
            if w[1] == 0:
                order += w[0]
                w[0] = None
                adj_cand()

def adj_cand():
    for i in m[order[-1]]:
        ok = True
        for j in dep[i]:
            ok = ok and (j in order)
        if ok:
            candidates.append(i)
    candidates.sort()

    
while len(order) < 26:
    while free() and candidates:
        getw(candidates.pop(0))
    tick()
print(order)
print(clock)


