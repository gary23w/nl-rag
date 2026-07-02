---
title: "Prime number (part 1/2)"
source: https://en.wikipedia.org/wiki/Prime_number
domain: number-theory
license: CC-BY-SA-4.0
tags: number theory, modular arithmetic, prime number, gcd
fetched: 2026-07-02
part: 1/2
---

# Prime number

A **prime number** (or a **prime**) is a natural number greater than 1 that is not a product of two smaller natural numbers. A natural number greater than 1 that is not prime is called a composite number. For example, 5 is prime because the only ways of writing it as a product, 1 × 5 or 5 × 1, involve 5 itself. However, 4 is composite because it is a product (2 × 2) in which both numbers are smaller than 4. Primes are central in number theory because of the fundamental theorem of arithmetic: every natural number greater than 1 is either a prime itself or can be factorized as a product of primes that is unique up to their order.

The property of being prime is called **primality**. A simple but slow method of checking the primality of a given number ⁠ n ⁠, called trial division, tests whether ⁠ n ⁠ is a multiple of any integer between 2 and ⁠ ${\sqrt {n}}$ ⁠. Faster algorithms include the Miller–Rabin primality test, which is fast but has a small chance of error, and the AKS primality test, which always produces the correct answer in polynomial time but is too slow to be practical. Particularly fast methods are available for numbers of special forms, such as Mersenne numbers, and these have been used to find large prime numbers.

There are infinitely many primes, as demonstrated by Euclid around 300 BC. No known simple formula separates prime numbers from composite numbers. However, the distribution of primes within the natural numbers in the large can be statistically modelled. The first result in that direction is the prime number theorem, proven at the end of the 19th century, which says roughly that the probability of a randomly chosen large number being prime is inversely proportional to its number of digits, that is, to its logarithm.

Several historical questions regarding prime numbers are still unsolved. These include Goldbach's conjecture, that every even integer greater than 2 can be expressed as the sum of two primes, and the twin prime conjecture, that there are infinitely many pairs of primes that differ by two. Such questions spurred the development of various branches of number theory, focusing on analytic or algebraic aspects of numbers. Primes are used in several routines in information technology, such as public-key cryptography, which relies on the difficulty of factoring large numbers into their prime factors. In abstract algebra, objects that behave in a generalized way like prime numbers include prime elements and prime ideals.


## Definition and examples

A natural number (1, 2, 3, 4, 5, 6, etc.) is called a *prime number* (or a *prime*) if it is greater than 1 and cannot be written as the product of two smaller natural numbers. The numbers greater than 1 that are not prime are called composite numbers. In other words, ⁠ n ⁠ is prime if ⁠ n ⁠ items cannot be divided up into smaller equal-size groups of more than one item, or if it is not possible to arrange ⁠ n ⁠ dots into a rectangular grid that is more than one dot wide and more than one dot high. For example, among the numbers 1 through 6, the numbers 2, 3, and 5 are the prime numbers, as there are no other numbers that divide them evenly (without a remainder). 1 is not prime, as it is specifically excluded in the definition. 4 = 2 × 2 and 6 = 2 × 3 are both composite.

The divisors of a natural number ⁠ n ⁠ are the natural numbers that divide ⁠ n ⁠ evenly. Every natural number has both 1 and itself as a divisor. If it has any other divisor, it cannot be prime. This leads to an equivalent definition of prime numbers: they are the numbers with exactly two positive divisors. Those two are 1 and the number itself. As 1 has only one divisor, itself, it is not prime by this definition. Yet another way to express the same thing is that a number ⁠ n ⁠ is prime if it is greater than one and if none of the numbers $2,3,\dots ,n-1$ divides ⁠ n ⁠ evenly.

The first 25 prime numbers (all the prime numbers less than 100) are:

2

,

3

,

5

,

7

,

11

,

13

,

17

,

19

,

23

,

29

,

31

,

37

,

41

,

43

,

47

,

53

,

59

,

61

,

67

,

71

,

73

,

79

,

83

,

89

,

97

(sequence

A000040

in the

OEIS

)

.

No even number ⁠ n ⁠ greater than 2 is prime because any such number can be expressed as the product ⁠ $2\times n/2$ ⁠. Therefore, every prime number other than 2 is an odd number, and is called an *odd prime*. Similarly, when written in the usual decimal system, all prime numbers larger than 5 end in 1, 3, 7, or 9. The numbers that end with other digits are all composite: decimal numbers that end in 0, 2, 4, 6, or 8 are even, and decimal numbers that end in 0 or 5 are divisible by 5.

