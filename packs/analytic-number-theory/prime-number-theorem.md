---
title: "Prime number theorem"
source: https://en.wikipedia.org/wiki/Prime_number_theorem
domain: analytic-number-theory
license: CC-BY-SA-4.0
tags: analytic number theory, prime number theorem, dirichlet series, riemann hypothesis
fetched: 2026-07-02
---

# Prime number theorem

In mathematics, the **prime number theorem** (**PNT**) describes the asymptotic distribution of prime numbers among the positive integers. It formalizes the intuitive idea that primes become less common as they become larger by precisely quantifying the rate at which this occurs. The theorem was proved independently by Jacques Hadamard and Charles Jean de la Vallée Poussin in 1896 using ideas introduced by Bernhard Riemann (in particular, the Riemann zeta function).

The first such distribution found is *π*(*N*) ~ ⁠*N*/log(*N*)⁠, where *π*(*N*) is the prime-counting function (the number of primes less than or equal to *N*) and log(*N*) is the natural logarithm of N. This means that for large enough N, the probability that a random integer not greater than N is prime is very close to 1 / log(*N*). In other words, the average gap between consecutive prime numbers among the first N integers is roughly log(*N*). Consequently, a random integer with at most 2*n* digits (for large enough n) is about half as likely to be prime as a random integer with at most n digits. For example, among the positive integers of at most 1000 digits, about one in 2300 is prime (log(101000) ≈ 2302.6), whereas among positive integers of at most 2000 digits, about one in 4600 is prime (log(102000) ≈ 4605.2).

## Statement

Let *π*(*x*) be the prime-counting function defined to be the number of primes less than or equal to x, for any real number x. For example, *π*(10) = 4 because there are four prime numbers (2, 3, 5 and 7) less than or equal to 10. The prime number theorem then states that *x* / log *x* is a good approximation to *π*(*x*) (where log here means the natural logarithm), in the sense that the limit of the *quotient* of the two functions *π*(*x*) and *x* / log *x* as x increases without bound is 1:

$\lim _{x\to \infty }{\frac {\;\pi (x)\;}{\;\left[{\frac {x}{\log(x)}}\right]\;}}=1,$

known as the **asymptotic law of distribution of prime numbers**. Using asymptotic notation this result can be restated as

$\pi (x)\sim {\frac {x}{\log x}}.$

This notation (and the theorem) does *not* say anything about the limit of the *difference* of the two functions as x increases without bound. Instead, the theorem states that *x* / log *x* approximates *π*(*x*) in the sense that the relative error of this approximation approaches 0 as x increases without bound.

The prime number theorem is equivalent to the statement that the nth prime number pn satisfies

$p_{n}\sim n\log(n),$

the asymptotic notation meaning, again, that the relative error of this approximation approaches 0 as n increases without bound. For example, the 2×1017th prime number is 8512677386048191063, and (2×1017)log(2×1017) rounds to 7967418752291744388, a relative error of about 6.4%.

On the other hand, the following asymptotic relations are logically equivalent:

${\begin{aligned}\lim _{x\rightarrow \infty }{\frac {\pi (x)\log x}{x}}&=1,{\text{ and}}\\\lim _{x\rightarrow \infty }{\frac {\pi (x)\log \pi (x)}{x}}\,&=1.\end{aligned}}$

As outlined below, the prime number theorem is also equivalent to

$\lim _{x\to \infty }{\frac {\vartheta (x)}{x}}=\lim _{x\to \infty }{\frac {\psi (x)}{x}}=1,$

where ϑ and ψ are the first and the second Chebyshev functions respectively, and to

$\lim _{x\to \infty }{\frac {M(x)}{x}}=0,$

where $M(x)=\sum _{n\leq x}\mu (n)$ is the Mertens function.

## History of the proof of the asymptotic law of prime numbers

Based on the tables by Anton Felkel and Jurij Vega, Adrien-Marie Legendre conjectured in 1797 or 1798 that *π*(*a*) is approximated by the function *a* / (*A* log *a* + *B*) , where A and B are unspecified constants. In the second edition of his book on number theory (1808) he then made a more precise conjecture, with *A* = 1 and *B* = −1.08366 . Carl Friedrich Gauss considered the same question at age 15 or 16 "in the year 1792 or 1793", according to his own recollection in 1849. In 1838 Peter Gustav Lejeune Dirichlet came up with his own approximating function, the logarithmic integral li(*x*) (under the slightly different form of a series, which he communicated to Gauss). Both Legendre's and Dirichlet's formulas imply the same conjectured asymptotic equivalence of *π*(*x*) and *x* / log(*x*) stated above, although it turned out that Dirichlet's approximation is considerably better if one considers the differences instead of quotients.

In two papers from 1848 and 1850, the Russian mathematician Pafnuty Chebyshev attempted to prove the asymptotic law of distribution of prime numbers. His work is notable for the use of the zeta function *ζ*(*s*), for real values of the argument "s", as in works of Leonhard Euler, as early as 1737. Chebyshev's papers predated Riemann's celebrated memoir of 1859, and he succeeded in proving a slightly weaker form of the asymptotic law, namely, that if the limit as x goes to infinity of *π*(*x*) / (*x* / log(*x*)) exists at all, then it is necessarily equal to one. He was able to prove unconditionally that this ratio is bounded above and below by 0.92129 and 1.10555, for all sufficiently large x. Although Chebyshev's paper did not prove the Prime Number Theorem, his estimates for *π*(*x*) were strong enough for him to prove Bertrand's postulate that there exists a prime number between *n* and 2*n* for any integer *n* ≥ 2.

