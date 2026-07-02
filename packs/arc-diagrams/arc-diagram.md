---
title: "Arc diagram"
source: https://en.wikipedia.org/wiki/Arc_diagram
domain: arc-diagrams
license: CC-BY-SA-4.0
tags: arc diagram, one dimensional layout, circular layout, node ordering
fetched: 2026-07-02
---

# Arc diagram

An **arc diagram** is a style of graph drawing, in which the vertices of a graph are placed along a line in the Euclidean plane and edges are drawn using semicircles or other convex curves above or below the line. These drawings are also called **linear embeddings** or **circuit diagrams**.

Applications of arc diagrams include information visualization, the Farey diagram of number-theoretic connections between rational numbers, and diagrams representing RNA secondary structure in which the crossings of the diagram represent pseudoknots in the structure.

## Description

In an arc diagram, the vertices of a graph are arranged along a line in the Euclidean plane. The edges are drawn as semicircles in one or both of the two halfplanes bounded by the line, or as smooth curves formed by sequences of semicircles. In some cases, line segments of the line itself are also allowed as edges, as long as they connect only vertices that are consecutive along the line. Variations of this drawing style in which the semicircles are replaced by convex curves of some other type are also commonly called arc diagrams.

For drawings of directed graphs, a common convention is to draw each arc in a clockwise direction, so that arcs that are directed from an earlier to a later vertex in the sequence are drawn above the vertex line, and arcs directed from a later to an earlier vertex are drawn below the line.

## History and nomenclature

The use of the phrase "arc diagram" for this kind of drawing follows the use of a similar type of diagram by Wattenberg (2002) to visualize the repetition patterns in strings, by using arcs to connect pairs of equal substrings. However, this style of graph drawing is much older than its name, dating back at least to the work of Saaty (1964) and Nicholson (1968), who used arc diagrams to study crossing numbers of graphs.

Arc diagrams are also called *linear embeddings*. In their application to the circuit topology of RNA secondary structure, they are called *circuit diagrams*.

## Planar graphs

As Nicholson (1968) observed, every drawing of a graph in the plane may be deformed into an arc diagram, without changing its number of crossings. In particular, every planar graph has a planar arc diagram. However, this embedding may need to use more than one semicircle for some of its edges.

If a graph is drawn without crossings using an arc diagram in which each edge is a single semicircle, then the drawing is a two-page book embedding. This kind of drawing is only possible for the subhamiltonian graphs, a proper subset of the planar graphs. For instance, a maximal planar graph has such an embedding if and only if it contains a Hamiltonian cycle. Therefore, a non-Hamiltonian maximal planar graph such as the Goldner–Harary graph cannot have a planar embedding with one semicircle per edge. Testing whether a given graph has a crossing-free arc diagram of this type (or equivalently, whether it has pagenumber two) is NP-complete.

However, every planar graph has an arc diagram in which each edge is drawn as a biarc with at most two semicircles. More strongly, every *st*-planar directed graph (a planar directed acyclic graph with a single source and a single sink, both on the outer face) has an arc diagram in which every edge forms a monotonic curve, with these curves all consistently oriented from one end of the vertex line towards the other. For undirected planar graphs, one way to construct an arc diagram with at most two semicircles per edge is to subdivide the graph and add extra edges so that the resulting graph has a Hamiltonian cycle (and so that each edge is subdivided at most once), and to use the ordering of the vertices on the Hamiltonian cycle as the ordering along the line. In a planar graph with n vertices, at most $n/2$ biarcs are needed.

## Minimizing crossings

Because it is NP-complete to test whether a given graph has an arc diagram with one semicircle per edge and no crossings, it is also NP-hard to find an arc diagram of this type that minimizes the number of crossings. This crossing minimization problem remains NP-hard, for non-planar graphs, even if the ordering of the vertices along the line is fixed. However, in the fixed-ordering case, an embedding without crossings (if one exists) may be found in polynomial time by translating the problem into a 2-satisfiability problem, in which the variables represent the placement of each arc and the constraints prevent crossing arcs from being placed on the same side of the vertex line. Additionally, in the fixed-ordering case, a crossing-minimizing embedding may be approximated by solving a maximum cut problem in an auxiliary graph that represents the semicircles and their potential crossings (or equivalently, by approximating the MAX2SAT version of the 2-satisfiability instance).

Cimikowski & Shope (1996), Cimikowski (2002), and He, Sýkora & Vrt'o (2005) discuss heuristics for finding arc diagrams with few crossings.

## Applications

For applications in information visualization, Heer, Bostock & Ogievetsky (2010) write that arc diagrams "may not convey the overall structure of the graph as effectively as a two-dimensional layout", but that their layout makes it easy to display multivariate data associated with the vertices of the graph. Arc diagrams were used by Brandes (1999) to visualize the state diagram of a shift register, by Djidjev & Vrt'o (2002) to show that the crossing number of every graph is lower-bounded by a combination of its cutwidth and vertex degrees, by Byrne et al. (2007) to visualize interactions between Bluetooth devices, and by Owens & Jankun-Kelly (2013) to visualize the yardage of plays in a game of American football. Additional applications of this visualization technique are surveyed by Nagel & Duval (2013).

The Farey diagram of a set of rational numbers is a structure that may be represented geometrically as an arc diagram. In this form it has a vertex for each number, placed on the number line, and a semicircular edge above the line connecting pairs of numbers $p/q$ and $r/s$ (in simplest terms) for which $|ps-rq|=1$ . The semicircles of the diagram may be thought of as lines in the Poincaré half-plane model of the hyperbolic plane, with the vertices placed at infinite points on the boundary line of this model. The Poincaré half-plane model has an infinite point that is not represented as point on the boundary line, the shared endpoint of all vertical rays in the model, and this may be represented by the "fraction" 1/0 (undefined as a number), with the same rule for determining its adjacencies. The Farey diagram of any set of rational numbers is a planar graph, and the Farey diagram of the set of all rational numbers forms a tessellation of the hyperbolic plane by ideal triangles.

Arc diagrams or circuit diagrams are commonly used in studying folded biopolymers such as proteins and nucleic acids (DNAs, RNAs). Biopolymers are typically represented by their primary monomer sequence along the line of the diagrams, and with arcs above the line representing bonds between monomers (e.g., amino acids in proteins or bases in RNA or DNA) that are adjacent in the physical structure of the polymer despite being nonadjacent in the sequence order. The theoretical framework of circuit topology is then typically applied to extract local and global topological information, which can in turn be related to biological function of the folded molecules. When arcs do not cross, the arrangement of the two arcs will be either parallel (P) or series (S). When there are crossings, the crossings represent what is often called as X arrangement in circuit topology. The statistics of P, S, and X can be used to learn about folding kinetics of these polymers.
