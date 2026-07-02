---
title: "Pigeonhole principle"
source: https://en.wikipedia.org/wiki/Pigeonhole_principle
domain: discrete-mathematics
license: CC-BY-SA-4.0
tags: discrete math, discrete mathematics, combinatorics, graph theory, set theory, permutation
fetched: 2026-07-02
---

# Pigeonhole principle

In mathematics, the **pigeonhole principle** states that if n items are put into m containers, with *n* > *m*, then at least one container must contain more than one item. For example, of three gloves, at least two must be right-handed or at least two must be left-handed, because there are three objects but only two categories of handedness to put them into. This seemingly obvious statement, a type of counting argument, can be used to demonstrate possibly unexpected results. For example, given that the population of London is more than one unit greater than the maximum number of hairs that can be on a human head, the principle requires that there must be at least two people in London who have the same number of hairs on their heads.

Although the pigeonhole principle appears as early as 1622 in a book by Jean Leurechon, it is commonly called **Dirichlet's box principle** or **Dirichlet's drawer principle** after an 1834 treatment of the principle by Peter Gustav Lejeune Dirichlet under the name *Schubfachprinzip* ("drawer principle" or "shelf principle").

The principle has several generalizations and can be stated in various ways. In a more quantified version: for natural numbers k and m, if *n* = *km* + 1 objects are distributed among m sets, the pigeonhole principle asserts that at least one of the sets will contain at least *k* + 1 objects. For arbitrary n and m, this generalizes to $k+1=\lfloor (n-1)/m\rfloor +1=\lceil n/m\rceil$ , where $\lfloor \cdots \rfloor$ and $\lceil \cdots \rceil$ denote the floor and ceiling functions, respectively.

Though the principle's most straightforward application is to finite sets (such as pigeons and boxes), it is also used with infinite sets that cannot be put into one-to-one correspondence. To do so requires the formal statement of the pigeonhole principle: "there does not exist an injective function whose codomain is smaller than its domain". Advanced mathematical proofs like Siegel's lemma build upon this more general concept.

## Etymology

Dirichlet published his works in both French and German, using either the German *Schubfach* or the French *tiroir*. The strict original meaning of these terms corresponds to the English *drawer*, that is, an *open-topped box that can be slid in and out of the cabinet that contains it*. (Dirichlet wrote about distributing pearls among drawers.) These terms morphed to *pigeonhole* in the sense of a *small open space in a desk, cabinet, or wall for keeping letters or papers*, metaphorically rooted in structures that house pigeons.

Because furniture with pigeonholes is commonly used for storing or sorting things into many categories (such as letters in a post office or room keys in a hotel), the translation *pigeonhole* may be a better rendering of Dirichlet's original "drawer". That understanding of the term *pigeonhole*, referring to some furniture features, is fading—especially among those who do not speak English natively but as a lingua franca in the scientific world—in favor of the more pictorial interpretation, literally involving pigeons and holes. This suggestive (though not misleading) interpretation of "pigeonhole" as "dovecote" has lately found its way back to a German back-translation of the "pigeonhole principle" as the "*Taubenschlagprinzip*".

Besides the original terms "*Schubfachprinzip*" in German and "*Principe des tiroirs*" in French, other literal translations are still in use in Arabic ("مبدأ برج الحمام"), Bulgarian ("принцип на чекмеджетата"), Chinese ("抽屉原理"), Danish ("*Skuffeprincippet*"), Dutch ("*ladenprincipe*"), Hungarian ("*skatulyaelv*"), Italian ("*principio dei cassetti*"), Japanese ("引き出し論法"), Persian ("اصل لانه کبوتری"), Polish ("*zasada szufladkowa*"), Portuguese ("*Princípio das Gavetas*"), Swedish ("*Lådprincipen*"), Turkish ("*çekmece ilkesi*"), and Vietnamese ("*nguyên lý hộp*").

## History

Perhaps the first written reference to the pigeonhole principle appears in a short sentence from the French Jesuit Jean Leurechon's 1622 work *Selectæ Propositiones*: "It is necessary that two men have the same number of hairs, écus, or other things, as each other." The full principle was spelled out two years later, with additional examples, in another book that has often been attributed to Leurechon, but might be by Jean Appier Hanzelet.

## Examples

### Sock picking

Suppose a drawer contains a mixture of black socks and blue socks, each of which can be worn on either foot. You pull a number of socks from the drawer without looking. What is the minimum number of pulled socks required to guarantee a pair of the same color? By the pigeonhole principle (*m* = 2, using one pigeonhole per color), the answer is three (*n* = 3 items). Either you have *three* of one color, or you have *two* of one color and *one* of the other.

