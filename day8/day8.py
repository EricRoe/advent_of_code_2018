with open('./input.txt') as f:
    d = f.readline().split()
    d = [int(i) for i in d]


#test = [2,3,0,3,10,11,12,1,1,0,1,99,2,1,1,2]

def get(tree):
    #print(tree)
    if not tree[0]:
    #    print('base ', tree[2:tree[1]+2])
        return (2 + tree[1], tree[2:tree[1]+2]) # skiplen, meta
    else:
        skiplen = 0
        ch_meta = []
        meta = []
        for i in range(tree[0]):
            s, m = get(tree[2+skiplen:])
            skiplen += s
            ch_meta.append(m)
        refs = tree[skiplen+2:skiplen+tree[1]+2]
        for i in refs:
            if not i or i > len(ch_meta):
                continue
            else:
                meta += ch_meta[i-1]
    #    print('else ', tree[skiplen+2:skiplen+tree[1]+1])
        return (skiplen + tree[1] + 2, meta)
_, meta = get(d)
print(sum(meta))
