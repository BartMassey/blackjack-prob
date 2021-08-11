nsim = 1000000

import random

deck = list(range(52))

def value(card):
    rank = card % 13
    if rank >= 2 and rank <= 9:
        return {rank}
    if rank == 0:
        return {1, 11}
    return {10}

bj_cards = [0] * 6

def game():
    global deck
    random.shuffle(deck)
    score = {0}
    for i, c in enumerate(deck[:5]):
        val = value(c)
        score = {s + v for s in score for v in val if s + v <= 21}
        if 21 in score:
            bj_cards[i] += 1
            return
        if not score:
            return

for _ in range(nsim):
    game()

assert bj_cards[0] == 0
for i in range(1, 5):
    print(i + 1, bj_cards[i], nsim, 100 * bj_cards[i] / nsim)
