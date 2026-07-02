---
title: "Hilbert's tenth problem"
source: https://en.wikipedia.org/wiki/Hilbert's_tenth_problem
domain: diophantine-equations
license: CC-BY-SA-4.0
tags: diophantine equation, pell's equation, fermat's last theorem, pythagorean triple
fetched: 2026-07-02
---

# Hilbert's tenth problem

**Hilbert's tenth problem** is the tenth on the list of mathematical problems that the German mathematician David Hilbert posed in 1900. It is the challenge to provide a general algorithm that, for any given Diophantine equation (a polynomial equation with integer coefficients and a finite number of unknowns), can decide whether the equation has a solution with all unknowns taking integer values.

For example, the Diophantine equation $3x^{2}-2xy-y^{2}z-7=0$ has an integer solution: $x=1,\ y=2,\ z=-2$ . By contrast, the Diophantine equation $x^{2}+y^{2}+1=0$ has no such solution.

The solution to Hilbert's tenth problem shows that such a general algorithm cannot exist. This is the result of combined work of Martin Davis, Yuri Matiyasevich, Hilary Putnam, and Julia Robinson spanning 21 years, with Matiyasevich completing the theorem in 1970. The theorem is now known as Matiyasevich's theorem or the MRDP theorem (an initialism for the surnames of the four principal contributors to its solution).

When all coefficients and variables are restricted to be *positive* integers, the related problem of polynomial identity testing is a decidable (exponentiation-free) variation of Tarski's high school algebra problem, sometimes denoted ${\overline {HSI}}.$

## Background

### Original formulation

Hilbert formulated the problem as follows:

> *Given a Diophantine equation with any number of unknown quantities and with rational integral numerical coefficients:* *To devise a process according to which it can be determined in a finite number of operations whether the equation is solvable in rational integers.*

The words "process" and "finite number of operations" have been taken to mean that Hilbert was asking for an algorithm. The term "rational integral" simply refers to the integers, positive, negative, or zero: 0, ±1, ±2, ... . So Hilbert was asking for a general algorithm to decide whether a given polynomial Diophantine equation with integer coefficients has a solution in integers.

Hilbert's problem is not concerned with finding the solutions. It only asks whether, in general, we can decide whether one or more solutions exist. The answer to this question is negative, in the sense that no "process can be devised" for answering that question. In modern terms, Hilbert's tenth problem is an undecidable problem.

### Diophantine sets

In a Diophantine equation, there are two kinds of variables: the parameters and the unknowns. The Diophantine set consists of the parameter assignments for which the Diophantine equation is solvable. A typical example is the linear Diophantine equation in two unknowns,

$a_{1}x+a_{2}y=a_{3},$

where the equation is solvable if and only if the greatest common divisor $\gcd(a_{1},a_{2})$ evenly divides $a_{3}$ . The set of all ordered triples $(a_{1},a_{2},a_{3})$ satisfying this restriction is called the *Diophantine set* defined by $a_{1}x+a_{2}y=a_{3}$ . In these terms, Hilbert's tenth problem asks whether there is an algorithm to determine if the Diophantine set corresponding to an arbitrary polynomial is non-empty.

The problem is generally understood in terms of the natural numbers (that is, the non-negative integers) rather than arbitrary integers. However, the two problems are equivalent: any general algorithm that can decide whether a given Diophantine equation has an integer solution could be modified into an algorithm that decides whether a given Diophantine equation has a natural-number solution, and vice versa. By Lagrange's four-square theorem, every natural number is the sum of the squares of four integers, so we could rewrite every natural-valued parameter in terms of the sum of the squares of four new integer-valued parameters. Similarly, since every integer is the difference of two natural numbers, we could rewrite every integer parameter as the difference of two natural parameters. Furthermore, we can always rewrite a system of simultaneous equations $p_{1}=0,\ldots ,p_{k}=0$ (where each $p_{i}$ is a polynomial) as a single equation $p_{1}^{\,2}+\cdots +p_{k}^{\,2}=0$ .

### Recursively enumerable sets

