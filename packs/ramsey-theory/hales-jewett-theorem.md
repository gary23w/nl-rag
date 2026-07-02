---
title: "Hales–Jewett theorem"
source: https://en.wikipedia.org/wiki/Hales%E2%80%93Jewett_theorem
domain: ramsey-theory
license: CC-BY-SA-4.0
tags: ramsey theory, ramsey's theorem, van der waerden's theorem, szemeredi theorem
fetched: 2026-07-02
---

# Hales–Jewett theorem

In mathematics, the **Hales–Jewett theorem** is a fundamental combinatorial result of Ramsey theory, named after Alfred W. Hales and Robert I. Jewett, that concerns the degree to which high-dimensional objects must necessarily exhibit some combinatorial structure.

An informal geometric statement of the theorem is that for any positive integers *n* and *c* there is a number *H* such that if the cells of a *H*-dimensional *n*×*n*×*n*×...×*n* cube are colored with *c* colors, there must be one row, column, or certain diagonal (more details below) of length *n* all of whose cells are the same color. In other words, assuming *n* and *c* are fixed, the higher-dimensional, multi-player, *n*-in-a-row generalization of a game of tic-tac-toe with *c* players cannot end in a draw, no matter how large *n* is, no matter how many people *c* are playing, and no matter which player plays each turn, provided only that it is played on a board of sufficiently high dimension *H*. By a standard strategy-stealing argument, one can thus conclude that if two players alternate, then the first player has a winning strategy when *H* is sufficiently large, though no practical algorithm for obtaining this strategy is known.

## Formal statement

Let *W**H* *n* be the set of words of length *H* over an alphabet with *n* letters; that is, the set of sequences of {1, 2, ..., *n*} of length *H*. This set forms the hypercube that is the subject of the theorem. A *variable word* *w*(*x*) over *W**H* *n* still has length *H* but includes the special element *x* in place of at least one of the letters. The words *w*(1), *w*(2), ..., *w*(*n*) obtained by replacing all instances of the special element *x* with 1, 2, ..., *n*, form a combinatorial line in the space *W**H* *n*; combinatorial lines correspond to rows, columns, and (some of the) diagonals of the hypercube. The Hales–Jewett theorem then states that for given positive integers *n* and *c*, there exists a positive integer *H*, depending on *n* and *c*, such that for any partition of *W**H* *n* into *c* parts, there is at least one part that contains an entire combinatorial line.

For example, take *n* = 3, *H* = 2, and *c* = 2. The hypercube *W**H* *n* in this case is just the standard tic-tac-toe board, with nine positions:

| 11 | 12 | 13 |
|---|---|---|
| 21 | 22 | 23 |
| 31 | 32 | 33 |

A typical combinatorial line would be the word 2x, which corresponds to the line 21, 22, 23; another combinatorial line is xx, which is the line 11, 22, 33. (Note that the line 13, 22, 31, while a valid line for the game tic-tac-toe, is not considered a combinatorial line.) In this particular case, the Hales–Jewett theorem does not apply; it is possible to divide the tic-tac-toe board into two sets, e.g. {11, 22, 23, 31} and {12, 13, 21, 32, 33}, neither of which contain a combinatorial line (and would correspond to a draw in the game of tic-tac-toe). On the other hand, if we increase *H* to, say, 8 (so that the board is now eight-dimensional, with 38 = 6561 positions), and partition this board into two sets (the "noughts" and "crosses"), then one of the two sets must contain a combinatorial line (i.e. no draw is possible in this variant of tic-tac-toe). For a proof, see below.

## Proof of Hales–Jewett theorem (in a special case)

We now prove the Hales–Jewett theorem in the special case *n* = 3, *c* = 2, *H* = 8 discussed above. The idea is to reduce this task to that of proving simpler versions of the Hales–Jewett theorem (in this particular case, to the cases *n* = 2, *c* = 2, *H* = 2 and *n* = 2, *c* = 6, *H* = 6). One can prove the general case of the Hales–Jewett theorem by similar methods, using mathematical induction.

