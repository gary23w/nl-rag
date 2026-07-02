---
title: "Riemann hypothesis (part 2/2)"
source: https://en.wikipedia.org/wiki/Riemann_hypothesis
domain: analytic-number-theory
license: CC-BY-SA-4.0
tags: analytic number theory, prime number theorem, dirichlet series, riemann hypothesis
fetched: 2026-07-02
part: 2/2
---

## Location of the zeros

### Number of zeros

The functional equation combined with the argument principle implies that the number of zeros of the zeta function with imaginary part between 0 and *T* is given by

$N(T)={\frac {1}{\pi }}\mathop {\mathrm {Arg} } (\xi (s))={\frac {1}{\pi }}\mathop {\mathrm {Arg} } (\Gamma ({\tfrac {s}{2}})\pi ^{-{\frac {s}{2}}}\zeta (s)s(s-1)/2)$

for *s* = 1/2 + *iT*, where the argument is defined by varying it continuously along the line with Im(*s*) = *T*, starting with argument 0 at ∞ + *iT*. This is the sum of a large but well understood term

${\frac {1}{\pi }}\mathop {\mathrm {Arg} } (\Gamma ({\tfrac {s}{2}})\pi ^{-s/2}s(s-1)/2)={\frac {T}{2\pi }}\log {\frac {T}{2\pi }}-{\frac {T}{2\pi }}+7/8+O(1/T)$

and a small but rather mysterious term

$S(T)={\frac {1}{\pi }}\mathop {\mathrm {Arg} } (\zeta (1/2+iT))=O(\log T).$

So the density of zeros with imaginary part near *T* is about log(*T*)/(2π), and the function *S* describes the small deviations from this. The function *S*(*t*) jumps by 1 at each zero of the zeta function, and for *t* ≥ 8 it decreases monotonically between zeros with derivative close to −log *t*.

Trudgian (2014) proved that, if *T* > *e*, then

$|N(T)-{\frac {T}{2\pi }}\log {\frac {T}{2\pi e}}|\leq 0.112\log T+0.278\log \log T+3.385+{\frac {0.2}{T}}$

.

Karatsuba (1996) proved that every interval (*T*, *T* + *H*] for $H\geq T^{{\frac {27}{82}}+\varepsilon }$ contains at least

$H(\log T)^{\frac {1}{3}}e^{-c{\sqrt {\log \log T}}}$

points where the function *S*(*t*) changes sign.

Selberg (1946) showed that the average moments of even powers of *S* are given by

$\int _{0}^{T}|S(t)|^{2k}dt={\frac {(2k)!}{k!(2\pi )^{2k}}}T(\log \log T)^{k}+O(T(\log \log T)^{k-1/2}).$

This suggests that *S*(*T*)/(log log *T*)1/2 resembles a Gaussian random variable with mean 0 and variance 2π2 (Ghosh (1983) proved this fact). In particular |*S*(*T*)| is usually somewhere around (log log *T*)1/2, but occasionally much larger. The exact order of growth of *S*(*T*) is not known. There has been no unconditional improvement to Riemann's original bound *S*(*T*) = *O*(log *T*), though the Riemann hypothesis implies the slightly smaller bound *S*(*T*) = *O*(log *T*/log log *T*). The true order of magnitude may be somewhat less than this, as random functions with the same distribution as *S*(*T*) tend to have growth of order about log(*T*)1/2. In the other direction it cannot be too small: Selberg (1946) showed that *S*(*T*) ≠ *o*((log *T*)1/3/(log log *T*)7/3), and assuming the Riemann hypothesis Montgomery showed that *S*(*T*) ≠ *o*((log *T*)1/2/(log log *T*)1/2).

Numerical calculations confirm that *S* grows very slowly: |*S*(*T*)| < 1 for *T* < 280, |*S*(*T*)| < 2 for *T* < 6800000, and the largest value of |*S*(*T*)| found so far is not much larger than 3.

Riemann's estimate *S*(*T*) = *O*(log *T*) implies that the gaps between zeros are bounded, and Littlewood improved this slightly, showing that the gaps between their imaginary parts tend to 0.

### Theorem of Hadamard and de la Vallée-Poussin

