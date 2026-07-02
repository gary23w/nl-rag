---
title: "Harmonic series (mathematics)"
source: https://en.wikipedia.org/wiki/Harmonic_sum
domain: mellin-transform
license: CC-BY-SA-4.0
tags: mellin transform, mellin inversion theorem, dirichlet series, harmonic sum
fetched: 2026-07-02
---

# Harmonic series (mathematics)

(Redirected from

Harmonic sum

)

In mathematics, the **harmonic series** is the infinite series formed by summing all positive unit fractions: $\sum _{i=1}^{\infty }{\frac {1}{i}}=1+{\frac {1}{2}}+{\frac {1}{3}}+{\frac {1}{4}}+{\frac {1}{5}}+\cdots .$

The first n terms of the series sum to approximately $\ln n+\gamma$ , where $\ln$ is the natural logarithm and $\gamma \approx 0.577$ is the Euler–Mascheroni constant. Because the logarithm has arbitrarily large values, the harmonic series does not have a finite limit: it is a divergent series. Its divergence was proven in the 14th century by Nicole Oresme using a precursor to the Cauchy condensation test for the convergence of infinite series. It can also be proven to diverge by comparing the sum to an integral, according to the integral test for convergence.

Applications of the harmonic series and its partial sums include Euler's proof that there are infinitely many prime numbers, the analysis of the coupon collector's problem on how many random trials are needed to provide a complete range of responses, the connected components of random graphs, the block-stacking problem on how far over the edge of a table a stack of blocks can be cantilevered, and the average case analysis of the quicksort algorithm.

## History

The name of the harmonic series derives from the concept of overtones or harmonics in music: the wavelengths of the overtones of a vibrating string are ${\tfrac {1}{2}}$ , ${\tfrac {1}{3}}$ , ${\tfrac {1}{4}}$ , etc., of the string's fundamental wavelength. Every term of the harmonic series after the first is the harmonic mean of the neighboring terms, so the terms form a harmonic progression; the phrases *harmonic mean* and *harmonic progression* likewise derive from music. Beyond music, harmonic sequences have also had a certain popularity with architects. This was so particularly in the Baroque period, when architects used them to establish the proportions of floor plans, of elevations, and to establish harmonic relationships between both interior and exterior architectural details of churches and palaces.

The divergence of the harmonic series was first proven in 1350 by Nicole Oresme. Oresme's work, and the contemporaneous work of Richard Swineshead on a different series, marked the first appearance of infinite series other than the geometric series in mathematics. However, this achievement fell into obscurity. Additional proofs were published in the 17th century by Pietro Mengoli and by Jacob Bernoulli. Bernoulli credited his brother Johann Bernoulli for finding the proof, and it was later included in Johann Bernoulli's collected works.

The partial sums of the harmonic series were named harmonic numbers, and given their usual notation $H_{n}$ , in 1968 by Donald Knuth.

## Definition and divergence

The harmonic series is the infinite series $\sum _{n=1}^{\infty }{\frac {1}{n}}=1+{\frac {1}{2}}+{\frac {1}{3}}+{\frac {1}{4}}+{\frac {1}{5}}+\cdots$ in which the terms are all of the positive unit fractions. It is a divergent series: as more terms of the series are included in partial sums of the series, the values of these partial sums grow arbitrarily large, beyond any finite limit. Because it is a divergent series, it should be interpreted as a formal sum, an abstract mathematical expression combining the unit fractions, rather than as something that can be evaluated to a numeric value. There are many different proofs of the divergence of the harmonic series, surveyed in a 2006 paper by S. J. Kifowit and T. A. Stamps. Two of the best-known are listed below.

### Comparison test