An important paper concerning the distribution of prime numbers was Riemann's 1859 memoir "On the Number of Primes Less Than a Given Magnitude", the only paper he ever wrote on the subject. Riemann introduced new ideas into the subject, chiefly that the distribution of prime numbers is intimately connected with the zeros of the analytically extended Riemann zeta function of a complex variable. In particular, it is in this paper that the idea to apply methods of complex analysis to the study of the real function *π*(*x*) originates. Extending Riemann's ideas, two proofs of the asymptotic law of the distribution of prime numbers were found independently by Jacques Hadamard and Charles Jean de la Vallée Poussin and appeared in the same year (1896). Both proofs used methods from complex analysis, establishing as a main step of the proof that the Riemann zeta function *ζ*(*s*) is nonzero for all complex values of the variable s that have the form *s* = 1 + *it* with *t* > 0 .

During the 20th century, the theorem of Hadamard and de la Vallée Poussin also became known as the Prime Number Theorem. Several different proofs of it were found, including the "elementary" proofs of Atle Selberg (1949) and Paul Erdős (1949). Hadamard's and de la Vallée Poussin's original proofs are long and elaborate; later proofs introduced various simplifications through the use of Tauberian theorems but remained difficult to digest. A short proof was discovered in 1980 by the American mathematician Donald J. Newman. Newman's proof is arguably the simplest known proof of the theorem, although it is not "elementary" since it uses Cauchy's integral theorem from complex analysis.

## Proof sketch

Here is a sketch of the proof referred to in one of Terence Tao's lectures. Like most proofs of the PNT, it starts out by reformulating the problem in terms of a less intuitive, but better-behaved, prime-counting function. The idea is to count the primes (or a related set such as the set of prime powers) with *weights* to arrive at a function with smoother asymptotic behavior. The most common such generalized counting function is the Chebyshev function *ψ*(*x*), defined by

$\psi (x)=\sum _{k\geq 1}\sum _{\overset {p^{k}\leq x,}{\!\!\!\!p{\text{ is prime}}\!\!\!\!}}\log p\;.$

This is sometimes written as

$\psi (x)=\sum _{n\leq x}\Lambda (n)\;,$

where *Λ*(*n*) is the von Mangoldt function, namely

$\Lambda (n)={\begin{cases}\log p&{\text{ if }}n=p^{k}{\text{ for some prime }}p{\text{ and integer }}k\geq 1,\\0&{\text{otherwise.}}\end{cases}}$

It is now relatively easy to check that the PNT is equivalent to the claim that

$\lim _{x\to \infty }{\frac {\psi (x)}{x}}=1\;.$

Indeed, this follows from the easy estimates

$\psi (x)=\sum _{\overset {p\leq x}{\!\!\!\!p{\text{ is prime}}\!\!\!\!}}\log p\left\lfloor {\frac {\log x}{\log p}}\right\rfloor \leq \sum _{\overset {p\leq x}{\!\!\!\!p{\text{ is prime}}\!\!\!\!}}\log x=\pi (x)\log x$

and (using big O notation) for any *ε* > 0,

$\psi (x)\geq \sum _{\!\!\!\!{\overset {x^{1-\varepsilon }\leq p\leq x}{p{\text{ is prime}}}}\!\!\!\!}\log p\geq \sum _{\!\!\!\!{\overset {x^{1-\varepsilon }\leq p\leq x}{p{\text{ is prime}}}}\!\!\!\!}(1-\varepsilon )\log x=(1-\varepsilon )\left(\pi (x)+O\left(x^{1-\varepsilon }\right)\right)\log x\;.$

The next step is to find a useful representation for *ψ*(*x*). Let *ζ*(*s*) be the Riemann zeta function. It can be shown that *ζ*(*s*) is related to the von Mangoldt function *Λ*(*n*), and hence to *ψ*(*x*), via the relation

