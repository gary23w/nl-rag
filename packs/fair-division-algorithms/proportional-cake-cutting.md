---
title: "Proportional cake-cutting"
source: https://en.wikipedia.org/wiki/Proportional_cake-cutting
domain: fair-division-algorithms
license: CC-BY-SA-4.0
tags: fair division, envy free allocation, cake cutting, proportional share
fetched: 2026-07-02
---

# Proportional cake-cutting

A **proportional cake-cutting** is a kind of fair cake-cutting. It is a division of a heterogeneous resource ("cake") that satisfies the proportionality criterion, namely, that every partner feels that their allocated share is worth at least 1/*n* of the total.

Two assumptions are typically made when proportional division is discussed:

- The valuations of the partners are *non-atomic*, i.e., there are no indivisible elements with positive value.
- The valuations of the partners are *additive*, i.e., when a piece is divided, the value of the piece is equal to the sum of its parts.

## Formal definitions

The cake is denoted by C . There are n people. Each person i has a value function $V_{i}$ . A partition of the cake, $X_{1}\sqcup \cdots \sqcup X_{n}=C$ , is called *proportional* if:

> $V_{i}(X_{i})\geq V_{i}(C)/n$ for every person $i\in \{1,\ldots ,n\}$ .

## Procedures

For two people, divide and choose is the classic solution. One person divides the resource into what they believe are equal halves, and the other person chooses the half they prefer. The non-atomicity assumption guarantees that the cutter can indeed cut the cake to two equal pieces; the additivity assumption guarantees that both partners value their pieces as at least 1/2.

There are many ways to extend this procedure to more than 2 people. Each way has its own advantages and disadvantages.

### Simple procedures

**Last diminisher** is the earliest proportional division procedure developed for *n* people:

- One of the partners is asked to draw a piece which he values as at least 1/*n*.
- The other partners in turn have the option to claim that the current piece is actually worth more than 1/*n*; in that case, they are asked to diminish it such that the remaining value is 1/*n* according to their own valuation.
- The last partner to diminish the current piece, receives it.
- The remaining cake is then divided in the same way among the remaining *n* − 1 people.

By induction, it is possible to prove that each partner following the rules is guaranteed to get a value of 1/*n*, regardless of what the other partners do. This is a discrete procedure that can be played in turns. In the worst case, $n\times (n-1)/2=O(n^{2})$ actions are needed: one action per player per turn. However, most of these actions can be done on paper; only *n* − 1 cuts of the cake are actually needed. Hence, it is possible for all the pieces to be contiguous under certain circumstances.

The **moving-knife procedure** is a continuous-time version of Last Diminisher.

- A knife is passed over the cake, perpendicular to the direction of travel, from left end toward the right end.
- Any person says 'stop' when they think $1/n$ of the cake is to the left of the knife. (The call stops the knife at what the caller thinks is fair and any delay in calling would allow the other to take what would by then have grown to be too much.) Then the cake is cut and they get that piece.
- This is repeated with the remaining cake and partners. The last partner gets the remainder of the cake.

**Fink protocol** is an algorithm that continues the division to successively smaller "equal" portions.

- The first partner divides the resource into what they believe are equal halves.
- The second then chooses a half, leaving the remainder for the first partner
- Each of these two partners then divide their respective portions into thirds.
- The third partner picks two of the resulting portions: one from the first partner and one from the second partner.
- If there are four partners, each of the first three partners divides their portions into fourths, and the process continues.

The advantage of this protocol is that it can be executed online – as new partners enter the party, the existing division is adjusted to accommodate them, without needing to restart the entire division process. The disadvantage is that the each partner receives a large number of disconnected pieces rather than a single connected piece.

**Lone divider** is a procedure based on an equal partition made by a single agent. Its advantage is that it can be generalized to yield a symmetric fair cake-cutting.

### Recursive halving

Using a divide-and-conquer strategy, it is possible to achieve a proportional division in time O(*n* log *n*). For simplicity the procedure is described here for an even number of partners, but it can be easily adapted to any number of partners:

- Each partner is asked to draw a line dividing the cake to two pieces that he believes to be of equal value. The cuts are required to be non-intersecting; a simple way to guarantee this is to allow only horizontal lines or only vertical lines.
- The algorithm sorts the *n* lines in increasing order and cuts the cake in the median of the lines. E.g., if there are 4 partners that draw lines at *x* = 1, *x* = 3, *x* = 5 and *x* = 9, then the algorithm cuts the cake vertically at *x* = 4.
- The algorithm assigns to each of the two halves *n*/2 partners – the partners whose line is inside that half. E.g., the partners that drew lines at *x* = 1 and *x* = 3 are assigned to the western half and the other two partners are assigned to the eastern half. Each half is divided recursively among the *n*/2 partners assigned to it.