Hadamard (1896) and de la Vallée-Poussin (1896) independently proved that no zeros could lie on the line Re(*s*) = 1. Together with the functional equation and the fact that there are no zeros with real part greater than 1, this showed that all non-trivial zeros must lie in the interior of the critical strip 0 < Re(*s*) < 1. This was a key step in their first proofs of the prime number theorem.

Both the original proofs that the zeta function has no zeros with real part 1 are similar, and depend on showing that if *ζ*(1 + *it*) vanishes, then *ζ*(1 + 2*it*) is singular, which is not possible. One way of doing this is by using the inequality

$|\zeta (\sigma )^{3}\zeta (\sigma +it)^{4}\zeta (\sigma +2it)|\geq 1$

for *σ* > 1, *t* real, and looking at the limit as *σ* → 1. This inequality follows by taking the real part of the log of the Euler product to see that

$|\zeta (\sigma +it)|=\exp \Re \sum _{p^{n}}{\frac {p^{-n(\sigma +it)}}{n}}=\exp \sum _{p^{n}}{\frac {p^{-n\sigma }\cos(t\log p^{n})}{n}},$

where the sum is over all prime powers *p**n*, so that

$|\zeta (\sigma )^{3}\zeta (\sigma +it)^{4}\zeta (\sigma +2it)|=\exp \sum _{p^{n}}p^{-n\sigma }{\frac {3+4\cos(t\log p^{n})+\cos(2t\log p^{n})}{n}}$

which is at least 1 because all the terms in the sum are positive, due to the inequality

$3+4\cos(\theta )+\cos(2\theta )=2(1+\cos(\theta ))^{2}\geq 0.$

### Zero-free regions

The most extensive computer search by Platt and Trudgian for counterexamples of the Riemann hypothesis has verified it for |*t*| ≤ 3.0001753328×1012. Beyond that zero-free regions are known as inequalities concerning *σ* + *i t*, which can be zeroes. The oldest version is from De la Vallée-Poussin (1899–1900), who proved there is a region without zeroes that satisfies 1 − *σ* ≥ ⁠*C*/log(*t*)⁠ for some positive constant *C*. In other words, zeros cannot be too close to the line *σ* = 1: there is a zero-free region close to this line. This has been enlarged by several authors using methods such as Vinogradov's mean-value theorem.

The most recent paper by Mossinghoff, Trudgian and Yang is from December 2022 and provides four zero-free regions that improved the previous results of Kevin Ford from 2002, Mossinghoff and Trudgian themselves from 2015 and Pace Nielsen's slight improvement of Ford from October 2022:

$\sigma \geq 1-{\frac {1}{5.558691\log |t|}}$

whenever

$|t|\geq 2$

,

$\sigma \geq 1-{\frac {1}{55.241(\log {|t|})^{2/3}(\log {\log {|t|}})^{1/3}}}$

whenever

$|t|\geq 3$

(largest known region in the bound

$3.0001753328\cdot 10^{12}\leq |t|\leq \exp(64.1)\approx 6.89\cdot 10^{27}$

),

$\sigma \geq 1-{\frac {0.04962-{\frac {0.0196}{1.15+\log 3+{\frac {1}{6}}\log t+\log \log t}}}{0.685+\log 3+{\frac {1}{6}}\log t+1.155\cdot \log \log t}}$

whenever

$|t|\geq 1.88\cdot 10^{14}$

(largest known region in the bound

$\exp(64.1)\leq |t|\leq \exp(1000)\approx 1.97\cdot 10^{434}$

) and

$\sigma \geq 1-{\frac {0.05035}{{\frac {27}{164}}(\log {|t|})+7.096}}+{\frac {0.0349}{({\frac {27}{164}}(\log {|t|})+7.096)^{2}}}$

whenever

$|t|\geq \exp(1000)$

(largest known region in its own bound)

The paper also presents an improvement to the second zero-free region, whose bounds are unknown on account of $|t|$ being merely assumed to be "sufficiently large" to fulfill the requirements of the paper's proof. This region is

$\sigma \geq 1-{\frac {1}{48.1588(\log {|t|})^{2/3}(\log {\log {|t|}})^{1/3}}}$

.


## Zeros on the critical line