The set of all primes is sometimes denoted by $\mathbf {P}$ (a boldface capital P) or by $\mathbb {P}$ (a blackboard bold capital P).


## History

From around 1550 BC, the Rhind Mathematical Papyrus has Egyptian fraction expansions of different forms for fractions with prime and composite denominators. However, the earliest surviving records of the study of prime numbers come from the ancient Greek mathematicians, who called them *prōtos arithmòs* (πρῶτος ἀριθμὸς). Euclid's *Elements* (c. 300 BC) proves the infinitude of primes and the fundamental theorem of arithmetic, and shows how to construct a perfect number from a Mersenne prime. Another Greek invention, the Sieve of Eratosthenes, is still used to construct lists of primes.

Around 1000 AD, the Islamic mathematician Ibn al-Haytham (Alhazen) found Wilson's theorem, characterizing the prime numbers as the numbers ⁠ n ⁠ that evenly divide ⁠ $(n-1)!+1$ ⁠. He also conjectured that all even perfect numbers come from Euclid's construction using Mersenne primes, but was unable to prove it. Another Islamic mathematician, Ibn al-Banna' al-Marrakushi, observed that the sieve of Eratosthenes can be sped up by considering only the prime divisors up to the square root of the upper limit. Fibonacci took the innovations from Islamic mathematics to Europe. His book *Liber Abaci* (1202) was the first to describe trial division for testing primality, again using divisors only up to the square root.

In 1640 Pierre de Fermat stated (without proof) Fermat's little theorem (later proved by Leibniz and Euler). Fermat also investigated the primality of the Fermat numbers ⁠ $2^{2^{n}}+1$ ⁠, and Marin Mersenne studied the Mersenne primes, prime numbers of the form $2^{p}-1$ with ⁠ p ⁠ itself a prime. Christian Goldbach formulated Goldbach's conjecture, that every even number is the sum of two primes, in a 1742 letter to Euler. Euler proved Alhazen's conjecture (now the Euclid–Euler theorem) that all even perfect numbers can be constructed from Mersenne primes. He introduced methods from mathematical analysis to this area in his proofs of the infinitude of the primes and the divergence of the sum of the reciprocals of the primes ⁠ ${\tfrac {1}{2}}+{\tfrac {1}{3}}+{\tfrac {1}{5}}+{\tfrac {1}{7}}+{\tfrac {1}{11}}+\cdots$ ⁠. At the start of the 19th century, Legendre and Gauss conjectured that as ⁠ x ⁠ tends to infinity, the number of primes up to ⁠ x ⁠ is asymptotic to ⁠ $x/\log x$ ⁠, where $\log x$ is the natural logarithm of ⁠ x ⁠. A weaker consequence of this high density of primes was Bertrand's postulate, that for every $n>1$ there is a prime between ⁠ n ⁠ and ⁠ $2n$ ⁠, proved in 1852 by Pafnuty Chebyshev. Ideas of Bernhard Riemann in his 1859 paper on the zeta-function sketched an outline for proving the conjecture of Legendre and Gauss. Although the closely related Riemann hypothesis remains unproven, Riemann's outline was completed in 1896 by Hadamard and de la Vallée Poussin, and the result is now known as the prime number theorem. Another important 19th century result was Dirichlet's theorem on arithmetic progressions, that certain arithmetic progressions contain infinitely many primes.

Many mathematicians have worked on primality tests for numbers larger than those where trial division is practicably applicable. Methods that are restricted to specific number forms include Pépin's test for Fermat numbers (1877), Proth's theorem (c. 1878), the Lucas–Lehmer primality test (originated 1856), and the generalized Lucas primality test.

Since 1951 all the largest known primes have been found using these tests on computers. The search for ever larger primes has generated interest outside mathematical circles, through the Great Internet Mersenne Prime Search and other distributed computing projects. The idea that prime numbers had few applications outside of pure mathematics was shattered in the 1970s when public-key cryptography and the RSA cryptosystem were invented, using prime numbers as their basis.

The increased practical importance of computerized primality testing and factorization led to the development of improved methods capable of handling large numbers of unrestricted form. The mathematical theory of prime numbers also moved forward with the Green–Tao theorem (2004) that there are arbitrarily long arithmetic progressions of prime numbers, and Yitang Zhang's 2013 proof that there exist infinitely many prime gaps of bounded size.

