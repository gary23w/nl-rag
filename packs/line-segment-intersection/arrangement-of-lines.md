---
title: "Arrangement of lines"
source: https://en.wikipedia.org/wiki/Arrangement_of_lines
domain: line-segment-intersection
license: CC-BY-SA-4.0
tags: line segment intersection, bentley ottmann algorithm, sweep line, computational geometry
fetched: 2026-07-02
---

# Arrangement of lines

In geometry, an **arrangement of lines** is the subdivision of the Euclidean plane formed by a finite set of lines. An arrangement consists of bounded and unbounded convex polygons, the *cells* of the arrangement, line segments and rays, the *edges* of the arrangement, and points where two or more lines cross, the *vertices* of the arrangement. When considered in the projective plane rather than in the Euclidean plane, every two lines cross, and an arrangement is the projective dual to a finite set of points. Arrangements of lines have also been considered in the hyperbolic plane, and generalized to *pseudolines*, curves that have similar topological properties to lines. The initial study of arrangements has been attributed to an 1826 paper by Jakob Steiner.

An arrangement is said to be *simple* when at most two lines cross at each vertex, and *simplicial* when all cells are triangles (including the unbounded cells, as subsets of the projective plane). There are three known infinite families of simplicial arrangements, as well as many *sporadic simplicial arrangements* that do not fit into any known family. Arrangements have also been considered for infinite but locally finite systems of lines. Certain infinite arrangements of parallel lines can form simplicial arrangements, and one way of constructing the aperiodic Penrose tiling involves finding the dual graph of an arrangement of lines forming five parallel subsets.

The maximum numbers of cells, edges, and vertices, for arrangements with a given number of lines, are quadratic functions of the number of lines. These maxima are attained by simple arrangements. The complexity of other features of arrangements have been studied in discrete geometry; these include zones, the cells touching a single line, and levels, the polygonal chains having a given number of lines passing below them. Roberts's triangle theorem and the Kobon triangle problem concern the minimum and maximum number of triangular cells in a Euclidean arrangement, respectively.

Algorithms in computational geometry are known for constructing the features of an arrangement in time proportional to the number of features, and space linear in the number of lines. As well, researchers have studied efficient algorithms for constructing smaller portions of an arrangement, and for problems such as the shortest path problem on the vertices and edges of an arrangement.

## Definition

As an informal thought experiment, consider cutting an infinite sheet of paper along finitely many lines. These cuts would partition the paper into convex polygons. Their edges would be one-dimensional line segments or rays, with vertices at the points where two cut lines cross. This can be formalized mathematically by classifying the points of the plane according to which side of each line they are on. Each line produces three possibilities per point: the point can be in one of the two open half-planes on either side of the line, or it can be on the line. Two points can be considered to be equivalent if they have the same classification with respect to all of the lines. This is an equivalence relation, whose equivalence classes are subsets of equivalent points. These subsets subdivide the plane into shapes of the following three types:

1. The *cells* or *chambers* of the arrangement are two-dimensional regions not part of any line. They form the interiors of bounded convex polygons or unbounded convex regions. These are the connected components of the points that would remain after removing all points on lines.
2. The *edges* or *panels* of the arrangement are one-dimensional regions belonging to a single line. They are the open line segments and open infinite rays into which each line is partitioned by its crossing points with the other lines. That is, if one of the lines is cut by all the other lines, these are the connected components of its uncut points.
3. The *vertices* of the arrangement are isolated points belonging to two or more lines, where those lines cross each other.

The boundary of a cell is the system of edges that touch it, and the boundary of an edge is the set of vertices that touch it (one vertex for a ray and two for a line segment). The system of objects of all three types, linked by this boundary operator, form a cell complex covering the plane. Two arrangements are said to be *isomorphic* or *combinatorially equivalent* if there is a one-to-one boundary-preserving correspondence between the objects in their associated cell complexes.

The same classification of points, and the same shapes of equivalence classes, can be used for infinite but *locally finite* arrangements, defined as arrangements in which every bounded subset of the plane is crossed by finitely many lines. In this case the unbounded cells may have infinitely many sides.

## Complexity of arrangements

It is straightforward to count the maximum numbers of vertices, edges, and cells in an arrangement, all of which are quadratic in the number of lines:

- An arrangement with n lines has at most $n(n-1)/2$ vertices (a triangular number), one per pair of crossing lines. This maximum is attained for *simple arrangements*, those in which each two lines cross at a vertex that is disjoint from all the other lines. The number of vertices is smaller when some lines are parallel, or when some vertices are crossed by more than two lines.
- An arrangement can be rotated, if necessary, to avoid axis-parallel lines. After this step, each ray that forms an edge of the arrangement extends either upward or downward from its endpoint; it cannot be horizontal. There are n downward rays, one per line, and these rays separate $n+1$ cells of the arrangement that are unbounded in the downward direction. The remaining cells all have a unique bottommost vertex (again, because there are no axis-parallel lines). For each pair of lines, there can be only one cell where the two lines meet at the bottom vertex, so the number of downward-bounded cells is at most the number of pairs of lines, $n(n-1)/2$ . Adding the unbounded and bounded cells, the total number of cells in an arrangement can be at most $n(n+1)/2+1$ . These are the numbers of the lazy caterer's sequence.
- The number of edges of the arrangement is at most $n^{2}$ , as may be seen either by using the Euler characteristic to calculate it from the numbers of vertices and cells, or by observing that each line is partitioned into at most n edges by the other $n-1$ lines. Simple arrangements have exactly $n^{2}$ edges.

More complex features go by the names of "zones", "levels", and "many faces":

- The *zone* of a line $\ell$ in a line arrangement is the collection of cells having edges belonging to $\ell$ . The zone theorem states that the total number of edges in the cells of a single zone is linear. More precisely, the total number of edges of the cells belonging to a single side of line $\ell$ is at most $5n-1$ , and the total number of edges of the cells belonging to both sides of $\ell$ is at most $\lfloor 9.5n\rfloor -1$ . More generally, the total complexity of the cells of a line arrangement that are intersected by any convex curve is $O(n\alpha (n))$ , where $\alpha$ denotes the inverse Ackermann function, as may be shown using Davenport–Schinzel sequences. The sum of squares of cell complexities in an arrangement is $O(n^{2})$ , as can be shown by summing the zones of all lines.
- The k -*level* of an arrangement is the polygonal chain formed by the edges that have exactly k other lines directly below them. The $\leq k$ -level is the portion of the arrangement below the k -level. Finding matching upper and lower bounds for the complexity of a k -level remains a major open problem in discrete geometry. The best upper bound known is $O(nk^{1/3})$ , while the best lower bound known is $n2^{\Omega ({\sqrt {\log k}})}$ . In contrast, the maximum complexity of the $\leq k$ -level is known to be $\Theta (nk)$ . A k -level is a special case of a monotone path in an arrangement; that is, a sequence of edges that intersects any vertical line in a single point. However, monotone paths may be much more complicated than k -levels: there exist arrangements and monotone paths in these arrangements where the number of points at which the path changes direction is $n^{2-o(1)}$ .
- Although a single cell in an arrangement may be bounded by all n lines, it is not possible in general for m different cells to all be bounded by n lines. Rather, the total complexity of m cells is at most $\Theta (m^{2/3}n^{2/3}+n)$ , almost the same bound as occurs in the Szemerédi–Trotter theorem on point-line incidences in the plane. A simple proof of this follows from the crossing number inequality: if m cells have a total of $x+n$ edges, one can form a graph with m nodes (one per cell) and x edges (one per pair of consecutive cells on the same line). The edges of this graph can be drawn as curves that do not cross within the cells corresponding to their endpoints, and then follow the lines of the arrangement. Therefore, there are $O(n^{2})$ crossings in this drawing. However, by the crossing number inequality, there are $\Omega (x^{3}/m^{2})$ crossings. In order to satisfy both bounds, x must be $O(m^{2/3}n^{2/3})$ .

## Projective arrangements and projective duality

It is convenient to study line arrangements in the projective plane as every pair of lines has a crossing point. Line arrangements cannot be defined using the sides of lines, because a line in the projective plane does not separate the plane into two distinct sides. One may still define the cells of an arrangement to be the connected components of the points not belonging to any line, the edges to be the connected components of sets of points belonging to a single line, and the vertices to be points where two or more lines cross. A line arrangement in the projective plane differs from its Euclidean counterpart in that the two Euclidean rays at either end of a line are replaced by a single edge in the projective plane that connects the leftmost and rightmost vertices on that line, and in that pairs of unbounded Euclidean cells are replaced in the projective plane by single cells that are crossed by the projective line at infinity.

An arrangement of lines in the Euclidean plane can be naturally interpreted as an arrangement of great circles on the 2-sphere $S^{2}$ . To see this, embed the Euclidean plane $\mathbb {R} ^{2}$ as an affine plane $A\subset \mathbb {R} ^{3}$ not passing through the origin. Every point of A determines a line through the origin, which intersects $S^{2}$ in a pair of antipodal points; likewise, every line in A maps to a great circle on the sphere. The equator associated with A separates the two hemispheres and plays the role of the line at infinity. Identifying antipodal points on $S^{2}$ yields the projective plane, where lines in $\mathbb {R} ^{2}$ extend naturally to great circles and parallel lines meet at infinity. In this way, the combinatorial structure of line arrangements, including incidences, regions, and intersections, is preserved when transferred to great-circle arrangements on the sphere.

