---
title: "Lattice of stable matchings"
source: https://en.wikipedia.org/wiki/Lattice_of_stable_matchings
domain: stable-matching
license: CC-BY-SA-4.0
tags: stable matching, gale shapley algorithm, stable marriage problem, hospital residents problem
fetched: 2026-07-02
---

# Lattice of stable matchings

In mathematics, economics, and computer science, a **lattice of stable matchings** is a distributive lattice whose elements are all the solutions to a given instance of the stable matching problem. These solutions, called *stable matchings*, pair up participants of two types in such a way that no two participants would prefer to be paired with each other than to accept their assigned pairings. Being a lattice means that, for a comparison operation between stable matchings based on the preferences of the participants, each two stable matchings have a unique greatest lower bound and a unique least upper bound. Together, the greatest lower bound and least upper bound operations obey the distributive law. This structure was originally described in the 1970s by John Horton Conway and Donald Knuth.

The Gale–Shapley algorithm can find either of two special stable matchings, the greatest and least matchings in the lattice. The entire lattice has a concise representation that can be constructed in polynomial time, by using Birkhoff's representation theorem to describe it as the family of lower sets of an underlying partially ordered set. The elements of this partially ordered set are called rotations; they are cycle graphs that describe the symmetric difference between two stable matchings that are adjacent in the lattice. Algorithms that operate on this partial order instead of directly on stable matchings, and that search for lower sets that are optimal in some way, can find in polynomial time the minimum or maximum weight stable matching, for weighted instances of the stable matching problem.

Every finite distributive lattice can be represented as a lattice of stable matchings. The number of matchings in the lattice can vary from an average case of $e^{-1}n\ln n$ to a worst case of exponential, where n is the number of participants of each kind to be matched. Computing the number of stable matchings for a given instance of stable matching is #P-complete.

## Background

In its simplest form, an instance of the stable matching problem consists of two equal-sized finite sets of participants to be matched to each other, for instance doctors seeking jobs and hospitals seeking to hire a doctor. Each participant has a preference ordering on the elements of the other type: the doctors each have different preferences for which hospital they would like to work at (for instance based on which cities they would prefer to live in), and the hospitals each have preferences for which doctor they would like to work for them (for instance based on specialization or recommendations). The goal is to find a matching that is *stable*: no pair of a doctor and a hospital prefer each other to their assigned match. Versions of this problem are used, for instance, by the National Resident Matching Program to match American medical students to hospitals.

In general, there may be many different stable matchings. For example, suppose there are three doctors (A,B,C) and three hospitals (X,Y,Z) which have preferences of:

A: YXZ

B: ZYX

C: XZY

X: BAC

Y: CBA

Z: ACB

There are three stable matchings for this system of preferences:

1. The doctors get their first choice and the hospitals get their third: AY, BZ, CX.
2. All participants get their second choice: AX, BY, CZ.
3. The hospitals get their first choice and the doctors their third: AZ, BX, CY.

The lattice of stable matchings organizes this collection of solutions, for any instance of stable matching, giving it the structure of a distributive lattice. (For the definition of a distributive lattice, see § Distributive lattice, below.)

## Structure

### Partial order on matchings

The lattice of stable matchings is based on the following weaker structure, a partially ordered set whose elements are the stable matchings. Define a comparison operation $\leq$ on the stable matchings, where $P\leq Q$ if and only if all doctors prefer matching Q to matching P : either they have the same assigned hospital in both matchings, or they are assigned a better hospital in Q than they are in P . If the doctors disagree on which matching they prefer, then P and Q are incomparable: neither one is $\leq$ the other. The same comparison operation can be defined in the same way for any two sets of participants to be matched, not just doctors and hospitals. The choice of which of the two sets of participants to use in the role of the doctors is arbitrary. Swapping the roles of the doctors and hospitals reverses the ordering of every pair of stable matchings, but does not otherwise change the structure of the partial order.

This ordering gives the matchings the structure of a partially ordered set. A partially ordered set is defined as an ordering that obeys the following three properties:

- For every matching P , $P\leq P$
- For every two different matchings P and Q , it cannot be the case that both $P\leq Q$ and $Q\leq P$ are true.
- For every three different matchings P , Q , and R , if $P\leq Q$ and $Q\leq R$ , then $P\leq R$ .

