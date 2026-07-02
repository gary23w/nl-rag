---
title: "Generalized geography"
source: https://en.wikipedia.org/wiki/Generalized_geography
domain: pspace
license: CC-BY-SA-4.0
tags: polynomial space, pspace complete, quantified boolean formula problem, generalized geography
fetched: 2026-07-02
---

# Generalized geography

In computational complexity theory, **generalized geography** is a well-known PSPACE-complete problem.

## Introduction

Geography is a children's game, where players take turns naming cities from anywhere in the world. Each city chosen must begin with the same letter that ended the previous city name. Repetition is not allowed. The game begins with an arbitrary starting city and ends when a player loses because they are unable to continue.

### Graph model

To visualize the game, a directed graph can be constructed whose nodes are each cities of the world. An arrow is added from node *N*1 to node *N*2 if and only if the city labeling *N*2 starts with the letter that ending the name of the city labeling node *N*1. In other words, we draw an arrow from one city to another if the first can lead to the second according to the game rules. Each alternate edge in the directed graph corresponds to each player (for a two player game). The first player unable to extend the path loses. An illustration of the game (containing some cities in Michigan) is shown in the figure below.

In a generalized geography (GG) game, we replace the graph of city names with an arbitrary directed graph. The following graph is an example of a generalized geography game.

### Playing the game

We define *P*1 as the player moving first and *P*2 as the player moving second and name the nodes *N*1 to *N**n*. In the above figure, *P*1 has a winning strategy as follows: *N*1 points only to nodes *N*2 and *N*3. Thus *P*1's first move must be one of these two choices. *P*1 chooses *N*2 (if *P*1 chooses *N*3, then *P*2 will choose *N*9 as that is the only option and *P*1 will lose). Next *P*2 chooses *N*4 because it is the only remaining choice. *P*1 now chooses *N*5 and *P*2 subsequently chooses *N*3 or *N*7. Regardless of *P*2's choice, *P*1 chooses *N*9 and *P*2 has no remaining choices and loses the game.

## Computational complexity

The problem of determining which player has a winning strategy in a generalized geography game is PSPACE-complete.

### Generalized geography is in PSPACE

Let GG = { ⟨*G*, *b*⟩ | *P*1 has a winning strategy for the generalized geography game played on graph *G* starting at node *b* }; to show that GG ∈ PSPACE, we present a polynomial-space recursive algorithm determining which player has a winning strategy. Given an instance of GG, ⟨*G*, *n*start⟩ where *G* is a directed graph and *n*start is the designated start node, the algorithm *M* proceeds as follows:

On *M*(⟨*G*, *n*start⟩):

1. Measure the out-degree of node *n*start. If this degree is 0, then return reject, because there are no moves available for player one.
2. Construct a list of all nodes reachable from *n*start by one edge: *n*1, *n*2, ..., *n**i*.
3. Remove *n*start and all edges connected to it from *G* to form *G*1.
4. For each node *n**j* in the list *n*1, ..., *n**i*, call *M*(⟨*G*1, *n**j*⟩).
5. If all of these calls return *accept*, then no matter which decision *P*1 makes, *P*2 has a strategy to win, so return *reject*. Otherwise (if one of the calls returns *reject*) *P*1 has a choice that will deny any successful strategies for *P*2, so return *accept*.

The algorithm *M* clearly decides GG. It is in PSPACE because the only non-obvious polynomial workspace consumed is in the recursion stack. The space consumed by the recursion stack is polynomial because each level of recursion adds a single node to the stack, and there are at most *n* levels, where *n* is the number of nodes in *G*. This is essentially equivalent to a depth-first search.

### Generalized geography is PSPACE-hard

The following proof is due to David Lichtenstein and Michael Sipser.

To establish the PSPACE-hardness of GG, we can reduce the FORMULA-GAME problem (which is known to be PSPACE-hard) to GG in polynomial time (P). In brief, an instance of the FORMULA-GAME problem consists of a quantified Boolean formula φ = ∃*x*1 ∀*x*2 ∃*x*3 ...*Qxk*(ψ) where *Q* is either ∃ or ∀. The game is played by two players, *Pa* and *Pe*, who alternate choosing values for successive *xi*. *Pe* wins the game if the formula ψ ends up *true*, and *Pa* wins if ψ ends up *false*. The formula ψ is assumed to be in conjunctive normal form.

In this proof, we assume that the quantifier list starts and ends with the existential qualifier, ∃, for simplicity. Note that any expression can be converted to this form by adding dummy variables that do not appear in ψ.

By constructing a graph *G* like the one shown above, we will show any instance of FORMULA-GAME can be reduced to an instance of Generalized Geography, where the optimal strategy for *P1* is equivalent to that of *Pe*, and the optimal strategy for *P2* is equivalent to that of *Pa*.

