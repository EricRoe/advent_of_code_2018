s = 4172
g = dict()

def power(x,y):
    rid = x+10
    p = rid*y
    p += s
    p *= rid
    if p < 100:
        return -5
    return (p//100 % 10) - 5


def check(x, y):
    best = 0
    l = []
    cur = 0
    for s in range(300-max(x,y)):
        cur += sum(g[(x+s, y+dy)] for dy in range(s))
        cur += sum(g[(x+dx, y+s)] for dx in range(s+1))
        l.append(cur)
    return (x,y,l.index(max(l))+1,max(l))


for x in range(300):
    for y in range(300):
        g[(x,y)] = power(x,y)



best = (0,0,0,-1e5)

for x in range(300):
    for y in range(300):
        cur = check(x,y)
        if best[3] < cur[3]:
            print(cur)
            best = cur

    print('{:.3f}'.format(x/300))


print(best)