For stable matchings, all three properties follow directly from the definition of the comparison operation.

### Top and bottom elements

Define the best match of a participant x of a stable matching instance to be the participant y that x most prefers, among all the participants for which there exists a stable matching that pairs x with y , and define the worst match analogously. Then no two participants can have the same best match. For, suppose to the contrary that doctors x and $x'$ both have y as their best match, and that y prefers x to $x'$ . Then, in the stable matching that matches $x'$ to y (which must exist by the definition of the best match of $x'$ ), x and y would be an unstable pair, because y prefers x to $x'$ and x prefers y to any other partner in any stable matching. However, a stable matching cannot have an unstable pair. This contradiction shows that best matches are distinct, and therefore that assigning all doctors to their best matches gives a matching. It is a stable matching, because any unstable pair would also be unstable for one of the matchings used to define best matches. This matching, assigning all doctor to their best matches, also assigns all hospitals to their worst matches. In the partial ordering on stable matchings, it is greater than all other stable matchings.

Symmetrically, assigning all doctors to their worst matches and assigning all hospitals to their best matches gives another stable matching. In the partial order on the matchings, it is less than all other stable matchings.

The Gale–Shapley algorithm gives a process for constructing stable matchings, that can be described as follows: until a matching is reached, the algorithm chooses an arbitrary hospital with an unfilled position, and that hospital makes a job offer to the doctor it most prefers among the ones it has not already made offers to. If the doctor is unemployed or has a less-preferred assignment, the doctor accepts the offer (and resigns from their other assignment if it exists). The process always terminates, because each doctor and hospital interact only once. When it terminates, the result is a stable matching, the one that assigns each hospital to its best match and that assigns all doctors to their worst matches. An algorithm that swaps the roles of the doctors and hospitals (in which unemployed doctors send a job applications to their next preference among the hospitals, and hospitals accept applications either when they have an unfilled position or they prefer the new applicant, firing the doctor they had previously accepted) instead produces the stable matching that assigns all doctors to their best matches and each hospital to its worst match.

### Join and meet

Given any two stable matchings P and Q for the same input, one can form two more matchings $P\vee Q$ and $P\wedge Q$ in the following way:

- In $P\vee Q$ , each doctor gets their best choice among the two hospitals they are matched to in P and Q (if these differ) and each hospital gets its worst choice among the two doctors it is matched to.
- In $P\wedge Q$ , each doctor gets their worst choice among the two hospitals they are matched to in P and Q (if these differ) and each hospital gets its best choice.

(The same operations can be defined in the same way for any two sets of elements to be matched, not just doctors and hospitals.)

Then both $P\vee Q$ and $P\wedge Q$ are matchings. It is not possible, for instance, for two doctors to have the same best choice and be matched to the same hospital in $P\vee Q$ , for regardless of which of the two doctors is preferred by the hospital, that doctor and hospital would form an unstable pair in whichever of P and Q they are not already matched in. Because the doctors are matched in $P\vee Q$ , the hospitals must also be matched. The same reasoning applies symmetrically to $P\wedge Q$ .

Additionally, both $P\vee Q$ and $P\wedge Q$ are stable. There cannot be a pair of a doctor and hospital who prefer each other to their match, because the same pair would necessarily also be an unstable pair for at least one of P and Q .

### Distributive lattice

The two operations $P\vee Q$ and $P\wedge Q$ form the join and meet operations of a finite distributive lattice. In this context, a finite lattice is defined as a partially ordered finite set (here, the set of stable matchings) in which there is a unique minimum element and a unique maximum element, in which every two elements have a unique least element greater than or equal to both of them (their join) and every two elements have a unique greatest element less than or equal to both of them (their meet).

In the case of the operations $P\vee Q$ and $P\wedge Q$ defined above, the join $P\vee Q$ is greater than or equal to both P and Q because it was defined to give each doctor their preferred choice, and because these preferences of the doctors are how the ordering on matchings is defined. It is below any other matching that is also above both P and Q , because any such matching would have to give each doctor an assigned match that is at least as good. Therefore, it fits the requirements for the join operation of a lattice. Symmetrically, the operation $P\wedge Q$ fits the requirements for the meet operation.

