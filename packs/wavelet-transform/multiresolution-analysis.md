---
title: "Multiresolution analysis"
source: https://en.wikipedia.org/wiki/Multiresolution_analysis
domain: wavelet-transform
license: CC-BY-SA-4.0
tags: wavelet transform, discrete wavelet transform, haar wavelet, multiresolution analysis
fetched: 2026-07-02
---

# Multiresolution analysis

A **multiresolution analysis** (**MRA**) or **multiscale approximation** (**MSA**) is the design method of most of the practically relevant discrete wavelet transforms (DWT) and the justification for the algorithm of the fast wavelet transform (FWT). It was introduced in this context in 1988/89 by Stephane Mallat and Yves Meyer and has predecessors in the microlocal analysis in the theory of differential equations (the *ironing method*) and the pyramid methods of image processing as introduced in 1981/83 by Peter J. Burt, Edward H. Adelson and James L. Crowley.

## Definition

A multiresolution analysis of the Lebesgue space $L^{2}(\mathbb {R} )$ consists of a sequence of nested subspaces

$\{0\}\subset \dots \subset V_{1}\subset V_{0}\subset V_{-1}\subset \dots \subset V_{-n}\subset V_{-(n+1)}\subset \dots \subset L^{2}(\mathbb {R} )$

that satisfies certain self-similarity relations in time-space and scale-frequency, as well as completeness and regularity relations.

- *Self-similarity* in *time* demands that each subspace *Vk* is invariant under shifts by integer multiples of *2k*. That is, for each $f\in V_{k},\;m\in \mathbb {Z}$ the function *g* defined as $g(x)=f(x-m2^{k})$ also contained in $V_{k}$ .
- *Self-similarity* in *scale* demands that all subspaces $V_{k}\subset V_{l},\;k>l,$ are time-scaled versions of each other, with scaling respectively dilation factor 2*k-l*. I.e., for each $f\in V_{k}$ there is a $g\in V_{l}$ with $\forall x\in \mathbb {R$ .
- In the sequence of subspaces, for *k*>*l* the space resolution 2*l* of the *l*-th subspace is higher than the resolution 2*k* of the *k*-th subspace.
- *Regularity* demands that the model subspace *V0* be generated as the linear hull (algebraically or even topologically closed) of the integer shifts of one or a finite number of generating functions $\phi$ or $\phi _{1},\dots ,\phi _{r}$ . Those integer shifts should at least form a frame for the subspace $V_{0}\subset L^{2}(\mathbb {R} )$ , which imposes certain conditions on the decay at infinity. The generating functions are also known as **scaling functions** or **father wavelets**. In most cases one demands of those functions to be piecewise continuous with compact support.
- *Completeness* demands that those nested subspaces fill the whole space, i.e., their union should be dense in $L^{2}(\mathbb {R} )$ , and that they are not too redundant, i.e., their intersection should only contain the zero element.

## Important conclusions

In the case of one continuous (or at least with bounded variation) compactly supported scaling function with orthogonal shifts, one may make a number of deductions. The proof of existence of this class of functions is due to Ingrid Daubechies.

Assuming the scaling function has compact support, then $V_{0}\subset V_{-1}$ implies that there is a finite sequence of coefficients $a_{k}=2\langle \phi (x),\phi (2x-k)\rangle$ for $|k|\leq N$ , and $a_{k}=0$ for $|k|>N$ , such that

$\phi (x)=\sum _{k=-N}^{N}a_{k}\phi (2x-k).$

Defining another function, known as **mother wavelet** or just **the wavelet**

$\psi (x):=\sum _{k=-N}^{N}(-1)^{k}a_{1-k}\phi (2x-k),$

one can show that the space $W_{0}\subset V_{-1}$ , which is defined as the (closed) linear hull of the mother wavelet's integer shifts, is the orthogonal complement to $V_{0}$ inside $V_{-1}$ . Or put differently, $V_{-1}$ is the orthogonal sum (denoted by $\oplus$ ) of $W_{0}$ and $V_{0}$ . By self-similarity, there are scaled versions $W_{k}$ of $W_{0}$ and by completeness one has

$L^{2}(\mathbb {R} )={\mbox{closure of }}\bigoplus _{k\in \mathbb {Z} }W_{k},$

thus the set

$\{\psi _{k,n}(x)={\sqrt {2}}^{-k}\psi (2^{-k}x-n):\;k,n\in \mathbb {Z} \}$

is a countable complete orthonormal wavelet basis in $L^{2}(\mathbb {R} )$ .
