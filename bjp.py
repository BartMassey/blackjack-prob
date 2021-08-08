deck = set(range(52))

def value(card):
    rank = card % 13
    if rank >= 2 and rank <= 9:
        return {rank}
    if rank == 0:
        return {1, 11}
    return {10}

def prob21(deck, cur, ncards):
    if ncards == 0:
        if 21 in cur:
            return (1, 1)
        else:
            return (0, 1)
    cur = {c for c in cur if c <= 21}
    if 21 in cur or len(cur) == 0:
        return (0, 1)
    nw, nt = 0, 0
    for c in deck:
        v = value(c)
        next_cur = { v1 + s for v1 in v for s in cur }
        next_deck = deck - {c}
        w, t = prob21(next_deck, next_cur, ncards - 1)
        nw += w
        nt += t
    return (nw, nt)

for i in range(2, 6):
    w, t = prob21(deck, {0}, i)
    print(i, w, t, 100 * w / t)
