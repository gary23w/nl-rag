---
title: "Ramsey's theorem"
source: https://en.wikipedia.org/wiki/Ramsey's_theorem
domain: ramsey-theory
license: CC-BY-SA-4.0
tags: ramsey theory, ramsey's theorem, van der waerden's theorem, szemeredi theorem
fetched: 2026-07-02
---

# Ramsey's theorem

In combinatorics, **Ramsey's theorem**, in one of its graph-theoretic forms, states that one will find monochromatic cliques in any edge labelling (with colours) of a sufficiently large complete graph.

As the simplest example, consider two colours (say, blue and red). Let r and s be any two positive integers. Ramsey's theorem states that there exists a least positive integer *R*(*r*, *s*) for which every blue-red edge colouring of the complete graph on *R*(*r*, *s*) vertices contains a blue clique on r vertices or a red clique on s vertices. (Here *R*(*r*, *s*) signifies an integer that depends on both r and s.)

Ramsey's theorem is a foundational result in combinatorics. The first version of this result was proved by Frank Ramsey. This initiated the combinatorial theory now called Ramsey theory, that seeks regularity amid disorder: general conditions for the existence of substructures with regular properties. In this application it is a question of the existence of *monochromatic subsets*, that is, subsets of connected edges of just one colour.

An extension of this theorem applies to any finite number of colours, rather than just two. More precisely, the theorem states that for any given number of colours, c, and any given integers *n*1, …, *nc*, there is a number, *R*(*n*1, …, *nc*), such that if the edges of a complete graph of order *R*(*n*1, …, *n**c*) are coloured with c different colours, then for some i between 1 and c, it must contain a complete subgraph of order ni whose edges are all colour i. The special case above has *c* = 2 (and *n*1 = *r* and *n*2 = *s*).

## Examples

### *R*(3, 3) = 6

Suppose the edges of a complete graph on 6 vertices are coloured red and blue. Pick a vertex, v. There are 5 edges incident to v and so (by the pigeonhole principle) at least 3 of them must be the same colour. Without loss of generality we can assume at least 3 of these edges, connecting the vertex, v, to vertices, r, s and t, are blue. (If not, exchange red and blue in what follows.) If any of the edges, (*rs*), (*rt*), (*st*), are also blue then we have an entirely blue triangle. If not, then those three edges are all red and we have an entirely red triangle. Since this argument works for any colouring, *any* *K*6 contains a monochromatic *K*3, and therefore *R*(3, 3) ≤ 6. The popular version of this is called the theorem on friends and strangers.

An alternative proof works by double counting. It goes as follows: Count the number of ordered triples of vertices, x, y, z, such that the edge, (*xy*), is red and the edge, (*yz*), is blue. Firstly, any given vertex will be the middle of either 0 × 5 = 0 (all edges from the vertex are the same colour), 1 × 4 = 4 (four are the same colour, one is the other colour), or 2 × 3 = 6 (three are the same colour, two are the other colour) such triples. Therefore, there are at most 6 × 6 = 36 such triples. Secondly, for any non-monochromatic triangle (*xyz*), there exist precisely two such triples. Therefore, there are at most 18 non-monochromatic triangles. Therefore, at least 2 of the 20 triangles in the *K*6 are monochromatic.

Conversely, it is possible to 2-colour a *K*5 without creating any monochromatic *K*3, showing that *R*(3, 3) > 5. The unique colouring is shown to the right. Thus *R*(3, 3) = 6.

The task of proving that *R*(3, 3) ≤ 6 was one of the problems of William Lowell Putnam Mathematical Competition in 1953, as well as in the Hungarian Math Olympiad in 1947.

### A multicolour example: *R*(3, 3, 3) = 17

The only two 3-colourings of

K

16

with no monochromatic

K

3

, up to isomorphism and permutation of colors: the untwisted (left) and twisted (right) colorings.

A multicolour Ramsey number is a Ramsey number using 3 or more colours. There are (up to symmetries) only two non-trivial multicolour Ramsey numbers for which the exact value is known, namely *R*(3, 3, 3) = 17 and *R*(3, 3, 4) = 30.

Suppose that we have an edge colouring of a complete graph using 3 colours, red, green and blue. Suppose further that the edge colouring has no monochromatic triangles. Select a vertex v. Consider the set of vertices that have a red edge to the vertex v. This is called the red neighbourhood of v. The red neighbourhood of v cannot contain any red edges, since otherwise there would be a red triangle consisting of the two endpoints of that red edge and the vertex v. Thus, the induced edge colouring on the red neighbourhood of v has edges coloured with only two colours, namely green and blue. Since *R*(3, 3) = 6, the red neighbourhood of v can contain at most 5 vertices. Similarly, the green and blue neighbourhoods of v can contain at most 5 vertices each. Since every vertex, except for v itself, is in one of the red, green or blue neighbourhoods of v, the entire complete graph can have at most 1 + 5 + 5 + 5 = 16 vertices. Thus, we have *R*(3, 3, 3) ≤ 17.

To see that *R*(3, 3, 3) = 17, it suffices to draw an edge colouring on the complete graph on 16 vertices with 3 colours that avoids monochromatic triangles. It turns out that there are exactly two such colourings on *K*16, the so-called untwisted and twisted colourings. Both colourings are shown in the figures to the right, with the untwisted colouring on the left, and the twisted colouring on the right.