### Hand shaking

If *n* people can shake hands with one another (where *n* > 1), the pigeonhole principle shows that there is always a pair of people who will shake hands with the same number of people. In this application of the principle, the "hole" to which a person is assigned is the number of hands that person shakes. Since each person shakes hands with some number of people from 0 to *n* − 1, there are *n* possible holes. On the other hand, either the "0" hole, the "*n* − 1" hole, or both must be empty, for it is impossible (if *n* > 1) for some person to shake hands with everybody else while some person shakes hands with nobody. This leaves *n* people to be placed into at most *n* − 1 non-empty holes, so the principle applies.

This hand-shaking example is equivalent to the statement that in any graph with more than one vertex, there is at least one pair of vertices that share the same degree. This can be seen by associating each person with a vertex and each edge with a handshake.

### Hair counting

One can demonstrate there must be at least two people in London with the same number of hairs on their heads as follows. Since a typical human head has an average of around 150,000 hairs, it is reasonable to assume (as an upper bound) that no one has more than 1,000,000 hairs on their head (*m* = 1 million holes). There are more than 1,000,000 people in London (*n* is bigger than 1 million items). Assigning a pigeonhole to each number of hairs on a person's head, and assigning people to pigeonholes according to the number of hairs on their heads, there must be at least two people assigned to the same pigeonhole by the 1,000,001st assignment (because they have the same number of hairs on their heads; or, *n* > *m*). Assuming London has 9.002 million people, it follows that at least ten Londoners have the same number of hairs, as having nine Londoners in each of the 1 million pigeonholes accounts for only 9 million people.

For the average case (*m* = 150,000) with the constraint: fewest overlaps, there will be at most one person assigned to every pigeonhole and the 150,001st person assigned to the same pigeonhole as someone else. In the absence of this constraint, there may be empty pigeonholes because the "collision" happens before the 150,001st person. The principle just proves the existence of an overlap; it says nothing about the number of overlaps (which falls under the subject of probability distribution).

There is a passing, satirical, allusion in English to this version of the principle in *A History of the Athenian Society*, prefixed to *A Supplement to the Athenian Oracle: Being a Collection of the Remaining Questions and Answers in the Old Athenian Mercuries* (printed for Andrew Bell, London, 1710). It seems that the question *whether there were any two persons in the World that have an equal number of hairs on their head?* had been raised in *The Athenian Mercury* before 1704.

### The birthday problem

The birthday problem asks, for a set of *n* randomly chosen people, what is the probability that some pair of them will have the same birthday? The problem itself is mainly concerned with counterintuitive probabilities, but we can also tell by the pigeonhole principle that among 367 people, there is at least one pair of people who share the same birthday with 100% probability, as there are only 366 possible birthdays to choose from.

### Team tournament

Imagine seven people who want to play in a tournament of teams (*n* = 7 items), with a limitation of only four teams (*m* = 4 holes) to choose from. The pigeonhole principle tells us that they cannot all play for different teams; there must be at least one team featuring at least two of the seven players:

$\left\lfloor {\frac {n-1}{m}}\right\rfloor +1=\left\lfloor {\frac {7-1}{4}}\right\rfloor +1=\left\lfloor {\frac {6}{4}}\right\rfloor +1=1+1=2$

### Subset sum

Any subset of size six from the set $S=\{1,2,3,\dots ,9\}$ must contain two elements whose sum is 10. The pigeonholes will be labeled by the two element subsets $\{1,9\},\{2,8\},\{3,7\},\{4,6\}$ and the singleton $\{5\}$ , five pigeonholes in all. When the six "pigeons" (elements of the size six subset) are placed into these pigeonholes, each pigeon going into the pigeonhole that has it contained in its label, at least one of the pigeonholes labeled with a two-element subset will have two pigeons in it.

### Hashing

Hashing in computer science is the process of mapping an arbitrarily large set of data *n* to *m* fixed-size values. This has applications in caching whereby large data sets can be stored by a reference to their representative values (their "hashes") in a "hash table" for fast recall. Typically, the number of unique objects in a data set *n* is larger than the number of available unique hash codes *m*, and the pigeonhole principle holds in this case that hashing those objects is no guarantee of uniqueness, since if you hashed all objects in the data set *n*, some objects must necessarily share the same hash code.

## Uses and applications

