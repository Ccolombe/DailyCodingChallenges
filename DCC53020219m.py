"""
This problem was asked by Square.

Assume you have access to a function toss_biased() which returns 0 or 1 with a probability that's not 50-50
(but also not 0-100 or 100-0). You do not know the bias of the coin.

Write a function to simulate an unbiased coin toss.
"""

# first lets simulate a biased coin.
import math
from random import random


class BiasedCoin:

    def __init__(self):
        """ Construct a coin object and give it a random biased probability of heads."""
        self.prob_heads = random()

    def flip(self):
        """ Generate a random number in [0,1] to compare to our biased probability."""
        rand_roll = random()

        if rand_roll < self.prob_heads:
            return 1
        else:
            return 0


# Okay now that we have created our biased coin. We want to somehow use it to simulate an unbiased coin toss.
# How might we go about solving this? Suppose we knew the coins bias. Which we could argue that we could eventually find
# out.

# IDEA: Use two rolls and let the sequence HT-> H' and TH -> T'. Both H' and T' have the same probability of occurring.
# Reroll until this one or the other happens.
class RegularCoin:

    def __init__(self):
        self.myBiasedCoin = BiasedCoin()
        print("Hi, I'm a regular coin. No bias here!")

    def flip(self):
        """ Return 1 for heads and 0 for tails"""

        rollOne = None
        rollTwo = None

        while (rollOne == rollTwo):

            rollOne = self.myBiasedCoin.flip()
            rollTwo = self.myBiasedCoin.flip()

            if rollOne == 1 and rollTwo == 0:
                return 1
            elif rollOne == 0 and rollTwo == 1:
                return 0


if __name__ == '__main__':

    """Let's try out our instance of a biased coin!"""
    myCoin = BiasedCoin()
    numTrials = 10000
    counter = 0

    for trial in range(numTrials):
        if myCoin.flip():
            counter += 1

    print("The approximate biased probability is:", '%.4f' % (counter / numTrials), "but the real probability was",
          '%.4f' % myCoin.prob_heads)

    """Let's try out our instance of an unbiased coin!"""
    myRegCoin = RegularCoin()

    numTrials = 100000
    counter = 0

    for trial in range(numTrials):
        if myRegCoin.flip():
            counter += 1

    print("The approximate unbiased probability is:", '%.4f' % (counter / numTrials), " Not too bad for using a coin with",
          "probability of heads of", '%.4f' % myRegCoin.myBiasedCoin.prob_heads)
