# Compute exact probabilities for achieving a 21 in Blackjack by drawing
# exactly five cards.
# Bart Massey 2021

# A basic deck.
ndeck = 52
deck = list(range(ndeck))

# Blackjack card value, which depends only on rank. Note
# that this is nondeterministic, since aces can be played as
# either 1 or 11.
def value(card):
    rank = card % 13
    # Spot card.
    if rank >= 2 and rank <= 9:
        return {rank}
    # Ace.
    if rank == 0:
        return {1, 11}
    # Face card.
    return {10}


# Generator that produces each unique set of n cards drawn
# from the deck.
def draws(n):
    def drawsi(i, n):
        if n < 0:
            return
        if n == 0:
            yield set()
            return
        for j in range(i, ndeck):
            c = deck[j]
            for r in drawsi(j + 1, n - 1):
                r.add(c)
                yield r

    return drawsi(0, n)

# Check each possible draw for 21.
ndraws = 0
nwins = 0
for cards in draws(5):
    sum = {0}
    for c in cards:
        v = value(c)
        sum = { v1 + s for v1 in v for s in sum if v1 + s <= 21 }
    ndraws += 1
    if 21 in sum:
        nwins += 1

print(5, nwins, ndraws, 100 * nwins / ndraws)

