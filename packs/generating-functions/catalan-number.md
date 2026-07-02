---
title: "Catalan number"
source: https://en.wikipedia.org/wiki/Catalan_number
domain: generating-functions
license: CC-BY-SA-4.0
tags: generating function, formal power series, catalan number, binomial coefficient
fetched: 2026-07-02
---

# Catalan number

The **Catalan numbers** are a sequence of natural numbers that occur in various counting problems, often involving recursively defined objects. They are named after Eugène Catalan, though they were previously discovered in the 1730s by Minggatu.

The n-th Catalan number can be expressed directly in terms of the central binomial coefficients by

$C_{n}={\frac {1}{n+1}}{2n \choose n}={\frac {(2n)!}{(n+1)!\,n!}}\qquad {\text{for }}n\geq 0.$

The first Catalan numbers for *n* = 0, 1, 2, 3, ... are

1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, ...

(sequence

A000108

in the

OEIS

).

## Properties

An alternative expression for *C**n* is $C_{n}={\binom {2n}{n}}-{\binom {2n}{n+1}}\quad {\text{for }}n\geq 0\,,$ which is equivalent to the expression given above because ${\textstyle {\binom {2n}{n+1}}={\frac {n}{n+1}}{\binom {2n}{n}}}$ . This expression shows that *C**n* is an integer, which is not immediately obvious from the first formula given. This expression forms the basis for a proof of the correctness of the formula.

Another alternative expression is $C_{n}={\frac {1}{2n+1}}{\binom {2n+1}{n}}\,,$ which can be directly interpreted in terms of the cycle lemma; see below.

The Catalan numbers satisfy the recurrence relations $C_{0}=1\quad {\text{and}}\quad C_{n}=\sum _{i=1}^{n}C_{i-1}C_{n-i}\quad {\text{for }}n>0$ and $C_{0}=1\quad {\text{and}}\quad C_{n}={\frac {2(2n-1)}{n+1}}C_{n-1}\quad {\text{for }}n>0.$

Asymptotically, the Catalan numbers grow as $C_{n}\sim {\frac {4^{n}}{n^{\frac {3}{2}}{\sqrt {\pi }}}}\,,$ in the sense that the quotient of the nth Catalan number and the expression on the right tends towards 1 as n approaches infinity.

This can be proved by using the asymptotic growth of the central binomial coefficients, by Stirling's approximation for *n*!, or via generating functions.

The only Catalan numbers *C**n* that are odd are those for which *n* = 2*k* − 1; all others are even. The only prime Catalan numbers are *C*2 = 2 and *C*3 = 5. More generally, the multiplicity with which a prime p divides *C**n* can be determined by first expressing *n* + 1 in base p. For *p* = 2, the multiplicity is the number of 1 bits, minus 1. For p an odd prime, count all digits greater than ⁠*p* + 1/2⁠; also count digits equal to ⁠*p* + 1/2⁠ unless final; and count digits equal to ⁠*p* − 1/2⁠ if not final and the next digit is counted. The only known odd Catalan numbers that do not have last digit 5 are *C*0 = 1, *C*1 = 1, *C*7 = 429, *C*31, *C*127 and *C*255. The odd Catalan numbers, *C**n* for *n* = 2*k* − 1, do not have last digit 5 if *n* + 1 has a base 5 representation containing 0, 1 and 2 only, except in the least significant place, which could also be a 3.

The Catalan numbers have the integral representations

$C_{n}={\frac {1}{2\pi }}\int _{0}^{4}x^{n}{\sqrt {\frac {4-x}{x}}}\,dx\,={\frac {2}{\pi }}4^{n}\int _{-1}^{1}t^{2n}{\sqrt {1-t^{2}}}\,dt.$ which immediately yields $\sum _{n=0}^{\infty }{\frac {C_{n}}{4^{n}}}=2.$

This has a simple probabilistic interpretation. Consider a random walk on the integer line, starting at 0. Let −1 be a "trap" state, such that if the walker arrives at −1, it will remain there. The walker can arrive at the trap state at times 1, 3, 5, 7,… and the number of ways the walker can arrive at the trap state at time 2*k* + 1 is *C**k*. Since the one-dimensional random walk is recurrent, the probability that the walker eventually arrives at −1 is $\sum _{n=0}^{\infty }{\frac {C_{n}}{2^{2n+1}}}=1.$

## Applications in combinatorics

