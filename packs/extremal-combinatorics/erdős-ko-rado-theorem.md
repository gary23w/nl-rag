---
title: "Erdős–Ko–Rado theorem"
source: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Ko%E2%80%93Rado_theorem
domain: extremal-combinatorics
license: CC-BY-SA-4.0
tags: extremal combinatorics, probabilistic method, dilworth's theorem, turan theorem
fetched: 2026-07-02
---

# Erdős–Ko–Rado theorem

In mathematics, the **Erdős–Ko–Rado theorem** limits the number of sets in a family of sets for which every two sets have at least one element in common. Paul Erdős, Chao Ko, and Richard Rado proved the theorem in 1938, but did not publish it until 1961. It is part of the field of combinatorics, and one of the central results of extremal set theory.

The theorem applies to families of sets that all have the same size, r , and are all subsets of some larger set of size n . One way to construct a family of sets with these parameters, each two sharing an element, is to choose a single element to belong to all the subsets, and then form all of the subsets of size r that contain the chosen element. The Erdős–Ko–Rado theorem states that when n is large enough for the problem to be nontrivial ( $n\geq 2r$ ) this construction produces the largest possible intersecting families. When $n=2r$ there are other equally-large families, but for larger values of n only the families constructed in this way can be largest.

The Erdős–Ko–Rado theorem can also be described in terms of hypergraphs or independent sets in Kneser graphs. Several analogous theorems apply to other kinds of mathematical object than sets, including linear subspaces, permutations, and strings. They again describe the largest possible intersecting families as being formed by choosing an element and forming the family of all objects that contain the chosen element.

## Statement

Suppose that ${\mathcal {A}}$ is a family of distinct r -element subsets of an n -element set with $n\geq 2r$ , and that each two subsets share at least one element. Then the theorem states that the number of sets in ${\mathcal {A}}$ is at most the binomial coefficient ${\binom {n-1}{r-1}}.$ The requirement that $n\geq 2r$ is necessary for the problem to be nontrivial: when $n<2r$ , all r -element sets intersect, and the largest intersecting family consists of all r -element sets, with size ${\tbinom {n}{r}}$ .

The same result can be formulated as part of the theory of hypergraphs. A family of sets may also be called a hypergraph, and when all the sets (which are called "hyperedges" in this context) are the same size r , it is called an r -uniform hypergraph. The theorem thus gives an upper bound for the number of pairwise overlapping hyperedges in an r -uniform hypergraph with n vertices and $n\geq 2r$ .

The theorem may also be formulated in terms of graph theory: the independence number of the Kneser graph $KG_{n,r}$ for $n\geq 2r$ is $\alpha (KG_{n,r})={\binom {n-1}{r-1}}.$ This is a graph with a vertex for each r -element subset of an n -element set, and an edge between every pair of disjoint sets. An independent set is a collection of vertices that has no edges between its pairs, and the independence number is the size of the largest independent set. Because Kneser graphs have symmetries taking any vertex to any other vertex (they are vertex-transitive graphs), their fractional chromatic number equals the ratio of their number of vertices to their independence number, so another way of expressing the Erdős–Ko–Rado theorem is that these graphs have fractional chromatic number exactly $n/r$ .

## History

Paul Erdős, Chao Ko, and Richard Rado proved this theorem in 1938 after working together on it in England. Rado had moved from Berlin to the University of Cambridge and Erdős from Hungary to the University of Manchester, both escaping the influence of Nazi Germany; Ko was a student of Louis J. Mordell at Manchester. However, they did not publish the result until 1961, with the long delay occurring in part because of a lack of interest in combinatorial set theory in the 1930s, and increased interest in the topic in the 1960s. The 1961 paper stated the result in an apparently more general form, in which the subsets were only required to be size *at most* r , and to satisfy the additional requirement that no subset be contained in any other. A family of subsets meeting these conditions can be enlarged to subsets of size exactly r either by an application of Hall's marriage theorem, or by choosing each enlarged subset from the same chain in a symmetric chain decomposition of sets.

## Maximum and maximal families

### Families of maximum size

