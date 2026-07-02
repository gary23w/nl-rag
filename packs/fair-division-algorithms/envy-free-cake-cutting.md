---
title: "Envy-free cake-cutting"
source: https://en.wikipedia.org/wiki/Envy-free_cake-cutting
domain: fair-division-algorithms
license: CC-BY-SA-4.0
tags: fair division, envy free allocation, cake cutting, proportional share
fetched: 2026-07-02
---

# Envy-free cake-cutting

An **envy-free cake-cutting** is a kind of fair cake-cutting. It is a division of a heterogeneous resource ("cake") that satisfies the envy-free criterion, namely, that every partner feels that their allocated share is at least as good as any other share, according to their own subjective valuation.

Unsolved problem in computer science

What is the runtime complexity of envy-free cake-cutting?

More unsolved problems in computer science

When there are only two partners, the problem is easy and was solved in antiquity by the divide and choose protocol. When there are three or more partners, the problem becomes much more challenging.

Two major variants of the problem have been studied:

- **Connected pieces**, e.g. if the cake is a 1-dimensional interval then each partner must receive a single sub-interval. If there are n partners, only $n-1$ cuts are needed.
- **General pieces**, e.g. if the cake is a 1-dimensional interval then each partner can receive a union of disjoint sub-intervals.

## Short history

Modern research into the fair cake-cutting problem started in the 1940s. The first fairness criterion studied was proportional division, and a procedure for *n* partners was soon found.

The stronger criterion of envy-freeness was introduced into the cake-cutting problem by George Gamow and Marvin Stern in 1950s.

A procedure for three partners and general pieces was found in 1960. A procedure for three partners and connected pieces was found only in 1980.

Envy-free division for four or more partners had been an open problem until the 1990s, when three procedures for general pieces and a procedure for connected pieces were published. All these procedures are *unbounded* - they may require a number of steps which is not bounded in advance. The procedure for connected pieces may even require an *infinite* number of steps.

Two lower bounds on the run-time complexity of envy-freeness were published in the 2000s.

- For general pieces, the lower bound is Ω(*n*2).
- For connected pieces the lower bound is infinity – there is provably no finite protocol for three or more partners.

In the 2010s, several approximation procedures and procedures for special cases were published. The question whether bounded-time procedures exist for the case of general pieces had remained open for a long time. The problem was finally solved in 2016. Haris Aziz and Simon Mackenzie presented a discrete envy-free protocol that requires at most $n^{n^{n^{n^{n^{n}}}}}$ or $n\uparrow \uparrow 6$ queries. There is still a very large gap between the lower bound and the procedure. As of October 2024, the exact run-time complexity of envy-freeness is still unknown.

