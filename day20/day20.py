from collections import defaultdict


class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dist = 1e9
        self.adj = []


    def __repr__(self, d = False):
        if d:
            return '{},{}:{}:{}'.format(self.x, self.y, [(r.x, r.y) for r in self.adj], self.dist)
        else:
            return '{},{}:{}'.format(self.x, self.y, [(r.x, r.y) for r in self.adj])


def add_room(curr, d):
    pt = directions[d](curr.x, curr.y)
    if pt in floor:
        new_room = floor[pt]
    else:
        new_room = Room(pt[0], pt[1])
        floor[pt] = new_room

    if curr not in new_room.adj:
        new_room.adj.append(curr)
    if new_room not in curr.adj:
        curr.adj.append(new_room)

    return new_room


def p(d=False):
    for r in floor.values():
        print(r.__repr__(d))
    print('='*10)


with open('./input.txt') as f:
    r = f.read()

debug = False
if debug:
    r = '(N|E|S|W)'*10
r = '(N|E|S|W)'*10


directions = {
        'N': lambda x,y: (x, y+1),
        'E': lambda x,y: (x+1, y),
        'S': lambda x,y: (x,y-1),
        'W': lambda x,y: (x-1, y)}

start = Room(0,0)
start.dist = 0
floor = {(0,0): start}
head_rooms = [start]
staged_rooms = []
stack = []

# Build Map
for i, c in enumerate(r):
    print(len(head_rooms))
    #if len(head_rooms) > 1:
    if debug:
        print('='*10)
        print(c)
        print('hr', head_rooms)
        print('s',stack)
        print('sr',staged_rooms)
        #p()
    if c in directions:
        for h in range(len(head_rooms)):
            head_rooms[h] = add_room(head_rooms[h], c)

    elif c == '(':
        stack.append(head_rooms.copy())
        staged_rooms.append([])

    elif c == '|':
        staged_rooms[-1] += head_rooms
        head_rooms = stack[-1].copy()

    elif c == ')':
        head_rooms += staged_rooms.pop()
        head_rooms = list(set(head_rooms))
        stack.pop()


# Fill Map Distances
stack = [floor[(0,0)]]
while stack:
    cur = stack.pop()
    for r in [r for r in cur.adj if r.dist > cur.dist+1]:
        r.dist = cur.dist + 1
        stack.append(r)


print(max(r.dist for r in floor.values()))

print(sum(r.dist >= 1000 for r in floor.values()))