Because they are defined using an element-wise minimum or element-wise maximum in the preference ordering, these two operations obey the same distributive laws obeyed by the minimum and maximum operations on linear orderings: for every three different matchings P , Q , and R ,

$P\wedge (Q\vee R)=(P\wedge Q)\vee (P\wedge R)$

and

$P\vee (Q\wedge R)=(P\vee Q)\wedge (P\vee R)$

Therefore, the lattice of stable matchings is a distributive lattice.

## Representation by rotations

### Join-irreducible matchings

Birkhoff's representation theorem states that any finite distributive lattice can be represented by a family of finite sets, with intersection and union as the meet and join operations, and with the relation of being a subset as the comparison operation for the associated partial order. More specifically, these sets can be taken to be the lower sets of an associated partial order. In the general form of Birkhoff's theorem, this partial order can be taken as the induced order on a subset of the matchings in the lattice, the join-irreducible matchings (matchings that cannot be formed as joins of a subset of other matchings).

When a stable matching M is join-irreducible, let $M'$ be the join of the matchings below M in the partial order of stable matchings. Then $M'$ is not M , because it is a join of matchings distinct from M and M is not such a join. $M'$ is below M in the partial order of stable matchings, and there are no other stable matchings between $M'$ and M .

### Rotations

For the lattice of stable matchings, the partial order of Birkhoff's representation theorem can alternatively be described in terms of structures called *rotations*, first described in 1986 by Robert W. Irving and Paul Leather.

Suppose that two different stable matchings P and Q are comparable and have no third stable matching between them in the partial order. Another way of stating this is that P and Q form a pair of the covering relation of the partial order of stable matchings. For instance, this is true for any join-irreducible matching M and the matching $M'$ formed by the join of the elements below M . Then the set of pairs of elements that are matched in one but not both of P and Q (the symmetric difference $P\oplus Q$ of their sets of matched pairs) is called a rotation. It forms a cycle graph whose edges alternate between matched pairs from P and from Q . Removing one of these two alternating sets of pairs, and adding the other alternating set, transforms P into Q or vice versa.

More than one pair of matchings $(P,Q)$ and $(R,S)$ may define the same rotation $P\oplus Q=R\oplus S$ . For any rotation, the top elements of pairs defining that rotation are closed under meet operations: if P and R are each the top matchings of pairs $(P,Q)$ and $(R,S)$ with $P\oplus Q=R\oplus S$ , then their meet $P\wedge R$ is also the top matching of another pair defining the same rotation. For every rotation, let M be the meet of all the top matchings of pairs defining that rotation. Then M is join-irreducible, and the rotation is $M\oplus M'$ where $M'$ is the join of the matchings below M . This gives a one-to-one correspondence between rotations and join-irreducible stable matchings.

### Matchings from lower sets

If the rotations are given the same partial ordering as their corresponding join-irreducible stable matchings, then Birkhoff's representation theorem gives a one-to-one correspondence between lower sets of rotations and all stable matchings. The set of rotations associated with any given stable matching can be obtained by changing the given matching by rotations downward in the partial ordering, choosing arbitrarily which rotation to perform at each step, until reaching the bottom element, and listing the rotations used in this sequence of changes. The stable matching associated with any lower set of rotations can be obtained by applying the rotations to the bottom element of the lattice of stable matchings, choosing arbitrarily which rotation to apply when more than one can apply.

Every pair $(x,y)$ of elements of a given stable matching instance belongs to at most two rotations: one rotation that, when applied to the lower of two matchings, removes other assignments to x and y and instead assigns them to each other, and a second rotation that, when applied to the lower of two matchings, removes pair $(x,y)$ from the matching and finds other assignments for those two elements. Because there are $n^{2}$ pairs of elements, there are $O(n^{2})$ rotations.

## Properties of the lattice

### Universality

Beyond being a finite distributive lattice, there are no other constraints on the lattice structure of stable matchings. This is because, for every finite distributive lattice L , there exists a stable matching instance whose lattice of stable matchings is isomorphic to L . More strongly, if a finite distributive lattice has k elements, then it can be realized using a stable matching instance with at most $k^{2}-k+4$ doctors and hospitals.