$-{\frac {\zeta '(s)}{\zeta (s)}}=\sum _{n=1}^{\infty }\Lambda (n)\,n^{-s}\;.$

A delicate analysis of this equation and related properties of the zeta function, using the Mellin transform and Perron's formula, shows that for non-integer x the equation

$\psi (x)=x\;-\;\log(2\pi )\;-\!\!\!\!\sum \limits _{\rho :\,\zeta (\rho )=0}{\frac {x^{\rho }}{\rho }}$

holds, where the sum is over all zeros (trivial and nontrivial) of the zeta function. This striking formula is one of the so-called explicit formulas of number theory, and is already suggestive of the result we wish to prove, since the term x (claimed to be the correct asymptotic order of *ψ*(*x*)) appears on the right-hand side, followed by (presumably) lower-order asymptotic terms.

The next step in the proof involves a study of the zeros of the zeta function. The trivial zeros −2, −4, −6, −8, ... can be handled separately:

$\sum _{n=1}^{\infty }{\frac {1}{2n\,x^{2n}}}=-{\frac {1}{2}}\log \left(1-{\frac {1}{x^{2}}}\right),$

which vanishes for large x. The nontrivial zeros, namely those on the critical strip 0 ≤ Re(*s*) ≤ 1, can potentially be of an asymptotic order comparable to the main term x if Re(*ρ*) = 1, so we need to show that all zeros have real part strictly less than 1.

### Non-vanishing on Re(*s*) = 1

To do this, we take for granted that *ζ*(*s*) is meromorphic in the half-plane Re(*s*) > 0, and is analytic there except for a simple pole at *s* = 1, and that there is a product formula

$\zeta (s)=\prod _{p}{\frac {1}{1-p^{-s}}}$

for Re(*s*) > 1. This product formula follows from the existence of unique prime factorization of integers, and shows that *ζ*(*s*) is never zero in this region, so that its logarithm is defined there and

$\log \zeta (s)=-\sum _{p}\log \left(1-p^{-s}\right)=\sum _{p,n}{\frac {p^{-ns}}{n}}\;.$

Write *s* = *x* + *iy* ; then

${\big |}\zeta (x+iy){\big |}=\exp \left(\sum _{n,p}{\frac {\cos ny\log p}{np^{nx}}}\right)\;.$

Now observe the identity

$3+4\cos \phi +\cos 2\phi =2(1+\cos \phi )^{2}\geq 0\;,$

so that

$\left|\zeta (x)^{3}\zeta (x+iy)^{4}\zeta (x+2iy)\right|=\exp \left(\sum _{n,p}{\frac {3+4\cos(ny\log p)+\cos(2ny\log p)}{np^{nx}}}\right)\geq 1$

for all *x* > 1. Suppose now that *ζ*(1 + *iy*) = 0. Certainly y is not zero, since *ζ*(*s*) has a simple pole at *s* = 1. Suppose that *x* > 1 and let x tend to 1 from above. Since $\zeta (s)$ has a simple pole at *s* = 1 and *ζ*(*x* + 2*iy*) stays analytic, the left hand side in the previous inequality tends to 0, a contradiction.

Finally, we can conclude that the PNT is heuristically true. To rigorously complete the proof there are still serious technicalities to overcome, due to the fact that the summation over zeta zeros in the explicit formula for *ψ*(*x*) does not converge absolutely but only conditionally and in a "principal value" sense. There are several ways around this problem but many of them require rather delicate complex-analytic estimates. Edwards's book provides the details. Another method is to use Ikehara's Tauberian theorem, though this theorem is itself quite hard to prove. D.J. Newman observed that the full strength of Ikehara's theorem is not needed for the prime number theorem, and one can get away with a special case that is much easier to prove.

## Newman's proof of the prime number theorem

D.J. Newman gives a quick proof of the prime number theorem (PNT). The proof is "non-elementary" by virtue of relying on complex analysis, but uses only elementary techniques from a first course in the subject: Cauchy's integral formula, Cauchy's integral theorem and estimates of complex integrals. Here is a brief sketch of this proof. See for the complete details.

The proof uses the same preliminaries as in the previous section except instead of the function ${\textstyle \ \psi \ ,}$ the Chebyshev function ${\textstyle \ \vartheta (x)=\sum _{p\leq x}\log p\ }$ is used, which is obtained by dropping some of the terms from the series for ${\textstyle \ \psi ~.}$ Similar to the argument in the previous proof based on Tao's lecture, we can show that *ϑ*(*x*) ≤ *π*(*x*) log *x* , and *ϑ*(*x*) ≥ ( 1 − *ɛ* )( *π*(*x*) + O( *x*1 − *ɛ* ) ) log *x* for any 0 < *ɛ* < 1 . Thus, the PNT is equivalent to $\ \lim _{x\to \infty }{\tfrac {\ \vartheta (x)\ }{x}}=1~.$ Likewise instead of $\ -{\tfrac {\ \zeta '(s)\ }{\zeta (s)}}\$ the function $\ \Phi (s)=\sum _{p\leq x}{\tfrac {\ \log p\ }{\;p^{s}\ }}\$ is used, which is obtained by dropping some terms in the series for $\ -{\tfrac {\ \zeta '(s)\ }{\zeta (s)}}~.$ The functions $\ \Phi (s)\$ and $\ -{\tfrac {\ \zeta '(s)\ }{\zeta (s)}}\$ differ by a function holomorphic on $\ \Re (s)=1~.$ Since, as was shown in the previous section, $\ \zeta (s)\$ has no zeroes on the line $\ \Re =1\ ,$ and $\ \Phi (s)-{\tfrac {1}{\ s-1\ }}\$ has no singularities on $\ \Re (s)=1~.$

One further piece of information needed in Newman's proof, and which is the key to the estimates in his simple method, is that $\ {\tfrac {\ \vartheta (x)\ }{x}}\$ is bounded. This is proved using an ingenious and easy method due to Chebyshev.

Integration by parts shows how $\ \vartheta (x)\$ and $\ \Phi (s)\$ are related: For $\ \Re (s)>1\ ,$

$\Phi (s)~=~\int _{1}^{\infty }{\frac {\operatorname {d} \vartheta (x)}{\;x^{s}\ }}~=~s\int _{1}^{\infty }{\frac {\vartheta (x)}{\ x^{s+1}\ }}\operatorname {d} x~=~s\int _{0}^{\infty }{\frac {\;\vartheta (e^{t})\ }{\;e^{st}\ }}\operatorname {d} t~.$

Newman's method proves the PNT by showing the integral

$I\equiv \int _{0}^{\infty }\left({\frac {\ \vartheta (e^{t})\ }{e^{t}}}-1\right)\operatorname {d} t~.$

converges, and therefore the integrand goes to zero as $\ t\to \infty \ ,$ which is the PNT. In general, the convergence of the improper integral does not imply that the integrand goes to zero at infinity, since it may oscillate, but since $\ \vartheta \$ is increasing, it is easy to show in this case.

To show the convergence of $\ I\ ,$ for $\ \Re (z)>0\$ let

$g_{T}(z)\equiv \int _{0}^{T}f(t)\ e^{-zt}\operatorname {d} t\quad$

and

$\quad g(z)\equiv \int _{0}^{\infty }f(t)\ e^{-zt}\operatorname {d} t\quad$

where

$\quad f(t)\equiv {\frac {\ \vartheta (e^{t})\ }{e^{t}}}-1\$