One way to prove divergence is to compare the harmonic series with another divergent series, where each denominator is replaced with the next-largest power of two: ${\begin{alignedat}{8}1&+{\frac {1}{2}}&&+{\frac {1}{3}}&&+{\frac {1}{4}}&&+{\frac {1}{5}}&&+{\frac {1}{6}}&&+{\frac {1}{7}}&&+{\frac {1}{8}}&&+{\frac {1}{9}}&&+\cdots \\[5pt]{}\geq 1&+{\frac {1}{2}}&&+{\frac {1}{\color {red}{\mathbf {4} }}}&&+{\frac {1}{4}}&&+{\frac {1}{\color {red}{\mathbf {8} }}}&&+{\frac {1}{\color {red}{\mathbf {8} }}}&&+{\frac {1}{\color {red}{\mathbf {8} }}}&&+{\frac {1}{8}}&&+{\frac {1}{\color {red}{\mathbf {16} }}}&&+\cdots \\[5pt]\end{alignedat}}$ Grouping equal terms shows that the second series diverges (because every grouping of convergent series is only convergent): ${\begin{aligned}&1+\left({\frac {1}{2}}\right)+\left({\frac {1}{4}}+{\frac {1}{4}}\right)+\left({\frac {1}{8}}+{\frac {1}{8}}+{\frac {1}{8}}+{\frac {1}{8}}\right)+\left({\frac {1}{16}}+\cdots +{\frac {1}{16}}\right)+\cdots \\[5pt]{}={}&1+{\frac {1}{2}}+{\frac {1}{2}}+{\frac {1}{2}}+{\frac {1}{2}}+\cdots .\end{aligned}}$ Because each term of the harmonic series is greater than or equal to the corresponding term of the second series (and the terms are all positive), and since the second series diverges, it follows (by the comparison test) that the harmonic series diverges as well. The same argument proves more strongly that, for every positive integer k , $\sum _{n=1}^{2^{k}}{\frac {1}{n}}\geq 1+{\frac {k}{2}}$ This is the original proof given by Nicole Oresme in around 1350. The Cauchy condensation test is a generalization of this argument.

### Integral test

It is possible to prove that the harmonic series diverges by comparing its sum with an improper integral. Specifically, consider the arrangement of rectangles shown in the figure to the right. Each rectangle is 1 unit wide and ${\tfrac {1}{n}}$ units high, so if the harmonic series converged then the total area of the rectangles would be the sum of the harmonic series. The curve $y={\tfrac {1}{x}}$ stays entirely below the upper boundary of the rectangles, so the area under the curve (in the range of x from one to infinity that is covered by rectangles) would be less than the area of the union of the rectangles. However, the area under the curve is given by a divergent improper integral, $\int _{1}^{\infty }{\frac {1}{x}}\,dx=\infty .$ Because this integral does not converge, the sum cannot converge either.

In the figure to the right, shifting each rectangle to the left by 1 unit, would produce a sequence of rectangles whose boundary lies below the curve rather than above it. This shows that the partial sums of the harmonic series differ from the integral by an amount that is bounded above and below by the unit area of the first rectangle: $\int _{1}^{N+1}{\frac {1}{x}}\,dx<\sum _{i=1}^{N}{\frac {1}{i}}<\int _{1}^{N}{\frac {1}{x}}\,dx+1.$ Generalizing this argument, any infinite sum of values of a monotone decreasing positive function of n (like the harmonic series) has partial sums that are within a bounded distance of the values of the corresponding integrals. Therefore, the sum converges if and only if the integral over the same range of the same function converges. When this equivalence is used to check the convergence of a sum by replacing it with an easier integral, it is known as the integral test for convergence.

## Partial sums

