from collections import defaultdict


class Room:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dist = 1e9
        #self.adj = []


    def __repr__(self):
        #return '{}:{}:{}:{}'.format(self.x, self.y, [(r.x, r.y) for r in self.adj], self.dist)
        return '{}:{}:{}'.format(self.x, self.y,  self.dist)


def add_room(curr, d):
    pt = directions[d](curr.x, curr.y)
    if pt in floor:
        new_room = floor[pt]
    else:
        new_room = Room(pt[0], pt[1])
        floor[pt] = new_room

    #if curr not in new_room.adj:
        #new_room.adj.append(curr)
    #if new_room not in curr.adj:
        #curr.adj.append(new_room)
    new_room.dist = min(curr.dist + 1, new_room.dist)

    return new_room


def p():
    for r in floor.values():
        print(r)
    print('='*10)


with open('./input.txt') as f:
    r = f.read()
#r = '^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$'


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

for i, c in enumerate(r):
    if not i % 10:
        print('='*10)
        print(100*i//len(r))
        print('hr', len(head_rooms))
        print('s',len(stack))
        print('sr',len(staged_rooms))
    #p()
    if c in directions:
        for h in range(len(head_rooms)):
            head_rooms[h] = add_room(head_rooms[h], c)

    elif c == '(':
        stack.append(head_rooms.copy())
        staged_rooms.append([])

    elif c == '|':
        staged_rooms[-1] += head_rooms
        head_rooms = stack[-1]

    elif c == ')':
        head_rooms += staged_rooms.pop()
        head_rooms = list(set(head_rooms))
        stack.pop()


print(max(r.dist for r in floor.values()))