Hardy (1914) and Hardy & Littlewood (1921) showed there are infinitely many zeros on the critical line, by considering moments of certain functions related to the zeta function. Selberg (1942) proved that at least a (small) positive proportion of zeros lie on the line. Levinson (1974) improved this to one-third of the zeros by relating the zeros of the zeta function to those of its derivative, and Conrey (1989) improved this further to two-fifths. In 2020, this estimate was extended to five-twelfths by Pratt, Robles, Zaharescu and Zeindler by considering extended mollifiers that can accommodate higher order derivatives of the zeta function and their associated Kloosterman sums.

Most zeros lie close to the critical line. More precisely, Bohr & Landau (1914) showed that for any positive *ε*, the number of zeros with real part at least 1/2+*ε* and imaginary part at between −*T* and *T* is $O(T)$ . Combined with the facts that zeros on the critical strip are symmetric about the critical line and that the total number of zeros in the critical strip is $\Theta (T\log T)$ , almost all non-trivial zeros are within a distance *ε* of the critical line. Ivić (1985) gives several more precise versions of this result, called *zero density estimates*, which bound the number of zeros in regions with imaginary part at most *T* and real part at least 1/2 + *ε*.

### Hardy–Littlewood conjectures

In 1914 Godfrey Harold Hardy proved that $\zeta \left({\tfrac {1}{2}}+it\right)$ has infinitely many real zeros.

The next two conjectures of Hardy and John Edensor Littlewood on the distance between real zeros of $\zeta \left({\tfrac {1}{2}}+it\right)$ and on the density of zeros of $\zeta \left({\tfrac {1}{2}}+it\right)$ on the interval $(T,T+H]$ for sufficiently large $T>0$ , and $H=T^{a+\varepsilon }$ and with as small as possible value of $a>0$ , where $\varepsilon >0$ is an arbitrarily small number, open two new directions in the investigation of the Riemann zeta function:

1. For any $\varepsilon >0$ there exists a lower bound $T_{0}=T_{0}(\varepsilon )>0$ such that for $T\geq T_{0}$ and $H=T^{{\tfrac {1}{4}}+\varepsilon }$ the interval $(T,T+H]$ contains a zero of odd order of the function $\zeta {\bigl (}{\tfrac {1}{2}}+it{\bigr )}$ .

Let $N(T)$ be the total number of real zeros, and $N_{0}(T)$ be the total number of zeros of odd order of the function $~\zeta \left({\tfrac {1}{2}}+it\right)~$ lying on the interval $(0,T]~$ .

2. For any $\varepsilon >0$ there exists $T_{0}=T_{0}(\varepsilon )>0$ and some $c=c(\varepsilon )>0$ , such that for $T\geq T_{0}$ and $H=T^{{\tfrac {1}{2}}+\varepsilon }$ the inequality $N_{0}(T+H)-N_{0}(T)\geq cH$ is true.

### Selberg's zeta function conjecture

Atle Selberg investigated the problem of Hardy–Littlewood *2* and proved that for any *ε* > 0 there exists such $T_{0}=T_{0}(\varepsilon )>0$ and *c* = *c*(*ε*) > 0, such that for $T\geq T_{0}$ and $H=T^{0.5+\varepsilon }$ the inequality $N(T+H)-N(T)\geq cH\log T$ is true. Selberg conjectured that this could be tightened to $H=T^{0.5}$ . Anatoly Karatsuba proved that for a fixed *ε* satisfying the condition 0 < *ε* < 0.001, a sufficiently large *T* and $H=T^{a+\varepsilon }$ , $a={\tfrac {27}{82}}={\tfrac {1}{3}}-{\tfrac {1}{246}}$ , the interval (*T*, *T*+*H*) contains at least *cH* log(*T*) real zeros of the Riemann zeta function $\zeta \left({\tfrac {1}{2}}+it\right)$ and therefore confirmed the Selberg conjecture. The estimates of Selberg and Karatsuba can not be improved in respect of the order of growth as *T* → ∞.

Karatsuba (1992) proved that an analog of the Selberg conjecture holds for almost all intervals (*T*, *T*+*H*], $H=T^{\varepsilon }$ , where *ε* is an arbitrarily small fixed positive number. The Karatsuba method permits to investigate zeros of the Riemann zeta function on "supershort" intervals of the critical line, that is, on the intervals (*T*, *T*+*H*], the length *H* of which grows slower than any, even arbitrarily small degree *T*. In particular, he proved that for any given numbers *ε*, $\varepsilon _{1}$ satisfying the conditions $0<\varepsilon ,\varepsilon _{1}<1$ almost all intervals (*T*, *T*+*H*] for $H\geq \exp {\{(\log T)^{\varepsilon }\}}$ contain at least $H(\log T)^{1-\varepsilon _{1}}$ zeros of the function $\zeta \left({\tfrac {1}{2}}+it\right)$ . This estimate is quite close to the one that follows from the Riemann hypothesis.