A simple way to construct an intersecting family of r -element sets whose size exactly matches the Erdős–Ko–Rado bound is to choose any fixed element x , and let ${\mathcal {A}}$ consist of all r -element subsets that include x . For instance, for 2-element subsets of the 4-element set $\{1,2,3,4\}$ , with $x=1$ , this produces the family

$\{1,2\}$

,

$\{1,3\}$

,

and

$\{1,4\}$

.

Any two sets in this family intersect, because they both include 1 . The number of sets is ${\tbinom {n-1}{r-1}}$ , because after the fixed element is chosen there remain $n-1$ other elements to choose, and each set chooses $r-1$ of these remaining elements.

When $n>2r$ this is the only intersecting family of this size. However, when $n=2r$ , there is a more general construction. Each r -element set can be matched up to its complement, the only r -element set from which it is disjoint. Then, choose one set from each of these complementary pairs. For instance, for the same parameters above, this more general construction can be used to form the family

$\{3,4\}$

,

$\{2,4\}$

,

and

$\{2,3\}$

,

where every two sets intersect despite no element belonging to all three sets. In this example, all of the sets have been complemented from the ones in the first example, but it is also possible to complement only some of the sets.

When $n>2r$ , families of the first type (variously known as stars, dictatorships, juntas, centered families, or principal families) are the unique maximum families. In this case, a family of nearly-maximum size has an element which is common to almost all of its sets. This property has been called *stability*, although the same term has also been used for a different property, the fact that (for a wide range of parameters) deleting randomly-chosen edges from the Kneser graph does not increase the size of its independent sets.

### Maximal intersecting families

An intersecting family of r -element sets may be maximal, in that no further set can be added (even by extending the ground set) without destroying the intersection property, but not of maximum size. An example with $n=7$ and $r=3$ is the set of seven lines of the Fano plane, much less than the Erdős–Ko–Rado bound of 15. More generally, the lines of any finite projective plane of order q form a maximal intersecting family that includes only n sets, for the parameters $r=q+1$ and $n=q^{2}+q+1$ . The Fano plane is the case $q=2$ of this construction.

The smallest possible size of a maximal intersecting family of r -element sets, in terms of r , is unknown but at least $3r$ for $r\geq 4$ . Projective planes produce maximal intersecting families whose number of sets is $r^{2}-r+1$ , but for infinitely many choices of r there exist smaller maximal intersecting families of size ${\tfrac {3}{4}}r^{2}$ .

The largest intersecting families of r -element sets that are maximal but not maximum have size ${\binom {n-1}{r-1}}-{\binom {n-r-1}{r-1}}+1.$ They are formed from an element x and an r -element set Y not containing x , by adding Y to the family of r -element sets that include both x and at least one element of Y . This result is called the **Hilton–Milner theorem**, after its proof by Anthony Hilton and Eric Charles Milner in 1967.

## Proofs

The original proof of the Erdős–Ko–Rado theorem used induction on n . The base case, for $n=2r$ , follows easily from the facts that an intersecting family cannot include both a set and its complement, and that in this case the bound of the Erdős–Ko–Rado theorem is exactly half the number of all r -element sets. The induction step for larger n uses a method called *shifting*, of substituting elements in intersecting families to make the family smaller in lexicographic order and reduce it to a canonical form that is easier to analyze.

In 1972, Gyula O. H. Katona gave the following short proof using double counting.

Let

${\mathcal {A}}$

be any intersecting family of

r

-element

subsets of an

n

-element

set. Arrange all

n

elements

into any

cyclic order

, and consider the sets from

${\mathcal {A}}$

that form intervals of

length

r

within this chosen cyclic order. For example if

$n=8$

and

$r=3$

,

one possible cyclic order for the numbers

$\{1,2,...,8\}$

is the order

$(3,1,5,4,2,7,6,8)$

,

which has eight 3-element intervals (including the ones that wrap around):

$(3,1,5)$

,

$(1,5,4)$

,

$(5,4,2)$

,

$(4,2,7)$

,

$(2,7,6)$

,

$(7,6,8)$

,

$(6,8,3)$

, and

$(8,3,1)$

.

