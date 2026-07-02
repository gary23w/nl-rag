---
title: "Prime number (part 2/2)"
source: https://en.wikipedia.org/wiki/Prime_number
domain: number-theory
license: CC-BY-SA-4.0
tags: number theory, modular arithmetic, prime number, gcd
fetched: 2026-07-02
part: 2/2
---

## Computational methods

For a long time, number theory in general, and the study of prime numbers in particular, was seen as the canonical example of pure mathematics, with no applications outside of mathematics other than the use of prime numbered gear teeth to distribute wear evenly. In particular, number theorists such as British mathematician G. H. Hardy prided themselves on doing work that had absolutely no military significance.

This vision of the purity of number theory was shattered in the 1970s, when it was publicly announced that prime numbers could be used as the basis for the creation of public-key cryptography algorithms. These applications have led to significant study of algorithms for computing with prime numbers, and in particular of primality testing, methods for determining whether a given number is prime. The most basic primality testing routine, trial division, is too slow to be useful for large numbers. One group of modern primality tests is applicable to arbitrary numbers, while more efficient tests are available for numbers of special types. Most primality tests only tell whether their argument is prime or not. Routines that also provide a prime factor of composite arguments (or all of its prime factors) are called factorization algorithms. Prime numbers are also used in computing for checksums, hash tables, and pseudorandom number generators.

### Trial division

The most basic method of checking the primality of a given integer ⁠ n ⁠ is called *trial division*. This method divides ⁠ n ⁠ by each integer from 2 up to the square root of ⁠ n ⁠. Any such integer dividing ⁠ n ⁠ evenly establishes ⁠ n ⁠ as composite; otherwise it is prime. Integers larger than the square root do not need to be checked because, whenever ⁠ $n=a\cdot b$ ⁠, one of the two factors ⁠ a ⁠ and ⁠ b ⁠ is less than or equal to the square root of ⁠ n ⁠. Another optimization is to check only primes as factors in this range. For instance, to check whether 37 is prime, this method divides it by the primes in the range from 2 to ⁠ ${\sqrt {37}}$ ⁠, which are 2, 3, and 5. Each division produces a nonzero remainder, so 37 is indeed prime.

Although this method is simple to describe, it is impractical for testing the primality of large integers, because the number of tests that it performs grows exponentially as a function of the number of digits of these integers. However, trial division is still used, with a smaller limit than the square root on the divisor size, to quickly discover composite numbers with small factors, before using more complicated methods on the numbers that pass this filter.

### Sieves

Before computers, mathematical tables listing all of the primes or prime factorizations up to a given limit were commonly printed. The oldest known method for generating a list of primes is called the sieve of Eratosthenes. The animation shows an optimized variant of this method. Another more asymptotically efficient sieving method for the same problem is the sieve of Atkin. In advanced mathematics, sieve theory applies similar methods to other problems.

### Primality testing versus primality proving

Some of the fastest modern tests for whether an arbitrary given number ⁠ n ⁠ is prime are probabilistic (or Monte Carlo) algorithms, meaning that they have a small random chance of producing an incorrect answer. For instance the Solovay–Strassen primality test on a given number ⁠ p ⁠ chooses a number ⁠ a ⁠ randomly from 2 through $p-2$ and uses modular exponentiation to check whether $a^{(p-1)/2}\pm 1$ is divisible by ⁠ p ⁠. If so, it answers yes and otherwise it answers no. If ⁠ p ⁠ really is prime, it will always answer yes, but if ⁠ p ⁠ is composite then it answers yes with probability at most 1/2 and no with probability at least 1/2. If this test is repeated ⁠ n ⁠ times on the same number, the probability that a composite number could pass the test every time is at most ⁠ $1/2^{n}$ ⁠. Because this decreases exponentially with the number of tests, it provides high confidence (although not certainty) that a number that passes the repeated test is prime. On the other hand, if the test ever fails, then the number is certainly composite. A composite number that passes such a test is called a pseudoprime.

In contrast, some other algorithms guarantee that their answer will always be correct: primes will always be determined to be prime and composites will always be determined to be composite. For instance, this is true of trial division. The algorithms with guaranteed-correct output include both deterministic (non-random) algorithms, such as the AKS primality test, and randomized Las Vegas algorithms where the random choices made by the algorithm do not affect its final answer, such as some variations of elliptic curve primality proving. When the elliptic curve method concludes that a number is prime, it provides primality certificate that can be verified quickly. The elliptic curve primality test is the fastest in practice of the guaranteed-correct primality tests, but has only heuristic arguments for its fast performance rather than rigorous proofs. The AKS primality test is proven to run in polynomial time, but with a higher polynomial exponent, making it slower in practice than the elliptic curve test. These methods can be used to generate large random prime numbers, by generating and testing random numbers until finding one that is prime; when doing this, a faster probabilistic test can quickly eliminate most composite numbers before a guaranteed-correct algorithm is used to verify that the remaining numbers are prime.