then

$\lim _{T\to \infty }g_{T}(z)~=~g(z)~=~{\frac {\ \Phi (s)\ }{s}}-{\frac {1}{\ s-1\ }}\qquad {\text{where}}\quad z\equiv s-1\$

which is equal to a function holomorphic on the line $\ \Re (z)=0~.$

The convergence of the integral $\ I\ ,$ and thus the PNT, is proved by showing that $\ \lim _{T\to \infty }g_{T}(0)~=~g(0)~.$ This involves change of order of limits since it can be written ${\textstyle \ \lim _{T\to \infty }\ \lim _{z\to 0}g_{T}(z)~=~\lim _{z\to 0}\ \lim _{T\to \infty }g_{T}(z)\ }$ and therefore classified as a Tauberian theorem.

The difference $\ g(0)-g_{T}(0)\$ is expressed using Cauchy's integral formula and then shown to be small for large $\ T\$ by estimating the integrand: Fix $\ R>0\$ and $\ \delta >0\$ so that $\ g(z)\$ is holomorphic in the region where $\ |z|\leq R~$ and $~\Re (z)\geq -\delta \ ,$ and let $\ C\$ be the boundary of that region. Since 0 is in the interior of the region, Cauchy's integral formula gives

$g(0)-g_{T}(0)~=~{\frac {1}{\ 2\pi i\ }}\int _{C}{\bigl (}\ g(z)-g_{T}(z)\ {\bigr )}\ {\frac {\ \operatorname {d} z\ }{z}}~=~{\frac {1}{2\pi i}}\int _{C}{\bigl (}\ g(z)-g_{T}(z)\ {\bigr )}\ F(z)\ {\frac {\ \operatorname {d} z\ }{z}}\$

where $\ F(z)\equiv e^{zT}\left(1+{\frac {\;z^{2}\ }{\;R^{2}\ }}\right)\$ is the factor introduced by Newman, which does not change the integral since $\ F\$ is entire and $\ F(0)=1~.$

To estimate the integral, break the contour $\ C\$ into two parts, $\ C=C_{+}+C_{-}\$ where $\ C_{+}\equiv C\cap \left\{z\ \vert \ \Re (z)>0\right\}\$ and $\ C_{-}\equiv C\cap \left\{z\ \vert \ \Re (z)\leq 0\right\}~.$ Then

$\ g(0)-g_{T}(0)~~=~~\int _{C_{+}}\int _{T}^{\infty }H(t,z)\operatorname {d} t\ \operatorname {d} z~~-~\int _{C_{-}}\int _{0}^{T}H(t,z)\operatorname {d} t\operatorname {d} z~~+~\int _{C_{-}}g(z)\ F(z){\frac {\operatorname {d} z}{\ 2\pi iz\ }}\ ,$

where $\ H(t,z)\equiv f(t)\ e^{-tz}{\frac {F(z)}{\ 2\pi i\ }}~.$ Note that $\ {\frac {\ \vartheta (x)\ }{x}}\ ,$ and hence $\ f(t)\ ,$ are bounded; so let $\ B\$ be some upper bound: $\ B\geq {\bigl |}f(t){\bigr |}~.$

This bound, combined with the estimate $\ \left|F\right|\ \leq \ 2\ \exp \!{\Bigl (}T\ \Re (z){\Bigr )}{\frac {\ \left|\Re (z)\right|\ }{R}}\$ for $\ |z|=R\ ,$ together give that the absolute value of the first integral must be $\ \leq {\frac {\ B\ }{R}}~.$ The integrand over $\ C_{-}\$ in the second integral is entire, so by Cauchy's integral theorem, the contour $\ C_{-}\$ can be modified to a semicircle of radius $\ R\$ in the left half-plane without changing the integral, and the same argument as for the first integral gives the absolute value of the second integral must be $\ \leq {\frac {\ B\ }{R}}~.$ Finally, letting $\ T\to \infty \ ,$ the third integral goes to zero since $\ e^{zT}\$ and hence $\ F\$ goes to zero on the contour. Combining the two estimates and the limit get

$\limsup _{T\to \infty }\ {\bigl |}\ g(0)-g_{T}(0)\ {\bigr |}\ \leq \ {\frac {\ 2B\ }{R}}\ ~.$

This holds for any $\ R\$ so $\ \lim _{T\to \infty }g_{T}(0)=g(0)\ ,$ and the PNT follows.

## Prime-counting function in terms of the logarithmic integral

In a handwritten note on a reprint of his 1838 paper "*Sur l'usage des séries infinies dans la théorie des nombres*", which he mailed to Gauss, Dirichlet conjectured (under a slightly different form appealing to a series rather than an integral) that an even better approximation to *π*(*x*) is given by the offset logarithmic integral function Li(*x*), defined by

$\operatorname {Li} (x)=\int _{2}^{x}{\frac {dt}{\log t}}=\operatorname {li} (x)-\operatorname {li} (2).$

Indeed, this integral is strongly suggestive of the notion that the "density" of primes around t should be 1 / log *t*. This function is related to the logarithm by the asymptotic expansion

$\operatorname {Li} (x)\sim {\frac {x}{\log x}}\sum _{k=0}^{\infty }{\frac {k!}{(\log x)^{k}}}={\frac {x}{\log x}}+{\frac {x}{(\log x)^{2}}}+{\frac {2x}{(\log x)^{3}}}+\cdots$

So, the prime number theorem can also be written as *π*(*x*) ~ Li(*x*). In fact, in another paper in 1899 de la Vallée Poussin proved that

