---
title: "Riemann hypothesis (part 1/2)"
source: https://en.wikipedia.org/wiki/Riemann_hypothesis
domain: analytic-number-theory
license: CC-BY-SA-4.0
tags: analytic number theory, prime number theorem, dirichlet series, riemann hypothesis
fetched: 2026-07-02
part: 1/2
---

# Riemann hypothesis

Unsolved problem in mathematics

Do all non-trivial zeros of the Riemann zeta function have a real part equal to one half?

More unsolved problems in mathematics

In mathematics, the **Riemann hypothesis** is the conjecture that the Riemann zeta function has its zeros only at the negative even integers and complex numbers with real part ⁠1/2⁠. Many consider it to be the most important unsolved problem in pure mathematics. It is of great interest in number theory because it implies results about the distribution of prime numbers. It was proposed by Bernhard Riemann, after whom it is named. According to a 2026 survey, there is overwhelming numerical evidence for the hypothesis, but no proof is known.

The Riemann hypothesis and some of its generalizations, along with Goldbach's conjecture and the twin prime conjecture, make up Hilbert's eighth problem in David Hilbert's list of twenty-three unsolved problems; it is also one of the Millennium Prize Problems of the Clay Mathematics Institute, which offers US$1 million for a solution to any of them. The name is also used for some closely related analogues, some of which have been proved, such as the Riemann hypothesis for curves over finite fields, which was proved by André Weil.

The Riemann zeta function $\zeta$ is a function whose argument may be any complex number other than 1, and whose values are also complex. It has zeros at the negative even integers; that is, $\zeta (s)=0$ when s is one of $-2,-4,-6,\dots$ These are called its *trivial zeros*. The zeta function is also zero for other values of s , which are called *nontrivial zeros*. The Riemann hypothesis is concerned with the locations of these nontrivial zeros, and states that:

> The real part of every nontrivial zero of the Riemann zeta function is ${\frac {1}{2}}$ .

Thus, the hypothesis states that all the nontrivial zeros lie on the *critical line*, consisting of the complex numbers ${\tfrac {1}{2}}+it$ where t is a real number and i is the imaginary unit.


## Riemann zeta function

The Riemann zeta function is defined for complex s with real part greater than 1 by the absolutely convergent infinite series

$\zeta (s)=\sum _{n=1}^{\infty }{\frac {1}{n^{s}}}={\frac {1}{1^{s}}}+{\frac {1}{2^{s}}}+{\frac {1}{3^{s}}}+\cdots$

Leonhard Euler considered this series in the 1730s for real values of s , in conjunction with his solution to the Basel problem. He also proved that it equals the Euler product

$\zeta (s)=\prod _{p{\text{ prime}}}{\frac {1}{1-p^{-s}}}={\frac {1}{1-2^{-s}}}\cdot {\frac {1}{1-3^{-s}}}\cdot {\frac {1}{1-5^{-s}}}\cdot {\frac {1}{1-7^{-s}}}\cdots$

where the infinite product extends over all prime numbers p .

The Riemann hypothesis discusses zeros outside the region of convergence of this series and Euler product. To make sense of the hypothesis, it is necessary to analytically continue the function to obtain a form that is valid for all complex s . Because the zeta function is meromorphic, all choices of how to perform this analytic continuation will lead to the same result, by the identity theorem. A first step in this continuation observes that the series for the zeta function and the Dirichlet eta function satisfy the relation

$\left(1-{\frac {2}{2^{s}}}\right)\zeta (s)=\eta (s)=\sum _{n=1}^{\infty }{\frac {(-1)^{n+1}}{n^{s}}}={\frac {1}{1^{s}}}-{\frac {1}{2^{s}}}+{\frac {1}{3^{s}}}-\cdots ,$

within the region of convergence for both series. But the eta function series on the right converges not just when the real part of s is greater than one, but more generally whenever s has positive real part. Thus, the zeta function can be redefined as $\eta (s)/(1-2/2^{s})$ , extending it from $\operatorname {Re} (s)>1$ to the larger domain $\operatorname {Re} (s)>0$ , except for the points where $1-2/2^{s}$ is zero. These are the points $s=1+2\pi in/\log 2$ , where n can be any nonzero integer; the zeta function can be extended to these values too by taking limits (see the article on the Dirichlet eta function), giving a finite value for all values of s with positive real part except the simple pole at $s=1$ .

In the strip $0<\operatorname {Re} (s)<1$ this extension of the zeta function satisfies the functional equation

$\zeta (s)=2^{s}\pi ^{s-1}\ \sin \left({\frac {\pi s}{2}}\right)\ \Gamma (1-s)\ \zeta (1-s).$

One may then define $\zeta (s)$ for all remaining nonzero complex numbers s ( $\operatorname {Re} (s)\leq 0$ and $s\neq 0$ ) by applying this equation outside the strip, and letting $\zeta (s)$ equal the right side of the equation whenever s has non-positive real part (and $s\neq 0$ ).

If s is a negative even integer, then $\zeta (s)=0$ , because the factor $\sin(\pi s/2)$ vanishes; these are the zeta function's *trivial zeros*. (If s is a positive even integer this argument does not apply because the zeros of the sine function are canceled by the poles of the gamma function as it takes negative integer arguments.)

The value *ζ*(0) = −1/2 is not determined by the functional equation, but is the limiting value of $\zeta (s)$ as s approaches zero. The functional equation also implies that the zeta function has no zeros with negative real part other than the trivial zeros, so all nontrivial zeros lie in the *critical strip* where s has real part between 0 and 1.