If we select any colour of either the untwisted or twisted colouring on *K*16, and consider the graph whose edges are precisely those edges that have the specified colour, we will get the Clebsch graph.

It is known that there are exactly two edge colourings with 3 colours on *K*15 that avoid monochromatic triangles, which can be constructed by deleting any vertex from the untwisted and twisted colourings on *K*16, respectively.

It is also known that there are exactly 115 edge colourings with 3 colours on *K*14 that avoid monochromatic triangles, provided that we consider edge colourings that differ by a permutation of the colours as being the same.

It is of interest to find the sequence of the multicolor Ramsey numbers R(3,3,...,3), where there are n 3's. The sequence currently is only known up to *n* = 3, with the bounds for values as early as *n* = 4 being relatively loose: 51 ≤ *a*(4) ≤ 62. (sequence A003323 in the OEIS)

## Proof

### 2-colour case

The theorem for the 2-colour case can be proved by induction on *r* + *s*. It is clear from the definition that for all n, *R*(*n*, 2) = *R*(2, *n*) = *n*. This starts the induction. We prove that *R*(*r*, *s*) exists by finding an explicit bound for it. By the inductive hypothesis *R*(*r* − 1, *s*) and *R*(*r*, *s* − 1) exist.

Lemma 1.

$R(r,s)\leq R(r-1,s)+R(r,s-1).$

*Proof.* Consider a complete graph on *R*(*r* − 1, *s*) + *R*(*r*, *s* − 1) vertices whose edges are coloured with two colours. Pick a vertex v from the graph, and partition the remaining vertices into two sets M and N, such that for every vertex w, w is in M if edge (*vw*) is blue, and w is in N if (*vw*) is red. Because the graph has $R(r-1,s)+R(r,s-1)=|M|+|N|+1$ vertices, it follows that either $|M|\geq R(r-1,s)$ or $|N|\geq R(r,s-1).$ In the former case, if M has a red Ks then so does the original graph and we are finished. Otherwise M has a blue *K**r* − 1 and so $M\cup \{v\}$ has a blue Kr by the definition of M. The latter case is analogous. Thus the claim is true and we have completed the proof for 2 colours.

In this 2-colour case, if *R*(*r* − 1, *s*) and *R*(*r*, *s* − 1) are both even, the induction inequality can be strengthened to:

$R(r,s)\leq R(r-1,s)+R(r,s-1)-1.$

*Proof*. Suppose *p* = *R*(*r* − 1, *s*) and *q* = *R*(*r*, *s* − 1) are both even. Let *t* = *p* + *q* − 1 and consider a two-coloured graph of t vertices. If di is the degree of the i-th vertex in the blue subgraph, then by the Handshaking lemma, $\textstyle \sum _{i=1}^{t}d_{i}$ is even. Given that t is odd, there must be an even di. Assume without loss of generality that *d*1 is even, and that M and N are the vertices incident to vertex 1 in the blue and red subgraphs, respectively. Then both $|M|=d_{1}$ and $|N|=t-1-d_{1}$ are even. By the Pigeonhole principle, either $|M|\geq p-1,$ or $|N|\geq q.$ Since $|M|$ is even and *p* – 1 is odd, the first inequality can be strengthened, so either $|M|\geq p$ or $|N|\geq q.$ Suppose $|M|\geq p=R(r-1,s).$ Then either the M subgraph has a red Ks and the proof is complete, or it has a blue *K**r* – 1 which along with vertex 1 makes a blue Kr. The case $|N|\geq q=R(r,s-1)$ is treated similarly.

### Case of more colours

*Lemma 2.* If *c* > 2, then $R(n_{1},\dots ,n_{c})\leq R(n_{1},\dots ,n_{c-2},R(n_{c-1},n_{c})).$

*Proof.* Consider a complete graph of $R(n_{1},\dots ,n_{c-2},R(n_{c-1},n_{c}))$ vertices and colour its edges with c colours. Now 'go colour-blind' and pretend that *c* − 1 and c are the same colour. Thus the graph is now (*c* − 1)-coloured. Due to the definition of $R(n_{1},\dots ,n_{c-2},R(n_{c-1},n_{c})),$ such a graph contains either a Kni mono-chromatically coloured with colour i for some 1 ≤ *i* ≤ *c* − 2 or a *K**R*(*n**c* − 1, *nc*)-coloured in the 'blurred colour'. In the former case we are finished. In the latter case, we recover our sight again and see from the definition of *R*(*n**c* − 1, *nc*) we must have either a (*c* − 1)-monochrome *K**n**c* − 1 or a c-monochrome Knc. In either case the proof is complete.

Lemma 1 implies that any *R*(*r*,*s*) is finite. The right hand side of the inequality in Lemma 2 expresses a Ramsey number for c colours in terms of Ramsey numbers for fewer colours. Therefore, any *R*(*n*1, …, *nc*) is finite for any number of colours. This proves the theorem.

## Ramsey numbers

