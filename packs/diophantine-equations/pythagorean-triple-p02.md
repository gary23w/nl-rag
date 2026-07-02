---
title: "Pythagorean triple (part 2/2)"
source: https://en.wikipedia.org/wiki/Pythagorean_triple
domain: diophantine-equations
license: CC-BY-SA-4.0
tags: diophantine equation, pell's equation, fermat's last theorem, pythagorean triple
fetched: 2026-07-02
part: 2/2
---

## Generalizations

There are several ways to generalize the concept of Pythagorean triples.

### Pythagorean n-tuple

The expression $\left(m_{1}^{2}-m_{2}^{2}-\ldots -m_{n}^{2}\right)^{2}+\sum _{k=2}^{n}(2m_{1}m_{k})^{2}=\left(m_{1}^{2}+\ldots +m_{n}^{2}\right)^{2}$ is a Pythagorean n-tuple for any tuple of positive integers (*m*1, ..., *m**n*) with *m*2 1 > *m*2 2 + ... + *m*2 *n*. The Pythagorean n-tuple can be made primitive by dividing out by the largest common divisor of its values.

Furthermore, any primitive Pythagorean n-tuple *a*2 1 + ... + *a*2 *n* = *c*2 can be found by this approach. Use (*m*1, ..., *m**n*) = (*c* + *a*1, *a*2, ..., *a**n*) to get a Pythagorean n-tuple by the above formula and divide out by the largest common integer divisor, which is 2*m*1 = 2(*c* + *a*1). Dividing out by the largest common divisor of these (*m*1, ..., *m**n*) values gives the same primitive Pythagorean n-tuple; and there is a one-to-one correspondence between tuples of setwise coprime positive integers (*m*1, ..., *m**n*) satisfying *m*2 1 > *m*2 2 + ... + *m*2 *n* and primitive Pythagorean n-tuples.

Examples of the relationship between setwise coprime values ${\vec {m}}$ and primitive Pythagorean n-tuples include:

${\begin{aligned}{\vec {m}}=(1)&\leftrightarrow 1^{2}=1^{2}\\{\vec {m}}=(2,1)&\leftrightarrow 3^{2}+4^{2}=5^{2}\\{\vec {m}}=(2,1,1)&\leftrightarrow 1^{2}+2^{2}+2^{2}=3^{2}\\{\vec {m}}=(3,1,1,1)&\leftrightarrow 1^{2}+1^{2}+1^{2}+1^{2}=2^{2}\\{\vec {m}}=(5,1,1,2,3)&\leftrightarrow 1^{2}+1^{2}+1^{2}+2^{2}+3^{2}=4^{2}\\{\vec {m}}=(4,1,1,1,1,2)&\leftrightarrow 1^{2}+1^{2}+1^{2}+1^{2}+1^{2}+2^{2}=3^{2}\\{\vec {m}}=(5,1,1,1,2,2,2)&\leftrightarrow 1^{2}+1^{2}+1^{2}+1^{2}+2^{2}+2^{2}+2^{2}=4^{2}\end{aligned}}$

#### Consecutive squares

Since the sum *F*(*k*,*m*) of k consecutive squares beginning with *m*2 is given by the formula,

$F(k,m)=km(k-1+m)+{\frac {k(k-1)(2k-1)}{6}}$

one may find values (*k*, *m*) so that *F*(*k*,*m*) is a square, such as one by Hirschhorn where the number of terms is itself a square,

$m={\tfrac {v^{4}-24v^{2}-25}{48}},\;k=v^{2},\;F(m,k)={\tfrac {v^{5}+47v}{48}}$

and *v* ≥ 5 is any integer not divisible by 2 or 3. For the smallest case *v* = 5, hence *k* = 25, this yields the well-known cannonball-stacking problem of Lucas,

$0^{2}+1^{2}+2^{2}+\dots +24^{2}=70^{2}$

a fact which is connected to the Leech lattice.

In addition, if in a Pythagorean n-tuple (*n* ≥ 4) all addends are consecutive except one, one can use the equation,

$F(k,m)+p^{2}=(p+1)^{2}$

Since the second power of p cancels out, this is only linear and easily solved for as $p={\tfrac {F(k,m)-1}{2}}$ though k, m should be chosen so that p is an integer, with a small example being *k* = 5, *m* = 1 yielding,