A recursively enumerable set can be characterized as one for which there exists an algorithm that will eventually halt when a member of the set is provided as input, but may continue indefinitely when the input is a non-member. It was the development of computability theory (also known as recursion theory) that provided a precise explication of the intuitive notion of algorithmic computability, thus making the notion of recursive enumerability perfectly rigorous. It is evident that Diophantine sets are recursively enumerable (also known as semi-decidable). This is because one can arrange all possible tuples of values of the unknowns in a sequence and then, for a given value of the parameter(s), test these tuples, one after another, to see whether they are solutions of the corresponding equation. The unsolvability of Hilbert's tenth problem is a consequence of the surprising fact that the converse is true:

> *Every recursively enumerable set is Diophantine.*

This result is variously known as Matiyasevich's theorem (because he provided the crucial step that completed the proof) and the MRDP theorem (for Yuri Matiyasevich, Julia Robinson, Martin Davis, and Hilary Putnam). Because *there exists a recursively enumerable set that is not computable,* the unsolvability of Hilbert's tenth problem is an immediate consequence. In fact, more can be said: there is a polynomial

$p(a,x_{1},\ldots ,x_{n})$

with integer coefficients such that the set of values of a for which the equation

$p(a,x_{1},\ldots ,x_{n})=0$

has solutions in natural numbers is not computable. So, not only is there no general algorithm for testing Diophantine equations for solvability, but there is none even for this family of single-parameter equations.

## History

| Year | Events |
|---|---|
| 1944 | Emil Leon Post declares that Hilbert's tenth problem "begs for an unsolvability proof". |
| 1949 | Martin Davis uses Kurt Gödel's method for applying the Chinese remainder theorem as a coding trick to obtain his normal form for recursively enumerable sets: $\left\{a\mid \exists y\,\forall k\leqslant y\,\exists x_{1},\ldots ,x_{n}:p\left(a,k,y,x_{1},\ldots ,x_{n}\right)=0\right\}$ where p is a polynomial with integer coefficients. Purely formally, it is only the bounded universal quantifier that stands in the way of this being a definition of a Diophantine set. Using a non-constructive but easy proof, he derives as a corollary to this normal form that the set of Diophantine sets is not closed under complementation, by showing that there exists a Diophantine set whose complement is not Diophantine. Because the recursively enumerable sets also are not closed under complementation, he conjectures that the two classes are identical. |
| 1950 | Julia Robinson, unaware of Davis's work, investigates the connection of the exponential function to the problem, and attempts to prove that EXP, the set of triplets $(a,b,c)$ for which $a=b^{c}$ , is Diophantine. Not succeeding, she makes the following *hypothesis* (later called J.R.): *There is a Diophantine set* D *of pairs* $(a,b)$ *such that* $(a,b)\in D\Rightarrow b<a^{a}$ *and for every positive* $k,$ there exists $(a,b)\in D$ *such that* $b>a^{k}.$ Using properties of the Pell equation, she proves that J.R. implies that EXP is Diophantine, as well as the binomial coefficients, the factorial, and the primes. |
| 1959 | Working together, Davis and Putnam study *exponential Diophantine sets*: sets definable by Diophantine equations in which some of the exponents may be unknowns. Using the Davis normal form together with Robinson's methods, and assuming the then unproved conjecture that *there are arbitrarily long arithmetic progressions consisting of prime numbers*, they prove that every recursively enumerable set is exponential Diophantine. They also prove as a corollary that J.R. implies that every recursively enumerable set is Diophantine, which in turn implies that Hilbert's tenth problem is unsolvable. |
| 1960 | Robinson simplifies the proof of the conditional result for exponential Diophantine sets and makes it independent from the conjecture about primes and thus a formal theorem. This makes the J.R. hypothesis a sufficient condition for the unsolvability of Hilbert's tenth problem. However, many were doubting that J.R. is true. |
| 1961–1969 | During this period, Davis and Putnam find various propositions that imply J.R., and Robinson, having previously shown that J.R. implies that the set of primes is a Diophantine set, proves that this is an if and only if condition. Yuri Matiyasevich publishes some reductions of Hilbert's tenth problem. |
| 1970 | Drawing from the recently published work of Nikolai Vorob'ev on Fibonacci numbers, Matiyasevich proves that the set $P=\{(a,b)\mid a>0,b=F_{2a}\},$ where $F_{n}$ is the *n*th Fibonacci number, is Diophantine and exhibits exponential growth. This proves the J.R. hypothesis, which by then had been an open question for 20 years. Combining J.R. with the theorem that every recursively enumerable set is exponential Diophantine, proves that recursively enumerable sets are Diophantine. This makes Hilbert's tenth problem unsolvable. |

