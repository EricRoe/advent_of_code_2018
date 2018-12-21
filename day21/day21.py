import re

def addr(a,b,c,r):
    r[c] = r[a]+r[b]
    return r

def addi(a,b,c,r):
    r[c] = r[a]+b
    return r

def mulr(a,b,c,r):
    r[c] = r[a]*r[b]
    return r

def muli(a,b,c,r):
    r[c] = r[a]*b
    return r

def banr(a,b,c,r):
    r[c] = r[a]&r[b]
    return r

def bani(a,b,c,r):
    r[c] = r[a]&b
    return r

def borr(a,b,c,r):
    r[c] = r[a]|r[b]
    return r

def bori(a,b,c,r):
    r[c] = r[a]|b
    return r

def setr(a,b,c,r):
    r[c] = r[a]
    return r

def seti(a,b,c,r):
    r[c] = a
    return r

def gtir(a,b,c,r):
    r[c] = 1 if a > r[b] else 0
    return r

def gtri(a,b,c,r):
    r[c] = 1 if r[a] > b else 0
    return r

def gtrr(a,b,c,r):
    r[c] = 1 if r[a] > r[b] else 0
    return r

def eqir(a,b,c,r):
    r[c] = 1 if a == r[b] else 0
    return r

def eqri(a,b,c,r):
    r[c] = 1 if r[a] == b else 0
    return r

def eqrr(a,b,c,r):
    r[c] = 1 if r[a] == r[b] else 0
    return r

instructions = {'addr':addr, 'addi':addi, 'bori':bori, 'banr':banr,
        'bani':bani, 'setr':setr, 'seti':seti, 'gtir':gtir,
        'gtri':gtri, 'borr':borr, 'gtrr':gtrr, 'mulr':mulr,
        'eqir':eqir, 'muli':muli, 'eqri':eqri, 'eqrr':eqrr}


with open('./input.txt') as f:
    program = [l.strip() for l in f]

ip = int(program.pop(0)[-1])

program = [(l[:4], *re.findall('-?\d+', l)) for l in program]
program = [(l[0], int(l[1]), int(l[2]), int(l[3])) for l in program]

r = [0] + [0]*5
t = 0
seen = set()
while True:
    if r[ip] == 28:
        if r[1] in seen:
            print('\nduplicate v')
        seen.add(r[1])
        print(program[r[ip]], r)

    r = instructions[program[r[ip]][0]](*program[r[ip]][1:], r)

    t += 1
    r[ip] += 1
    if r[ip] > len(program) or 0 > r[ip]:
        break

print(t)
print(r)

