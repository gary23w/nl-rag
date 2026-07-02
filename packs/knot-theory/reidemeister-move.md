---
title: "Reidemeister move"
source: https://en.wikipedia.org/wiki/Reidemeister_move
domain: knot-theory
license: CC-BY-SA-4.0
tags: knot theory, knot invariant, jones polynomial, braid group
fetched: 2026-07-02
---

# Reidemeister move

In the mathematical area of knot theory, a **Reidemeister move** is any of three local moves on a link diagram. Kurt Reidemeister (1927) and, independently, James Waddell Alexander and Garland Baird Briggs (1926), demonstrated that two knot diagrams belonging to the same knot, up to planar isotopy, can be related by a sequence of the three Reidemeister moves.

Each move operates on a small region of the diagram and is one of three types:

1. Twist and untwist in either direction.
2. Move one loop completely over another.
3. Move a string completely over or under a crossing.

No other part of the diagram is involved in the picture of a move, and a planar isotopy may distort the picture. The numbering for the types of moves corresponds to how many strands are involved, e.g. a type II move operates on two strands of the diagram.

One important context in which the Reidemeister moves appear is in defining knot invariants. By demonstrating a property of a knot diagram which is not changed when we apply any of the Reidemeister moves, an invariant is defined. Many important invariants can be defined in this way, including the Jones polynomial.

The type I move is the only move that affects the writhe of the diagram. The type III move is the only one which does not change the crossing number of the diagram.

In applications such as the Kirby calculus, in which the desired equivalence class of knot diagrams is not a knot but a framed link, one must replace the type I move with a "modified type I" (type I') move composed of two type I moves of opposite sense. The type I' move affects neither the framing of the link nor the writhe of the overall knot diagram.

Trace (1983) showed that two knot diagrams for the same knot are related by using only type II and III moves if and only if they have the same writhe and winding number. Furthermore, combined work of Östlund (2001), Manturov (2004), and Hagge (2006) shows that for every knot type there are a pair of knot diagrams so that every sequence of Reidemeister moves taking one to the other must use all three types of moves. Alexander Coward demonstrated that for link diagrams representing equivalent links, there is a sequence of moves ordered by type: first type I moves, then type II moves, type III, and then type II. The moves before the type III moves increase crossing number while those after decrease crossing number.

Hayashi (2005) proved there is also an upper bound, depending on crossing number, on the number of Reidemeister moves required to split a link.

Coward & Lackenby (2014) proved the existence of an exponential tower upper bound (depending on crossing number) on the number of Reidemeister moves required to pass between two diagrams of the same link. In detail, let n be the sum of the crossing numbers of the two diagrams, then the upper bound is $2^{2^{2^{.^{.^{n}}}}}$ where the height of the tower of 2 s (with a single n at the top) is $10^{1,000,000n}$ .

Lackenby (2015) proved the existence of a polynomial upper bound (depending on crossing number) on the number of Reidemeister moves required to change a diagram of the unknot to the standard unknot. In detail, for any such diagram with c crossings, the upper bound is $(236c)^{11}$ .
