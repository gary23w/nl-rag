---
title: "Abel–Ruffini theorem"
source: https://en.wikipedia.org/wiki/Abel%E2%80%93Ruffini_theorem
domain: galois-theory
license: CC-BY-SA-4.0
tags: galois theory, galois group, field extension, solvable group
fetched: 2026-07-02
---

# Abel–Ruffini theorem

In mathematics, the **Abel–Ruffini theorem** (also known as **Abel's impossibility theorem**) states that there is no solution in radicals to general polynomial equations of degree five or higher with arbitrary coefficients. Here, *general* means that the coefficients of the equation are viewed and manipulated as indeterminates.

The theorem is named after Paolo Ruffini, who made an incomplete proof in 1799 (which was refined and completed in 1813 and accepted by Cauchy) and Niels Henrik Abel, who provided a proof in 1824.

The term can also refer to the slightly stronger result that there are equations of degree five and higher that cannot be solved by radicals. This does not follow from Abel's statement of the theorem, but is a corollary of his proof, as his proof is based on the fact that some polynomials in the coefficients of the equation are not the zero polynomial. This improved statement follows directly from Galois theory § A non-solvable quintic example. Galois theory implies also that

$x^{5}-x-1=0$

is the simplest equation that cannot be solved in radicals, and that *almost all* polynomials of degree five or higher cannot be solved in radicals.

The impossibility of solving in degree five or higher contrasts with the case of lower degree: one has the quadratic formula, the cubic formula, and the quartic formula for degrees two, three, and four, respectively.

## Context

Polynomial equations of degree two can be solved with the quadratic formula, which has been known since antiquity. Similarly the cubic formula for degree three, and the quartic formula for degree four, were found during the 16th century. At that time a fundamental problem was whether equations of higher degree could be solved in a similar way.

The fact that every polynomial equation of positive degree has solutions, possibly non-real, was asserted during the 17th century, but completely proved only at the beginning of the 19th century. This is the fundamental theorem of algebra, which does not provide any tool for computing the solutions, although several methods are known for approximating all solutions to any desired accuracy.

From the 16th century to the beginning of the 19th century, the main problem of algebra was to search for a formula for the solutions of polynomial equations of degree five and higher, hence the name the "fundamental theorem of algebra". This meant a solution in radicals, that is, an expression involving only the coefficients of the equation, and the operations of addition, subtraction, multiplication, division, and nth root extraction.

The Abel–Ruffini theorem proves that this is impossible. However, this impossibility does not imply that a specific equation of any degree cannot be solved in radicals. On the contrary, there are equations of any degree that can be solved in radicals. This is the case of the equation $x^{n}-1=0$ for any n, and the equations defined by cyclotomic polynomials, all of whose solutions can be expressed in radicals.

Abel's proof of the theorem does not explicitly contain the assertion that there are specific equations that cannot be solved by radicals. Such an assertion is not a consequence of Abel's statement of the theorem, as the statement does not exclude the possibility that "every particular quintic equation might be soluble, with a special formula for each equation." However, the existence of specific equations that cannot be solved in radicals seems to be a consequence of Abel's proof, as the proof uses the fact that some polynomials in the coefficients are not the zero polynomial, and, given a finite number of polynomials, there are values of the variables at which none of the polynomials takes the value zero.

Soon after Abel's publication of his proof, Évariste Galois introduced a theory, now called Galois theory, that allows deciding, for any given equation, whether it is solvable in radicals. This was purely theoretical before the rise of electronic computers. With modern computers and programs, deciding whether a polynomial is solvable by radicals can be done for polynomials of degree greater than 100. Computing the solutions in radicals of solvable polynomials requires huge computations. Even for the degree five, the expression of the solutions is so huge that it has no practical interest.

## Proof

The proof of the Abel–Ruffini theorem predates Galois theory. However, Galois theory allows a better understanding of the subject, and modern proofs are generally based on it, while the original proofs of the Abel–Ruffini theorem are still presented for historical purposes.

The proofs based on Galois theory comprise four main steps: the characterization of solvable equations in terms of field theory; the use of the Galois correspondence between subfields of a given field and the subgroups of its Galois group for expressing this characterization in terms of solvable groups; the proof that the symmetric group is not solvable if its degree is five or higher; and the existence of polynomials with a symmetric Galois group.

### Algebraic solutions and field theory

An algebraic solution of a polynomial equation is an expression involving the four basic arithmetic operations (addition, subtraction, multiplication, and division), and root extractions. Such an expression may be viewed as the description of a computation that starts from the coefficients of the equation to be solved and proceeds by computing some numbers, one after the other.

At each step of the computation, one may consider the smallest field that contains all numbers that have been computed so far. This field is changed only for the steps involving the computation of an nth root.

So, an algebraic solution produces a sequence

$F_{0}\subseteq F_{1}\subseteq \cdots \subseteq F_{k}$

of fields, and elements $x_{i}\in F_{i}$ such that $F_{i}=F_{i-1}(x_{i})$ for $i=1,\ldots ,k,$ with $x_{i}^{n_{i}}\in F_{i-1}$ for some integer $n_{i}>1.$ An algebraic solution of the initial polynomial equation exists if and only if there exists such a sequence of fields such that $F_{k}$ contains a solution.

For having normal extensions, which are fundamental for the theory, one must refine the sequence of fields as follows. If $F_{i-1}$ does not contain all $n_{i}$ -th roots of unity, one introduces the field $K_{i}$ that extends $F_{i-1}$ by a primitive root of unity, and one redefines $F_{i}$ as $K_{i}(x_{i}).$

So, if one starts from a solution in terms of radicals, one gets an increasing sequence of fields such that the last one contains the solution, and each is a normal extension of the preceding one with a Galois group that is cyclic.

Conversely, if one has such a sequence of fields, the equation is solvable in terms of radicals. For proving this, it suffices to prove that a normal extension with a cyclic Galois group can be built from a succession of radical extensions.

### Galois correspondence

The Galois correspondence establishes a one to one correspondence between the subextensions of a normal field extension $F/E$ and the subgroups of the Galois group of the extension. This correspondence maps a field K such $E\subseteq K\subseteq F$ to the Galois group $\operatorname {Gal} (F/K)$ of the automorphisms of F that leave K fixed, and, conversely, maps a subgroup H of $\operatorname {Gal} (F/E)$ to the field of the elements of F that are fixed by H.

The preceding section shows that an equation is solvable in terms of radicals if and only if the Galois group of its splitting field (the smallest field that contains all the roots) is solvable, that is, it contains a sequence of subgroups such that each is normal in the preceding one, with a quotient group that is cyclic. (Solvable groups are commonly defined with abelian instead of cyclic quotient groups, but the fundamental theorem of finite abelian groups shows that the two definitions are equivalent).

So, for proving the Abel–Ruffini theorem, it remains to show that the symmetric group $S_{5}$ is not solvable, and that there are polynomials with symmetric Galois groups.

### Solvable symmetric groups

For *n* ≥ 5, the symmetric group ${\mathcal {S}}_{n}$ of degree n has only the alternating group ${\mathcal {A}}_{n}$ as a nontrivial normal subgroup (see Symmetric group § Normal subgroups). For *n* ≥ 5, the alternating group ${\mathcal {A}}_{n}$ is simple (that is, it does not have any nontrivial normal subgroup) and not abelian. This implies that both ${\mathcal {A}}_{n}$ and ${\mathcal {S}}_{n}$ are not solvable for *n* ≥ 5. Thus, the Abel–Ruffini theorem results from the existence of polynomials with a symmetric Galois group; this will be shown in the next section.

On the other hand, for *n* ≤ 4, the symmetric group and all its subgroups are solvable. This explains the existence of the quadratic, cubic, and quartic formulas, since a major result of Galois theory is that a polynomial equation has a solution in radicals if and only if its Galois group is solvable (the term "solvable group" takes its origin from this theorem).

### Polynomials with symmetric Galois groups

#### General equation

The *general* or *generic* polynomial equation of degree n is the equation

$x^{n}+a_{1}x^{n-1}+\cdots +a_{n-1}x+a_{n}=0,$

where $a_{1},\ldots ,a_{n}$ are distinct indeterminates. This is an equation defined over the field $F=\mathbb {Q} (a_{1},\ldots ,a_{n})$ of the rational fractions in $a_{1},\ldots ,a_{n}$ with rational number coefficients. The original Abel–Ruffini theorem asserts that, for *n* ≥ 5, this equation is not solvable in radicals. In view of the preceding sections, this results from the fact that the Galois group over F of the equation is the symmetric group ${\mathcal {S}}_{n}$ (this Galois group is the group of the field automorphisms of the splitting field of the equation that fix the elements of F, where the splitting field is the smallest field containing all the roots of the equation).

For proving that the Galois group is ${\mathcal {S}}_{n},$ it is simpler to start from the roots. Let $x_{1},\ldots ,x_{n}$ be new indeterminates, aimed to be the roots, and consider the polynomial

$P(x)=x^{n}+b_{1}x^{n-1}+\cdots +b_{n-1}x+b_{n}=(x-x_{1})\cdots (x-x_{n}).$

Let $H=\mathbb {Q} (x_{1},\ldots ,x_{n})$ be the field of the rational fractions in $x_{1},\ldots ,x_{n},$ and $K=\mathbb {Q} (b_{1},\ldots ,b_{n})$ be its subfield generated by the coefficients of $P(x).$ The permutations of the $x_{i}$ induce automorphisms of H. Vieta's formulas imply that every element of K is a symmetric function of the $x_{i},$ and is thus fixed by all these automorphisms. It follows that the Galois group $\operatorname {Gal} (H/K)$ is the symmetric group ${\mathcal {S}}_{n}.$

The fundamental theorem of symmetric polynomials implies that the $b_{i}$ are algebraic independent, and thus that the map that sends each $a_{i}$ to the corresponding $b_{i}$ is a field isomorphism from F to K. This means that one may consider $P(x)=0$ as a generic equation. This finishes the proof that the Galois group of a general equation is the symmetric group, and thus proves the original Abel–Ruffini theorem, which asserts that the general polynomial equation of degree n cannot be solved in radicals for *n* ≥ 5.

#### Explicit example

The equation $x^{5}-x-1=0$ is not solvable in radicals, as will be explained below.

Let q be $x^{5}-x-1$ . Let G be its Galois group, which acts faithfully on the set of complex roots of q. Numbering the roots lets one identify G with a subgroup of the symmetric group ${\mathcal {S}}_{5}$ . Since $q{\bmod {2}}$ factors as $(x^{2}+x+1)(x^{3}+x^{2}+1)$ in $\mathbb {F} _{2}[x]$ , the group G contains a permutation g that is a product of disjoint cycles of lengths 2 and 3 (in general, when a monic integer polynomial reduces modulo a prime to a product of distinct monic irreducible polynomials, the degrees of the factors give the lengths of the disjoint cycles in some permutation belonging to the Galois group); then G also contains $g^{3}$ , which is a transposition. Since $q{\bmod {3}}$ is irreducible in $\mathbb {F} _{3}[x]$ , the same principle shows that G contains a 5-cycle. Because 5 is prime, any transposition and 5-cycle in ${\mathcal {S}}_{5}$ generate the whole group; see Symmetric group § Generators and relations. Thus $G={\mathcal {S}}_{5}$ . Since the group ${\mathcal {S}}_{5}$ is not solvable, the equation $x^{5}-x-1=0$ is not solvable in radicals.

## Cayley's resolvent

Testing whether a specific quintic is solvable in radicals can be done by using Cayley's resolvent. This is a univariate polynomial of degree six whose coefficients are polynomials in the coefficients of a generic quintic. A specific irreducible quintic is solvable in radicals if and only, when its coefficients are substituted in Cayley's resolvent, the resulting sextic polynomial has a rational root, which can be easily tested for using the rational root theorem.

## History

Around 1770, Joseph Louis Lagrange began the groundwork that unified the many different methods that had been used up to that point to solve equations, relating them to the theory of groups of permutations, in the form of Lagrange resolvents. This innovative work by Lagrange was a precursor to Galois theory, and its failure to develop solutions for equations of fifth and higher degrees hinted that such solutions might be impossible, but it did not provide conclusive proof. The first person who conjectured that the problem of solving quintics by radicals might be impossible to solve was Carl Friedrich Gauss, who wrote in 1798 in section 359 of his book *Disquisitiones Arithmeticae* (which would be published only in 1801) that "there is little doubt that this problem does not so much defy modern methods of analysis as that it proposes the impossible". The next year, in his thesis, he wrote "After the labors of many geometers left little hope of ever arriving at the resolution of the general equation algebraically, it appears more and more likely that this resolution is impossible and contradictory." And he added "Perhaps it will not be so difficult to prove, with all rigor, the impossibility for the fifth degree. I shall set forth my investigations of this at greater length in another place." Actually, Gauss published nothing else on this subject.

The theorem was first nearly proved by Paolo Ruffini in 1799. He sent his proof to several mathematicians to get it acknowledged, amongst them Lagrange (who did not reply) and Augustin-Louis Cauchy, who sent him a letter saying: "Your memoir on the general solution of equations is a work which I have always believed should be kept in mind by mathematicians and which, in my opinion, proves conclusively the algebraic unsolvability of general equations of higher than fourth degree." However, in general, Ruffini's proof was not considered convincing. Abel wrote: "The first and, if I am not mistaken, the only one who, before me, has sought to prove the impossibility of the algebraic solution of general equations is the mathematician Ruffini. But his memoir is so complicated that it is very difficult to determine the validity of his argument. It seems to me that his argument is not completely satisfying."

The proof also, as it was discovered later, was incomplete. Ruffini assumed that all radicals that he was dealing with could be expressed from the roots of the polynomial using field operations alone; in modern terms, he assumed that the radicals belonged to the splitting field of the polynomial. To see why this is really an extra assumption, consider, for instance, the polynomial $P(x)=x^{3}-15x-20$ . According to Cardano's formula, one of its roots (all of them, actually) can be expressed as the sum of a cube root of $10+5i$ with a cube root of $10-5i$ . On the other hand, since $P(-3)<0$ , $P(-2)>0$ , $P(-1)<0$ , and $P(5)>0$ , the roots $r_{1}$ , $r_{2}$ , and $r_{3}$ of $P(x)$ are all real and therefore the field $\mathbf {Q} (r_{1},r_{2},r_{3})$ is a subfield of $\mathbf {R}$ . But then the numbers $10\pm 5i$ cannot belong to $\mathbf {Q} (r_{1},r_{2},r_{3})$ . While Cauchy either did not notice Ruffini's assumption or felt that it was a minor one, most historians believe that the proof was not complete until Abel proved the theorem on natural irrationalities, which asserts that the assumption holds in the case of general polynomials. The Abel–Ruffini theorem is thus generally credited to Abel, who published a proof compressed into just six pages in 1824. (Abel adopted a very terse style to save paper and money: the proof was printed at his own expense.) A more elaborated version of the proof would be published in 1826.

Proving that the general quintic (and higher) equations were unsolvable by radicals did not completely settle the matter, because the Abel–Ruffini theorem does not provide necessary and sufficient conditions for saying precisely which quintic (and higher) equations are unsolvable by radicals. Abel was working on a complete characterization when he died in 1829.

According to Nathan Jacobson, "The proofs of Ruffini and of Abel [...] were soon superseded by the crowning achievement of this line of research: Galois' discoveries in the theory of equations." In 1830, Galois (at the age of 18) submitted to the Paris Academy of Sciences a memoir on his theory of solvability by radicals, which was ultimately rejected in 1831 as being too sketchy and for giving a condition in terms of the roots of the equation instead of its coefficients. Galois was aware of the contributions of Ruffini and Abel, since he wrote "It is a common truth, today, that the general equation of degree greater than 4 cannot be solved by radicals... this truth has become common (by hearsay) despite the fact that geometers have ignored the proofs of Abel and Ruffini..." Galois then died in 1832 and his paper *Mémoire sur les conditions de resolubilité des équations par radicaux* remained unpublished until 1846, when it was published by Joseph Liouville accompanied by some of his own explanations. Prior to this publication, Liouville announced Galois' result to the academy in a speech he gave on 4 July 1843. A simplification of Abel's proof was published by Pierre Wantzel in 1845. When Wantzel published it, he was already aware of the contributions by Galois and he mentions that, whereas Abel's proof is valid only for general polynomials, Galois' approach can be used to provide a concrete polynomial of degree 5 whose roots cannot be expressed in radicals from its coefficients.

In 1963, Vladimir Arnold discovered a topological proof of the Abel–Ruffini theorem, which served as a starting point for topological Galois theory.