The following table lists some of these tests. Their running time is given in terms of ⁠ n ⁠, the number to be tested and, for probabilistic algorithms, the number ⁠ k ⁠ of tests performed. Moreover, $\varepsilon$ is an arbitrarily small positive number, and log is the logarithm to an unspecified base. The big O notation means that each time bound should be multiplied by a constant factor to convert it from dimensionless units to units of time; this factor depends on implementation details such as the type of computer used to run the algorithm, but not on the input parameters ⁠ n ⁠ and ⁠ k ⁠.

| Test | Developed in | Type | Running time | Notes | References |
|---|---|---|---|---|---|
| AKS primality test | 2002 | deterministic | $O((\log n)^{6+\varepsilon })$ |   |   |
| Elliptic curve primality proving | 1986 | Las Vegas | $O((\log n)^{4+\varepsilon })$ *heuristically* |   |   |
| Baillie–PSW primality test | 1980 | Monte Carlo | $O((\log n)^{2+\varepsilon })$ |   |   |
| Miller–Rabin primality test | 1980 | Monte Carlo | $O(k(\log n)^{2+\varepsilon })$ | error probability $4^{-k}$ |   |
| Solovay–Strassen primality test | 1977 | Monte Carlo | $O(k(\log n)^{2+\varepsilon })$ | error probability $2^{-k}$ |   |

### Special-purpose algorithms and the largest known prime

In addition to the aforementioned tests that apply to any natural number, some numbers of a special form can be tested for primality more quickly. For example, the Lucas–Lehmer primality test can determine whether a Mersenne number (one less than a power of two) is prime, deterministically, in the same time as a single iteration of the Miller–Rabin test. This is why since 1992 (as of October 2024) the largest *known* prime has always been a Mersenne prime. It is conjectured that there are infinitely many Mersenne primes.

The following table gives the largest known primes of various types. Some of these primes have been found using distributed computing. In 2009, the Great Internet Mersenne Prime Search project was awarded a US$100,000 prize for first discovering a prime with at least 10 million digits. The Electronic Frontier Foundation also offers $150,000 and $250,000 for primes with at least 100 million digits and 1 billion digits, respectively.

| Type | Prime | Number of decimal digits | Date | Found by |
|---|---|---|---|---|
| Mersenne prime | 2136,279,841 − 1 | 41,024,320 | October 12, 2024 | Luke Durant, Great Internet Mersenne Prime Search |
| Proth prime | 10,223 × 231,172,165 + 1 | 9,383,761 | October 31, 2016 | Péter Szabolcs, PrimeGrid |
| factorial prime | 208,003! − 1 | 1,015,843 | July 2016 | Sou Fukui |
| primorial prime | 1,098,133# − 1 | 476,311 | March 2012 | James P. Burt, PrimeGrid |
| twin primes | 2,996,863,034,895 × 21,290,000 ± 1 | 388,342 | September 2016 | Tom Greer, PrimeGrid |

### Integer factorization

Given a composite integer ⁠ n ⁠, the task of providing one (or all) prime factors is referred to as *factorization* of ⁠ n ⁠. It is significantly more difficult than primality testing, and although many factorization algorithms are known, they are slower than the fastest primality testing methods. Trial division and Pollard's rho algorithm can be used to find very small factors of ⁠ n ⁠, and elliptic curve factorization can be effective when ⁠ n ⁠ has factors of moderate size. Methods suitable for arbitrary large numbers that do not depend on the size of its factors include the quadratic sieve and general number field sieve. As with primality testing, there are also factorization algorithms that require their input to have a special form, including the special number field sieve. As of December 2019 the largest number known to have been factored by a general-purpose algorithm is RSA-240, which has 240 decimal digits (795 bits) and is the product of two large primes.

Shor's algorithm can factor any integer in a polynomial number of steps on a quantum computer. However, current technology can only run this algorithm for very small numbers. As of October 2012, the largest number that has been factored by a quantum computer running Shor's algorithm is 21.

### Other computational applications

Several public-key cryptography algorithms, such as RSA and the Diffie–Hellman key exchange, are based on large prime numbers (2048-bit primes are common). RSA relies on the assumption that it is much easier (that is, more efficient) to perform the multiplication of two (large) numbers ⁠ x ⁠ and ⁠ y ⁠ than to calculate ⁠ x ⁠ and ⁠ y ⁠ (assumed coprime) if only the product $xy$ is known. The Diffie–Hellman key exchange relies on the fact that there are efficient algorithms for modular exponentiation (computing ⁠ $a^{b}{\bmod {c}}$ ⁠), while the reverse operation (the discrete logarithm) is thought to be a hard problem.

Prime numbers are frequently used for hash tables. For instance the original method of Carter and Wegman for universal hashing was based on computing hash functions by choosing random linear functions modulo large prime numbers. Carter and Wegman generalized this method to ⁠ k ⁠-independent hashing by using higher-degree polynomials, again modulo large primes. As well as in the hash function, prime numbers are used for the hash table size in quadratic probing based hash tables to ensure that the probe sequence covers the whole table.