Due to projective duality, many statements about the combinatorial properties of points in the plane may be more easily understood in an equivalent dual form about arrangements of lines. For instance, the Sylvester–Gallai theorem, stating that any non-collinear set of points in the plane has an *ordinary line* containing exactly two points, transforms under projective duality to the statement that any projective arrangement of finitely many lines with more than one vertex has an *ordinary point*, a vertex where only two lines cross. The earliest known proof of the Sylvester–Gallai theorem, by Eberhard Melchior in 1940, uses the Euler characteristic to show that such a vertex must always exist.

## Triangles in arrangements

An arrangement of lines in the projective plane is said to be *simplicial* if every cell of the arrangement is bounded by exactly three edges. Simplicial arrangements were first studied by Melchior. Three infinite families of simplicial line arrangements are known:

1. A *near-pencil* consisting of $n-1$ lines through a single point, together with a single additional line that does not go through the same point,
2. The family of lines formed by the sides of a regular polygon together with its axes of symmetry, and
3. The sides and axes of symmetry of an even regular polygon, together with the line at infinity.

Additionally there are many other examples of *sporadic simplicial arrangements* that do not fit into any known infinite family. Conjecturally, there are only finitely many of them. This is known to be true under a linear bound on the number of double points. As Branko Grünbaum writes, simplicial arrangements "appear as examples or counterexamples in many contexts of combinatorial geometry and its applications." For instance, simplicial arrangements form counterexamples to a conjecture on the relation between the degree of a set of differential equations and the number of invariant lines the equations may have. The two known counterexamples to the Dirac–Motzkin conjecture (which states that any n -line arrangement has at least $n/2$ ordinary points) are both simplicial.

The dual graph of a line arrangement has one node per cell and one edge linking any pair of cells that share an edge of the arrangement. These graphs are partial cubes, graphs in which the nodes can be labeled by bitvectors in such a way that the graph distance equals the Hamming distance between labels. In the case of a line arrangement, each coordinate of the labeling assigns 0 to nodes on one side of one of the lines and 1 to nodes on the other side. Dual graphs of simplicial arrangements have been used to construct infinite families of 3-regular partial cubes, isomorphic to the graphs of simple zonohedra.

An arrangement with the minimum number of triangles according to

Roberts's triangle theorem

Kobon triangles

in an arrangement of 17 lines

It is also of interest to study the extremal numbers of triangular cells in arrangements that may not necessarily be simplicial. Any arrangement in the projective plane must have at least n triangles. Every arrangement that has only n triangles must be simple. For Euclidean rather than projective arrangements, the minimum number of triangles is $n-2$ , by Roberts's triangle theorem. The maximum possible number of triangular faces in a simple arrangement is known to be upper bounded by $n(n-1)/3$ and lower bounded by $n(n-3)/3$ ; the lower bound is achieved by certain subsets of the diagonals of a regular $2n$ -gon. For projective arrangements that are not required to be simple, there exist arrangements with $n(n-1)/3+4$ triangles for all $n\geq 4$ , and all arrangements with $n\geq 6$ have at most $7n(n-1)/18+1/3$ triangles. The closely related Kobon triangle problem asks for the maximum number of non-overlapping finite triangles in an arrangement in the Euclidean plane, not counting the unbounded faces that might form triangles in the projective plane. Again, the arrangements are not required to be simple. For some but not all values of n , there exist arrangements with $n(n-2)/3$ triangles.

## Multigrids and rhombus tilings

The dual graph of a simple line arrangement may be represented geometrically as a collection of rhombi, one per vertex of the arrangement, with sides perpendicular to the lines that meet at that vertex. These rhombi may be joined together to form a tiling of a convex polygon in the case of an arrangement of finitely many lines, or of the entire plane in the case of a locally finite arrangement with infinitely many lines. This construction is sometimes known as a Klee diagram, after a publication of Rudolf Klee in 1938 that used this technique. Not every rhombus tiling comes from lines in this way, however.

In a 1981 paper, N. G. de Bruijn investigated special cases of this construction in which the line arrangement consists of k sets of equally spaced parallel lines. For two perpendicular families of parallel lines this construction gives the square tiling of the plane, and for three families of lines at 120-degree angles from each other (themselves forming a trihexagonal tiling) this produces the rhombille tiling. However, for more families of lines this construction produces aperiodic tilings. In particular, for five families of lines at equal angles to each other (or, as de Bruijn calls this arrangement, a *pentagrid*) it produces a family of tilings that include the rhombic version of the Penrose tilings.

Tetrakis square tiling

Triangular tiling

Bisected hexagonal tiling