## Applications

The Matiyasevich/MRDP theorem relates two notions—one from computability theory, the other from number theory—and has some surprising consequences. Perhaps the most surprising is the existence of a *universal* Diophantine equation:

There exists a polynomial

$p(a,n,x_{1},\ldots ,x_{k})$

such that, given any Diophantine set

S

there is a number

$n_{0}$

such that

$S=\{\,a\mid \exists x_{1},\ldots ,x_{k}\,[p(a,n_{0},x_{1},\ldots ,x_{k})=0]\,\}.$

This is true simply because Diophantine sets, being equal to recursively enumerable sets, are also equal to Turing machines. It is a well known property of Turing machines that there exist universal Turing machines, capable of executing any algorithm.

Hilary Putnam has pointed out that for any Diophantine set S of positive integers, there is a polynomial

$q(x_{0},x_{1},\ldots ,x_{n})$

such that S consists of exactly the positive numbers among the values assumed by q as the variables

$x_{0},x_{1},\ldots ,x_{n}$

range over all natural numbers. This can be seen as follows: If

$p(a,y_{1},\ldots ,y_{n})=0$

provides a Diophantine definition of S , then it suffices to set

$q(x_{0},x_{1},\ldots ,x_{n})=x_{0}[1-p(x_{0},x_{1},\ldots ,x_{n})^{2}].$

So, for example, there is a polynomial for which the positive part of its range is exactly the prime numbers. (On the other hand, no polynomial can only take on prime values.) The same holds for other recursively enumerable sets of natural numbers: the factorial, the binomial coefficients, the fibonacci numbers, etc.

Other applications concern what logicians refer to as $\Pi _{1}^{0}$ propositions, sometimes also called propositions of *Goldbach type*. These are like Goldbach's conjecture, in stating that all natural numbers possess a certain property that is algorithmically checkable for each particular number. The Matiyasevich/MRDP theorem implies that each such proposition is equivalent to a statement that asserts that some particular Diophantine equation has no solutions in natural numbers. A number of important and celebrated problems are of this form: in particular, Fermat's Last Theorem, the Riemann hypothesis, and the four color theorem. In addition the assertion that particular formal systems such as Peano arithmetic or ZFC are consistent can be expressed as $\Pi _{1}^{0}$ sentences. The idea is to follow Kurt Gödel in coding proofs by natural numbers in such a way that the property of being the number representing a proof is algorithmically checkable.

$\Pi _{1}^{0}$ sentences have the special property that if they are false, that fact will be provable in any of the usual formal systems. This is because the falsity amounts to the existence of a counter-example that can be verified by simple arithmetic. So if a $\Pi _{1}^{0}$ sentence is such that neither it nor its negation is provable in one of these systems, that sentence must be true.

A particularly striking form of Gödel's incompleteness theorem is also a consequence of the Matiyasevich/MRDP theorem:

> Let
> 
> $p(a,x_{1},\ldots ,x_{k})=0$
> 
> provide a Diophantine definition of a non-computable set. Let A be an algorithm that outputs a sequence of natural numbers n such that the corresponding equation
> 
> $p(n,x_{1},\ldots ,x_{k})=0$
> 
> has no solutions in natural numbers. Then there is a number $n_{0}$ that is not output by A while in fact the equation
> 
> $p(n_{0},x_{1},\ldots ,x_{k})=0$
> 
> has no solutions in natural numbers.

