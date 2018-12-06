def dist(p, x, y):
    return abs(p[0]-x) + abs(p[1]-y)

fieldsize = 400
padding = 0
distance = 10000

with open('./input.txt') as f:
    d = [line.split(', ') for line in f]
    d = [(int(l[0])+padding, int(l[1])+padding) for l in d]

    d = [(d[i][0], d[i][1], i) for i in range(len(d))]


field = [[None for y in range(fieldsize)] for x in range(fieldsize)]

for p in d:
    for y in range(len(field)):
        for x in range(len(field[0])):
            if field[x][y] is None:
                field[x][y] = dist(p, x, y)
            else:
                field[x][y] += dist(p, x, y)



           # if field[x][y] is None or dist(p, x, y) < field[x][y][0]:
           #     field[x][y] = (dist(p, x, y), p[2])
           # elif dist(p, x, y) == field[x][y][0]:
           #     field[x][y] = (dist(p,x,y), -1)

    print(p)


#pv = dict((p, sum(p[2] == y[1] for x in field for y in x)) for p in d)
#
#l = sorted([(p[0][2], p[1]) for p in pv.items()], key = lambda t: t[1])
#for i in l:
    #print(i)
#
#
#inf = {p[1] for p in field[0]}
#inf.update(p[1] for p in field[-1])
#inf.update(r[0][1] for r in field)
#inf.update(r[-1][1] for r in field)
#print()
#print(inf)
#print()
#
#for i in l:
    #if i[0] not in inf:
        #print(i)


print(sum(y < distance for x in field for y in x))

