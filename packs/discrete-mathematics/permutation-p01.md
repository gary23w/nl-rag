---
title: "Permutation (part 1/2)"
source: https://en.wikipedia.org/wiki/Permutation
domain: discrete-mathematics
license: CC-BY-SA-4.0
tags: discrete math, discrete mathematics, combinatorics, graph theory, set theory, permutation
fetched: 2026-07-02
part: 1/2
---

# Permutation

In mathematics, a **permutation** of a set can mean one of two different things:

- an arrangement of its members in a sequence or linear order, or
- the act or process of changing the linear order of an ordered set.

An example of the first meaning is the six permutations (orderings) of the set {1, 2, 3}: written as tuples, they are (1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), and (3, 2, 1). Anagrams of a word whose letters are all different are also permutations: the letters are already ordered in the original word, and the anagram reorders them. The study of permutations of finite sets is an important topic in combinatorics and group theory.

Permutations are used in almost every branch of mathematics and in many other fields of science. In computer science, they are used for analyzing sorting algorithms; in quantum physics, for describing states of particles; and in biology, for describing RNA sequences.

The number of permutations of *n* distinct objects is *n* factorial, usually written as *n*!, which means the product of all positive integers less than or equal to *n*.

According to the second meaning, a permutation of a set *S* is defined as a bijection from *S* to itself. That is, it is a function from *S* to *S* for which every element occurs exactly once as an image value. Such a function $\sigma :S\to S$ is equivalent to the rearrangement of the elements of *S* in which each element *i* is replaced by the corresponding $\sigma (i)$ . For example, the permutation (3, 1, 2) corresponds to the function $\sigma$ defined as $\sigma (1)=3,\quad \sigma (2)=1,\quad \sigma (3)=2.$ The collection of all permutations of a set form a group called the symmetric group of the set. The group operation is the composition of functions (performing one rearrangement after the other), which results in another function (rearrangement).

In elementary combinatorics, the ***k*-permutations**, or partial permutations, are the ordered arrangements of *k* distinct elements selected from a set. When *k* is equal to the size of the set, these are the permutations in the previous sense.


## History

Permutation-like objects called hexagrams were used in China in the I Ching (Pinyin: Yi Jing) as early as 1000 BC.

In Greece, Plutarch wrote that Xenocrates of Chalcedon (396–314 BC) discovered the number of different syllables possible in the Greek language. This would have been the first attempt on record to solve a difficult problem in permutations and combinations.

Al-Khalil (717–786), an Arab mathematician and cryptographer, wrote the *Book of Cryptographic Messages*. It contains the first use of permutations and combinations, to list all possible Arabic words with and without vowels.

The rule to determine the number of permutations of *n* objects was known in Indian culture around 1150 AD. The *Lilavati* by the Indian mathematician Bhāskara II contains a passage that translates as follows:

> The product of multiplication of the arithmetical series beginning and increasing by unity and continued to the number of places, will be the variations of number with specific figures.

In 1677, Fabian Stedman described factorials when explaining the number of permutations of bells in change ringing. Starting from two bells: "first, *two* must be admitted to be varied in two ways", which he illustrates by showing 1 2 and 2 1. He then explains that with three bells there are "three times two figures to be produced out of three" which again is illustrated. His explanation involves "cast away 3, and 1.2 will remain; cast away 2, and 1.3 will remain; cast away 1, and 2.3 will remain". He then moves on to four bells and repeats the casting away argument showing that there will be four different sets of three. Effectively, this is a recursive process. He continues with five bells using the "casting away" method and tabulates the resulting 120 combinations. At this point he gives up and remarks:

> Now the nature of these methods is such, that the changes on one number comprehends the changes on all lesser numbers, ... insomuch that a compleat Peal of changes on one number seemeth to be formed by uniting of the compleat Peals on all lesser numbers into one entire body;

Stedman widens the consideration of permutations; he goes on to consider the number of permutations of the letters of the alphabet and of horses from a stable of 20.

A first case in which seemingly unrelated mathematical questions were studied with the help of permutations occurred around 1770, when Joseph Louis Lagrange, in the study of polynomial equations, observed that properties of the permutations of the roots of an equation are related to the possibilities to solve it. This line of work ultimately resulted, through the work of Évariste Galois, in Galois theory, which gives a complete description of what is possible and impossible with respect to solving polynomial equations (in one unknown) by radicals. In modern mathematics, there are many similar situations in which understanding a problem requires studying certain permutations related to it.

