---
title: "Trial division"
source: https://en.wikipedia.org/wiki/Trial_division
domain: prime-sieve-algorithms
license: CC-BY-SA-4.0
tags: sieve of eratosthenes, sieve of atkin, wheel factorization, prime generation
fetched: 2026-07-02
---

# Trial division

**Trial division** is the most laborious but easiest to understand of the integer factorization algorithms. The essential idea behind trial division tests to see if an integer n, the integer to be factored, can be divided by each number in turn that is less than or equal to the square root of n.

For example, to find the prime factors of *n* = 70, one can try to divide 70 by successive primes: first, 70 / 2 = 35; next, neither 2 nor 3 evenly divides 35; finally, 35 / 5 = 7, and 7 is itself prime. So 70 = 2 × 5 × 7.

Trial division was first described by Fibonacci in his book *Liber Abaci* (1202).

## Method

Given an integer *n* (*n* refers to "the integer to be factored"), the trial division consists of systematically testing whether *n* is divisible by any smaller number. Clearly, it is only worthwhile to test candidate factors less than *n*, and in order from two upwards because an arbitrary *n* is more likely to be divisible by two than by three, and so on. With this ordering, there is no point in testing for divisibility by four if the number has already been determined not divisible by two, and so on for three and any multiple of three, etc. Therefore, the effort can be reduced by selecting only prime numbers as candidate factors, provided they are repeatedly tested until they fail. Furthermore, the trial factors need go no further than $\scriptstyle {\sqrt {n}}$ because if *n* is composite, it must have at least one factor ≤ $\scriptstyle {\sqrt {(}}n)$ , which would have been detected earlier; having all factors > $\scriptstyle {\sqrt {(}}n)$ is impossible because the product of any two would be > *n*.

When a trial division is successful, the process is applied recursively to the resulting quotient.

A definite bound on the prime factors is possible. Suppose Pi is the i'th prime, so that *P*1 = 2, *P*2 = 3, *P*3 = 5, etc. Then the last prime number worth testing as a possible factor of *n* is Pi where *P*2*i* + 1 > *n*; equality here would mean that *P**i* + 1 is a factor. Thus, testing with 2, 3, and 5 suffices up to *n* = 48 not just 25 because the square of the next prime is 49, and below *n* = 25 just 2 and 3 are sufficient. Should the square root of *n* be an integer, then it is a factor and *n* is a perfect square.

The trial division algorithm in pseudocode:

```
algorithm trial-division is
    input: Integer n to be factored
    output: List F of prime factors of n

    P ← set of all primes ≤ 
  
    
      
        
          
            n
          
        
      
    
    {\displaystyle {\sqrt {n}}}
  

    F ← empty list of factors

    for each prime p in P do
        while n mod p is 0
            Add factor p to list F
            n ← n/p

    if F is empty    (Original n is prime?)
        Add factor n to list F
```

Determining the primes less than or equal to ${\sqrt {n}}$ is not a trivial task as *n* gets larger, so the simplest computer programs to factor a number just try successive integers, prime and composite, from 2 to ${\sqrt {n}}$ as possible factors.

## Speed

In the worst case, trial division is a laborious algorithm. For a base-2 *n* digit number *a*, if it starts from two and works up only to the square root of *a*, the algorithm requires

$\pi (2^{n/2})\approx {2^{n/2} \over \left({\frac {n}{2}}\right)\ln 2}$

trial divisions, where $\pi (x)$ denotes the prime-counting function, the number of primes less than *x*. This does not take into account the overhead of primality testing to obtain the prime numbers as candidate factors. A useful table need not be large: P(3512) = 32749, the last prime that fits into a sixteen-bit signed integer and P(6542) = 65521 for unsigned sixteen-bit integers. That would suffice to test primality for numbers up to 655372 = 4,295,098,369. Preparing such a table (usually via the Sieve of Eratosthenes) would only be worthwhile if many numbers were to be tested. If instead a variant is used without primality testing, but simply dividing by every odd number less than the square root the base-2 *n* digit number *a*, prime or not, it can take up to about:

$2^{n/2}$

In both cases, the required time grows exponentially with the digits of the number.

Even so, this is a quite satisfactory method, considering that even the best-known algorithms have exponential time growth. For *a* chosen uniformly at random from integers of a given length, there is a 50% chance that 2 is a factor of *a* and a 33% chance that 3 is a factor of *a*, and so on. It can be shown that 88% of all positive integers have a factor under 100 and that 92% have a factor under 1000. Thus, when confronted by an arbitrary large *a*, it is worthwhile to check for divisibility by the small primes, since for $a=1000$ , in base-2 $n=10$ .

However, many-digit numbers that do not have factors in the small primes can require days or months to factor with trial division. In such cases other methods are used such as the quadratic sieve and the general number field sieve (GNFS). Because these methods also have superpolynomial time growth a practical limit of *n* digits is reached very quickly. For this reason, in public key cryptography, values for *a* are chosen to have large prime factors of similar size so that they cannot be factored by any publicly known method in a useful time period on any available computer system or computer cluster such as supercomputers and computer grids. The largest cryptography-grade number that has been factored is RSA-250, a 250-digit number, using the GNFS and resources of several supercomputers. The running time was 2700 core years.
