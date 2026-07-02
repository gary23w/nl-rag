---
title: "Generation of primes"
source: https://en.wikipedia.org/wiki/Generation_of_primes
domain: prime-sieve-algorithms
license: CC-BY-SA-4.0
tags: sieve of eratosthenes, sieve of atkin, wheel factorization, prime generation
fetched: 2026-07-02
---

# Generation of primes

In computational number theory, a variety of algorithms make it possible to generate prime numbers efficiently. These are used in various applications, for example hashing, public-key cryptography, and search of prime factors in large numbers.

For relatively small numbers, it is possible to just apply trial division to each successive odd number. Prime sieves are almost always faster. Prime sieving is the fastest known way to deterministically enumerate the primes. There are some known formulas that can calculate the next prime but there is no known way to express the next prime in terms of the previous primes. Also, there is no effective known general manipulation and/or extension of some mathematical expression (even such including later primes) that deterministically calculates the next prime.

## Prime sieves

A prime sieve or prime number sieve is a fast type of algorithm for finding primes. There are many prime sieves. The simple sieve of Eratosthenes (250s BCE), the sieve of Sundaram (1934), the still faster but more complicated sieve of Atkin (2003), sieve of Pritchard (1979), and various wheel sieves are most common.

A prime sieve works by creating a list of all integers up to a desired limit and progressively removing composite numbers (which it directly generates) until only primes are left. This is the most efficient way to obtain a large range of primes; however, to find individual primes, direct primality tests are more efficient. Furthermore, based on the sieve formalisms, some integer sequences (sequence A240673 in the OEIS) are constructed which also could be used for generating primes in certain intervals.

Historically some prime sieves were realised or partly realised in hardware, including the stencils used by Anton Felkel, Carl Hindenburg and D. N. Lehmer as aids to manual computation; and the electromechanical machines, and one later electronic machine, known as the Lehmer sieves by D. H. Lehmer (on at least one occasion with D. N. Lehmer).

## Large primes

Cryptography requires the use of very large primes: for example, with the RSA cryptosystem two primes of at least 1,024 bits (i.e. at least 21023) are recommended. To generate these primes, the mainstream method is to generate random numbers in a target range and test them for primality using fast probabilistic methods: a short round of sieving (sieve of Eratosthenes or trial division) followed by Baillie–PSW primality test or the Miller–Rabin primality test; a probable prime with a chance of 2-112 of being composite is considered plenty for the 2,048-bit case. Even if a composite number is chosen, it will likely be quickly discovered by causing failed operations, except when a Carmichael number happens to be chosen in the case of RSA.

A less common choice is to use provable primes, which can be generated based on variants of Pocklington primality test, especially Maurer's algorithm. Both the provable and probable primality tests rely on modular exponentiation.

In addition with RSA, so-called "strong primes" with both p-1 and p+1 having a large prime factor is preferred, as this is expected to slow down factoring attempts using the Polard's p-1 and Williams' p+1 algorithms. Such a choice has little effect against elliptic-curve factoring methods, however.

Integers of special forms, such as Mersenne primes or Fermat primes, can be efficiently tested for primality if the prime factorization of *p* − 1 or *p* + 1 is known.

## Complexity

The sieve of Eratosthenes is generally considered the easiest sieve to implement, but it is not the fastest in the sense of the number of operations for a given range for large sieving ranges. In its usual standard implementation (which may include basic wheel factorization for small primes), it can find all the primes up to *N* in time $O(N\log \log N),$ while basic implementations of the sieve of Atkin and wheel sieves run in linear time $O(N)$ . Special versions of the Sieve of Eratosthenes using wheel sieve principles can have this same linear $O(N)$ time complexity. A special version of the Sieve of Atkin and some special versions of wheel sieves which may include sieving using the methods from the Sieve of Eratosthenes can run in sublinear time complexity of $O(N/\log \log N)$ . Note that just because an algorithm has decreased asymptotic time complexity does not mean that a practical implementation runs faster than an algorithm with a greater asymptotic time complexity: If in order to achieve that lesser asymptotic complexity the individual operations have a constant factor of increased time complexity that may be many times greater than for the simpler algorithm, it may never be possible within practical sieving ranges for the advantage of the reduced number of operations for reasonably large ranges to make up for this extra cost in time per operation.

Some sieving algorithms, such as the Sieve of Eratosthenes with large amounts of wheel factorization, take much less time for smaller ranges than their asymptotic time complexity would indicate because they have large negative constant offsets in their complexity and thus don't reach that asymptotic complexity until far beyond practical ranges. For instance, the Sieve of Eratosthenes with a combination of wheel factorization and pre-culling using small primes up to 19 uses time of about a factor of two less than that predicted for the total range for a range of 1019, which total range takes hundreds of core-years to sieve for the best of sieve algorithms.

The simple naive "one large sieving array" sieves of any of these sieve types take memory space of about $O(N)$ , which means that 1) they are very limited in the sieving ranges they can handle to the amount of RAM (memory) available and 2) that they are typically quite slow since memory access speed typically becomes the speed bottleneck more than computational speed once the array size grows beyond the size of the CPU caches. The normally implemented page segmented sieves of both Eratosthenes and Atkin take space $O(N/\log N)$ plus small sieve segment buffers which are normally sized to fit within the CPU cache; page segmented wheel sieves including special variations of the Sieve of Eratosthenes typically take much more space than this by a significant factor in order to store the required wheel representations; Pritchard's variation of the linear time complexity sieve of Eratosthenes/wheel sieve takes $O(N^{1/2}\log \log N/\log N)$ space. The better time complexity special version of the Sieve of Atkin takes space $N^{1/2+o(1)}$ . Sorenson shows an improvement to the wheel sieve that takes even less space at $O(N/((\log N)^{L}\log \log N))$ for any $L>1$ . However, the following is a general observation: the more the amount of memory is reduced, the greater the constant factor increase in the cost in time per operation even though the asymptotic time complexity may remain the same, meaning that the memory-reduced versions may run many times slower than the non-memory-reduced versions by quite a large factor.
