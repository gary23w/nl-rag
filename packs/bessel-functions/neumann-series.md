---
title: "Neumann series"
source: https://en.wikipedia.org/wiki/Neumann_series
domain: bessel-functions
license: CC-BY-SA-4.0
tags: bessel function, spherical bessel function, modified bessel function, kelvin functions
fetched: 2026-07-02
---

# Neumann series

A **Neumann series** is a mathematical series that sums *k*-times repeated applications of an operator T . This has the generator form

$\sum _{k=0}^{\infty }T^{k}$

where $T^{k}$ is the *k*-times repeated application of T ; $T^{0}$ is the identity operator I and $T^{k}:={}T^{k-1}\circ {T}$ for $k>0$ . This is a special case of the generalization of a geometric series of real or complex numbers to a geometric series of operators. The generalized initial term of the series is the identity operator $T^{0}=I$ and the generalized common ratio of the series is the operator $T.$

The series is named after the mathematician Carl Neumann, who used it in 1877 in the context of potential theory. The Neumann series is used in functional analysis. It is closely connected to the resolvent formalism for studying the spectrum of bounded operators and, applied from the left to a function, it forms the Liouville-Neumann series that formally solves Fredholm integral equations.

## Properties

Suppose that T is a bounded linear operator on the normed vector space X . If the Neumann series converges in the operator norm, then $I-T$ is invertible and its inverse is the series:

$(I-T)^{-1}=\sum _{k=0}^{\infty }T^{k}$

,

where I is the identity operator in X . To see why, consider the partial sums

$S_{n}:=\sum _{k=0}^{n}T^{k}$

.

Then we have

$\lim _{n\rightarrow \infty }(I-T)S_{n}=\lim _{n\rightarrow \infty }\left(\sum _{k=0}^{n}T^{k}-\sum _{k=0}^{n}T^{k+1}\right)=\lim _{n\rightarrow \infty }\left(I-T^{n+1}\right)=I$

This result on operators is analogous to geometric series in $\mathbb {R}$ .

One case in which convergence is guaranteed is when X is a Banach space and $|T|<1$ in the operator norm; another compatible case is that ${\textstyle \sum _{k=0}^{\infty }|T^{k}|}$ converges. However, there are also results which give weaker conditions under which the series converges.

## Example

Let $C\in \mathbb {R} ^{3\times 3}$ be given by:

${\begin{pmatrix}0&{\frac {1}{2}}&{\frac {1}{4}}\\{\frac {5}{7}}&0&{\frac {1}{7}}\\{\frac {3}{10}}&{\frac {3}{5}}&0\end{pmatrix}}.$

For the Neumann series ${\textstyle \sum _{k=0}^{n}C^{k}}$ to converge to $(I-C)^{-1}$ as n goes to infinity, the spectral norm of C must be smaller than unity. This norm is about $0.9056$ as can be checked numerically (e.g., by computing the singular values), confirming that the Neumann series converges.

## Approximate matrix inversion

A truncated Neumann series can be used for approximate matrix inversion. To approximate the inverse of an invertible matrix A , consider that

${\begin{aligned}A^{-1}&=(I-I+A)^{-1}\\&=(I-(I-A))^{-1}\\&=(I-T)^{-1}\end{aligned}}$

for $T=(I-A).$ Then, using the Neumann series identity that ${\textstyle \sum _{k=0}^{\infty }T^{k}=(I-T)^{-1}}$ if the appropriate norm condition on $T=(I-A)$ is satisfied, ${\textstyle A^{-1}=(I-(I-A))^{-1}=\sum _{k=0}^{\infty }(I-A)^{k}.}$ Since these terms shrink with increasing $k,$ given the conditions on the norm, then truncating the series at some finite n may give a practical approximation to the inverse matrix:

$A^{-1}\approx \sum _{k=0}^{n}(I-A)^{k}.$

## The set of invertible operators is open

A corollary is that the set of invertible operators between two Banach spaces B and $B'$ is open in the topology induced by the operator norm. Indeed, let $S:B\to B'$ be an invertible operator and let $T:B\to B'$ be another operator. If $|S-T|<|S^{-1}|^{-1}$ , then T is also invertible. Since $|I-S^{-1}T|<1$ , the Neumann series ${\textstyle \sum _{k=0}^{\infty }(I-S^{-1}T)^{k}}$ is convergent. Therefore, we have

$T^{-1}S=(I-(I-S^{-1}T))^{-1}=\sum _{k=0}^{\infty }(I-S^{-1}T)^{k}$

Taking the norms, we get

$|T^{-1}S|\leq {\frac {1}{1-|I-(S^{-1}T)|}}$

The norm of $T^{-1}$ can be bounded by

$|T^{-1}|\leq {\tfrac {1}{1-q}}|S^{-1}|\quad {\text{where}}\quad q=|S-T|\,|S^{-1}|.$

## Applications

The Neumann series has been used for linear data detection in massive multiuser multiple-input multiple-output (MIMO) wireless systems. Using a truncated Neumann series avoids computation of an explicit matrix inverse, which reduces the complexity of linear data detection from cubic to square.

Another application is the theory of propagation graphs which takes advantage of Neumann series to derive closed form expressions for transfer functions.
