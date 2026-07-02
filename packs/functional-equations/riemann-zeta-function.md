---
title: "Riemann zeta function"
source: https://en.wikipedia.org/wiki/Riemann_zeta_function
domain: functional-equations
license: CC-BY-SA-4.0
tags: functional equation, cauchy functional equation, recurrence relation, generating function
fetched: 2026-07-02
---

# Riemann zeta function

The **Riemann zeta function** or **Euler–Riemann zeta function**, denoted by the lowercase Greek letter *ζ* (zeta), is a mathematical function of a complex variable defined as $\zeta (s)=\sum _{n=1}^{\infty }{\frac {1}{n^{s}}}={\frac {1}{1^{s}}}+{\frac {1}{2^{s}}}+{\frac {1}{3^{s}}}+\cdots$ for $\mathrm {Re} (s)>1$ , and its analytic continuation elsewhere.

The Riemann zeta function plays a pivotal role in analytic number theory and has applications in physics, probability theory, and applied statistics.

Leonhard Euler first introduced and studied the function over the reals in the first half of the eighteenth century. Bernhard Riemann's 1859 article "On the Number of Primes Less Than a Given Magnitude" extended the Euler definition to a complex variable, proved its meromorphic continuation and functional equation, and established a relation between its zeros and the distribution of prime numbers. This paper also contained the Riemann hypothesis, a conjecture about the distribution of complex zeros of the Riemann zeta function that many mathematicians consider the most important unsolved problem in pure mathematics.

The values of the Riemann zeta function at even positive integers were computed by Euler. The first of them, *ζ*(2), provides a solution to the Basel problem. In 1979, Roger Apéry proved the irrationality of *ζ*(3), and as a consequence, the number was named after him. The values at negative integer points, also found by Euler, are rational numbers and play an important role in the theory of modular forms. Many generalizations of the Riemann zeta function, such as Dirichlet series, Dirichlet *L*-functions and *L*-functions, are known.

## Definition

The Riemann zeta function *ζ*(*s*) is a function of a complex variable *s* = *σ* + *it*, where *σ* and *t* are real numbers. (The notation *s*, *σ*, and *t* is used traditionally in the study of the zeta function, following Riemann.) When Re(*s*) = *σ* > 1, the function can be written as a converging summation or as an integral:

$\zeta (s)=\sum _{n=1}^{\infty }{\frac {1}{n^{s}}}={\frac {1}{\Gamma (s)}}\int _{0}^{\infty }{\frac {x^{s-1}}{e^{x}-1}}\,\mathrm {d} x\,,$

where

$\Gamma (s)=\int _{0}^{\infty }x^{s-1}\,e^{-x}\,\mathrm {d} x$

is the gamma function. The Riemann zeta function is defined for other complex values via analytic continuation of the function defined for *σ* > 1.

Leonhard Euler considered the above series in 1740 for positive integer values of *s*, and later Chebyshev extended the definition to Re(*s*) > 1.

The above series is a prototypical Dirichlet series that converges absolutely to an analytic function for *s* such that *σ* > 1 and diverges for all other values of *s*. Riemann showed that the function defined by the series on the half-plane of convergence can be continued analytically to all complex values *s* ≠ 1. For *s* = 1, the series is the harmonic series which diverges to +∞, and $\lim _{s\to 1}(s-1)\zeta (s)=1.$ Thus the Riemann zeta function is a meromorphic function on the whole complex plane, which is holomorphic everywhere except for a simple pole at *s* = 1 with residue 1.

## Euler's product formula

In 1737, the connection between the zeta function and prime numbers was discovered by Euler, who proved the identity

$\sum _{n=1}^{\infty }{\frac {1}{n^{s}}}=\prod _{p{\text{ prime}}}{\frac {1}{1-p^{-s}}},$

where, by definition, the left hand side is *ζ*(*s*) and the infinite product on the right hand side extends over all prime numbers *p* (such expressions are called Euler products):

$\prod _{p{\text{ prime}}}{\frac {1}{1-p^{-s}}}={\frac {1}{1-2^{-s}}}\cdot {\frac {1}{1-3^{-s}}}\cdot {\frac {1}{1-5^{-s}}}\cdot {\frac {1}{1-7^{-s}}}\cdot {\frac {1}{1-11^{-s}}}\cdots {\frac {1}{1-p^{-s}}}\cdots$