To see that the theorem is true, it suffices to notice that if there were no such number $n_{0}$ , one could algorithmically test membership of a number n in this non-computable set by simultaneously running the algorithm A to see whether n is output while also checking all possible k -tuples of natural numbers seeking a solution of the equation

$p(n,x_{1},\ldots ,x_{k})=0$

and we may associate an algorithm A with any of the usual formal systems such as Peano arithmetic or ZFC by letting it systematically generate consequences of the axioms and then output a number n whenever a sentence of the form

$\neg \exists x_{1},\ldots ,x_{k}\,[p(n,x_{1},\ldots ,x_{k})=0]$

is generated. Then the theorem tells us that either a false statement of this form is proved or a true one remains unproved in the system in question.

## Further results

We may speak of the *degree* of a Diophantine set as being the least degree of a polynomial in an equation defining that set. Similarly, we can call the *dimension* of such a set the fewest unknowns in a defining equation. Because of the existence of a universal Diophantine equation, it is clear that there are absolute upper bounds to both of these quantities, and there has been much interest in determining these bounds.

Already in the 1920s Thoralf Skolem showed that any Diophantine equation is equivalent to one of degree 4 or less. His trick was to introduce new unknowns by equations setting them equal to the square of an unknown or the product of two unknowns. Repetition of this process results in a system of second degree equations; then an equation of degree 4 is obtained by summing the squares. So every Diophantine set is trivially of degree 4 or less. It is not known whether this result is best possible.

Julia Robinson and Yuri Matiyasevich showed that every Diophantine set has dimension no greater than 13. Later, Matiyasevich sharpened their methods to show that 9 unknowns suffice. Although it may well be that this result is not the best possible, there has been no further progress. So, in particular, there is no algorithm for testing Diophantine equations with 9 or fewer unknowns for solvability in natural numbers. For the case of rational integer solutions (as Hilbert had originally posed it), the 4-squares trick shows that there is no algorithm for equations with no more than 36 unknowns. But Zi-Wei Sun showed that the problem for integers is unsolvable even for equations with no more than 11 unknowns.

Martin Davis studied algorithmic questions involving the number of solutions of a Diophantine equation. Hilbert's tenth problem asks whether or not that number is 0. Let $A=\{0,1,2,3,\ldots ,\aleph _{0}\}$ and let C be a proper non-empty subset of A . Davis proved that there is no algorithm to test a given Diophantine equation to determine whether the number of its solutions is a member of the set C . Thus there is no algorithm to determine whether the number of solutions of a Diophantine equation is finite, odd, a perfect square, a prime, etc.

The proof of the MRDP theorem has been formalized in Rocq (previously known as *Coq*).

## Extensions of Hilbert's tenth problem

Although Hilbert posed the problem for the rational integers, it can be just as well asked for many rings (in particular, for any ring whose number of elements is countable). Obvious examples are the rings of integers of algebraic number fields as well as the rational numbers.

There has been much work on Hilbert's tenth problem for the rings of integers of algebraic number fields. Basing themselves on earlier work by Jan Denef and Leonard Lipschitz and using class field theory, Harold N. Shapiro and Alexandra Shlapentokh were able to prove:

> *Hilbert's tenth problem is unsolvable for the ring of integers of any algebraic number field whose Galois group over the rationals is abelian.*

Shlapentokh and Thanases Pheidas (independently of one another) obtained the same result for algebraic number fields admitting exactly one pair of complex conjugate embeddings.

The problem for the ring of integers of algebraic number fields other than those covered by the results above remains open. Likewise, despite much interest, the problem for equations over the rationals remains open. Barry Mazur has conjectured that for any variety over the rationals, the topological closure over the reals of the set of solutions has only finitely many components. This conjecture implies that the integers are not Diophantine over the rationals, and so if this conjecture is true, a negative answer to Hilbert's Tenth Problem would require a different approach than that used for other rings.

In 2024, Peter Koymans and Carlo Pagano published a claimed proof that Hilbert's 10th problem is undecidable for every ring of integers using additive combinatorics. Another team of mathematicians subsequently claimed another proof of the same result, using different methods.