Some checksum methods are based on the mathematics of prime numbers. For instance the checksums used in International Standard Book Numbers are defined by taking the rest of the number modulo 11, a prime number. Because 11 is prime this method can detect both single-digit errors and transpositions of adjacent digits. Another checksum method, Adler-32, uses arithmetic modulo 65521, the largest prime number less than ⁠ $2^{16}$ ⁠. Prime numbers are also used in pseudorandom number generators including linear congruential generators and the Mersenne Twister.


## Other applications

Prime numbers are of central importance to number theory but also have many applications to other areas within mathematics, including abstract algebra and elementary geometry. For example, it is possible to place prime numbers of points in a two-dimensional grid so that no three are in a line, or so that every triangle formed by three of the points has large area. Another example is Eisenstein's criterion, a test for whether a polynomial is irreducible based on divisibility of its coefficients by a prime number and its square.

The concept of a prime number is so important that it has been generalized in different ways in various branches of mathematics. Generally, "prime" indicates minimality or indecomposability, in an appropriate sense. For example, the prime field of a given field is its smallest subfield that contains both 0 and 1. It is either the field of rational numbers or a finite field with a prime number of elements, whence the name. Often a second, additional meaning is intended by using the word prime, namely that any object can be, essentially uniquely, decomposed into its prime components. For example, in knot theory, a prime knot is a knot that is indecomposable in the sense that it cannot be written as the connected sum of two nontrivial knots. Any knot can be uniquely expressed as a connected sum of prime knots. The prime decomposition of 3-manifolds is another example of this type.

Beyond mathematics and computing, prime numbers have potential connections to quantum mechanics, and have been used metaphorically in the arts and literature. They have also been used in evolutionary biology to explain the life cycles of cicadas.

### Constructible polygons and polygon partitions

Fermat primes are primes of the form

$F_{k}=2^{2^{k}}+1,$

with ⁠ k ⁠ a nonnegative integer. They are named after Pierre de Fermat, who conjectured that all such numbers are prime. The first five of these numbers – 3, 5, 17, 257, and 65,537 – are prime, but $F_{5}$ is composite and so are all other Fermat numbers that have been verified as of 2017. A regular ⁠ n ⁠-gon is constructible using straightedge and compass if and only if the odd prime factors of ⁠ n ⁠ (if any) are distinct Fermat primes. Likewise, a regular ⁠ n ⁠-gon may be constructed using straightedge, compass, and an angle trisector if and only if the prime factors of ⁠ n ⁠ are any number of copies of 2 or 3 together with a (possibly empty) set of distinct Pierpont primes, primes of the form ⁠ $2^{a}3^{b}+1$ ⁠.

It is possible to partition any convex polygon into ⁠ n ⁠ smaller convex polygons of equal area and equal perimeter, when ⁠ n ⁠ is a power of a prime number, but this is not known for other values of ⁠ n ⁠.

### Quantum mechanics

Beginning with the work of Hugh Montgomery and Freeman Dyson in the 1970s, mathematicians and physicists have speculated that the zeros of the Riemann zeta function are connected to the energy levels of quantum systems. Prime numbers are also significant in quantum information science, thanks to mathematical structures such as mutually unbiased bases and symmetric informationally complete positive-operator-valued measures.

### Biology

The evolutionary strategy used by cicadas of the genus *Magicicada* makes use of prime numbers. These insects spend most of their lives as grubs underground. They only pupate and then emerge from their burrows after 7, 13 or 17 years, at which point they fly about, breed, and then die after a few weeks at most. Biologists theorize that these prime-numbered breeding cycle lengths have evolved in order to prevent predators from synchronizing with these cycles. In contrast, the multi-year periods between flowering in bamboo plants are hypothesized to be smooth numbers, having only small prime numbers in their factorizations.

### Arts and literature

Prime numbers have influenced many artists and writers. The French composer Olivier Messiaen used prime numbers to create ametrical music through "natural phenomena". In works such as *La Nativité du Seigneur* (1935) and *Quatre études de rythme* (1949–1950), he simultaneously employs motifs with lengths given by different prime numbers to create unpredictable rhythms: the primes 41, 43, 47 and 53 appear in the third étude, "Neumes rythmiques". According to Messiaen this way of composing was "inspired by the movements of nature, movements of free and unequal durations".

In his science fiction novel *Contact*, scientist Carl Sagan suggested that prime factorization could be used as a means of establishing two-dimensional image planes in communications with aliens, an idea that he had first developed informally with American astronomer Frank Drake in 1975. In the novel *The Curious Incident of the Dog in the Night-Time* by Mark Haddon, the narrator arranges the sections of the story by consecutive prime numbers as a way to convey the mental state of its main character, a mathematically gifted teen with Asperger syndrome. Prime numbers are used as a metaphor for loneliness and isolation in the Paolo Giordano novel *The Solitude of Prime Numbers*, in which they are portrayed as "outsiders" among integers. The 1992 caper movie *Sneakers* features a fictional method for quickly factoring large numbers into primes, thereby breaking computer encryption systems.