There are many counting problems in combinatorics whose solution is given by the Catalan numbers. The book *Enumerative Combinatorics: Volume 2* by combinatorialist Richard P. Stanley contains a set of exercises which describe 66 different interpretations of the Catalan numbers. Following are some examples, with illustrations of the cases *C*3 = 5 and *C*4 = 14.

- *C**n* is the number of Dyck words of length 2*n*. A Dyck word is a string consisting of n X's and n Y's such that no initial segment of the string has more Y's than X's. For example, the following are the Dyck words up to length 6:

- XY
- XXYYXYXY
- XXXYYYXYXXYYXYXYXYXXYYXYXXYXYY

- Re-interpreting the symbol X as an opening parenthesis and Y as a closing parenthesis, *C**n* counts the number of expressions containing n pairs of parentheses which are correctly matched. For instance, for *n* = 3 these are

- ((()))
- (()())
- (())()
- ()(())
- ()()()

- *C**n* is the number of different ways *n* + 1 factors can be completely parenthesized, i.e. the number of ways of associating n applications of a binary operator (as in the matrix chain multiplication problem). For *n* = 3, for example, we have the following five different complete parenthesizations of four factors:

- ((ab)c)d
- (a(bc))d
- (ab)(cd)
- a((bc)d)
- a(b(cd))

- Successive applications of a binary operator can be represented in terms of a full binary tree, by labeling each leaf *a*, *b*, *c*, *d*. It follows that *C**n* is the number of full binary trees with *n* + 1 leaves, or, equivalently, with a total of n internal nodes:

- *C**n* is the number of non-isomorphic ordered (or plane) trees with *n* + 1 vertices. See encoding ordered trees as binary trees. For example, *C**n* is the number of possible parse trees for a sentence (assuming binary branching), in natural language processing.
- *C**n* is the number of monotonic lattice paths along the edges of a grid with *n* × *n* square cells, which do not pass above the diagonal. A monotonic path is one which starts in the lower left corner, finishes in the upper right corner, and consists entirely of edges pointing rightwards or upwards. Counting such paths is equivalent to counting Dyck words: X stands for "move right" and Y stands for "move up".

The following diagrams show the case

n

= 4

:

This can be represented by listing the Catalan elements by column height:

- [0,0,0,0][0,0,0,1][0,0,0,2][0,0,1,1]
- [0,1,1,1][0,0,1,2][0,0,0,3][0,1,1,2][0,0,2,2][0,0,1,3]
- [0,0,2,3][0,1,1,3][0,1,2,2][0,1,2,3]

- A convex polygon with *n* + 2 sides can be cut into triangles by connecting vertices with non-crossing line segments (a form of polygon triangulation). The number of triangles formed is n and the number of different ways that this can be achieved is *C**n*. The following hexagons illustrate the case *n* = 4:

- *C**n* is the number of stack-sortable permutations of {1, ..., *n*}. A permutation w is called stack-sortable if *S*(*w*) = (1, ..., *n*), where *S*(*w*) is defined recursively as follows: write *w* = *unv* where n is the largest element in w and u and v are shorter sequences, and set *S*(*w*) = *S*(*u*)*S*(*v*)*n*, with S being the identity for one-element sequences.
- *C**n* is the number of permutations of {1, ..., *n*} that avoid the permutation pattern 123 (or, alternatively, any of the other patterns of length 3); that is, the number of permutations with no three-term increasing subsequence. For *n* = 3, these permutations are 132, 213, 231, 312 and 321. For *n* = 4, they are 1432, 2143, 2413, 2431, 3142, 3214, 3241, 3412, 3421, 4132, 4213, 4231, 4312 and 4321.
- *C**n* is the number of noncrossing partitions of the set {1, ..., *n*}. *A fortiori*, *C**n* never exceeds the n-th Bell number. *C**n* is also the number of noncrossing partitions of the set {1, ..., 2*n*} in which every block is of size 2.
- *C**n* is the number of ways to tile a stairstep shape of height n with n rectangles. Cutting across the anti-diagonal and looking at only the edges gives full binary trees. The following figure illustrates the case *n* = 4:

- *C**n* is the number of ways to form a "mountain range" with n upstrokes and n downstrokes that all stay above a horizontal line. The mountain range interpretation is that the mountains will never go below the horizon.