The numbers *R*(*r*, *s*) in Ramsey's theorem (and their extensions to more than two colours) are known as Ramsey numbers. The Ramsey number *R*(*m*, *n*) gives the solution to the party problem, which asks the minimum number of guests, *R*(*m*, *n*), that must be invited so that at least m will know each other or at least n will not know each other. In the language of graph theory, the Ramsey number is the minimum number of vertices, *v* = *R*(*m*, *n*), such that all undirected simple graphs of order v, contain a clique of order m, or an independent set of order n. Ramsey's theorem states that such a number exists for all m and n.

By symmetry, it is true that *R*(*m*, *n*) = *R*(*n*, *m*). An upper bound for *R*(*r*, *s*) can be extracted from the proof of the theorem, and other arguments give lower bounds. (The first exponential lower bound was obtained by Paul Erdős using the probabilistic method.) However, there is a vast gap between the tightest lower bounds and the tightest upper bounds. There are also very few numbers r and s for which we know the exact value of *R*(*r*, *s*).

Computing a lower bound L for *R*(*r*, *s*) usually requires exhibiting a blue/red colouring of the graph *K**L*−1 with no blue Kr subgraph and no red Ks subgraph. Such a counterexample is called a *Ramsey graph*. Brendan McKay maintains a list of known Ramsey graphs. Upper bounds are often considerably more difficult to establish: one either has to check all possible colourings to confirm the absence of a counterexample, or to present a mathematical argument for its absence.

### Computational complexity

> Erdős asks us to imagine an alien force, vastly more powerful than us, landing on Earth and demanding the value of *R*(5, 5) or they will destroy our planet. In that case, he claims, we should marshal all our computers and all our mathematicians and attempt to find the value. But suppose, instead, that they ask for *R*(6, 6). In that case, he believes, we should attempt to destroy the aliens.

— Joel Spencer

A sophisticated computer program does not need to look at all colourings individually in order to eliminate all of them; nevertheless it is a very difficult computational task that existing software can only manage on small sizes. Each complete graph Kn has ⁠1/2⁠*n*(*n* − 1) edges, so there would be a total of *c**n*(*n* − 1)/2 graphs to search through (for *c* colours) if brute force is used. Therefore, the complexity for searching all possible graphs (via brute force) is *O*(*c**n*2) for c colourings and at most n nodes.

