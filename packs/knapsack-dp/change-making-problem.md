---
title: "Change-making problem"
source: https://en.wikipedia.org/wiki/Change-making_problem
domain: knapsack-dp
license: CC-BY-SA-4.0
tags: knapsack problem, dynamic programming, combinatorial optimization, change making problem
fetched: 2026-07-02
---

# Change-making problem

The **change-making problem** addresses the question of finding the minimum number of coins (of certain denominations) that add up to a given amount of money. It is a special case of the integer knapsack problem, and has applications wider than just currency.

It is also the most common variation of the *coin change problem*, a general case of partition in which, given the available denominations of an infinite set of coins, the objective is to find out the number of possible ways of making a change for a specific amount of money, without considering the order of the coins.

It is weakly NP-hard, but may be solved optimally in pseudo-polynomial time by dynamic programming.

## Mathematical definition

Coin values can be modeled by a set of n distinct positive integer values (whole numbers), arranged in increasing order as *w*1 through *w**n*. The problem is: given an amount W, also a positive integer, to find a set of non-negative (positive or zero) integers {*x*1, *x*2, ..., *x**n*}, with each *x**j* representing how often the coin with value *w**j* is used, which minimize the total number of coins *f*(*W*)

$f(W)=\sum _{j=1}^{n}x_{j}$

subject to

$\sum _{j=1}^{n}w_{j}x_{j}=W.$

## Non-currency examples

An application of change-making problem can be found in computing the ways one can make a nine dart finish in a game of darts.

Another application is computing the possible atomic (or isotopic) composition of a given mass/charge peak in mass spectrometry.

## Methods of solving

### Simple dynamic programming

A classic dynamic programming strategy works upward by finding the combinations of all smaller values that would sum to the current threshold. Thus, at each threshold, all previous thresholds are potentially considered to work upward to the goal amount *W*. For this reason, this dynamic programming approach requires a number of steps that is O(*nW),* where *n* is the number of types of coins.

#### Implementation

The following is a dynamic programming implementation (with Python 3) which uses a matrix to keep track of the optimal solutions to sub-problems, and returns the minimum number of coins, or "Infinity" if there is no way to make change with the coins given. A second matrix may be used to obtain the set of coins for the optimal solution.

```mw
def _get_change_making_matrix(set_of_coins, r: int):
    m = [[0 for _ in range(r + 1)] for _ in range(len(set_of_coins) + 1)]
    for i in range(1, r + 1):
        m[0][i] = float("inf")  # By default there is no way of making change
    return m

def change_making(coins, n: int):
    """This function assumes that all coins are available infinitely.
    if coins are only to be used once, change m[c][r - coin] to m[c - 1][r - coin].
    n is the number to obtain with the fewest coins.
    coins is a list or tuple with the available denominations.
    """
    m = _get_change_making_matrix(coins, n)
    for c, coin in enumerate(coins, 1):
        for r in range(1, n + 1):
            # Just use the coin
            if coin == r:
                m[c][r] = 1
            # coin cannot be included.
            # Use the previous solution for making r,
            # excluding coin
            elif coin > r:
                m[c][r] = m[c - 1][r]
            # coin can be used.
            # Decide which one of the following solutions is the best:
            # 1. Using the previous solution for making r (without using coin).
            # 2. Using the previous solution for making r - coin (without
            #      using coin) plus this 1 extra coin.
            else:
                m[c][r] = min(m[c - 1][r], 1 + m[c][r - coin])
    return m[-1][-1]
```

### Greedy method

For many real-world coin systems, such as those used in the US and many other countries, a greedy algorithm of picking the largest denomination of coin which is not greater than the remaining amount to be made will produce the optimal result. This is not the case for arbitrary coin systems or even some real world systems, though. For instance, if we consider the old (now withdrawn) Indian coin denominations of 5, 10, 20 and 25 paise, then to make 40 paise, the greedy algorithm would choose three coins (25, 10, 5) whereas the optimal solution is two coins (20, 20). Another example is attempting to make 40 US cents without nickels (denomination 25, 10, 1) with similar result — the greedy chooses seven coins (25, 10, and 5 × 1), but the optimal is four (4 × 10). A coin system is called "canonical" if the greedy algorithm always solves its change-making problem optimally. It is possible to test whether a coin system is canonical in polynomial time.

The "optimal denomination problem" is a problem for people who design entirely new currencies. It asks what denominations should be chosen for the coins in order to minimize the average cost of making change, that is, the average number of coins needed to make change. The version of this problem assumed that the people making change will use the minimum number of coins (from the denominations available). One variation of this problem assumes that the people making change will use the "greedy algorithm" for making change, even when that requires more than the minimum number of coins. Most current currencies use a 1-2-5 series, but some other set of denominations would require fewer denominations of coins or a smaller average number of coins to make change or both.