### Numerical calculations

The function

$\pi ^{-{\frac {s}{2}}}\Gamma ({\tfrac {s}{2}})\zeta (s)$

has the same zeros as the zeta function in the critical strip, and is real on the critical line because of the functional equation, so one can prove the existence of zeros exactly on the real line between two points by checking numerically that the function has opposite signs at these points. Usually one writes

$\zeta ({\tfrac {1}{2}}+it)=Z(t)e^{-i\theta (t)}$

where Hardy's Z function and the Riemann–Siegel theta function *θ* are uniquely defined by this and the condition that they are smooth real functions with *θ*(0) = 0. By finding many intervals where the function *Z* changes sign one can show that there are many zeros on the critical line. To verify the Riemann hypothesis up to a given imaginary part *T* of the zeros, one also has to check that there are no further zeros off the line in this region. This can be done by calculating the total number of zeros in the region using Turing's method and checking that it is the same as the number of zeros found on the line. This allows one to verify the Riemann hypothesis computationally up to any desired value of *T* (provided all the zeros of the zeta function in this region are simple and on the critical line).

These calculations can also be used to estimate $\pi (x)$ for finite ranges of x . For example, using the latest result from 2020 (zeros up to height $3\times 10^{12}$ ), it has been shown that

$|\pi (x)-\operatorname {li} (x)|<{\frac {1}{8\pi }}{\sqrt {x}}\log(x),\qquad {\text{for }}2657\leq x\leq 1.101\times 10^{26}.$

In general, this inequality holds if

$x\geq 2657$

and

${\frac {9.06}{\log {\log {x}}}}{\sqrt {\frac {x}{\log {x}}}}\leq T,$

where T is the largest known value such that the Riemann hypothesis is true for all zeros $\rho$ with $\Im {\left(\rho \right)}\in \left(0,T\right]$ .

Some calculations of zeros of the zeta function are listed below, where the "height" of a zero is the magnitude of its imaginary part, and the height of the *n*th zero is denoted by *γn*. So far all zeros that have been checked are on the critical line and are simple. (A multiple zero would cause problems for the zero finding algorithms, which depend on finding sign changes between zeros.) For tables of the zeros, see Haselgrove & Miller (1960) or Odlyzko.