$\pi (x)=\operatorname {Li} (x)+O\left(xe^{-a{\sqrt {\log x}}}\right)\quad {\text{as }}x\to \infty$

for some positive constant a, where *O*(...) is the big O notation. This has been improved to

$\pi (x)=\operatorname {li} (x)+O\left(x\exp \left(-{\frac {A(\log x)^{\frac {3}{5}}}{(\log \log x)^{\frac {1}{5}}}}\right)\right)$

where

$A=0.2098$

.

In 2016, Timothy Trudgian proved an explicit upper bound for the difference between $\pi (x)$ and $\operatorname {li} (x)$ :

${\big |}\pi (x)-\operatorname {li} (x){\big |}\leq 0.2795{\frac {x}{(\log x)^{3/4}}}\exp \left(-{\sqrt {\frac {\log x}{6.455}}}\right)$

for $x\geq 229$ .

The connection between the Riemann zeta function and *π*(*x*) is one reason the Riemann hypothesis has considerable importance in number theory: if established, it would yield a far better estimate of the error involved in the prime number theorem than is available today. More specifically, Helge von Koch showed in 1901 that if the Riemann hypothesis is true, the error term in the above relation can be improved to

$\pi (x)=\operatorname {Li} (x)+O\left({\sqrt {x}}\log x\right)$

(this last estimate is in fact equivalent to the Riemann hypothesis). The constant involved in the big O notation was estimated in 1976 by Lowell Schoenfeld, assuming the Riemann hypothesis:

${\big |}\pi (x)-\operatorname {li} (x){\big |}<{\frac {{\sqrt {x}}\log x}{8\pi }}$

for all *x* ≥ 2657. He also derived a similar bound for the Chebyshev prime-counting function ψ:

${\big |}\psi (x)-x{\big |}<{\frac {{\sqrt {x}}(\log x)^{2}}{8\pi }}$

for all *x* ≥ 73.2 . This latter bound has been shown to express a variance to mean power law (when regarded as a random function over the integers) and ⁠1/ f ⁠ noise and to also correspond to the Tweedie compound Poisson distribution. (The Tweedie distributions represent a family of scale invariant distributions that serve as foci of convergence for a generalization of the central limit theorem.) A lower bound is also derived by J. E. Littlewood, assuming the Riemann hypothesis:

${\big |}\pi (x)-\operatorname {li} (x){\big |}=\Omega \left({\sqrt {x}}{\frac {\log \log \log x}{\log x}}\right)$

The logarithmic integral li(*x*) is larger than *π*(*x*) for "small" values of x. This is because it is (in some sense) counting not primes, but prime powers, where a power pn of a prime p is counted as ⁠1/ n ⁠ of a prime. This suggests that li(*x*) should usually be larger than *π*(*x*) by roughly $\ {\tfrac {1}{2}}\operatorname {li} ({\sqrt {x}})\ ,$ and in particular should always be larger than *π*(*x*). However, in 1914, Littlewood proved that $\ \pi (x)-\operatorname {li} (x)\$ changes sign infinitely often. The first value of x where *π*(*x*) exceeds li(*x*) is probably around *x* ~ 10316 ; see the article on Skewes' number for more details. (On the other hand, the offset logarithmic integral Li(*x*) is smaller than *π*(*x*) already for *x* = 2; indeed, Li(2) = 0, while *π*(2) = 1.)

## Elementary proofs

In the first half of the twentieth century, some mathematicians (notably G. H. Hardy) believed that there exists a hierarchy of proof methods in mathematics depending on what sorts of numbers (integers, reals, complex) a proof requires, and that the prime number theorem (PNT) is a "deep" theorem by virtue of requiring complex analysis. This belief was somewhat shaken by a proof of the PNT based on Wiener's tauberian theorem, though Wiener's proof ultimately relies on properties of the Riemann zeta function on the line $Re(s)=1$ , where complex analysis must be used.

In March 1948, Atle Selberg established, by "elementary" means, the asymptotic formula

$\vartheta (x)\log(x)+\sum \limits _{p\leq x}{\log(p)}\ \vartheta \left({\frac {x}{p}}\right)=2x\log(x)+O(x)$

where

$\vartheta (x)=\sum \limits _{p\leq x}{\log(p)}$

for primes p. By July of that year, Selberg and Paul Erdős had each obtained elementary proofs of the PNT, both using Selberg's asymptotic formula as a starting point. These proofs effectively laid to rest the notion that the PNT was "deep" in that sense, and showed that technically "elementary" methods were more powerful than had been believed to be the case. On the history of the elementary proofs of the PNT, including the Erdős–Selberg priority dispute, see an article by Dorian Goldfeld.

There is some debate about the significance of Erdős and Selberg's result. There is no rigorous and widely accepted definition of the notion of elementary proof in number theory, so it is not clear exactly in what sense their proof is "elementary". Although it does not use complex analysis, it is in fact much more technical than the standard proof of PNT. One possible definition of an "elementary" proof is "one that can be carried out in first-order Peano arithmetic." There are number-theoretic statements (for example, the Paris–Harrington theorem) provable using second order but not first-order methods, but such theorems are rare to date. Erdős and Selberg's proof can certainly be formalized in Peano arithmetic, and in 1994, Charalambos Cornaros and Costas Dimitracopoulos proved that their proof can be formalized in a very weak fragment of PA, namely *I*Δ0 + exp. However, this does not address the question of whether or not the standard proof of PNT can be formalized in PA.

A more recent "elementary" proof of the prime number theorem uses ergodic theory, due to Florian Richter. The prime number theorem is obtained there in an equivalent form that the Cesàro sum of the values of the Liouville function is zero. The Liouville function is $(-1)^{\omega (n)}$ where $\omega (n)$ is the number of prime factors, with multiplicity, of the integer n . Bergelson and Richter (2022) then obtain this form of the prime number theorem from an ergodic theorem which they prove:

Let

X

be a compact

metric space

,

T

a continuous self-map of

X

, and

$\mu$

a

T

-invariant Borel

probability measure

for which

T

is

uniquely ergodic

. Then, for every

$f\in C(X)$

,

${\tfrac {1}{N}}\sum _{n=1}^{N}f(T^{\omega (n)}x)\to \int _{X}f\,d\mu ,\quad \forall x\in X.$

This ergodic theorem can also be used to give "soft" proofs of results related to the prime number theorem, such as the Pillai–Selberg theorem and Erdős–Delange theorem.

## Computer verifications

In 2005, Avigad *et al.* employed the Isabelle theorem prover to devise a computer-verified variant of the Erdős–Selberg proof of the PNT. This was the first machine-verified proof of the PNT. Avigad chose to formalize the Erdős–Selberg proof rather than an analytic one because while Isabelle's library at the time could implement the notions of limit, derivative, and transcendental function, it had almost no theory of integration to speak of.

In 2009, John Harrison employed HOL Light to formalize a proof employing complex analysis. By developing the necessary analytic machinery, including the Cauchy integral formula, Harrison was able to formalize "a direct, modern and elegant proof instead of the more involved 'elementary' Erdős–Selberg argument".

## Prime number theorem for arithmetic progressions

Let *π**d*,*a*(*x*) denote the number of primes in the arithmetic progression *a*, *a* + *d*, *a* + 2*d*, *a* + 3*d*, ... that are less than x. Dirichlet and Legendre conjectured, and de la Vallée Poussin proved, that if a and d are coprime, then

$\pi _{d,a}(x)\sim {\frac {\operatorname {Li} (x)}{\varphi (d)}}\ ,$

where φ is Euler's totient function. In other words, the primes are distributed evenly among the residue classes [*a*] modulo d with gcd(*a*, *d*) = 1 . This is stronger than Dirichlet's theorem on arithmetic progressions (which only states that there is an infinity of primes in each class) and can be proved using similar methods used by Newman for his proof of the prime number theorem.

The Siegel–Walfisz theorem gives a good estimate for the distribution of primes in residue classes.

Bennett *et al.* proved the following estimate that has explicit constants A and B (Theorem 1.3): Let d $\geq 3$ be an integer and let a be an integer that is coprime to d. Then there are positive constants A and B such that

$\left|\pi _{d,a}(x)-{\frac {\ \operatorname {Li} (x)\ }{\ \varphi (d)\ }}\right|<{\frac {A\ x}{\ (\log x)^{2}\ }}\quad {\text{ for all }}\quad x\geq B\ ,$

where

$A={\frac {1}{\ 840\ }}\quad {\text{ if }}\quad 3\leq d\leq 10^{4}\quad {\text{ and }}\quad A={\frac {1}{\ 160\ }}\quad {\text{ if }}\quad d>10^{4}~,$

and

$B=8\cdot 10^{9}\quad {\text{ if }}\quad 3\leq d\leq 10^{5}\quad {\text{ and }}\quad B=\exp(\ 0.03\ {\sqrt {d\ }}\ (\log {d})^{3}\ )\quad {\text{ if }}\quad d>10^{5}\ .$

### Prime number race

Although we have in particular

$\pi _{4,1}(x)\sim \pi _{4,3}(x)\ ,$

empirically the primes congruent to 3 are more numerous and are nearly always ahead in this "prime number race"; the first reversal occurs at *x* = 26861. However Littlewood showed in 1914 that there are infinitely many sign changes for the function

$\pi _{4,1}(x)-\pi _{4,3}(x)~,$

so the lead in the race switches back and forth infinitely many times. The phenomenon that *π*4,3(*x*) is ahead most of the time is called Chebyshev's bias. The prime number race generalizes to other moduli and is the subject of much research; Pál Turán asked whether it is always the case that *π**c*,*a*(*x*) and *π**c*,*b*(*x*) change places when a and b are coprime to c. Granville and Martin give a thorough exposition and survey.

Another example is the distribution of the last digit of prime numbers. Except for 2 and 5, all prime numbers end in 1, 3, 7, or 9. Dirichlet's theorem states that asymptotically, 25% of all primes end in each of these four digits. However, empirical evidence shows that, for a given limit, there tend to be slightly more primes that end in 3 or 7 than end in 1 or 9 (a generation of the Chebyshev's bias). This follows that 1 and 9 are quadratic residues modulo 10, and 3 and 7 are quadratic nonresidues modulo 10.

## Non-asymptotic bounds on the prime-counting function

The prime number theorem is an *asymptotic* result. It gives an ineffective bound on *π*(*x*) as a direct consequence of the definition of the limit: for all *ε* > 0, there is an S such that for all *x* > *S*,

$(1-\varepsilon ){\frac {x}{\log x}}\;<\;\pi (x)\;<\;(1+\varepsilon ){\frac {x}{\log x}}\;.$

However, better bounds on *π*(*x*) are known, for instance Pierre Dusart's

${\frac {x}{\log x}}\left(1+{\frac {1}{\log x}}\right)\;<\;\pi (x)\;<\;{\frac {x}{\log x}}\left(1+{\frac {1}{\log x}}+{\frac {2.51}{(\log x)^{2}}}\right)\;.$

The first inequality holds for all *x* ≥ 599 and the second one for *x* ≥ 355991.

The proof by de la Vallée Poussin implies the following bound: For every *ε* > 0, there is an S such that for all *x* > *S*,