However, only some of these intervals can belong to ${\mathcal {A}}$ , because they do not all intersect. Katona's key observation is that at most r intervals from a single cyclic order may belong to ${\mathcal {A}}$ . This is because, if $(a_{1},a_{2},\dots ,a_{r})$ is one of these intervals, then every other interval of the same cyclic order that belongs to ${\mathcal {A}}$ separates $a_{i}$ from $a_{i+1}$ , for some i , by containing precisely one of these two elements. The two intervals that separate these elements are disjoint, so at most one of them can belong to ${\mathcal {A}}$ . Thus, the number of intervals in ${\mathcal {A}}$ is at most one plus the number $r-1$ of pairs that can be separated.

Based on this idea, it is possible to count the pairs $(S,C)$ , where S is a set in ${\mathcal {A}}$ and C is a cyclic order for which S is an interval, in two ways. First, for each set S one may generate C by choosing one of $r!$ permutations of S and $(n-r)!$ permutations of the remaining elements, showing that the number of pairs is $|{\mathcal {A}}|r!(n-r)!$ . And second, there are $(n-1)!$ cyclic orders, each of which has at most r intervals of ${\mathcal {A}}$ , so the number of pairs is at most $r(n-1)!$ . Comparing these two counts gives the inequality $|{\mathcal {A}}|r!(n-r)!\leq r(n-1)!$ and dividing both sides by $r!(n-r)!$ gives the result

$|{\mathcal {A}}|\leq {\frac {r(n-1)!}{r!(n-r)!}}={n-1 \choose r-1}.$

It is also possible to derive the Erdős–Ko–Rado theorem as a special case of the Kruskal–Katona theorem, another important result in extremal set theory. Many other proofs are known.

### Generalizations

A generalization of the theorem applies to subsets that are required to have large intersections. This version of the theorem has three parameters: n , the number of elements the subsets are drawn from, r , the size of the subsets, as before, and t , the minimum size of the intersection of any two subsets. For the original form of the Erdős–Ko–Rado theorem, $t=1$ . In general, for n large enough with respect to the other two parameters, the generalized theorem states that the size of a t -intersecting family of subsets is at most ${\binom {n-t}{r-t}}.$ More precisely, this bound holds when $n\geq (t+1)(r-t+1)$ , and does not hold for smaller values of n . When $n>(t+1)(r-t+1)$ , the only t -intersecting families of this size are obtained by designating t elements as the common intersection of all the subsets, and constructing the family of all r -element subsets that include these t designated elements. The maximal size of a t-intersecting family when $n<(t+1)(r-t+1)$ was determined by Ahlswede and Khachatrian, in their Ahlswede–Khachatrian theorem.

The corresponding graph-theoretic formulation of this generalization involves Johnson graphs in place of Kneser graphs. For large enough values of n and in particular for $n>{\tfrac {1}{2}}r^{2}$ , both the Erdős–Ko–Rado theorem and its generalization can be strengthened from the independence number to the Shannon capacity of a graph: the Johnson graph corresponding to the t -intersecting r -element subsets has Shannon capacity ${\tbinom {n-t}{r-t}}$ .

The theorem can also be generalized to families in which every h subsets have a common intersection. Because this strengthens the condition that every pair intersects (for which $h=2$ ), these families have the same bound on their maximum size, ${\tbinom {n-1}{r-1}}$ when n is sufficiently large. However, in this case the meaning of "sufficiently large" can be relaxed from $n\geq 2r$ to $n\geq {\tfrac {h}{h-1}}r$ .

### Analogs

Many results analogous to the Erdős–Ko–Rado theorem, but for other classes of objects than finite sets, are known. These generally involve a statement that the largest families of intersecting objects, for some definition of intersection, are obtained by choosing an element and constructing the family of all objects that include that chosen element. Examples include the following:

There is a q-analog of the Erdős–Ko–Rado theorem for intersecting families of linear subspaces over finite fields. If ${\mathcal {S}}$ is an intersecting family of r -dimensional subspaces of an n -dimensional vector space over a finite field of order q , and $n\geq 2r$ , then $|{\mathcal {S}}|\leq {\binom {n-1}{r-1}}_{q},$ where the subscript q marks the notation for the Gaussian binomial coefficient, the number of subspaces of a given dimension within a vector space of a larger dimension over a finite field of order q. In this case, a largest intersecting family of subspaces may be obtained by choosing any nonzero vector and constructing the family of subspaces of the given dimension that all contain the chosen vector.