| Year | Number of zeros | Author |
|---|---|---|
| 1859? | 3 | B. Riemann used the Riemann–Siegel formula (unpublished, but reported in Siegel 1932). |
| 1903 | 15 | J. P. Gram (1903) used the Euler–Maclaurin formula and discovered Gram's law. He showed that all 10 zeros with imaginary part at most 50 range lie on the critical line with real part 1/2 by computing the sum of the inverse 10th powers of the roots he found. |
| 1914 | 79 (*γn* ≤ 200) | R. J. Backlund (1914) introduced a better method of checking all the zeros up to that point are on the line, by studying the argument *S*(*T*) of the zeta function. |
| 1925 | 138 (*γn* ≤ 300) | J. I. Hutchinson (1925) found the first failure of Gram's law, at the Gram point *g*126. |
| 1935 | 195 | E. C. Titchmarsh (1935) used the recently rediscovered Riemann–Siegel formula, which is much faster than Euler–Maclaurin summation. It takes about O(*T*3/2 + *ε*) steps to check zeros with imaginary part less than *T*, while the Euler–Maclaurin method takes about O(*T*2 + *ε*) steps. |
| 1936 | 1041 | E. C. Titchmarsh (1936) and L. J. Comrie were the last to find zeros by hand. |
| 1953 | 1104 | A. M. Turing (1953) found a more efficient way to check that all zeros up to some point are accounted for by the zeros on the line, by checking that *Z* has the correct sign at several consecutive Gram points and using the fact that *S*(*T*) has average value 0. This requires almost no extra work because the sign of *Z* at Gram points is already known from finding the zeros, and is still the usual method used. This was the first use of a digital computer to calculate the zeros. |
| 1956 | 15000 | D. H. Lehmer (1956) discovered a few cases where the zeta function has zeros that are "only just" on the line: two zeros of the zeta function are so close together that it is unusually difficult to find a sign change between them. This is called "Lehmer's phenomenon", and first occurs at the zeros with imaginary parts 7005.063 and 7005.101, which differ by only .04 while the average gap between other zeros near this point is about 1. |
| 1956 | 25000 | D. H. Lehmer |
| 1958 | 35337 | N. A. Meller |
| 1966 | 250000 | R. S. Lehman |
| 1968 | 3500000 | Rosser, Yohe & Schoenfeld (1969) stated Rosser's rule (described below). |
| 1977 | 40000000 | R. P. Brent |
| 1979 | 81000001 | R. P. Brent |
| 1982 | 200000001 | R. P. Brent, J. van de Lune, H. J. J. te Riele, D. T. Winter |
| 1983 | 300000001 | J. van de Lune, H. J. J. te Riele |
| 1986 | 1500000001 | van de Lune, te Riele & Winter (1986) gave some statistical data about the zeros and give several graphs of *Z* at places where it has unusual behavior. |
| 1987 | A few of large (≈1012) height | A. M. Odlyzko (1987) computed smaller numbers of zeros of much larger height, around 1012, to high precision to check Montgomery's pair correlation conjecture. |
| 1992 | A few of large (≈1020) height | A. M. Odlyzko (1992) computed 175 million zeros of heights around 1020 and a few more of heights around 2×1020, and gave an extensive discussion of the results. |
| 1998 | 10000 of large (≈1021) height | A. M. Odlyzko (1998) computed some zeros of height about 1021 |
| 2001 | 1010 | J. van de Lune (unpublished) |
| 2004 | ≈9×1011 | S. Wedeniwski (ZetaGrid distributed computing) |
| 2004 | 1013 and a few of large (up to ≈1024) heights | Xavier Gourdon (2004) and Patrick Demichel used the Odlyzko–Schönhage algorithm. They also checked two billion zeros around heights *γn* = 1013, 1014, ..., 1024. |
| 2020 | 1.2363×1013 (*γn* ≤ 3×1012) | Platt & Trudgian (2021). They also verified the work of Gourdon (2004) and others. |

### Gram points

A Gram point is a point on the critical line 1/2 + *it* where the zeta function is real and non-zero. Using the expression for the zeta function on the critical line, *ζ*(1/2 + *it*) = *Z*(*t*)*e*−*iθ*(*t*), where Hardy's function, *Z*, is real for real *t*, and *θ* is the Riemann–Siegel theta function, we see that zeta is real when sin(*θ*(*t*)) = 0. This implies that *θ*(*t*) is an integer multiple of π, which allows for the location of Gram points to be calculated fairly easily by inverting the formula for *θ*. They are usually numbered as *gn* for *n* = 0, 1, ..., where *gn* is the unique solution of *θ*(*t*) = *n*π.

Gram observed that there was often exactly one zero of the zeta function between any two consecutive Gram points; Hutchinson called this observation **Gram's law**. There are several other closely related statements that are also sometimes called Gram's law: for example, (−1)*n**Z*(*gn*) is usually positive, or *Z*(*t*) usually has opposite sign at consecutive Gram points. The imaginary parts *γn* of the first few zeros (in blue) and the first few Gram points *gn* are given in the following table

g

−1

γ

1

g

0

γ

2

g

1

γ

3

g

2

γ

4

g

3

γ

5

g

4

γ

6

g

5

0

3.436

9.667

14.135

17.846

21.022

23.170

25.011

27.670

30.425

31.718

32.935

35.467

37.586

38.999

The first failure of Gram's law occurs at the 127th zero and the Gram point *g*126, which are in the "wrong" order.

g

124

γ

126

g

125

g

126

γ

127

γ

128

g

127

γ

129

g

128

279.148

279.229

280.802

282.455

282.465

283.211

284.104

284.836

285.752

