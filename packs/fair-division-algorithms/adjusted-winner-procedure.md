---
title: "Adjusted winner procedure"
source: https://en.wikipedia.org/wiki/Adjusted_winner_procedure
domain: fair-division-algorithms
license: CC-BY-SA-4.0
tags: fair division, envy free allocation, cake cutting, proportional share
fetched: 2026-07-02
---

# Adjusted winner procedure

**Adjusted Winner (AW)** is an algorithm for envy-free item allocation. Given two parties and some discrete goods, it returns a partition of the goods between the two parties that is:

1. Envy-free: Each party believes their share of the goods is as good as or better than their opponent's;
2. Equitable: The "relative happiness levels" of both parties from their shares are equal;
3. Pareto-optimal: no other allocation is better for one party and still at least as good for the other party; and
4. Involves splitting at most one good between the parties.

It is the only procedure that can satisfy all four properties simultaneously. Despite this, however, there are no accounts of the algorithm actually being used to resolve disputes.

The procedure was designed by Steven Brams and Alan D. Taylor, and published in their book on fair division and later in a stand-alone book. Adjusted Winning was previously patented in the United States, but expired in 2016.

## Algorithm

Each party is given the list of goods and an equal, fixed number of points to distribute among them. They then assign values to each good and submit their (sealed) list of bids to an arbiter, who assigns each item to its highest bidder.

If the combined value of one party's goods are then greater than the other's, the algorithm then orders the higher-valued-party's goods in increasing order based on the ratio ${\frac {\text{value for higher-combined-value party}}{\text{value for lower-combined-value party}}},$ and begins transferring them from the higher-combined value party to the lower-combined value party until their valuations are almost equal (moving any more goods would cause the lower-combined-value party to now have a higher combined value than the other). The next good is then divided between the parties such that their values become the same.

As an example, if two parties have the following valuations for four goods:

- Alice: 86, 75, 30, 9
- Bob: 19, 81, 60, 40

The goods would first be divided such that Alice receives good 1, while Bob receives goods 2, 3, and 4. At this point, Alice's combined valuation of her goods is 86, while Bob's is 81 + 60 + 40 = 181; as such, Bob's goods are then ordered based on the ratio ${\frac {\text{Bob's valuations}}{\text{Alice's valuations}}}$ , giving

- [Good 2 = ${\frac {81}{75}}$ ], [Good 3 = ${\frac {60}{30}}$ ], [Good 4 = ${\frac {40}{9}}$ ].

Moving Good 2 from Bob to Alice would cause Alice to have a valuation greater than Bob's (161 versus 100), so no goods are transferred. Instead, Good 2 is split between Alice and Bob: Alice receives ${\frac {95}{156}}$ th of the good (approximately 60.9%), while Bob receives ${\frac {61}{156}}$ th (approximately 39.1%). Their valuations now become $86+{\frac {95}{156}}(75)=131.673...$ and $60+40+{\frac {61}{156}}(81)=131.673...$ respectively, which are equal.

## Simulations

There are no cases of Adjusted Winner being used to resolve real-life disputes. However, some studies have simulated how certain disputes would have resulted had the algorithm been used, including

- the Camp David Accords, whose valuation functions were modelled on the relative importance of each issue for Israel and Egypt, and whose theoretical results were similar to the actual agreement;
- For the Israeli–Palestinian conflict;
- For the Spratly Islands dispute;
- the Panama Canal Treaties; and
- the 1980 *Jolis v. Jolis* divorce case.

## Limitations

AW is not a truthful mechanism: a party can gain from spying on its opponent and modifying their reports in order to get a larger share. However, Adjusted Winner always has an approximate Nash equilibrium, and under informed tie-breaking, also a pure Nash equilibrium.

As patented, the algorithm assumes the parties have additive utility functions: the value of their goods is equal to the sum of the individual goods' values. It does not handle, for example, multiple instances of a good with diminishing marginal utilities.

The algorithm also is designed for two parties only; when there are three or more parties, there may be no allocation that is simultaneously envy-free, equitable, and Pareto-optimal. This can be shown by the following example, constructed by J.H.Reijnierse, involving three parties and their valuations:

- Alice: 40, 50, 10
- Bob: 30, 40, 30
- Carl: 30, 30, 40

The only Pareto-optimal and equitable allocation would be the one giving good 1 to Alice, good 2 to Bob, and good 3 to Carl; however, this allocation would not be envy-free since Alice would envy Bob.

Any two of these three properties can be satisfied simultaneously:

- An envy-free and equitable allocation could be found by giving each party an equal amount of each good.
- An envy-free and Pareto-optimal allocation could be found via Pareto-efficient envy-free division or Weller's theorem.
- An equitable and Pareto-optimal allocation could be found via linear programming.

Moreover, it is possible to find an allocation that, while being Pareto-optimal/envy-free or Pareto-optimal/equitable, would minimize the number of objects that have to be shared between two or more parties. This it usually considered the generalization of the Adjusted Winner procedure to three or more parties.

Adjusted Winner is designed for agents with positive valuations over the items. It can be generalized for parties with mixed (positive and negative) valuations, however.

The Brams–Taylor procedure was designed by the same authors, but it is instead a procedure for envy-free cake-cutting: it handles heterogeneous resources ("cake") which are more challenging to divide than Adjusted Winning's homogeneous goods. Accordingly, BT guarantees only envy-freeness, not any other attributes.

The article on Fair division experiments describes some laboratory experiments comparing AW to related procedures.