Both sides of the Euler product formula converge for Re(*s*) > 1. The proof of Euler's identity uses only the formula for the geometric series and the fundamental theorem of arithmetic. Since the harmonic series, obtained when *s* = 1, diverges, Euler's formula (which becomes Π*p* ⁠*p*/*p* − 1⁠) implies that there are infinitely many primes. Since the logarithm of *p*/(*p* − 1) is approximately 1/*p*, the formula can also be used to prove the stronger result that the sum of the reciprocals of the primes is infinite. On the other hand, combining that with the sieve of Eratosthenes shows that the density of the set of primes within the set of positive integers is zero.

The Euler product formula can be used to calculate the asymptotic probability that *s* randomly selected integers within a bound are set-wise coprime. Intuitively, the probability that any single number is divisible by a prime (or any integer) *p* is 1/*p*. Hence the probability that *s* numbers are all divisible by this prime is 1/*p**s*, and the probability that at least one of them is *not* is 1 − 1/*p**s*. Now, for distinct primes, these divisibility events are mutually independent because the candidate divisors are coprime (a number is divisible by coprime divisors *n* and *m* if and only if it is divisible by *nm*, an event which occurs with probability 1/(*nm*)). Thus the asymptotic probability that *s* numbers are coprime is given by a product over all primes,

$\prod _{p{\text{ prime}}}\left(1-{\frac {1}{p^{s}}}\right)=\left(\prod _{p{\text{ prime}}}{\frac {1}{1-p^{-s}}}\right)^{-1}={\frac {1}{\zeta (s)}}.$

## Riemann's functional equation

This zeta function satisfies the functional equation $\zeta (s)=2^{s}\pi ^{s-1}\ \sin \left({\frac {\pi s}{2}}\right)\ \Gamma (1-s)\ \zeta (1-s)\ ,$ where Γ(*s*) is the gamma function. This is an equality of meromorphic functions valid on the whole complex plane. The equation relates values of the Riemann zeta function at the points *s* and 1 − *s*, in particular relating even positive integers with odd negative integers. Owing to the zeros of the sine function, the functional equation implies that *ζ*(*s*) has a simple zero at each even negative integer *s* = −2*n*, known as the **trivial zeros** of *ζ*(*s*). When *s* is an even positive integer, the product $\sin \left({\frac {\pi s}{2}}\right)\Gamma (1-s)$ on the right is non-zero because Γ(1 − *s*) has a simple pole, which cancels the simple zero of the sine factor. When *s* is 0, the zero of the sine factor is cancelled by the simple pole of *ζ*(1).

| Proof of Riemann's functional equation |
|---|
| A proof of the functional equation proceeds as follows: We observe that if Re(*s*) > 0, then $\int _{0}^{\infty }x^{{\frac {1}{2}}s-1}e^{-n^{2}\pi x}\ \mathrm {d} x\ =\ {\frac {\ \Gamma \!\left({\frac {s}{2}}\right)\ }{\ n^{s}\ \pi ^{\frac {s}{2}}\ }}~.$ As a result, if Re(*s*) > 1 then ${\frac {\ \Gamma \!\left({\frac {s}{2}}\right)\ \zeta (s)\ }{\ \pi ^{\frac {s}{2}}\ }}\ =\ \sum _{n=1}^{\infty }\ \int _{0}^{\infty }\ x^{{s \over 2}-1}\ e^{-n^{2}\pi x}\ \mathrm {d} x\ =\ \int _{0}^{\infty }x^{{s \over 2}-1}\sum _{n=1}^{\infty }e^{-n^{2}\pi x}\ \mathrm {d} x\ ,$ with the inversion of the limiting processes justified by absolute convergence (hence the stricter requirement on s ). For convenience, let $\psi (x)\ :=\ \sum _{n=1}^{\infty }\ e^{-n^{2}\pi x},$ which is a special case of the theta function. Because $e^{-n^{2}\pi x}$ and ${\frac {1}{\sqrt {x}}}e^{\frac {-n^{2}\pi }{x}}$ are Fourier transform pairs, then, by the Poisson summation formula, we have $\sum _{n=-\infty }^{\infty }\ e^{-n^{2}\pi \ x}\ =\ {\frac {1}{\ {\sqrt {x\ }}\ }}\ \sum _{n=-\infty }^{\infty }\ e^{-{\frac {\ n^{2}\pi \ }{x}}}\ ,$ so that $\ 2\ \psi (x)+1\ =\ {\frac {1}{\ {\sqrt {x\ }}\ }}\left(\ 2\ \psi \!\left({\frac {1}{x}}\right)+1\ \right)~.$ Hence $\pi ^{-{\frac {s}{2}}}\ \Gamma \!\left({\frac {s}{2}}\right)\ \zeta (s)\ =\ \int _{0}^{1}\ x^{{\frac {s}{2}}-1}\ \psi (x)\ \mathrm {d} x+\int _{1}^{\infty }x^{{\frac {s}{2}}-1}\psi (x)\ \mathrm {d} x~.$ The right side is equivalent to $\int _{0}^{1}x^{{\frac {s}{2}}-1}\left({\frac {1}{\ {\sqrt {x\ }}\ }}\ \psi \!\left({\frac {1}{x}}\right)+{\frac {1}{\ 2{\sqrt {x\ }}\ }}-{\frac {1}{2}}\ \right)\ \mathrm {d} x+\int _{1}^{\infty }x^{{s \over 2}-1}\psi (x)\ \mathrm {d} x$ or ${\frac {1}{\ s-1\ }}-{\frac {1}{\ s\ }}+\int _{0}^{1}\ x^{{\frac {s}{2}}-{\frac {3}{2}}}\ \psi \!\left({\frac {1}{\ x\ }}\right)\ \mathrm {d} x+\int _{1}^{\infty }\ x^{{\frac {s}{2}}-1}\ \psi (x)\ \mathrm {d} x~.$ So $\pi ^{-{\frac {s}{2}}}\ \Gamma \!\left({\frac {\ s\ }{2}}\right)\ \zeta (s)\ =\ {\frac {1}{\ s(s-1)\ }}+\int _{1}^{\infty }\ \left(x^{-{\frac {s}{2}}-{\frac {1}{2}}}+x^{{\frac {s}{2}}-1}\right)\ \psi (x)\ \mathrm {d} x$ which is convergent for all *s*, because *ψ*(*x*) → 0 more quickly than any power of *x* for *x* > 1, so the integral converges. As the RHS remains the same if *s* is replaced by 1 − *s*, ${\frac {\ \Gamma \!\left(\ {\frac {s}{2}}\ \right)\ \zeta \!\left(\ s\ \right)\ }{\ \pi ^{{\frac {s}{2}}\ }\ }}\ =\ {\frac {\ \Gamma \!\left(\ {\frac {1}{2}}-{\frac {s}{2}}\ \right)\ \zeta \!\left(\ 1-s\ \right)\ }{\ \pi ^{{\frac {1}{2}}-{\frac {s}{2}}}\ }}$ which is the functional equation attributed to Bernhard Riemann. The functional equation above can be obtained using both the reflection formula and the duplication formula. First collect terms of *π*: $\Gamma \left({\frac {s}{2}}\right)\zeta \left(s\right)=\Gamma \left({\frac {1}{2}}-{\frac {s}{2}}\right)\zeta \left(1-s\right)\pi ^{s-{\frac {1}{2}}}$ Then multiply both sides by Γ(1 − *s*/2) and use the reflection formula: $\Gamma \left(1-{\frac {s}{2}}\right)\Gamma \left({\frac {s}{2}}\right)\zeta \left(s\right)=\Gamma \left(1-{\frac {s}{2}}\right)\Gamma \left({\frac {1}{2}}-{\frac {s}{2}}\right)\zeta \left(1-s\right)\pi ^{s-{\frac {1}{2}}}$ $\zeta \left(s\right)=\sin \left({\frac {\pi s}{2}}\right)\Gamma \left(1-{\frac {s}{2}}\right)\Gamma \left({\frac {1}{2}}-{\frac {s}{2}}\right)\zeta \left(1-s\right)\pi ^{s-{\frac {3}{2}}}$ Use the duplication formula with *z* = (1 − *s*)/2 $\zeta \left(s\right)=\sin \left({\frac {\pi s}{2}}\right)2^{1-1+s}{\sqrt {\pi }}\Gamma \left(1-s\right)\zeta \left(1-s\right)\pi ^{s-{\frac {3}{2}}}$ so that $\zeta \left(s\right)=\sin \left({\frac {\pi s}{2}}\right)2^{s}\Gamma \left(1-s\right)\zeta \left(1-s\right)\pi ^{s-1}$ |