| n | Partial sum of the harmonic series, $H_{n}$ |   |   |   |
|---|---|---|---|---|
| expressed as a fraction | decimal | relative size |   |   |
| 1 | 1 | ~1 |   |   |
| 2 | 3 | /2 | 1.5 |   |
| 3 | 11 | /6 | ~1.83333 |   |
| 4 | 25 | /12 | ~2.08333 |   |
| 5 | 137 | /60 | ~2.28333 |   |
| 6 | 49 | /20 | 2.45 |   |
| 7 | 363 | /140 | ~2.59286 |   |
| 8 | 761 | /280 | ~2.71786 |   |
| 9 | 7129 | /2520 | ~2.82897 |   |
| 10 | 7381 | /2520 | ~2.92897 |   |
| 11 | 83711 | /27720 | ~3.01988 |   |
| 12 | 86021 | /27720 | ~3.10321 |   |
| 13 | 1145993 | /360360 | ~3.18013 |   |
| 14 | 1171733 | /360360 | ~3.25156 |   |
| 15 | 1195757 | /360360 | ~3.31823 |   |
| 16 | 2436559 | /720720 | ~3.38073 |   |
| 17 | 42142223 | /12252240 | ~3.43955 |   |
| 18 | 14274301 | /4084080 | ~3.49511 |   |
| 19 | 275295799 | /77597520 | ~3.54774 |   |
| 20 | 55835135 | /15519504 | ~3.59774 |   |

Adding the first n terms of the harmonic series produces a partial sum, called a harmonic number and denoted $H_{n}$ : $H_{n}=\sum _{k=1}^{n}{\frac {1}{k}}.$

### Growth rate

These numbers grow very slowly, with logarithmic growth, as can be seen from the integral test. More precisely, by the Euler–Maclaurin formula, $H_{n}=\ln n+\gamma +{\frac {1}{2n}}-\varepsilon _{n}$ where $\gamma \approx 0.5772$ is the Euler–Mascheroni constant and $0\leq \varepsilon _{n}\leq 1/(8n^{2})$ which approaches 0 as n goes to infinity.

### Divisibility

No harmonic numbers are integers except for $H_{1}=1$ . One way to prove that $H_{n}$ is not an integer is to consider the highest power of two $2^{k}$ in the range from 1 to n . If M is the least common multiple of the numbers from 1 to n , then $H_{k}$ can be rewritten as a sum of fractions with equal denominators $H_{n}=\sum _{i=1}^{n}{\tfrac {M/i}{M}}$ in which only one of the numerators, $M/2^{k}$ , is odd and the rest are even, and (when $n>1$ ) M is itself even. Therefore, the result is a fraction with an odd numerator and an even denominator, which cannot be an integer. More generally, any sequence of consecutive integers has a unique member divisible by a greater power of two than all the other sequence members, from which it follows by the same argument that no two harmonic numbers differ by an integer.

Another proof that the harmonic numbers are not integers observes that the denominator of $H_{n}$ must be divisible by all prime numbers greater than $n/2$ and less than or equal to n , and uses Bertrand's postulate to prove that this set of primes is non-empty. The same argument implies more strongly that, except for $H_{1}=1$ , $H_{2}=1.5$ , and $H_{6}=2.45$ , no harmonic number can have a terminating decimal representation. It has been conjectured that every prime number divides the numerators of only a finite subset of the harmonic numbers, but this remains unproven.

### Interpolation