${\frac {x}{\log x-(1-\varepsilon )}}\;<\;\pi (x)\;<\;{\frac {x}{\log x-(1+\varepsilon )}}\;.$

The value *ε* = 3 gives a weak but sometimes useful bound for *x* ≥ 55:

${\frac {x}{\log x+2}}\;<\;\pi (x)\;<\;{\frac {x}{\log x-4}}\;.$

In Pierre Dusart's thesis there are stronger versions of this type of inequality that are valid for larger x. Later in 2010, Dusart proved:

${\begin{aligned}{\frac {x}{\log x-1}}\;&<\;\pi (x)&&{\text{ for }}x\geq 5393\;,{\text{ and }}\\\pi (x)&<\;{\frac {x}{\log x-1.1}}&&{\text{ for }}x\geq 60184\;.\end{aligned}}$

Note that the first of these obsoletes the *ε* > 0 condition on the lower bound.

## Approximations for the *n*th prime number

As a consequence of the prime number theorem, one gets an asymptotic expression for the nth prime number, denoted by *p**n*:

$p_{n}\sim n\log n.$

A better approximation is by Cesàro (1894):

$p_{n}=nB_{2}(\log n),{\text{ where}}$

$B_{2}(x)=x+\log x-1+{\frac {\log x-2}{x}}-{\frac {(\log x)^{2}-6\log x+11}{2x^{2}}}+o\left({\frac {1}{x^{2}}}\right).$

Again considering the 2×1017th prime number 8512677386048191063, assuming the trailing error term is zero gives an estimate of 8512681315554715386; the first 5 digits match and relative error is about 0.46 parts per million.

Cipolla (1902) showed that these are the leading terms of an infinite series which may be truncated at arbitrary degree, with

$B_{k}(x)=x+\log x-1-\sum _{i=1}^{k}(-1)^{i}{\frac {P_{i}(\log x)}{ix^{i}}}+O\left({\frac {(\log x)^{k+1}}{x^{k+1}}}\right),$

where each *Pi* is a degree-i monic polynomial. (*P*1(*y*) = *y* − 2, *P*2(*y*) = *y*2 − 6*y* + 11, *P*3(*y*) = *y*3 − ⁠21/2⁠*y*2 + 42*y* + ⁠131/2⁠, and so on.)

Rosser's theorem states that

$p_{n}>n\log n.$

Dusart (1999). found tighter bounds using the form of the Cesàro/Cipolla approximations but varying the lowest-order constant term. *Bk*(*x*; *C*) is the same function as above, but with the lowest-order constant term replaced by a parameter C:

${\begin{aligned}p_{n}\;&>\;nB_{0}(\log n;1)&&{\text{for }}n\geq 2,{\text{ and}}\\p_{n}\;&<\;nB_{0}(\log n;0.9484)&&{\text{for }}n\geq 39017,{\text{ where}}\\B_{0}(x;C)\;&=\;x+\log x-C.\\p_{n}\;&>\;nB_{1}(\log n;2.25)&&{\text{for }}n\geq 2,{\text{ and}}\\p_{n}\;&<\;nB_{1}(\log n;1.8)&&{\text{for }}n\geq 27076,{\text{ where}}\\B_{1}(x;C)\;&=\;x+\log x-1+{\frac {\log x-C}{x}}.\end{aligned}}$

The upper bounds can be extended to smaller n by loosening the parameter. For example, *pn* < *n B*1(log *n*; 0.5) for all *n* ≥ 20.

Axler (2019) extended this to higher order, showing:

${\begin{aligned}p_{n}\;&>\;nB_{2}(\log n;11.321)\quad {\text{for }}n\geq 2,{\text{ and }}\\p_{n}\;&<\;nB_{2}(\log n;10.667)\quad {\text{for }}n\geq 46\,254\,381,{\text{ where}}\\B_{2}(x;C)\;&=\;x+\log x-1+{\frac {\log x-2}{x}}-{\frac {(\log x)^{2}-6\log x+C}{2x^{2}}}.\end{aligned}}$

Again, the bound on n may be decreased by loosening the parameter. For example, *pn* < *n B*2(log *n*; 0) for n ≥ 3468.

## Table of *π*(*x*), *x* / log *x*, and li(*x*)

The table compares exact values of *π*(*x*) to the two approximations *x* / log *x* and li(*x*). The approximation difference columns are rounded to the nearest integer, but the "% error" columns are computed based on the unrounded approximations. The last column, *x* / *π*(*x*), is the average prime gap below x.

