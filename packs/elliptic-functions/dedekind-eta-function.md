---
title: "Dedekind eta function"
source: https://en.wikipedia.org/wiki/Dedekind_eta_function
domain: elliptic-functions
license: CC-BY-SA-4.0
tags: elliptic function, jacobi elliptic functions, weierstrass elliptic function, theta function
fetched: 2026-07-02
---

# Dedekind eta function

In mathematics, the **Dedekind eta function**, named after Richard Dedekind, is a modular form of weight 1/2 and is a function defined on the upper half-plane of complex numbers, where the imaginary part is positive. It also occurs in bosonic string theory.

## Definition

For any complex number τ with Im(*τ*) > 0, let *q* = *e*2*πiτ*; then the eta function is defined by,

$\eta (\tau )=e^{\frac {\pi i\tau }{12}}\prod _{n=1}^{\infty }\left(1-e^{2n\pi i\tau }\right)=q^{\frac {1}{24}}\prod _{n=1}^{\infty }\left(1-q^{n}\right).$

Raising the eta equation to the 24th power and multiplying by (2*π*)12 gives

$\Delta (\tau )=(2\pi )^{12}\eta ^{24}(\tau )$

where Δ is the modular discriminant. The presence of 24 can be understood by connection with other occurrences, such as in the 24-dimensional Leech lattice.

The eta function is holomorphic on the upper half-plane but cannot be continued analytically beyond it.

The eta function satisfies the functional equations

${\begin{aligned}\eta (\tau +1)&=e^{\frac {\pi i}{12}}\eta (\tau ),\\\eta \left(-{\frac {1}{\tau }}\right)&={\sqrt {-i\tau }}\,\eta (\tau ).\,\end{aligned}}$

In the second equation the branch of the square root is chosen such that √−*iτ* = 1 when *τ* = *i*.

More generally, suppose *a*, *b*, *c*, *d* are integers with *ad* − *bc* = 1, so that

$\tau \mapsto {\frac {a\tau +b}{c\tau +d}}$

is a transformation belonging to the modular group. We may assume that either *c* > 0, or *c* = 0 and *d* = 1. Then

$\eta \left({\frac {a\tau +b}{c\tau +d}}\right)=\epsilon (a,b,c,d)\left(c\tau +d\right)^{\frac {1}{2}}\eta (\tau ),$

where

$\epsilon (a,b,c,d)={\begin{cases}e^{\frac {bi\pi }{12}}&c=0,\,d=1,\\e^{i\pi \left({\frac {a+d}{12c}}-s(d,c)-{\frac {1}{4}}\right)}&c>0.\end{cases}}$

Here *s*(*h*,*k*) is the Dedekind sum

$s(h,k)=\sum _{n=1}^{k-1}{\frac {n}{k}}\left({\frac {hn}{k}}-\left\lfloor {\frac {hn}{k}}\right\rfloor -{\frac {1}{2}}\right).$

Because of these functional equations the eta function is a modular form of weight ⁠1/2⁠ and level 1 for a certain character of order 24 of the metaplectic double cover of the modular group, and can be used to define other modular forms. In particular the modular discriminant of the Weierstrass elliptic function with

$\omega _{2}=\tau \omega _{1}$

can be defined as

$\Delta (\tau )=(2\pi \omega _{1})^{12}\eta (\tau )^{24}\,$

and is a modular form of weight 12. Some authors omit the factor of (2*π*)12, so that the series expansion has integral coefficients.

The Jacobi triple product implies that the eta is (up to a factor) a Jacobi theta function for special values of the arguments:

$\eta (\tau )=\sum _{n=1}^{\infty }\chi (n)\exp \left({\frac {\pi in^{2}\tau }{12}}\right),$

where *χ*(*n*) is "the" Dirichlet character modulo 12 with *χ*(±1) = 1 and *χ*(±5) = −1. Explicitly,

$\eta (\tau )=e^{\frac {\pi i\tau }{12}}\vartheta \left({\frac {\tau +1}{2}};3\tau \right).$

The Euler function

${\begin{aligned}\phi (q)&=\prod _{n=1}^{\infty }\left(1-q^{n}\right)\\&=q^{-{\frac {1}{24}}}\eta (\tau ),\end{aligned}}$

has a power series by the Euler Pentagonal number theorem:

$\phi (q)=\sum _{n=-\infty }^{\infty }(-1)^{n}q^{\frac {3n^{2}-n}{2}}.$

Note that by using this theorem for ${\mathfrak {I}}(\tau )>0$ , the eta function can be expressed as

$\eta (\tau )=\sum _{n=-\infty }^{\infty }e^{\pi in}e^{3\pi i\left(n-{\frac {1}{6}}\right)^{2}\tau }.$

This can be proved by using $x=2\pi i\tau$ in Euler Pentagonal number theorem with the definition of eta function.

Another way to see the Eta function is through the following limit

$\lim _{z\to 0}{\frac {\vartheta _{1}(z|\tau )}{z}}=2\pi \eta ^{3}(\tau )$

