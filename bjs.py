# Estimate probabilities for achieving a Blackjack in 2..5
# cards by simulating games.
# Bart Massey 2021

# Number of simulation runs to perform.
nsim = 1000000

import random

# A basic deck.
deck = list(range(52))

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

# Total number of blackjacks so far, indexed by number of
# cards to get them.
bj_cards = [0] * 6

# Simulate a single game.
def game():
    global deck
    random.shuffle(deck)
    # Keep the running score for the game as a set of
    # possibilities, based on the possible values of any
    # aces encountered.
    score = {0}
    # Draw up to five cards.
    for i, c in enumerate(deck[:5]):
        val = value(c)
        score = {s + v for s in score for v in val if s + v <= 21}

        # Hit a blackjack, so done.
        if 21 in score:
            bj_cards[i] += 1
            return

        # Busted, so done.
        if not score:
            return

# Run out all the simulations.
for _ in range(nsim):
    game()

assert bj_cards[0] == 0
for i in range(1, 5):
    print(i + 1, bj_cards[i], nsim, 100 * bj_cards[i] / nsim)
