---
title: "Schönhage–Strassen algorithm"
source: https://en.wikipedia.org/wiki/Schönhage–Strassen_algorithm
domain: karatsuba-multiplication
license: CC-BY-SA-4.0
tags: karatsuba algorithm, fast multiplication, toom cook multiplication, divide and conquer
fetched: 2026-07-02
---

# Schönhage–Strassen algorithm

The **Schönhage–Strassen algorithm** is an asymptotically fast multiplication algorithm for large integers, published by Arnold Schönhage and Volker Strassen in 1971. It works by recursively applying fast Fourier transform (FFT) over the integers modulo $2^{n}+1$ . The run-time bit complexity to multiply two n-digit numbers using the algorithm is $O(n\cdot \log n\cdot \log \log n)$ in big O notation.

The Schönhage–Strassen algorithm was the asymptotically fastest multiplication method known from 1971 until 2007. It is asymptotically faster than older methods such as Karatsuba and Toom–Cook multiplication, and starts to outperform them in practice for numbers beyond about 10,000 to 100,000 decimal digits. In 2007, Martin Fürer published an algorithm with faster asymptotic complexity. In 2019, David Harvey and Joris van der Hoeven demonstrated that multi-digit multiplication has theoretical $O(n\log n)$ complexity; however, their algorithm has constant factors which make it impossibly slow for any conceivable practical problem (see galactic algorithm).

Applications of the Schönhage–Strassen algorithm include large computations done for their own sake such as the Great Internet Mersenne Prime Search and approximations of π, as well as practical applications such as Lenstra elliptic curve factorization via Kronecker substitution, which reduces polynomial multiplication to integer multiplication.

## Description

This section has a simplified version of the algorithm, showing how to compute the product $ab$ of two natural numbers $a,b$ , modulo a number of the form $2^{n}+1$ , where $n=2^{k}M$ is some fixed number. The integers $a,b$ are to be divided into $D=2^{k}$ blocks of M bits, so in practical implementations, it is important to strike the right balance between the parameters $M,k$ . In any case, this algorithm will provide a way to multiply two positive integers, provided n is chosen so that $ab<2^{n}+1$ .

Let $n=DM$ be the number of bits in the signals a and b , where $D=2^{k}$ is a power of two. Divide the signals a and b into D blocks of M bits each, storing the resulting blocks as arrays $A,B$ (whose entries we shall consider for simplicity as arbitrary precision integers).