| $n=0:$ | * | 1 way |
|---|---|---|
| $n=1:$ | /\ | 1 way |
| $n=2:$ | 0000000/\ /\/\,0/00\ | 2 ways |
| $n=3:$ | 0000000000000000000000000000000000/\ 00000000000/\0000/\000000/\/\0000/00\ /\/\/\,0/\/00\,0/00\/\,0/0000\,0/0000\ | 5 ways |

- *C**n* is the number of standard Young tableaux whose diagram is a 2-by-n rectangle. In other words, it is the number of ways the numbers 1, 2, ..., 2*n* can be arranged in a 2-by-n rectangle so that each row and each column is increasing. As such, the formula can be derived as a special case of the hook-length formula.

```
123   124   125   134   135
456   356   346   256   246
```

- *C**n* is the number of length n sequences that start with 1, and can increase by either 0 or 1, or decrease by any number (to at least 1). For *n* = 4 these are 1234, 1233, 1232, 1231, 1223, 1222, 1221, 1212, 1211, 1123, 1122, 1121, 1112, 1111. From a Dyck path, start a counter at 0. An X increases the counter by 1 and a Y decreases it by 1. Record the values at only the X's. Compared to the similar representation of the Bell numbers, only 1213 is missing.

## Proof of the formula

There are several ways of explaining why the formula $C_{n}={\frac {1}{n+1}}{2n \choose n}$ solves the combinatorial problems listed above. The first proof below uses a generating function. The other proofs are examples of bijective proofs; they involve literally counting a collection of some kind of object to arrive at the correct formula.

### First proof

We first observe that all of the combinatorial problems listed above satisfy Segner's recurrence relation

$C_{0}=1\quad {\text{and}}\quad C_{n+1}=\sum _{i=0}^{n}C_{i}\,C_{n-i}\quad {\text{for }}n\geq 0\,.$

For example, every Dyck word w of length 2 or more can be written in a unique way in the form

w

= X

w

1

Y

w

2

with (possibly empty) Dyck words *w*1 and *w*2.

The generating function for the Catalan numbers is defined by

$c(x)=\sum _{n=0}^{\infty }C_{n}x^{n}\,.$

The recurrence relation given above can then be summarized in generating function form by the relation

$c(x)=1+xc(x)^{2}\,;$

in other words, this equation follows from the recurrence relation by expanding both sides into power series. On the one hand, the recurrence relation uniquely determines the Catalan numbers; on the other hand, interpreting *xc*2 − *c* + 1 = 0 as a quadratic equation of c and using the quadratic formula, the generating function relation can be algebraically solved to yield two solution possibilities

$c(x)={\begin{cases}{\dfrac {1+{\sqrt {1-4x}}}{2x}}\\[4px]{\dfrac {1-{\sqrt {1-4x}}}{2x}}\end{cases}}\,.$

From the two possibilities, the second must be chosen because only the second gives

$C_{0}=\lim _{x\to 0}c(x)=1\,.$

The square root term can be expanded as a power series using the binomial series

${\begin{aligned}1-{\sqrt {1-4x}}&=-\sum _{n=1}^{\infty }{\binom {\frac {1}{2}}{n}}(-4x)^{n}=-\sum _{n=1}^{\infty }{\frac {(-1)^{n-1}(2n-3)!!}{2^{n}n!}}(-4x)^{n}\\[6px]&=-\sum _{n=0}^{\infty }{\frac {(-1)^{n}(2n-1)!!}{2^{n+1}(n+1)!}}(-4x)^{n+1}=\sum _{n=0}^{\infty }{\frac {2^{n+1}(2n-1)!!}{(n+1)!}}x^{n+1}\\[6px]&=\sum _{n=0}^{\infty }{\frac {2(2n)!}{(n+1)!n!}}x^{n+1}=\sum _{n=0}^{\infty }{\frac {2}{n+1}}{\binom {2n}{n}}x^{n+1}\,.\end{aligned}}$ Thus, $c(x)={\frac {1-{\sqrt {1-4x}}}{2x}}=\sum _{n=0}^{\infty }{\frac {1}{n+1}}{\binom {2n}{n}}x^{n}\,.$

### Second proof

Call a bad path one that starts at (*x*, *y*) = (0, 0), ends at (*n*, *n*), is monotonic, and contains a point above the line *y* = *x*. We count the number of bad paths by establishing a bijection with paths that start at (0, 0), end at (*n* − 1, *n* + 1), and are monotonic.