- (Riemann zeta function along the critical line with Re(s) = 1/2. Real values are shown on the horizontal axis and imaginary values are on the vertical axis. Re(ζ(1/2 + it)), Im(ζ(1/2 + it)) is plotted with t ranging between −30 and 30.[5]) Riemann zeta function along the critical line with Re(*s*) = 1/2. Real values are shown on the horizontal axis and imaginary values are on the vertical axis. Re(*ζ*(1/2 + *it*)), Im(*ζ*(1/2 + *it*)) is plotted with *t* ranging between −30 and 30.
- 3D animation showing critical strip (blue, where s has real part between 0 and 1), critical line (red, for real part of s equals 0.5) and zeroes (cross between red and orange): [*x*,*y*,*z*] = [Re(*ζ*(*r* + *it*)), Im(*ζ*(*r* + *it*)), *t*] with $0.1\leq r\leq 0.9$ and $1\leq t\leq 51$ .
- (The real part (red) and imaginary part (blue) of the Riemann zeta function '"`UNIQ--postMath-00000033-QINU`"' along the critical line in the complex plane with real part '"`UNIQ--postMath-00000034-QINU`"'. The first nontrivial zeros, where '"`UNIQ--postMath-00000035-QINU`"' equals zero, occur where both curves touch the horizontal '"`UNIQ--postMath-00000036-QINU`"'-axis, for complex numbers with imaginary parts equaling '"`UNIQ--postMath-00000037-QINU`"', '"`UNIQ--postMath-00000038-QINU`"' and '"`UNIQ--postMath-00000039-QINU`"'.) The real part (red) and imaginary part (blue) of the Riemann zeta function $\zeta (s)$ along the critical line in the complex plane with real part $\operatorname {Re} (s)=1/2$ . The first nontrivial zeros, where $\zeta (s)$ equals zero, occur where both curves touch the horizontal x -axis, for complex numbers with imaginary parts equaling $\pm 14.135$ , $\pm 21.022$ and $\pm 25.011$ .


## Origin

> *... es ist sehr wahrscheinlich, dass alle Wurzeln reell sind. Hiervon wäre allerdings ein strenger Beweis zu wünschen; ich habe indess die Aufsuchung desselben nach einigen flüchtigen vergeblichen Versuchen vorläufig bei Seite gelassen, da er für den nächsten Zweck meiner Untersuchung entbehrlich schien.* ... it is very probable that all roots are real. Of course one would wish for a rigorous proof here; I have for the time being, after some fleeting vain attempts, provisionally put aside the search for this, as it appears dispensable for the immediate objective of my investigation.

— Riemann's statement of the Riemann hypothesis, from (Riemann 1859). (He was discussing a variant of the zeta function, modified in a way that the real line be mapped to the critical line.)

> At the death of Riemann, a note was found among his papers, saying "These properties of *ζ*(*s*) (the function in question) are deduced from an expression of it which, however, I did not succeed in simplifying enough to publish it." We still have not the slightest idea of what the expression could be. As to the properties he simply enunciated, some thirty years elapsed before I was able to prove all of them but one [the Riemann Hypothesis itself].

— Jacques Hadamard, The Mathematician's Mind, VIII. Paradoxical Cases of Intuition

Riemann's original motivation for studying the zeta function and its zeros was their occurrence in his explicit formula for the number of primes $\pi (x)$ less than or equal to a given number x , which he published in his 1859 paper "On the Number of Primes Less Than a Given Magnitude". His formula was given in terms of the related function

$\Pi (x)=\pi (x)+{\frac {\pi (x^{1/2})}{2}}+{\frac {\pi (x^{1/3})}{3}}+{\frac {\pi (x^{1/4})}{4}}+{\frac {\pi (x^{1/5})}{5}}+{\frac {\pi (x^{1/6})}{6}}+\cdots$

which counts the primes and prime powers up to x , counting a prime power $p^{n}$ as $1/n$ . The number of primes can be recovered from this function by using the Möbius inversion formula:

${\begin{aligned}\pi (x)&=\sum _{n=1}^{\infty }{\frac {\mu (n)}{n}}\Pi (x^{1/n})\\&=\Pi (x)-{\frac {1}{2}}\Pi (x^{1/2})-{\frac {1}{3}}\Pi (x^{1/3})-{\frac {1}{5}}\Pi (x^{1/5})+{\frac {1}{6}}\Pi (x^{1/6})-\cdots ,\end{aligned}}$

where $\mu$ is the Möbius function. Riemann's formula is then

$\Pi _{0}(x)=\operatorname {li} (x)-\sum _{\rho }\operatorname {li} (x^{\rho })-\log 2+\int _{x}^{\infty }{\frac {dt}{t(t^{2}-1)\log t}}$

,

where the sum is over the nontrivial zeros of the zeta function and where $\Pi _{0}$ is a slightly modified version of $\Pi$ that replaces its value at its points of discontinuity by the average of its upper and lower limits:

$\Pi _{0}(x)=\lim _{\varepsilon \to 0}{\frac {\Pi (x-\varepsilon )+\Pi (x+\varepsilon )}{2}}.$

The summation in Riemann's formula is not absolutely convergent, but may be evaluated by taking the zeros $\rho$ in order of the absolute value of their imaginary part. The function $\operatorname {li}$ occurring in the first term is the (unoffset) logarithmic integral function given by the Cauchy principal value of the divergent integral

$\operatorname {li} (x)=\int _{0}^{x}{\frac {dt}{\log t}}.$

