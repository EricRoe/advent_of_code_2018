with open('./input.txt') as f:
    d = [l.strip() for l in f]

B = d[:796*4:4]
I = d[1:796*4:4]
A = d[2:796*4:4]

B = [[int(s[0][-1]), int(s[1]), int(s[2]), int(s[3][1])] for s in [r.split(',') for r in B]]
I = [(int(s[0]), int(s[1]), int(s[2]), int(s[3])) for s in [r.split() for r in I]]
A = [[int(s[0][-1]), int(s[1]), int(s[2]), int(s[3][1])] for s in [r.split(',') for r in A]]

d = d[796*4+2:]
d = [list(map(int, s)) for s in [dd.split() for dd in d]]


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

instructions = [addr, addi, bori, banr, bani, setr, seti, gtir, gtri, borr, gtrr, mulr, eqir, muli, eqri, eqrr]


#Part One
total = 0
for i in range(len(B)):
    ti = 0
    for inst in instructions:
        b = B[i]
        ii = I[i]
        a = A[i]
        r = inst(*I[i][1:], B[i].copy())

        eq = [exp == act for exp, act in zip(a, r)]

        if all(eq):
            ti += 1

    total += 1 if ti >= 3 else 0

print(total)


#Part Two
found = {}
while len(found) < 16:
    for i in range(len(B)):
        ti = []
        for f in instructions:
            b = B[i]
            ii = I[i]
            a = A[i]
            r = f(*I[i][1:], B[i].copy())

            eq = all(exp == act for exp, act in zip(a, r))

            if eq:
                ti.append((ii, f))

        if len(ti) == 1:
            found[ti[0][0][0]] = ti[0][1]
            instructions.remove(ti[0][1])

    remove = [i for i,v in enumerate(I) if v[0] in found.keys()]
    remove.sort(reverse=True)

    for i in remove:
        B.pop(i)
        I.pop(i)
        A.pop(i)


r = [0, 0, 0, 0]
for i in d:
    r = found[i[0]](*i[1:], r)
print(r[0])


