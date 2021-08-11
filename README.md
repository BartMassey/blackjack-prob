# Blackjack Probability Simulators
Bart Massey 2021

Inspired by
[this Reddit post](https://www.reddit.com/r/dailyprogrammer_ideas/comments/p04977/probability_for_blackjack_medium/),
I wrote two Python 3 programs that calculate the probability
of getting a
[blackjack](https://en.wikipedia.org/wiki/Blackjack) after
drawing *n* cards. Since official Blackjack rules call for a
loss after 5 cards, the programs produce results for 2, 3, 4
and 5 cards.

* `bjs.py` runs one million simulated blackjack games, and
  produces the probability estimates from this simulation.
  The program runs in about 13s on my box, and produced the
  following results in a typical run.

        n wins  trials  percent

        2 48274 1000000 4.8274
        3 75948 1000000 7.5948
        4 39647 1000000 3.9647
        5 12273 1000000 1.2273

  Because randomness, results will vary slightly from run to
  run: they appear to be good to a little better than two
  places.

* `bjp.py` computes the exact probabilities by effectively
  simulating each possible five-card draw. In principle,
  there are about 312 million possible draws. However, the
  program uses some pruning and combinatoric tricks to
  improve the runtime, and only evaluates about 57M draws.
  The program runs in about 56s on my box. Here are the
  exact probabilities: *wins / trials* is exact,
  but the percentages are rounded.

        n wins  trials  percent

        2 128 2652 4.826546003016591
        3 10152 132344 7.67091821314151
        4 257280 6424544 4.004642197173839
        5 3794208 311875200 1.2165789392680149

Getting the simulation and the exact calculation to match
reasonably is always the challenge in this kind of problem.
That they match well provides decent evidence that they are
both right.

## License

This work is available under the "MIT License". Please see
the file `LICENSE` in this distribution for license terms.