### Primality of one

Most early Greeks did not even consider 1 to be a number, so they could not consider its primality. A few scholars in the Greek and later Roman tradition, including Nicomachus, Iamblichus, Boethius, and Cassiodorus, also considered the prime numbers to be a subdivision of the odd numbers, so they did not consider ⁠ 2 ⁠ to be prime either. However, Euclid and a majority of the other Greek mathematicians considered ⁠ 2 ⁠ as prime. The medieval Islamic mathematicians largely followed the Greeks in viewing 1 as not being a number. By the Middle Ages and Renaissance, mathematicians began treating 1 as a number, and by the 17th century some of them included it as the first prime number. In the mid-18th century, Christian Goldbach listed 1 as prime in his correspondence with Leonhard Euler; however, Euler himself did not consider 1 to be prime. Many 19th century mathematicians still considered 1 to be prime, and Derrick Norman Lehmer included 1 in his *list of primes less than ten million* published in 1914. Lists of primes that included 1 continued to be published as recently as 1956. However, by the early 20th century mathematicians began to agree that 1 should not be listed as prime, but rather in its own special category as a "unit".

If 1 were to be considered a prime, many statements involving primes would need to be awkwardly reworded. For example, the fundamental theorem of arithmetic would need to be rephrased in terms of factorizations into primes greater than 1, because every number would have multiple factorizations with any number of copies of 1. Similarly, the sieve of Eratosthenes would not work correctly if it handled 1 as a prime, because it would eliminate all multiples of 1 (that is, all other numbers) and output only the single number 1. Some other more technical properties of prime numbers also do not hold for the number 1: for instance, the formulas for Euler's totient function or for the sum of divisors function are different for prime numbers than they are for 1.


## Elementary properties

### Unique factorization

Writing a number as a product of prime numbers is called a *prime factorization* of the number. For example:

${\begin{aligned}50&=2\times 5\times 5\\&=2\times 5^{2}.\end{aligned}}$

The terms in the product are called *prime factors*. The same prime factor may occur more than once; this example has two copies of the prime factor $5.$ When a prime occurs multiple times, exponentiation can be used to group together multiple copies of the same prime number: for example, in the second way of writing the product above, $5^{2}$ denotes the square or second power of ⁠ 5 ⁠.

The central importance of prime numbers to number theory and mathematics in general stems from the *fundamental theorem of arithmetic*. This theorem states that every integer larger than 1 can be written as a product of one or more primes. More strongly, this product is unique in the sense that any two prime factorizations of the same number will have the same numbers of copies of the same primes, although their ordering may differ. So, although there are many different ways of finding a factorization using an integer factorization algorithm, they all must produce the same result. Primes can thus be considered the "basic building blocks" of the natural numbers.

Some proofs of the uniqueness of prime factorizations are based on Euclid's lemma: If ⁠ p ⁠ is a prime number and ⁠ p ⁠ divides a product $ab$ of integers ⁠ a ⁠ and $b,$ then ⁠ p ⁠ divides ⁠ a ⁠ or ⁠ p ⁠ divides ⁠ b ⁠ (or both). Conversely, if a number ⁠ p ⁠ has the property that when it divides a product it always divides at least one factor of the product, then ⁠ p ⁠ must be prime.

### Infinitude

There are infinitely many prime numbers. Another way of saying this is that the sequence

$2,3,5,7,11,13,...$

of prime numbers never ends. This statement is referred to as *Euclid's theorem* in honor of the ancient Greek mathematician Euclid, since the first known proof for this statement is attributed to him. Many more proofs of the infinitude of primes are known, including an analytical proof by Euler, Goldbach's proof based on Fermat numbers, Furstenberg's proof using general topology, and Kummer's proof by contradiction.

Euclid's proof shows that every finite list of primes is incomplete. The key idea is to multiply together the primes in any given list and add $1.$ If the list consists of the primes $p_{1},p_{2},\ldots ,p_{n},$ this gives the number

$N=1+p_{1}\cdot p_{2}\cdots p_{n}.$

By the fundamental theorem of arithmetic, ⁠ N ⁠ has a prime factorization

$N=p'_{1}\cdot p'_{2}\cdots p'_{m}$

