---
title: "Seven Bridges of Königsberg"
source: https://en.wikipedia.org/wiki/Seven_Bridges_of_Königsberg
domain: eulerian-path-traversal
license: CC-BY-SA-4.0
tags: eulerian path, eulerian circuit, degree condition, bridge finding
fetched: 2026-07-02
---

# Seven Bridges of Königsberg

The **Seven Bridges of Königsberg** is a historical puzzle asking for a walking tour through the bridges of the city of Königsberg (now Kaliningrad in Russia) that is a circuit ending where it started. Its mathematical formalization and proof of impossibility by Leonhard Euler, in 1736, laid the foundations of graph theory and foreshadowed the idea of topology.

## Background and problem statement

The city of Königsberg in Prussia (now Kaliningrad, Russia) was set on both sides of the Pregel River, and included two large islands—Kneiphof and Lomse—which were connected to each other, and to the two mainland portions of the city—Altstadt and Vorstadt—by seven bridges. The problem was to devise a walk through the city that would cross each of those bridges once and only once.

By way of specifying the logical task unambiguously, solutions involving either

1. reaching an island or mainland bank other than via one of the bridges, or
2. accessing any bridge without crossing to its other end

are explicitly unacceptable.

Euler proved that the problem has no solution. The difficulty he faced was the development of a suitable technique of analysis, and of subsequent tests that established this assertion with mathematical rigor.

## Euler's analysis

Euler first pointed out that the choice of route inside each land mass is irrelevant and that the only important feature of a route is the sequence of bridges crossed. This allowed him to reformulate the problem in abstract terms (laying the foundations of graph theory), eliminating all features except the list of land masses and the bridges connecting them. In modern terms, one replaces each land mass with an abstract "vertex" or node, and each bridge with an abstract connection, an "edge", which only serves to record which pair of vertices (land masses) is connected by that bridge. The resulting mathematical structure is a graph.

→ →

Since only the connection information is relevant, the shape of pictorial representations of a graph may be distorted in any way, without changing the graph itself. Only the number of edges (possibly zero) between each pair of nodes is significant. It does not, for instance, matter whether the edges drawn are straight or curved, or whether one node is to the left or right of another.

Next, Euler observed that (except at the endpoints of the walk), whenever one enters a vertex by a bridge, one leaves the vertex by a bridge. In other words, during any walk in the graph, the number of times one enters a non-terminal vertex equals the number of times one leaves it. Now, if every bridge has been traversed exactly once, it follows that, for each land mass (except for the ones chosen for the start and finish), the number of bridges touching that land mass must be *even* (half of them, in the particular traversal, will be traversed "toward" the landmass; the other half, "away" from it). However, all four of the land masses in the original problem are touched by an *odd* number of bridges (one is touched by 5 bridges, and each of the other three is touched by 3). Since, at most, two land masses can serve as the endpoints of a walk, the proposition of a walk traversing each bridge once leads to a contradiction.

In modern language, Euler shows that the possibility of a walk through a graph, traversing each edge exactly once, depends on the degrees of the nodes. The degree of a node is the number of edges touching it. Euler's argument shows that a necessary condition for the walk of the desired form is that the graph be connected and have exactly zero or two nodes of odd degree. This condition turns out also to be sufficient—a result stated by Euler and later proved by Carl Hierholzer. Such a walk is now called an *Eulerian trail* or *Euler walk* in his honor. Further, if there are nodes of odd degree, then any Eulerian path will start at one of them and end at the other. Since the graph corresponding to historical Königsberg has four nodes of odd degree, it cannot have an Eulerian path.

An alternative form of the problem asks for a path that traverses all bridges and also has the same starting and ending point. Such a walk is called an *Eulerian circuit* or an *Euler tour*. Such a circuit exists if, and only if, the graph is connected and all nodes have even degree. All Eulerian circuits are also Eulerian paths, but not all Eulerian paths are Eulerian circuits.

Euler's work was presented to the St. Petersburg Academy on 26 August 1735, and published as *Solutio problematis ad geometriam situs pertinentis* (The solution of a problem relating to the geometry of position) in the journal *Commentarii academiae scientiarum Petropolitanae* in 1741. It is available in English translation in *The World of Mathematics* by James R. Newman.

## Significance in the history and philosophy of mathematics

In the history of mathematics, Euler's solution of the Königsberg bridge problem is considered to be the first theorem of graph theory and the first true proof in the network theory, a subject now generally regarded as a branch of combinatorics. Combinatorial problems of other types such as the enumeration of permutations and combinations had been considered since antiquity.

Euler's recognition that the key information was the number of bridges and the list of their endpoints (rather than their exact positions) presaged the development of topology. The difference between the actual layout and the graph schematic is a good example of the idea that topology is not concerned with the rigid shape of objects.

Hence, as Euler recognized, the "geometry of position" is not about "measurements and calculations" but about something more general. That called in question the traditional Aristotelian view that mathematics is the "science of quantity". Though that view fits arithmetic and Euclidean geometry, it did not fit topology and the more abstract structural features studied in modern mathematics.

Philosophers have noted that Euler's proof is not about an abstraction or a model of reality, but directly about the real arrangement of bridges. Hence the certainty of mathematical proof can apply directly to reality. The proof is also explanatory, giving insight into why the result must be true.

## Present state of the bridges

Two of the seven original bridges did not survive the bombing of Königsberg in World War II. Two others were later demolished and replaced by a highway. The three other bridges remain, although only two of them are from Euler's time (one was rebuilt in 1935). These changes leave five bridges existing at the same sites that were involved in Euler's problem. In terms of graph theory, two of the nodes now have degree 2, and the other two have degree 3. Therefore, an Eulerian path is now possible, but it must begin on one island and end on the other.

The University of Canterbury in Christchurch has incorporated a model of the bridges into a grass area between the old Physical Sciences Library and the Erskine Building, housing the Departments of Mathematics, Statistics and Computer Science. The rivers are replaced with short bushes and the central island sports a stone tōrō. Rochester Institute of Technology has incorporated the puzzle into the pavement in front of the Gene Polisseni Center, an ice hockey arena that opened in 2014, and the Georgia Institute of Technology also installed a landscape art model of the seven bridges in 2018.

A popular variant of the puzzle is the Bristol Bridges Walk. Like historical Königsberg, Bristol occupies two river banks and two river islands. However, the configuration of the 45 major bridges in Bristol is such that an Eulerian circuit exists. This cycle has been popularized by a book and news coverage and has featured in different charity events.
