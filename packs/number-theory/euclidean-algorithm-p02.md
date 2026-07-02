---
title: "Euclidean algorithm (part 2/2)"
source: https://en.wikipedia.org/wiki/Euclidean_algorithm
domain: number-theory
license: CC-BY-SA-4.0
tags: number theory, modular arithmetic, prime number, gcd
fetched: 2026-07-02
part: 2/2
---

## Algorithmic efficiency

The computational efficiency of Euclid's algorithm has been studied thoroughly. This efficiency can be described by the number of division steps the algorithm requires, multiplied by the computational expense of each step. The first known analysis of Euclid's algorithm is due to A. A. L. Reynaud in 1811, who showed that the number of division steps on input (*u*, *v*) is bounded by *v*; later he improved this to *v*/2 + 2. Later, in 1841, P. J. E. Finck showed that the number of division steps is at most 2 log2 *v* + 1, and hence Euclid's algorithm runs in time polynomial in the size of the input. Émile Léger, in 1837, studied the worst case, which is when the inputs are consecutive Fibonacci numbers. Finck's analysis was refined by Gabriel Lamé in 1844, who showed that the number of steps required for completion is never more than five times the number *h* of base-10 digits of the smaller number *b*.

In the uniform cost model (suitable for analyzing the complexity of gcd calculation on numbers that fit into a single machine word), each step of the algorithm takes constant time, and Lamé's analysis implies that the total running time is also *O*(*h*). However, in a model of computation suitable for computation with larger numbers, the computational expense of a single remainder computation in the algorithm can be as large as *O*(*h*2). In this case the total time for all of the steps of the algorithm can be analyzed using a telescoping series, showing that it is also *O*(*h*2). Modern algorithmic techniques based on the Schönhage–Strassen algorithm for fast integer multiplication can be used to speed this up, leading to quasilinear algorithms for the GCD.

### Number of steps

The number of steps to calculate the GCD of two natural numbers, *a* and *b*, may be denoted by *T*(*a*, *b*). If *g* is the GCD of *a* and *b*, then *a* = *mg* and *b* = *ng* for two coprime numbers *m* and *n*. Then

T

(

a

,

b

) =

T

(

m

,

n

)

as may be seen by dividing all the steps in the Euclidean algorithm by *g*. By the same argument, the number of steps remains the same if *a* and *b* are multiplied by a common factor *w*: *T*(*a*, *b*) = *T*(*wa*, *wb*). Therefore, the number of steps *T* may vary dramatically between neighboring pairs of numbers, such as T(*a*, *b*) and T(*a*, *b* + 1), depending on the size of the two GCDs.

The recursive nature of the Euclidean algorithm gives another equation

T

(

a

,

b

) = 1 +

T

(

b

,

r

0

) = 2 +

T

(

r

0

,

r

1

) = … =

N

+

T

(

r

N

−2

,

r

N

−1

) =

N

+ 1

where *T*(*x*, 0) = 0 by assumption.

#### Worst-case

If the Euclidean algorithm requires *N* steps for a pair of natural numbers *a* > *b* > 0, the smallest values of *a* and *b* for which this is true are the Fibonacci numbers *F**N*+2 and *F**N*+1, respectively. More precisely, if the Euclidean algorithm requires *N* steps for the pair *a* > *b*, then one has *a* ≥ *F**N*+2 and *b* ≥ *F**N*+1. This can be shown by induction. If *N* = 1, *b* divides *a* with no remainder; the smallest natural numbers for which this is true is *b* = 1 and *a* = 2, which are *F*2 and *F*3, respectively. Now assume that the result holds for all values of *N* up to *M* − 1. The first step of the *M*-step algorithm is *a* = *q*0*b* + *r*0, and the Euclidean algorithm requires *M* − 1 steps for the pair *b* > *r*0. By induction hypothesis, one has *b* ≥ *F**M*+1 and *r*0 ≥ *F**M*. Therefore, *a* = *q*0*b* + *r*0 ≥ *b* + *r*0 ≥ *F**M*+1 + *F**M* = *F**M*+2, which is the desired inequality. This proof, published by Gabriel Lamé in 1844, represents the beginning of computational complexity theory, and also the first practical application of the Fibonacci numbers.