For a given bad path, construct a reflected path as follows. Let P be the first point on the bad path intersecting the line *y* = *x* + 1. The bad path from (0, 0) to P is the beginning of the reflected path. The part of the bad path from P to (*n*, *n*) reflected across the line *y* = *x* + 1 is the rest of the reflected path. See the illustration for an example. The black line is the points shared between the two paths, the dotted red line is the rest of the bad path, the solid red line is the rest of the reflected path.

This is a bijection because every monotonic path from (0, 0) to (*n* − 1, *n* + 1) is constructable from a bad path, and every reflected path is uniquely invertible by finding the unique point P, which must exist because every such path must intersect *y* = *x* + 1.

The number of steps in the reflected path is (*n* − 1) + (*n* + 1) = 2*n*. The number of upward steps is *n* + 1 because the path is monotonic and starts at *y* = 0 and ends at *y* = *n* + 1.

The number of reflected paths can be counted in the usual way, by counting how many way upward steps may be distributed among total steps, which is ${\textstyle {\binom {2n}{n+1}}}$ , and the number of Catalan paths (good paths) is obtained by removing the number of bad paths from the total number of monotonic paths of the original grid,

$C_{n}={\binom {2n}{n}}-{\binom {2n}{n+1}}={\binom {2n}{n}}-{\frac {n}{n+1}}{\binom {2n}{n}}={\frac {1}{n+1}}{\binom {2n}{n}}.$

This proof can be restated in terms of Dyck words. We start with a (non-Dyck) sequence of n Xs and n Ys and interchange all Xs and Ys after the first Y that violates the Dyck condition.

### Third proof

This bijective proof provides a natural explanation for the term *n* + 1 appearing in the denominator of the formula for *C**n*. A generalized version of this proof can be found in a paper of Rukavicka (2011).

Given a monotonic path, the **exceedance** of the path is defined to be the number of **vertical** edges above the diagonal. For example, in Figure 2, the edges above the diagonal are marked in red, so the exceedance of this path is 5.

Given a monotonic path whose exceedance is not zero, we apply the following algorithm to construct a new path whose exceedance is 1 less than the one we started with.

- Starting from the bottom left, follow the path until it first travels above the diagonal.
- Continue to follow the path until it *touches* the diagonal again. Denote by X the first such edge that is reached.
- Swap the portion of the path occurring before X with the portion occurring after X.

In Figure 3, the black dot indicates the point where the path first crosses the diagonal. The black edge is X, and we place the last lattice point of the red portion in the top-right corner, and the first lattice point of the green portion in the bottom-left corner, and place X accordingly, to make a new path, shown in the second diagram.

The exceedance has dropped from 3 to 2. In fact, the algorithm causes the exceedance to decrease by 1 for any path that we feed it, because the first vertical step starting on the diagonal (at the point marked with a black dot) is the only vertical edge that changes from being above the diagonal to being below it when we apply the algorithm – all the other vertical edges stay on the same side of the diagonal.

It can be seen that this process is *reversible*: given any path P whose exceedance is less than n, there is exactly one path which yields P when the algorithm is applied to it. Indeed, the (black) edge X, which originally was the first horizontal step ending on the diagonal, has become the *last* horizontal step *starting* on the diagonal. Alternatively, reverse the original algorithm to look for the first edge that passes *below* the diagonal.

This implies that the number of paths of exceedance n is equal to the number of paths of exceedance *n* − 1, which is equal to the number of paths of exceedance *n* − 2, and so on, down to zero. In other words, we have split up the set of *all* monotonic paths into *n* + 1 equally sized classes, corresponding to the possible exceedances between 0 and n. Since there are ${\textstyle {\binom {2n}{n}}}$ monotonic paths, we obtain the desired formula $C_{n}={\frac {1}{n+1}}{\binom {2n}{n}}.$

Figure 4 illustrates the situation for *n* = 3. Each of the 20 possible monotonic paths appears somewhere in the table. The first column shows all paths of exceedance three, which lie entirely above the diagonal. The columns to the right show the result of successive applications of the algorithm, with the exceedance decreasing one unit at a time. There are five rows, that is *C*3 = 5, and the last column displays all paths no higher than the diagonal.

Using Dyck words, start with a sequence from ${\textstyle {\binom {2n}{n}}}$ . Let *X**d* be the first X that brings an initial subsequence to equality, and configure the sequence as (*F*)*Xd*(*L*). The new sequence is LXF.

### Fourth proof

This proof uses the triangulation definition of Catalan numbers to establish a relation between *C**n* and *C**n*+1.