The situation is unlikely to improve with the advent of quantum computers. One of the best-known searching algorithms for unstructured datasets exhibits only a quadratic speedup (cf. Grover's algorithm) relative to classical computers, so that the computation time is still exponential in the number of nodes.

### Known values

Unsolved problem in mathematics

What is the value of

R

(5, 5)

?

More unsolved problems in mathematics

As described above, *R*(3, 3) = 6. It is easy to prove that *R*(4, 2) = 4, and, more generally, that *R*(*s*, 2) = *s* for all s: a graph on *s* − 1 nodes with all edges coloured red serves as a counterexample and proves that *R*(*s*, 2) ≥ *s*; among colourings of a graph on s nodes, the colouring with all edges coloured red contains a s-node red subgraph, and all other colourings contain a 2-node blue subgraph (that is, a pair of nodes connected with a blue edge.)

Using induction inequalities and the handshaking lemma, it can be concluded that *R*(4, 3) ≤ *R*(4, 2) + *R*(3, 3) − 1 = 9, and therefore *R*(4, 4) ≤ *R*(4, 3) + *R*(3, 4) ≤ 18. There are only two (4, 4, 16) graphs (that is, 2-colourings of a complete graph on 16 nodes without 4-node red or blue complete subgraphs) among 6.4 × 1022 different 2-colourings of 16-node graphs, and only one (4, 4, 17) graph (the Paley graph of order 17) among 2.46 × 1026 colourings. It follows that *R*(4, 4) = 18.

The fact that *R*(4, 5) = 25 was first established by Brendan McKay and Stanisław Radziszowski in 1995.

The exact value of *R*(5, 5) is unknown, although it is known to lie between 43 (Geoffrey Exoo (1989)) and 46 (Angeltveit and McKay (2024)), inclusive.

In 1997, McKay, Radziszowski and Exoo employed computer-assisted graph generation methods to conjecture that *R*(5, 5) = 43. They were able to construct exactly 656 (5, 5, 42) graphs, arriving at the same set of graphs through different routes. None of the 656 graphs can be extended to a (5, 5, 43) graph.

In 2025, Tamburini performed a heuristic numerical calculation which identified 45 as "the most promising candidate" for *R*(5, 5).

For *R*(*r*, *s*) with *r*, *s* > 5, only weak bounds are available. Lower bounds for *R*(6, 6) and *R*(8, 8) have not been improved since 1965 and 1972, respectively.

*R*(*r*, *s*) with *r*, *s* ≤ 10 are shown in the table below. Where the exact value is unknown, the table lists the best known bounds. *R*(*r*, *s*) with *r* < 3 are given by *R*(1, *s*) = 1 and *R*(2, *s*) = *s* for all values of s.

The standard survey on the development of Ramsey number research is the *Dynamic Survey 1* of the *Electronic Journal of Combinatorics*, by Radziszowski, which is periodically updated. Where not cited otherwise, entries in the table below are taken from the June 2024 edition. (Note there is a trivial symmetry across the diagonal since *R*(*r*, *s*) = *R*(*s*, *r*).)

Values / known bounding ranges for Ramsey numbers

R

(

r

,

s

)

(sequence

A212954

in the

OEIS

)

s

r

1

2

3

4

5

6

7

8

9

10

1

1

1

1

1

1

1

1

1

1

1

2

2

3

4

5

6

7

8

9

10

3

6

9

14

18

23

28

36

40–41

4

18

25

36–40

49–58

59

–79

73–105

92–135

5

43–46

59

–85

80–133

101–193

133–282

149

–381

6

102–160

115

–270

134

–423

183–651

204–944

7

205–492

219–832

252–1368

292–2119

8

282–1518

329–2662

343–4402

9

565–4956

581–8675

10

798–16064

It is also interesting that Erdős showed R(*P*n, *K*m) = (n − 1).(m − 1) + 1, for a path and a complete graph with n and m vertices respectively. Also Chvatal showed R(*T*n, *K*m) = (n − 1).(m − 1) + 1, for a tree and a complete graph with n and m vertices respectively. These two theorems are the best examples of formulating Ramsey numbers for some special graphs.

### Asymptotics

The inequality *R*(*r*, *s*) ≤ *R*(*r* − 1, *s*) + *R*(*r*, *s* − 1) may be applied inductively to prove that

$R(r,s)\leq {\binom {r+s-2}{r-1}}.$

In particular, this result, due to Erdős and Szekeres, implies that when *r* = *s*,

$R(s,s)\leq (1+o(1)){\frac {4^{s-1}}{\sqrt {\pi s}}}.$

An exponential lower bound,

$R(s,s)\geq (1+o(1)){\frac {s}{{\sqrt {2}}e}}2^{s/2},$

was given by Erdős in 1947 and was instrumental in his introduction of the probabilistic method. There is a huge gap between these two bounds: for example, for *s* = 10, this gives 101 ≤ *R*(10, 10) ≤ 48,620. Nevertheless, the exponential growth factors of either bound were not improved for a long time, and for the lower bound it still stands at √2. There is no known explicit construction producing an exponential lower bound. The best known lower and upper bounds for diagonal Ramsey numbers are

$[1+o(1)]{\frac {{\sqrt {2}}s}{e}}2^{\frac {s}{2}}\leq R(s,s)\leq s^{-(c\log s)/(\log \log s)}4^{s},$

due to Spencer and Conlon, respectively; a 2023 preprint by Campos, Griffiths, Morris and Sahasrabudhe claims to have made exponential progress using an algorithmic construction relying on a graph structure called a "book", improving the upper bound to

$R(s,s)\leq (4-\varepsilon )^{s}{\text{ and }}R(s,t)\leq e^{-\delta t+o(s)}{\binom {s+t}{t}}.$

with $\varepsilon =2^{-7}$ and $\delta =50^{-1}$ .

In a separate preprint in 2024, Balister, Bollobás, Coampos, Griffiths, Hurley, Morris, Sahasrabudhe, and Tiba showed that there exists $\delta >0$ such that the r -colour Ramsey number $R_{r}(k)$ is bounded below by $\left(e^{-\delta }r^{r}\right)^{k}$ , and in particular

$R_{r}(k)\leq \left(e^{-2^{-160}r^{-12}}r^{r}\right)^{k}$

for sufficiently large k .

A 2024 preprint by Gupta, Ndiaye, Norin, and Wei claims an improvement of $\delta$ to $-0.14e^{-1}\leq 20^{-1}$ , and the diagonal Ramsey upper bound to

$R(s,s)\leq \left(4e^{-0.14e^{-1}}\right)^{s+o(s)}=3.7992...^{s+o(s)}$

For the off-diagonal Ramsey numbers *R*(3, *t*), it is known that they are of order ⁠*t*2/log *t*⁠; this may be stated equivalently as saying that the smallest possible independence number in an n-vertex triangle-free graph is

$\Theta \left({\sqrt {n\log n}}\right).$

The upper bound for *R*(3, *t*) is given by Ajtai, Komlós, and Szemerédi, the lower bound was obtained originally by Kim, and the implicit constant was improved independently by Fiz Pontiveros, Griffiths and Morris, and Bohman and Keevash, by analysing the triangle-free process.

In general, studying the more general "*H*-free process" has set the best known asymptotic lower bounds for general off-diagonal Ramsey numbers, *R*(*s*, *t*)

$c'_{s}{\frac {t^{\frac {s+1}{2}}}{(\log t)^{{\frac {s+1}{2}}-{\frac {1}{s-2}}}}}\leq R(s,t)\leq c_{s}{\frac {t^{s-1}}{(\log t)^{s-2}}}.$

In particular this gives an upper bound of $R(4,t)\leq c_{s}t^{3}(\log t)^{-2}$ . Mattheus and Verstraete (2024) gave a lower bound of $R(4,t)\geq c'_{s}t^{3}(\log t)^{-4}$ , determining the asymptotics of $R(4,t)$ up to logarithmic factors, and settling a question of Erdős, who offered 250 dollars for a proof that the lower limit has form $c'_{s}t^{3}(\log t)^{-d}$ .

### Formal verification of Ramsey numbers

The Ramsey number $R(3,8)$ and $R(3,9)$ have been formally verified to be 28 and 36. This verification was achieved using a combination of Boolean satisfiability (SAT) solving and computer algebra systems (CAS). The proof was generated automatically using the SAT+CAS approach, marking the first certifiable proof of $R(3,8)=28$ and $R(3,9)=36$ . The verification process for $R(3,8)$ and $R(3,9)$ was conducted using the SAT+CAS framework MathCheck, which integrates a SAT solver with a computer algebra system. The verification for $R(3,8)=28$ was completed in approximately 8 hours of wall clock time, producing a total proof size of 5.8 GiB. The verification for $R(3,9)=36$ was significantly more computationally intensive, requiring 26 hours of wall clock time and generating 289 GiB of proof data. The correctness of these results was independently verified using a modified version of the DRAT-trim proof checker.

The Ramsey number $R(4,5)$ has been formally verified to be 25. The original proof, developed by McKay and Radziszowski in 1995, combined high-level mathematical arguments with computational steps and used multiple independent implementations to reduce the possibility of programming errors. The formal proof was carried out using the HOL4 interactive theorem prover, limiting the potential for errors to the HOL4 kernel. Rather than directly verifying the original algorithms, the authors utilized HOL4's interface to the MiniSat SAT solver to formally prove key gluing lemmas.

## Induced Ramsey

There is a less well-known yet interesting analogue of Ramsey's theorem for induced subgraphs. Roughly speaking, instead of finding a monochromatic subgraph, we are now required to find a monochromatic induced subgraph. In this variant, it is no longer sufficient to restrict our focus to complete graphs, since the existence of a complete subgraph does not imply the existence of an induced subgraph. The qualitative statement of the theorem in the next section was first proven independently by Erdős, Hajnal and Pósa, Deuber and Rödl in the 1970s. Since then, there has been much research in obtaining good bounds for induced Ramsey numbers.

### Statement

Let H be a graph on n vertices. Then, there exists a graph G such that any coloring of the edges of G using two colors contains a monochromatic induced copy of H (i.e. an induced subgraph of G such that it is isomorphic to H and its edges are monochromatic). The smallest possible number of vertices of G is the **induced Ramsey number** *r*ind(*H*).

Sometimes, we also consider the asymmetric version of the problem. We define *r*ind(*X*,*Y*) to be the smallest possible number of vertices of a graph G such that every coloring of the edges of G using only red or blue contains a red induced subgraph of X or blue induced subgraph of Y.

### History and bounds

Similar to Ramsey's theorem, it is unclear a priori whether induced Ramsey numbers exist for every graph H. In the early 1970s, Erdős, Hajnal and Pósa, Deuber, and Rödl independently proved that this is the case. However, the original proofs gave terrible bounds (e.g. towers of twos) on the induced Ramsey numbers. It is interesting to ask if better bounds can be achieved. In 1974, Paul Erdős conjectured that there exists a constant c such that every graph H on k vertices satisfies *r*ind(*H*) ≤ 2*ck*. If this conjecture is true, it would be optimal up to the constant c because the complete graph achieves a lower bound of this form (in fact, it's the same as Ramsey numbers). However, this conjecture is still open as of now.

