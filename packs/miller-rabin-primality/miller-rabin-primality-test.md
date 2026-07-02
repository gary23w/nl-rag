---
title: "Miller–Rabin primality test"
source: https://en.wikipedia.org/wiki/Miller–Rabin_primality_test
domain: miller-rabin-primality
license: CC-BY-SA-4.0
tags: miller rabin primality test, probabilistic primality test, fermat little theorem, carmichael number
fetched: 2026-07-02
---

# Miller–Rabin primality test

The **Miller–Rabin primality test** or **Rabin–Miller primality test** is a probabilistic primality test: an algorithm which determines whether a given number is likely to be prime, similar to the Fermat primality test and the Solovay–Strassen primality test.

It is of historical significance in the search for a polynomial-time deterministic primality test. Its probabilistic variant remains widely used in practice, as one of the simplest and fastest tests known.

Gary L. Miller discovered the test in 1976. Miller's version of the test is deterministic, but its correctness relies on the unproven extended Riemann hypothesis. Michael O. Rabin modified it to obtain an unconditional probabilistic algorithm in 1980.

## Mathematical concepts

Similarly to the Fermat and Solovay–Strassen tests, the Miller–Rabin primality test checks whether a specific property, which is known to hold for prime values, holds for the number under testing.

### Strong probable primes

The property is the following. For a given odd integer $n>2$ , let’s write $n-1$ as $2^{s}d$ where s is a positive integer and d is an odd positive integer. Let’s consider an integer  a , called a *base*, which is coprime to n . Then, n is said to be a **strong probable prime to base *a*** if one of these congruence relations holds:

- $a^{d}\equiv 1\!\!\!{\pmod {n}}$ , or
- $a^{2^{r}d}\equiv -1\!\!\!{\pmod {n}}$ for some $0\leq r<s$ .

This simplifies to first checking for $a^{d}\equiv 1{\pmod {n}}$ and then $a^{2^{r}d}\equiv n-1{\pmod {n}}$ for successive values of r . For each value of r , the value of the expression may be calculated using the value obtained for the previous value of r by squaring under the modulus of n .

The idea beneath this test is that when n is an odd prime, it passes the test because of two facts:

- by Fermat's little theorem, $a^{n-1}\equiv 1{\pmod {n}}$ (this property alone defines the weaker notion of *probable prime to base* a , on which the Fermat test is based);
- the only square roots of 1 modulo n are 1 and −1.

Hence, by contraposition, if n is not a strong probable prime to base a , then n is definitely composite, and a is called a **witness** for the compositeness of n .

However, this property is not an exact characterization of prime numbers. If n is composite, it may nonetheless be a strong probable prime to base a , in which case it is called a **strong pseudoprime**, and a is a **strong liar**.

### Choices of bases

No composite number is a strong pseudoprime to all bases at the same time (contrary to the Fermat primality test for which Fermat pseudoprimes to all bases exist: the Carmichael numbers). However no simple way of finding a witness is known. A naïve solution is to try all possible bases, which yields an inefficient deterministic algorithm. The Miller test is a more efficient variant of this (see section *Miller test* below).

Another solution is to pick a base at random. This yields a fast probabilistic test. When *n* is composite, most bases are witnesses, so the test will detect *n* as composite with a reasonably high probability (see section *Accuracy* below). We can quickly reduce the probability of a false positive to an arbitrarily small rate, by combining the outcome of as many independently chosen bases as necessary to achieve the said rate. This is the Miller–Rabin test. There seems to be diminishing returns in trying many bases, because if *n* is a pseudoprime to some base, then it seems more likely to be a pseudoprime to another base.

Note that *a**d* ≡ 1 (mod *n*) holds trivially for *a* ≡ 1 (mod *n*), because the congruence relation is compatible with exponentiation. And *a**d* = *a*20*d* ≡ −1 (mod *n*) holds trivially for *a* ≡ −1 (mod *n*) since d is odd, for the same reason. That is why random a are usually chosen in the interval 1 < *a* < *n* − 1.

For testing arbitrarily large n, choosing bases at random is essential, as we don't know the distribution of witnesses and strong liars among the numbers 2, 3, ..., *n* − 2.

However, a pre-selected set of a few small bases guarantees the identification of all composites up to a pre-computed maximum. This maximum is generally quite large compared to the bases. This gives very fast deterministic tests for small enough *n* (see section *Testing against small sets of bases* below).