with one or more prime factors. ⁠ N ⁠ is evenly divisible by each of these factors, but ⁠ N ⁠ has a remainder of one when divided by any of the prime numbers in the given list, so none of the prime factors of ⁠ N ⁠ can be in the given list. Because there is no finite list of all the primes, there must be infinitely many primes.

The numbers formed by adding one to the products of the smallest primes are called Euclid numbers. The first five of them are prime, but the sixth,

$1+{\big (}2\cdot 3\cdot 5\cdot 7\cdot 11\cdot 13{\big )}=30031=59\cdot 509,$

is a composite number.

### Formulas for primes

There is no known efficient formula for primes. For example, there is no non-constant polynomial, even in several variables, that takes only prime values. However, there are numerous expressions that do encode all primes, or only primes. One possible formula is based on Wilson's theorem and generates the number 2 many times and all other primes exactly once. There is also a set of Diophantine equations in nine variables and one parameter with the following property: the parameter is prime if and only if the resulting system of equations has a solution over the natural numbers. This can be used to obtain a single formula with the property that all its positive values are prime.

Other examples of prime-generating formulas come from Mills' theorem and a theorem of Wright. These assert that there are real constants $A>1$ and $\mu$ such that

$\left\lfloor A^{3^{n}}\right\rfloor {\text{ and }}\left\lfloor 2^{\cdots ^{2^{2^{\mu }}}}\right\rfloor$

are prime for any natural number ⁠ n ⁠ in the first formula, and any number of exponents in the second formula. Here $\lfloor {}\cdot {}\rfloor$ represents the floor function, the largest integer less than or equal to the number in question. However, these are not useful for generating primes, as the primes must be generated first in order to compute the values of ⁠ A ⁠ or $\mu .$

### Open questions

Many conjectures revolving about primes have been posed. Often having an elementary formulation, many of these conjectures have withstood proof for decades: all four of Landau's problems from 1912 are still unsolved. One of them is Goldbach's conjecture, which asserts that every even integer ⁠ n ⁠ greater than ⁠ 2 ⁠ can be written as a sum of two primes. As of 2014, this conjecture has been verified for all numbers up to $n=4\cdot 10^{18}.$ Weaker statements than this have been proven; for example, Vinogradov's theorem says that every sufficiently large odd integer can be written as a sum of three primes. Chen's theorem says that every sufficiently large even number can be expressed as the sum of a prime and a semiprime (the product of two primes). Also, any even integer greater than 10 can be written as the sum of six primes. The branch of number theory studying such questions is called additive number theory.

Another type of problem concerns prime gaps, the differences between consecutive primes. The existence of arbitrarily large prime gaps can be seen by noting that the sequence $n!+2,n!+3,\dots ,n!+n$ consists of $n-1$ composite numbers, for any natural number $n.$ However, large prime gaps occur much earlier than this argument shows. For example, the first prime gap of length 8 is between the primes 89 and 97, much smaller than $8!=40320.$ It is conjectured that there are infinitely many twin primes, pairs of primes with difference 2; this is the twin prime conjecture. Polignac's conjecture states more generally that for every positive integer $k,$ there are infinitely many pairs of consecutive primes that differ by $2k.$ Andrica's conjecture, Brocard's conjecture, Legendre's conjecture, and Oppermann's conjecture all suggest that the largest gaps between primes from 1 to ⁠ n ⁠ should be at most approximately ${\sqrt {n}},$ a result that is known to follow from the Riemann hypothesis, while the much stronger Cramér conjecture sets the largest gap size at ⁠ $O((\log n)^{2})$ ⁠. Prime gaps can be generalized to prime ⁠ k ⁠-tuples, patterns in the differences among more than two prime numbers. Their infinitude and density are the subject of the first Hardy–Littlewood conjecture, which can be motivated by the heuristic that the prime numbers behave similarly to a random sequence of numbers with density given by the prime number theorem.


## Analytic properties

Analytic number theory studies number theory through the lens of continuous functions, limits, infinite series, and the related mathematics of the infinite and infinitesimal.

This area of study began with Leonhard Euler and his first major result, the solution to the Basel problem. The problem asked for the value of the infinite sum $1+{\tfrac {1}{4}}+{\tfrac {1}{9}}+{\tfrac {1}{16}}+\dots ,$ which today can be recognized as the value $\zeta (2)$ of the Riemann zeta function. This function is closely connected to the prime numbers and to one of the most significant unsolved problems in mathematics, the Riemann hypothesis. Euler showed that ⁠ $\zeta (2)=\pi ^{2}/6$ ⁠. The reciprocal of this number, ⁠ $6/\pi ^{2}$ ⁠, is the limiting probability that two random numbers selected uniformly from a large range are relatively prime (have no factors in common).

