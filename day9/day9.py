from collections import defaultdict, deque

p = 471
lm = 72026*100
scores = defaultdict(int)

curi = 0
curm = 1
circle = deque([0])

while curm <= lm:
    if curm % 23 != 0:
        circle.rotate(-2)
        circle.appendleft(curm)
        #curi = (curi + 2) % len(circle)
        #circle.insert(curi, curm)
    else:
        scores[curm % p] += curm
        circle.rotate(7)
        #curi = (curi - 7) % len(circle)
        scores[curm % p] += circle.popleft()
        #circle.remove(circle[curi])
    curm += 1
    if curm % (lm//100) == 0:
        print(curm/lm)



print(max(scores.items(), key = lambda t: t[1]))