Two permutations on the same set of elements are defined to be intersecting if there is some element that has the same image under both permutations. On an n -element set, there is an obvious family of $(n-1)!$ intersecting permutations, the permutations that fix one of the elements (the stabilizer subgroup of this element). The analogous theorem is that no intersecting family of permutations can be larger, and that the only intersecting families of size $(n-1)!$ are the cosets of one-element stabilizers. These can be described more directly as the families of permutations that map some fixed element to another fixed element. More generally, for any t and sufficiently large n , a family of permutations each pair of which has t elements in common has maximum size $(n-t)!$ , and the only families of this size are cosets of pointwise stabilizers. Alternatively, in graph theoretic terms, the n -element permutations correspond to the perfect matchings of a complete bipartite graph $K_{n,n}$ and the theorem states that, among families of perfect matchings each pair of which share t edges, the largest families are formed by the matchings that all contain t chosen edges. Another analog of the theorem, for partitions of a set, includes as a special case the perfect matchings of a complete graph $K_{n}$ (with n even). There are $(n-1)!!$ matchings, where ${\displaystyle$ denotes the double factorial. The largest family of matchings that pairwise intersect (meaning that they have an edge in common) has size $(n-3)!!$ and is obtained by fixing one edge and choosing all ways of matching the remaining $n-2$ vertices.

A partial geometry is a system of finitely many abstract points and lines, satisfying certain axioms including the requirement that all lines contain the same number of points and all points belong to the same number of lines. In a partial geometry, a largest system of pairwise-intersecting lines can be obtained from the set of lines through any single point.

A signed set consists of a set together with sign function that maps each element to $\{1,-1\}$ . Two signed sets may be said to intersect when they have a common element that has the same sign in each of them. Then an intersecting family of r -element signed sets, drawn from an n -element universe, consists of at most $2^{r-1}{\binom {n-1}{r-1}}$ signed sets. This number of signed sets may be obtained by fixing one element and its sign and letting the remaining $r-1$ elements and signs vary.

For strings of length n over an alphabet of size q , two strings can be defined to intersect if they have a position where both share the same symbol. The largest intersecting families are obtained by choosing one position and a fixed symbol for that position, and letting the rest of the positions vary arbitrarily. These families consist of ${\textstyle q^{n-1}}$ strings, and are the only pairwise intersecting families of this size. More generally, the largest families of strings in which every two have t positions with equal symbols are obtained by choosing $t+2i$ positions and symbols for those positions, for a number i that depends on n , q , and t , and constructing the family of strings that each have at least $t+i$ of the chosen symbols. These results can be interpreted graph-theoretically in terms of the Hamming scheme.

Unsolved problem in mathematics

Is the largest family of intersecting triangulations of a convex polygon obtained by cutting off one vertex and choosing all triangulations of the remaining polygon?

More unsolved problems in mathematics

An unproven conjecture, posed by Gil Kalai and Karen Meagher, concerns another analog for the family of triangulations of a convex polygon with n vertices. The number of all triangulations is a Catalan number $C_{n-2}$ , and the conjecture states that a family of triangulations every pair of which shares an edge has maximum size $C_{n-3}$ . An intersecting family of size exactly $C_{n-3}$ may be obtained by cutting off a single vertex of the polygon by a triangle, and choosing all ways of triangulating the remaining $(n-1)$ -vertex polygon.

## Applications

The Erdős–Ko–Rado theorem can be used to prove the following result in probability theory. Let $x_{i}$ be independent 0–1 random variables with probability $p\geq {\tfrac {1}{2}}$ of being one, and let $c({\vec {x}})$ be any fixed convex combination of these variables. Then $\Pr \left[c({\vec {x}})\geq {\tfrac {1}{2}}\right]\geq p.$ The proof involves observing that subsets of variables whose indicator vectors have large convex combinations must be non-disjoint and using the Erdős–Ko–Rado theorem to bound the number of these subsets.

The stability properties of the Erdős–Ko–Rado theorem play a key role in an efficient algorithm for finding monochromatic edges in improper colorings of Kneser graphs. The Erdős–Ko–Rado theorem has also been used to characterize the symmetries of the space of phylogenetic trees.