In 1984, Erdős and Hajnal claimed that they proved the bound

$r_{\text{ind}}(H)\leq 2^{2^{k^{1+o(1)}}}.$

However, that was still far from the exponential bound conjectured by Erdős. It was not until 1998 when a major breakthrough was achieved by Kohayakawa, Prömel and Rödl, who proved the first almost-exponential bound of *r*ind(*H*) ≤ 2*ck*(log *k*)2 for some constant c. Their approach was to consider a suitable random graph constructed on projective planes and show that it has the desired properties with nonzero probability. The idea of using random graphs on projective planes have also previously been used in studying Ramsey properties with respect to vertex colorings and the induced Ramsey problem on bounded degree graphs H.

Kohayakawa, Prömel and Rödl's bound remained the best general bound for a decade. In 2008, Fox and Sudakov provided an explicit construction for induced Ramsey numbers with the same bound. In fact, they showed that every (*n*,*d*,λ)-graph G with small λ and suitable d contains an induced monochromatic copy of any graph on k vertices in any coloring of edges of G in two colors. In particular, for some constant c, the Paley graph on *n* ≥ 2*ck* log2*k* vertices is such that all of its edge colorings in two colors contain an induced monochromatic copy of every k-vertex graph.

In 2010, Conlon, Fox and Sudakov were able to improve the bound to *r*ind(*H*) ≤ 2*ck* log *k*, which remains the current best upper bound for general induced Ramsey numbers. Similar to the previous work in 2008, they showed that every (*n*,*d*,λ)-graph G with small λ and edge density 1⁄2 contains an induced monochromatic copy of every graph on k vertices in any edge coloring in two colors. Currently, Erdős's conjecture that *r*ind(*H*) ≤ 2*ck* remains open and is one of the important problems in extremal graph theory.

For lower bounds, not much is known in general except for the fact that induced Ramsey numbers must be at least the corresponding Ramsey numbers. Some lower bounds have been obtained for some special cases (see Special Cases).

It is sometimes quite difficult to compute the Ramsey number. Indeed, the inequalities