There also exist three infinite simplicial arrangements formed from sets of parallel lines. The tetrakis square tiling is an infinite arrangement of lines forming a periodic tiling that resembles a multigrid with four parallel families, but in which two of the families are more widely spaced than the other two, and in which the arrangement is simplicial rather than simple. Its dual is the truncated square tiling. Similarly, the triangular tiling is an infinite simplicial line arrangement with three parallel families, which has as its dual the hexagonal tiling, and the bisected hexagonal tiling is an infinite simplicial line arrangement with six parallel families and two line spacings, dual to the great rhombitrihexagonal tiling. These three examples come from three affine reflection groups in the Euclidean plane, systems of symmetries based on reflection across each line in these arrangements.

## Algorithms

Constructing an arrangement means, given as input a list of the lines in the arrangement, computing a representation of the vertices, edges, and cells of the arrangement together with the adjacencies between these objects. For instance, these features may be represented as a doubly connected edge list. Arrangements can be constructed efficiently by an incremental algorithm that adds one line at a time to the arrangement of the previously added lines. Each new line can be added in time proportional to the size of its zone, linear by the zone theorem. This results in a total construction time of $O(n^{2})$ . The memory requirements of this algorithm are also $O(n^{2})$ . It is possible instead to report the features of an arrangement without storing them all at once, in time $O(n^{2})$ and space $O(n)$ , by an algorithmic technique known as topological sweeping. Computing a line arrangement exactly requires a numerical precision several times greater than that of the input coordinates: if a line is specified by two points on it, the coordinates of the arrangement vertices may need four times as much precision as these input points. Therefore, computational geometers have also studied algorithms for constructing arrangements with limited numerical precision.

As well, researchers have studied efficient algorithms for constructing smaller portions of an arrangement, such as zones, k -levels, or the set of cells containing a given set of points. The problem of finding the arrangement vertex with the median x -coordinate arises (in a dual form) in robust statistics as the problem of computing the Theil–Sen estimator of a set of points.

Marc van Kreveld suggested the algorithmic problem of computing shortest paths between vertices in a line arrangement, where the paths are restricted to follow the edges of the arrangement, more quickly than the quadratic time that it would take to apply a shortest path algorithm to the whole arrangement graph. An approximation algorithm is known, and the problem may be solved efficiently for lines that fall into a small number of parallel families (as is typical for urban street grids), but the general problem remains open.

## Non-Euclidean line arrangements

A non-stretchable pseudoline arrangement of nine pseudolines. (All arrangements of fewer than nine pseudolines are stretchable.) Per

Pappus's hexagon theorem

, this arrangement cannot be realized in a

projective plane

over any field.

A hyperbolic line arrangement combinatorially equivalent to a

chord diagram

used by

Ageev (1996)

to show that

triangle-free

circle graphs

may sometimes need

5 colors

.

An arrangement of pseudolines is a family of curves that share similar topological properties with a line arrangement. These can be defined in the projective plane as simple closed curves any two of which meet in a single crossing point. A pseudoline arrangement is said to be *stretchable* if it is combinatorially equivalent to a line arrangement. Determining stretchability is a difficult computational task: it is complete for the existential theory of the reals to distinguish stretchable arrangements from non-stretchable ones. Every arrangement of finitely many pseudolines can be extended so that they become lines in a "spread", a type of non-Euclidean incidence geometry in which every two points of a topological plane are connected by a unique line (as in the Euclidean plane) but in which other axioms of Euclidean geometry may not apply.

Another type of non-Euclidean geometry is the hyperbolic plane, and arrangements of lines in this geometry have also been studied. Any finite set of lines in the Euclidean plane has a combinatorially equivalent arrangement in the hyperbolic plane (e.g. by enclosing the vertices of the arrangement by a large circle and interpreting the interior of the circle as a Klein model of the hyperbolic plane). However, parallel (non-crossing) pairs of lines are less restricted in hyperbolic line arrangements than in the Euclidean plane: in particular, the relation of being parallel is an equivalence relation for Euclidean lines but not for hyperbolic lines. The intersection graph of the lines in a hyperbolic arrangement can be an arbitrary circle graph. The corresponding concept to hyperbolic line arrangements for pseudolines is a *weak pseudoline arrangement*, a family of curves having the same topological properties as lines such that any two curves in the family either meet in a single crossing point or have no intersection.

## History

In a survey on arrangements, Pankaj Agarwal and Micha Sharir attribute the study of arrangements to Jakob Steiner, writing that "the first paper on this topic is perhaps" an 1826 paper of Steiner. In this paper, Steiner proved bounds on the maximum number of features of different types that an arrangement may have. After Steiner, the study of arrangements turned to higher-dimensional arrangements of hyperplanes, focusing on their overall structure and on single cells in these arrangements. The study of arrangements of lines, and of more complex features such as zones within these arrangements, returned to interest beginning in the 1980s as part of the foundations of computational geometry.
