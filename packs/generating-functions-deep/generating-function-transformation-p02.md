---
title: "Generating function transformation (part 2/2)"
source: https://en.wikipedia.org/wiki/Generating_function_transformation
domain: generating-functions-deep
license: CC-BY-SA-4.0
tags: generating function, formal power series, umbral calculus, lagrange inversion theorem
fetched: 2026-07-02
part: 2/2
---

## Inversion relations and generating function identities

### Inversion relations

An *inversion relation* is a pair of equations of the form

$g_{n}=\sum _{k=0}^{n}A_{n,k}\cdot f_{k}\quad \longleftrightarrow \quad f_{n}=\sum _{k=0}^{n}B_{n,k}\cdot g_{k},$

which is equivalent to the *orthogonality relation*

$\sum _{k=j}^{n}A_{n,k}\cdot B_{k,j}=\delta _{n,j}.$

Given two sequences, $\{f_{n}\}$ and $\{g_{n}\}$ , related by an inverse relation of the previous form, we sometimes seek to relate the OGFs and EGFs of the pair of sequences by functional equations implied by the inversion relation. This goal in some respects mirrors the more number theoretic (Lambert series) generating function relation guaranteed by the Möbius inversion formula, which provides that whenever

$a_{n}=\sum _{d|n}b_{d}\quad \longleftrightarrow \quad b_{n}=\sum _{d|n}\mu \left({\frac {n}{d}}\right)a_{d},$

the generating functions for the sequences, $\{a_{n}\}$ and $\{b_{n}\}$ , are related by the *Möbius transform* given by

$\sum _{n\geq 1}a_{n}z^{n}=\sum _{n\geq 1}{\frac {b_{n}z^{n}}{1-z^{n}}}.$

Similarly, the *Euler transform* of generating functions for two sequences, $\{a_{n}\}$ and $\{b_{n}\}$ , satisfying the relation

$1+\sum _{n\geq 1}b_{n}z^{n}=\prod _{i\geq 1}{\frac {1}{(1-z^{i})^{a_{i}}}},$

is given in the form of

$1+B(z)=\exp \left(\sum _{k\geq 1}{\frac {A(z^{k})}{k}}\right),$

where the corresponding inversion formulas between the two sequences is given in the reference.

The remainder of the results and examples given in this section sketch some of the more well-known generating function transformations provided by sequences related by inversion formulas (the binomial transform and the Stirling transform), and provides several tables of known inversion relations of various types cited in Riordan's *Combinatorial Identities* book. In many cases, we omit the corresponding functional equations implied by the inversion relationships between two sequences (*this part of the article needs more work*).

### The binomial transform

The first inversion relation provided below implicit to the binomial transform is perhaps the simplest of all inversion relations we will consider in this section. For any two sequences, $\{f_{n}\}$ and $\{g_{n}\}$ , related by the inversion formulas

$g_{n}=\sum _{k=0}^{n}{\binom {n}{k}}(-1)^{k}f_{k}\quad \longleftrightarrow \quad f_{n}=\sum _{k=0}^{n}{\binom {n}{k}}(-1)^{k}g_{k},$

we have functional equations between the OGFs and EGFs of these sequences provided by the binomial transform in the forms of

$G(z)={\frac {1}{1-z}}F\left({\frac {-z}{1-z}}\right)$

and

${\widehat {G}}(z)=e^{z}{\widehat {F}}(-z).$

### The Stirling transform

For any pair of sequences, $\{f_{n}\}$ and $\{g_{n}\}$ , related by the Stirling number inversion formula

$g_{n}=\sum _{k=1}^{n}\left\{{\begin{matrix}n\\k\end{matrix}}\right\}f_{k}\quad \longleftrightarrow \quad f_{n}=\sum _{k=1}^{n}\left[{\begin{matrix}n\\k\end{matrix}}\right](-1)^{n-k}g_{k},$

these inversion relations between the two sequences translate into functional equations between the sequence EGFs given by the Stirling transform as

${\widehat {G}}(z)={\widehat {F}}\left(e^{z}-1\right)$

and

${\widehat {F}}(z)={\widehat {G}}\left(\log(1+z)\right).$