We now select a modulus for the Fourier transform, as follows. Let $M'$ be such that $DM'\geq 2M+k$ . Also put $n'=DM'$ , and regard the elements of the arrays $A,B$ as (arbitrary precision) integers modulo $2^{n'}+1$ . Observe that since $2^{n'}+1\geq 2^{2M+k}+1=D2^{2M}+1$ , the modulus is large enough to accommodate any carries that can result from multiplying a and b . Thus, the product $ab$ (modulo $2^{n}+1$ ) can be calculated by evaluating the convolution of $A,B$ . Also, with $g=2^{2M'}$ , we have $g^{D/2}\equiv -1{\pmod {2^{n'}+1}}$ , and so g is a primitive D th root of unity modulo $2^{n'}+1$ .

We now take the discrete Fourier transform of the arrays $A,B$ in the ring $\mathbb {Z} /(2^{n'}+1)\mathbb {Z}$ , using the root of unity g for the Fourier basis, giving the transformed arrays ${\widehat {A}},{\widehat {B}}$ . Because $D=2^{k}$ is a power of two, this can be achieved in logarithmic time using a fast Fourier transform.

Let ${\widehat {C}}_{i}={\widehat {A}}_{i}{\widehat {B}}_{i}$ (pointwise product), and compute the inverse transform C of the array ${\widehat {C}}$ , again using the root of unity g . The array C is now the convolution of the arrays $A,B$ . Finally, the product $ab{\pmod {2^{n}+1}}$ is given by evaluating $ab\equiv \sum _{j}C_{j}2^{Mj}\mod {2^{n}+1}.$

This basic algorithm can be improved in several ways. Firstly, it is not necessary to store the digits of $a,b$ to arbitrary precision, but rather only up to $n'+1$ bits, which gives a more efficient machine representation of the arrays $A,B$ . Secondly, it is clear that the multiplications in the forward transforms are simple bit shifts. With some care, it is also possible to compute the inverse transform using only shifts. Taking care, it is thus possible to eliminate any true multiplications from the algorithm except for where the pointwise product ${\widehat {C}}_{i}={\widehat {A}}_{i}{\widehat {B}}_{i}$ is evaluated. It is therefore advantageous to select the parameters $D,M$ so that this pointwise product can be performed efficiently, either because it is a single machine word or using some optimized algorithm for multiplying integers of a (ideally small) number of words. Selecting the parameters $D,M$ is thus an important area for further optimization of the method.

## Details

Every number in base B, can be written as a polynomial:

$X=\sum _{i=0}^{N}{x_{i}B^{i}}$

Furthermore, multiplication of two numbers could be thought of as a product of two polynomials:

$XY=\left(\sum _{i=0}^{N}{x_{i}B^{i}}\right)\left(\sum _{j=0}^{N}{y_{i}B^{j}}\right)$

Because, for $B^{k}$ : $c_{k}=\sum _{(i,j):i+j=k}{a_{i}b_{j}}=\sum _{i=0}^{k}{a_{i}b_{k-i}}$ , we have a convolution.

By using FFT (fast Fourier transform), used in the original version rather than NTT (Number-theoretic transform), with convolution rule; we get

${\hat {f}}(a*b)={\hat {f}}\left(\sum _{i=0}^{k}a_{i}b_{k-i}\right)={\hat {f}}(a)\bullet {\hat {f}}(b).$

That is; $C_{k}=a_{k}\bullet b_{k}$ , where $C_{k}$ is the corresponding coefficient in Fourier space. This can also be written as: ${\text{fft}}(a*b)={\text{fft}}(a)\bullet {\text{fft}}(b)$ .

We have the same coefficients due to linearity under the Fourier transform, and because these polynomials only consist of one unique term per coefficient:

${\hat {f}}(x^{n})=\left({\frac {i}{2\pi }}\right)^{n}\delta ^{(n)}$

and

${\hat {f}}(a\,X(\xi )+b\,Y(\xi ))=a\,{\hat {X}}(\xi )+b\,{\hat {Y}}(\xi )$

Convolution rule: ${\hat {f}}(X*Y)=\ {\hat {f}}(X)\bullet {\hat {f}}(Y)$

We have reduced our convolution problem to product problem, through FFT.

By finding the FFT of the polynomial interpolation of each $C_{k}$ , one can determine the desired coefficients.

This algorithm uses the divide-and-conquer method to divide the problem into subproblems.

### Convolution under mod *N*

$c_{k}=\sum _{(i,j):i+j\equiv k{\pmod {N(n)}}}a_{i}b_{j}$

, where

$N(n)=2^{n}+1$

.

By letting:

$a_{i}'=\theta ^{i}a_{i}$

and

$b_{j}'=\theta ^{j}b_{j},$

where $\theta ^{N}=-1$ is the nth root, one sees that:

${\begin{aligned}C_{k}&=\sum _{(i,j):i+j\equiv k{\pmod {N(n)}}}a_{i}b_{j}=\theta ^{-k}\sum _{(i,j):i+j\equiv k{\pmod {N(n)}}}a_{i}'b_{j}'\\[6pt]&=\theta ^{-k}\left(\sum _{(i,j):i+j=k}a_{i}'b_{j}'+\sum _{(i,j):i+j=k+n}a_{i}'b_{j}'\right)\\[6pt]&=\theta ^{-k}\left(\sum _{(i,j):i+j=k}a_{i}b_{j}\theta ^{k}+\sum _{(i,j):i+j=k+n}a_{i}b_{j}\theta ^{n+k}\right)\\[6pt]&=\sum _{(i,j):i+j=k}a_{i}b_{j}+\theta ^{n}\sum _{(i,j):i+j=k+n}a_{i}b_{j}.\end{aligned}}$

This mean, one can use weight $\theta ^{i}$ , and then multiply with $\theta ^{-k}$ after.

Instead of using weight, as $\theta ^{N}=-1$ , in first step of recursion (when $n=N$ ), one can calculate:

$C_{k}=\sum _{(i,j):i+j\equiv k{\pmod {N(N)}}}=\sum _{(i,j):i+j=k}a_{i}b_{j}-\sum _{(i,j):i+j=k+n}a_{i}b_{j}$

In a normal FFT which operates over complex numbers, one would use:

$\exp \left({\frac {2k\pi i}{n}}\right)=\cos {\frac {2k\pi }{n}}+i\sin {\frac {2k\pi }{n}},\qquad k=0,1,\dots ,n-1.$

${\begin{aligned}C_{k}&=\theta ^{-k}\left(\sum _{(i,j):i+j=k}a_{i}b_{j}\theta ^{k}+\sum _{(i,j):i+j=k+n}a_{i}b_{j}\theta ^{n+k}\right)\\[6pt]&=e^{-i2\pi k/n}\left(\sum _{(i,j):i+j=k}a_{i}b_{j}e^{i2\pi k/n}+\sum _{(i,j):i+j=k+n}a_{i}b_{j}e^{i2\pi (n+k)/n}\right)\end{aligned}}$

However, FFT can also be used as a NTT (number theoretic transformation) in Schönhage–Strassen. This means that we have to use θ to generate numbers in a finite field (for example $\mathrm {GF} (2^{n}+1)$ ).

A root of unity under a finite field GF(*r*), is an element a such that $\theta ^{r-1}\equiv 1$ or $\theta ^{r}\equiv \theta$ . For example GF(*p*), where p is a prime number, gives $\{1,2,\ldots ,p-1\}$ .

Notice that $2^{n}\equiv -1$ in $\operatorname {GF} (2^{n}+1)$ and ${\sqrt {2}}\equiv -1$ in $\operatorname {GF} (2^{n+2}+1)$ . For these candidates, $\theta ^{N}\equiv -1$ under its finite field, and therefore act the way we want .

Same FFT algorithms can still be used, though, as long as θ is a root of unity of a finite field.

To find FFT/NTT transform, we do the following:

${\begin{aligned}C_{k}'&={\hat {f}}(k)={\hat {f}}\left(\theta ^{-k}\left(\sum _{(i,j):i+j=k}a_{i}b_{j}\theta ^{k}+\sum _{(i,j):i+j=k+n}a_{i}b_{j}\theta ^{n+k}\right)\right)\\[6pt]C_{k+k}'&={\hat {f}}(k+k)={\hat {f}}\left(\sum _{(i,j):i+j=2k}a_{i}b_{j}\theta ^{k}+\sum _{(i,j):i+j=n+2k}a_{i}b_{j}\theta ^{n+k}\right)\\[6pt]&={\hat {f}}\left(\sum _{(i,j):i+j=2k}a_{i}b_{j}\theta ^{k}+\sum _{(i,j):i+j=2k+n}a_{i}b_{j}\theta ^{n+k}\right)\\[6pt]&={\hat {f}}\left(A_{k\leftarrow k}\right)\bullet {\hat {f}}(B_{k\leftarrow k})+{\hat {f}}(A_{k\leftarrow k+n})\bullet {\hat {f}}(B_{k\leftarrow k+n})\end{aligned}}$

First product gives contribution to $c_{k}$ , for each k. Second gives contribution to $c_{k}$ , due to $(i+j)$ mod $N(n)$ .

To do the inverse:

$C_{k}=2^{-m}{\hat {f^{-1}}}(\theta ^{-k}C_{k+k}')$

or

$C_{k}={\hat {f^{-1}}}(\theta ^{-k}C_{k+k}')$

depending whether data needs to be normalized.

One multiplies by $2^{-m}$ to normalize FFT data into a specific range, where ${\frac {1}{n}}\equiv 2^{-m}{\bmod {N}}(n)$ , where m is found using the modular multiplicative inverse.

## Implementation details

### Why *N* = 2*M* + 1 mod *N*

In Schönhage–Strassen algorithm, $N=2^{M}+1$ . This should be thought of as a binary tree, where one have values in $0\leq {\text{index}}\leq 2^{M}=2^{i+j}$ . By letting $K\in [0,M]$ , for each K one can find all $i+j=K$ , and group all $(i,j)$ pairs into M different groups. Using $i+j=k$ to group $(i,j)$ pairs through convolution is a classical problem in algorithms.

Having this in mind, $N=2^{M}+1$ help us to group $(i,j)$ into ${\frac {M}{2^{k}}}$ groups for each group of subtasks in depth k in a tree with $N=2^{\frac {M}{2^{k}}}+1$

Notice that $N=2^{M}+1=2^{2^{L}}+1$ , for some L. This makes N a Fermat number. When doing mod $N=2^{M}+1=2^{2^{L}}+1$ , we have a Fermat ring.

Because some Fermat numbers are Fermat primes, one can in some cases avoid calculations.

There are other *N* that could have been used, of course, with same prime number advantages. By letting $N=2^{k}-1$ , one have the maximal number in a binary number with $k+1$ bits. $N=2^{k}-1$ is a Mersenne number, that in some cases is a Mersenne prime. It is a natural candidate against Fermat number $N=2^{2^{L}}+1$

Doing several mod calculations against different N, can be helpful when it comes to solving integer product. By using the Chinese remainder theorem, after splitting M into smaller different types of N, one can find the answer of multiplication xy

Fermat numbers and Mersenne numbers are just two types of numbers, in something called generalized Fermat Mersenne number (GSM); with formula:

$G_{q,p,n}=\sum _{i=1}^{p}q^{(p-i)n}={\frac {q^{pn}-1}{q^{n}-1}}$

$M_{p,n}=G_{2,p,n}$

In this formula, $M_{2,2^{k}}$ is a Fermat number, and $M_{p,1}$ is a Mersenne number.

This formula can be used to generate sets of equations, that can be used in CRT (Chinese remainder theorem):

$g^{\frac {(M_{p,n}-1)}{2}}\equiv -1{\pmod {M_{p,n}}}$

, where

g

is a number such that there exists an

x

where

$x^{2}\equiv g{\pmod {M_{p,n}}}$

, assuming

$N=2^{n}$

Furthermore; $g^{2^{(p-1)n}-1}\equiv a^{2^{n}-1}{\pmod {M_{p,n}}}$ , where a is an element that generates elements in $\{1,2,4,...2^{n-1},2^{n}\}$ in a cyclic manner.

If $N=2^{t}$ , where $1\leq t\leq n$ , then $g_{t}=a^{(2^{n}-1)2^{n-t}}$ .

### How to choose *K* for a specific *N*

The following formula is helpful, finding a proper K (number of groups to divide N bits into) given bit size N by calculating efficiency :

$E={\frac {{\frac {2N}{K}}+k}{n}}$ N is bit size (the one used in $2^{N}+1$ ) at outermost level. K gives ${\frac {N}{K}}$ groups of bits, where $K=2^{k}$ .

n is found through N, K and k by finding the smallest x, such that $2N/K+k\leq n=K2^{x}$

If one assume efficiency above 50%, ${\frac {n}{2}}\leq {\frac {2N}{K}},K\leq n$ and k is very small compared to rest of formula; one get

$K\leq 2{\sqrt {N}}$

This means: When something is very effective; K is bound above by $2{\sqrt {N}}$ or asymptotically bound above by ${\sqrt {N}}$

### Pseudocode

Following algorithm, the standard Modular Schönhage-Strassen Multiplication algorithm (with some optimizations), is found in overview through

1. Split both input numbers a and b into n coefficients of s bits each. Use at least ⁠ $K+1$ ⁠ bits to store them, to allow encoding of the value ⁠ $2^{K}.$ ⁠
2. Weight both coefficient vectors according to (2.24) with powers of θ by performing cyclic shifts on them.
3. Shuffle the coefficients ⁠ $a_{i}$ ⁠ and ⁠ $b_{j}$ ⁠ .
4. Evaluate ⁠ $a_{i}$ ⁠ and ⁠ $b_{j}$ ⁠ . Multiplications by powers of ω are cyclic shifts.
5. Do n pointwise multiplications ⁠ $c_{k}:=a_{k}b_{k}$ ⁠ in ⁠ $Z/(2^{K}+1)Z$ ⁠. If SMUL is used recursively, provide K as parameter. Otherwise, use some other multiplication function like T3MUL and reduce modulo ⁠ $2^{K}+1$ ⁠ afterwards.
6. Shuffle the product coefficients ⁠ $c_{k}$ ⁠.
7. Evaluate the product coefficients ⁠ $c_{k}$ ⁠.
8. Apply the counterweights to the ⁠ $c_{k}$ ⁠ according to (2.25). Since ⁠ $\theta ^{2n}\equiv 1$ ⁠ it follows that ⁠ $\theta ^{-k}\equiv \theta ^{n-k}$ ⁠
9. Normalize the ⁠ $c_{k}$ ⁠ with ⁠ $1/n\equiv 2^{-m}$ ⁠ (again a cyclic shift).
10. Add up the ⁠ $c_{k}$ ⁠ and propagate the carries. Make sure to properly handle negative coefficients.
11. Do a reduction modulo ⁠ $2^{N}+1$ ⁠.

- T3MUL = Toom–Cook multiplication
- SMUL = Schönhage–Strassen multiplication
- Evaluate = FFT/IFFT

### Further study

For implementation details, one can read the book *Prime Numbers: A Computational Perspective*. This variant differs somewhat from Schönhage's original method in that it exploits the discrete weighted transform to perform negacyclic convolutions more efficiently. Another source for detailed information is Knuth's *The Art of Computer Programming*.

## Optimizations

This section explains a number of important practical optimizations, when implementing Schönhage–Strassen.

### Use of other multiplications algorithm, inside algorithm

Below a certain cutoff point, it's more efficient to use other multiplication algorithms, such as Toom–Cook multiplication.

### Square root of 2 trick

The idea is to use ${\sqrt {2}}$ as a root of unity of order $2^{n+2}$ in finite field $\mathrm {GF} (2^{n+2}+1)$ (it is a solution to equation $\theta ^{2^{n+2}}\equiv 1{\pmod {2^{n+2}+1}}$ ), when weighting values in NTT (number theoretic transformation) approach. It has been shown to save 10% in integer multiplication time.

### Granlund's trick

By letting $m=N+h$ , one can compute $uv{\bmod {2^{N}+1}}$ and $(u{\bmod {2^{h}}})(v{\bmod {2}}^{h})$ in combination with CRT (Chinese Remainder Theorem) to find exact values of multiplication uv.