This result suffices to show that the number of steps in Euclid's algorithm can never be more than five times the number of its digits (base 10). For if the algorithm requires *N* steps, then *b* is greater than or equal to *F**N*+1 which in turn is greater than or equal to *φ**N*−1, where *φ* is the golden ratio. Since *b* ≥ *φ**N*−1, then *N* − 1 ≤ log*φ**b*. Since log10*φ* > 1/5, (*N* − 1)/5 < log10*φ* log*φ**b* = log10*b*. Thus, *N* ≤ 5 log10*b*. Thus, the Euclidean algorithm always needs less than *O*(*h*) divisions, where *h* is the number of digits in the smaller number *b*.

#### Average

The average number of steps taken by the Euclidean algorithm has been defined in three different ways. The first definition is the average time *T*(*a*) required to calculate the GCD of a given number *a* and a smaller natural number *b* chosen with equal probability from the integers 0 to *a* − 1

$T(a)={\frac {1}{a}}\sum _{0\leq b<a}T(a,b).$

However, since *T*(*a*, *b*) fluctuates dramatically with the GCD of the two numbers, the averaged function *T*(*a*) is likewise "noisy".

To reduce this noise, a second average *τ*(*a*) is taken over all numbers coprime with *a*

$\tau (a)={\frac {1}{\varphi (a)}}\sum _{\begin{smallmatrix}0\leq b<a\\\gcd(a,b)=1\end{smallmatrix}}T(a,b).$

There are *φ*(*a*) coprime integers less than *a*, where *φ* is Euler's totient function. This tau average grows smoothly with *a*

$\tau (a)={\frac {12}{\pi ^{2}}}\ln 2\ln a+C+O(a^{-1/6-\varepsilon })$

with the residual error being of order *a*−(1/6)+*ε*, where *ε* is infinitesimal. The constant *C* in this formula is called Porter's constant and equals