The distribution of primes in the large, such as the question how many primes are smaller than a given, large threshold, is described by the prime number theorem, but no efficient formula for the ⁠ n ⁠-th prime is known. Dirichlet's theorem on arithmetic progressions, in its basic form, asserts that linear polynomials

$p(n)=a+bn$

with relatively prime integers ⁠ a ⁠ and ⁠ b ⁠ take infinitely many prime values. Although conjectures have been formulated about the proportions of primes in higher-degree polynomials, they remain unproven, and it is unknown whether there exists a quadratic polynomial that (for integer arguments) is prime infinitely often.

### Analytical proof of Euclid's theorem

Euler's proof that there are infinitely many primes considers the sums of reciprocals of primes,

${\frac {1}{2}}+{\frac {1}{3}}+{\frac {1}{5}}+{\frac {1}{7}}+\cdots +{\frac {1}{p}}.$

Euler showed that, for any arbitrary real number ⁠ x ⁠, there exists a prime ⁠ p ⁠ for which this sum is greater than ⁠ x ⁠. This shows that there are infinitely many primes, because if there were finitely many primes the sum would reach its maximum value at the biggest prime rather than growing past every ⁠ x ⁠. The growth rate of this sum is described more precisely by Mertens' second theorem. For comparison, the sum

${\frac {1}{1^{2}}}+{\frac {1}{2^{2}}}+{\frac {1}{3^{2}}}+\cdots +{\frac {1}{n^{2}}}$

does not grow to infinity as ⁠ n ⁠ goes to infinity (see the Basel problem). In this sense, prime numbers occur more often than squares of natural numbers, although both sets are infinite. Brun's theorem states that the sum of the reciprocals of twin primes,

$\left({{\frac {1}{3}}+{\frac {1}{5}}}\right)+\left({{\frac {1}{5}}+{\frac {1}{7}}}\right)+\left({{\frac {1}{11}}+{\frac {1}{13}}}\right)+\cdots ,$

is finite. Because of Brun's theorem, it is not possible to use Euler's method to solve the twin prime conjecture, that there exist infinitely many twin primes.

### Number of primes below a given bound

The prime-counting function $\pi (n)$ is defined as the number of primes not greater than ⁠ n ⁠. For example, ⁠ $\pi (11)=5$ ⁠, since there are five primes less than or equal to 11. Methods such as the Meissel–Lehmer algorithm can compute exact values of $\pi (n)$ faster than it would be possible to list each prime up to ⁠ n ⁠. The prime number theorem states that $\pi (n)$ is asymptotic to ⁠ $n/\log n$ ⁠, which is denoted as

$\pi (n)\sim {\frac {n}{\log n}},$

and means that the ratio of $\pi (n)$ to the right-hand fraction approaches 1 as ⁠ n ⁠ grows to infinity. This implies that the likelihood that a randomly chosen number less than ⁠ n ⁠ is prime is (approximately) inversely proportional to the number of digits in ⁠ n ⁠. It also implies that the ⁠ n ⁠th prime number is proportional to $n\log n$ and therefore that the average size of a prime gap is proportional to ⁠ $\log n$ ⁠. A more accurate estimate for $\pi (n)$ is given by the offset logarithmic integral

$\pi (n)\sim \operatorname {Li} (n)=\int _{2}^{n}{\frac {dt}{\log t}}.$

### Arithmetic progressions

An arithmetic progression is a finite or infinite sequence of numbers such that consecutive numbers in the sequence all have the same difference. This difference is called the modulus of the progression. For example,

$3,12,21,30,39,...,$

is an infinite arithmetic progression with modulus 9. In an arithmetic progression, all the numbers have the same remainder when divided by the modulus; in this example, the remainder is 3. Because both the modulus 9 and the remainder 3 are multiples of 3, so is every element in the sequence. Therefore, this progression contains only one prime number, 3 itself. In general, the infinite progression

$a,a+q,a+2q,a+3q,\dots$

can have more than one prime only when its remainder ⁠ a ⁠ and modulus ⁠ q ⁠ are relatively prime. If they are relatively prime, Dirichlet's theorem on arithmetic progressions asserts that the progression contains infinitely many primes.

