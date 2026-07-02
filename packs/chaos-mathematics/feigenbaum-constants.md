---
title: "Feigenbaum constants"
source: https://en.wikipedia.org/wiki/Feigenbaum_constants
domain: chaos-mathematics
license: CC-BY-SA-4.0
tags: chaos theory, butterfly effect, lyapunov exponent, strange attractor
fetched: 2026-07-02
---

# Feigenbaum constants

In mathematics, specifically bifurcation theory, the **Feigenbaum constants** /ˈfaɪɡənbaʊm/ δ and α are two mathematical constants which both express ratios in a bifurcation diagram for a non-linear map. They are named after the physicist Mitchell J. Feigenbaum.

## History

Feigenbaum originally related the first constant to the period-doubling bifurcations in the logistic map, but also showed it to hold for all one-dimensional maps with a single quadratic maximum. As a consequence of this generality, every chaotic system that corresponds to this description will bifurcate at the same rate. Feigenbaum made this discovery in 1975, and he officially published it in 1978.

## The first constant

The **first Feigenbaum constant** or simply **Feigenbaum constant** δ is the limiting ratio of each bifurcation interval to the next between every period doubling, of a one-parameter map

$x_{i+1}=f(x_{i}),$

where *f* (*x*) is a function parameterized by the bifurcation parameter **a**.

It is given by the limit:

$\delta =\lim _{n\to \infty }{\frac {a_{n-1}-a_{n-2}}{a_{n}-a_{n-1}}}$

where an are discrete values of **a** at the nth period doubling.

This gives its numerical value (sequence A006890 in the OEIS):

$\delta =4.669\,201\,609\,102\,990\,671\,853\,203\,820\,466\ldots$

- A simple rational approximation is ⁠621/133⁠, which is correct to 5 significant values (when rounding). For more precision use ⁠1228/263⁠, which is correct to 7 significant values.
- It is approximately equal to ⁠10/π − 1⁠, with an error of 0.0047 %.

### Illustration

#### Non-linear maps

To see how this number arises, consider the real one-parameter map

$f(x)=a-x^{2}.$

Here a is the bifurcation parameter, x is the variable. The values of a for which the period doubles (e.g. the largest value for a with no period-2 orbit, or the largest a with no period-4 orbit), are *a*1, *a*2 etc. These are tabulated below:

| n | Period | Bifurcation parameter (an) | Ratio ⁠*a**n*−1 − *a**n*−2/*a**n* − *a**n*−1⁠ |
|---|---|---|---|
| 1 | 2 | 0.75 | — |
| 2 | 4 | 1.25 | — |
| 3 | 8 | 1.3680989 | 4.2337 |
| 4 | 16 | 1.3940462 | 4.5515 |
| 5 | 32 | 1.3996312 | 4.6458 |
| 6 | 64 | 1.4008286 | 4.6639 |
| 7 | 128 | 1.4010853 | 4.6682 |
| 8 | 256 | 1.4011402 | 4.6689 |

The ratio in the last column converges to the first Feigenbaum constant. The same number arises for the logistic map

$f(x)=ax(1-x)$

with real parameter a and variable x. Tabulating the bifurcation values again:

| n | Period | Bifurcation parameter (an) | Ratio ⁠*a**n*−1 − *a**n*−2/*a**n* − *a**n*−1⁠ |
|---|---|---|---|
| 1 | 2 | 3 | — |
| 2 | 4 | 3.4494897 | — |
| 3 | 8 | 3.5440903 | 4.7514 |
| 4 | 16 | 3.5644073 | 4.6562 |
| 5 | 32 | 3.5687594 | 4.6683 |
| 6 | 64 | 3.5696916 | 4.6686 |
| 7 | 128 | 3.5698913 | 4.6680 |
| 8 | 256 | 3.5699340 | 4.6768 |

#### Fractals

In the case of the Mandelbrot set for complex quadratic polynomial

$f(z)=z^{2}+c$

the Feigenbaum constant is the limiting ratio between the diameters of successive circles on the real axis in the complex plane (see animation on the rightabove).

| n | Period = 2*n* | Bifurcation parameter (cn) | Ratio $={\dfrac {c_{n-1}-c_{n-2}}{c_{n}-c_{n-1}}}$ |
|---|---|---|---|
| 1 | 2 | −0.75 | — |
| 2 | 4 | −1.25 | — |
| 3 | 8 | −1.3680989 | 4.2337 |
| 4 | 16 | −1.3940462 | 4.5515 |
| 5 | 32 | −1.3996312 | 4.6459 |
| 6 | 64 | −1.4008287 | 4.6639 |
| 7 | 128 | −1.4010853 | 4.6668 |
| 8 | 256 | −1.4011402 | 4.6740 |
| 9 | 512 | −1.401151982029 | 4.6596 |
| 10 | 1024 | −1.401154502237 | 4.6750 |
| ... | ... | ... | ... |
| ∞ |   | −1.4011551890... |   |

Bifurcation parameter is a root point of period-2*n* component. This series converges to **the Feigenbaum point** c = −1.401155...... The ratio in the last column converges to the first Feigenbaum constant.

Other maps also reproduce this ratio; in this sense the Feigenbaum constant in bifurcation theory is analogous to π in geometry and *e* in calculus.

## The second constant

The **second Feigenbaum constant** or **Feigenbaum reduction parameter** α is given by (sequence A006891 in the OEIS):

$\alpha =2.502\,907\,875\,095\,892\,822\,283\,902\,873\,218\ldots$

It is the ratio between the width of a tine and the width of one of its two subtines (except the tine closest to the fold). A negative sign is applied to α when the ratio between the lower subtine and the width of the tine is measured.

These numbers apply to a large class of dynamical systems (for example, dripping faucets to population growth).

A simple rational approximation is ⁠5/2⁠, which is correct to 2 significant values. For more precision, ⁠13/11⁠ × ⁠17/11⁠ × ⁠37/27⁠ = ⁠8177/3267⁠ is used, which is correct to 8 significant values.

## Properties

Both numbers are believed to be transcendental, although they have not been proven to be so. In fact, there is no known proof that either constant is even irrational.

The first proof of the universality of the Feigenbaum constants was carried out by Oscar Lanford—with computer-assistance—in 1982 (with a small correction by Jean-Pierre Eckmann and Peter Wittwer of the University of Geneva in 1987). Over the years, non-numerical methods were discovered for different parts of the proof, aiding Mikhail Lyubich in producing the first complete non-numerical proof.

## Other values

The period-3 window in the logistic map also has a period-tripling route to chaos (moving at each step to the period-3 subwindow), reaching chaos at $r=3.854077963591\dots$ , and it has its own two Feigenbaum constants: $\delta =55.26,\alpha =9.277$ . Similar results hold for the other isolated period-n windows in the chaotic region, yielding $\alpha$ and $\delta$ for each window. There is a universal relation between the two constants due to Eckmann, Epstein, and Wittwer, that ${\textstyle 3\delta \approx \alpha ^{2}}$ .