The principle can be used to prove that any lossless compression algorithm, provided it makes some inputs smaller (as "compression" suggests), will also make some other inputs larger. Otherwise, the set of all input sequences up to a given length L could be mapped to the (much) smaller set of all sequences of length less than L without collisions (because the compression is lossless), a possibility that the pigeonhole principle excludes.

A notable problem in mathematical analysis is, for a fixed irrational number a , to show that the set ⁠ $\{[na]:n\in \mathbb {Z} \}$ ⁠ of fractional parts is dense in $[0,1]$ . One finds that it is not easy to explicitly find integers n , m such that $|na-m|<\varepsilon ,$ where $\varepsilon >0$ is a small positive number and a is some arbitrary irrational number. But if one takes M such that $1/M<\varepsilon$ , by the pigeonhole principle there must be $n_{1},n_{2}\in \{1,2,\ldots ,M+1\}$ such that $n_{1}a$ and $n_{2}a$ are in the same integer subdivision of size $1/M$ (there are only M such subdivisions between consecutive integers). In particular, one can find $n_{1}$ , $n_{2}$ such that

$n_{1}a\in \left(p+{\frac {k}{M}},\ p+{\frac {k+1}{M}}\right),\quad n_{2}a\in \left(q+{\frac {k}{M}},\ q+{\frac {k+1}{M}}\right),$

for some integers p , q and $k\in \{0,1,\cdots ,M-1\}$ . One can then easily verify that

$(n_{2}-n_{1})a\in \left(q-p-{\frac {1}{M}},q-p+{\frac {1}{M}}\right).$

This implies that $[na]<1/M<\varepsilon$ , where $n=n_{2}-n_{1}$ or $n=n_{1}-n_{2}$ . This shows that 0 is a limit point of $\{[na]\}$ . One can then use this fact to prove the case for p in $(0,1]$ : find n such that $[na]<1/M<\varepsilon$ ; then if $p\in (0,1/M]$ , the proof is complete. Otherwise

$p\in \left({\frac {j}{M}},{\frac {j+1}{M}}\right],$

and by setting

$k=\sup \left\{r\in N:r[na]<{\frac {j}{M}}\right\},$

one obtains

${\Bigl |}{\bigl [}(k+1)na{\bigr ]}-p{\Bigr |}<{\frac {1}{M}}<\varepsilon .$

Variants occur in a number of proofs. In the proof of the pumping lemma for regular languages, a version that mixes finite and infinite sets is used: If infinitely many objects are placed into finitely many boxes, then two objects share a box. In Fisk's solution to the Art gallery problem a sort of converse is used: If n objects are placed into k boxes, then there is a box containing at most $n/k$ objects.

## Alternative formulations

The following are alternative formulations of the pigeonhole principle.

1. If *n* objects are distributed over *m* places, and if *n* > *m*, then some place receives at least two objects.
2. (equivalent formulation of 1) If *n* objects are distributed over *n* places in such a way that no place receives more than one object, then each place receives exactly one object.
3. (generalization of 1) If *S* and *T* are sets, and the cardinality of *S* is greater than the cardinality of *T*, then there is no injective function from *S* to *T*.
4. If *n* objects are distributed over *m* places, and if *n* < *m*, then some place receives no object.
5. (equivalent formulation of 4) If *n* objects are distributed over *n* places in such a way that no place receives no object, then each place receives exactly one object.
6. (generalization of 4) If *S* and *T* are sets, and the cardinality of *S* is less than the cardinality of *T*, then there is no surjective function from *S* to *T*.

## Strong form

Let *q*1, *q*2, ..., *q**n* be positive integers. If

$q_{1}+q_{2}+\cdots +q_{n}-n+1$

objects are distributed into *n* boxes, then either the first box contains at least *q*1 objects, or the second box contains at least *q*2 objects, ..., or the *n*th box contains at least *q**n* objects.

The simple form is obtained from this by taking *q*1 = *q*2 = ... = *q**n* = 2, which gives *n* + 1 objects. Taking *q*1 = *q*2 = ... = *q**n* = *r* gives the more quantified version of the principle, namely:

Let *n* and *r* be positive integers. If *n*(*r* − 1) + 1 objects are distributed into *n* boxes, then at least one of the boxes contains *r* or more of the objects.

This can also be stated as, if *k* discrete objects are to be allocated to *n* containers, then at least one container must hold at least $\lceil k/n\rceil$ objects, where $\lceil x\rceil$ is the ceiling function, denoting the smallest integer larger than or equal to *x*. Similarly, at least one container must hold no more than $\lfloor k/n\rfloor$ objects, where $\lfloor x\rfloor$ is the floor function, denoting the largest integer smaller than or equal to *x*.