### Proofs

Here is a proof that, if *n* is a prime, then the only square roots of 1 modulo *n* are 1 and −1.

Proof

Certainly 1 and −1, when squared modulo *n*, always yield 1. It remains to show that there are no other square roots of 1 modulo *n*. This is a special case, here applied with the polynomial X2 − 1 over the finite field **Z**/*n***Z**, of the more general fact that a polynomial over some field has no more roots than its degree (this theorem follows from the existence of an Euclidean division for polynomials). Here follows a more elementary proof. Suppose that *x* is a square root of 1 modulo *n*. Then:

$(x-1)(x+1)=x^{2}-1\equiv 0{\pmod {n}}.$

In other words, *n* divides the product (*x* − 1)(*x* + 1). By Euclid's lemma, since *n* is prime, it divides one of the factors *x* − 1 or *x* + 1, implying that *x* is congruent to either 1 or −1 modulo *n*.

Here is a proof that, if *n* is an odd prime, then it is a strong probable prime to base *a*.

Proof

If *n* is an odd prime and we write *n* − 1= 2*s**d* where *s* is a positive integer and *d* is an odd positive integer, by Fermat's little theorem:

$a^{2^{s}d}\equiv 1{\pmod {n}}.$

Each term of the sequence $a^{2^{s}d},a^{2^{s-1}d},\dots ,a^{2d},a^{d}$ is a square root of the previous term. Since the first term is congruent to 1, the second term is a square root of 1 modulo *n*. By the previous lemma, it is congruent to either 1 or −1 modulo *n*. If it is congruent to −1, we are done. Otherwise, it is congruent to 1 and we can iterate the reasoning. At the end, either one of the terms is congruent to −1, or all of them are congruent to 1, and in particular the last term, *a**d*, is.

## Example

Suppose we wish to determine if $n=221$ is prime. We write $n-1{\text{ as }}2^{2}\times 55$ , so that we have $s=2{\text{ and }}d=55$ . We randomly select a number a such that $2\leq a\leq n-2$ .

Say $a=174$ :

${\begin{aligned}a^{{s^{0}}d}{\text{ mod }}n\rightarrow &174^{{2^{0}}55}{\text{ mod }}221\equiv 174^{55}\equiv 47{\text{. Since }}47\neq 1{\text{ and }}47\neq n-1{\text{, we continue.}}\\&174^{{2^{1}}55}{\text{ mod }}221\equiv 174^{110}\equiv 220=n-1\end{aligned}}$

Since $220\equiv -1{\text{ mod }}n$ , either 221 is prime, or 174 is a strong liar for 221. We try another random a , this time choosing $a=137$ :

${\begin{aligned}a^{{s^{0}}d}{\text{ mod }}n\rightarrow &137^{{2^{0}}55}{\text{ mod }}221\equiv 137^{55}\equiv 188{\text{. Since }}188\neq 1{\text{ and }}188\neq n-1{\text{, we continue.}}\\&137^{{2^{1}}55}{\text{ mod }}221\equiv 137^{110}\equiv 205\neq n-1\end{aligned}}$

Hence 137 is a witness for the compositeness of 221, and 174 was in fact a strong liar. Note that this tells us nothing about the factors of 221 (which are 13 and 17). However, the example with 341 in a later section shows how these calculations can sometimes produce a factor of *n*.

For a practical guide to choosing the value of *a*, see Testing against small sets of bases.

## Miller–Rabin test

The algorithm can be written in pseudocode as follows. The parameter *k* determines the accuracy of the test. The greater the number of rounds, the more accurate the result.

```
Input #1: n > 2, an odd integer to be tested for primality
Input #2: k, the number of rounds of testing to perform
Output: “composite” if n is found to be composite, “probably prime” otherwise
```

```
let s > 0 and d odd > 0 such that n − 1 = 2sd  # by factoring out powers of 2 from n − 1
repeat k times:
    a ← random(2, n − 2)  # n is always a probable prime to base 1 and n − 1
    x ← ad mod n
    repeat s times:
        y ← x2 mod n
        if y = 1 and x ≠ 1 and x ≠ n − 1 then # nontrivial square root of 1 modulo n
            return “composite”
        x ← y
    if y ≠ 1 then
        return “composite”
return “probably prime”
```

### Complexity

Using repeated squaring, the running time of this algorithm is O(*k* *n*3), for an *n*-digit number, and *k* is the number of rounds performed; thus this is an efficient, polynomial-time algorithm. FFT-based multiplication, for example the Schönhage–Strassen algorithm, can decrease the running time to O(*k* *n*2 log *n* log log *n*) = Õ(*k* *n*2).

### Accuracy

The error made by the primality test is measured by the probability that a composite number is declared probably prime. The more bases *a* are tried, the better the accuracy of the test. It can be shown that if *n* is composite, then at most ⁠1/4⁠ of the bases *a* are strong liars for *n*. As a consequence, if *n* is composite then running *k* iterations of the Miller–Rabin test will declare *n* probably prime with a probability at most 4−*k*.

This is an improvement over the Solovay–Strassen test, whose worst‐case error bound is 2−*k*. Moreover, the Miller–Rabin test is strictly stronger than the Solovay–Strassen test in the sense that for every composite *n*, the set of strong liars for *n* is a subset of the set of Euler liars for *n*, and for many *n*, the subset is proper.

In addition, for large values of *n*, the probability for a composite number to be declared probably prime is often significantly smaller than 4−*k*. For instance, for most numbers *n*, this probability is bounded by 8−*k*; the proportion of numbers *n* which invalidate this upper bound vanishes as we consider larger values of *n*. Hence the *average* case has a much better accuracy than 4−*k*, a fact which can be exploited for *generating* probable primes (see below). However, such improved error bounds should not be relied upon to *verify* primes whose probability distribution is not controlled, since a cryptographic adversary might send a carefully chosen pseudoprime in order to defeat the primality test. In such contexts, only the *worst‐case* error bound of 4−*k* can be relied upon.

The above error measure is the probability for a composite number to be declared as a strong probable prime after *k* rounds of testing; in mathematical words, it is the conditional probability $\Pr(M\!R_{k}\mid \lnot P)$ where *P* is the event that the number being tested is prime, and *MRk* is the event that it passes the Miller–Rabin test with *k* rounds. We are often interested instead in the inverse conditional probability $\Pr(\lnot P\mid M\!R_{k})$ : the probability that a number which has been declared as a strong probable prime is in fact composite. These two probabilities are related by Bayes' law:

${\begin{aligned}\Pr(\lnot P\mid M\!R_{k})&={\frac {\Pr(\lnot P\land M\!R_{k})}{\Pr(\lnot P\land M\!R_{k})+\Pr(P\land M\!R_{k})}}\\&={\frac {1}{1+{\frac {\Pr(M\!R_{k}\mid P)}{\Pr(M\!R_{k}\mid \lnot P)}}{\frac {\Pr(P)}{\Pr(\lnot P)}}}}\\&={\frac {1}{1+{\frac {1}{\Pr(M\!R_{k}\mid \lnot P)}}{\frac {\Pr(P)}{1-\Pr(P)}}}}\end{aligned}}$

In the last equation, we simplified the expression using the fact that all prime numbers are correctly reported as strong probable primes (the test has no false negative). By dropping the left part of the denominator, we derive a simple upper bound:

$\Pr(\lnot P\mid M\!R_{k})<\Pr(M\!R_{k}\mid \lnot P)\left({\tfrac {1}{\Pr(P)}}-1\right)$

Hence this conditional probability is related not only to the error measure discussed above — which is bounded by 4−*k* — but also to the probability distribution of the input number. In the general case, as said earlier, this distribution is controlled by a cryptographic adversary, thus unknown, so we cannot deduce much about $\Pr(\lnot P\mid M\!R_{k})$ . However, in the case when we use the Miller–Rabin test to *generate* primes (see below), the distribution is chosen by the generator itself, so we can exploit this result.

### Combining multiple tests

Caldwell points out that strong probable prime tests to different bases sometimes provide an additional primality test. Just as the strong test checks for the existence of more than two square roots of 1 modulo *n*, two such tests can sometimes check for the existence of more than two square roots of −1.

Suppose that, in the course of our probable prime tests, we come across two bases *a* and *a′* for which $a^{2^{r}d}\equiv a^{\prime \,2^{r'}d}\equiv -1{\pmod {n}}$ with *r*, *r′* ≥ 1. This means that we have computed two square roots as part of the testing, and can check whether $a^{2^{r-1}d}\equiv \pm a^{\prime \,2^{r'-1}d}{\pmod {n}}$ . This must always hold if *n* is prime; if not, we have found more than two square roots of −1 and proved that *n* is composite.

This is only possible if *n* ≡ 1 (mod 4), and we pass probable prime tests with two or more bases *a* such that *ad* ≢ ±1 (mod *n*), but it is an inexpensive addition to the basic Miller–Rabin test.

## Deterministic variants

### Miller test

The Miller–Rabin algorithm can be made deterministic by trying all possible values of *a* below a certain limit. Taking *n* as the limit would imply O(*n*) trials, hence the running time would be exponential with respect to the size log *n* of the input. To improve the running time, the challenge is then to lower the limit as much as possible while keeping the test reliable.

If the tested number *n* is composite, the strong liars *a* coprime to *n* are contained in a proper subgroup of the group (**Z**/*n***Z**)*, which means that if we test all *a* from a set which generates (**Z**/*n***Z**)*, one of them must lie outside the said subgroup, hence must be a witness for the compositeness of *n*. Assuming the truth of the generalized Riemann hypothesis (which Miller, confusingly, calls the "extended Riemann hypothesis"), it is known that the group is generated by its elements smaller than O((ln *n*)2), which was already noted by Miller. The constant involved in the Big O notation was reduced to 2 by Eric Bach. This leads to the following primality testing algorithm, known as the **Miller test**, which is deterministic assuming the extended Riemann hypothesis:

```
Input: n > 2, an odd integer to be tested for primality
Output: “composite” if n is composite, “prime” otherwise
```

```
let s > 0 and d odd > 0 such that n − 1 = 2sd  # by factoring out powers of 2 from n − 1
for all a in the range [2, min(n − 2, ⌊2(ln n)2⌋)]:
    x ← ad mod n
    repeat s times:
        y ← x2 mod n
        if y = 1 and x ≠ 1 and x ≠ n − 1 then  # nontrivial square root of 1 modulo n
            return “composite”
        x ← y
    if y ≠ 1 then
        return “composite”
return “prime”
```

The full power of the generalized Riemann hypothesis is not needed to ensure the correctness of the test: as we deal with subgroups of even index, it suffices to assume the validity of GRH for quadratic Dirichlet characters.

The running time of the algorithm is, in the soft-O notation, Õ((log *n*)4) (using FFT‐based multiplication).

The Miller test is not used in practice. For most purposes, proper use of the probabilistic Miller–Rabin test or the Baillie–PSW primality test gives sufficient confidence while running much faster. It is also slower in practice than commonly used proof methods such as APR-CL and ECPP which give results that do not rely on unproven assumptions. For theoretical purposes requiring a deterministic polynomial time algorithm, it was superseded by the AKS primality test, which also does not rely on unproven assumptions.

### Testing against small sets of bases

When the number *n* to be tested is small, trying all *a* < 2(ln *n*)2 is not necessary, as much smaller sets of potential witnesses are known to suffice. For example, Pomerance, Selfridge, Wagstaff and Jaeschke have verified that

- if *n* < 2,047, it is enough to test *a* = 2;
- if *n* < 1,373,653, it is enough to test *a* = 2 and 3;
- if *n* < 9,080,191, it is enough to test *a* = 31 and 73;
- if *n* < 25,326,001, it is enough to test *a* = 2, 3, and 5;
- if *n* < 3,215,031,751, it is enough to test *a* = 2, 3, 5, and 7;
- if *n* < 4,759,123,141, it is enough to test *a* = 2, 7, and 61;
- if *n* < 1,122,004,669,633, it is enough to test *a* = 2, 13, 23, and 1662803;
- if *n* < 2,152,302,898,747, it is enough to test *a* = 2, 3, 5, 7, and 11;
- if *n* < 3,474,749,660,383, it is enough to test *a* = 2, 3, 5, 7, 11, and 13;
- if *n* < 341,550,071,728,321, it is enough to test *a* = 2, 3, 5, 7, 11, 13, and 17.
- adding a test with *a* = 19 does not improve the preceding bound.

Using the 2010 work of Feitsma and Galway enumerating all base 2 pseudoprimes up to 264, this was extended (see OEIS: A014233), with the first result later shown using different methods in Jiang and Deng:

- if *n* < 3,825,123,056,546,413,051, it is enough to test *a* = 2, 3, 5, 7, 11, 13, 17, 19, and 23.
- adding tests with *a* = 29 and 31 does not improve the preceding bound.
- if *n* < 264 = 18,446,744,073,709,551,616, it is enough to test *a* = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, and 37.

Sorenson and Webster verify the above and calculate precise results for these larger than 64‐bit results:

- if *n* < 318,665,857,834,031,151,167,461, it is enough to test *a* = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, and 37.
- if *n* < 3,317,044,064,679,887,385,961,981, it is enough to test *a* = 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, and 41.

Zhang (2007), by focusing on particular integers provides further predictions, e.g. that 18 consecutive primes would be enough for *n* < 1,543,267,864,443,420,616,877,677,640,751,301. However, proving this to hold for all integers up to the bound is substantially more difficult.

Other criteria of this sort, often more efficient (fewer bases required) than those shown above, exist by removing the requirement for the bases to be consecutive. For example, two bases *a* = 336,781,006,125 and 9,639,812,373,923,155 are sufficient for *n* < 1,050,535,501; seven bases are sufficient for *n* < 264. Further optimization by Steve Worley and others, involves partitioning the integers less than N into subsets and preselecting witnesses that correctly evaluate all elements of that subset. Such a test can use only 2 witnesses for all N less than 2^64

There is a small list of potential witnesses for every possible input size (at most *b* values for *b*‐bit numbers). However, no finite set of bases is sufficient for all composite numbers. Alford, Granville, and Pomerance have shown that there exist infinitely many composite numbers *n* whose smallest compositeness witness is at least (ln *n*)1/(3ln ln ln *n*). They also argue heuristically that the smallest number *w* such that every composite number below *n* has a compositeness witness less than *w* should be of order Θ(log *n* log log *n*).

## Variants for finding factors

By inserting greatest common divisor calculations into the above algorithm, we can sometimes obtain a factor of *n* instead of merely determining that *n* is composite. This occurs for example when *n* is a probable prime to base *a* but not a strong probable prime to base *a*.

If *x* is a nontrivial square root of 1 modulo *n*,

- since *x*2 ≡ 1 (mod *n*), we know that *n* divides *x*2 − 1 = (*x* − 1)(*x* + 1);
- since *x* ≢ ±1 (mod *n*), we know that *n* does not divide *x* − 1 nor *x* + 1.

From this we deduce that *A* = gcd(*x* − 1, *n*) and *B* = gcd(*x* + 1, *n*) are nontrivial (not necessarily prime) factors of *n* (in fact, since *n* is odd, these factors are coprime and *n* = *AB*). Hence, if factoring is a goal, these gcd calculations can be inserted into the algorithm at little additional computational cost. This leads to the following pseudocode, where the added or changed code is highlighted:

```
Input #1: n > 2, an odd integer to be tested for primality
Input #2: k, the number of rounds of testing to perform
Output: (“multiple of”, m) if a nontrivial factor m of n is found,
        “composite” if n is otherwise found to be composite,
        “probably prime” otherwise
```

```
let s > 0 and d odd > 0 such that n − 1 = 2sd  # by factoring out powers of 2 from n − 1
repeat k times:
    a ← random(2, n − 2)  # n is always a probable prime to base 1 and n − 1
    x ← ad mod n
    repeat s times:
        y ← x2 mod n
        if y = 1 and x ≠ 1 and x ≠ n − 1 then  # nontrivial square root of 1 modulo n
            return (“multiple of”, gcd(x − 1, n))
        x ← y
    if y ≠ 1 then
        return “composite”
return “probably prime”
```

This is *not* a probabilistic factorization algorithm because it is only able to find factors for numbers *n* which are pseudoprime to base *a* (in other words, for numbers *n* such that *a**n*−1 ≡ 1 mod *n*). For other numbers, the algorithm only returns "composite" with no further information.

For example, consider *n* = 341 and *a* = 2. We have *n* − 1 = 85 × 4. Then 285 mod 341 = 32 and 322 mod 341 = 1. This tells us that *n* is a pseudoprime base 2, but not a strong pseudoprime base 2. By computing a gcd at this stage, we find a factor of 341: gcd(32 − 1, 341) = 31. Indeed, 341 = 11 × 31.

The same technique can be applied to the square roots of any other value, particularly the square roots of −1 mentioned in § Combining multiple tests. If two (successful) strong probable prime tests find *x*2 ≡ −1 (mod *n*) and *y*2 ≡ −1 (mod *n*), but *x* ≢ ±*y* (mod *n*), then gcd(*x* − *y*, *n*) and gcd(*x* + *y*, *n*) are nontrivial factors of *n*.

For example, *n* = 46,856,248,255,981 is a strong pseudoprime to bases 2 and 7, but in the course of performing the tests we find

$2^{(n-1)/2}\equiv 7^{(n-1)/2}\equiv -1{\pmod {n}},$

$2^{(n-1)/4}\equiv 34456063004337{\pmod {n}},{\text{ and}}$

$7^{(n-1)/4}\equiv 21307242304265{\pmod {n}}.$

This gives us the factor gcd(34456063004337 − 21307242304265, *n*) = 4840261.

## Generation of probable primes

The Miller–Rabin test can be used to generate strong probable primes, simply by drawing integers at random until one passes the test. This algorithm terminates almost surely (since at each iteration there is a chance to draw a prime number). The pseudocode for generating *b*‐bit strong probable primes (with the most significant bit set) is as follows:

```
Input #1: b, the number of bits of the result
Input #2: k, the number of rounds of testing to perform
Output: a strong probable prime n
```

```
while True:
    pick a random odd integer n in the range [2b−1, 2b−1]
    if the Miller–Rabin test with inputs n and k returns “probably prime” then
        return n
```

### Complexity

Of course the worst-case running time is infinite, since the outer loop may never terminate, but that happens with probability zero. As per the geometric distribution, the expected number of draws is ${\tfrac {1}{\Pr(M\!R_{k})}}$ (reusing notations from earlier).

As any prime number passes the test, the probability of being prime gives a coarse lower bound to the probability of passing the test. If we draw odd integers uniformly in the range [2*b*−1, 1*b*−1], then we get:

$\Pr(M\!R_{k})>\Pr(1)={\frac {\pi \left(2^{b}\right)-\pi \left(2^{b-1}\right)}{2^{b-2}}}$

where π is the prime-counting function. Using an asymptotic expansion of π (an extension of the prime number theorem), we can approximate this probability when *b* grows towards infinity. We find:

$\Pr(P)={\tfrac {2}{\ln 2}}b^{-1}+{\mathcal {O}}\left(b^{-3}\right)$

${\tfrac {1}{\Pr(P)}}={\tfrac {\ln 2}{2}}b+{\mathcal {O}}\left(b^{-1}\right)$

Hence we can expect the generator to run no more Miller–Rabin tests than a number proportional to *b*. Taking into account the worst-case complexity of each Miller–Rabin test (see earlier), the expected running time of the generator with inputs *b* and *k* is then bounded by O(*k* *b*4) (or Õ(*k* *b*3) using FFT-based multiplication).

### Accuracy

The error measure of this generator is the probability that it outputs a composite number.

Using the relation between conditional probabilities (shown in an earlier section) and the asymptotic behavior of $\Pr(P)$ (shown just before), this error measure can be given a coarse upper bound:

$\Pr(\lnot P\mid M\!R_{k})<\Pr(M\!R_{k}\mid \lnot P)\left({\tfrac {1}{\Pr(P)}}-1\right)\leq 4^{-k}\left({\tfrac {\ln 2}{2}}b-1+{\mathcal {O}}\left(b^{-1}\right)\right).$

Hence, for large enough *b*, this error measure is less than ${\tfrac {\ln 2}{2}}4^{-k}b$ . However, much better bounds exist.

Using the fact that the Miller–Rabin test itself often has an error bound much smaller than 4−*k* (see earlier), Damgård, Landrock and Pomerance derived several error bounds for the generator, with various classes of parameters *b* and *k*. These error bounds allow an implementor to choose a reasonable *k* for a desired accuracy.

One of these error bounds is 4−*k*, which holds for all *b* ≥ 2 (the authors only showed it for *b* ≥ 51, while Ronald Burthe Jr. completed the proof with the remaining values 2 ≤ *b* ≤ 50). Again this simple bound can be improved for large values of *b*. For instance, another bound derived by the same authors is:

$\left({\frac {1}{7}}b^{\frac {15}{4}}2^{-{\frac {b}{2}}}\right)4^{-k}$

which holds for all *b* ≥ 21 and *k* ≥ *b*/4. This bound is smaller than 4−*k* as soon as *b* ≥ 32.