| x | *π*(*x*) | *π*(*x*) − ⁠*x*/log(*x*)⁠ | li(*x*) − *π*(*x*) | % error | ⁠*x*/*π*(*x*)⁠ |   |
|---|---|---|---|---|---|---|
| ⁠*x*/log(*x*)⁠ | li(*x*) |   |   |   |   |   |
| 10 | 4 | 0 | 2 | 8.22% | 42.606% | 2.500 |
| 102 | 25 | 3 | 5 | 14.06% | 18.597% | 4.000 |
| 103 | 168 | 23 | 10 | 14.85% | 5.561% | 5.952 |
| 104 | 1,229 | 143 | 17 | 12.37% | 1.384% | 8.137 |
| 105 | 9,592 | 906 | 38 | 9.91% | 0.393% | 10.425 |
| 106 | 78,498 | 6,116 | 130 | 8.11% | 0.164% | 12.739 |
| 107 | 664,579 | 44,158 | 339 | 6.87% | 0.051% | 15.047 |
| 108 | 5,761,455 | 332,774 | 754 | 5.94% | 0.013% | 17.357 |
| 109 | 50,847,534 | 2,592,592 | 1,701 | 5.23% | 3.34×10−3 % | 19.667 |
| 1010 | 455,052,511 | 20,758,029 | 3,104 | 4.66% | 6.82×10−4 % | 21.975 |
| 1011 | 4,118,054,813 | 169,923,159 | 11,588 | 4.21% | 2.81×10−4 % | 24.283 |
| 1012 | 37,607,912,018 | 1,416,705,193 | 38,263 | 3.83% | 1.02×10−4 % | 26.590 |
| 1013 | 346,065,536,839 | 11,992,858,452 | 108,971 | 3.52% | 3.14×10−5 % | 28.896 |
| 1014 | 3,204,941,750,802 | 102,838,308,636 | 314,890 | 3.26% | 9.82×10−6 % | 31.202 |
| 1015 | 29,844,570,422,669 | 891,604,962,452 | 1,052,619 | 3.03% | 3.52×10−6 % | 33.507 |
| 1016 | 279,238,341,033,925 | 7,804,289,844,393 | 3,214,632 | 2.83% | 1.15×10−6 % | 35.812 |
| 1017 | 2,623,557,157,654,233 | 68,883,734,693,928 | 7,956,589 | 2.66% | 3.03×10−7 % | 38.116 |
| 1018 | 24,739,954,287,740,860 | 612,483,070,893,536 | 21,949,555 | 2.51% | 8.87×10−8 % | 40.420 |
| 1019 | 234,057,667,276,344,607 | 5,481,624,169,369,961 | 99,877,775 | 2.36% | 4.26×10−8 % | 42.725 |
| 1020 | 2,220,819,602,560,918,840 | 49,347,193,044,659,702 | 222,744,644 | 2.24% | 1.01×10−8 % | 45.028 |
| 1021 | 21,127,269,486,018,731,928 | 446,579,871,578,168,707 | 597,394,254 | 2.13% | 2.82×10−9 % | 47.332 |
| 1022 | 201,467,286,689,315,906,290 | 4,060,704,006,019,620,994 | 1,932,355,208 | 2.03% | 9.59×10−10 % | 49.636 |
| 1023 | 1,925,320,391,606,803,968,923 | 37,083,513,766,578,631,309 | 7,250,186,216 | 1.94% | 3.76×10−10 % | 51.939 |
| 1024 | 18,435,599,767,349,200,867,866 | 339,996,354,713,708,049,069 | 17,146,907,278 | 1.86% | 9.31×10−11 % | 54.243 |
| 1025 | 176,846,309,399,143,769,411,680 | 3,128,516,637,843,038,351,228 | 55,160,980,939 | 1.78% | 3.21×10−11 % | 56.546 |
| 1026 | 1,699,246,750,872,437,141,327,603 | 28,883,358,936,853,188,823,261 | 155,891,678,121 | 1.71% | 9.17×10−12 % | 58.850 |
| 1027 | 16,352,460,426,841,680,446,427,399 | 267,479,615,610,131,274,163,365 | 508,666,658,006 | 1.64% | 3.11×10−12 % | 61.153 |
| 1028 | 157,589,269,275,973,410,412,739,598 | 2,484,097,167,669,186,251,622,127 | 1,427,745,660,374 | 1.58% | 9.05×10−13 % | 63.456 |
| 1029 | 1,520,698,109,714,272,166,094,258,063 | 23,130,930,737,541,725,917,951,446 | 4,551,193,622,464 | 1.53% | 2.99×10−13 % | 65.759 |

The value for *π*(1024) was originally computed assuming the Riemann hypothesis; it has since been verified unconditionally.

## Analogue for irreducible polynomials over a finite field

There is an analogue of the prime number theorem that describes the "distribution" of irreducible polynomials over a finite field; the form it takes is strikingly similar to the case of the classical prime number theorem.

To state it precisely, let *F* = GF(*q*) be the finite field with q elements, for some fixed q, and let Nn be the number of monic *irreducible* polynomials over F whose degree is equal to n. That is, we are looking at polynomials with coefficients chosen from F, which cannot be written as products of polynomials of smaller degree. In this setting, these polynomials play the role of the prime numbers, since all other monic polynomials are built up of products of them. One can then prove that

$N_{n}\sim {\frac {q^{n}}{n}}.$

If we make the substitution *x* = *q**n*, then the right hand side is just

${\frac {x}{\log _{q}x}},$

which makes the analogy clearer. Since there are precisely *q**n* monic polynomials of degree n (including the reducible ones), this can be rephrased as follows: if a monic polynomial of degree n is selected randomly, then the probability of it being irreducible is about ⁠1/*n*⁠.

One can even prove an analogue of the Riemann hypothesis, namely that

$N_{n}={\frac {q^{n}}{n}}+O\left({\frac {q^{\frac {n}{2}}}{n}}\right).$

The proofs of these statements are far simpler than in the classical case. It involves a short, combinatorial argument, summarised as follows: every element of the degree n extension of F is a root of some irreducible polynomial whose degree d divides n; by counting these roots in two different ways one establishes that

$q^{n}=\sum _{d\mid n}dN_{d},$

where the sum is over all divisors d of n. Möbius inversion then yields

$N_{n}={\frac {1}{n}}\sum _{d\mid n}\mu \left({\frac {n}{d}}\right)q^{d},$

where *μ*(*k*) is the Möbius function. (This formula was known to Gauss.) The main term occurs for *d* = *n*, and it is not difficult to bound the remaining terms. The "Riemann hypothesis" statement depends on the fact that the largest proper divisor of n can be no larger than ⁠*n*/2⁠.