## Generalizations of the pigeonhole principle

A probabilistic generalization of the pigeonhole principle states that if *n* pigeons are randomly put into *m* pigeonholes with uniform probability 1/*m*, then at least one pigeonhole will hold more than one pigeon with probability

$1-{\frac {(m)_{n}}{m^{n}}},$

where (*m*)*n* is the falling factorial *m*(*m* − 1)(*m* − 2)...(*m* − *n* + 1). For *n* = 0 and for *n* = 1 (and *m* > 0), that probability is zero; in other words, if there is just one pigeon, there cannot be a conflict. For *n* > *m* (more pigeons than pigeonholes) it is one, in which case it coincides with the ordinary pigeonhole principle. But even if the number of pigeons does not exceed the number of pigeonholes (*n* ≤ *m*), due to the random nature of the assignment of pigeons to pigeonholes there is often a substantial chance that clashes will occur. For example, if 2 pigeons are randomly assigned to 4 pigeonholes, there is a 25% chance that at least one pigeonhole will hold more than one pigeon; for 5 pigeons and 10 holes, that probability is 69.76%; and for 10 pigeons and 20 holes it is about 93.45%. If the number of holes stays fixed, there is always a greater probability of a pair when you add more pigeons. This problem is treated at much greater length in the birthday paradox.

A further probabilistic generalization is that when a real-valued random variable *X* has a finite mean *E*(*X*), then the probability is nonzero that *X* is greater than or equal to *E*(*X*), and similarly the probability is nonzero that *X* is less than or equal to *E*(*X*). To see that this implies the standard pigeonhole principle, take any fixed arrangement of *n* pigeons into *m* holes and let *X* be the number of pigeons in a hole chosen uniformly at random. The mean of *X* is *n*/*m*, so if there are more pigeons than holes the mean is greater than one. Therefore, *X* is sometimes at least 2.

## Infinite sets

The pigeonhole principle can be extended to infinite sets by phrasing it in terms of cardinal numbers: if the cardinality of set A is greater than the cardinality of set B, then there is no injection from A to B. However, in this form the principle is tautological, since the meaning of the statement that the cardinality of set A is greater than the cardinality of set B is exactly that there is no injective map from A to B. However, adding at least one element to a finite set is sufficient to ensure that the cardinality increases.

Another way to phrase the pigeonhole principle for finite sets is similar to the principle that finite sets are Dedekind finite: Let A and B be finite sets. If there is a surjection from A to B that is not injective, then no surjection from A to B is injective. In fact no function of any kind from A to B is injective. This is not true for infinite sets: Consider the function on the natural numbers that sends 1 and 2 to 1, 3 and 4 to 2, 5 and 6 to 3, and so on.

There is a similar principle for infinite sets: If uncountably many pigeons are stuffed into countably many pigeonholes, there will exist at least one pigeonhole having uncountably many pigeons stuffed into it.

This principle is not a generalization of the pigeonhole principle for finite sets however: It is in general false for finite sets. In technical terms it says that if A and B are finite sets such that any surjective function from A to B is not injective, then there exists an element b of B such that there exists a bijection between the preimage of b and A. This is a quite different statement, and is absurd for large finite cardinalities.

## Quantum mechanics

Yakir Aharonov et al. presented arguments that quantum mechanics may violate the pigeonhole principle, and proposed interferometric experiments to test the pigeonhole principle in quantum mechanics.

Later research has called this conclusion into question. In a January 2015 arXiv preprint, researchers Alastair Rae and Ted Forgan at the University of Birmingham performed a theoretical wave function analysis, employing the standard pigeonhole principle, on the flight of electrons at various energies through an interferometer. If the electrons had no interaction strength at all, they would each produce a single, perfectly circular peak. At high interaction strength, each electron produces four distinct peaks, for a total of 12 peaks on the detector; these peaks are the result of the four possible interactions each electron could experience (alone, together with the first other particle only, together with the second other particle only, or all three together). If the interaction strength was fairly low, as would be the case in many real experiments, the deviation from a zero-interaction pattern would be nearly indiscernible, much smaller than the lattice spacing of atoms in solids, such as the detectors used for observing these patterns. This would make it very difficult or impossible to distinguish a weak-but-nonzero interaction strength from no interaction whatsoever, and thus give an illusion of three electrons that did not interact despite all three passing through two paths.
