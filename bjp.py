# Compute exact probabilities for achieving a Blackjack in 2..5 cards.
# Bart Massey 2021

from math import factorial, comb

# A basic deck.
deck = set(range(52))

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

# For each number of already-drawn cards, compute the number
# of remaining draws (assuming a 5-card draw) "controlled"
# by this count. This allows early termination on blackjack
# or bustout while still keeping the count correct.
derate = [ factorial(i) * comb(52 - (5 - i), i) for i in range(0, 6) ]


# Counts the number of draws at which a position terminated,
# accumulated over all runs of prob21(). This gives an
# estimate of the pruning speedup.
ndraws = 0

# Given a current deck of undrawn cards, a set of cur possible
# total scores, and the number of cards remaining to be drawn
# for this probability, return the number of winning hands
# and the number of hands considered.
#
# This statement is a bit confusing: see the code for details.
def prob21(deck, cur, ncards):
    global ndraws

    # We have reached the target number of draws.
    # Return whether or not we just reached a blackjack,
    # and count 1.
    if ncards == 0:
        ndraws += 1
        if 21 in cur:
            return 1, 1
        else:
            return 0, 1

    # We have busted out, or hit blackjack early.
    # Return zero, and count the number of hands
    # that would have been evaluated if we had
    # continued to the root.
    if not cur or 21 in cur:
        ndraws += 1
        return 0, derate[ncards]

    # We are still playing. Accumulate wins and counts from
    # all possible successive positions.
    nw, nt = 0, 0
    for c in deck:
        v = value(c)
        # Update the possible scores with all non-busted possibilities
        # given the value of the current drawn card.
        next_cur = { v1 + s for v1 in v for s in cur if v1 + s <= 21 }
        # Remove the drawn card from the deck.
        next_deck = deck - {c}
        # Continue the calculation.
        w, t = prob21(next_deck, next_cur, ncards - 1)
        # Update the totals
        nw += w
        nt += t
    # Return accumulated counts.
    return nw, nt

for i in range(2, 6):
    w, t = prob21(deck, {0}, i)
    print(i, w, t, 100 * w / t)
print(ndraws)