$C=-{\frac {1}{2}}+{\frac {6\ln 2}{\pi ^{2}}}\left(4\gamma -{\frac {24}{\pi ^{2}}}\zeta '(2)+3\ln 2-2\right)\approx 1.467$

where *γ* is the Euler–Mascheroni constant and *ζ*′ is the derivative of the Riemann zeta function. The leading coefficient (12/π2) ln 2 was determined by two independent methods.

Since the first average can be calculated from the tau average by summing over the divisors *d* of *a*

$T(a)={\frac {1}{a}}\sum _{d\mid a}\varphi (d)\tau (d)$

it can be approximated by the formula

$T(a)\approx C+{\frac {12}{\pi ^{2}}}\ln 2\,{\biggl (}{\ln a}-\sum _{d\mid a}{\frac {\Lambda (d)}{d}}{\biggr )}$

where Λ(*d*) is the Mangoldt function.

A third average *Y*(*n*) is defined as the mean number of steps required when both *a* and *b* are chosen randomly (with uniform distribution) from 1 to *n*

$Y(n)={\frac {1}{n^{2}}}\sum _{a=1}^{n}\sum _{b=1}^{n}T(a,b)={\frac {1}{n}}\sum _{a=1}^{n}T(a).$

Substituting the approximate formula for *T*(*a*) into this equation yields an estimate for *Y*(*n*)

$Y(n)\approx {\frac {12}{\pi ^{2}}}\ln 2\ln n+0.06.$

### Computational expense per step

In each step *k* of the Euclidean algorithm, the quotient *q**k* and remainder *r**k* are computed for a given pair of integers *r**k*−2 and *r**k*−1

r

k

−2

=

q

k

r

k

−1

+

r

k

.

The computational expense per step is associated chiefly with finding *q**k*, since the remainder *r**k* can be calculated quickly from *r**k*−2, *r**k*−1, and *q**k*

r

k

=

r

k

−2

−

q

k

r

k

−1

.

The computational expense of dividing *h*-bit numbers scales as *O*(*h*(*ℓ* + 1)), where ℓ is the length of the quotient.

For comparison, Euclid's original subtraction-based algorithm can be much slower. A single integer division is equivalent to the quotient *q* number of subtractions. If the ratio of *a* and *b* is very large, the quotient is large and many subtractions will be required. On the other hand, it has been shown that the quotients are very likely to be small integers. The probability of a given quotient *q* is approximately ln |*u*/(*u* − 1)| where *u* = (*q* + 1)2. For illustration, the probability of a quotient of 1, 2, 3, or 4 is roughly 41.5%, 17.0%, 9.3%, and 5.9%, respectively. Since the operation of subtraction is faster than division, particularly for large numbers, the subtraction-based Euclid's algorithm is competitive with the division-based version. This is exploited in the binary version of Euclid's algorithm.

Combining the estimated number of steps with the estimated computational expense per step shows that the Euclid's algorithm grows quadratically (*h*2) with the average number of digits *h* in the initial two numbers *a* and *b*. Let *h*0, *h*1, ..., *h**N*−1 represent the number of digits in the successive remainders *r*0, *r*1, ..., *r**N*−1. Since the number of steps *N* grows linearly with *h*, the running time is bounded by

$O{\Big (}\sum _{i<N}h_{i}(h_{i}-h_{i+1}+2){\Big )}\subseteq O{\Big (}h\sum _{i<N}(h_{i}-h_{i+1}+2){\Big )}\subseteq O(h(h_{0}+2N))\subseteq O(h^{2}).$

### Alternative methods

Euclid's algorithm is widely used in practice, especially for small numbers, due to its simplicity. For comparison, the efficiency of alternatives to Euclid's algorithm may be determined.

One inefficient approach to finding the GCD of two natural numbers *a* and *b* is to calculate all their common divisors; the GCD is then the largest common divisor. The common divisors can be found by dividing both numbers by successive integers from 2 to the smaller number *b*. The number of steps of this approach grows linearly with *b*, or exponentially in the number of digits. Another inefficient approach is to find the prime factors of one or both numbers. As noted above, the GCD equals the product of the prime factors shared by the two numbers *a* and *b*. Present methods for prime factorization are also inefficient; many modern cryptography systems even rely on that inefficiency.

The binary GCD algorithm is an efficient alternative that substitutes division with faster operations by exploiting the binary representation used by computers. However, this alternative also scales like *O*(*h*²). It is generally faster than the Euclidean algorithm on real computers, even though it scales in the same way. Additional efficiency can be gleaned by examining only the leading digits of the two numbers *a* and *b*. The binary algorithm can be extended to other bases (*k*-ary algorithms), with up to fivefold increases in speed. Lehmer's GCD algorithm uses the same general principle as the binary algorithm to speed up GCD computations in arbitrary bases.

A recursive approach for very large integers (with more than 25,000 digits) leads to quasilinear integer GCD algorithms, such as those of Schönhage, and Stehlé and Zimmermann. These algorithms exploit the 2×2 matrix form of the Euclidean algorithm given above. These quasilinear methods generally scale as *O*(*h* log *h*2 log log *h*).


## Generalizations

Although the Euclidean algorithm is used to find the greatest common divisor of two natural numbers (positive integers), it may be generalized to the real numbers, and to other mathematical objects, such as polynomials, quadratic integers and Hurwitz quaternions. In the latter cases, the Euclidean algorithm is used to demonstrate the crucial property of unique factorization, i.e., that such numbers can be factored uniquely into irreducible elements, the counterparts of prime numbers. Unique factorization is essential to many proofs of number theory.

### Rational and real numbers

Euclid's algorithm can be applied to real numbers, as described by Euclid in Book 10 of his *Elements*. The goal of the algorithm is to identify a real number g such that two given real numbers, a and b, are integer multiples of it: *a* = *mg* and *b* = *ng*, where m and n are integers. This identification is equivalent to finding an integer relation among the real numbers a and b; that is, it determines integers s and t such that *sa* + *tb* = 0. If such an equation is possible, *a* and *b* are called commensurable lengths, otherwise they are incommensurable lengths.

The real-number Euclidean algorithm differs from its integer counterpart in two respects. First, the remainders *r**k* are real numbers, although the quotients *q**k* are integers as before. Second, the algorithm is not guaranteed to end in a finite number N of steps. If it does, the fraction *a*/*b* is a rational number, i.e., the ratio of two integers

${\frac {a}{b}}={\frac {mg}{ng}}={\frac {m}{n}},$

and can be written as a finite continued fraction [*q*0; *q*1, *q*2, ..., *q**N*]. If the algorithm does not stop, the fraction *a*/*b* is an irrational number and can be described by an infinite continued fraction [*q*0; *q*1, *q*2, …]. Examples of infinite continued fractions are the golden ratio *φ* = [1; 1, 1, ...] and the square root of two, √2 = [1; 2, 2, ...]. When applied to two arbitrary real numbers, the algorithm is unlikely to stop, since almost all ratios *a*/*b* of two real numbers are irrational.

An infinite continued fraction may be truncated at a step *k* [*q*0; *q*1, *q*2, ..., *q**k*] to yield an approximation to *a*/*b* that improves as k is increased. The approximation is described by convergents *m**k*/*n**k*; the numerator and denominators are coprime and obey the recurrence relation

${\begin{aligned}m_{k}&=q_{k}m_{k-1}+m_{k-2}\\n_{k}&=q_{k}n_{k-1}+n_{k-2},\end{aligned}}$

where *m*−1 = *n*−2 = 1 and *m*−2 = *n*−1 = 0 are the initial values of the recursion. The convergent *m**k*/*n**k* is the best rational number approximation to *a*/*b* with denominator *n**k*:

$\left|{\frac {a}{b}}-{\frac {m_{k}}{n_{k}}}\right|<{\frac {1}{n_{k}^{2}}}.$

### Polynomials

Polynomials in a single variable *x* can be added, multiplied and factored into irreducible polynomials, which are the analogs of the prime numbers for integers. The greatest common divisor polynomial *g*(*x*) of two polynomials *a*(*x*) and *b*(*x*) is defined as the product of their shared irreducible polynomials, which can be identified using the Euclidean algorithm. The basic procedure is similar to that for integers. At each step k, a quotient polynomial *q**k*(*x*) and a remainder polynomial *r**k*(*x*) are identified to satisfy the recursive equation

$r_{k-2}(x)=q_{k}(x)r_{k-1}(x)+r_{k}(x),$

where *r*−2(*x*) = *a*(*x*) and *r*−1(*x*) = *b*(*x*). Each quotient polynomial is chosen such that each remainder is either zero or has a degree that is smaller than the degree of its predecessor: deg[*r**k*(*x*)] < deg[*r**k*−1(*x*)]. Since the degree is a nonnegative integer, and since it decreases with every step, the Euclidean algorithm concludes in a finite number of steps. The last nonzero remainder is the greatest common divisor of the original two polynomials, *a*(*x*) and *b*(*x*).

For example, consider the following two quartic polynomials, which each factor into two quadratic polynomials

${\begin{aligned}a(x)&=x^{4}-4x^{3}+4x^{2}-3x+14=(x^{2}-5x+7)(x^{2}+x+2)\qquad {\text{and}}\\b(x)&=x^{4}+8x^{3}+12x^{2}+17x+6=(x^{2}+7x+3)(x^{2}+x+2).\end{aligned}}$

Dividing *a*(*x*) by *b*(*x*) yields a remainder *r*0(*x*) = *x*3 + (2/3)*x*2 + (5/3)*x* − (2/3). In the next step, *b*(*x*) is divided by *r*0(*x*) yielding a remainder *r*1(*x*) = *x*2 + *x* + 2. Finally, dividing *r*0(*x*) by *r*1(*x*) yields a zero remainder, indicating that *r*1(*x*) is the greatest common divisor polynomial of *a*(*x*) and *b*(*x*), consistent with their factorization.

Many of the applications described above for integers carry over to polynomials. The Euclidean algorithm can be used to solve linear Diophantine equations and Chinese remainder problems for polynomials; continued fractions of polynomials can also be defined.

The polynomial Euclidean algorithm has other applications, such as Sturm chains, a method for counting the zeros of a polynomial that lie inside a given real interval. This in turn has applications in several areas, such as the Routh–Hurwitz stability criterion in control theory.

Finally, the coefficients of the polynomials need not be drawn from integers, real numbers or even the complex numbers. For example, the coefficients may be drawn from a general field, such as the finite fields GF(*p*) described above. The corresponding conclusions about the Euclidean algorithm and its applications hold even for such polynomials.

### Gaussian integers

The Gaussian integers are complex numbers of the form *α* = *u* + *vi*, where u and v are ordinary integers and i is the square root of negative one. By defining an analog of the Euclidean algorithm, Gaussian integers can be shown to be uniquely factorizable, by the argument above. This unique factorization is helpful in many applications, such as deriving all Pythagorean triples or proving Fermat's theorem on sums of two squares. In general, the Euclidean algorithm is convenient in such applications, but not essential; for example, the theorems can often be proven by other arguments.

The Euclidean algorithm developed for two Gaussian integers α and β is nearly the same as that for ordinary integers, but differs in two respects. As before, we set *r*−2 = *α* and *r*−1 = *β*, and the task at each step k is to identify a quotient *q**k* and a remainder *r**k* such that

$r_{k}=r_{k-2}-q_{k}r_{k-1},$

where every remainder is strictly smaller than its predecessor: |*r**k*| < |*r**k*−1|. The first difference is that the quotients and remainders are themselves Gaussian integers, and thus are complex numbers. The quotients *q**k* are generally found by rounding the real and complex parts of the exact ratio (such as the complex number *α*/*β*) to the nearest integers. The second difference lies in the necessity of defining how one complex remainder can be "smaller" than another. To do this, a norm function *f*(*u* + *vi*) = *u*2 + *v*2 is defined, which converts every Gaussian integer *u* + *vi* into an ordinary integer. After each step k of the Euclidean algorithm, the norm of the remainder *f*(*r**k*) is smaller than the norm of the preceding remainder, *f*(*r**k*−1). Since the norm is a nonnegative integer and decreases with every step, the Euclidean algorithm for Gaussian integers ends in a finite number of steps. The final nonzero remainder is gcd(*α*, *β*), the Gaussian integer of largest norm that divides both α and β; it is unique up to multiplication by a unit, ±1 or ±*i*.

