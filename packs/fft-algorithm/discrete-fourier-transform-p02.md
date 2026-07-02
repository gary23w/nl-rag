---
title: "Discrete Fourier transform (part 2/2)"
source: https://en.wikipedia.org/wiki/Discrete_Fourier_transform
domain: fft-algorithm
license: CC-BY-SA-4.0
tags: fast fourier transform, cooley tukey algorithm, discrete fourier transform, convolution theorem
fetched: 2026-07-02
part: 2/2
---

## Generalizations

### Representation theory

The DFT can be interpreted as a complex-valued representation of the finite cyclic group. In other words, a sequence of n complex numbers can be thought of as an element of n -dimensional complex space $\mathbb {C} ^{n}$ or equivalently a function f from the finite cyclic group of order n to the complex numbers, $\mathbb {Z} _{n}\mapsto \mathbb {C}$ . So f is a class function on the finite cyclic group, and thus can be expressed as a linear combination of the irreducible characters of this group, which are the roots of unity.

From this point of view, one may generalize the DFT to representation theory generally, or more narrowly to the representation theory of finite groups.

More narrowly still, one may generalize the DFT by either changing the target (taking values in a field other than the complex numbers), or the domain (a group other than a finite cyclic group), as detailed in the sequel.

### Other fields

Many of the properties of the DFT only depend on the fact that $e^{-{\frac {i2\pi }{N}}}$ is a primitive root of unity, sometimes denoted $\omega _{N}$ or $W_{N}$ (so that $\omega _{N}^{N}=1$ ). Such properties include the completeness, orthogonality, Plancherel/Parseval, periodicity, shift, convolution, and unitarity properties above, as well as many FFT algorithms. For this reason, the discrete Fourier transform can be defined by using roots of unity in fields other than the complex numbers, and such generalizations are commonly called *number-theoretic transforms* (NTTs) in the case of finite fields. For more information, see number-theoretic transform and discrete Fourier transform (general).

### Other finite groups

The standard DFT acts on a sequence *x*0, *x*1, ..., *x**N*−1 of complex numbers, which can be viewed as a function {0, 1, ..., *N* − 1} → **C**. The multidimensional DFT acts on multidimensional sequences, which can be viewed as functions

$\{0,1,\ldots ,N_{1}-1\}\times \cdots \times \{0,1,\ldots ,N_{d}-1\}\to \mathbb {C} .$

This suggests the generalization to Fourier transforms on arbitrary finite groups, which act on functions *G* → **C** where *G* is a finite group. In this framework, the standard DFT is seen as the Fourier transform on a cyclic group, while the multidimensional DFT is a Fourier transform on a direct sum of cyclic groups.

Further, Fourier transform can be on cosets of a group.


## Alternatives

There are various alternatives to the DFT for various applications, prominent among which are wavelets. The analog of the DFT is the discrete wavelet transform (DWT). From the point of view of time–frequency analysis, a key limitation of the Fourier transform is that it does not include *location* information, only *frequency* information, and thus has difficulty in representing transients. As wavelets have location as well as frequency, they are better able to represent location, at the expense of greater difficulty representing frequency. For details, see comparison of the discrete wavelet transform with the discrete Fourier transform.