$2^{n/2}\leq R(K_{n},K_{n})\leq 2^{2n}$

were proved by Erdős in 1947.

### Special cases

While the general bounds for the induced Ramsey numbers are exponential in the size of the graph, the behaviour is much different on special classes of graphs (in particular, sparse ones). Many of these classes have induced Ramsey numbers polynomial in the number of vertices.

If H is a cycle, path or star on k vertices, it is known that *r*ind(*H*) is linear in k.

If H is a tree on k vertices, it is known that *r*ind(*H*) = *O*(*k*2 log2*k*). It is also known that *r*ind(*H*) is superlinear (i.e. *r*ind(*H*) = ω(*k*)). Note that this is in contrast to the usual Ramsey numbers, where the Burr–Erdős conjecture (now proven) tells us that *r*(*H*) is linear (since trees are 1-degenerate).

For graphs H with number of vertices k and bounded degree Δ, it was conjectured that *r*ind(*H*) ≤ *cn**d*(Δ), for some constant d depending only on Δ. This result was first proven by Łuczak and Rödl in 1996, with *d*(Δ) growing as a tower of twos with height *O*(Δ2). More reasonable bounds for *d*(Δ) were obtained since then. In 2013, Conlon, Fox and Zhao showed using a counting lemma for sparse pseudorandom graphs that *r*ind(*H*) ≤ *cn*2Δ+8, where the exponent is best possible up to constant factors.

### Generalizations

Similar to Ramsey numbers, we can generalize the notion of induced Ramsey numbers to hypergraphs and multicolor settings.

#### More colors

We can also generalize the induced Ramsey's theorem to a multicolor setting. For graphs *H*1, *H*2, …, *Hr*, define *r*ind(*H*1, *H*2, …, *Hr*) to be the minimum number of vertices in a graph G such that, given any coloring of the edges of G into r colors, there exists an i such that 1 ≤ *i* ≤ *r* and such that G contains an induced subgraph isomorphic to Hi whose edges are all colored in the i-th color. Let *r*ind(*H*;*q*) := *r*ind(*H*, *H*, …, *H*) (q copies of H).

It is possible to derive a bound on *r*ind(*H*;*q*) which is approximately a tower of two of height ~ log *q* by iteratively applying the bound on the two-color case. The current best known bound is due to Fox and Sudakov, which achieves *r*ind(*H*;*q*) ≤ 2*ck*3, where k is the number of vertices of H and c is a constant depending only on q.

#### Hypergraphs

We can extend the definition of induced Ramsey numbers to d-uniform hypergraphs by simply changing the word *graph* in the statement to *hypergraph*. Furthermore, we can define the multicolor version of induced Ramsey numbers in the same way as the previous subsection.

Let H be a d-uniform hypergraph with k vertices. Define the tower function *tr*(*x*) by letting *t*1(*x*) = *x* and for *i* ≥ 1, *t**i*+1(*x*) = 2*ti*(*x*). Using the hypergraph container method, Conlon, Dellamonica, La Fleur, Rödl and Schacht were able to show that for *d* ≥ 3, *q* ≥ 2, *r*ind(*H*;*q*) ≤ *td*(*ck*) for some constant c depending on only d and q. In particular, this result mirrors the best known bound for the usual Ramsey number when *d* = 3.

## Extensions of the theorem

### Infinite graphs

A further result, also commonly called *Ramsey's theorem*, applies to infinite graphs. In a context where finite graphs are also being discussed it is often called the "Infinite Ramsey theorem". As intuition provided by the pictorial representation of a graph is diminished when moving from finite to infinite graphs, theorems in this area are usually phrased in set-theoretic terminology.

Theorem.

Let

X

be some

infinite set

and colour the elements of

$[X]^{n}$

(the subsets of

X

of size

n

) in

c

different colours. Then there exists some infinite subset

M

of

X

such that the size

n

subsets of

M

all have the same colour.

*Proof*: The proof is by induction on n, the size of the subsets. For *n* = 1, the statement is equivalent to saying that if you split an infinite set into a finite number of sets, then one of them is infinite. This is evident. Assuming the theorem is true for *n* ≤ *r*, we prove it for *n* = *r* + 1. Given a c-colouring of the (*r* + 1)-element subsets of X, let *a*0 be an element of X and let *Y* = *X* \ {*a*0}. We then induce a c-colouring of the r-element subsets of Y, by just adding *a*0 to each r-element subset (to get an (*r* + 1)-element subset of X). By the induction hypothesis, there exists an infinite subset *Y*1 of Y such that every r-element subset of *Y*1 is coloured the same colour in the induced colouring. Thus there is an element *a*0 and an infinite subset *Y*1 such that all the (*r* + 1)-element subsets of X consisting of *a*0 and r elements of *Y*1 have the same colour. By the same argument, there is an element *a*1 in *Y*1 and an infinite subset *Y*2 of *Y*1 with the same properties. Inductively, we obtain a sequence {*a*0, *a*1, *a*2, …} such that the colour of each (*r* + 1)-element subset (*a**i*(1), *a**i*(2), …, *a**i*(*r* + 1)) with *i*(1) < *i*(2) < … < *i*(*r* + 1) depends only on the value of *i*(1). Further, there are infinitely many values of *i*(*n*) such that this colour will be the same. Take these *a**i*(*n*)'s to get the desired monochromatic set.