Primes in the arithmetic progressions modulo 9. Each row of the thin horizontal band shows one of the nine possible progressions mod 9, with prime numbers marked in red. The progressions of numbers that are 0, 3, or 6 mod 9 contain at most one prime number (the number 3); the remaining progressions of numbers that are 1, 2, 4, 5, 7, and 8 mod 9 have infinitely many prime numbers, with similar numbers of primes in each progression.

The Green–Tao theorem shows that there are arbitrarily long finite arithmetic progressions consisting only of primes.

### Prime values of quadratic polynomials

Euler noted that the function

$n^{2}-n+41$

yields prime numbers for ⁠ $1\leq n\leq 40$ ⁠, although composite numbers appear among its later values. The search for an explanation for this phenomenon led to the deep algebraic number theory of Heegner numbers and the class number problem. The Hardy–Littlewood conjecture F predicts the density of primes among the values of quadratic polynomials with integer coefficients in terms of the logarithmic integral and the polynomial coefficients. No quadratic polynomial has been proven to take infinitely many prime values.

The Ulam spiral arranges the natural numbers in a two-dimensional grid, spiraling in concentric squares surrounding the origin with the prime numbers highlighted. Visually, the primes appear to cluster on certain diagonals and not others, suggesting that some quadratic polynomials take prime values more often than others.

Russian mathematician Viktor Bunyakovsky in 1857 conjectured that any one-variable polynomial $f(x)$ with integer coefficients would produce infinitely many primes in the sequence $f(1),f(2),f(3),\dots$ . A polynomial must meet the conditions that its leading coefficient is positive, it is irreducible over the rationals, and the value of such a sequence has no common factor larger than 1. This conjecture was generalized by Polish mathematician Andrzej Schinzel's hypothesis H, and later extended to multivariable polynomials in Dickson's conjecture and then Bateman–Horn conjecture.

### Zeta function and the Riemann hypothesis

One of the most famous unsolved questions in mathematics, dating from 1859, and one of the Millennium Prize Problems, is the Riemann hypothesis, which asks where the zeros of the Riemann zeta function $\zeta (s)$ are located. This function is an analytic function on the complex numbers. For complex numbers ⁠ s ⁠ with real part greater than one it equals both an infinite sum over all integers, and an infinite product over the prime numbers, $\zeta (s)=\sum _{n=1}^{\infty }{\frac {1}{n^{s}}}=\prod _{p{\text{ prime}}}{\frac {1}{1-p^{-s}}}.$ This equality between a sum and a product, discovered by Euler, is called an Euler product. The Euler product can be derived from the fundamental theorem of arithmetic, and shows the close connection between the zeta function and the prime numbers. It leads to another proof that there are infinitely many primes: if there were only finitely many, then the sum-product equality would also be valid at ⁠ $s=1$ ⁠, but the sum would diverge (it is the harmonic series ⁠ $1+{\tfrac {1}{2}}+{\tfrac {1}{3}}+\dots$ ⁠) while the product would be finite, a contradiction.

The Riemann hypothesis states that the zeros of the zeta-function are all either negative even numbers, or complex numbers with real part equal to 1/2. The original proof of the prime number theorem was based on a weak form of this hypothesis, that there are no zeros with real part equal to 1, although other more elementary proofs have been found. The prime-counting function can be expressed by Riemann's explicit formula as a sum in which each term comes from one of the zeros of the zeta function; the main term of this sum is the logarithmic integral, and the remaining terms cause the sum to fluctuate above and below the main term. In this sense, the zeros control how regularly the prime numbers are distributed. If the Riemann hypothesis is true, these fluctuations will be small, and the asymptotic distribution of primes given by the prime number theorem will also hold over much shorter intervals (of length about the square root of ⁠ x ⁠ for intervals near a number ⁠ x ⁠).


## Abstract algebra

### Modular arithmetic and finite fields