Given a polygon P with *n* + 2 sides and a triangulation, mark one of its sides as the base, and also orient one of its 2*n* + 1 total edges. There are (4*n* + 2)*C**n* such marked triangulations for a given base.

Given a polygon Q with *n* + 3 sides and a (different) triangulation, again mark one of its sides as the base. Mark one of the sides other than the base side (and not an inner triangle edge). There are (*n* + 2)*C**n* + 1 such marked triangulations for a given base.

There is a simple bijection between these two marked triangulations: We can either collapse the triangle in Q whose side is marked (in two ways, and subtract the two that cannot collapse the base), or, in reverse, expand the oriented edge in P to a triangle and mark its new side.

Thus $(4n+2)C_{n}=(n+2)C_{n+1}\,.$

Write ${\frac {4n-2}{n+1}}C_{n-1}=C_{n}\,.$

Because

$(2n)!=(2n)!!(2n-1)!!=2^{n}n!(2n-1)!!\,,$

we have

${\frac {(2n)!}{n!}}=2^{n}(2n-1)!!=(4n-2)!!!!\,.$

Applying the recursion with *C*0 = 1 gives the result.

### Fifth proof

This proof is based on the Dyck words interpretation of the Catalan numbers, so Cn is the number of ways to correctly match n pairs of brackets. We denote a (possibly empty) correct string with c and its inverse with c′. Since any c can be uniquely decomposed into *c* = (*c*1)*c*2, summing over the possible lengths of *c*1 immediately gives the recursive definition $C_{0}=1\quad {\text{and}}\quad C_{n+1}=\sum _{i=0}^{n}C_{i}\,C_{n-i}\quad {\text{for }}n\geq 0$ .

Let b be a balanced string of length 2*n*, i.e. b contains an equal number of ( and ), so *Bn* = ${\textstyle {\binom {2n}{n}}}$ . A balanced string can also be uniquely decomposed into either (*c*)*b* or )*c′*(*b*, so

$B_{n+1}=2\sum _{i=0}^{n}B_{i}C_{n-i}\,.$

Any incorrect (non-Catalan) balanced string starts with *c*), and the remaining string has one more ( than ), so $B_{n+1}-C_{n+1}=\sum _{i=0}^{n}{\binom {2i+1}{i}}C_{n-i}$

Also, from the definitions, we have:

$B_{n+1}-C_{n+1}=2\sum _{i=0}^{n}B_{i}C_{n-i}-\sum _{i=0}^{n}C_{i}\,C_{n-i}=\sum _{i=0}^{n}(2B_{i}-C_{i})C_{n-i}\,.$

Therefore, as this is true for all n,

${\begin{aligned}2B_{i}-C_{i}&={\binom {2i+1}{i}}\\[6px]C_{i}&=2B_{i}-{\binom {2i+1}{i}}\\[6px]&=2{\binom {2i}{i}}-{\binom {2i+1}{i}}\\[6px]&={\frac {1}{i+1}}{\binom {2i}{i}}\,.\end{aligned}}$

### Sixth proof

This proof is based on the Dyck words interpretation of the Catalan numbers and uses the cycle lemma of Dvoretzky and Motzkin.

We call a sequence of Xs and Ys *dominating* if, reading from left to right, the number of Xs is always strictly greater than the number of Ys. The cycle lemma states that any sequence of m Xs and n Ys, where *m* > *n*, has precisely *m* − *n* dominating circular shifts. To see this, arrange the given sequence of *m* + *n* Xs and Ys in a circle. Repeatedly removing XY pairs leaves exactly *m* − *n* Xs. Each of these Xs was the start of a dominating circular shift before anything was removed. For example, consider XXYXY. This sequence is dominating, but none of its circular shifts XYXYX, YXYXX, XYXXY and YXXYX are.

A string is a Dyck word of n Xs and n Ys if and only if prepending an X to the Dyck word gives a dominating sequence with *n* + 1 Xs and n Ys, so we can count the former by instead counting the latter. In particular, when *m* = *n* + 1, there is exactly one dominating circular shift. There are ${\textstyle {\binom {2n+1}{n}}}$ sequences with exactly *n* + 1 Xs and n Ys. For each of these, only one of the 2*n* + 1 circular shifts is dominating. Therefore there are ${\textstyle {\frac {1}{2n+1}}{\binom {2n+1}{n}}}$ = *Cn* distinct sequences of *n* + 1 Xs and n Ys that are dominating, each of which corresponds to exactly one Dyck word.

## Hankel matrix

