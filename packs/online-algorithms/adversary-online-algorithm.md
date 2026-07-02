---
title: "Adversary model"
source: https://en.wikipedia.org/wiki/Adversary_(online_algorithm)
domain: online-algorithms
license: CC-BY-SA-4.0
tags: online algorithm, competitive analysis, ski rental problem, list update problem
fetched: 2026-07-02
---

# Adversary model

(Redirected from

Adversary (online algorithm)

)

In computer science, an online algorithm measures its competitiveness against different **adversary models**. For deterministic algorithms, the adversary is the same as the adaptive offline adversary. For randomized online algorithms competitiveness can depend upon the adversary model used.

## Common adversaries

The three common adversaries are the oblivious adversary, the adaptive online adversary, and the adaptive offline adversary.

The **oblivious adversary** is sometimes referred to as the weak adversary. This adversary knows the algorithm's code, but does not get to know the randomized results of the algorithm.

The **adaptive online adversary** is sometimes called the medium adversary. This adversary must make its own decision before it is allowed to know the decision of the algorithm.

The **adaptive offline adversary** is sometimes called the strong adversary. This adversary knows everything, even the random number generator. This adversary is so strong that randomization does not help against it.

## Important results

From S. Ben-David, A. Borodin, R. Karp, G. Tardos, A. Wigderson we have:

- If there is a randomized algorithm that is α-competitive against any adaptive offline adversary then there also exists an α-competitive deterministic algorithm.
- If G is a c-competitive randomized algorithm against any adaptive online adversary, and there is a randomized d-competitive algorithm against any oblivious adversary, then G is a randomized (c * d)-competitive algorithm against any adaptive offline adversary.