Modular arithmetic modifies usual arithmetic by only using the numbers ⁠ $\{0,1,2,\dots ,n-1\}$ ⁠, for a natural number ⁠ n ⁠ called the modulus. Any other natural number can be mapped into this system by replacing it by its remainder after division by ⁠ n ⁠. Modular sums, differences and products are calculated by performing the same replacement by the remainder on the result of the usual sum, difference, or product of integers. Equality of integers corresponds to *congruence* in modular arithmetic: ⁠ x ⁠ and ⁠ y ⁠ are congruent (written $x\equiv y$ mod ⁠ n ⁠) when they have the same remainder after division by ⁠ n ⁠. In this system of numbers, division by all nonzero numbers is possible if and only if the modulus is prime. For instance, with the prime number 7 as modulus, division by 3 is possible: ⁠ $2/3\equiv 3{\bmod {7}}$ ⁠, because clearing denominators by multiplying both sides by 3 gives the valid formula ⁠ $2\equiv 9{\bmod {7}}$ ⁠. However, with the composite modulus 6, division by 3 is impossible. There is no valid solution to $2/3\equiv x{\bmod {6}}$ : clearing denominators by multiplying by 3 causes the left-hand side to become 2 while the right-hand side becomes either 0 or 3. In the terminology of abstract algebra, the ability to perform division means that modular arithmetic modulo a prime number forms a field or, more specifically, a finite field, while other moduli only give a ring but not a field.

Several theorems about primes can be formulated using modular arithmetic. For instance, Fermat's little theorem states that if $a\not \equiv 0$ (mod ⁠ p ⁠), then $a^{p-1}\equiv 1$ (mod ⁠ p ⁠). Summing this over all choices of ⁠ a ⁠ gives the equation

$\sum _{a=1}^{p-1}a^{p-1}\equiv (p-1)\cdot 1\equiv -1{\pmod {p}},$

valid whenever ⁠ p ⁠ is prime. Giuga's conjecture says that this equation is also a sufficient condition for ⁠ p ⁠ to be prime. Wilson's theorem says that an integer $p>1$ is prime if and only if the factorial $(p-1)!$ is congruent to $-1$ mod ⁠ p ⁠. For a composite number ⁠ $n=r\cdot s$ ⁠ this cannot hold, since one of its factors divides both n and ⁠ $(n-1)!$ ⁠, and so $(n-1)!\equiv -1{\pmod {n}}$ is impossible.

### *p*-adic numbers

The ⁠ p ⁠-adic order $\nu _{p}(n)$ of an integer ⁠ n ⁠ is the number of copies of ⁠ p ⁠ in the prime factorization of ⁠ n ⁠. The same concept can be extended from integers to rational numbers by defining the ⁠ p ⁠-adic order of a fraction $m/n$ to be ⁠ $\nu _{p}(m)-\nu _{p}(n)$ ⁠. The ⁠ p ⁠-adic absolute value $|q|_{p}$ of any rational number ⁠ q ⁠ is then defined as ⁠ $\vert q\vert _{p}=p^{-\nu _{p}(q)}$ ⁠. Multiplying an integer by its ⁠ p ⁠-adic absolute value cancels out the factors of ⁠ p ⁠ in its factorization, leaving only the other primes. Just as the distance between two real numbers can be measured by the absolute value of their difference, the distance between two rational numbers can be measured by their ⁠ p ⁠-adic distance, the ⁠ p ⁠-adic absolute value of their difference. For this definition of distance, two numbers are close together (they have a small distance) when their difference is divisible by a high power of ⁠ p ⁠. In the same way that the real numbers can be formed from the rational numbers and their distances, by adding extra limiting values to form a complete field, the rational numbers with the ⁠ p ⁠-adic distance can be extended to a different complete field, the ⁠ p ⁠-adic numbers.

This picture of an order, absolute value, and complete field derived from them can be generalized to algebraic number fields and their valuations (certain mappings from the multiplicative group of the field to a totally ordered additive group, also called orders), absolute values (certain multiplicative mappings from the field to the real numbers, also called norms), and places (extensions to complete fields in which the given field is a dense set, also called completions). The extension from the rational numbers to the real numbers, for instance, is a place in which the distance between numbers is the usual absolute value of their difference. The corresponding mapping to an additive group would be the logarithm of the absolute value, although this does not meet all the requirements of a valuation. According to Ostrowski's theorem, up to a natural notion of equivalence, the real numbers and ⁠ p ⁠-adic numbers, with their orders and absolute values, are the only valuations, absolute values, and places on the rational numbers. The local–global principle allows certain problems over the rational numbers to be solved by piecing together solutions from each of their places, again underlining the importance of primes to number theory.

### Prime elements of a ring