Many of the other applications of the Euclidean algorithm carry over to Gaussian integers. For example, it can be used to solve linear Diophantine equations and Chinese remainder problems for Gaussian integers; continued fractions of Gaussian integers can also be defined.

### Euclidean domains

A set of elements under two binary operations, denoted as addition and multiplication, is called a Euclidean domain if it forms a commutative ring R and, roughly speaking, if a generalized Euclidean algorithm can be performed on them. The two operations of such a ring need not be the addition and multiplication of ordinary arithmetic; rather, they can be more general, such as the operations of a mathematical group or monoid. Nevertheless, these general operations should respect many of the laws governing ordinary arithmetic, such as commutativity, associativity and distributivity.

The generalized Euclidean algorithm requires a *Euclidean function*, i.e., a mapping f from R into the set of nonnegative integers such that, for any two nonzero elements a and b in R, there exist q and r in R such that *a* = *qb* + *r* and *f*(*r*) < *f*(*b*). Examples of such mappings are the absolute value for integers, the degree for univariate polynomials, and the norm for Gaussian integers above. The basic principle is that each step of the algorithm reduces *f* inexorably; hence, if f can be reduced only a finite number of times, the algorithm must stop in a finite number of steps. This principle relies on the well-ordering property of the non-negative integers, which asserts that every non-empty set of non-negative integers has a smallest member.