### Tables of inversion pairs from Riordan's book

These tables appear in chapters 2 and 3 in Riordan's book providing an introduction to inverse relations with many examples, though which does not stress functional equations between the generating functions of sequences related by these inversion relations. The interested reader is encouraged to pick up a copy of the original book for more details.

#### Several forms of the simplest inverse relations

| Relation | Formula | Inverse Formula | Generating Functions (OGF) | Generating Functions (EGF) | Notes / References |
|---|---|---|---|---|---|
| 1 | $a_{n}=\sum _{k=0}^{n}{\binom {n}{k}}b_{k}$ | $b_{n}=\sum _{k=0}^{n}{\binom {n}{k}}(-1)^{n-k}a_{k}$ | $B(z)={\frac {1}{1-z}}A\left(-{\frac {z}{1-z}}\right)$ | ${\widehat {B}}(z)=e^{z}{\widehat {A}}(-z)$ | See the Binomial transform |
| 2 | $a_{n}=\sum _{k=0}^{n}{\binom {p-k}{p-n}}b_{k}$ | $b_{n}=\sum _{k=0}^{n}{\binom {p-k}{p-n}}(-1)^{n-k}a_{k}$ | $\ast$ | $\ast$ |   |
| 3 | $a_{n}=\sum _{k=0}^{n}{\binom {n+p}{k+p}}b_{k}$ | $b_{n}=\sum _{k=0}^{n}{\binom {n+p}{k+p}}(-1)^{n-k}a_{k}$ | $B(z)={\frac {1}{(1+z)^{p+1}}}A\left({\frac {z}{1+z}}\right)$ | $\ast$ |   |
| 4 | $a_{n}=\sum _{k\geq n}{\binom {k+p}{n+p}}b_{k}$ | $b_{n}=\sum _{k\geq n}{\binom {k+p}{n+p}}(-1)^{n-k}a_{k}$ | $\ast$ | $\ast$ |   |
| 5 | $a_{n}=\sum _{k=1}^{n}{\frac {n!}{k!}}{\binom {n-1}{k-1}}b_{k}$ | $b_{n}=\sum _{k=1}^{n}{\frac {n!}{k!}}{\binom {n-1}{k-1}}(-1)^{n-k}a_{k}$ | $\ast$ | ${\widehat {B}}(z)={\widehat {A}}\left({\frac {z}{1+z}}\right)$ |   |
| 6 | $a_{n}=\sum _{k=0}^{n}{\binom {n}{k}}^{2}k!b_{n-k}$ | $b_{n}=\sum _{k=0}^{n}{\binom {n}{k}}^{2}(-1)^{k}k!a_{n-k}$ | $\ast$ | ${\widehat {B}}(z)={\frac {1}{1+z}}{\widehat {A}}\left({\frac {z}{1+z}}\right)$ |   |
| 7 | ${\frac {n!a_{n}}{(n+p)!}}=\sum _{k=0}^{n}{\binom {n}{k}}{\frac {k!b_{k}}{(k+p)!}}$ | ${\frac {n!b_{n}}{(n+p)!}}=\sum _{k=0}^{n}{\binom {n}{k}}{\frac {(-1)^{n-k}k!a_{k}}{(k+p)!}}$ | $B(z)={\frac {1}{(1+z)^{p+1}}}A\left({\frac {z}{1+z}}\right)$ | $\ast$ |   |
| 8 | $s_{n}=\sum _{k\geq 0}{\binom {n+k}{m+2k}}a_{k}$ | $\ast$ | $S(z)={\frac {z^{m}}{(1-z)^{m+1}}}A\left({\frac {z}{(1-z)^{2}}}\right)$ | $\ast$ | See. |
| 9 | $a_{n}=\sum _{k=0}^{n}{\binom {n}{k}}a^{k}(-c)^{n-k}b_{k}$ | $\ast$ | $A(z)={\frac {1}{1+cx}}B\left({\frac {ax}{1+cx}}\right)$ | $\ast$ | Generalization of the binomial transform for $a,b,c\in \mathbb {C}$ such that $\left\|{\frac {ax}{1+cx}}\right\|<\sigma _{B}$ . |
| 10 | $w_{n}=\sum _{i=0}^{n}{\binom {n}{i}}k^{n}a_{i},\ k\neq 0$ | $\ast$ | $\ast$ | ${\widehat {W}}(A,k;z)=e^{kz}{\widehat {A}}(kz)$ | The **k -binomial transform** (see ) |
| 11 | $f_{n}=\sum _{i=0}^{n}{\binom {n}{i}}k^{n-i}a_{i},\ k\neq 0$ | $\ast$ | $\ast$ | ${\widehat {F}}(A,k;z)=e^{kz}{\widehat {A}}(z)$ | The **falling k -binomial transform** (refer to Spivey's article in ) |
| 12 | $r_{n}=\sum _{i=0}^{n}{\binom {n}{i}}k^{i}a_{i},\ k\neq 0$ | $\ast$ | $\ast$ | ${\widehat {R}}(A,k;z)=e^{z}{\widehat {A}}(kz)$ | The **rising k -binomial transform** (refer to Spivey's article in ) |

#### Gould classes of inverse relations

The terms, $A_{n,k}$ and $B_{n,k}$ , in the inversion formulas of the form

$a_{n}=\sum _{k}A_{n,k}\cdot b_{k}\quad \longleftrightarrow \quad b_{n}=\sum _{k}B_{n,k}\cdot (-1)^{n-k}a_{k},$

forming several special cases of *Gould classes of inverse relations* are given in the next table.

| Class | $A_{n,k}$ | $B_{n,k}$ |
|---|---|---|
| 1 | ${\binom {p+qk-k}{n-k}}$ | ${\binom {p+qn-k}{n-k}}-q{\binom {p+qn-k-1}{n-k-1}}$ |
| 2 | ${\binom {p+qk-k}{n-k}}+q{\binom {p+qk-k}{n-1-k}}$ | ${\binom {p+qn-k}{n-k}}$ |
| 3 | ${\binom {p+qn-n}{k-n}}$ | ${\binom {p+qk-n}{k-n}}-q{\binom {p+qk-n-1}{k-n-1}}$ |
| 4 | ${\binom {p+qn-n}{k-n}}+q{\binom {p+qn-n}{k-1-n}}$ | ${\binom {p+qk-n}{k-n}}$ |

For classes 1 and 2, the range on the sum satisfies $k\in [0,n]$ , and for classes 3 and 4 the bounds on the summation are given by $k=n,n+1,\ldots$ . These terms are also somewhat simplified from their original forms in the table by the identities

${\binom {p+qn-k}{n-k}}-q\times {\binom {p+qn-k-1}{n-k-1}}={\frac {p+qk-k}{p+qn-k}}{\binom {p+qn-k}{n-k}}$

${\binom {p+qk-k}{n-k}}+q\times {\binom {p+qk-k}{n-1-k}}={\frac {p+qn-n+1}{p+qk-n+1}}{\binom {p+qk-k}{n-k}}.$

#### The simpler Chebyshev inverse relations

The so-termed *simpler* cases of the Chebyshev classes of inverse relations in the subsection below are given in the next table.

| Relation | Formula for $a_{n}$ | Inverse Formula for $b_{n}$ |
|---|---|---|
| 1 | $a_{n}=\sum _{k}{\binom {n}{k}}b_{n-2k}$ | $b_{n}=\sum _{k}\left[{\binom {n-k}{k}}+{\binom {n-k-1}{k-1}}\right](-1)^{k}a_{n-2k}$ |
| 2 | $a_{n}=\sum _{k}\left[{\binom {n}{k}}-{\binom {n}{k-1}}\right]b_{n-2k}$ | $b_{n}=\sum _{k}{\binom {n-k}{k}}(-1)^{k}a_{n-2k}$ |
| 3 | $a_{n}=\sum _{k}{\binom {n+2k}{k}}b_{n+2k}$ | $b_{n}=\sum _{k}\left[{\binom {n+k}{k}}+{\binom {n+k-1}{k-1}}\right](-1)^{k}a_{n+2k}$ |
| 4 | $a_{n}=\sum _{k}\left[{\binom {n+2k}{k}}-{\binom {n+2k}{k-1}}\right]b_{n+2k}$ | $b_{n}=\sum _{k}{\binom {n+2k}{k}}(-1)^{k}a_{n+2k}$ |
| 5 | $a_{n}=\sum _{k}{\binom {n-k}{k}}b_{n-k}$ | $b_{n}=\sum _{k}\left[{\binom {n+k-1}{k}}-{\binom {n+k-1}{k-1}}\right](-1)^{k}a_{n-k}$ |
| 6 | $a_{n}=\sum _{k}\left[{\binom {n+1-k}{k}}+{\binom {n-k}{k-1}}\right]b_{n-k}$ | $b_{n}=\sum _{k}{\binom {n+k}{k}}(-1)^{k}a_{n-k}$ |
| 7 | $a_{n}=\sum _{k=0}^{n}{\binom {n}{k}}b_{n+ck}$ | $b_{n}=\sum _{k}{\binom {n+ck+k}{k}}{\frac {n(-1)^{k}}{n+ck+k}}a_{n+ck}$ |

The formulas in the table are simplified somewhat by the following identities:

${\begin{aligned}{\binom {n-k}{k}}+{\binom {n-k-1}{k-1}}&={\frac {n}{n-k}}{\binom {n-k}{k}}\\{\binom {n}{k}}-{\binom {n}{k-1}}&={\frac {n+1-k}{n+1-2k}}{\binom {n}{k}}\\{\binom {n+2k}{k}}-{\binom {n+2k}{k-1}}&={\frac {n+1}{n+1+k}}{\binom {n+2k}{k}}\\{\binom {n+k-1}{k}}-{\binom {n+k-1}{k-1}}&={\frac {n-k}{n+k}}{\binom {n+k}{k}}.\end{aligned}}$

Additionally the inversion relations given in the table also hold when $n\longmapsto n+p$ in any given relation.

#### Chebyshev classes of inverse relations

The terms, $A_{n,k}$ and $B_{n,k}$ , in the inversion formulas of the form

$a_{n}=\sum _{k}A_{n,k}\cdot b_{n+ck}\quad \longleftrightarrow \quad b_{n}=\sum _{k}B_{n,k}\cdot (-1)^{k}a_{n+ck},$

for non-zero integers c forming several special cases of *Chebyshev classes of inverse relations* are given in the next table.

| Class | $A_{n,k}$ | $B_{n,k}$ |
|---|---|---|
| 1 | ${\binom {n}{k}}$ | ${\binom {n+ck+k}{k}}-(c+1){\binom {n+ck+k-1}{k-1}}$ |
| 2 | ${\binom {n}{k}}+(c+1){\binom {n}{k-1}}$ | ${\binom {n+ck+k}{k}}$ |
| 3 | ${\binom {n+ck}{k}}$ | ${\binom {n-1+k}{k}}+c{\binom {n-1+k}{k-1}}$ |
| 4 | ${\binom {n+ck}{k}}-(c-1){\binom {n+ck}{k-1}}$ | ${\binom {n+k}{k}}$ |

Additionally, these inversion relations also hold when $n\longmapsto n+p$ for some $p=0,1,2,\ldots ,$ or when the sign factor of $(-1)^{k}$ is shifted from the terms $B_{n,k}$ to the terms $A_{n,k}$ . The formulas given in the previous table are simplified somewhat by the identities

${\begin{aligned}{\binom {n+ck+k}{k}}-(c+1){\binom {n+ck+k-1}{k-1}}&={\frac {n}{n+ck+k}}{\binom {n+ck+k}{k}}\\{\binom {n}{k}}+(c+1){\binom {n}{k-1}}&={\frac {n+1+ck}{n+1-k}}{\binom {n}{k}}\\{\binom {n-1+k}{k}}+c{\binom {n-1+k}{k-1}}&={\frac {n+ck}{n}}{\binom {n-1+k}{k}}\\{\binom {n+ck}{k}}-(c-1){\binom {n+ck}{k-1}}&={\frac {n+1}{n+1+ck-k}}{\binom {n+ck}{k}}.\end{aligned}}$

#### The simpler Legendre inverse relations

| Relation | Formula for $a_{n}$ | Inverse Formula for $b_{n}$ |
|---|---|---|
| 1 | $a_{n}=\sum _{k}{\binom {n+p+k}{n-k}}b_{k}$ | $b_{n}=\sum _{k}\left[{\binom {2n+p}{n-k}}-{\binom {2n+p}{n-k-1}}\right](-1)^{n-k}a_{k}$ |
| 2 | $a_{n}=\sum _{k}{\binom {2n+p}{n-k}}b_{k}$ | $b_{n}=\sum _{k}\left[{\binom {n+p+k}{n-k}}-{\binom {n+p+k-1}{n-k-1}}\right](-1)^{n-k}a_{k}$ |
| 3 | $a_{n}=\sum _{k\geq n}{\binom {n+p+k}{k-n}}b_{k}$ | $b_{n}=\sum _{k\geq n}\left[{\binom {2k+p}{k-n}}-{\binom {2k+p}{k-n-1}}\right](-1)^{n-k}a_{k}$ |
| 4 | $a_{n}=\sum _{k\geq n}{\binom {2k+p}{k-n}}b_{k}$ | $b_{n}=\sum _{k\geq n}\left[{\binom {n+p+k}{k-n}}-{\binom {n+p+k-1}{k-n-1}}\right](-1)^{n-k}a_{k}$ |
| 5 | $a_{n}=\sum _{k}{\binom {2n+p}{k}}b_{n-2k}$ | $b_{n}=\sum _{k}\left[{\binom {2n+p-3k}{k}}+3{\binom {2n+p-3k-1}{k-1}}\right](-1)^{k}a_{n-2k}$ |
| 6 | $a_{n}=\sum _{k}\left[{\binom {2n+p}{k}}-3{\binom {2n+p}{k-1}}\right]b_{n-2k}$ | $b_{n}=\sum _{k}{\binom {2n+p-3k}{k}}(-1)^{k}a_{n-2k}$ |
| 7 | $a_{n}=\sum _{k=0}^{[n/2]}{\binom {3n}{k}}b_{n-2k}$ | $b_{n}=\sum _{k=0}^{[n/2]}\left[{\binom {3n-5k}{k}}+5{\binom {3n-5k-1}{k-1}}\right](-1)^{k}a_{n-2k}$ |
| 8 | $a_{n}=\sum _{k=0}^{[n/3]}{\binom {2n}{k}}b_{n-3k}$ | $b_{n}=\sum _{k=0}^{[n/3]}\left[{\binom {2n-5k}{k}}+5{\binom {2n-5k-1}{k-1}}\right](-1)^{k}a_{n-3k}$ |

#### Legendre–Chebyshev classes of inverse relations

The *Legendre–Chebyshev classes of inverse relations* correspond to inversion relations of the form

$a_{n}=\sum _{k}A_{n,k}\cdot b_{k}\quad \longleftrightarrow \quad b_{n}=\sum _{k}B_{n,k}\cdot (-1)^{n-k}a_{k},$

where the terms, $A_{n,k}$ and $B_{n,k}$ , implicitly depend on some fixed non-zero $c\in \mathbb {Z}$ . In general, given a class of Chebyshev inverse pairs of the form

$a_{n}=\sum _{k}A_{n,k}\cdot b_{n-ck}\quad \longleftrightarrow \quad b_{n}=\sum _{k}B_{n,k}\cdot (-1)^{k}a_{n-ck},$

if c a prime, the substitution of $n\longmapsto cn+p$ , $a_{cn+p}\longmapsto A_{n}$ , and $b_{cn+p}\longmapsto B_{n}$ (possibly replacing $k\longmapsto n-k$ ) leads to a *Legendre–Chebyshev* pair of the form

$A_{n}=\sum _{k}A_{cn+p,k}B_{n-k}\quad \longleftrightarrow \quad B_{n}=\sum _{k}B_{cn+p,k}(-1)^{k}A_{n-k}.$

Similarly, if the positive integer $c:=de$ is composite, we can derive inversion pairs of the form

$A_{n}=\sum _{k}A_{dn+p,k}B_{n-ek}\quad \longleftrightarrow \quad B_{n}=\sum _{k}B_{dn+p,k}(-1)^{k}A_{n-ek}.$

The next table summarizes several generalized classes of Legendre–Chebyshev inverse relations for some non-zero integer c .

| Class | $A_{n,k}$ | $B_{n,k}$ |
|---|---|---|
| 1 | ${\binom {cn+p}{n-k}}$ | ${\binom {n+p-1+ck-k}{n-k}}+c{\binom {n+p-1+ck-k}{n-k-1}}$ |
| 2 | ${\binom {cn+p}{k-n}}$ | ${\binom {ck+k+p-n-1}{k-n}}-c{\binom {ck+k+p-n-1}{k-n-1}}$ |
| 3 | ${\binom {ck+p}{n-p}}$ | ${\binom {cn+n+p-k-1}{n-k}}-c{\binom {cn+n+p-k-1}{n-k-1}}$ |
| 4 | ${\binom {ck+p}{k-n}}$ | ${\binom {cn-n+p+k-1}{k-n}}+c{\binom {cn-n+p+k-1}{k-n-1}}$ |
| 5 | ${\binom {cn+p}{n-k}}-(c-1){\binom {cn+p}{n-k-1}}$ | ${\binom {n+p+ck-k}{n-k}}$ |
| 6 | ${\binom {cn+p}{k-n}}+(c+1){\binom {cn+p}{k-n-1}}$ | ${\binom {ck+k+p-n}{k-n}}$ |
| 7 | ${\binom {ck+p}{n-k}}+(c+1){\binom {ck+p}{n-k-1}}$ | ${\binom {cn+n+p-k}{n-k}}$ |
| 8 | ${\binom {ck+p}{k-n}}-(c-1){\binom {ck+p}{k-n-1}}$ | ${\binom {cn-n+p+k}{k-n}}$ |

#### Abel inverse relations

*Abel inverse relations* correspond to *Abel inverse pairs* of the form

$a_{n}=\sum _{k=0}^{n}{\binom {n}{k}}A_{nk}b_{k}\quad \longleftrightarrow \quad b_{n}=\sum _{k=0}^{n}{\binom {n}{k}}B_{nk}(-1)^{n-k}a_{k},$

where the terms, $A_{nk}$ and $B_{nk}$ , may implicitly vary with some indeterminate summation parameter x . These relations also still hold if the binomial coefficient substitution of ${\binom {n}{k}}\longmapsto {\binom {n+p}{k+p}}$ is performed for some non-negative integer p . The next table summarizes several notable forms of these Abel inverse relations.

| Number | $A_{nk}$ | $B_{nk}$ | Generating Function Identity |
|---|---|---|---|
| 1 | $x(x+n-k)^{n-k-1}$ | $x(x-n+k)^{n-k-1}$ | $\ast$ |
| 2 | $(x+n-k)^{n-k}$ | $(x^{2}-n+k)(x-n+k)^{n-k-2}$ | $\ast$ |
| 3 | $(x+k)^{n-k}$ | $(x+k)(x+n)^{n-k-1}$ | $\ast$ |
| 3a | $(x+n)(x+k)^{n-k-1}$ | $(x+n)^{n-k}$ | $\ast$ |
| 4 | $(x+2n)(x+n+k)^{n-k-1}$ | $(x+2n)(x+n+k)^{n-k-1}$ | $\ast$ |
| 4a | $(x+2k)(x+n+k)^{n-k-1}$ | $(x+2k)(x+n+k)^{n-k-1}$ | $\ast$ |
| 5 | $(n+k)^{n-k}$ | $\left[n+k(4n-1)\right](n+k)^{n-k-2}$ | $\ast$ |

#### Inverse relations derived from ordinary generating functions

If we let the *convolved Fibonacci numbers*, $f_{k}^{(\pm p)}$ , be defined by

${\begin{aligned}f_{n}^{(p)}&=\sum _{j\geq 0}{\binom {p+n-j-1}{n-j}}{\binom {n-j}{j}}\\f_{n}^{(-p)}&=\sum _{j\geq 0}{\binom {p}{n+j}}{\binom {n-j}{j}}(-1)^{n-j},\end{aligned}}$

we have the next table of inverse relations which are obtained from properties of ordinary sequence generating functions proved as in section 3.3 of Riordan's book.

| Relation | Formula for $a_{n}$ | Inverse Formula for $b_{n}$ |
|---|---|---|
| 1 | $a_{n}=\sum _{k=0}^{n}{\binom {p+k}{k}}b_{n-k}$ | $b_{n}=\sum _{k=0}^{n}{\binom {p+1}{k}}(-1)^{k}a_{n-k}$ |
| 2 | $a_{n}=\sum _{k\geq 0}{\binom {p+k}{k}}b_{n-qk}$ | $b_{n}=\sum _{k}{\binom {p+1}{k}}(-1)^{k}a_{n-qk}$ |
| 3 | $a_{n}=\sum _{k=0}^{n}f_{k}^{(p)}b_{n-k}$ | $b_{n}=\sum _{k=0}^{n}f_{k}^{(-p)}a_{n-k}$ |
| 4 | $a_{n}=\sum _{k=0}^{n}{\binom {2k}{k}}b_{n-k}$ | $\sum _{k=0}^{n}{\binom {2k}{k}}{\frac {a_{n-k}}{(1-2k)}}$ |
| 5 | $a_{n}=\sum _{k=0}^{n}{\binom {2k}{k}}{\frac {b_{n-k}}{(k+1)}}$ | $b_{n}=a_{n}-\sum _{k=1}^{n}{\binom {2k}{k}}{\frac {a_{n-k}}{k}}$ |
| 6 | $a_{n}=\sum _{k=0}^{n}{\binom {2p+2k}{p+k}}{\binom {p+k}{k}}{\binom {2p}{p}}^{-1}b_{n-k}$ | $b_{n}=\sum _{k=0}^{n}{\binom {2p+1}{2k}}{\binom {p+k}{k}}{\binom {p+k}{2k}}^{-1}(-1)^{k}a_{n-k}$ |
| 7 | $a_{n}=\sum _{k}{\binom {4k}{2k}}b_{n-2k}$ | $b_{n}=\sum _{k}{\binom {4k}{2k}}{\frac {(8k+1)a_{n-2k}}{(2k+1)(k+1)}}$ |
| 8 | $a_{n}=\sum _{k}{\binom {4k+2}{2k+1}}b_{n-2k}$ | $b_{n}={\frac {a_{n}}{2}}-\sum _{k\geq 1}{\binom {4k-2}{2k-1}}{\frac {(8k-3)a_{n-2k}}{2k(4k-3)}}$ |
| 9 | $a_{n}={\binom {4k}{2k}}{\frac {b_{n-2k}}{(1-4k)}}$ | $b_{n}=\sum _{k}{\binom {4k}{2k}}{\frac {a_{n-2k}}{(2k+1)}}$ |

Note that relations 3, 4, 5, and 6 in the table may be transformed according to the substitutions $a_{n-k}\longmapsto a_{n-qk}$ and $b_{n-k}\longmapsto b_{n-qk}$ for some fixed non-zero integer $q\geq 1$ .

#### Inverse relations derived from exponential generating functions

Let $B_{n}$ and $E_{n}$ denote the Bernoulli numbers and Euler numbers, respectively, and suppose that the sequences, $\{d_{2n}\}$ , $\{e_{2n}\}$ , and $\{f_{2n}\}$ are defined by the following exponential generating functions:

${\begin{aligned}\sum _{n\geq 0}{\frac {d_{2n}z^{2n}}{(2n)!}}&={\frac {2z}{e^{z}-e^{-z}}}\\\sum _{n\geq 0}{\frac {e_{2n}z^{2n}}{(2n)!}}&={\frac {z^{2}}{e^{z}+e^{-z}-2}}\\\sum _{n\geq 0}{\frac {f_{2n}z^{2n}}{(2n)!}}&={\frac {z^{3}}{3(e^{z}-e^{-z}-2z)}}.\end{aligned}}$

The next table summarizes several notable cases of inversion relations obtained from exponential generating functions in section 3.4 of Riordan's book.

| Relation | Formula for $a_{n}$ | Inverse Formula for $b_{n}$ |
|---|---|---|
| 1 | $a_{n}=\sum _{k=0}^{n}{\binom {n}{k}}{\frac {b_{k}}{(k+1)}}$ | $b_{n}=\sum _{k=0}^{n}B_{k}a_{n-k}$ |
| 2 | $a_{n}=\sum _{k}{\binom {n+k}{k}}{\frac {b_{n+k}}{(k+1)}}$ | $b_{n}=\sum _{k}{\binom {n+k}{k}}B_{k}a_{n+k}$ |
| 3 | $a_{n}=\sum _{k}{\binom {n}{2k}}b_{n-2k}$ | $b_{n}=\sum _{k}{\binom {n}{2k}}E_{2k}a_{n-2k}$ |
| 4 | $a_{n}=\sum _{k}{\binom {n+2k}{2k}}b_{n+2k}$ | $b_{n}=\sum _{k}{\binom {n+2k}{2k}}E_{2k}a_{n+2k}$ |
| 5 | $a_{n}=\sum _{k}{\binom {n}{2k}}{\frac {b_{n-2k}}{(2k+1)}}$ | $b_{n}=\sum _{k}{\binom {n}{2k}}d_{2k}a_{n-2k}$ |
| 6 | $a_{n}=\sum _{k}{\binom {n+1}{2k+1}}b_{n-2k}$ | $(n+1)\cdot b_{n}=\sum _{k}{\binom {n+1}{2k}}d_{2k}a_{n-2k}$ |
| 7 | $a_{n}=\sum _{k}{\binom {n}{2k}}{\binom {2k+2}{2}}^{-1}b_{n-2k}$ | $b_{n}=\sum _{k}{\binom {n}{2k}}e_{2k}a_{n-2k}$ |
| 8 | $a_{n}=\sum _{k}{\binom {n+2}{2k+2}}b_{n-2k}$ | ${\binom {n+2}{2}}\cdot b_{n}=\sum _{k}{\binom {n+2}{2k}}e_{2k}a_{n-2k}$ |
| 9 | $a_{n}=\sum _{k}{\binom {n}{2k}}{\binom {2k+3}{3}}^{-1}b_{n-2k}$ | $b_{n}=\sum _{k}{\binom {n}{2k}}f_{2k}a_{n-2k}$ |
| 10 | $a_{n}=\sum _{k}{\binom {n+3}{2k+3}}b_{n-2k}$ | ${\binom {n+3}{3}}\cdot b_{n}=\sum _{k}{\binom {n+3}{2k}}f_{2k}a_{n-2k}$ |

#### Multinomial inverses

The inverse relations used in formulating the binomial transform cited in the previous subsection are generalized to corresponding two-index inverse relations for sequences of two indices, and to multinomial inversion formulas for sequences of $j\geq 3$ indices involving the binomial coefficients in Riordan. In particular, we have the form of a two-index inverse relation given by

$a_{mn}=\sum _{j=0}^{m}\sum _{k=0}^{n}{\binom {m}{j}}{\binom {n}{k}}(-1)^{j+k}b_{jk}\quad \longleftrightarrow \quad b_{mn}=\sum _{j=0}^{m}\sum _{k=0}^{n}{\binom {m}{j}}{\binom {n}{k}}(-1)^{j+k}a_{jk},$

and the more general form of a multinomial pair of inversion formulas given by

$a_{n_{1}n_{2}\cdots n_{j}}=\sum _{k_{1},\ldots ,k_{j}}{\binom {n_{1}}{k_{1}}}\cdots {\binom {n_{j}}{k_{j}}}(-1)^{k_{1}+\cdots +k_{j}}b_{k_{1}k_{2}\cdots k_{j}}\quad \longleftrightarrow \quad b_{n_{1}n_{2}\cdots n_{j}}=\sum _{k_{1},\ldots ,k_{j}}{\binom {n_{1}}{k_{1}}}\cdots {\binom {n_{j}}{k_{j}}}(-1)^{k_{1}+\cdots +k_{j}}a_{k_{1}k_{2}\cdots k_{j}}.$
