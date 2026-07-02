---
title: "Reconfiguration"
source: https://en.wikipedia.org/wiki/Reconfiguration
domain: pspace
license: CC-BY-SA-4.0
tags: polynomial space, pspace complete, quantified boolean formula problem, generalized geography
fetched: 2026-07-02
---

# Reconfiguration

In discrete mathematics and theoretical computer science, **reconfiguration** problems are computational problems involving reachability or connectivity of state spaces.

## Types of problems

Here, a state space is a discrete set of configurations of a system or solutions of a combinatorial problem, called states, together with a set of allowed moves linking one state to another. Reconfiguration problems may ask:

- For a given class of problems, is the state space always connected? That is, can one transform every pair of states into each other with a sequence of moves? If not, what is the computational complexity of determining whether the state space for a particular problem is connected?
- What is the diameter of the state space, the smallest number D such that every two states can be transformed into each other with at most D moves?
- Given two states, what is the complexity of determining whether they can be transformed into each other, or of finding the shortest sequence of moves for transforming one into another?
- If moves are chosen randomly with a carefully chosen probability distribution so that the resulting Markov chain converges to a discrete uniform distribution, how many moves are needed in a random walk in order to ensure that the state at the end up the walk is nearly uniformly distributed? That is, what is the Markov chain mixing time?

## Examples

Examples of problems studied in reconfiguration include:

- Games or puzzles such as the 15 puzzle or Rubik's Cube. This type of puzzle can often be modeled mathematically using the theory of permutation groups, leading to fast algorithms for determining whether states are connected; however, finding the state space diameter or the shortest path between two states may be more difficult. For instance, for $n\times n\times n$ version's of the Rubik's Cube, the state space diameter is $\Theta (n^{2}/\log n)$ , and the complexity of finding shortest solutions is unknown, but for a generalized version of the puzzle (in which some cube faces are unlabeled) it is NP-hard. Other reconfiguration puzzles such as Sokoban may be modeled as token reconfiguration but lack a group-theoretic structure. For such problems, the complexity can be higher; in particular, testing reachability for Sokoban is PSPACE-complete.
- Rotation distance in binary trees and related problems of flip distance in flip graphs. A rotation is an operation that changes the structure of a binary tree without affecting the left-to-right ordering of its nodes, often used to rebalence binary search trees. Rotation distance is the minimum number of rotations needed to transform one tree into another. The same state space also models the triangulations of a convex polygon, and moves that "flip" one triangulation into another by removing one diagonal of the polygon and replacing it by another; similar problems have also been studied on other kinds of triangulation. The maximum possible rotation distance between two trees with a given number of nodes is known, but it remains an open problem whether the rotation distance between two arbitrary trees can be found in polynomial time. The analogous problems for flip distance between triangulations of point sets or non-convex polygons are NP-hard.
- Reconfiguration of graph colorings. The moves that have been considered for coloring reconfiguration include changing the color of a single vertex, or swapping the colors of a Kempe chain. When the number of colors is at least two plus the degeneracy of a graph, then the state space of single-vertex recolorings is connected, and Cereceda's conjecture suggests that it has polynomial diameter. For fewer colors, some graphs have disconnected state spaces. For 3-colorings, testing global connectivity of the single-vertex recoloring state space is co-NP-complete, but when two colorings can be reconfigured to each other, the shortest reconfiguration sequence can be found in polynomial time. For more than three colors, single-vertex reconfiguration is PSPACE-complete.
- Nondeterministic constraint logic is a combinatorial problem on orientations of cubic graphs whose edges are colored red and blue. In a valid state of the system, each vertex must have at least one blue edge or at least two edges coming into it. A move in this state space reverses the orientation of a single edge while preserving these constraints. It is PSPACE-complete to test whether the resulting state space is connected or whether two states are reachable from each other, even when the underlying graph has bounded bandwidth. These hardness results are often used as the basis of reductions proving that other reconfiguration problems, such as the ones arising from games and puzzles, are also hard.