Which alternatively is:

$\sum _{n=0}^{\infty }(-1)^{n}(2n+1)q^{\frac {(2n+1)^{2}}{8}}=\eta ^{3}(\tau )$

Where $\vartheta _{1}(z|\tau )$ is the Jacobi Theta function and $\vartheta _{1}(z|\tau )=-\vartheta _{11}(z;\tau )$

Because the eta function is easy to compute numerically from either power series, it is often helpful in computation to express other functions in terms of it when possible, and products and quotients of eta functions, called eta quotients, can be used to express a great variety of modular forms.

The picture on this page shows the modulus of the Euler function: the additional factor of *q*⁠1/24⁠ between this and eta makes almost no visual difference whatsoever. Thus, this picture can be taken as a picture of eta as a function of q.

## Combinatorial identities

The theory of the algebraic characters of the affine Lie algebras gives rise to a large class of previously unknown identities for the eta function. These identities follow from the Weyl–Kac character formula, and more specifically from the so-called "denominator identities". The characters themselves allow the construction of generalizations of the Jacobi theta function which transform under the modular group; this is what leads to the identities. An example of one such new identity is

$\eta (8\tau )\eta (16\tau )=\sum _{m,n\in \mathbb {Z} \atop m\leq |3n|}(-1)^{m}q^{(2m+1)^{2}-32n^{2}}$

where *q* = *e*2*πiτ* is the q-analog or "deformation" of the highest weight of a module.

## Special values

From the above connection with the Euler function together with the special values of the latter, it can be easily deduced that

${\begin{aligned}\eta (i)&={\frac {\Gamma \left({\frac {1}{4}}\right)}{2\pi ^{\frac {3}{4}}}}\\[6pt]\eta \left({\tfrac {1}{2}}i\right)&={\frac {\Gamma \left({\frac {1}{4}}\right)}{2^{\frac {7}{8}}\pi ^{\frac {3}{4}}}}\\[6pt]\eta (2i)&={\frac {\Gamma \left({\frac {1}{4}}\right)}{2^{\frac {11}{8}}\pi ^{\frac {3}{4}}}}\\[6pt]\eta (3i)&={\frac {\Gamma \left({\frac {1}{4}}\right)}{2{\sqrt[{3}]{3}}\left(3+2{\sqrt {3}}\right)^{\frac {1}{12}}\pi ^{\frac {3}{4}}}}\\[6pt]\eta (4i)&={\frac {{\sqrt[{4}]{-1+{\sqrt {2}}}}\,\Gamma \left({\frac {1}{4}}\right)}{2^{\frac {29}{16}}\pi ^{\frac {3}{4}}}}\\[6pt]\eta \left(e^{\frac {2\pi i}{3}}\right)&=e^{-{\frac {\pi i}{24}}}{\frac {{\sqrt[{8}]{3}}\,\Gamma \left({\frac {1}{3}}\right)^{\frac {3}{2}}}{2\pi }}\end{aligned}}$

## Eta quotients

Eta quotients are defined by quotients of the form

$\prod _{0<d\mid N}\eta (d\tau )^{r_{d}}$

where d is a non-negative integer and rd is any integer. Linear combinations of eta quotients at imaginary quadratic arguments may be algebraic, while combinations of eta quotients may even be integral. For example, define,

${\begin{aligned}j(\tau )&=\left(\left({\frac {\eta (\tau )}{\eta (2\tau )}}\right)^{8}+2^{8}\left({\frac {\eta (2\tau )}{\eta (\tau )}}\right)^{16}\right)^{3}\\[6pt]j_{2A}(\tau )&=\left(\left({\frac {\eta (\tau )}{\eta (2\tau )}}\right)^{12}+2^{6}\left({\frac {\eta (2\tau )}{\eta (\tau )}}\right)^{12}\right)^{2}\\[6pt]j_{3A}(\tau )&=\left(\left({\frac {\eta (\tau )}{\eta (3\tau )}}\right)^{6}+3^{3}\left({\frac {\eta (3\tau )}{\eta (\tau )}}\right)^{6}\right)^{2}\\[6pt]j_{4A}(\tau )&=\left(\left({\frac {\eta (\tau )}{\eta (4\tau )}}\right)^{4}+4^{2}\left({\frac {\eta (4\tau )}{\eta (\tau )}}\right)^{4}\right)^{2}=\left({\frac {\eta ^{2}(2\tau )}{\eta (\tau )\,\eta (4\tau )}}\right)^{24}\end{aligned}}$

with the 24th power of the Weber modular function 𝔣(*τ*). Then,