A commutative ring is an algebraic structure where addition, subtraction and multiplication are defined. The integers are a ring, and the prime numbers in the integers have been generalized to rings in two different ways, *prime elements* and *irreducible elements*. An element ⁠ p ⁠ of a ring ⁠ R ⁠ is called prime if it is nonzero, has no multiplicative inverse (that is, it is not a unit), and satisfies the following requirement: whenever ⁠ p ⁠ divides the product $xy$ of two elements of ⁠ R ⁠, it also divides at least one of ⁠ x ⁠ or ⁠ y ⁠. An element is irreducible if it is neither a unit nor the product of two other non-unit elements. In the ring of integers, the prime and irreducible elements form the same set,

$\{\dots ,-11,-7,-5,-3,-2,2,3,5,7,11,\dots \}\,.$

In an arbitrary ring, all prime elements are irreducible. The converse does not hold in general, but does hold for unique factorization domains.

The fundamental theorem of arithmetic continues to hold (by definition) in unique factorization domains. An example of such a domain is the Gaussian integers ⁠ $\mathbb {Z} [i]$ ⁠, the ring of complex numbers of the form $a+bi$ where ⁠ i ⁠ denotes the imaginary unit and ⁠ a ⁠ and ⁠ b ⁠ are arbitrary integers. Its prime elements are known as Gaussian primes. Not every number that is prime among the integers remains prime in the Gaussian integers; for instance, the number 2 can be written as a product of the two Gaussian primes $1+i$ and ⁠ $1-i$ ⁠. Rational primes (the prime elements in the integers) congruent to 3 mod 4 are Gaussian primes, but rational primes congruent to 1 mod 4 are not. This is a consequence of Fermat's theorem on sums of two squares, which states that an odd prime ⁠ p ⁠ is expressible as the sum of two squares, ⁠ $p=x^{2}+y^{2}$ ⁠, and therefore factorable as ⁠ $p=(x+iy)(x-iy)$ ⁠, exactly when ⁠ p ⁠ is 1 mod 4.

### Prime ideals

Not every ring is a unique factorization domain. For instance, in the ring of numbers $a+b{\sqrt {-5}}$ (for integers ⁠ a ⁠ and ⁠ b ⁠) the number $21$ has two factorizations ⁠ $21=3\cdot 7=(1+2{\sqrt {-5}})(1-2{\sqrt {-5}})$ ⁠, where none of the four factors can be reduced any further, so it does not have a unique factorization. In order to extend unique factorization to a larger class of rings, the notion of a number can be replaced with that of an ideal, a subset of the elements of a ring that contains all sums of pairs of its elements, and all products of its elements with ring elements. *Prime ideals*, which generalize prime elements in the sense that the principal ideal generated by a prime element is a prime ideal, are an important tool and object of study in commutative algebra, algebraic number theory and algebraic geometry. The prime ideals of the ring of integers are the ideals ⁠ $(0)$ ⁠, ⁠ $(2)$ ⁠, ⁠ $(3)$ ⁠, ⁠ $(5)$ ⁠, ⁠ $(7)$ ⁠, ⁠ $(11)$ ⁠, ... The fundamental theorem of arithmetic generalizes to the Lasker–Noether theorem, which expresses every ideal in a Noetherian commutative ring as an intersection of primary ideals, which are the appropriate generalizations of prime powers.

The spectrum of a ring is a geometric space whose points are the prime ideals of the ring. Arithmetic geometry also benefits from this notion, and many concepts exist in both geometry and number theory. For example, factorization or ramification of prime ideals when lifted to an extension field, a basic problem of algebraic number theory, bears some resemblance with ramification in geometry. These concepts can even assist with in number-theoretic questions solely concerned with integers. For example, prime ideals in the ring of integers of quadratic number fields can be used in proving quadratic reciprocity, a statement that concerns the existence of square roots modulo integer prime numbers. Early attempts to prove Fermat's Last Theorem led to Kummer's introduction of regular primes, integer prime numbers connected with the failure of unique factorization in the cyclotomic integers. The question of how many integer prime numbers factor into a product of multiple prime ideals in an algebraic number field is addressed by Chebotarev's density theorem, which (when applied to the cyclotomic integers) has Dirichlet's theorem on primes in arithmetic progressions as a special case.

### Group theory

In the theory of finite groups the Sylow theorems imply that, if a power of a prime number $p^{n}$ divides the order of a group, then the group has a subgroup of order ⁠ $p^{n}$ ⁠. By Lagrange's theorem, any group of prime order is a cyclic group, and by Burnside's theorem any group whose order is divisible by only two primes is solvable.