A stronger but unbalanced infinite form of Ramsey's theorem for graphs, the Erdős–Dushnik–Miller theorem, states that every infinite graph contains either a countably infinite independent set, or an infinite clique of the same cardinality as the original graph.

#### Infinite version implies the finite

It is possible to deduce the finite Ramsey theorem from the infinite version by a proof by contradiction. Suppose the finite Ramsey theorem is false. Then there exist integers c, n, T such that for every integer k, there exists a c-colouring of [*k*](*n*) without a monochromatic set of size T. Let Ck denote the c-colourings of [*k*](*n*) without a monochromatic set of size T.

For any k, the restriction of a colouring in *C**k*+1 to [*k*](*n*) (by ignoring the colour of all sets containing *k* + 1) is a colouring in Ck. Define ⁠ $C_{k}^{1}$ ⁠ to be the colourings in Ck which are restrictions of colourings in *C**k*+1. Since *C**k*+1 is not empty, neither is ⁠ $C_{k}^{1}$ ⁠.

Similarly, the restriction of any colouring in ⁠ $C_{k+1}^{1}$ ⁠ is in ⁠ $C_{k}^{1}$ ⁠, allowing one to define ⁠ $C_{k}^{2}$ ⁠ as the set of all such restrictions, a non-empty set. Continuing so, define ⁠ $C_{k}^{m}$ ⁠ for all integers m, k.

Now, for any integer k,

$C_{k}\supseteq C_{k}^{1}\supseteq C_{k}^{2}\supseteq \cdots$

and each set is non-empty. Furthermore, Ck is finite as

$|C_{k}|\leq c^{\frac {k!}{n!(k-n)!}}$

It follows that the intersection of all of these sets is non-empty, and let

$D_{k}=C_{k}\cap C_{k}^{1}\cap C_{k}^{2}\cap \cdots$

Then every colouring in Dk is the restriction of a colouring in *D**k*+1. Therefore, by unrestricting a colouring in Dk to a colouring in *D**k*+1, and continuing doing so, one constructs a colouring of $\mathbb {N} ^{(n)}$ without any monochromatic set of size T. This contradicts the infinite Ramsey theorem.

If a suitable topological viewpoint is taken, this argument becomes a standard compactness argument showing that the infinite version of the theorem implies the finite version.

### Hypergraphs

The theorem can also be extended to hypergraphs. An m-hypergraph is a graph whose "edges" are sets of m vertices – in a normal graph an edge is a set of 2 vertices. The full statement of Ramsey's theorem for hypergraphs is that for any integers m and c, and any integers *n*1, …, *nc*, there is an integer *R*(*n*1, …, *nc*; m) such that if the hyperedges of a complete m-hypergraph of order *R*(*n*1, …, *nc*; *m*) are coloured with c different colours, then for some i between 1 and c, the hypergraph must contain a complete sub-m-hypergraph of order ni whose hyperedges are all colour i. This theorem is usually proved by induction on m, the 'hyper-ness' of the graph. The base case for the proof is *m* = 2, which is exactly the theorem above.

For *m* = 3 we know the exact value of one non-trivial Ramsey number, namely *R*(4, 4; 3) = 13. This fact was established by Brendan McKay and Stanisław Radziszowski in 1991. Additionally, we have: *R*(4, 5; 3) ≥ 35, *R*(4, 6; 3) ≥ 63 and *R*(5, 5; 3) ≥ 88.

### Directed graphs

It is also possible to define Ramsey numbers for *directed* graphs; these were introduced by P. Erdős and L. Moser (1964). Let *R*(*n*) be the smallest number Q such that any complete graph with singly directed arcs (also called a "tournament") and with ≥ *Q* nodes contains an acyclic (also called "transitive") n-node subtournament.

This is the directed-graph analogue of what (above) has been called *R*(*n*, *n*; 2), the smallest number Z such that any 2-colouring of the edges of a complete *un*directed graph with ≥ *Z* nodes, contains a monochromatic complete graph on n nodes. (The directed analogue of the two possible arc *colours* is the two *directions* of the arcs, the analogue of "monochromatic" is "all arc-arrows point the same way"; i.e., "acyclic.")

We have *R*(0) = 0, *R*(1) = 1, *R*(2) = 2, *R*(3) = 4, *R*(4) = 8, *R*(5) = 14, *R*(6) = 28, and 34 ≤ *R*(7) ≤ 47.

### Uncountable cardinals

In terms of the partition calculus, Ramsey's theorem can be stated as $\aleph _{0}\rightarrow (\aleph _{0})_{k}^{n}$ for all finite *n* and *k*. Wacław Sierpiński showed that the Ramsey theorem does not extend to graphs of size $\aleph _{1}$ by showing that $2^{\aleph _{0}}\nrightarrow (\aleph _{1})_{2}^{2}$ . In particular, the continuum hypothesis implies that $\aleph _{1}\nrightarrow (\aleph _{1})_{2}^{2}$ . Stevo Todorčević showed that in fact in ZFC, $\aleph _{1}\nrightarrow [\aleph _{1}]_{\aleph _{1}}^{2}$ , a much stronger statement than $\aleph _{1}\nrightarrow (\aleph _{1})_{2}^{2}$ . Justin T. Moore has strengthened this result further. On the positive side, a Ramsey cardinal is a large cardinal $\kappa$ axiomatically defined to satisfy the related formula: $\kappa \rightarrow (\kappa )_{2}^{<\omega }$ . The existence of Ramsey cardinals cannot be proved in ZFC.