Each element of the hypercube *W*8 3 is a string of eight numbers from 1 to 3, e.g. 13211321 is an element of the hypercube. We are assuming that this hypercube is completely filled with "noughts" and "crosses". We shall use a proof by contradiction and assume that neither the set of noughts nor the set of crosses contains a combinatorial line. If we fix the first six elements of such a string and let the last two vary, we obtain an ordinary tic-tac-toe board, for instance "132113??" gives such a board. For each such board "abcdef??", we consider the positions "abcdef11", "abcdef12", "abcdef22". Each of these must be filled with either a nought or a cross, so by the pigeonhole principle two of them must be filled with the same symbol. Since any two of these positions are part of a combinatorial line, the third element of that line must be occupied by the opposite symbol (since we are assuming that no combinatorial line has all three elements filled with the same symbol). In other words, for each choice of "abcdef" (which can be thought of as an element of the six-dimensional hypercube *W*6 3), there are six (overlapping) possibilities:

1. abcdef11 and abcdef12 are noughts; abcdef13 is a cross.
2. abcdef11 and abcdef22 are noughts; abcdef33 is a cross.
3. abcdef12 and abcdef22 are noughts; abcdef32 is a cross.
4. abcdef11 and abcdef12 are crosses; abcdef13 is a nought.
5. abcdef11 and abcdef22 are crosses; abcdef33 is a nought.
6. abcdef12 and abcdef22 are crosses; abcdef32 is a nought.

Thus we can partition the six-dimensional hypercube *W*6 3 into six classes, corresponding to each of the above six possibilities. (If an element abcdef obeys multiple possibilities, we can choose one arbitrarily, e.g. by choosing the highest one on the above list).

Now consider the seven elements 111111, 111112, 111122, 111222, 112222, 122222, 222222 in *W*6 3. By the pigeonhole principle, two of these elements must fall into the same class. Suppose for instance 111112 and 112222 fall into class (5), thus 11111211, 11111222, 11222211, 11222222 are crosses and 11111233, 11222233 are noughts. But now consider the position 11333233, which must be filled with either a cross or a nought. If it is filled with a cross, then the combinatorial line 11xxx2xx is filled entirely with crosses, contradicting our hypothesis. If instead it is filled with a nought, then the combinatorial line 11xxx233 is filled entirely with noughts, again contradicting our hypothesis. Similarly if any other two of the above seven elements of *W*6 3 fall into the same class. Since we have a contradiction in all cases, the original hypothesis must be false; thus there must exist at least one combinatorial line consisting entirely of noughts or entirely of crosses.

The above argument was somewhat wasteful; in fact the same theorem holds for *H* = 4. If one extends the above argument to general values of *n* and *c*, then *H* will grow very fast; even when *c* = 2 (which corresponds to two-player tic-tac-toe) the *H* given by the above argument grows as fast as the Ackermann function. The first primitive recursive bound is due to Saharon Shelah, and is still the best known bound in general for the *Hales–Jewett number* *H* = *H*(*n*, *c*).

## Connections with other theorems

### Van der Waerden's theorem

Observe that the above argument also gives the following corollary: if we let *A* be the set of all eight-digit numbers whose digits are all either 1, 2, 3 (thus *A* contains numbers such as 11333233), and we color *A* with two colors, then *A* contains at least one arithmetic progression of length three, all of whose elements are the same color. This is simply because all of the combinatorial lines appearing in the above proof of the Hales–Jewett theorem, also form arithmetic progressions in decimal notation. A more general formulation of this argument can be used to show that the Hales–Jewett theorem generalizes van der Waerden's theorem. Indeed the Hales–Jewett theorem is substantially a stronger theorem.

### Density Hales-Jewett theorem

Just as van der Waerden's theorem has a stronger *density version* in Szemerédi's theorem, the Hales–Jewett theorem also has a density version. In this strengthened version of the Hales–Jewett theorem, instead of coloring the entire hypercube *W**H* *n* into *c* colors, one is given an arbitrary subset *A* of the hypercube *W**H* *n* with some given density 0 < δ < 1. The theorem states that if *H* is sufficiently large depending on *n* and δ, then the set *A* must necessarily contain an entire combinatorial line.

The density Hales–Jewett theorem was originally proved by Furstenberg and Katznelson using ergodic theory. In 2009, the Polymath Project developed a new proof of the density Hales–Jewett theorem based on ideas from the proof of the corners theorem. Dodos, Kanellopoulos, and Tyros gave a simplified version of the Polymath proof.

### Higher dimensions

The Hales–Jewett theorem is further generalized by the Graham–Rothschild theorem on higher-dimensional combinatorial cubes.