A Gram point *t* is called good if the zeta function is positive at 1/2 + *it*. The indices of the "bad" Gram points where *Z* has the "wrong" sign are 126, 134, 195, 211, ... (sequence A114856 in the OEIS). A *Gram block* is an interval bounded by two good Gram points such that all the Gram points between them are bad. A refinement of Gram's law called Rosser's rule due to Rosser, Yohe & Schoenfeld (1969) says that Gram blocks often have the expected number of zeros in them (the same as the number of Gram intervals), even though some of the individual Gram intervals in the block may not have exactly one zero in them. For example, the interval bounded by *g*125 and *g*127 is a Gram block containing a unique bad Gram point *g*126, and contains the expected number 2 of zeros although neither of its two Gram intervals contains a unique zero. Rosser et al. checked that there were no exceptions to Rosser's rule in the first 3 million zeros, although there are infinitely many exceptions to Rosser's rule over the entire zeta function.

Gram's rule and Rosser's rule both say that in some sense zeros do not stray too far from their expected positions. The distance of a zero from its expected position is controlled by the function *S* defined above, which grows extremely slowly: its average value is of the order of (log log *T*)1/2, which only reaches 2 for T around 1024. This means that both rules hold most of the time for small *T* but eventually break down often. Indeed, Trudgian (2011) showed that both Gram's law and Rosser's rule fail in a positive proportion of cases. To be specific, it is expected that in about 66% one zero is enclosed by two successive Gram points, but in 17% no zero and in 17% two zeros are in such a Gram-interval on the long run Hanga (2020).

### Random matrix theory and quantum chaos

Assuming the Riemann hypothesis one can ask what further regularities might govern the distribution of the zeros of the zeta function on the critical line. One conjectural picture is that the critical zeros of the zeta function behave statistically like the eigenvalues of large random Hermitian matrices. The idea began with Hugh Montgomery's work on the pair correlation conjecture for the zeros of the zeta function. After a suitable rescaling to account for the increasing density of zeros with height, the conjectured pair correlation function agrees with that of eigenvalues in the Gaussian unitary ensemble (GUE) in random matrix theory.

The connection was tested numerically by Andrew Odlyzko, who found that the spacing statistics of zeros high on the critical line agree closely with the predictions of GUE random matrix theory. The agreement extends beyond nearest-neighbor spacings to higher correlation functions, and is widely regarded as strong evidence that the zeros are modeled by the same local statistics as random matrices.

The random matrix analogy is also related to the Hilbert–Pólya conjecture, and to ideas from quantum chaos. In quantum chaotic systems, eigenvalues often obey random matrix statistics, so the appearance of the same statistics in the zeros of the zeta function can be interpreted as evidence that they may arise from a selfadjoint operator or from a chaotic dynamical system. This gives a heuristic picture of why the zeros might lie on a spectral line and why their spacings exhibit strong repulsion rather than random clustering.

This viewpoint was adopted by Nicholas Katz and Peter Sarnak, who proposed that families of L-functions have symmetry types governed by the compact classical groups (unitary, orthogonal, or symplectic), and that the distributions of their low-lying zeros should match the corresponding random-matrix ensembles. For the Riemann zeta function, the relevant ensemble is that of the unitary group.

Random matrix theory has also led to conjectures about the growth of moments of the zeta function on the critical line. In particular, Jonathan Keating and Nina Snaith used averages over random unitary matrices to predict the main constants in asymptotic moment formulas such as ${\frac {1}{T}}\int _{0}^{T}|\zeta (1/2+it)|^{2k}\,dt$ as $T\to \infty$ . Their conjectures separate a universal random-matrix factor from an arithmetic Euler product factor, and have influenced later work on moments and ratios of L-functions.

Random matrix theory and quantum chaos are thus heuristic framework surrounding the Riemann hypothesis, even though no proof of the hypothesis is known from this approach.


## Arguments for and against the Riemann hypothesis

Mathematical papers about the Riemann hypothesis tend to be cautiously noncommittal about its truth. Of authors who express an opinion, most of them, such as Riemann (1859) and Bombieri (2000), imply that they expect (or at least hope) that it is true. The few authors who express serious doubt about it include Ivić (2008), who lists some reasons for skepticism, and Littlewood (1962), who flatly states that he believes it false, that there is no evidence for it and no imaginable reason it would be true. The consensus of the survey articles (Bombieri 2000, Conrey 2003, and Sarnak 2005) is that the evidence for it is strong but not overwhelming, so that while it is probably true there is reasonable doubt.