The study of permutations as substitutions on n elements led to the notion of group as algebraic structure, through the works of Cauchy (1815 memoir).

Permutations played an important role in the cryptanalysis of the Enigma machine, a cipher device used by Nazi Germany during World War II. In particular, one important property of permutations, namely, that two permutations are conjugate exactly when they have the same cycle type, was used by cryptologist Marian Rejewski to break the German Enigma cipher in turn of years 1932–1933.


## Definition

In mathematics texts it is customary to denote permutations using lowercase Greek letters.

A permutation can be defined as a bijection (an invertible mapping, a one-to-one and onto function) from a set *S* to itself: $\sigma :S\ {\stackrel {\sim }{\longrightarrow }}\ S.$ The identity permutation is defined by $\sigma (x)=x$ for all elements $x\in S$ , and can be denoted by the number 1 , by ${\text{id}}={\text{id}}_{S}$ , or by a single 1-cycle (x).

The set of all permutations of a set with *n* elements forms the symmetric group $S_{n}$ , where the group operation is composition of functions. Thus for two permutations $\sigma$ and $\tau$ in the group $S_{n}$ , their product $\pi =\sigma \tau$ is defined by $\pi (i)=\sigma (\tau (i)).$ Composition is usually written without a dot or other sign. In general, composition of two permutations is not commutative; that is, typically the permutations $\tau \sigma$ and $\sigma \tau$ are not equal.

As a bijection from a set to itself, a permutation is a function that *performs* a rearrangement of a set, termed an *active permutation* or *substitution*. An older viewpoint sees a permutation as an ordered arrangement or list of all the elements of *S*, called a *passive permutation*. According to this definition, all permutations in § One-line notation are passive. This meaning is subtly distinct from how passive (i.e. *alias*) is used in Active and passive transformation and elsewhere, which would consider all permutations open to passive interpretation (regardless of whether they are in one-line notation, two-line notation, etc.).

A permutation $\sigma$ can be decomposed into one or more disjoint *cycles* which are the orbits of the cyclic group $\langle \sigma \rangle =\{1,\sigma ,\sigma ^{2},\ldots \}$ acting on the set *S*. A cycle is found by repeatedly applying the permutation to an element: $x,\sigma (x),\sigma (\sigma (x)),\ldots ,\sigma ^{k-1}(x)$ , where we assume $\sigma ^{k}(x)=x$ . A cycle consisting of *k* elements is called a *k*-cycle. (See § Cycle notation below.)

A fixed point of a permutation $\sigma$ is an element *x* which is taken to itself, that is $\sigma (x)=x$ , forming a 1-cycle $(\,x\,)$ . A permutation with no fixed points is called a derangement. A permutation exchanging two elements (a single 2-cycle) and leaving the others fixed is called a transposition.


## Notations

Several notations are widely used to represent permutations conveniently. The properties of permutations do not depend on the nature of the elements being permuted, only on their number, so one often considers the standard set $\{1,2,\ldots ,n\}$ . *Cycle notation* is a popular choice, as it is compact and shows the permutation's structure clearly. This article will use cycle notation unless otherwise specified.

### Two-line notation

Cauchy's *two-line notation* lists the elements of *S* in the first row, and the image of each element below it in the second row. For example, the permutation of *S* = {1, 2, 3, 4, 5, 6} given by the function

> $\sigma (1)=2,\ \ \sigma (2)=6,\ \ \sigma (3)=5,\ \ \sigma (4)=4,\ \ \sigma (5)=3,\ \ \sigma (6)=1$

can be written as

$\sigma ={\begin{pmatrix}1&2&3&4&5&6\\2&6&5&4&3&1\end{pmatrix}}.$

The elements of *S* may appear in any order in the first row, so this permutation could also be written:

$\sigma ={\begin{pmatrix}2&3&4&5&6&1\\6&5&4&3&1&2\end{pmatrix}}={\begin{pmatrix}6&5&4&3&2&1\\1&3&4&5&6&2\end{pmatrix}}.$

