n = '330121'

nn = [int(c) for c in n]

recipes = [3,7]
elves = [0,1]

def new(i):
    s = str(i)
    for c in s:
        recipes.append(int(c))


def step():
    new(sum(recipes[e] for e in elves))
    for i in range(len(elves)):
        elves[i] = (elves[i] + 1 + recipes[elves[i]]) % len(recipes)

t=0
while True:
    t +=1
    if t%1000 == 0:
        print(t)
    step()
    if len(recipes) > len(n) and (recipes[-1*len(n):] == nn or recipes[-1*len(n)-1:-1] == nn):
        break

print(len(recipes) - len(n))