It is possible to prove by induction that every partner playing by the rules is guaranteed a piece with a value of at least 1/*n*, regardless of what the other partners do.

Thanks to the divide-and-choose strategy, the number of iterations is only O(log *n*), in contrast to O(*n*) in the Last Diminisher procedure. In each iteration, each partner is required to make a single mark. Hence, the total number of marks required is O(*n* log *n*).

This algorithm has a randomized version which can be used to reduce the number of marks; see Even-Paz algorithm.

### Selection procedures

A different approach to cake-cutting is to let every partner draw a certain number of pieces depending on the number of partners, *p*(*n*), and give each partner one of his selected pieces, such that the pieces do not overlap.

As a simple example of a selection procedure, assume the cake is a 1-dimensional interval and that each partner wants to receive a single contiguous interval. Use the following protocol:

1. Each partner privately partitions the cake to *n* intervals that he considers to be of equal value; these are called *candidate pieces*.
2. The protocol orders the *n*^2 candidates by increasing order of their eastern (from west to east) and select the interval with the most western eastern end. This interval is called a *final piece*.
3. The protocol gives the final piece to its owner and remove all candidates intersected by it. Step #2 is then repeated with the remaining intervals of the remaining *n* − 1 partners.

The selection rule in step #2 guarantees that, at each iteration, at most one interval of every partner is removed. Hence, after each iteration the number of intervals per partners is still equal to the number of partners, and the process can proceed until every partner receives an interval.

This protocol requires each partner to answer *n* queries so the query complexity is O(*n*2), similarly to Last Diminisher.

#### Randomized versions

It is possible to use randomization in order to reduce the number of queries. The idea is that each partner reports, not the entire collection of *n* candidates but only a constant number *d* of candidates, picked at random. The query complexity is O(*n*), which is obviously the best possible. In many cases, it will still be possible to give each partner a single candidate such that the candidates do not overlap. However, there are scenarios in which such an allocation will be impossible.

We can still cut a cake using O(*n*) queries if we make several compromises:

- Instead of guaranteeing full proportionality, we guarantee *partial proportionality*, i.e. each partner receives a certain constant fraction *f*(*n*) of the total value, where *f*(*n*)<1/*n*.
- Instead of giving each partner a single contiguous piece, we give each partner a union of one or more disjoint pieces.

The general scheme is as follows:

1. Each partner privately partitions the cake to *an* pieces of equal subjective value. These *n⋅an* pieces are called *candidate pieces*.
2. Each partner picks 2*d* candidate pieces uniformly at random, with replacement. The candidates are grouped into *d* pairs, which the partner reports to the algorithm. These *n⋅d* pairs are called *quarterfinal brackets*.
3. From each quarterfinal bracket, the algorithm selects a single piece – the piece that intersects the fewer number of other candidate pieces. These *n⋅d* pieces are called *semifinal pieces*.
4. For each partner, the algorithm selects a single piece; they are called *final pieces*. The final pieces are selected such that each point of the cake is covered by at most 2 final pieces (see below). If this succeeds, proceed to step #5. If this fails, start over at step #1.
5. Each part of the cake which belongs to only a single final piece, is given to the owner of that piece. Each part of the cake which belongs to two final pieces, is divided proportionally by any deterministic proportional division algorithm.

The algorithm guarantees that, with probability O(1*a*2), each partner receives at least half of one of his candidate pieces, which implies (if the values are additive) a value of at least 1/2*an*. There are O(*n*) candidate pieces and O(*n*) additional divisions in step #5, each of which takes O(1) time. Hence the total run-time of the algorithm is O(*n*).

The main challenge in this scheme is selecting the final pieces in step #4. For details, see Edmonds–Pruhs protocol.

## Hardness results

The hardness results are stated in terms of the Robertson–Webb query model, i.e., they relate to procedures asking the agents two types of queries: "Evaluate" and "Mark".

Every deterministic proportional division procedure for *n*≥3 partners must use at least *n* queries, even if all valuations are identical.

Moreover, every deterministic or randomized proportional division procedure assigning each person a contiguous piece must use Ω(*n* log *n*) actions.

Moreover, every deterministic proportional division procedure must use Ω(*n* log *n*) queries, even if the procedure is allowed to assign to each partner a piece that is a union of intervals, and even if the procedure is allowed to only guarantee *approximate fairness*. The proof is based on lower bounding the complexity to find, for a single player, a piece of cake that is both rich in value, and thin in width.

These hardness results imply that recursive halving is the fastest possible algorithm for achieving full proportionality with contiguous pieces, and it is the fastest possible deterministic algorithm for achieving even partial proportionality and even with disconnected pieces. The only case in which it can be improved is with randomized algorithms guaranteeing partial proportionality with disconnected pieces.

If the players are able to cut with only finite precision, then the Ω(n log n) lower bound also includes randomized protocols.

The following table summarizes the known results:

| Proportionality (full/partial) | Pieces (contiguous/disjoint) | Protocol type (deterministic/randomized) | Queries (exact/approximate) | #queries |
|---|---|---|---|---|
| full | contiguous | det. | exact | O(*n* log *n*) Ω(*n* log *n*) |
| full | contiguous | det. | approximate | Ω(*n* log *n*) |
| full | contiguous | rand. | exact | O(*n* log *n*) Ω(*n* log *n*) |
| full | contiguous | rand. | approximate | Ω(*n* log *n*) |
| full | disconnected | det. | exact | O(*n* log *n*) Ω(*n* log *n*) |
| full | disconnected | det. | approximate | Ω(*n* log *n*) |
| full | disconnected | rand. | exact | O(*n* log *n*) |
| full | disconnected | rand. | approximate | Ω(*n* log *n*) |
| partial | contiguous | det. | exact | O(*n* log *n*) Ω(*n* log *n*) |
| partial | contiguous | det. | approximate | Ω(*n* log *n*) |
| partial | contiguous | rand. | exact | O(*n* log *n*) |
| partial | contiguous | rand. | approximate | Ω(*n* log *n*) |
| partial | disconnected | det. | exact | O(*n* log *n*) Ω(*n* log *n*) |
| partial | disconnected | det. | approximate | Ω(*n* log *n*) |
| partial | disconnected | rand. | exact | O(*n*) |
| partial | disconnected | rand. | weakly approx. (error independent of value) | O(*n*) |
| partial | disconnected | rand. | approximate | Ω(*n* log *n*) |

## Variants

### Different entitlements

The proportionality criterion can be generalized to situations in which the entitlements of the partners are not equal. For example, the resource may belong to two shareholders such that Alice holds 8/13 and George holds 5/13. This leads to the criterion of *weighted proportionality* (WPR): there are several weights *wi* that sum up to 1, and every partner *i* should receive at least a fraction *wi* of the resource by their own valuation. Several algorithms can be used to find a WPR division. The main challenge is that the number of cuts may be large, even when there are only two partners.

### Super-proportional division

A *super-proportional division* is a division in which each partner receives strictly more than 1/*n* of the resource by their own subjective valuation.

Of course such a division does not always exist: when all partners have exactly the same value functions, the best we can do is give each partner exactly 1/*n*. So a necessary condition for the existence of a super-proportional division is that not all partners have the same value measure.

The surprising fact is that, when the valuations are additive and non-atomic, this condition is also sufficient. I.e., when there are at least *two* partners whose value function is even slightly different, then there is a super-proportional division in which *all* partners receive more than 1/*n*.

### Adjacency constraint

In addition to the usual constraint that all pieces must be connected, in some cases there are additional constraints. In particular, when the *cake* to divide is a disputed territory lying among several countries, it may be required that the piece allocated to each country is adjacent to its current location. A proportional division with this property always exists and can be found by combining the Last Diminisher protocol with geometric tricks involving conformal mappings.

### Two-dimensional geometric constraints

When the "cake" to be divided is two-dimensional, such as a land-estate or an advertisement space in print or electronic media, it is often required that the pieces satisfy some geometric constraints, in addition to connectivity. For example, it may be required that each piece be a square, a fat rectangle, or generally a fat object. With such fatness constraints, a proportional division usually does not exist, but a partially-proportional division usually exists and can be found by efficient algorithms.

### Economically efficient division

In addition to being proportional, it is often required that the division be economically efficient, i.e., maximize the social welfare (defined as the sum of the utilities of all agents).

For example, consider a cake which contains 500 gram chocolate and 500 gram vanilla, divided between two partners one of whom wants only the chocolate and the other wants only the vanilla. Many cake-cutting protocols will give each agent 250 gram chocolate and 250 gram vanilla. This division is proportional because each partner receives 0.5 of his total value so the normalized social welfare is 1. However, this partition is very inefficient because we could give all the chocolate to one partner and all the vanilla to the other partner, achieving a normalized social welfare of 2.

The *optimal proportional division* problem is the problem of finding a proportional allocation that maximizes the social welfare among all possible proportional allocations. This problem currently has a solution only for the very special case where the cake is a 1-dimensional interval and the utility density functions are linear (i.e. *u*(*x*) = *Ax* +  *B*). In general the problem is NP-hard. When the utility functions are not normalized (i.e. we allow each partner to have a different value for the whole cake), the problem is even NP-hard to approximate within a factor of 1/√*n*.

### Truthful division

Truthfulness is not a property of a division but rather a property of the protocol. All protocols for proportional division are *weakly truthful* in that each partner acting according to his true valuation is guaranteed to get at least 1/*n* (or 1/*an* in case of a partially proportional protocol) regardless of what the other partners do. Even if all other partners make a coalition with the only intent to harm him, he will still receive his guaranteed proportion.

However, most of the protocols are not *strongly truthful* in that some partners may have an incentive to lie in order to receive even more than the guaranteed share. This is true even for the simple divide and choose protocol: if the cutter knows the preferences of the chooser, he can cut a piece which the chooser values as slightly less than 1/2, but which the cutter himself values as much more than 1/2.

There are truthful mechanisms for achieving a perfect division; since a perfect division is proportional, these are also truthful mechanisms for proportional division.

These mechanisms can be extended to provide a super-proportional division when it exists:

1. Ask each partner to report his entire value measure.
2. Pick a random partition (see for more details).
3. If the random partition happens to be super-proportional according to the reported value measures, then implement it. Otherwise, use a truthful mechanism for providing a perfect division.

When a super-proportional division exists, there is a positive chance that it will be picked in step 2. Hence the expected value of every truthful partner is strictly more than 1/*n*. To see that the mechanism is truthful, consider three cases: (a) If the picked partition is truly super-proportional, then the only possible result of lying is to mislead the mechanism to think that it is not; this will make the mechanism implement a perfect division, which will be worse for all partners including the liar. (b) If the picked partition is not super-proportional because it gives only the liar a value of 1/*n* or less, then the only effect of lying is to make the mechanism think that the partition *is* super-proportional and implement it, which only harms the liar himself. (c) If the picked partition is truly not super-proportional because it gives another partner a value of 1/*n* or less, then lying has no effect at all since the partition will not be implemented in any case.

### Proportional division of chores

When the resource to divide is undesirable (like in chore division), a proportional division is defined as a division giving each person *at most* 1/*n* of the resource (i.e. the sign of inequality is inversed).

Most algorithms for proportional division can be adapted to chore division in a straightforward way.
