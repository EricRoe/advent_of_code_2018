r = [0]*6
six = True

while True:
    if six:
        r[5] = r[1] | 65536
        r[1] = 858263
        six = False

    r[2] = r[5] % 256
    r[1] = ((r[1] + r[2]) * 65899) % 16777216

    if 256 > r[5]:
        print(r[1])
        if r[1] == r[0]:
            break
        six = True

    while (r[2] + 1) * 256 > r[5]:
        r[2] += 1
    r[5] = r[2]