### One-line notation

If there is a "natural" order for the elements of *S*, say $x_{1},x_{2},\ldots ,x_{n}$ , then one uses this for the first row of the two-line notation:

$\sigma ={\begin{pmatrix}x_{1}&x_{2}&x_{3}&\cdots &x_{n}\\\sigma (x_{1})&\sigma (x_{2})&\sigma (x_{3})&\cdots &\sigma (x_{n})\end{pmatrix}}.$

Under this assumption, one may omit the first row and write the permutation in *one-line notation* as

$\sigma =\sigma (x_{1})\;\sigma (x_{2})\;\sigma (x_{3})\;\cdots \;\sigma (x_{n})$

,

that is, as an ordered arrangement of the elements of *S*. Care must be taken to distinguish one-line notation from the cycle notation described below: a common usage is to omit parentheses or other enclosing marks for one-line notation, while using parentheses for cycle notation. The one-line notation is also called the *word representation*.

The example above would then be:

> $\sigma ={\begin{pmatrix}1&2&3&4&5&6\\2&6&5&4&3&1\end{pmatrix}}=265431.$

(It is typical to use commas to separate these entries only if some have two or more digits.)

This compact form is common in elementary combinatorics and computer science. It is especially useful in applications where the permutations are to be compared as larger or smaller using lexicographic order.

### Cycle notation

Cycle notation describes the effect of repeatedly applying the permutation on the elements of the set *S*, with an orbit being called a *cycle*. The permutation is written as a list of cycles; since distinct cycles involve disjoint sets of elements, this is referred to as "decomposition into disjoint cycles".

To write down the permutation $\sigma$ in cycle notation, one proceeds as follows:

1. Write an opening bracket followed by an arbitrary element *x* of S : $(\,x$
2. Trace the orbit of *x*, writing down the values under successive applications of $\sigma$ : $(\,x,\sigma (x),\sigma (\sigma (x)),\ldots$
3. Repeat until the value returns to *x,* and close the parenthesis without repeating *x*: $(\,x\,\sigma (x)\,\sigma (\sigma (x))\,\ldots \,)$
4. Continue with an element *y* of *S* which was not yet written, and repeat the above process: $(\,x\,\sigma (x)\,\sigma (\sigma (x))\,\ldots \,)(\,y\,\ldots \,)$
5. Repeat until all elements of *S* are written in cycles.

Also, it is common to omit 1-cycles, since these can be inferred: for any element *x* in *S* not appearing in any cycle, one implicitly assumes $\sigma (x)=x$ .

Following the convention of omitting 1-cycles, one may interpret an individual cycle as a permutation which fixes all the elements not in the cycle (a cyclic permutation having only one cycle of length greater than 1). Then the list of disjoint cycles can be seen as the composition of these cyclic permutations. For example, the one-line permutation $\sigma =265431$ can be written in cycle notation as: $\sigma =(126)(35)(4)=(126)(35).$ This may be seen as the composition $\sigma =\kappa _{1}\kappa _{2}$ of cyclic permutations $\kappa _{1}=(126)=(126)(3)(4)(5),\quad \kappa _{2}=(35)=(35)(1)(2)(4)(6).$ While permutations in general do not commute, disjoint cycles do; for example: $\sigma =(126)(35)=(35)(126).$ Also, each cycle can be rewritten from a different starting point; for example, $\sigma =(126)(35)=(261)(53).$ Thus one may write the disjoint cycles of a given permutation in many different ways.

A convenient feature of cycle notation is that inverting the permutation is given by reversing the order of the elements in each cycle. For example, $\sigma ^{-1}=\left({\vphantom {A^{2}}}(126)(35)\right)^{-1}=(621)(53).$

### Canonical cycle notation

Any permutation has a particular choice of cycle notation which is useful in many combinatorial contexts, especially Foata's bijection described below. The *canonical cycle notation* is defined by:

- each cycle has its *largest* element listed first;
- the cycles are sorted in *increasing* order of their first element, not omitting 1-cycles.

For example, $(513)(6)(827)(94)$ is a permutation of $S=\{1,2,\ldots ,9\}$ in canonical cycle notation (Miklós Bóna's terminology) . Richard Stanley calls this the *standard representation*, and Martin Aigner uses *standard form*. Sergey Kitaev also uses the "standard form" terminology, but reverses both choices; that is, each cycle lists its minimal element first, and the cycles are sorted in decreasing order of their minimal elements.

### Composition of permutations

There are two ways to denote the composition of two permutations. In the most common notation, $\sigma \cdot \tau$ is the function that maps any element *x* to $\sigma (\tau (x))$ . The rightmost permutation is applied to the argument first, because the argument is written to the right of the function.

A *different* rule for multiplying permutations comes from writing the argument to the left of the function, so that the leftmost permutation acts first. In this notation, the permutation is often written as an exponent, so *σ* acting on *x* is written *x**σ*; then the product is defined by $x^{\sigma \cdot \tau }=(x^{\sigma })^{\tau }$ . This article uses the first definition, where the rightmost permutation is applied first.

The function composition operation satisfies the axioms of a group. It is associative, meaning $(\rho \sigma )\tau =\rho (\sigma \tau )$ , and products of more than two permutations are usually written without parentheses. The composition operation also has an identity element (the identity permutation ${\text{id}}$ ), and each permutation $\sigma$ has an inverse $\sigma ^{-1}$ (its inverse function) with $\sigma ^{-1}\sigma =\sigma \sigma ^{-1}={\text{id}}$ .


## Other uses of the term *permutation*

The concept of a permutation as an ordered arrangement admits several generalizations that have been called *permutations*, especially in older literature.

### *k*-permutations of *n*

In older literature and elementary textbooks, a ***k*-permutation of *n*** (sometimes called a **partial permutation**, **sequence without repetition**, **variation**, or **arrangement**) means an ordered arrangement (list) of a *k*-element subset of an *n*-set. The number of such *k*-permutations (*k*-arrangements) of n is denoted variously by such symbols as $P_{k}^{n}$ , $_{n}P_{k}$ , $^{n}\!P_{k}$ , $P_{n,k}$ , $P(n,k)$ , or $A_{n}^{k}$ , computed by the formula: $P(n,k)=\underbrace {n\cdot (n-1)\cdot (n-2)\cdots (n-k+1)} _{k\ \mathrm {factors} },$

which is 0 when *k* > *n*, and otherwise is equal to ${\frac {n!}{(n-k)!}}.$

The product is well defined without the assumption that n is a non-negative integer, and is of importance outside combinatorics as well; it is known as the Pochhammer symbol $(n)_{k}$ or as the k -th falling factorial power $n^{\underline {k}}$ : $P(n,k)={_{n}}P_{k}=(n)_{k}=n^{\underline {k}}.$

This usage of the term *permutation* is closely associated with the term *combination* to mean a subset: that is, a *k-combination* of a set *S* is a *k-*element (unordered) subset of *S*. Ordering the *k*-combinations of *S* in all possible ways produces the *k*-permutations of *S*. The number of *k*-combinations of an *n*-set, *C*(*n*,*k*), is therefore related to the number of *k*-permutations of *n* by: $C(n,k)={\frac {P(n,k)}{P(k,k)}}={\frac {n^{\underline {k}}}{k!}}={\frac {n!}{(n-k)!\,k!}}.$

These numbers are also known as binomial coefficients, usually denoted ${\tbinom {n}{k}}$ : $C(n,k)={_{n}}C_{k}={\binom {n}{k}}.$

### Permutations with repetition

Ordered arrangements of *k* elements of a set *S*, where repetition is allowed, are called *k*-tuples. They have sometimes been referred to as **permutations with repetition**, although they are not permutations in the usual sense. They are also called words or strings over the alphabet *S*. If the set *S* has *n* elements, the number of *k*-tuples over *S* is $n^{k}.$

### Permutations of multisets

If *M* is a finite multiset, then a **multiset permutation** is an ordered arrangement of elements of *M* in which each element appears a number of times equal exactly to its multiplicity in *M*. An anagram of a word having some repeated letters is an example of a multiset permutation. If the multiplicities of the elements of *M* (taken in some order) are $m_{1}$ , $m_{2}$ , ..., $m_{l}$ and their sum (that is, the size of *M*) is *n*, then the number of multiset permutations of *M* is given by a multinomial coefficient: ${n \choose m_{1},m_{2},\ldots ,m_{l}}={\frac {n!}{m_{1}!\,m_{2}!\,\cdots \,m_{l}!}}={\frac {\left(\sum _{i=1}^{l}{m_{i}}\right)!}{\prod _{i=1}^{l}{m_{i}!}}}.$ For example, the number of distinct anagrams of the word MISSISSIPPI is ${\frac {11!}{1!\,4!\,4!\,2!}}=34650.$

A ***k*-permutation** of a multiset *M* is a sequence of *k* elements of *M* in which each element appears *a number of times less than or equal to* its multiplicity in *M* (an element's *repetition number*). In this case, the number of permutations can be determined with generating functions: it is $k!$ times the coefficient of $x^{k}$ in the product

$\prod _{i=1}^{l}\sum _{j=0}^{m_{i}}{\frac {x^{j}}{j!}}$

.

Continuing the example from above, in the case of the multiset of letters in MISSISSIPPI, the resulting generating function is ${\begin{aligned}&(1+x)\cdot (1+x+x^{2}/2)\cdot (1+x+x^{2}/2+x^{3}/6+x^{4}/24)^{2}=\\&1+4x+{\frac {15}{2!}}x^{2}+{\frac {53}{3!}}x^{3}+{\frac {176}{4!}}x^{4}+{\frac {550}{5!}}x^{5}+{\frac {1610}{6!}}x^{6}+{\frac {4340}{7!}}x^{7}+{\frac {10430}{8!}}x^{8}+{\frac {21420}{9!}}x^{9}+{\frac {34650}{10!}}x^{10}+{\frac {34650}{11!}}x^{11}.\end{aligned}}$ Thus, the number of 11-permutations is 34650 (the same result as above), but we also have the number of *k*-permutations with *k* ranging from 0 to 11.

### Circular permutations

Permutations, when considered as arrangements, are sometimes referred to as *linearly ordered* arrangements. If, however, the objects are arranged in a circular manner this distinguished ordering is weakened: there is no "first element" in the arrangement, as any element can be considered as the start. An arrangement of distinct objects in a circular manner is called a **circular permutation**. These can be formally defined as equivalence classes of ordinary permutations of these objects, for the equivalence relation generated by moving the final element of the linear arrangement to its front.

Two circular permutations are equivalent if one can be rotated into the other. The following four circular permutations on four letters are considered to be the same.

${\begin{matrix}&1&\\4&&3\\&2&\end{matrix}}\qquad {\begin{matrix}&4&\\2&&1\\&3&\end{matrix}}\qquad {\begin{matrix}&2&\\3&&4\\&1&\end{matrix}}\qquad {\begin{matrix}&3&\\1&&2\\&4&\end{matrix}}$

The circular arrangements are to be read counter-clockwise, so the following two are not equivalent since no rotation can bring one to the other.

${\begin{matrix}&1&\\4&&3\\&2&\end{matrix}}\qquad {\begin{matrix}&1&\\3&&4\\&2&\end{matrix}}$

There are (*n* – 1)! circular permutations of a set with *n* elements.


## Properties

The number of permutations of *n* distinct objects is *n*!.

The number of *n*-permutations with *k* disjoint cycles is the signless Stirling number of the first kind, denoted $c(n,k)$ or $[{\begin{smallmatrix}n\\k\end{smallmatrix}}]$ .

### Cycle type

The cycles (including the fixed points) of a permutation $\sigma$ of a set with n elements partition that set; so the lengths of these cycles form an integer partition of n, which is called the **cycle type** (or sometimes **cycle structure** or **cycle shape**) of $\sigma$ . There is a "1" in the cycle type for every fixed point of $\sigma$ , a "2" for every transposition, and so on. The cycle type of $\beta =(1\,2\,5\,)(\,3\,4\,)(6\,8\,)(\,7\,)$ is $(3,2,2,1).$

This may also be written in a more compact form as [112231]. More precisely, the general form is $[1^{\alpha _{1}}2^{\alpha _{2}}\dotsm n^{\alpha _{n}}]$ , where $\alpha _{1},\ldots ,\alpha _{n}$ are the numbers of cycles of respective length. The number of permutations of a given cycle type is

${\frac {n!}{1^{\alpha _{1}}2^{\alpha _{2}}\dotsm n^{\alpha _{n}}\alpha _{1}!\alpha _{2}!\dotsm \alpha _{n}!}}$

.

The number of cycle types of a set with n elements equals the value of the partition function $p(n)$ .

Polya's cycle index polynomial is a generating function which counts permutations by their cycle type.

### Conjugating permutations

In general, composing permutations written in cycle notation follows no easily described pattern – the cycles of the composition can be different from those being composed. However the cycle type is preserved in the special case of conjugating a permutation $\sigma$ by another permutation $\pi$ , which means forming the product $\pi \sigma \pi ^{-1}$ . Here, $\pi \sigma \pi ^{-1}$ is the *conjugate* of $\sigma$ by $\pi$ and its cycle notation can be obtained by taking the cycle notation for $\sigma$ and applying $\pi$ to all the entries in it. It follows that two permutations are conjugate exactly when they have the same cycle type.

### Order of a permutation

The order of a permutation $\sigma$ is the smallest positive integer *m* so that $\sigma ^{m}=\mathrm {id}$ . It is the least common multiple of the lengths of its cycles. For example, the order of $\sigma =(152)(34)$ is ${\text{lcm}}(3,2)=6$ .

### Parity of a permutation

Every permutation of a finite set can be expressed as the product of transpositions. Although many such expressions for a given permutation may exist, either they all contain an even number of transpositions or they all contain an odd number of transpositions. Thus all permutations can be classified as even or odd depending on this number.

This result can be extended so as to assign a *sign*, written $\operatorname {sgn} \sigma$ , to each permutation. $\operatorname {sgn} \sigma =+1$ if $\sigma$ is even and $\operatorname {sgn} \sigma =-1$ if $\sigma$ is odd. Then for two permutations $\sigma$ and $\pi$

$\operatorname {sgn} (\sigma \pi )=\operatorname {sgn} \sigma \cdot \operatorname {sgn} \pi .$

It follows that $\operatorname {sgn} \left(\sigma \sigma ^{-1}\right)=+1.$

The sign of a permutation is equal to the determinant of its permutation matrix (below).

### Matrix representation

A *permutation matrix* is an *n* × *n* matrix that has exactly one entry 1 in each column and in each row, and all other entries are 0. There are several ways to assign a permutation matrix to a permutation of {1, 2, ..., *n*}. One natural approach is to define $L_{\sigma }$ to be the linear transformation of $\mathbb {R} ^{n}$ which permutes the standard basis $\{\mathbf {e} _{1},\ldots ,\mathbf {e} _{n}\}$ by $L_{\sigma }(\mathbf {e} _{j})=\mathbf {e} _{\sigma (j)}$ , and define $M_{\sigma }$ to be its matrix. That is, $M_{\sigma }$ has its *j*th column equal to the n × 1 column vector $\mathbf {e} _{\sigma (j)}$ : its (*i*, *j*) entry is 1 if *i* = *σ*(*j*), and 0 otherwise. Since composition of linear mappings is described by matrix multiplication, it follows that this construction is compatible with composition of permutations: $M_{\sigma }M_{\tau }=M_{\sigma \tau }.$ For example, the one-line permutations $\sigma =213,\ \tau =231$ have product $\sigma \tau =132$ , and the corresponding matrices are: $M_{\sigma }M_{\tau }={\begin{pmatrix}0&1&0\\1&0&0\\0&0&1\end{pmatrix}}{\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}}={\begin{pmatrix}1&0&0\\0&0&1\\0&1&0\end{pmatrix}}=M_{\sigma \tau }.$

It is also common in the literature to find the inverse convention, where a permutation *σ* is associated to the matrix $P_{\sigma }=(M_{\sigma })^{-1}=(M_{\sigma })^{T}$ whose (*i*, *j*) entry is 1 if *j* = *σ*(*i*) and is 0 otherwise. In this convention, permutation matrices multiply in the opposite order from permutations, that is, $P_{\sigma }P_{\tau }=P_{\tau \sigma }$ . In this correspondence, permutation matrices act on the right side of the standard $1\times n$ row vectors $({\bf {e}}_{i})^{T}$ : $({\bf {e}}_{i})^{T}P_{\sigma }=({\bf {e}}_{\sigma (i)})^{T}$ .

The Cayley table on the right shows these matrices for permutations of 3 elements.


## Permutations of totally ordered sets

In some applications, the elements of the set being permuted will be compared with each other. This requires that the set *S* has a total order so that any two elements can be compared. The set {1, 2, ..., *n*} with the usual ≤ relation is the most frequently used set in these applications.

A number of properties of a permutation are directly related to the total ordering of *S,* considering the permutation written in one-line notation as a sequence $\sigma =\sigma (1)\sigma (2)\cdots \sigma (n)$ .

### Ascents, descents, runs, exceedances, records

An *ascent* of a permutation *σ* of *n* is any position *i* < *n* where the following value is bigger than the current one. That is, *i* is an ascent if $\sigma (i)<\sigma (i{+}1)$ . For example, the permutation 3452167 has ascents (at positions) 1, 2, 5, and 6.

Similarly, a *descent* is a position *i* < *n* with $\sigma (i)>\sigma (i{+}1)$ , so every *i* with $1\leq i<n$ is either an ascent or a descent.

An *ascending run* of a permutation is a nonempty increasing contiguous subsequence that cannot be extended at either end; it corresponds to a maximal sequence of successive ascents (the latter may be empty: between two successive descents there is still an ascending run of length 1). By contrast an *increasing subsequence* of a permutation is not necessarily contiguous: it is an increasing sequence obtained by omitting some of the values of the one-line notation. For example, the permutation 2453167 has the ascending runs 245, 3, and 167, while it has an increasing subsequence 2367.

If a permutation has *k* − 1 descents, then it must be the union of *k* ascending runs.

The number of permutations of *n* with *k* ascents is (by definition) the Eulerian number $\textstyle \left\langle {n \atop k}\right\rangle$ ; this is also the number of permutations of *n* with *k* descents. Some authors however define the Eulerian number $\textstyle \left\langle {n \atop k}\right\rangle$ as the number of permutations with *k* ascending runs, which corresponds to *k* − 1 descents.

An exceedance of a permutation *σ*1*σ*2...*σ**n* is an index *j* such that *σ**j* > *j*. If the inequality is not strict (that is, *σ**j* ≥ *j*), then *j* is called a *weak exceedance*. The number of *n*-permutations with *k* exceedances coincides with the number of *n*-permutations with *k* descents.

A *record* or *left-to-right maximum* of a permutation *σ* is an element *i* such that *σ*(*j*) < *σ*(*i*) for all *j < i*.

### Foata's transition lemma

Foata's *fundamental bijection* transforms a permutation σ with a given canonical cycle form into the permutation $f(\sigma )={\hat {\sigma }}$ whose one-line notation has the same sequence of elements with parentheses removed. For example: $\sigma =(513)(6)(827)(94)={\begin{pmatrix}1&2&3&4&5&6&7&8&9\\3&7&5&9&1&6&8&2&4\end{pmatrix}},$

${\hat {\sigma }}=513682794={\begin{pmatrix}1&2&3&4&5&6&7&8&9\\5&1&3&6&8&2&7&9&4\end{pmatrix}}.$

Here the first element in each canonical cycle of σ becomes a record (left-to-right maximum) of ${\hat {\sigma }}$ . Given ${\hat {\sigma }}$ , one may find its records and insert parentheses to construct the inverse transformation $\sigma =f^{-1}({\hat {\sigma }})$ . Underlining the records in the above example: ${\hat {\sigma }}={\underline {5}}\,1\,3\,{\underline {6}}\,{\underline {8}}\,2\,7\,{\underline {9}}\,4$ , which allows the reconstruction of the cycles of σ.

The following table shows ${\hat {\sigma }}$ and σ for the six permutations of *S* = {1, 2, 3}, with the bold text on each side showing the notation used in the bijection: one-line notation for ${\hat {\sigma }}$ and canonical cycle notation for σ.

${\begin{array}{l|l}{\hat {\sigma }}=f(\sigma )&\sigma =f^{-1}({\hat {\sigma }})\\\hline \mathbf {123} =(\,1\,)(\,2\,)(\,3\,)&123=\mathbf {(\,1\,)(\,2\,)(\,3\,)} \\\mathbf {132} =(\,1\,)(\,3\,2\,)&132=\mathbf {(\,1\,)(\,3\,2\,)} \\\mathbf {213} =(\,2\,1\,)(\,3\,)&213=\mathbf {(\,2\,1\,)(\,3\,)} \\\mathbf {231} =(\,3\,1\,2\,)&321=\mathbf {(\,2\,)(\,3\,1\,)} \\\mathbf {312} =(\,3\,2\,1\,)&231=\mathbf {(\,3\,1\,2\,)} \\\mathbf {321} =(\,2\,)(\,3\,1\,)&312=\mathbf {(\,3\,2\,1\,)} \end{array}}$ As a first corollary, the number of *n*-permutations with exactly *k* records is equal to the number of *n*-permutations with exactly *k* cycles: this last number is the signless Stirling number of the first kind, $c(n,k)$ . Furthermore, Foata's mapping takes an *n*-permutation with *k* weak exceedances to an *n*-permutation with *k* − 1 ascents. For example, (2)(31) = 321 has *k =* 2 weak exceedances (at index 1 and 2), whereas *f*(321) = 231 has *k* − 1 = 1 ascent (at index 1; that is, from 2 to 3).

### Inversions

An *inversion* of a permutation *σ* is a pair (*i*, *j*) of positions where the entries of a permutation are in the opposite order: $i<j$ and $\sigma (i)>\sigma (j)$ . Thus a descent is an inversion at two adjacent positions. For example, *σ* = 23154 has (*i*, *j*) = (1, 3), (2, 3), and (4, 5), where (*σ*(*i*), *σ*(*j*)) = (2, 1), (3, 1), and (5, 4).

Sometimes an inversion is defined as the pair of values (*σ*(*i*), *σ*(*j*)); this makes no difference for the *number* of inversions, and the reverse pair (*σ*(*j*), *σ*(*i*)) is an inversion in the above sense for the inverse permutation *σ*−1.

The number of inversions is an important measure for the degree to which the entries of a permutation are out of order; it is the same for *σ* and for *σ*−1. To bring a permutation with *k* inversions into order (that is, transform it into the identity permutation), by successively applying (right-multiplication by) adjacent transpositions, is always possible and requires a sequence of *k* such operations. Moreover, any reasonable choice for the adjacent transpositions will work: it suffices to choose at each step a transposition of *i* and *i* + 1 where *i* is a descent of the permutation as modified so far (so that the transposition will remove this particular descent, although it might create other descents). This is so because applying such a transposition reduces the number of inversions by 1; as long as this number is not zero, the permutation is not the identity, so it has at least one descent. Bubble sort and insertion sort can be interpreted as particular instances of this procedure to put a sequence into order. Incidentally this procedure proves that any permutation *σ* can be written as a product of adjacent transpositions; for this one may simply reverse any sequence of such transpositions that transforms *σ* into the identity. In fact, by enumerating all sequences of adjacent transpositions that would transform *σ* into the identity, one obtains (after reversal) a *complete* list of all expressions of minimal length writing *σ* as a product of adjacent transpositions.

The number of permutations of *n* with *k* inversions is expressed by a Mahonian number. This is the coefficient of $q^{k}$ in the expansion of the product

$[n]_{q}!=\prod _{m=1}^{n}\sum _{i=0}^{m-1}q^{i}=1\left(1+q\right)\left(1+q+q^{2}\right)\cdots \left(1+q+q^{2}+\cdots +q^{n-1}\right),$

The notation $[n]_{q}!$ denotes the q-factorial. This expansion commonly appears in the study of necklaces.

Let $\sigma \in S_{n},i,j\in \{1,2,\dots ,n\}$ such that $i<j$ and $\sigma (i)>\sigma (j)$ . In this case, say the weight of the inversion $(i,j)$ is $\sigma (i)-\sigma (j)$ . Kobayashi (2011) proved the enumeration formula $\sum _{i<j,\sigma (i)>\sigma (j)}(\sigma (i)-\sigma (j))=|\{\tau \in S_{n}\mid \tau \leq \sigma ,\tau {\text{ is bigrassmannian}}\}$

where $\leq$ denotes Bruhat order in the symmetric groups. This graded partial order often appears in the context of Coxeter groups.