${\begin{aligned}j\left({\frac {1+{\sqrt {-163}}}{2}}\right)&=-640320^{3},&e^{\pi {\sqrt {163}}}&\approx 640320^{3}+743.99999999999925\dots \\[6pt]j_{2A}\left({\frac {\sqrt {-58}}{2}}\right)&=396^{4},&e^{\pi {\sqrt {58}}}&\approx 396^{4}-104.00000017\dots \\[6pt]j_{3A}\left({\frac {1+{\sqrt {-{\frac {89}{3}}}}}{2}}\right)&=-300^{3},&e^{\pi {\sqrt {\frac {89}{3}}}}&\approx 300^{3}+41.999971\dots \\[6pt]j_{4A}\left({\frac {\sqrt {-7}}{2}}\right)&=2^{12},&e^{\pi {\sqrt {7}}}&\approx 2^{12}-24.06\dots \end{aligned}}$

and so on, values which appear in Ramanujan–Sato series.

Eta quotients may also be a useful tool for describing bases of modular forms, which are difficult to compute and express directly. In 1959 Morris Newman proved that if an eta quotient ηg of the form given above, namely $\prod _{0<d\mid N}\eta (d\tau )^{r_{d}}$ satisfies

$\sum _{0<d\mid N}dr_{d}\equiv 0{\pmod {24}}\quad {\text{and}}\quad \sum _{0<d\mid N}{\frac {N}{d}}r_{d}\equiv 0{\pmod {24}},$

then ηg is a weight k modular form for the congruence subgroup Γ0(*N*) (up to holomorphicity) where

$k={\frac {1}{2}}\sum _{0<d\mid N}r_{d}.$

This result was extended in 2019 such that the converse holds for cases when N is coprime to 6, and it remains open that the original theorem is sharp for all integers N. This also extends to state that any modular eta quotient for any level n congruence subgroup must also be a modular form for the group Γ(*N*). While these theorems characterize modular eta quotients, the condition of holomorphicity must be checked separately using a theorem that emerged from the work of Gérard Ligozat and Yves Martin:

If ηg is an eta quotient satisfying the above conditions for the integer N and c and d are coprime integers, then the order of vanishing at the cusp ⁠*c*/*d*⁠ relative to Γ0(*N*) is

${\frac {N}{24}}\sum _{0<\delta |N}{\frac {\gcd \left(d,\delta \right)^{2}r_{\delta }}{\gcd \left(d,{\frac {N}{d}}\right)d\delta }}.$

These theorems provide an effective means of creating holomorphic modular eta quotients, however this may not be sufficient to construct a basis for a vector space of modular forms and cusp forms. A useful theorem for limiting the number of modular eta quotients to consider states that a holomorphic weight k modular eta quotient on Γ0(*N*) must satisfy

$\sum _{0<d\mid N}|r_{d}|\leq \prod _{p\mid N}\left({\frac {p+1}{p-1}}\right)^{\min {\bigl (}2,{\text{ord}}_{p}(N){\bigr )}},$

where ord*p*(*N*) denotes the largest integer m such that pm divides N. These results lead to several characterizations of spaces of modular forms that can be spanned by modular eta quotients. Using the graded ring structure on the ring of modular forms, we can compute bases of vector spaces of modular forms composed of $\mathbb {C}$ -linear combinations of eta-quotients. For example, if we assume *N* = *pq* is a semiprime then the following process can be used to compute an eta-quotient basis of *Mk*(Γ0(*N*)).

1. Fix a semiprime *N* = *pq* which is coprime to 6 (that is, *p*, *q* > 3). We know that any modular eta quotient may be found using the above theorems, therefore it is reasonable to algorithmically to compute them.
2. Compute the dimension D of *Mk*(Γ0(*N*)). This tells us how many linearly-independent modular eta quotients we will need to compute to form a basis.
3. Reduce the number of eta quotients to consider. For semiprimes we can reduce the number of partitions using the bound on $\sum _{0<d\mid N}|r_{d}|$ and by noticing that the sum of the orders of vanishing at the cusps of Γ0(*N*) must equal $S:={\frac {(p+1)(q+1)}{6}}$ .
4. Find all partitions of S into 4-tuples (there are 4 cusps of Γ0(*N*)), and among these consider only the partitions which satisfy Newman's conditions (we can convert orders of vanishing into exponents). Each of these partitions corresponds to a unique eta quotient.
5. Determine the minimum number of terms in the q-expansion of each eta quotient required to identify elements uniquely (this uses a result known as Sturm's bound). Then use linear algebra to determine a maximal independent set among these eta quotients.
6. Assuming that we have not already found D linearly independent eta quotients, find an appropriate vector space *M**k*′(Γ0(*N*)) such that *k*′ and *M**k*′(Γ0(*N*)) is spanned by (weakly holomorphic) eta quotients, and *M**k*′−*k*(Γ0(*N*)) contains an eta quotient ηg.
7. Take a modular form f with weight k that is not in the span of our computed eta quotients, and compute *f* *ηg* as a linear combination of eta-quotients in *M**k*′(Γ0(*N*)) and then divide out by ηg. The result will be an expression of f as a linear combination of eta quotients as desired. Repeat this until a basis is formed.

A collection of over 6300 product identities for the Dedekind eta function in a canonical, standardized form is available at the Wayback machine of Michael Somos' website.