The left vertical chain of nodes is designed to mimic the procedure of choosing values for variables in FORMULA-GAME. Each diamond structure corresponds to a quantified variable. Players take turns deciding paths at each branching node. Because we assumed the first quantifier would be existential, *P*1 goes first, selecting the left node if *x*1 is *true* and the right node if *x*1 is *false*. Each player must then take forced turns, and then *P2* chooses a value for *x*2. These alternating assignments continue down the left side. After both players pass through all the diamonds, it is again *P*1 's turn, because we assumed that the last quantifier is existential. *P*1 has no choice but to follow the path to the right side of the graph. Then it is *P*2 's turn to make a move.

When the play gets to the right side of the graph, it is similar to the end of play in the formula game. Recall that in the formula game, *Pe* wins if ψ is *true*, while *Pa* wins if ψ is *false*. The right side of the graph guarantees that *P1* wins if and only if *Pe* wins, and that *P*2 wins if and only if *Pa* wins.

First we show that *P*2 always wins when *Pa* wins. If *Pa* wins, ψ is *false*. If ψ is *false*, there exists an unsatisfying clause. *P*2 will choose an unsatisfying clause to win. Then when it is *P*1's turn he must choose a literal in that clause chosen by *P*2. Since all the literals in the clause are *false*, they do not connect to previously visited nodes in the left vertical chain. This allows *P*2 to follow the connection to the corresponding node in a diamond of the left chain and select it. However, *P*1 is now unable to select any adjacent nodes and loses.

Now we show that *P*1 always wins when *Pe* wins. If *Pe* wins, ψ is *true*. If ψ is *true*, every clause in the right side of the graph contains a *true* literal. *P*2 can choose any clause. Then *P*1 chooses the literal that is *true*. And because it is *true*, its adjacent node in the left vertical node has already been selected, so *P*2 has no moves to make and loses.

### Planar generalized geography is PSPACE-complete

Generalized geography is PSPACE-complete, even when played on planar graphs. The following proof is from theorem 3 of.

Since planar GG is a special case of GG, and GG is in PSPACE, so planar GG is in PSPACE. It remains to show that planar GG is PSPACE-hard. This can be proved by showing how to convert an arbitrary graph into a planar graph, such that a game of GG played on this graph will have the same outcome as on the original graph.

In order to do that, it's only necessary to eliminate all the edge crossings of the original graph. We draw the graph such that no three edges intersect at a point, and no pair of crossing edges can both be used in the same game. This is not possible in general, but is always possible for the graph constructed from a FORMULA-GAME instance; for example we could have only the edges from clause vertices involved in crossings. Now we replace each crossing with this construction:

(The intersection is eliminated by adding 9 vertices and redrawing the edges as shown.)

The result is a planar graph, and the same player can force a win as in the original graph: if a player chooses to move "up" from V in the transformed game, then both players must continuing moving "up" to W or lose immediately. So moving "up" from V in the transformed game simulates the move V→W in the original game. If V→W is a winning move, then moving "up" from V in the transformed game is also a winning move, and vice versa.

Thus, the game of GG played on the transformed graph will have the same outcome as on the original graph. This transformation takes time that is a constant multiple to the number of edge intersections in the original graph, thus it takes polynomial time.

Thus planar GG is PSPACE-complete.

### Planar bipartite graph with maximum degree 3

GG played on planar bipartite graphs with maximum degree 3 is still PSPACE-complete, by replacing the vertices of degree higher than 3 with a chain of vertices with degree at most 3. Proof is in. and uses the following construction:

If one player uses any of the entrances to this construction, the other player chooses which exit will be used. Also the construction can only be traversed once, because the central vertex is always visited. Hence this construction is equivalent to the original vertex.

## Edge geography

A variant of GG is called **edge geography**, where after each move, the edge that the player went through is erased. This is in contrast to the original GG, where after each move, the vertex that the player used to be on is erased. In this view, the original GG can be called **Vertex Geography**.

Edge geography is PSPACE-complete. This can be proved used the same construction that was used for vertex geography.

## Undirected geography

One may also consider playing either Geography game on an undirected graph (that is, the edges can be traversed in both directions). Fraenkel, Scheinerman, and Ullman show that **undirected vertex geography** can be solved in polynomial time, whereas **undirected edge geography** is PSPACE-complete, even for planar graphs with maximum degree 3. If the graph is bipartite, then Undirected Edge Geography is solvable in polynomial time.

## Consequences

Given that GG is PSPACE-complete, no polynomial time algorithm exists for optimal play in GG unless P = PSPACE. However, it may not be as easy to prove the complexity of other games because certain games (such as chess) contain a finite number of game positions — making it hard (or impossible) to formulate a mapping to a PSPACE-complete problem. In spite of this, the complexity of certain games can still be analyzed by generalization (e.g., to an *n* × *n* board). See the references for a proof for generalized Go, as a corollary of the proof of the completeness of GG.
