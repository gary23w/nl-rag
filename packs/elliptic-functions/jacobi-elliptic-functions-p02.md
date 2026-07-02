---
title: "Jacobi elliptic functions (part 2/2)"
source: https://en.wikipedia.org/wiki/Jacobi_elliptic_functions
domain: elliptic-functions
license: CC-BY-SA-4.0
tags: elliptic function, jacobi elliptic functions, weierstrass elliptic function, theta function
fetched: 2026-07-02
part: 2/2
---

## Continued fractions

Assuming real numbers $a,p$ with $0<a<p$ and the nome $q=e^{\pi i\tau }$ , $\operatorname {Im} (\tau )>0$ with elliptic modulus ${\textstyle k(\tau )={\sqrt {1-k'(\tau )^{2}}}=(\vartheta _{10}(0;\tau )/\vartheta _{00}(0;\tau ))^{2}}$ . If $K[\tau ]=K(k(\tau ))$ , where $K(x)=\pi /2\cdot {}_{2}F_{1}(1/2,1/2;1;x^{2})$ is the complete elliptic integral of the first kind, then holds the following continued fraction expansion ${\begin{aligned}&{\frac {{\textrm {dn}}\left((p/2-a)\tau K\left[{\frac {p\tau }{2}}\right];k\left({\frac {p\tau }{2}}\right)\right)}{\sqrt {k'\left({\frac {p\tau }{2}}\right)}}}={\frac {\sum \limits _{n=-\infty }^{\infty }q^{p/2n^{2}+(p/2-a)n}}{\sum \limits _{n=-\infty }^{\infty }(-1)^{n}q^{p/2n^{2}+(p/2-a)n}}}\\[4pt]&=-1+{\cfrac {2}{1-{\cfrac {q^{a}+q^{p-a}}{1-q^{p}+{\cfrac {(q^{a}+q^{2p-a})(q^{a+p}+q^{p-a})}{1-q^{3p}+{\cfrac {q^{p}(q^{a}+q^{3p-a})(q^{a+2p}+q^{p-a})}{1-q^{5p}+{\cfrac {q^{2p}(q^{a}+q^{4p-a})(q^{a+3p}+q^{p-a})}{1-q^{7p}+\cdots }}}}}}}}}}\end{aligned}}$ Known continued fractions involving ${\textrm {sn}}(t),{\textrm {cn}}(t)$ and ${\textrm {dn}}(t)$ with elliptic modulus k are

For $z\in \mathbb {C}$ , $|k|<1$ : pg. 374 $\int _{0}^{\infty }{\textrm {sn}}(t)e^{-tz}\,\mathrm {d} t={\frac {1}{1^{2}(1+k^{2})+z^{2}-{}}}\,{\frac {1\cdot 2^{2}\cdot 3k^{2}}{3^{2}(1+k^{2})+z^{2}-{}}}\,{\frac {3\cdot 4^{2}\cdot 5k^{2}}{5^{2}(1+k^{2})+z^{2}-{}}}\cdots$

For $z\in \mathbb {C} \setminus \{0\}$ , $|k|<1$ : pg. 375 $\int _{0}^{\infty }{\textrm {sn}}^{2}(t)e^{-tz}\,\mathrm {d} t={\frac {2z^{-1}}{2^{2}(1+k^{2})+z^{2}-{}}}\,{\frac {2\cdot 3^{2}\cdot 4k^{2}}{4^{2}(1+k^{2})+z^{2}-{}}}\,{\frac {4\cdot 5^{2}\cdot 6k^{2}}{6^{2}(1+k^{2})+z^{2}-{}}}\cdots$

For $z\in \mathbb {C} \setminus \{0\}$ , $|k|<1$ : pg. 220 $\int _{0}^{\infty }{\textrm {cn}}(t)e^{-tz}\,\mathrm {d} t={\frac {1}{z+{}}}\,{\frac {1^{2}}{z+{}}}\,{\frac {2^{2}k^{2}}{z+{}}}\,{\frac {3^{2}}{z+{}}}\,{\frac {4^{2}k^{2}}{z+{}}}\,{\frac {5^{2}}{z+{}}}\cdots$

For $z\in \mathbb {C} \setminus \{0\}$ , $|k|<1$ : pg. 374 $\int _{0}^{\infty }{\textrm {dn}}(t)e^{-tz}\,\mathrm {d} t={\frac {1}{z+{}}}\,{\frac {1^{2}k^{2}}{z+{}}}\,{\frac {2^{2}}{z+{}}}\,{\frac {3^{2}k^{2}}{z+{}}}\,{\frac {4^{2}}{z+{}}}\,{\frac {5^{2}k^{2}}{z+{}}}\cdots$

For $z\in \mathbb {C}$ , $|k|<1$ : pg. 375 $\int _{0}^{\infty }{\frac {{\textrm {sn}}(t){\textrm {cn}}(t)}{{\textrm {dn}}(t)}}e^{-tz}\,\mathrm {d} t={\frac {1}{2\cdot 1^{2}(2-k^{2})+z^{2}-{}}}\,{\frac {1\cdot 2^{2}\cdot 3k^{4}}{2\cdot 3^{2}(2-k^{2})+z^{2}-{}}}\,{\frac {3\cdot 4^{2}\cdot 5k^{4}}{2\cdot 5^{2}(2-k^{2})+z^{2}-{}}}\cdots$


## Inverse functions

The inverses of the Jacobi elliptic functions can be defined similarly to the inverse trigonometric functions; if $x=\operatorname {sn} (\xi ,m)$ , $\xi =\operatorname {arcsn} (x,m)$ . They can be represented as elliptic integrals, and power series representations have been found.

- $\operatorname {arcsn} (x,m)=\int _{0}^{x}{\frac {\mathrm {d} t}{\sqrt {(1-t^{2})(1-mt^{2})}}}$
- $\operatorname {arccn} (x,m)=\int _{x}^{1}{\frac {\mathrm {d} t}{\sqrt {(1-t^{2})(1-m+mt^{2})}}}$
- $\operatorname {arcdn} (x,m)=\int _{x}^{1}{\frac {\mathrm {d} t}{\sqrt {(1-t^{2})(t^{2}+m-1)}}}$


## Map projection

The Peirce quincuncial projection is a map projection based on Jacobian elliptic functions.