$1^{2}+2^{2}+3^{2}+4^{2}+5^{2}+27^{2}=28^{2}$

Thus, one way of generating Pythagorean n-tuples is by using, for various x,

$x^{2}+(x+1)^{2}+\cdots +(x+q)^{2}+p^{2}=(p+1)^{2},$

where *q = n*–2 and where

$p={\frac {(q+1)x^{2}+q(q+1)x+{\frac {q(q+1)(2q+1)}{6}}-1}{2}}.$

### Fermat's Last Theorem

A generalization of the concept of Pythagorean triples is the search for triples of positive integers a, b, and c, such that *a**n* + *b**n* = *c**n*, for some n strictly greater than 2. Pierre de Fermat in 1637 claimed that no such triple exists, a claim that came to be known as Fermat's Last Theorem because it took longer than any other conjecture by Fermat to be proved or disproved. The first proof was given by Andrew Wiles in 1994.

### *n* − 1 or n nth powers summing to an nth power

Another generalization is searching for sequences of *n* + 1 positive integers for which the nth power of the last is the sum of the nth powers of the previous terms. The smallest sequences for known values of n are:

- n = 3: {3, 4, 5; 6}.
- n = 4: {30, 120, 272, 315; 353}
- n = 5: {19, 43, 46, 47, 67; 72}
- n = 7: {127, 258, 266, 413, 430, 439, 525; 568}
- n = 8: {90, 223, 478, 524, 748, 1088, 1190, 1324; 1409}

For the *n* = 3 case, in which $x^{3}+y^{3}+z^{3}=w^{3},$ called the Fermat cubic, a general formula exists giving all solutions.

A slightly different generalization allows the sum of (*k* + 1) nth powers to equal the sum of (*n* − *k*) nth powers. For example:

- (*n* = 3): 13 + 123 = 93 + 103, made famous by Hardy's recollection of a conversation with Ramanujan about the number 1729 being the smallest number that can be expressed as a sum of two cubes in two distinct ways.

There can also exist *n* − 1 positive integers whose nth powers sum to an nth power (though, by Fermat's Last Theorem, not for *n* = 3); these are counterexamples to Euler's sum of powers conjecture. The smallest known counterexamples are

- *n* = 4: (95800, 217519, 414560; 422481)
- *n* = 5: (27, 84, 110, 133; 144)

### Heronian triangle triples

A **Heronian triangle** is commonly defined as one with integer sides whose area is also an integer. The lengths of the sides of such a triangle form a **Heronian triple** (*a, b, c*) for *a* ≤ *b* ≤ *c*. Every Pythagorean triple is a Heronian triple, because at least one of the legs a, b must be even in a Pythagorean triple, so the area *ab*/2 is an integer. Not every Heronian triple is a Pythagorean triple, however, as the example (4, 13, 15) with area 24 shows.

If (*a*, *b*, *c*) is a Heronian triple, so is (*ka*, *kb*, *kc*) where k is any positive integer; its area will be the integer that is *k*2 times the integer area of the (*a*, *b*, *c*) triangle. The Heronian triple (*a*, *b*, *c*) is **primitive** provided *a*, *b*, *c* are setwise coprime. (With primitive Pythagorean triples the stronger statement that they are *pairwise* coprime also applies, but with primitive Heronian triangles the stronger statement does not always hold true, such as with (7, 15, 20).) Here are a few of the simplest primitive Heronian triples that are not Pythagorean triples:

(4, 13, 15) with area 24

(3, 25, 26) with area 36

(7, 15, 20) with area 42

(6, 25, 29) with area 60

(11, 13, 20) with area 66

(13, 14, 15) with area 84

(13, 20, 21) with area 126

By Heron's formula, the extra condition for a triple of positive integers (*a*, *b*, *c*) with *a* < *b* < *c* to be Heronian is that

(

a

2

+

b

2

+

c

2

)

2

− 2(

a

4

+

b

4

+

c

4

)

or equivalently

2(

a

2

b

2

+

a

2

c

2

+

b

2

c

2

) − (

a

4

+

b

4

+

c

4

)

be a nonzero perfect square divisible by 16.

### Application to cryptography

Primitive Pythagorean triples have been used in cryptography as random sequences and for the generation of keys.