The fundamental theorem of arithmetic applies to any Euclidean domain: Any number from a Euclidean domain can be factored uniquely into irreducible elements. Any Euclidean domain is a unique factorization domain (UFD), although the converse is not true. The Euclidean domains and the UFD's are subclasses of the GCD domains, domains in which a greatest common divisor of two numbers always exists. In other words, a greatest common divisor may exist (for all pairs of elements in a domain), although it may not be possible to find it using a Euclidean algorithm. A Euclidean domain is always a principal ideal domain (PID), an integral domain in which every ideal is a principal ideal. Again, the converse is not true: not every PID is a Euclidean domain.

The unique factorization of Euclidean domains is useful in many applications. For example, the unique factorization of the Gaussian integers is convenient in deriving formulae for all Pythagorean triples and in proving Fermat's theorem on sums of two squares. Unique factorization was also a key element in an attempted proof of Fermat's Last Theorem published in 1847 by Gabriel Lamé, the same mathematician who analyzed the efficiency of Euclid's algorithm, based on a suggestion of Joseph Liouville. Lamé's approach required the unique factorization of numbers of the form *x* + *ωy*, where x and y are integers, and *ω* = *e*2*iπ*/*n* is an nth root of 1, that is, *ω**n* = 1. Although this approach succeeds for some values of n (such as *n* = 3, the Eisenstein integers), in general such numbers do *not* factor uniquely. This failure of unique factorization in some cyclotomic fields led Ernst Kummer to the concept of ideal numbers and, later, Richard Dedekind to ideals.

#### Unique factorization of quadratic integers

The quadratic integer rings are helpful to illustrate Euclidean domains. Quadratic integers are generalizations of the Gaussian integers in which the imaginary unit *i* is replaced by a number ω. Thus, they have the form *u* + *vω*, where u and v are integers and ω has one of two forms, depending on a parameter D. If D does not equal a multiple of four plus one, then

$\omega ={\sqrt {D}}.$

If, however, *D* does equal a multiple of four plus one, then

$\omega ={\frac {1+{\sqrt {D}}}{2}}.$

If the function f corresponds to a norm function, such as that used to order the Gaussian integers above, then the domain is known as *norm-Euclidean*. The norm-Euclidean rings of quadratic integers are exactly those where D is one of the values −11, −7, −3, −2, −1, 2, 3, 5, 6, 7, 11, 13, 17, 19, 21, 29, 33, 37, 41, 57, or 73. The cases *D* = −1 and *D* = −3 yield the Gaussian integers and Eisenstein integers, respectively.

If f is allowed to be any Euclidean function, then the list of possible values of D for which the domain is Euclidean is not yet known. The first example of a Euclidean domain that was not norm-Euclidean (with *D* = 69) was published in 1994. In 1973, Weinberger proved that a quadratic integer ring with *D* > 0 is Euclidean if, and only if, it is a principal ideal domain, provided that the generalized Riemann hypothesis holds.

### Noncommutative rings

The Euclidean algorithm may be applied to some noncommutative rings such as the set of Hurwitz quaternions. Let α and β represent two elements from such a ring. They have a common right divisor δ if *α* = *ξδ* and *β* = *ηδ* for some choice of ξ and η in the ring. Similarly, they have a common left divisor if *α* = *dξ* and *β* = *dη* for some choice of ξ and η in the ring. Since multiplication is not commutative, there are two versions of the Euclidean algorithm, one for right divisors and one for left divisors. Choosing the right divisors, the first step in finding the gcd(*α*, *β*) by the Euclidean algorithm can be written

$\rho _{0}=\alpha -\psi _{0}\beta =(\xi -\psi _{0}\eta )\delta ,$

where *ψ*0 represents the quotient and *ρ*0 the remainder. Here the quotient and remainder are chosen so that (if nonzero) the remainder has *N*(*ρ*0) < *N*(*β*) for a "Euclidean function" *N* defined analogously to the Euclidean functions of Euclidean domains in the non-commutative case. This equation shows that any common right divisor of α and β is likewise a common divisor of the remainder *ρ*0. The analogous equation for the left divisors would be

$\rho _{0}=\alpha -\beta \psi _{0}=\delta (\xi -\eta \psi _{0}).$

With either choice, the process is repeated as above until the greatest common right or left divisor is identified. As in the Euclidean domain, the "size" of the remainder *ρ*0 (formally, its Euclidean function or "norm") must be strictly smaller than β, and there must be only a finite number of possible sizes for *ρ*0, so that the algorithm is guaranteed to terminate.

Many results for the GCD carry over to noncommutative numbers. For example, Bézout's identity states that the right gcd(*α*, *β*) can be expressed as a linear combination of α and β. In other words, there are numbers σ and τ such that

$\Gamma _{\text{right}}=\sigma \alpha +\tau \beta .$

The analogous identity for the left GCD is nearly the same:

$\Gamma _{\text{left}}=\alpha \sigma +\beta \tau .$

Bézout's identity can be used to solve Diophantine equations. For instance, one of the standard proofs of Lagrange's four-square theorem, that every positive integer can be represented as a sum of four squares, is based on quaternion GCDs in this way.