For the case of connected pieces, it was noted that the hardness result assumes that the entire cake must be divided. If this requirement is replaced by the weaker requirement that every partner receives a proportional value (at least 1/*n* of the total cake value according to their own valuation), then a bounded procedure for three partners is known, but it has remained an open problem whether there exist bounded-time procedures for four or more partners.

## Connected pieces

### Existence proof

An envy-free division for *n* agents with connected pieces always exists under the following mild assumptions:

- No agent prefers an empty piece over a non-empty piece.
- The preferences of the agents are continuous.

Note that it is *not* required that the preferences of the agents are represented by an additive function.

The main concept in the proof is the *simplex of partitions*. Suppose the cake is the interval [0,1]. Each partition with connected pieces can be uniquely represented by *n*−1 numbers in [0,1] which represent the cut locations. The union of all partitions is a simplex.

For each partition, each agent has one or more pieces which they weakly prefer. E.g., for the partition represented by "0.3,0.5", one agent may prefer piece #1 (the piece [0,0.3]) while another agent might prefer piece #2 (the piece [0.3,0.5]) while a third agent might prefer both piece #1 and piece #2 (which means that they are indifferent between them but like any of them more than piece #3).

For every agent, the partition simplex is covered by *n* parts, possibly overlapping at their boundaries, such that for all partitions in part *i*, the agent prefers piece *i*. In the interior of part *i*, the agent prefers *only* piece *i*, while in the boundary of part *i*, the agent also prefers some other pieces. So for every *i*, there is a certain region in the partition simplex in which at least one agent prefers only piece *i*. Call this region *U**i*. Using a certain topological lemma (that is similar to the Knaster–Kuratowski–Mazurkiewicz lemma), it is possible to prove that the intersection of all *U**i*'s is non-empty. Hence, there is a partition in which every piece is the unique preference of an agent. Since the number of pieces equals the number of agents, we can allocate each piece to the agent that prefers it and get an envy-free allocation.

### Procedures

For three agents, an envy-free division can be found using several different procedures:

- The Stromquist moving-knives procedure uses four simultaneously-moving knives - one moved by a referee and another one for each agent.
- Barbanel–Brams moving-knives procedure uses two simultaneously-moving knives.
- The Robertson–Webb rotating-knife procedure can be used when the cake is two-dimensional, and uses only a single moving-knife.

These are continuous procedures - they rely on people moving knives continuously and simultaneously. They cannot be executed in a finite number of discrete steps.

For *n* agents, an envy-free division can be found by Simmons' cake-cutting protocol. The protocol uses a *simplex of partitions* similar to the one used in Stromquist's existence proof. It generates a sequence of partitions which converges to an envy-free partition. The convergence might take infinitely many steps.

It is not a coincidence that all these algorithms may require infinitely many queries. As we show in the following subsection, it may be impossible to find an envy-free cake-cutting with connected pieces with a finite number of queries.

### Hardness result

An envy-free division with connected pieces for 3 or more agents cannot be found by a finite protocol in the Robertson–Webb query model. The reason this result doesn't contradict the previously mentioned algorithms is that they are not finite in the mathematical sense.

The impossibility proof uses a *rigid measure system* (RMS) – a system of *n* value measures, for which an envy-free division must cut the cake at very specific locations. Then, finding an envy-free division reduces to finding these specific locations. Assuming the cake is the real interval [0,1], finding an envy-free division using queries to the agents is equivalent to finding a real number in the interval [0,1] using yes/no questions. This might require an infinite number of questions.

A RMS for three agents can be constructed as follows. Let *x*, *y*, *s*, and *t* be parameters satisfying:

- $0<x<y<1,$
- $0<s<1/3<t<1/2,$
- $s+2t=1.$

Construct a set of three measures with these two properties:

1. The density of each measure is always strictly between √2/2 and √2 (so for a given piece, the agents' valuations differ by a factor of less than 2).
2. The values of the pieces determined by *x* and *y* are as in the table:

| Agent | [0,*x*] | [*x*,*y*] | [*y*,1] |
|---|---|---|---|
| A | *t* | *t* | *s* |
| B | *s* | *t* | *t* |
| C | *t* | *s* | *t* |

Then, every envy-free division among Alice Bob and Carl must have cuts at *x* and *y* (there are exactly two such divisions), since all other options lead to envy:

- If *x**≥*x* and *y**≤*y*, and one of the inequalities is strict, then everyone values either the right piece or the left piece more than the middle, so whoever gets the middle will be envious.
- If *x**≤*x* and *y**≥*y*, and one of the inequalities is strict, then both Alice and Bob prefer the middle piece over any other piece, so whoever won't get it out of the two will be envious of the other.
- If cuts are made to the right of *x* and to the right of *y* (say, at *x**>*x* and *y**>*y*), then both Alice and Carl prefer the leftmost piece to the rightmost piece, so Bob must agree to accept the rightmost piece. This means that Bob must value the piece [*x*,*x**] at least twice as much as [*y*,*y**]. But because of the restriction on the value densities, this means that both Alice and Carl value [*y*,*y**] less than twice as much as [*x*,*x**], so they insist on the leftmost piece.
- The fourth case (cuts to the left of *x* and to the left of *y*) is analogous.

For every RMS, every agent *i* and every constant ε>0, there is a slightly different RMS with the following properties:

- The new value measure of agent *i* is completely identical to his old value measure;
- The new value measures of the other two agents are identical to their old value measure everywhere *except* in an ε-neighbourhood of *x* and *y*.

This implies that, if all queries answered so far were outside the *ε*-neighbourhood of *x* and *y*, then agent *i* has no way to know whether we are in the old RMS or in the new RMS.

Equipped with this knowledge, an adversary can trick every envy-free division protocol to go on forever:

1. Start with any RMS, e.g. with parameters *x* = 1/3, *y* = 2/3, *s* = 0.3 and *t* = 0.35.
2. As long as the protocol makes cuts at points other than *x* and *y*, let it continue.
3. Whenever the protocol asks agent *i* to make a cut at *x* or *y*, switch to a different RMS with *x'≠x* and *y'≠y*, making sure that the values are the same for all previously made cuts.

Thus the protocol can never make cuts at the correct *x* and *y* required for an envy-free division.

### Approximations

Since envy-free cake-cutting with connected pieces cannot be done in finite time, cake-cutters have tried to find work-arounds.

One work-around is looking for divisions which are only *approximately-envy-free*. There are two ways to define the approximation - in units of *length* or in units of *value*.

**Length-based approximation** uses the following definitions:

- A *partition* of a cake is represented by the *n* lengths of intervals it creates. So (0.2,0.5,0.3) is a partition of the unit interval to three sub-intervals with lengths 0.2, 0.5 and 0.3 (it is generated by cutting the unit interval at 0.2 and at 0.7).
- A *multi-partition* is a set of several different partitions.
- A multi-partition X is called *envy-free* if there exists a permutation of the partners such that, for every *i*, there exists an element of X such that the *i*-th partner prefers the *i*-th segment.
- A *δ-multi-partition* is a multi-partition in which, for each pair of partitions, the difference between each of their coordinates is at most *δ*. For example: {(0.2+*δ*,0.5,0.3), (0.2,0.5+*δ*,0.3), (0.2,0.5,0.3+*δ*)}.

The parameter *δ* represents the tolerance of the partners in units of length. E.g., if land is divided and the partners agree that a difference of 0.01 meter in the location of the border is not relevant to them, then it makes sense to look for a 0.01-multi-partition which is envy-free. Deng at al present a modification of Simmons' cake-cutting protocol which finds an envy-free *δ*-multi-partition using $O[(1/\delta )^{n-2}]$ queries. Moreover, they prove a lower bound of $\Omega [(1/\delta )^{n-2}/2^{(n-1)(n-2)}]$ queries. Even when the utility functions are given explicitly by polynomial-time algorithms, the envy-free cake-cutting problem is PPAD-complete.

**Value-based approximation** uses the following definitions:

- A partition X is called *ε-envy-free* if there exists a permutation of the partners such that, for every *i*, the value of the *i*-th piece plus *ε* is at least as much as the value of any other piece: $\forall i,j:V_{i}(X_{i})+\varepsilon \geq V_{i}(X_{j})$ .
- A value measure is called Lipschitz continuous if there exists a constant *K* such that, for any pair of intervals, the difference of values between them is at most *K* times the length of their symmetric difference $\exists K:\forall j:|V_{i}(X_{i})-V_{i}(X_{j})|\leq K\cdot \mathrm {length} (X_{i}\setminus X_{j}\cup X_{j}\setminus X_{i})$ .

If all value measures are Lipschitz continuous, then the two approximation definitions are related. Let $\epsilon =2K\delta$ . Then, every partition in an envy-free *δ*-multi-partition is *ε*-envy-free. Hence, Deng et al.'s results prove that, if all partners have Lipschitz continuous valuations, an *ε*-envy-free partition can be found with $\Theta [(1/\epsilon )^{n-2}]$ queries with general valuations.

With additive valuations, for any ε > 0, an ε-envy-free connected cake-cutting requires at least Ω(log ε−1) queries. For 3 agents, an O(log ε−1) protocol exists. For 4 or more agents, the best known protocol requires O(*n* ε−1), which shows an exponential gap in the query complexity. Moreover, although the latter protocol has query complexity polynomial in *n*, its computational complexity is exponential in *n*, even for constant ε. If polynomial-time computation is required, the best-known approximation is $1/3$ -envy-freeness.

**Offline calculation** is a second work-around that finds a totally-envy-free division but only for a restricted class of valuations. If all value measures are polynomials of degree at most *d*, there is an algorithm which is polynomial in *n* and *d*. Given *d*, the algorithm asks the agents *d*+1 evaluation queries, which give *d*+1 points in the graph of the value measure. It is known that *d*+1 points are sufficient to interpolate a polynomial of degree *d*. Hence, the algorithm can interpolate the entire value measures of all agents, and find an envy-free division offline. The number of required queries is $O(n^{2}d)$ .

Another restriction on the valuations is that they are *piecewise-constant* - for each agent, there are at most *m* desired intervals, and the agent's value-density in each interval is constant. Under this assumption, a connected envy-free allocation can be found by solving ${\frac {n\cdot (2mn+n-1)!}{(2mn)!}}\in O(m^{n})$ linear programs. Thus, when *n* is constant, the problem is polynomial in *m*.

**Free disposal** is a third work-around that keeps the requirement that the division be totally envy-free and works for all value measures, but drops the requirement that the entire cake must be divided. I.e, it allows to divide a subset of the cake and discard the remainder. Without further requirements the problem is trivial, since it is always envy-free to give nothing to all agents. Thus, the real goal is to give each agent a strictly positive value. Every cake allocation can be characterized by its level of *proportionality*, which is the value of the least fortunate agent. An envy-free division of the entire cake is also a proportional division, and its proportionality level is at least $1/n$ , which is the best possible. But when free disposal is allowed, an envy-free division may have a lower proportionality level, and the goal is to find an envy-free division with the highest possible proportionality. The currently known bounds are:

- For 3 agents the proportionality is $1/3$ , i.e., an envy-free *and proportional* division is attainable in bounded time.
- For 4 agents the proportionality is $1/7$ .
- For *n* agents, the proportionality is $1/(3n)$ .

It is not known whether there exists a bounded-time envy-free and proportional division procedure for four or more partners with connected pieces.

### Variants

Most procedures for cake-cutting with connected pieces assume that the cake is a 1-dimensional interval and the pieces are 1-dimensional sub-intervals. Often, it is desirable that the pieces have a certain geometric shape, such as a square. With such constraints, it may be impossible to divide the entire cake (e.g., a square cannot be divided to two squares), so we must allow free disposal. As explained above, when free disposal is allowed, the procedures are measured by their level of *proportionality* - the value that they guarantee to all agents. The following results are currently known:

- For two partners sharing a square cake and wanting square pieces the proportionality is $1/4$ , and this is the best that can be guaranteed even without envy.
- For three partners sharing a square cake and wanting square pieces the proportionality is $1/10$ ; the best that can be guaranteed without envy is $1/6$ .

An envy-free division exists even with non-additive value functions, multi-dimensional simplex cake, and the pieces must be polytopes.

## Disconnected pieces

### Procedures

For three partners, the Selfridge–Conway discrete procedure makes an envy-free division with at most 5 cuts. Other procedures using moving knives require fewer cuts:

- The Levmore–Cook moving-knives procedure requires at most 4 cuts;
- The Brams–Taylor–Zwicker rotating-knives procedure for pie-cutting requires at most 3 cuts (this results in three connected pieces when the cake is a circle, but when the cake is an interval there will be four pieces);
- Using the Austin moving-knife procedure for two partners, it is possible to get an envy-free division for 3 partners using at most 3 cuts. This idea is attributed to William Webb.

For four partners, The Brams–Taylor–Zwicker procedure makes an envy-free division with at most 11 cuts. For five partners, a procedure by Saberi and Wang makes an envy-free division with a bounded number of cuts. Both these procedures use Austin's procedure for two partners and general fractions as an initial step. Hence, these procedures should be considered infinite - they cannot be completed using a finite number of steps.

For four or more partners, there are three algorithms which are finite but unbounded - there is no fixed bound on the number of cuts required. There are three such algorithms:

- The Brams–Taylor protocol, first published in a 1995 paper and later in a 1996 book.
- The Robertson–Webb protocol, first published in a 1997 paper and later in a 1998 book.
- The Pikhurko protocol, published in 2000.

Although the protocols are different, the main idea behind them is similar: Divide the cake to a finite but unbounded number of "crumbs", each of which is so small that its value for all partners is negligible. Then combine the crumbs in a sophisticated way to get the desired division. William Gasarch has compared the three unbounded algorithms using ordinal numbers.

The question of whether envy-free cake-cutting can be done in bounded time for four or more partners had been open for many years. It was finally solved in 2016 by Haris Aziz and Simon Mackenzie. Initially they developed a bounded-time algorithm for four partners. Then they extended their algorithm to handle any number of partners. Their algorithm requires at most $n^{n^{n^{n^{n^{n}}}}}$ queries. While this number is bounded, it is very far from the lower bound of $\Omega (n^{2})$ . So the question of how many queries are required for envy-free cake-cutting is still open.

### Approximations and partial solutions

A reentrant variant of the last diminisher protocol finds an additive approximation to an envy-free division in bounded time. Specifically, for every constant $\epsilon >0$ , it returns a division in which the value of each partner is at least the largest value minus $\epsilon$ , in time $n^{2}/\epsilon$ .

If all value measures are *piecewise linear*, there is an algorithm which is polynomial in the size of the representation of the value functions. The number of queries is $O(n^{6}k\ln {k})$ , where k is the number of discontinuities in the derivatives of the value density functions.

### Hardness result

Every envy-free procedure for *n* people requires at least Ω(*n*2) queries in the Robertson–Webb query model. The proof relies on a careful analysis of the amount of information the algorithm has on each partner.

**A.** Assume that the cake is the 1-dimensional interval [0,1], and that the value of the entire cake for each of the partners is normalized 1. In each step, the algorithm asks a certain partner either to *evaluate* a certain interval contained in [0,1], or to *mark* an interval with a specified value. In both cases, the algorithm gathers information only about intervals whose end-points were mentioned in the query or in the reply. Let's call these endpoints *landmarks*. Initially the only landmarks of *i* are 0 and 1 since the only thing the algorithm knows about partner *i* is that *v**i*([0,1])=1. If the algorithm asks partner *i* to evaluate the interval [0.2,1], then after the reply the landmarks of *i* are {0,0.2,1}. The algorithm can calculate *v**i*([0,0.2]), but not the value of any interval whose endpoint is different than 0.2. The number of landmarks increases by at most 2 in each query. In particular, the value of the interval [0,0.2] might be concentrated entirely near 0, or entirely near 0.2, or anywhere in between.

**B.** An interval between two consecutive landmarks of partner *i* is called a *landmark-interval* of partner *i*, When the algorithm decides to allocate a piece of cake to partner *i*, it must allocate a piece whose total value for *i* is at least as large as any landmark-interval of *i*. The proof is by contradiction: suppose there is a certain landmark-interval *J* whose value for *i* is more than the value actually allocated to *i*. Some other partner, say *j*, will necessarily receive some part of the landmark-interval *J*. By paragraph A, it is possible that all the value of interval *J* is concentrated inside the share allocated to partner *j*. Thus, *i* envies *j* and the division is not envy-free.

**C.** Suppose all partners answer all queries *as if* their value measure is uniform (i.e. the value of an interval is equal to its length). By paragraph B, the algorithm may assign a piece to partner *i*, only if it is longer than all landmark-intervals of *i*. At least *n*/2 partners must receive an interval with a length of at most 2/*n*; hence all their landmark-intervals must have a length of at most 2/*n*; hence they must have at least *n*/2 landmark-intervals; hence they must have at least *n*/2 landmarks.

**D.** Each query answered by partner *i* involves at most two new endpoints, so it increases the number of landmarks of *i* by at most 2. Hence, in the case described by paragraph C, the algorithm must ask each of *n*/2 partners, at least *n*/4 queries. The total number of queries is thus at least *n*2/8 = Ω(*n*2).

### Existence proofs and variants

In addition to the general existence proofs implied by the algorithms described above, there are proofs for the existence of envy-free partitions with additional properties:

- There exists an **exact division**, which is in particular envy-free; see Dubins–Spanier theorems.
- There exists an envy-free division which is also **Pareto efficient**; See Weller's theorem.

Both proofs work only for additive and non-atomic value measures, and rely on the ability to give each partner a large number of disconnected pieces.

Some other variants are:

- **Strong envy-freeness** requires that each agent strictly prefers his bundle to the other bundles.
- **Super envy-freeness** requires that each agent strictly prefers his bundle to 1/*n* of the total value, and strictly prefers 1/*n* to each of the other bundles. Clearly, super envy-freeness implies strong envy-freeness which implies envy-freeness.

## Envy-free division with different entitlements

A common generalization of the envy-free criterion is that each of the partners has a different entitlement. I.e., for every partner *i* there is a weight *wi* describing the fraction of the cake that they are entitled to receive (the sum of all *wi* is 1). Then a weighted-envy-free division is defined as follows. For every agent *i* with value measure *Vi*, and for every other agent *j*:

> $V_{i}(X_{i})/w_{i}\geq V_{i}(X_{j})/w_{j}$

I.e., every partner thinks that their allocation relative to their entitlement is at least as large as any other allocation relative to the other partner's entitlement.

When all weights are the same (and equal to 1/*n*), this definition reduces to the standard definition of envy-freeness.

When the pieces may be disconnected, a weighted envy-free division always exists and can be found by the Robertson-Webb protocol, for any set of weights. Zeng presented an alternative algorithm for approximate weighted envy-free division, which requires a smaller number of cuts.

But when the pieces must be connected, a weighted envy-free division may not exist. To see this, note that every weighted-envy-free division is also *weighted-proportional* with the same weight-vector; this means that, for every agent *i* with value measure *Vi*:

> $V_{i}(X_{i})/w_{i}\geq V_{i}(C)$

It is known that weighted-proportional allocation with connected pieces may not exist: see proportional cake-cutting with different entitlements for an example.

Note that there is an alternative definition of weighted-envy-free division, where the weights are assigned to *pieces* rather than to agents. With this definition, a weighted envy-free division is known to exist in the following cases (each case generalizes the previous case):

- Additive value functions, 1-dimensional cake (interval), and the pieces must be connected intervals.
- Additive value functions, multi-dimensional simplex cake, and the pieces must be simplexes. The proof uses Sperner's theorem, the K-K-M lemma, Gale's covering lemma and Ky Fan's lemma on coincidence points.

## Dividing a 'bad' cake

In some cases, the 'cake' to be divided has a negative value. For example, it might be piece of lawn that has to be mowed, or a piece of wasteland that has to be cleaned. Then, the cake is a 'heterogeneous bad' rather than a 'heterogeneous good'.

Some procedures for envy-free cake-cutting can be adapted to work for a bad cake, but the adaptation is often not trivial. See envy-free chore division for more details.

## Summary tables

Summary by result

Name

Type

Cake

Pieces

#partners (

n

)

#queries

#cuts

envy

proportionality

Comments

Divide and choose

Discrete proc

Any

Connected

2

2

1 (optimal)

None

1/2

Stromquist

Moving-knife proc

Interval

Connected

3

∞

2 (optimal)

None

1/3

Selfridge–Conway

Discrete proc

Any

Disconnected

3

9

5

None

1/3

Brams–Taylor–Zwicker

Moving-knife proc

Any

Disconnected

4

∞

11

None

1/4

Saberi–Wang

Discrete proc

Any

Disconnected

4

Bounded

Bounded

None

1/4

Free disposal

Aziz–Mackenzie

Discrete proc

Any

Disconnected

4

584

203

None

1/4

Saberi–Wang

Moving-knife proc

Any

Disconnected

5

∞

Bounded

None

1/5

Stromquist

Existence

Interval

Connected

n

—

n

-1

None

1/

n

Simmons

Discrete proc

Interval

Connected

n

∞

n

-1

None

1/

n

Deng-Qi-Saberi

Discrete proc

Interval

Connected

n

$\left({\frac {1}{\epsilon }}\right)^{n-2}$

n

-1

Additive

$\epsilon$

$\left({\tfrac {1}{n}}\right)-\epsilon$

Only when valuations are Lipschitz continuous

Branzei

Discrete proc

Interval

Connected

n

$n^{2}d$

?

None

1/

n

Only when value densities are polynomial with degree at most

d

.

Waste-Makes-Haste

Discrete proc

Interval

Connected

3

9

4

None

1/3

Free disposal

Waste-Makes-Haste

Discrete proc

Any

Connected

4

16

6

None

1/7

Free disposal

Waste-Makes-Haste

Discrete proc

Any

Connected

n

$2^{n}$

$2^{n-1}-1$

None

${\frac {1}{2^{n-1}}}$

Free disposal

Aziz-Mackenzie ConnectedPieces

Discrete proc

Any

Connected

n

$n^{n+1}$

$n^{n+1}$

None

${\frac {1}{3n}}$

Free disposal

Brams-Taylor

Discrete proc

Any

Disconnected

n

Unbounded

Unbounded

None

1/

n

Robertson-Webb

Discrete proc

Any

Disconnected

n

Unbounded

Unbounded

None

1/

n

Weighted-envy-free.

Pikhurko

Discrete proc

Any

Disconnected

n

Unbounded

Unbounded

None

1/

n

Aziz–Mackenzie

Discrete proc

Any

Disconnected

n

$n^{n^{n^{n^{n^{n}}}}}$

$n^{n^{n^{n^{n^{n}}}}}$

None

1/

n

Reentrant last diminisher

Discrete proc

Interval

Disconnected

n

$n^{2}/\epsilon$

?

Additive

$\epsilon$

1/

n

Kurokawa-Lai-Procaccia

Discrete proc

Interval

Disconnected

n

$n^{6}k\ln k$

?

None

1/

n

Only when value densities are piecewise linear with at most

k

discontinuities.

Weller

Existence

Any

Disconnected

n

—

∞

None

1/

n

Pareto efficient

.

2-D

Discrete proc

Square

Connected and Square

2

2

2

None

1/4

Free disposal

2-D

Moving-knife proc

Square

Connected and Square

3

∞

6

None

1/10

Free disposal

Summary by number of agents and type of pieces:

| # agents | Connected pieces | General pieces |
|---|---|---|
| 2 | Divide and choose |   |
| 3 | Stromquist moving-knives procedure (infinite time); Waste-makes-haste (bounded-time, bounded cuts, free disposal, proportional) | Selfridge–Conway discrete procedure (bounded-time, at most 5 cuts). |
| 4 | Waste-makes-haste (bounded-time, bounded cuts, free disposal, proportionality 1/7). | Brams–Taylor–Zwicker moving knives procedure (infinite time, at most 11 cuts). Saberi–Wang discrete procedure (bounded time, bounded cuts, free disposal, proportional). Aziz–Mackenzie discrete procedure (bounded time, bounded cuts, proportional). |
| 5 |   | Saberi–Wang moving-knives procedure (infinite time, bounded cuts). |
| n | Simmons' protocol (infinite time) Deng-Qi-Saberi (approximately envy-free, exponential time). Waste-makes-haste (fully envy-free, exponential time, free-disposal, exponential proportionality) Aziz-Mackenzie ConnectedPieces (fully envy-free, exponential time, free-disposal, linear proportionality) | Brams and Taylor (1995); Robertson and Webb (1998). - Both algorithms require a finite but unbounded number of cuts. Aziz-Mackenzie discrete procedure (bounded time, bounded cuts, proportional). |
| Hardness | All algorithms for *n* ≥ 3 must be infinite (Stromquist, 2008). | All algorithms must use at least Ω(*n*2) steps (Procaccia, 2009). |
| Variants | A weighted envy-free division exists for arbitrary weights (Idzik, 1995), even when the cake and pieces are simplexes (Idzik and Ichiishi, 1996). An envy-free division exists even with non-additive preferences (Dall'Aglio and Maccheroni, 2009). | Robertson-Webb can find weighted-envy-free divisions for arbitrary weights. A perfect division exists (Dubins&Spanier, 1961). An envy-free and efficient cake-cutting exists (Weller's theorem). |