The functional equation was established by Riemann in his 1859 paper "On the Number of Primes Less Than a Given Magnitude" and used to construct the analytic continuation in the first place.

In the adelic formulation developed in Tate's thesis, the so-called Gamma factor $\pi ^{-s/2}\Gamma (s/2)$ is interpreted as the local zeta factor at the Archimedean place.

## Riemann's xi function

Riemann also found a symmetric version of the functional equation by setting $\xi (s)={\frac {s(s-1)}{2}}\times \pi ^{-{\frac {s}{2}}}\Gamma \left({\frac {s}{2}}\right)\zeta (s)=(s-1)\pi ^{-{\frac {s}{2}}}\Gamma \left({\frac {s}{2}}+1\right)\zeta (s)$ that satisfies: $\xi (s)=\xi (1-s)~.$

Returning to the functional equation's derivation in the previous section, we have $\xi (s)={\frac {1}{2}}+{\frac {s(s-1)}{2}}\int _{1}^{\infty }\left(x^{-{\frac {s}{2}}-{\frac {1}{2}}}+x^{{\frac {s}{2}}-1}\right)\psi (x)dx$

Using integration by parts, $\xi (s)={\frac {1}{2}}-\left[\left(sx^{\frac {1-s}{2}}+(1-s)x^{\frac {s}{2}}\right)\psi (x)\right]_{1}^{\infty }+\int _{1}^{\infty }\left(sx^{\frac {1-s}{2}}+(1-s)x^{\frac {s}{2}}\right)\psi '(x)dx$ $\xi (s)={\frac {1}{2}}+\psi (1)+\int _{1}^{\infty }\left(sx^{\frac {1-s}{2}}+(1-s)x^{\frac {s}{2}}\right)\psi '(x)dx$

Using integration by parts again with a factorization of *x*3/2, $\xi (s)={\frac {1}{2}}+\psi (1)-2\left[x^{\frac {3}{2}}\psi '(x)\left(x^{\frac {s-1}{2}}+x^{-{\frac {s}{2}}}\right)\right]_{1}^{\infty }+2\int _{1}^{\infty }\left(x^{\frac {s-1}{2}}+x^{-{\frac {s}{2}}}\right){\frac {d}{dx}}\left[x^{\frac {3}{2}}\psi '(x)\right]dx$ $\xi (s)={\frac {1}{2}}+\psi (1)+4\psi '(1)+2\int _{1}^{\infty }{\frac {d}{dx}}\left[x^{\frac {3}{2}}\psi '(x)\right]\left(x^{\frac {s-1}{2}}+x^{-{\frac {s}{2}}}\right)dx$

As ${\frac {1}{2}}+\psi (1)+4\psi '(1)=0$ , $\xi (s)=2\int _{1}^{\infty }{\frac {d}{dx}}\left[x^{\frac {3}{2}}\psi '(x)\right]\left(x^{\frac {s-1}{2}}+x^{-{\frac {s}{2}}}\right)dx$