### Number of elements

The lattice of stable matchings can be used to study the computational complexity of counting the number of stable matchings of a given instance. From the equivalence between lattices of stable matchings and arbitrary finite distributive lattices, it follows that this problem has equivalent computational complexity to counting the number of elements in an arbitrary finite distributive lattice, or to counting the antichains in an arbitrary partially ordered set. Computing the number of stable matchings is #P-complete.

In a uniformly-random instance of the stable marriage problem with n doctors and n hospitals, the average number of stable matchings is asymptotically $e^{-1}n\ln n$ . In a stable marriage instance chosen to maximize the number of different stable matchings, this number can be at least $2^{n-1}$ , and us also upper-bounded by an exponential function of n (significantly smaller than the naive factorial bound on the number of matchings).

## Algorithmic consequences

The family of rotations and their partial ordering can be constructed in polynomial time from a given instance of stable matching, and provides a concise representation to the family of all stable matchings, which can for some instances be exponentially larger when listed explicitly. This allows several other computations on stable matching instances to be performed efficiently.

### Weighted stable matching and closure

If each pair of participants in a stable matching instance is assigned a real-valued weight, it is possible to find the minimum or maximum weight stable matching in polynomial time. One possible method for this is to apply linear programming to the order polytope of the partial order of rotations, or to the stable matching polytope. An alternative, combinatorial algorithm is possible, based on the same partial order.

From the weights on pairs of participants, one can assign weights to each rotation, where a rotation that changes a given stable matching to another one higher in the partial ordering of stable matchings is assigned the change in weight that it causes: the total weight of the higher matching minus the total weight of the lower matching. By the correspondence between stable matchings and lower sets of rotations, the total weight of any matching is then equal to the total weight of its corresponding lower set, plus the weight of the bottom element of the lattice of matchings. The problem of finding the minimum or maximum weight stable matching becomes in this way equivalent to the problem of finding the minimum or maximum weight lower set in a partially ordered set of polynomial size, the partially ordered set of rotations.

This optimal lower set problem is equivalent to an instance of the closure problem, a problem on vertex-weighted directed graphs in which the goal is to find a subset of vertices of optimal weight with no outgoing edges. The optimal lower set is an optimal closure of a directed acyclic graph that has the elements of the partial order as its vertices, with an edge from $\alpha$ to $\beta$ whenever $\alpha \leq \beta$ in the partial order. The closure problem can, in turn, be solved in polynomial time by transforming it into an instance of the maximum flow problem.

### Minimum regret

Dan Gusfield has defined the *regret* of a participant in a stable matching to be the distance of their assigned match from the top of their preference list. He defines the regret of a stable matching to be the maximum regret of any participant. Then one can find the minimum-regret stable matching by a simple greedy algorithm that starts at the bottom element of the lattice of matchings and then repeatedly applies any rotation that reduces the regret of a participant with maximum regret, until this would cause some other participant to have greater regret.

### Median stable matching

The elements of any distributive lattice form a median graph, a structure in which any three elements P , Q , and R (here, stable matchings) have a unique median element $m(P,Q,R)$ that lies on a shortest path between any two of them. It can be defined as:

$m(P,Q,R)=(P\wedge Q)\vee (P\wedge R)\vee (Q\wedge R)=(P\vee Q)\wedge (P\vee R)\wedge (Q\vee R).$

For the lattice of stable matchings, this median can instead be taken element-wise, by assigning each doctor the median in the doctor's preferences of the three hospitals matched to that doctor in P , Q , and R and similarly by assigning each hospital the median of the three doctors matched to it. More generally, any set of an odd number of elements of any distributive lattice (or median graph) has a median, a unique element minimizing its sum of distances to the given set. For the median of an odd number of stable matchings, each participant is matched to the median element of the multiset of their matches from the given matchings. For an even set of stable matchings, this can be disambiguated by choosing the assignment that matches each doctor to the higher of the two median elements, and each hospital to the lower of the two median elements. In particular, this leads to a definition for the median matching in the set of all stable matchings. However, for some instances of the stable matching problem, finding this median of all stable matchings is NP-hard.
