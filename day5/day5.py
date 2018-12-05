with open('./input.txt') as f:
    data = [line.strip() for line in f]

def react(s):
    for i in range(len(s)-1):
        if s[i][1] == s[i+1][1] and s[i][0] != s[i+1][0]:
            s.pop(i)
            s.pop(i)
            return s
    return s

st = data[0]
#st = 'dabAcCaCBAcCcaDA'
s = [(c, c.lower()) for c in st]

def partOne(s):
    while True:
       c = react(s.copy())
       if c == s:
           break
       if len(c) %100 == 0:
           print(len(c))
       s = c
    return len(s)

def partTwo(s):
    d = dict((i, 0) for i in set(l.lower() for (c, l) in s))

    for k in d.keys():
        ss = []
        for c in s:
            if c[1] != k:
                ss.append(c)

        while True:
            sss = react(ss.copy())
            if sss == ss:
                d[k] = len(ss)
                break
            if len(ss)%1000 == 0:
                print(len(ss))
            ss = sss

        print(k)

    print(min(d.items(), key=lambda t: t[1]))

#print(partOne(s.copy()))

partTwo(s.copy())