The terms $\operatorname {li} (x^{\rho })$ involving the zeros of the zeta function need some care in their definition as $\operatorname {li}$ has branch points at 0 and 1, and are defined (for $x>1$ ) by analytic continuation in the complex variable $\rho$ in the region $\operatorname {Re} (\rho )>0$ ; i.e., they should be considered as Ei(*ρ* log *x*). The other terms also correspond to zeros: the dominant term $\operatorname {li} (x)$ comes from the pole at $s=1$ , considered as a zero of multiplicity $-1$ , and the remaining small terms come from the trivial zeros. For some graphs of the sums of the first few terms of this series see Riesel & Göhl (1970) or Zagier (1977).

This formula says that the zeros of the Riemann zeta function control the oscillations of primes around their "expected" positions. Riemann knew that the non-trivial zeros of the zeta function were symmetrically distributed about the line $s=1/2+it$ , and he knew that all of its non-trivial zeros must lie in the range $0\leq \operatorname {Re} (s)\leq 1$ . He checked that a few of the zeros lay on the critical line with real part $1/2$ and suggested that they all do; this is the Riemann hypothesis.

> The result has caught the imagination of most mathematicians because it is so unexpected, connecting two seemingly unrelated areas in mathematics; namely, number theory, which is the study of the discrete, and complex analysis, which deals with continuous processes.

— (Burton 2006, p. 376)


## Consequences

The practical uses of the Riemann hypothesis include many propositions known to be true under the Riemann hypothesis, and some that can be shown to be equivalent to the Riemann hypothesis.

### Distribution of prime numbers

Riemann's explicit formula for the number of primes less than a given number states that, in terms of a sum over the zeros of the Riemann zeta function, the magnitude of the oscillations of primes around their expected position is controlled by the real parts of the zeros of the zeta function. In particular, the error term in the prime number theorem is closely related to the position of the zeros. For example, if $\beta$ is the upper bound of the real parts of the zeros, then $\pi (x)-\operatorname {li} (x)=O\!\left(x^{\beta }\log x\right)$ , where $\pi (x)$ is the prime-counting function and $\operatorname {li} (x)$ is the logarithmic integral function. It is already known that $1/2\leq \beta \leq 1$ .

Helge von Koch proved that the Riemann hypothesis implies the "best possible" bound for the error of the prime number theorem. A precise version of von Koch's result, due to Schoenfeld (1976), says that the Riemann hypothesis implies

$|\pi (x)-\operatorname {li} (x)|<{\frac {1}{8\pi }}{\sqrt {x}}\log(x)$

for all $x\geq 2657$ . Schoenfeld (1976) also showed that the Riemann hypothesis implies

$|\psi (x)-x|<{\frac {1}{8\pi }}{\sqrt {x}}\log ^{2}x$

for all $x\geq 73.2$ , where $\psi (x)$ is Chebyshev's second function.

Adrian Dudek proved that the Riemann hypothesis implies that for $x\geq 2$ , there is a prime p satisfying

$x-{\frac {4}{\pi }}{\sqrt {x}}\log x<p\leq x$

.

The constant $4/\pi$ may be reduced to $1+\varepsilon$ provided that x is taken to be sufficiently large. This is an explicit version of a theorem of Cramér.

### Growth of arithmetic functions

The Riemann hypothesis implies strong bounds on the growth of many other arithmetic functions, in addition to the primes counting function above.

One example involves the Möbius function *μ*. The statement that the equation

${\frac {1}{\zeta (s)}}=\sum _{n=1}^{\infty }{\frac {\mu (n)}{n^{s}}}$

is valid for every *s* with real part greater than 1/2, with the sum on the right hand side converging, is equivalent to the Riemann hypothesis. From this we can also conclude that if the Mertens function is defined by

$M(x)=\sum _{n\leq x}\mu (n)$

then the claim that

$M(x)=O\left(x^{{\frac {1}{2}}+\varepsilon }\right)$

for every positive *ε* is equivalent to the Riemann hypothesis (J. E. Littlewood, 1912; see for instance: paragraph 14.25 in Titchmarsh (1986)). The determinant of the order *n* Redheffer matrix is equal to *M*(*n*), so the Riemann hypothesis can also be stated as a condition on the growth of these determinants. Littlewood's result has been improved several times since then, by Edmund Landau, Edward Charles Titchmarsh, Helmut Maier and Hugh Montgomery, and Kannan Soundararajan. Soundararajan's result is that, conditional on the Riemann hypothesis,

$M(x)=O\left(x^{1/2}\exp \left((\log x)^{1/2}(\log \log x)^{14}\right)\right).$

The Riemann hypothesis puts a rather tight bound on the growth of *M*, since Odlyzko & te Riele (1985) disproved the slightly stronger Mertens conjecture

$|M(x)|\leq {\sqrt {x}}.$

Another closely related result is due to Björner (2011), that the Riemann hypothesis is equivalent to the statement that the Euler characteristic of the simplicial complex determined by the lattice of integers under divisibility is $o(n^{1/2+\epsilon })$ for all $\epsilon >0$ (see incidence algebra).

The Riemann hypothesis is equivalent to many other conjectures about the rate of growth of other arithmetic functions aside from *μ*(*n*). A typical example is Robin's theorem, which states that if *σ*(*n*) is the sigma function, given by

$\sigma (n)=\sum _{d\mid n}d$

then

$\sigma (n)<e^{\gamma }n\log \log n$

for all *n* > 5040 if and only if the Riemann hypothesis is true, where *γ* is the Euler–Mascheroni constant.

A related bound was given by Jeffrey Lagarias in 2002, who proved that the Riemann hypothesis is equivalent to the statement that:

$\sigma (n)<H_{n}+\log(H_{n})e^{H_{n}}$

for every natural number *n* > 1, where $H_{n}$ is the *n*th harmonic number.

The Riemann hypothesis is also true if and only if the inequality

${\frac {n}{\varphi (n)}}<e^{\gamma }\log \log n+{\frac {e^{\gamma }(4+\gamma -\log 4\pi )}{\sqrt {\log n}}}$

is true for all *n* ≥ 120569#, where *φ*(*n*) is Euler's totient function and 120569# is the product of the first 120569 primes.

Another example was found by Jérôme Franel, and extended by Landau (see Franel & Landau (1924)). The Riemann hypothesis is equivalent to several statements showing that the terms of the Farey sequence are fairly regular. One such equivalence is as follows: if *F**n* is the Farey sequence of order *n*, beginning with 1/*n* and up to 1/1, then the claim that for all *ε* > 0

$\sum _{i=1}^{m}|F_{n}(i)-{\tfrac {i}{m}}|=O\left(n^{{\frac {1}{2}}+\epsilon }\right)$

is equivalent to the Riemann hypothesis. Here

$m=\sum _{i=1}^{n}\varphi (i)$

is the number of terms in the Farey sequence of order *n*.

For an example from group theory, if *g*(*n*) is Landau's function given by the maximal order of elements of the symmetric group S*n* of degree *n*, then Massias, Nicolas & Robin (1988) showed that the Riemann hypothesis is equivalent to the bound

$\log g(n)<{\sqrt {\operatorname {Li} ^{-1}(n)}}$

for all sufficiently large *n*.

### Lindelöf hypothesis and growth of the zeta function

The Riemann hypothesis has various weaker consequences as well; one is the Lindelöf hypothesis on the rate of growth of the zeta function on the critical line, which says that, for any *ε* > 0,

$\zeta \left({\frac {1}{2}}+it\right)=O(t^{\varepsilon }),$

as *t* → $\infty$ .

The Riemann hypothesis also implies quite sharp bounds for the growth rate of the zeta function in other regions of the critical strip. For example, it implies that

$e^{\gamma }\leq \limsup _{t\rightarrow +\infty }{\frac {|\zeta (1+it)|}{\log \log t}}\leq 2e^{\gamma }$

${\frac {6}{\pi ^{2}}}e^{\gamma }\leq \limsup _{t\rightarrow +\infty }{\frac {1/|\zeta (1+it)|}{\log \log t}}\leq {\frac {12}{\pi ^{2}}}e^{\gamma }$

so the growth rate of *ζ*(1 + *it*) and its inverse would be known up to a factor of 2.

### Large prime gap conjecture

The prime number theorem implies that on average, the gap between the prime *p* and its successor is log *p*. However, some gaps between primes may be much larger than the average. Cramér proved that, assuming the Riemann hypothesis, every gap is *O*(√*p* log *p*). This is a case in which even the best bound that can be proved using the Riemann hypothesis is far weaker than what seems true: Cramér's conjecture implies that every gap is *O*((log *p*)2), which, while larger than the average gap, is far smaller than the bound implied by the Riemann hypothesis. Numerical evidence supports Cramér's conjecture.

### Analytic criteria equivalent to the Riemann hypothesis

Many statements equivalent to the Riemann hypothesis have been found, though so far none of them have led to much progress in proving (or disproving) it. Some typical examples are as follows. (Others involve the divisor function *σ*(*n*).)

The Riesz criterion was given by Riesz (1916), to the effect that the bound

$-\sum _{k=1}^{\infty }{\frac {(-x)^{k}}{(k-1)!\zeta (2k)}}=O\left(x^{{\frac {1}{4}}+\epsilon }\right)$

holds for all ε > 0 if and only if the Riemann hypothesis holds. See also the Hardy–Littlewood criterion.

Nyman (1950) proved that the Riemann hypothesis is true if and only if the space of functions of the form

$f(x)=\sum _{\nu =1}^{n}c_{\nu }\rho \left({\frac {\theta _{\nu }}{x}}\right)$

where *ρ*(*z*) is the fractional part of *z*, 0 ≤ *θ**ν* ≤ 1, and

$\sum _{\nu =1}^{n}c_{\nu }\theta _{\nu }=0,$

is dense in the Hilbert space *L*2(0,1) of square-integrable functions on the unit interval. Beurling (1955) extended this by showing that the zeta function has no zeros with real part greater than 1/*p* if and only if this function space is dense in *Lp*(0,1). This Nyman-Beurling criterion was strengthened by Baez-Duarte to the case where $\theta _{\nu }\in \{1/k\}_{k\geq 1}$ .

Salem (1953) showed that the Riemann hypothesis is true if and only if the integral equation

$\int _{0}^{\infty }{\frac {z^{-\sigma -1}\varphi (z)}{{e^{x/z}}+1}}\,dz=0$

has no non-trivial bounded solutions $\varphi$ for $1/2<\sigma <1$ .

Weil's criterion is the statement that the positivity of a certain function is equivalent to the Riemann hypothesis. Related is Li's criterion, a statement that the positivity of a certain sequence of numbers is equivalent to the Riemann hypothesis.

Speiser (1934) proved that the Riemann hypothesis is equivalent to the statement that *ζ*′(*s*), the derivative of *ζ*(*s*), has no zeros in the strip

$0<\Re (s)<{\frac {1}{2}}.$

That *ζ*(*s*) has only simple zeros on the critical line is equivalent to its derivative having no zeros on the critical line.

The Farey sequence provides two equivalences, due to Jerome Franel and Edmund Landau in 1924.

The de Bruijn–Newman constant denoted by Λ and named after Nicolaas Govert de Bruijn and Charles M. Newman, is defined as the unique real number such that the function

$H(\lambda ,z):=\int _{0}^{\infty }e^{\lambda u^{2}}\Phi (u)\cos(zu)\,du$

,

that is parametrised by a real parameter *λ*, has a complex variable *z* and is defined using a super-exponentially decaying function

$\Phi (u)=\sum _{n=1}^{\infty }(2\pi ^{2}n^{4}e^{9u}-3\pi n^{2}e^{5u})e^{-\pi n^{2}e^{4u}}$

,

has only real zeros if and only if *λ* ≥ Λ. Since the Riemann hypothesis is equivalent to the claim that all the zeroes of *H*(0, *z*) are real, the Riemann hypothesis is equivalent to the conjecture that Λ ≤ 0. Brad Rodgers and Terence Tao discovered the equivalence is actually Λ = 0 by proving zero to be the lower bound of the constant. Proving zero is also the upper bound would therefore prove the Riemann hypothesis. Newman noted that this conjecture (now theorem) "is a quantitative version of the dictum that the Riemann hypothesis, if true, is only barely so." As of April 2020 the upper bound is Λ ≤ 0.2.

### Consequences of the generalized Riemann hypothesis

Several applications use the generalized Riemann hypothesis for Dirichlet L-series or zeta functions of number fields rather than just the Riemann hypothesis. Many basic properties of the Riemann zeta function can easily be generalized to all Dirichlet L-series, so it is plausible that a method that proves the Riemann hypothesis for the Riemann zeta function would also work for the generalized Riemann hypothesis for Dirichlet L-functions. Several results first proved using the generalized Riemann hypothesis were later given unconditional proofs without using it, though these were usually much harder. Many of the consequences on the following list are taken from Conrad (2010).

- In 1913, Grönwall showed that the generalized Riemann hypothesis implies that Gauss's list of imaginary quadratic fields with class number 1 is complete, though Baker, Stark and Heegner later gave unconditional proofs of this without using the generalized Riemann hypothesis.
- In 1917, Hardy and Littlewood showed that the generalized Riemann hypothesis implies a conjecture of Chebyshev that $\lim _{x\to 1^{-}}\sum _{p>2}(-1)^{(p+1)/2}x^{p}=+\infty ,$ which says that primes 3 mod 4 are more common than primes 1 mod 4 in some sense. (For related results, see *Prime number theorem § Prime number race*.)
- In 1923, Hardy and Littlewood showed that the generalized Riemann hypothesis implies a weak form of the Goldbach conjecture for odd numbers: that every sufficiently large odd number is the sum of three primes, though in 1937 Vinogradov gave an unconditional proof. In 1997 Deshouillers, Effinger, te Riele, and Zinoviev showed that the generalized Riemann hypothesis implies that every odd number greater than 5 is the sum of three primes. In 2013 Harald Helfgott proved the ternary Goldbach conjecture without the GRH dependence, subject to some extensive calculations completed with the help of David J. Platt.
- In 1934, Chowla showed that the generalized Riemann hypothesis implies that the first prime in the arithmetic progression *a* mod *m* is at most *Km*2log(*m*)2 for some fixed constant *K*.
- In 1967, Hooley showed that the generalized Riemann hypothesis implies Artin's conjecture on primitive roots.
- In 1973, Weinberger showed that the generalized Riemann hypothesis implies that Euler's list of idoneal numbers is complete.
- Weinberger (1973) showed that the generalized Riemann hypothesis for the zeta functions of all algebraic number fields implies that any number field with class number 1 is either Euclidean or an imaginary quadratic number field of discriminant −19, −43, −67, or −163.
- In 1976, G. Miller showed that the generalized Riemann hypothesis implies that one can test if a number is prime in polynomial time via the Miller test. In 2002, Manindra Agrawal, Neeraj Kayal and Nitin Saxena proved this result unconditionally using the AKS primality test.
- Odlyzko (1990) discussed how the generalized Riemann hypothesis can be used to give sharper estimates for discriminants and class numbers of number fields.
- Ono & Soundararajan (1997) showed that the generalized Riemann hypothesis implies that Ramanujan's integral quadratic form *x*2 + *y*2 + 10*z*2 represents all integers that it represents locally, with exactly 18 exceptions.
- In 2021, Alexander (Alex) Dunn and Maksym Radziwill proved Patterson's conjecture on cubic Gauss sums, under the assumption of the GRH.

### Excluded middle

Some consequences of the RH are also consequences of its negation, and are thus theorems. In their discussion of the Hecke, Deuring, Mordell, Heilbronn theorem, Ireland & Rosen (1990, p. 359) say

> The method of proof here is truly amazing. If the generalized Riemann hypothesis is true, then the theorem is true. If the generalized Riemann hypothesis is false, then the theorem is true. Thus, the theorem is true!!

Care should be taken to understand what is meant by saying the generalized Riemann hypothesis is false: one should specify exactly which class of Dirichlet series has a counterexample.

#### Littlewood's theorem

This concerns the sign of the error in the prime number theorem. It has been computed that π(*x*) < li(*x*) for all *x* ≤ 1025 (see this table), and no value of *x* is known for which π(*x*) > li(*x*).

In 1914, Littlewood proved that there are arbitrarily large values of *x* for which

$\pi (x)>\operatorname {li} (x)+{\frac {1}{3}}{\frac {\sqrt {x}}{\log x}}\log \log \log x,$

and that there are also arbitrarily large values of *x* for which

$\pi (x)<\operatorname {li} (x)-{\frac {1}{3}}{\frac {\sqrt {x}}{\log x}}\log \log \log x.$

Thus the difference π(*x*) − li(*x*) changes sign infinitely many times. Skewes' number is an estimate of the value of *x* corresponding to the first sign change.

Littlewood's proof is divided into two cases: the RH is assumed false (about half a page of Ingham 1932, Chapt. V), and the RH is assumed true (about a dozen pages). Stanisław Knapowski followed this up with a paper on the number of times $\Delta (n)$ changes sign in the interval $\Delta (n)$ .

#### Gauss's class number conjecture

This is the conjecture (first stated in article 303 of Gauss's *Disquisitiones Arithmeticae*) that there are only finitely many imaginary quadratic fields with a given class number. One way to prove it would be to show that as the discriminant *D* → −∞ the class number *h*(*D*) → ∞.

The following sequence of theorems involving the Riemann hypothesis is described in Ireland & Rosen 1990, pp. 358–361:

**Theorem (Hecke; 1918)**—Let *D* < 0 be the discriminant of an imaginary quadratic number field *K*. Assume the generalized Riemann hypothesis for *L*-functions of all imaginary quadratic Dirichlet characters. Then there is an absolute constant *C* such that $h(D)>C{\frac {\sqrt {|D|}}{\log |D|}}.$

**Theorem (Deuring; 1933)**—If the RH is false then *h*(*D*) > 1 if |*D*| is sufficiently large.

**Theorem (Mordell; 1934)**—If the RH is false then *h*(*D*) → ∞ as *D* → −∞.

**Theorem (Heilbronn; 1934)**—If the generalized RH is false for the *L*-function of some imaginary quadratic Dirichlet character then *h*(*D*) → ∞ as *D* → −∞.

(In the work of Hecke and Heilbronn, the only *L*-functions that occur are those attached to imaginary quadratic characters, and it is only for those *L*-functions that *GRH is true* or *GRH is false* is intended; a failure of GRH for the *L*-function of a cubic Dirichlet character would, strictly speaking, mean GRH is false, but that was not the kind of failure of GRH that Heilbronn had in mind, so his assumption was more restricted than simply *GRH is false*.)

In 1935, Carl Siegel strengthened the result without using RH or GRH in any way.

#### Growth of Euler's totient

In 1983 J. L. Nicolas proved that $\varphi (n)<e^{-\gamma }{\frac {n}{\log \log n}}$ for infinitely many *n*, where *φ*(*n*) is Euler's totient function and *γ* is Euler's constant. Ribenboim remarks that: "The method of proof is interesting, in that the inequality is shown first under the assumption that the Riemann hypothesis is true, secondly under the contrary assumption."


## Generalizations and analogs

### Dirichlet L-series and other number fields

The Riemann hypothesis can be generalized by replacing the Riemann zeta function by the formally similar, but much more general, global L-functions. In this broader setting, one expects the non-trivial zeros of the global *L*-functions to have real part 1/2. It is these conjectures, rather than the classical Riemann hypothesis only for the single Riemann zeta function, which account for the true importance of the Riemann hypothesis in mathematics.

The most common generalized Riemann hypothesis extends the Riemann hypothesis to all Dirichlet L-functions. In particular it implies the conjecture that Siegel zeros (zeros of *L*-functions between 1/2 and 1) do not exist.

The extended Riemann hypothesis extends the Riemann hypothesis to all Dedekind zeta functions of algebraic number fields. Since Dedekind zeta function for abelian extension of the rationals can be expressed as product of Dirichlet L-functions and only possible pole is in 1 for Riemann zeta function (thus no pole can cancel nontrivial zero), this version of Riemann hypothesis implies generalized Riemann hypothesis.

The Riemann hypothesis can also be extended to the *L*-functions of Hecke characters of number fields. Since Dirichlet L-functions are Hecke L-functions for finite characters, then this hypothesis directly implies generalized Riemann hypothesis. Dedekind zeta functions can be expressed as product of Hecke L-functions and only possible pole of Hecke L-function is at 1, then this version of Riemann Hypothesis implies also version for Dedekind zeta functions.

There are two approaches for extension of Riemann hypothesis that seem to be the most general. The grand Riemann hypothesis extends it to all Automorphic L-functions, such as Mellin transforms of Hecke eigenforms. The Riemann hypothesis for Selberg class extends it rather for functions satisfying some properties (at least conjecturaly satisfied by most functions usually called *zeta functions* or *L-functions*) than for functions defined by direct formula. Though it is expected that Selberg class should be equal to class of automorphic L-functions, and thus this approaches should be equivalent, this is important open problem itself and part of Langlands program.

### Function fields and zeta functions of varieties over finite fields

Artin (1924) introduced global zeta functions of (quadratic) function fields and conjectured an analogue of the Riemann hypothesis for them, which has been proved by Hasse in the genus 1 case and by Weil (1948) in general. For instance, the fact that the Gauss sum, of the quadratic character of a finite field of size *q* (with *q* odd), has absolute value ${\sqrt {q}}$ is actually an instance of the Riemann hypothesis in the function field setting. This led Weil (1949) to conjecture a similar statement for all algebraic varieties; the resulting Weil conjectures were proved by Pierre Deligne.

### Arithmetic zeta functions of arithmetic schemes and their L-factors

Arithmetic zeta functions generalise the Riemann and Dedekind zeta functions as well as the zeta functions of varieties over finite fields to every arithmetic scheme or a scheme of finite type over integers. The arithmetic zeta function of a regular connected equidimensional arithmetic scheme of Kronecker dimension *n* can be factorized into the product of appropriately defined L-factors and an auxiliary factor. Assuming a functional equation and meromorphic continuation, the generalized Riemann hypothesis for the L-factor states that its zeros inside the critical strip $\Re (s)\in (0,n)$ lie on the central line. Correspondingly, the generalized Riemann hypothesis for the arithmetic zeta function of a regular connected equidimensional arithmetic scheme states that its zeros inside the critical strip lie on vertical lines $\Re (s)=1/2,3/2,\dots ,n-1/2$ and its poles inside the critical strip lie on vertical lines $\Re (s)=1,2,\dots ,n-1$ . This is known for schemes in positive characteristic and follows from Pierre Deligne, but remains entirely unknown in characteristic zero.

### Selberg zeta functions

Selberg (1956) introduced the Selberg zeta function of a Riemann surface. These are similar to the Riemann zeta function: they have a functional equation, and an infinite product similar to the Euler product but taken over closed geodesics rather than primes. The Selberg trace formula is the analogue for these functions of the explicit formulas in prime number theory. Selberg proved that the Selberg zeta functions satisfy the analogue of the Riemann hypothesis, with the imaginary parts of their zeros related to the eigenvalues of the Laplacian operator of the Riemann surface.

### Ihara zeta functions

The Ihara zeta function of a finite graph is an analogue of the Selberg zeta function, which was first introduced by Yasutaka Ihara in the context of discrete subgroups of the two-by-two p-adic special linear group. A regular finite graph is a Ramanujan graph, a mathematical model of efficient communication networks, if and only if its Ihara zeta function satisfies the analogue of the Riemann hypothesis as was pointed out by T. Sunada.

### Montgomery's pair correlation conjecture

Montgomery (1973) suggested the pair correlation conjecture that the correlation functions of the (suitably normalized) zeros of the zeta function should be the same as those of the eigenvalues of a random hermitian matrix. Odlyzko (1987) showed that this is supported by large-scale numerical calculations of these correlation functions.

Montgomery showed that (assuming the Riemann hypothesis) at least 2/3 of all zeros are simple, and a related conjecture is that all zeros of the zeta function are simple (or more generally have no non-trivial integer linear relations between their imaginary parts). Dedekind zeta functions of algebraic number fields, which generalize the Riemann zeta function, often do have multiple complex zeros. This is because the Dedekind zeta functions factorize as a product of powers of Artin L-functions, so zeros of Artin L-functions sometimes give rise to multiple zeros of Dedekind zeta functions. Other examples of zeta functions with multiple zeros are the L-functions of some elliptic curves: these can have multiple zeros at the real point of their critical line; the Birch-Swinnerton-Dyer conjecture predicts that the multiplicity of this zero is the rank of the elliptic curve.

### Other zeta functions

There are many other examples of zeta functions with analogues of the Riemann hypothesis, some of which have been proved. Goss zeta functions of function fields have a Riemann hypothesis, proved by Sheats (1998). The main conjecture of Iwasawa theory, proved by Barry Mazur and Andrew Wiles for cyclotomic fields, and Wiles for totally real fields, identifies the zeros of a *p*-adic *L*-function with the eigenvalues of an operator, so can be thought of as an analogue of the Hilbert–Pólya conjecture for *p*-adic *L*-functions.


## Attempted proofs

Several mathematicians have addressed the Riemann hypothesis, but none of their attempts has yet been accepted as a proof. Watkins (2021) lists some incorrect solutions.

### Operator theory

Hilbert and Pólya suggested that one way to derive the Riemann hypothesis would be to find a self-adjoint operator, from the existence of which the statement on the real parts of the zeros of *ζ*(*s*) would follow when one applies the criterion on real eigenvalues. Some support for this idea comes from several analogues of the Riemann zeta functions whose zeros correspond to eigenvalues of some operator: the zeros of a zeta function of a variety over a finite field correspond to eigenvalues of a Frobenius element on an étale cohomology group, the zeros of a Selberg zeta function are eigenvalues of a Laplacian operator of a Riemann surface, and the zeros of a p-adic zeta function correspond to eigenvectors of a Galois action on ideal class groups.

Odlyzko (1987) showed that the distribution of the zeros of the Riemann zeta function shares some statistical properties with the eigenvalues of random matrices drawn from the Gaussian unitary ensemble. This gives some support to the Hilbert–Pólya conjecture.

In 1999, Michael Berry and Jonathan Keating conjectured that there is some unknown quantization ${\hat {H}}$ of the classical Hamiltonian *H* = *xp* so that $\zeta (1/2+i{\hat {H}})=0$ and even more strongly, that the Riemann zeros coincide with the spectrum of the operator $1/2+i{\hat {H}}$ . This is in contrast to canonical quantization, which leads to the Heisenberg uncertainty principle $\sigma _{x}\sigma _{p}\geq {\frac {\hbar }{2}}$ and the natural numbers as spectrum of the quantum harmonic oscillator. The crucial point is that the Hamiltonian should be a self-adjoint operator so that the quantization would be a realization of the Hilbert–Pólya program. In a connection with this quantum mechanical problem Berry and Connes had proposed that the inverse of the potential of the Hamiltonian is connected to the half-derivative of the function $N(s)={\frac {1}{\pi }}\operatorname {Arg} \xi (1/2+i{\sqrt {s}})$ then, in Hilbert-Polya approach $V^{-1}(x)={\sqrt {4\pi }}{\frac {d^{1/2}N(x)}{dx^{1/2}}}.$ This yields a Hamiltonian whose eigenvalues are the square of the imaginary part of the Riemann zeros, and also that the functional determinant of this Hamiltonian operator is just the Riemann Xi function. In fact the Riemann Xi function would be proportional to the functional determinant (Hadamard product) $\det(H+1/4+s(s-1))$ ${\frac {\xi (s)}{\xi (0)}}={\frac {\det(H+s(s-1)+1/4)}{\det(H+1/4)}}.$ However this operator is not useful in practice since it includes the inverse function (implicit function) of the potential but not the potential itself. The analogy with the Riemann hypothesis over finite fields suggests that the Hilbert space containing eigenvectors corresponding to the zeros might be some sort of first cohomology group of the spectrum Spec (*Z*) of the integers. Deninger (1998) described some of the attempts to find such a cohomology theory.

Zagier (1981) constructed a natural space of invariant functions on the upper half plane that has eigenvalues under the Laplacian operator that correspond to zeros of the Riemann zeta function—and remarked that in the unlikely event that one could show the existence of a suitable positive definite inner product on this space, the Riemann hypothesis would follow. Cartier (1982) discussed a related example, where due to a bizarre bug a computer program listed zeros of the Riemann zeta function as eigenvalues of the same Laplacian operator.

Schumayer & Hutchinson (2011) surveyed some of the attempts to construct a suitable physical model related to the Riemann zeta function.

### Lee–Yang theorem

The Lee–Yang theorem states that the zeros of certain partition functions in statistical mechanics all lie on a "critical line" with their real part equal to 0, and this has led to some speculation about a relationship with the Riemann hypothesis.

### Turán's result

Pál Turán showed that if the functions $\sum _{n=1}^{N}n^{-s}$ have no zeros when the real part of *s* is greater than one then $T(x)=\sum _{n\leq x}{\frac {\lambda (n)}{n}}\geq 0{\text{ for }}x>0,$ where λ(*n*) is the Liouville function given by (−1)*r* if *n* has *r* prime factors. He showed that this in turn would imply that the Riemann hypothesis is true. But Haselgrove (1958) proved that *T*(*x*) is negative for infinitely many *x* (and also disproved the closely related Pólya conjecture), and Borwein, Ferguson & Mossinghoff (2008) showed that the smallest such *x* is 72185376951205. Spira (1968) showed by numerical calculation that the finite Dirichlet series above for *N* = 19 has a zero with real part greater than 1. Turán also showed that a somewhat weaker assumption, the nonexistence of zeros with real part greater than 1 + *N*−1/2+*ε* for large *N* in the finite Dirichlet series above, would also imply the Riemann hypothesis, but Montgomery (1983) showed that for all sufficiently large *N* these series have zeros with real part greater than 1 + (log log *N*)/(4 log *N*). Therefore, Turán's result is vacuously true and cannot help prove the Riemann hypothesis.

### Noncommutative geometry

Alain Connes has described a relationship between the Riemann hypothesis and noncommutative geometry, and showed that a suitable analog of the Selberg trace formula for the action of the idèle class group on the adèle class space would imply the Riemann hypothesis. Some of these ideas are elaborated in Lapidus (2008).

### Hilbert spaces of entire functions

Louis de Branges showed that the Riemann hypothesis would follow from a positivity condition on a certain Hilbert space of entire functions. However Conrey & Li (2000) showed that the necessary positivity conditions are not satisfied. Despite this obstacle, de Branges has continued to work on an attempted proof of the Riemann hypothesis along the same lines, but this has not been widely accepted by other mathematicians.

### Quasicrystals

The Riemann hypothesis implies that the zeros of the zeta function form a quasicrystal, a distribution with discrete support whose Fourier transform also has discrete support. Dyson (2009) suggested trying to prove the Riemann hypothesis by classifying, or at least studying, 1-dimensional quasicrystals.

### Arithmetic zeta functions of models of elliptic curves over number fields

When one goes from geometric dimension one, e.g. an algebraic number field, to geometric dimension two, e.g. a regular model of an elliptic curve over a number field, the two-dimensional part of the generalized Riemann hypothesis for the arithmetic zeta function of the model deals with the poles of the zeta function. In dimension one the study of the zeta integral in Tate's thesis does not lead to new important information on the Riemann hypothesis. Contrary to this, in dimension two work of Ivan Fesenko on two-dimensional generalisation of Tate's thesis includes an integral representation of a zeta integral closely related to the zeta function. In this new situation, not possible in dimension one, the poles of the zeta function can be studied via the zeta integral and associated adele groups. Related conjecture of Ivan Fesenko on the positivity of the fourth derivative of a boundary function associated to the zeta integral essentially implies the pole part of the generalized Riemann hypothesis. Suzuki (2011) proved that the latter, together with some technical assumptions, implies Fesenko's conjecture.

### Multiple zeta functions

Deligne's proof of the Riemann hypothesis over finite fields used the zeta functions of product varieties, whose zeros and poles correspond to sums of zeros and poles of the original zeta function, in order to bound the real parts of the zeros of the original zeta function. By analogy, Kurokawa (1992) introduced multiple zeta functions whose zeros and poles correspond to sums of zeros and poles of the Riemann zeta function. To make the series converge he restricted to sums of zeros or poles all with non-negative imaginary part. So far, the known bounds on the zeros and poles of the multiple zeta functions are not strong enough to give useful estimates for the zeros of the Riemann zeta function.