The digamma function is defined as the logarithmic derivative of the gamma function $\psi (x)={\frac {d}{dx}}\ln {\big (}\Gamma (x){\big )}={\frac {\Gamma '(x)}{\Gamma (x)}}.$ Just as the gamma function provides a continuous interpolation of the factorials, the digamma function provides a continuous interpolation of the harmonic numbers, in the sense that $\psi (n)=H_{n-1}-\gamma$ . This equation can be used to extend the definition to harmonic numbers with rational indices.

### Ramanujan summation

Although the harmonic series is divergent, its Ramanujan summation has the Euler–Mascheroni constant ⁠ $\gamma$ ⁠ as its finite value: $\textstyle \sum _{n\geq 1}^{\mathfrak {R}}{\frac {1}{n}}=\gamma .$

## Applications

Many well-known mathematical problems have solutions involving the harmonic series and its partial sums.

### Crossing a desert

The jeep problem or desert-crossing problem is included in a 9th-century problem collection by Alcuin, *Propositiones ad Acuendos Juvenes* (formulated in terms of camels rather than jeeps), but with an incorrect solution. The problem asks how far into the desert a jeep can travel and return, starting from a base with n loads of fuel, by carrying some of the fuel into the desert and leaving it in depots. The optimal solution involves placing depots spaced at distances ${\tfrac {r}{2n}},{\tfrac {r}{2(n-1)}},{\tfrac {r}{2(n-2)}},\dots$ from the starting point and each other, where r is the range of distance that the jeep can travel with a single load of fuel. On each trip out and back from the base, the jeep places one more depot, refueling at the other depots along the way, and placing as much fuel as it can in the newly placed depot while still leaving enough for itself to return to the previous depots and the base. Therefore, the total distance reached on the n th trip is ${\frac {r}{2n}}+{\frac {r}{2(n-1)}}+{\frac {r}{2(n-2)}}+\cdots ={\frac {r}{2}}H_{n},$ where $H_{n}$ is the n th harmonic number. The divergence of the harmonic series implies that crossings of any length are possible with enough fuel.

For instance, for Alcuin's version of the problem, $r=30$ : a camel can carry 30 measures of grain and can travel one leuca while eating a single measure, where a leuca is a unit of distance roughly equal to 2.3 kilometres (1.4 mi). The problem has $n=3$ : there are 90 measures of grain, enough to supply three trips. For the standard formulation of the desert-crossing problem, it would be possible for the camel to travel ${\tfrac {30}{2}}{\bigl (}{\tfrac {1}{3}}+{\tfrac {1}{2}}+{\tfrac {1}{1}})=27.5$ leucas and return, by placing a grain storage depot 5 leucas from the base on the first trip and 12.5 leucas from the base on the second trip. However, Alcuin instead asks how much grain can be transported a distance of 30 leucas without a final return trip, either stranding some camels in the desert or failing to account for the amount of grain consumed by camels on their return trips.

### Stacking blocks

In the block-stacking problem, one must place a pile of n identical rectangular blocks, one per layer, so that they hang as far as possible over the edge of a table without falling. The top block can be placed with ${\tfrac {1}{2}}$ of its length extending beyond the next lower block. If it is placed in this way, the next block down needs to be placed with at most ${\tfrac {1}{2}}\cdot {\tfrac {1}{2}}$ of its length extending beyond the next lower block, so that the center of mass of the top two blocks is supported and they do not topple. The third block needs to be placed with at most ${\tfrac {1}{2}}\cdot {\tfrac {1}{3}}$ of its length extending beyond the next lower block, so that the center of mass of the top three blocks is supported and they do not topple, and so on. In this way, it is possible to place the n blocks in such a way that they extend ${\tfrac {1}{2}}H_{n}$ lengths beyond the table, where $H_{n}$ is the n th harmonic number. The divergence of the harmonic series implies that there is no limit on how far beyond the table the block stack can extend. For stacks with one block per layer, no better solution is possible, but significantly more overhang can be achieved using stacks with more than one block per layer.

### Counting primes and divisors

In 1737, Leonhard Euler observed that, as a formal sum, the harmonic series is equal to an Euler product in which each term comes from a prime number: $\sum _{i=1}^{\infty }{\frac {1}{i}}=\prod _{p\in \mathbb {P} }\left(1+{\frac {1}{p}}+{\frac {1}{p^{2}}}+\cdots \right)=\prod _{p\in \mathbb {P} }{\frac {1}{1-1/p}},$ where $\mathbb {P}$ denotes the set of prime numbers. The left equality comes from applying the distributive law to the product and recognizing the resulting terms as the prime factorizations of the terms in the harmonic series, and the right equality uses the standard formula for a geometric series. The product is divergent, just like the sum, but if it converged one could take logarithms and obtain $\ln \prod _{p\in \mathbb {P} }{\frac {1}{1-1/p}}=\sum _{p\in \mathbb {P} }\ln {\frac {1}{1-1/p}}=\sum _{p\in \mathbb {P} }\left({\frac {1}{p}}+{\frac {1}{2p^{2}}}+{\frac {1}{3p^{3}}}+\cdots \right)=\sum _{p\in \mathbb {P} }{\frac {1}{p}}+K.$ Here, each logarithm is replaced by its Taylor series, and the constant K on the right is the evaluation of the convergent series of terms with exponent greater than one. It follows from these manipulations that the sum of reciprocals of primes, on the right hand of this equality, must diverge, for if it converged these steps could be reversed to show that the harmonic series also converges, which it does not. An immediate corollary is that there are infinitely many prime numbers, because a finite sum cannot diverge. Although Euler's work is not considered adequately rigorous by the standards of modern mathematics, it can be made rigorous by taking more care with limits and error bounds. Euler's conclusion that the partial sums of reciprocals of primes grow as a double logarithm of the number of terms has been confirmed by later mathematicians as one of Mertens' theorems, and can be seen as a precursor to the prime number theorem.

Another problem in number theory closely related to the harmonic series concerns the average number of divisors of the numbers in a range from 1 to n , formalized as the average order of the divisor function, ${\frac {1}{n}}\sum _{i=1}^{n}\left\lfloor {\frac {n}{i}}\right\rfloor \leq {\frac {1}{n}}\sum _{i=1}^{n}{\frac {n}{i}}=H_{n}.$ The operation of rounding each term in the harmonic series to the next smaller integer multiple of ${\tfrac {1}{n}}$ causes this average to differ from the harmonic numbers by a small constant, and Peter Gustav Lejeune Dirichlet showed more precisely that the average number of divisors is $\ln n+2\gamma -1+O(1/{\sqrt {n}})$ (expressed in big O notation). Bounding the final error term more precisely remains an open problem, known as Dirichlet's divisor problem.

### Collecting coupons

Several common games or recreations involve repeating a random selection from a set of items until all possible choices have been selected; these include the collection of trading cards and the completion of parkrun bingo, in which the goal is to obtain all 60 possible numbers of seconds in the times from a sequence of running events. More serious applications of this problem include sampling all variations of a manufactured product for its quality control, and the connectivity of random graphs. In situations of this form, once there are k items remaining to be collected out of a total of n equally-likely items, the probability of collecting a new item in a single random choice is $k/n$ and the expected number of random choices needed until a new item is collected is $n/k$ . Summing over all values of k from n down to 1 shows that the total expected number of random choices needed to collect all items is $nH_{n}$ , where $H_{n}$ is the n th harmonic number.

### Analyzing algorithms

The quicksort algorithm for sorting a set of items can be analyzed using the harmonic numbers. The algorithm operates by choosing one item as a "pivot", comparing it to all the others, and recursively sorting the two subsets of items whose comparison places them before the pivot and after the pivot. In either its average-case complexity (with the assumption that all input permutations are equally likely) or in its expected time analysis of worst-case inputs with a random choice of pivot, all of the items are equally likely to be chosen as the pivot. For such cases, one can compute the probability that two items are ever compared with each other, throughout the recursion, as a function of the number of other items that separate them in the final sorted order. If items x and y are separated by k other items, then the algorithm will make a comparison between x and y only when, as the recursion progresses, it picks x or y as a pivot before picking any of the other k items between them. Because each of these $k+2$ items is equally likely to be chosen first, this happens with probability ${\tfrac {2}{k+2}}$ . The total expected number of comparisons, which controls the total running time of the algorithm, can then be calculated by summing these probabilities over all pairs, giving $\sum _{i=2}^{n}\sum _{k=0}^{i-2}{\frac {2}{k+2}}=\sum _{i=1}^{n-1}2H_{i}=O(n\log n).$ The divergence of the harmonic series corresponds in this application to the fact that, in the comparison model of sorting used for quicksort, it is not possible to sort in linear time.

### Alternating harmonic series

The series $\sum _{n=1}^{\infty }{\frac {(-1)^{n+1}}{n}}=1-{\frac {1}{2}}+{\frac {1}{3}}-{\frac {1}{4}}+{\frac {1}{5}}-\cdots$ is known as the **alternating harmonic series**. It is conditionally convergent by the alternating series test, but not absolutely convergent. Its sum is the natural logarithm of 2.

More precisely, the asymptotic expansion of the series begins as ${\frac {1}{1}}-{\frac {1}{2}}+\cdots +{\frac {1}{2n-1}}-{\frac {1}{2n}}=H_{2n}-H_{n}=\ln 2-{\frac {1}{4n}}+O(n^{-2}).$ This results from the equality ${\textstyle H_{n}=2\sum _{k=1}^{n}{\frac {1}{2k}}}$ and the Euler–Maclaurin formula.

Using alternating signs with only odd unit fractions produces a related series, the Leibniz formula for π $\sum _{n=0}^{\infty }{\frac {(-1)^{n}}{2n+1}}=1-{\frac {1}{3}}+{\frac {1}{5}}-{\frac {1}{7}}+\cdots ={\frac {\pi }{4}}.$

### Riemann zeta function

The Riemann zeta function is defined for real $x>1$ by the convergent series $\zeta (x)=\sum _{n=1}^{\infty }{\frac {1}{n^{x}}}={\frac {1}{1^{x}}}+{\frac {1}{2^{x}}}+{\frac {1}{3^{x}}}+\cdots ,$ which for $x=1$ would be the harmonic series. It can be extended by analytic continuation to a holomorphic function on all complex numbers except $x=1$ , where the extended function has a simple pole. Other important values of the zeta function include $\zeta (2)=\pi ^{2}/6$ , the solution to the Basel problem, Apéry's constant $\zeta (3)$ , proved by Roger Apéry to be an irrational number, and the "critical line" of complex numbers with real part ${\tfrac {1}{2}}$ , conjectured by the Riemann hypothesis to be the only values other than negative integers where the function can be zero.

### Random harmonic series

The random harmonic series is $\sum _{n=1}^{\infty }{\frac {s_{n}}{n}},$ where the values $s_{n}$ are independent and identically distributed random variables that take the two values $+1$ and $-1$ with equal probability ${\tfrac {1}{2}}$ . It converges with probability 1, as can be seen by using the Kolmogorov three-series theorem or of the closely related Kolmogorov maximal inequality. The sum of the series, which can be rearranged as an infinite sum of uniform variables on $[-{\tfrac {1}{2n+1}},{\tfrac {1}{2n+1}}]$ with probability 1, is a random variable whose probability density function is

${\begin{aligned}g(x)&={\frac {1}{\pi }}\int _{0}^{\infty }\cos(xt)\prod _{n=0}^{\infty }{\frac {\sin(2t/(2n+1))}{2t/(2n+1)}}dt\\&={\frac {1}{\pi }}\int _{0}^{\infty }\cos(xt)\prod _{n=1}^{\infty }\cos(t/n)dt.\end{aligned}}$

This function is close to ${\tfrac {1}{4}}$ for values between $-1$ and 1 , with the $g(0)\approx 0.2499943958$ to ten decimal places. It decreases asymptotically like a normal distribution for values greater than 3 or less than $-3$ . Intermediate between these ranges, at the values $\pm 2$ , the probability density is ${\tfrac {1}{8}}-\varepsilon$ for a nonzero but very small value $\varepsilon <10^{-42}$ .

### Depleted harmonic series

The depleted harmonic series where all of the terms in which the digit 9 appears anywhere in the denominator are removed can be shown to converge to the value 22.92067661926415034816.... In fact, when all the terms containing any particular string of digits (in any base) are removed, the series converges.