Remove a factor of *x*−1/4 to make the exponents in the remainder opposites. $\xi (s)=2\int _{1}^{\infty }{\frac {d}{dx}}\left[x^{\frac {3}{2}}\psi '(x)\right]x^{-{\frac {1}{4}}}\left(x^{\frac {s-1/2}{2}}+x^{\frac {1/2-s}{2}}\right)dx$

Using the hyperbolic functions, namely cos(*x*) = cosh(*ix*), and letting *s* = 1/2 + *it* gives $\xi (s)=4\int _{1}^{\infty }{\frac {d}{dx}}\left[x^{\frac {3}{2}}\psi '(x)\right]x^{-{\frac {1}{4}}}\cos({\frac {t}{2}}\log x)dx$ and by separating the integral and using the power series for cos, $\xi (s)=\sum _{n=0}^{\infty }a_{2n}t^{2n}$ which led Riemann to his famous hypothesis.

## Zeros, the critical line, and the Riemann hypothesis

The functional equation shows that the Riemann zeta function has zeros at −2, −4, .... These are called the **trivial zeros**. They are trivial in the sense that their existence is relatively easy to prove, for example, from sin(*πs*/2) being 0 in the functional equation. The non-trivial zeros have captured far more attention because their distribution not only is far less understood but, more importantly, their study yields important results concerning prime numbers and related objects in number theory. It is known that any non-trivial zero lies in the open strip {*s* ∈ $\mathbb {C}$ | 0 < Re(*s*) < 1}, which is called the **critical strip**. The set {*s* ∈ $\mathbb {C}$ | Re(*s*) = 1/2} is called the **critical line**. The Riemann hypothesis, considered one of the greatest unsolved problems in mathematics, asserts that all non-trivial zeros are on the critical line. In 1989, Conrey proved that more than 40% of the non-trivial zeros of the Riemann zeta function are on the critical line. This has since been improved to 41.7%.

For the Riemann zeta function on the critical line, see *Z*-function.

| Zero |
|---|
| 1/2 ± 14.134725... *i* |
| 1/2 ± 21.022040... *i* |
| 1/2 ± 25.010858... *i* |
| 1/2 ± 30.424876... *i* |
| 1/2 ± 32.935062... *i* |
| 1/2 ± 37.586178... *i* |
| 1/2 ± 40.918719... *i* |

### Number of zeros in the critical strip

Let *N*(*T*) be the number of zeros of *ζ*(*s*) in the critical strip 0 < Re(*s*) < 1, whose imaginary parts are in the interval 0 < Im(*s*) < *T*. Timothy Trudgian proved that, if *T* > *e*, then

$\left|N(T)-{\frac {T}{2\pi }}\log {\frac {T}{2\pi e}}\right|\leq 0.112\log T+0.278\log \log T+3.385+{\frac {0.2}{T}}$

.

### Hardy–Littlewood conjectures

In 1914, G. H. Hardy proved that *ζ*(⁠1/2⁠ + *it*) has infinitely many real zeros.

Hardy and J. E. Littlewood formulated two conjectures on the density and distance between the zeros of *ζ*(1/2 + *it*) on intervals of large positive real numbers. In the following, *N*(*T*) is the total number of real zeros and *N*0(*T*) the total number of zeros of odd order of the function *ζ*(1/2 + *it*) lying in the interval (0, *T*].

1. For any *ε* > 0, there exists a *T*0(*ε*) > 0 such that when $T\geq T_{0}(\varepsilon )\quad {\text{ and }}\quad H=T^{{\frac {1}{4}}+\varepsilon },$ the interval (*T*, *T* + *H*] contains a zero of odd order.
2. For any *ε* > 0, there exists a *T*0(*ε*) > 0 and *c**ε* > 0 such that the inequality $N_{0}(T+H)-N_{0}(T)\geq c_{\varepsilon }H$ holds when $T\geq T_{0}(\varepsilon )\quad {\text{ and }}\quad H=T^{{\frac {1}{2}}+\varepsilon }.$

These two conjectures opened up new directions in the investigation of the Riemann zeta function.

### Zero-free region

The location of the Riemann zeta function's zeros is of great importance in number theory. The prime number theorem is equivalent to the fact that there are no zeros of the zeta function on the line Re(*s*) = 1. It is also known that zeros do not exist in certain regions slightly to the left of the line Re(*s*) = 1, known as zero-free regions. For instance, Korobov and Vinogradov independently showed via the Vinogradov's mean-value theorem that for sufficiently large |*t*|, *ζ*(*σ* + *it*) ≠ 0 for

$\sigma \geq 1-{\frac {c}{(\log |t|)^{2/3+\varepsilon }}}$

for any *ε* > 0 and a number *c* > 0 depending on *ε*. Asymptotically, this is the largest known zero-free region for the zeta function.

Explicit zero-free regions are also known. Platt and Trudgian verified computationally that *ζ*(*σ* + *it*) ≠ 0 if *σ* ≠ 1/2 and |*t*| ≤ 3⋅1012. Mossinghoff, Trudgian and Yang proved that zeta has no zeros in the region

$\sigma \geq 1-{\frac {1}{5.558691\log |t|}}$

for |*t*| ≥ 2, which is the largest known zero-free region in the critical strip for 3⋅1012 < |*t*| < exp(64.1) ≈ 7⋅1027 (for previous results see). Yang showed that *ζ*(*σ* + *it*) ≠ 0 if

$\sigma \geq 1-{\frac {\log \log |t|}{21.233\log |t|}}$

and

$|t|\geq 3$

which is the largest known zero-free region for exp(170.2) < |*t*| < exp(4.8⋅105). Bellotti proved (building on the work of Ford) the zero-free region

$\sigma \geq 1-{\frac {1}{53.989(\log |t|)^{2/3}(\log \log |t|)^{1/3}}}$

and

$|t|\geq 3$

.

This is the largest known zero-free region for fixed |*t*| ≥ exp(4.8⋅105). Bellotti also showed that for sufficiently large |*t*|, the following better result is known: *ζ*(*σ* + *it*) ≠ 0 for

$\sigma \geq 1-{\frac {1}{48.0718(\log |t|)^{2/3}(\log \log |t|)^{1/3}}}.$

The strongest result of this kind one can hope for is the truth of the Riemann hypothesis, which would have many profound consequences in the theory of numbers.

### Other results

It is known that there are infinitely many zeros on the critical line. Littlewood showed that if the sequence (*γn*) contains the imaginary parts of all zeros in the upper half-plane in ascending order, then

$\lim _{n\rightarrow \infty }\left(\gamma _{n+1}-\gamma _{n}\right)=0.$

The critical line theorem asserts that a positive proportion of the nontrivial zeros lies on the critical line. (The Riemann hypothesis would imply that this proportion is 1.)

In the critical strip, the zero with smallest non-negative imaginary part is 1/2 + 14.13472514... *i* (OEIS: A058303). The fact that, for all complex *s* ≠ 1,

$\zeta (s)={\overline {\zeta ({\overline {s}})}}$

implies that the zeros of the Riemann zeta function are symmetric about the real axis. Combining this symmetry with the functional equation, furthermore, one sees that the non-trivial zeros are symmetric about the critical line Re(*s*) = 1/2.

It is also known that no zeros lie on the line with real part 1.

A large class of modified zeta functions exists that share the same non-trivial zeros as the Riemann zeta function, where modification means replacing the prime numbers in the Euler product by real numbers, which was shown in a result by Grosswald and Schnitzer.

## Specific values

For any positive even integer 2*n*, $\zeta (2n)={\frac {|{B_{2n}}|(2\pi )^{2n}}{2(2n)!}},$ where *B*2*n* is the (2*n*)th Bernoulli number. The demonstration of the particular value $\zeta (2)=1+{\frac {1}{2^{2}}}+{\frac {1}{3^{2}}}+\cdots ={\frac {\pi ^{2}}{6}}$ is known as the Basel problem. The reciprocal of this sum answers the question: 'What is the probability that two numbers selected from a uniform distribution from 1 to *n*] are coprime as *n* → ∞?'

For odd positive integers, no such simple expression is known, although these values are thought to be related to the algebraic *K*-theory of the integers; see Special values of *L*-functions. The value $\zeta (3)=1+{\frac {1}{2^{3}}}+{\frac {1}{3^{3}}}+\cdots =1.202056903159594285399...$ is Apéry's constant.

For nonpositive integers, the series does not converge, but via analytic continuation one can show that $\zeta (-n)=-{\frac {B_{n+1}}{n+1}}$ for *n* ≥ 0 (using the convention that *B*1 = 1/2). In particular, *ζ* vanishes at the negative even integers because *B**m* = 0 for all odd *m* other than 1. These are the so-called "trivial zeros" of the zeta function. Another particular value is $\zeta (-1)=-{\tfrac {1}{12}}$ This gives a pretext for assigning a finite value to the divergent series 1 + 2 + 3 + 4 + ⋯, which has been used in certain contexts (Ramanujan summation) such as string theory. Analogously, $\zeta (0)=-{\tfrac {1}{2}}$ can be viewed as assigning a finite result to the divergent series 1 + 1 + 1 + 1 + ⋯.

The value $\zeta {\bigl (}{\tfrac {1}{2}}{\bigr )}=-1.46035450880958681288\ldots$ is employed in calculating kinetic boundary layer problems of linear kinetic equations.

Although $\zeta (1)=1+{\tfrac {1}{2}}+{\tfrac {1}{3}}+\cdots$ diverges, its Cauchy principal value $\lim _{\varepsilon \to 0}{\frac {\zeta (1+\varepsilon )+\zeta (1-\varepsilon )}{2}}$ exists and is equal to the Euler–Mascheroni constant *γ* = 0.5772....

Taking the limit *s* → +∞ through the real numbers, one obtains *ζ*(+∞) = 1. But at complex infinity on the Riemann sphere the zeta function has an essential singularity.

## Various properties

For sums involving the zeta function at integer and half-integer values, see rational zeta series.

### Reciprocal

The reciprocal of the zeta function may be expressed as a Dirichlet series over the Möbius function *μ*(*n*):

${\frac {1}{\zeta (s)}}=\sum _{n=1}^{\infty }{\frac {\mu (n)}{n^{s}}}$

for every complex number *s* with real part greater than 1. There are a number of similar relations involving various well-known multiplicative functions; these are given in the article on the Dirichlet series.

The Riemann hypothesis is equivalent to the claim that this expression is valid when the real part of *s* is greater than 1/2.

### Universality

The critical strip of the Riemann zeta function has the remarkable property of **universality**. This zeta function universality states, roughly, that vertical translates of $\zeta (s)$ can uniformly approximate any nonvanishing holomorphic function on suitable compact subsets of the strip $1/2<\operatorname {Re} (s)<1$ . Since holomorphic functions are very general, this property is quite remarkable. The first proof of universality was provided by Sergei Mikhailovitch Voronin in 1975. More recent work has included effective versions of Voronin's theorem and extending it to Dirichlet *L*-functions.

### Estimates of the maximum of the modulus of the zeta function

Let the functions *F*(*T*; *H*) and *G*(*s*0; Δ) be defined by the equalities

$F(T;H)=\max _{|t-T|\leq H}\left|\zeta \left({\tfrac {1}{2}}+it\right)\right|,\qquad G(s_{0};\Delta )=\max _{|s-s_{0}|\leq \Delta }|\zeta (s)|.$

Here *T* is a sufficiently large positive number, 0 < *H* ≪ log log *T*, *s*0 = *σ*0 + *iT*, 1/2 ≤ *σ*0 ≤ 1, 0 < Δ < 1/3. Estimating the values *F* and *G* from below shows, how large (in modulus) values *ζ*(*s*) can take on short intervals of the critical line or in small neighborhoods of points lying in the critical strip 0 ≤ Re(*s*) ≤ 1.

The case *H* ≫ log log *T* was studied by Kanakanahalli Ramachandra; the case Δ > *c*, where *c* is a sufficiently large constant, is trivial.

Anatolii Karatsuba proved, in particular, that if the values *H* and Δ exceed certain sufficiently small constants, then the estimates

$F(T;H)\geq T^{-c_{1}},\qquad G(s_{0};\Delta )\geq T^{-c_{2}},$

hold, where *c*1 and *c*2 are certain absolute constants.

### Argument of the Riemann zeta function

The function

$S(t)={\frac {1}{\pi }}\arg {\zeta \left({\tfrac {1}{2}}+it\right)}$

is called the argument of the Riemann zeta function. Here arg *ζ*(1/2 + *it*) is the increment of an arbitrary continuous branch of arg *ζ*(*s*) along the broken line joining the points 2, 2 + *it* and 1/2 + *it*.

There are some theorems on properties of the function *S*(*t*). Among those results are the mean value theorems for *S*(*t*) and its first integral

$S_{1}(t)=\int _{0}^{t}S(u)\,\mathrm {d} u$

on intervals of the real line, and also the theorem claiming that every interval (*T*, *T* + *H*] for

$H\geq T^{{\frac {27}{82}}+\varepsilon }$

contains at least

$H{\sqrt[{3}]{\ln T}}e^{-c{\sqrt {\ln \ln T}}}$

points where the function *S*(*t*) changes sign. Earlier similar results were obtained by Atle Selberg for the case

$H\geq T^{{\frac {1}{2}}+\varepsilon }.$

## Representations

### Dirichlet series

An extension of the area of convergence can be obtained by rearranging the original series. The series

$\zeta (s)={\frac {1}{s-1}}\sum _{n=1}^{\infty }\left({\frac {n}{(n+1)^{s}}}-{\frac {n-s}{n^{s}}}\right)$

converges for Re(*s*) > 0, while

$\zeta (s)={\frac {1}{s-1}}\sum _{n=1}^{\infty }{\frac {n(n+1)}{2}}\left({\frac {2n+3+s}{(n+1)^{s+2}}}-{\frac {2n-1-s}{n^{s+2}}}\right)$

converge even for Re(*s*) > −1. In this way, the area of convergence can be extended to Re(*s*) > −*k* for any negative integer −*k*.

The recurrence connection is clearly visible from the expression valid for Re(*s*) > −2 enabling further expansion by integration by parts.

${\begin{aligned}\zeta (s)=&1+{\frac {1}{s-1}}-{\frac {s}{2!}}[\zeta (s+1)-1]\\-&{\frac {s(s+1)}{3!}}[\zeta (s+2)-1]\\&-{\frac {s(s+1)(s+2)}{3!}}\sum _{n=1}^{\infty }\int _{0}^{1}{\frac {t^{3}dt}{(n+t)^{s+3}}}.\end{aligned}}$

This recurrence leads to this other series development that uses the rising factorial and is valid for the entire complex plane

$\zeta (s)={\frac {s}{s-1}}-\sum _{n=1}^{\infty }{\bigl (}\zeta (s+n)-1{\bigr )}{\frac {s(s+1)\cdots (s+n-1)}{(n+1)!}}.$

This can be used recursively to extend the Dirichlet series definition to all complex numbers.

The Riemann zeta function also appears in a form similar to the Mellin transform in an integral over the Gauss–Kuzmin–Wirsing operator acting on *x**s*−1; that context gives rise to a series expansion in terms of the falling factorial.

### Mellin-type integrals

The Mellin transform of a function *f*(*x*) is defined as

$\int _{0}^{\infty }f(x)x^{s}\,{\frac {\mathrm {d} x}{x}}$

in the region where the integral is defined. There are various expressions for the zeta function as Mellin transform-like integrals. If the real part of *s* is greater than one, we have

$\Gamma (s)\zeta (s)=\int _{0}^{\infty }{\frac {x^{s-1}}{e^{x}-1}}\,\mathrm {d} x\quad$

and

$\quad \Gamma (s)\zeta (s)={\frac {1}{2s}}\int _{0}^{\infty }{\frac {x^{s}}{\cosh(x)-1}}\,\mathrm {d} x,$

where Γ denotes the gamma function. By modifying the contour, Riemann showed that

$2\sin(\pi s)\Gamma (s)\zeta (s)=i\oint _{H}{\frac {(-x)^{s-1}}{e^{x}-1}}\,\mathrm {d} x$

for all *s* (where *H* denotes the Hankel contour).

We can also find expressions which relate to prime numbers and the prime number theorem. If *π*(*x*) is the prime-counting function, then

$\ln \zeta (s)=s\int _{0}^{\infty }{\frac {\pi (x)}{x(x^{s}-1)}}\,\mathrm {d} x,$

for values with Re(*s*) > 1.

A similar Mellin transform involves the Riemann function *J*(*x*), which counts prime powers *p**n* with a weight of 1/*n*, so that

$J(x)=\sum {\frac {\pi \left(x^{\frac {1}{n}}\right)}{n}}.$

Now

$\ln \zeta (s)=s\int _{0}^{\infty }J(x)x^{-s-1}\,\mathrm {d} x.$

These expressions can be used to prove the prime number theorem by means of the inverse Mellin transform. Riemann's prime-counting function is easier to work with, and *π*(*x*) can be recovered from it by Möbius inversion.

### Theta functions

The Riemann zeta function can be given by a Mellin transform

$2\pi ^{-{\frac {s}{2}}}\Gamma \left({\frac {s}{2}}\right)\zeta (s)=\int _{0}^{\infty }{\bigl (}\theta (it)-1{\bigr )}t^{{\frac {s}{2}}-1}\,\mathrm {d} t,$

in terms of Jacobi's theta function

$\theta (\tau )=\sum _{n=-\infty }^{\infty }e^{\pi in^{2}\tau }.$

However, this integral only converges if the real part of *s* is greater than 1, but it can be regularized. This gives the following expression for the zeta function, which is well defined for all *s* except 0 and 1:

$\pi ^{-{\frac {s}{2}}}\Gamma \left({\frac {s}{2}}\right)\zeta (s)={\frac {1}{s-1}}-{\frac {1}{s}}+{\frac {1}{2}}\int _{0}^{1}\left(\theta (it)-t^{-{\frac {1}{2}}}\right)t^{{\frac {s}{2}}-1}\,\mathrm {d} t+{\frac {1}{2}}\int _{1}^{\infty }{\bigl (}\theta (it)-1{\bigr )}t^{{\frac {s}{2}}-1}\,\mathrm {d} t.$

### Laurent series

The Riemann zeta function is meromorphic with a single pole of order one at *s* = 1. It can therefore be expanded as a Laurent series about *s* = 1; the series development is then

$\zeta (s)={\frac {1}{s-1}}+\sum _{n=0}^{\infty }{\frac {\gamma _{n}}{n!}}(1-s)^{n}.$

The constants *γ**n* here are called the Stieltjes constants and can be defined by the limit

$\gamma _{n}=\lim _{m\rightarrow \infty }{\left(\left(\sum _{k=1}^{m}{\frac {(\ln k)^{n}}{k}}\right)-{\frac {(\ln m)^{n+1}}{n+1}}\right)}.$

The constant term *γ*0 is the Euler–Mascheroni constant.

### Integral

For all *s* ∈ $\mathbb {C}$ , *s* ≠ 1, the integral relation (cf. Abel–Plana formula)

$\zeta (s)={\frac {1}{s-1}}+{\frac {1}{2}}+2\int _{0}^{\infty }{\frac {\sin(s\arctan t)}{\left(1+t^{2}\right)^{s/2}\left(e^{2\pi t}-1\right)\ }}\ \operatorname {d} t$

holds true, which may be used for a numerical evaluation of the zeta function.

### Hadamard product

On the basis of Weierstrass's factorization theorem, Hadamard gave the infinite product expansion

$\zeta (s)={\frac {e^{\left(\log(2\pi )-1-{\frac {\gamma }{2}}\right)s}}{2(s-1)\Gamma \left(1+{\frac {s}{2}}\right)}}\prod _{\rho }\left(1-{\frac {s}{\rho }}\right)e^{\frac {s}{\rho }},$

where the product is over the non-trivial zeros *ρ* of *ζ* and the letter *γ* again denotes the Euler–Mascheroni constant. A simpler infinite product expansion is

$\zeta (s)=\pi ^{\frac {s}{2}}{\frac {\prod _{\rho }\left(1-{\frac {s}{\rho }}\right)}{2(s-1)\Gamma \left(1+{\frac {s}{2}}\right)}}.$

This form clearly displays the simple pole at *s* = 1, the trivial zeros at −2, −4, ... due to the gamma function term in the denominator, and the non-trivial zeros at *s* = *ρ*. (To ensure convergence in the latter formula, the product should be taken over "matching pairs" of zeros, i.e. the factors for a pair of zeros of the form *ρ* and 1 − *ρ* should be combined.)

### Globally convergent series

A globally convergent series for the zeta function, valid for all complex numbers *s* except *s* = 1 + ⁠2π*i*/ln 2⁠*n* for some integer *n*, was conjectured by Konrad Knopp in 1926 and proven by Helmut Hasse in 1930 (cf. Euler summation):

$\zeta (s)={\frac {1}{1-2^{1-s}}}\sum _{n=0}^{\infty }{\frac {1}{2^{n+1}}}\sum _{k=0}^{n}{\binom {n}{k}}{\frac {(-1)^{k}}{(k+1)^{s}}}.$

The series appeared in an appendix to Hasse's paper, and was published for the second time by Jonathan Sondow in 1994.

Hasse also proved the globally converging series

$\zeta (s)={\frac {1}{s-1}}\sum _{n=0}^{\infty }{\frac {1}{n+1}}\sum _{k=0}^{n}{\binom {n}{k}}{\frac {(-1)^{k}}{(k+1)^{s-1}}}$

in the same publication. Research by Iaroslav Blagouchine has found that a similar, equivalent series was published by Joseph Ser in 1926.

In 1997 K. Maślanka gave another globally convergent (except *s* = 1) series for the Riemann zeta function:

$\zeta (s)={\frac {1}{s-1}}\sum _{k=0}^{\infty }{\biggl (}\prod _{i=1}^{k}(i-{\frac {s}{2}}){\biggl )}{\frac {A_{k}}{k!}}={\frac {1}{s-1}}\sum _{k=0}^{\infty }{\biggl (}1-{\frac {s}{2}}{\biggl )}_{k}{\frac {A_{k}}{k!}}$

where real coefficients $A_{k}$ are given by:

$A_{k}=\sum _{j=0}^{k}(-1)^{j}{\binom {k}{j}}(2j+1)\zeta (2j+2)=\sum _{j=0}^{k}{\binom {k}{j}}{\frac {B_{2j+2}\pi ^{2j+2}}{\left(2\right)_{j}\left({\frac {1}{2}}\right)_{j}}}$

Here *B**n* are the Bernoulli numbers and (*x*)*k* denotes the Pochhammer symbol.

Note that this representation of the zeta function is essentially an interpolation with nodes, where the nodes are points *s* = 2, 4, 6, ..., i.e. exactly those where the zeta values are precisely known, as Euler showed. An elegant and very short proof of this representation of the zeta function, based on Carlson's theorem, was presented by Philippe Flajolet in 2006.

The asymptotic behavior of the coefficients $A_{k}$ is rather curious: for growing k values, we observe regular oscillations with a nearly exponentially decreasing amplitude and slowly decreasing frequency (roughly as $k^{-2/3}$ ). Using the saddle point method, we can show that

$A_{k}\sim {\frac {4\pi ^{3/2}}{\sqrt {3\kappa }}}\exp {\biggl (}-{\frac {3\kappa }{2}}+{\frac {\pi ^{2}}{4\kappa }}{\biggl )}\cos {\biggl (}{\frac {4\pi }{3}}-{\frac {3{\sqrt {3}}\kappa }{2}}+{\frac {{\sqrt {3}}\pi ^{2}}{4\kappa }}{\biggl )}$

where $\kappa$ stands for:

$\kappa :={\sqrt[{3}]{\pi ^{2}k}}$

(see for details).

On the basis of this representation, in 2003 Luis Báez-Duarte provided a new criterion for the Riemann hypothesis. Namely, if we define the coefficients *c**k* as

$c_{k}:=\sum _{j=0}^{k}(-1)^{j}{\binom {k}{j}}{\frac {1}{\zeta (2j+2)}}$

then the Riemann hypothesis is equivalent to

$c_{k}={\mathcal {O}}\left(k^{-3/4+\varepsilon }\right)\qquad (\forall \varepsilon >0)$

### Rapidly convergent series

Peter Borwein developed an algorithm that applies Chebyshev polynomials to the Dirichlet eta function to produce a very rapidly convergent series suitable for high precision numerical calculations.

### Series representation at positive integers via the primorial

$\zeta (k)={\frac {2^{k}}{2^{k}-1}}+\sum _{r=2}^{\infty }{\frac {(p_{r-1}\#)^{k}}{J_{k}(p_{r}\#)}}\qquad k=2,3,\ldots .$

Here *pn*# is the primorial sequence and *Jk* is Jordan's totient function.

### Series representation by the incomplete poly-Bernoulli numbers

The function *ζ* can be represented, for Re(*s*) > 1, by the infinite series

$\zeta (s)=\sum _{n=0}^{\infty }B_{n,\geq 2}^{(s)}{\frac {(W_{k}(-1))^{n}}{n!}},$

where *k* ∈ {−1, 0}, *Wk* is the kth branch of the Lambert W-function, and *B*(*μ*) *n*,≥2 is an incomplete poly-Bernoulli number.

### Mellin transform of the Engel map

The function *g*(*x*) = *x*(1 + ⌊*x*−1⌋) − 1 is iterated to find the coefficients appearing in Engel expansions.

The Mellin transform of the map $g(x)$ is related to the Riemann zeta function by the formula

${\begin{aligned}\int _{0}^{1}g(x)x^{s-1}\,dx&=\sum _{n=1}^{\infty }\int _{\frac {1}{n+1}}^{\frac {1}{n}}(x(n+1)-1)x^{s-1}\,dx\\[6pt]&=\sum _{n=1}^{\infty }{\frac {n^{-s}(s-1)+(n+1)^{-s-1}(n^{2}+2n+1)+n^{-s-1}s-n^{1-s}}{(s+1)s(n+1)}}\\[6pt]&={\frac {\zeta (s+1)}{s+1}}-{\frac {1}{s(s+1)}}\end{aligned}}$

### Stochastic representations

The Brownian motion and Riemann zeta function are connected through the moment-generating functions of stochastic processes derived from the Brownian motion.

## Numerical algorithms

A classical algorithm, in use prior to about 1930, proceeds by applying the Euler–Maclaurin formula to obtain, for positive integers *n* and *m*,

$\zeta (s)=\sum _{j=1}^{n-1}j^{-s}+{\tfrac {1}{2}}n^{-s}+{\frac {n^{1-s}}{s-1}}+\sum _{k=1}^{m}T_{k,n}(s)+E_{m,n}(s)$

where, letting $B_{2k}$ denote the indicated Bernoulli number,

$T_{k,n}(s)={\frac {B_{2k}}{(2k)!}}n^{1-s-2k}\prod _{j=0}^{2k-2}(s+j)$

and the error satisfies

$|E_{m,n}(s)|<\left|{\frac {s+2m+1}{\sigma +2m+1}}T_{m+1,n}(s)\right|,$

with *σ* = Re(*s*).

A modern numerical algorithm is the Odlyzko–Schönhage algorithm.

## Applications

The zeta function occurs in applied statistics including Zipf's law, Zipf–Mandelbrot law, and Lotka's law.

Zeta function regularization is used as one possible means of regularization of divergent series and divergent integrals in quantum field theory. In one notable example, the Riemann zeta function shows up explicitly in one method of calculating the Casimir effect. The zeta function is also useful for the analysis of dynamical systems.

### Musical tuning

In the theory of musical tunings, the zeta function can be used to find equal divisions of the octave (EDOs) that closely approximate the intervals of the harmonic series. For increasing values of $t\in \mathbb {R}$ , the value of

$\left\vert \zeta \left({\frac {1}{2}}+{\frac {2\pi {i}}{\ln {(2)}}}t\right)\right\vert$

peaks near integers that correspond to such EDOs. Examples include popular choices such as 12, 19, and 53.

### Infinite series

The zeta function evaluated at equidistant positive integers appears in infinite series representations of a number of constants.

- $\sum _{n=2}^{\infty }{\bigl (}\zeta (n)-1{\bigr )}=1$

In fact the even and odd terms give the two sums

- $\sum _{n=1}^{\infty }{\bigl (}\zeta (2n)-1{\bigr )}={\frac {3}{4}}$

and

- $\sum _{n=1}^{\infty }{\bigl (}\zeta (2n+1)-1{\bigr )}={\frac {1}{4}}$

Parametrized versions of the above sums are given by

- $\sum _{n=1}^{\infty }(\zeta (2n)-1)\,t^{2n}={\frac {t^{2}}{t^{2}-1}}+{\frac {1}{2}}\left(1-\pi t\cot(t\pi )\right)$

and

- $\sum _{n=1}^{\infty }(\zeta (2n+1)-1)\,t^{2n}={\frac {t^{2}}{t^{2}-1}}-{\frac {1}{2}}\left(\psi ^{0}(t)+\psi ^{0}(-t)\right)-\gamma$

with |*t*| < 2 and where $\psi$ and $\gamma$ are the polygamma function and Euler's constant, respectively, as well as

- $\sum _{n=1}^{\infty }{\frac {\zeta (2n)-1}{n}}\,t^{2n}=\log \left({\dfrac {1-t^{2}}{\operatorname {sinc} (\pi \,t)}}\right)$

all of which are continuous at $t=1$ . Other sums include

- $\sum _{n=2}^{\infty }{\frac {\zeta (n)-1}{n}}=1-\gamma$
- $\sum _{n=1}^{\infty }{\frac {\zeta (2n)-1}{n}}=\ln 2$
- $\sum _{n=2}^{\infty }{\frac {\zeta (n)-1}{n}}\left(\left({\tfrac {3}{2}}\right)^{n-1}-1\right)={\frac {1}{3}}\ln \pi$
- $\sum _{n=1}^{\infty }{\bigl (}\zeta (4n)-1{\bigr )}={\frac {7}{8}}-{\frac {\pi }{4}}\left({\frac {e^{2\pi }+1}{e^{2\pi }-1}}\right)$
- $\sum _{n=2}^{\infty }{\frac {\zeta (n)-1}{n}}\Im {\bigl (}(1+i)^{n}-1-i^{n}{\bigr )}={\frac {\pi }{4}}$

where $\Im$ denotes the imaginary part of a complex number.

Another interesting series that relates to the natural logarithm of the lemniscate constant is the following

- $\sum _{n=2}^{\infty }\left[{\frac {2(-1)^{n}\zeta (n)}{4^{n}n}}-{\frac {(-1)^{n}\zeta (n)}{2^{n}n}}\right]=\ln \left({\frac {\varpi }{2{\sqrt {2}}}}\right)$

There are yet more formulas in the article Harmonic number.

## Generalizations

There are a number of related zeta functions that can be considered to be generalizations of the Riemann zeta function. These include the Hurwitz zeta function

$\zeta (s,q)=\sum _{k=0}^{\infty }{\frac {1}{(k+q)^{s}}}$

(the convergent series representation was given by Helmut Hasse in 1930, cf. Hurwitz zeta function), which coincides with the Riemann zeta function when *q* = 1 (the lower limit of summation in the Hurwitz zeta function is 0, not 1), the Dirichlet *L*-functions and the Dedekind zeta function. For other related functions see the articles zeta function and *L*-function.

The polylogarithm is given by

$\operatorname {Li} _{s}(z)=\sum _{k=1}^{\infty }{\frac {z^{k}}{k^{s}}}$

which coincides with the Riemann zeta function when *z* = 1. The Clausen function Cl*s*(*θ*) can be chosen as the real or imaginary part of Li*s*(*e**iθ*).

The Lerch transcendent is given by

$\Phi (z,s,q)=\sum _{k=0}^{\infty }{\frac {z^{k}}{(k+q)^{s}}}$

which coincides with the Riemann zeta function when *z* = 1 and *q* = 1 (the lower limit of summation in the Lerch transcendent is 0, not 1).

The multiple zeta functions are defined by

$\zeta (s_{1},s_{2},\ldots ,s_{n})=\sum _{k_{1}>k_{2}>\cdots >k_{n}>0}{k_{1}}^{-s_{1}}{k_{2}}^{-s_{2}}\cdots {k_{n}}^{-s_{n}}.$

One can analytically continue these functions to the *n*-dimensional complex space. The special values taken by these functions at positive integer arguments are called multiple zeta values by number theorists and have been connected to many different branches in mathematics and physics.