## Reverse mathematics

In reverse mathematics, there is a significant difference in proof strength between the versions of Ramsey's theorem. Some are equally strong as one of the big five subsystems in reverse mathematics, but others are not. By a theorem of David Seetapun, the graph version of the theorem is weaker than ACA0, and (combining Seetapun's result with others) it does not fall into one of the big five subsystems.

Let $RT_{k}^{n}$ denote Ramsey's theorem for when we *k*-color the *n*-sized subsets of the natural numbers $\mathbb {N}$ , and let $RT_{<\infty }^{n}:=\forall k,RT_{k}^{n}$ denote Ramsey's theorem for any finite *k* with a single fixed *n*.

Also, let $c:\mathbb {N} ^{2}\to \{1,2,\dots ,k\}$ be a *k*-coloring of the complete graph on $\mathbb {N}$ . It is a **stable coloring** iff $\forall n\in \mathbb {N}$ , there exists some color i , such that $c(n,m)=i$ for all large enough *m*. The **Stable Ramsey's Theorem for Pairs** $SRT_{k}^{2}$ is defined as Ramsey's theorem for when we stably k-color the edges of the complete graph on $\mathbb {N}$ . This is a weakening on $RT_{k}^{2}$ , since by definition, we have $RT_{k}^{2}\vdash SRT_{k}^{2}$ .

Over the system of RCA0, we have

- $RT_{<\infty }^{1}$ is the infinite pigeonhole principle.
- For any particularly fixed *k*, $RCA_{0}\vdash RT_{k}^{1}$ .
- However, $RCA_{0}\not \vdash RT_{<\infty }^{1}$ . In fact, $RT_{<\infty }^{1}$ is slightly stronger, and equivalent in strength to $B\Sigma _{2}^{0}$ and to $I\Delta _{2}^{0}$ .
  - This shows that RCA0 is not ω-complete.
  - The axiom schema $I\Delta _{2}^{0}$ , called " $\Delta _{2}^{0}$ -induction", states that

$\varphi (0)\to \forall n(\varphi (n)\to \varphi (Sn))\to \forall n,\varphi (n)$ for each $\phi$ that is a $\Delta _{2}^{0}$ formula without quantification over set variables.

  - The axiom schema $B\Sigma _{2}^{0}$ , called " $\Sigma _{2}^{0}$ -bounding", states that $\forall n[\forall i<n\exists k,\phi (i,k)\to \exists b\forall i<n\exists k<b,\phi (i,k)]$ for each $\phi$ that is a $\Sigma _{2}^{0}$ formula without quantification over set variables. Intuitively, it says that if $\phi (0,k),\phi (1,k),\dots ,\phi (n,k)$ each can be satisfied for some $k_{1},k_{2},\dots ,k_{n}$ , then there exists some common upper bound $b>k_{1},\dots ,k_{n}$ . This allows one to exchange bounded quantifiers with unbounded quantifiers.
- $RCA_{0}+SRT_{2}^{2}\vdash RT_{<\infty }^{1}$
- $WKL_{0},RT_{2}^{2}$ are mutually incomparable in strength over RCA0. That is, both $RCA_{0}+RT_{2}^{2}\not \vdash WKL_{0}$ and $WKL_{0}\not \vdash RT_{2}^{2}$ .
- $WKL_{0}+RT_{2}^{2}\not \vdash ACA_{0}$ . That is, their combined system is still too weak to prove the system with the arithmetical comprehension axiom.
- $RCA_{0}+RT_{2}^{3}\vdash ACA_{0}$ .
- For any $n\geq 3$ , $ACA_{0}\vdash RT_{<\infty }^{n}$ . That is, $ACA_{0},RT_{2}^{3},RT_{<\infty }^{3},RT_{<\infty }^{4},\dots$ are equivalent in strength.
- However, $ACA_{0}\not \vdash \forall n,RT_{<\infty }^{n}$ . In fact, $\forall n,RT_{<\infty }^{n}$ is stronger than ACA0, such that it is sufficient to prove the Paris–Harrington theorem.
  - This is the same issue as with $RCA_{0}\not \vdash RT_{<\infty }^{1}$ . Roughly, in the previous statement, given some *n*, the proof of $RT_{<\infty }^{n}$ can be carried out in ACA0, but there is no proof that works uniformly over all *n*. That is, the "for any *n*" part was *external* to the system. This shows that ACA0 is not ω-complete.

From the recursion theory side, the power of $RT_{2}^{n}$ is that it allows us to construct the sets at exactly the level of $\emptyset ^{(n-2)}$ , using the notation for Turing jumps.

Over ZF, the graph version implies the classical Kőnig's lemma, whereas the converse implication does not hold, since Kőnig's lemma is equivalent to countable choice from finite sets in this setting.