The *n* × *n* Hankel matrix whose (*i*, *j*) entry is the Catalan number *C**i*+*j*−2 has determinant 1, regardless of the value of n. For example, for *n* = 4 we have $\det {\begin{bmatrix}1&1&2&5\\1&2&5&14\\2&5&14&42\\5&14&42&132\end{bmatrix}}=1.$

Moreover, if the indexing is "shifted" so that the (*i*, *j*) entry is filled with the Catalan number *C**i*+*j*−1 then the determinant is still 1, regardless of the value of n. For example, for *n* = 4 we have $\det {\begin{bmatrix}1&2&5&14\\2&5&14&42\\5&14&42&132\\14&42&132&429\end{bmatrix}}=1.$

Taken together, these two conditions uniquely define the Catalan numbers.

Another feature unique to the Catalan–Hankel matrix is that the *n* × *n* submatrix starting at 2 has determinant *n* + 1.

$\det {\begin{bmatrix}2\end{bmatrix}}=2$

$\det {\begin{bmatrix}2&5\\5&14\end{bmatrix}}=3$

$\det {\begin{bmatrix}2&5&14\\5&14&42\\14&42&132\end{bmatrix}}=4$

$\det {\begin{bmatrix}2&5&14&42\\5&14&42&132\\14&42&132&429\\42&132&429&1430\end{bmatrix}}=5$

et cetera.

## History

The Catalan sequence was described in 1751 by Leonhard Euler, who was interested in the number of different ways of dividing a polygon into triangles. The sequence is named after Eugène Charles Catalan, who discovered the connection to parenthesized expressions during his exploration of the Towers of Hanoi puzzle. The reflection counting trick (second proof) for Dyck words was found by Désiré André in 1887.

The name “Catalan numbers” originated from John Riordan.

In 1988, it came to light that the Catalan number sequence had been used in China by the Mongolian mathematician Mingantu by 1730, when he started to write his book *Ge Yuan Mi Lu Jie Fa* *[The Quick Method for Obtaining the Precise Ratio of Division of a Circle]*, which was completed by his student Chen Jixin in 1774 but published sixty years later. Peter J. Larcombe (1999) sketched some of the features of the work of Mingantu, including the stimulus of Pierre Jartoux, who brought three infinite series to China early in the 1700s.

For instance, Mingantu used the Catalan sequence to express series expansions of $\sin(2\alpha )$ and $\sin(4\alpha )$ in terms of $\sin(\alpha )$ .

## Generalizations

The Catalan numbers can be interpreted as a special case of the Bertrand's ballot theorem. Specifically, $C_{n}$ is the number of ways for a candidate A with *n* + 1 votes to lead candidate B with n votes.

The two-parameter sequence of non-negative integers ${\frac {(2m)!(2n)!}{(m+n)!m!n!}}$ is a generalization of the Catalan numbers. These are named **super-Catalan numbers**, per Ira Gessel. These should not confused with the Schröder–Hipparchus numbers, which sometimes are also called super-Catalan numbers.

For $m=1$ , this is just two times the ordinary Catalan numbers, and for $m=n$ , the numbers have an easy combinatorial description. However, other combinatorial descriptions are only known for $m=2,3$ and 4 , and it is an open problem to find a general combinatorial interpretation.

Sergey Fomin and Nathan Reading have given a generalized Catalan number associated to any finite crystallographic Coxeter group, namely the number of fully commutative elements of the group; in terms of the associated root system, it is the number of anti-chains (or order ideals) in the poset of positive roots. The classical Catalan number $C_{n}$ corresponds to the root system of type $A_{n}$ . The classical recurrence relation generalizes: the Catalan number of a Coxeter diagram is equal to the sum of the Catalan numbers of all its maximal proper sub-diagrams.

The Catalan numbers are a solution of a version of the Hausdorff moment problem.

For coprime positive integers r and s, the *rational Catalan numbers* ${\frac {1}{r+s}}{\binom {r+s}{r}}$ count the number of lattice paths with steps of unit length rightwards and upwards from (0,0) to (*r*,*s*) that never go above the line *ry* = *sx*.

## Catalan k-fold convolution

The Catalan k-fold convolution is:

$\sum _{i_{1}+\cdots +i_{k}=n \atop i_{1},\ldots ,i_{k}\geq 0}C_{i_{1}}\cdots C_{i_{k}}={\dfrac {k}{2n+k}}{\binom {2n+k}{n}}$