Some of the arguments for and against the Riemann hypothesis are listed by Conrey (2003), Sarnak (2005), and Ivić (2008), and include the following:

- Several analogues of the Riemann hypothesis have already been proved. The proof of the Riemann hypothesis for varieties over finite fields by Deligne (1974) is possibly the single strongest theoretical reason in favor of the Riemann hypothesis. This provides some evidence for the more general conjecture that all zeta functions associated with automorphic forms satisfy a Riemann hypothesis, which includes the classical Riemann hypothesis as a special case. Similarly Selberg zeta functions satisfy the analogue of the Riemann hypothesis, and are in some ways similar to the Riemann zeta function, having a functional equation and an infinite product expansion analogous to the Euler product expansion. But there are also some major differences; for example, they are not given by Dirichlet series. The Riemann hypothesis for the Goss zeta function was proved by Sheats (1998). In contrast to these positive examples, some Epstein zeta functions do not satisfy the Riemann hypothesis even though they have an infinite number of zeros on the critical line. These functions are quite similar to the Riemann zeta function, and have a Dirichlet series expansion and a functional equation, but the ones known to fail the Riemann hypothesis do not have an Euler product and are not directly related to automorphic representations.
- At first, the numerical verification that many zeros lie on the line seems strong evidence for it. But analytic number theory has had many conjectures supported by substantial numerical evidence that turned out to be false. See Skewes number for a notorious example, where the first exception to a plausible conjecture related to the Riemann hypothesis probably occurs around 10316; a counterexample to the Riemann hypothesis with imaginary part this size would be far beyond anything that can currently be computed using a direct approach. The problem is that the behavior is often influenced by very slowly increasing functions such as log log *T*, that tend to infinity, but do so so slowly that this cannot be detected by computation. Such functions occur in the theory of the zeta function controlling the behavior of its zeros; for example the function *S*(*T*) above has average size around (log log *T*)1/2. As *S*(*T*) jumps by at least 2 at any counterexample to the Riemann hypothesis, one might expect any counterexamples to the Riemann hypothesis to start appearing only when *S*(*T*) becomes large. It is never much more than 3 as far as it has been calculated, but is known to be unbounded, suggesting that calculations may not have yet reached the region of typical behavior of the zeta function.
- Denjoy's probabilistic argument for the Riemann hypothesis is based on the observation that if *μ*(*x*) is a random sequence of "1"s and "−1"s then, for every *ε* > 0, the partial sums $M(x)=\sum _{n\leq x}\mu (n)$ (the values of which are positions in a simple random walk) satisfy the bound $M(x)=O(x^{1/2+\varepsilon })$ with probability 1. The Riemann hypothesis is equivalent to this bound for the Möbius function μ and the Mertens function *M* derived in the same way from it. In other words, the Riemann hypothesis is in some sense equivalent to saying that *μ*(*x*) behaves like a random sequence of coin tosses. When *μ*(*x*) is nonzero its sign gives the parity of the number of prime factors of *x*, so informally the Riemann hypothesis says that the parity of the number of prime factors of an integer behaves randomly. Such probabilistic arguments in number theory often give the right answer, but tend to be very hard to make rigorous, and occasionally give the wrong answer for some results, such as Maier's theorem.
- The calculations in Odlyzko (1987) show that the zeros of the zeta function behave very much like the eigenvalues of a random Hermitian matrix, suggesting that they are the eigenvalues of some self-adjoint operator, which would imply the Riemann hypothesis. All attempts to find such an operator have failed.
- There are several theorems, such as Goldbach's weak conjecture for sufficiently large odd numbers, that were first proved using the generalized Riemann hypothesis, and later shown to be true unconditionally. This could be considered as weak evidence for the generalized Riemann hypothesis, as several of its "predictions" are true.
- Lehmer's phenomenon, where two zeros are sometimes very close, is sometimes given as a reason to disbelieve the Riemann hypothesis. But one would expect this to happen occasionally by chance even if the Riemann hypothesis is true, and Odlyzko's calculations suggest that nearby pairs of zeros occur just as often as predicted by Montgomery's conjecture.
- Patterson suggests that the most compelling reason for the Riemann hypothesis for most mathematicians is the hope that primes are distributed as regularly as possible.
