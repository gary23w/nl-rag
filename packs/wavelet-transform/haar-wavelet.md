---
title: "Haar wavelet"
source: https://en.wikipedia.org/wiki/Haar_wavelet
domain: wavelet-transform
license: CC-BY-SA-4.0
tags: wavelet transform, discrete wavelet transform, haar wavelet, multiresolution analysis
fetched: 2026-07-02
---

# Haar wavelet

In mathematics, the **Haar wavelet** is a sequence of rescaled "square-shaped" functions which together form a wavelet family or basis. Wavelet analysis is similar to Fourier analysis in that it allows a target function over an interval to be represented in terms of an orthonormal basis. The Haar sequence is now recognised as the first known wavelet basis and is extensively used as a teaching example.

The **Haar sequence** was proposed in 1909 by Alfréd Haar. Haar used these functions to give an example of an orthonormal system for the space of square-integrable functions on the unit interval [0, 1]. The study of wavelets, and even the term "wavelet", did not come until much later. As a special case of the Daubechies wavelet, the Haar wavelet is also known as **Db1**.

The Haar wavelet is also the simplest possible wavelet. The technical disadvantage of the Haar wavelet is that it is not continuous, and therefore not differentiable. This property can, however, be an advantage for the analysis of signals with sudden transitions (discrete signals), such as monitoring of tool failure in machines.

The Haar wavelet's mother wavelet function $\psi (t)$ can be described as

$\psi (t)={\begin{cases}1\quad &0\leq t<{\frac {1}{2}},\\-1&{\frac {1}{2}}\leq t<1,\\0&{\mbox{otherwise.}}\end{cases}}$

Its scaling function $\varphi (t)$ can be described as

$\varphi (t)={\begin{cases}1\quad &0\leq t<1,\\0&{\mbox{otherwise.}}\end{cases}}$

## Haar functions and Haar system

For every pair *n*, *k* of integers in $\mathbb {Z}$ , the **Haar function** *ψ**n*,*k* is defined on the real line $\mathbb {R}$ by the formula

$\psi _{n,k}(t)=2^{n/2}\psi (2^{n}t-k),\quad t\in \mathbb {R} .$

This function is supported on the right-open interval *I**n*,*k* = [ *k*2−*n*, (*k*+1)2−*n*), *i.e.*, it vanishes outside that interval. It has integral 0 and norm 1 in the Hilbert space *L*2( $\mathbb {R}$ ),

$\int _{\mathbb {R} }\psi _{n,k}(t)\,dt=0,\quad \|\psi _{n,k}\|_{L^{2}(\mathbb {R} )}^{2}=\int _{\mathbb {R} }\psi _{n,k}(t)^{2}\,dt=1.$

The Haar functions are pairwise orthogonal,

$\int _{\mathbb {R} }\psi _{n_{1},k_{1}}(t)\psi _{n_{2},k_{2}}(t)\,dt=\delta _{n_{1}n_{2}}\delta _{k_{1}k_{2}},$

where $\delta _{ij}$ represents the Kronecker delta. Here is the reason for orthogonality: when the two supporting intervals $I_{n_{1},k_{1}}$ and $I_{n_{2},k_{2}}$ are not equal, then they are either disjoint, or else the smaller of the two supports, say $I_{n_{1},k_{1}}$ , is contained in the lower or in the upper half of the other interval, on which the function $\psi _{n_{2},k_{2}}$ remains constant. It follows in this case that the product of these two Haar functions is a multiple of the first Haar function, hence the product has integral 0.

The **Haar system** on the real line is the set of functions

$\{\psi _{n,k}(t)\;:\;n\in \mathbb {Z} ,\;k\in \mathbb {Z} \}.$

It is complete in *L*2( $\mathbb {R}$ ): *The Haar system on the line is an orthonormal basis in* *L*2( $\mathbb {R}$ ).

## Haar wavelet properties

The Haar wavelet has several notable properties:

1. Any continuous real function with compact support can be approximated uniformly by linear combinations of $\varphi (t),\varphi (2t),\varphi (4t),\dots ,\varphi (2^{n}t),\dots$ and their shifted functions. This extends to those function spaces where any function therein can be approximated by continuous functions.
2. Any continuous real function on [0, 1] can be approximated uniformly on [0, 1] by linear combinations of the constant function **1**, $\psi (t),\psi (2t),\psi (4t),\dots ,\psi (2^{n}t),\dots$ and their shifted functions.
3. Orthogonality in the form $\int _{-\infty }^{\infty }2^{(n+n_{1})/2}\psi (2^{n}t-k)\psi (2^{n_{1}}t-k_{1})\,dt=\delta _{nn_{1}}\delta _{kk_{1}}.$ Here, $\delta _{ij}$ represents the Kronecker delta. The dual function of ψ(*t*) is ψ(*t*) itself.
4. Wavelet/scaling functions with different scale *n* have a functional relationship: since ${\begin{aligned}\varphi (t)&=\varphi (2t)+\varphi (2t-1)\\[.2em]\psi (t)&=\varphi (2t)-\varphi (2t-1),\end{aligned}}$ it follows that coefficients of scale *n* can be calculated by coefficients of scale *n+1*: If $\chi _{w}(k,n)=2^{n/2}\int _{-\infty }^{\infty }x(t)\varphi (2^{n}t-k)\,dt$ and $\mathrm {X} _{w}(k,n)=2^{n/2}\int _{-\infty }^{\infty }x(t)\psi (2^{n}t-k)\,dt$ then $\chi _{w}(k,n)=2^{-1/2}{\bigl (}\chi _{w}(2k,n+1)+\chi _{w}(2k+1,n+1){\bigr )}$ $\mathrm {X} _{w}(k,n)=2^{-1/2}{\bigl (}\chi _{w}(2k,n+1)-\chi _{w}(2k+1,n+1){\bigr )}.$

In this section, the discussion is restricted to the unit interval [0, 1] and to the Haar functions that are supported on [0, 1]. The system of functions considered by Haar in 1910, called the **Haar system on [0, 1]** in this article, consists of the subset of Haar wavelets defined as

$\{t\in [0,1]\mapsto \psi _{n,k}(t)\;:\;n,k\in \mathbb {N} \cup \{0\},\;0\leq k<2^{n}\},$

with the addition of the constant function **1** on [0, 1].

In Hilbert space terms, this Haar system on [0, 1] is a complete orthonormal system, *i.e.*, an orthonormal basis, for the space *L*2([0, 1]) of square integrable functions on the unit interval.

The Haar system on [0, 1] —with the constant function **1** as first element, followed with the Haar functions ordered according to the lexicographic ordering of couples (*n*, *k*)— is further a monotone Schauder basis for the space *L**p*([0, 1]) when 1 ≤ *p* < ∞. This basis is unconditional when 1 < *p* < ∞.

There is a related Rademacher system consisting of sums of Haar functions,

$r_{n}(t)=2^{-n/2}\sum _{k=0}^{2^{n}-1}\psi _{n,k}(t),\quad t\in [0,1],\ n\geq 0.$

Notice that |*r**n*(*t*)| = 1 on [0, 1). This is an orthonormal system but it is not complete. In the language of probability theory, the Rademacher sequence is an instance of a sequence of independent Bernoulli random variables with mean 0. The Khintchine inequality expresses the fact that in all the spaces *L**p*([0, 1]), 1 ≤ *p* < ∞, the Rademacher sequence is equivalent to the unit vector basis in ℓ*2*. In particular, the closed linear span of the Rademacher sequence in *L**p*([0, 1]), 1 ≤ *p* < ∞, is isomorphic to ℓ*2*.

### The Faber–Schauder system

The **Faber–Schauder system** is the family of continuous functions on [0, 1] consisting of the constant function **1**, and of multiples of indefinite integrals of the functions in the Haar system on [0, 1], chosen to have norm 1 in the maximum norm. This system begins with *s*0 = **1**, then *s*1(*t*) = *t* is the indefinite integral vanishing at 0 of the function **1**, first element of the Haar system on [0, 1]. Next, for every integer *n* ≥ 0, functions *s**n*,*k* are defined by the formula

$s_{n,k}(t)=2^{1+n/2}\int _{0}^{t}\psi _{n,k}(u)\,du,\quad t\in [0,1],\ 0\leq k<2^{n}.$

These functions *s**n*,*k* are continuous, piecewise linear, supported by the interval *I**n*,*k* that also supports ψ*n*,*k*. The function *s**n*,*k* is equal to 1 at the midpoint *x**n*,*k* of the interval  *I**n*,*k*, linear on both halves of that interval. It takes values between 0 and 1 everywhere.

The Faber–Schauder system is a Schauder basis for the space *C*([0, 1]) of continuous functions on [0, 1]. For every *f* in *C*([0, 1]), the partial sum

$f_{n+1}=a_{0}s_{0}+a_{1}s_{1}+\sum _{m=0}^{n-1}{\Bigl (}\sum _{k=0}^{2^{m}-1}a_{m,k}s_{m,k}{\Bigr )}\in C([0,1])$

of the series expansion of *f* in the Faber–Schauder system is the continuous piecewise linear function that agrees with *f* at the 2*n* + 1 points *k*2−*n*, where 0 ≤ *k* ≤ 2*n*. Next, the formula

$f_{n+2}-f_{n+1}=\sum _{k=0}^{2^{n}-1}{\bigl (}f(x_{n,k})-f_{n+1}(x_{n,k}){\bigr )}s_{n,k}=\sum _{k=0}^{2^{n}-1}a_{n,k}s_{n,k}$

gives a way to compute the expansion of *f* step by step. Since *f* is uniformly continuous, the sequence {*f**n*} converges uniformly to *f*. It follows that the Faber–Schauder series expansion of *f* converges in *C*([0, 1]), and the sum of this series is equal to *f*.

### The Franklin system

The **Franklin system** is obtained from the Faber–Schauder system by the Gram–Schmidt orthonormalization procedure. Since the Franklin system has the same linear span as that of the Faber–Schauder system, this span is dense in *C*([0, 1]), hence in *L*2([0, 1]). The Franklin system is therefore an orthonormal basis for *L*2([0, 1]), consisting of continuous piecewise linear functions. P. Franklin proved in 1928 that this system is a Schauder basis for *C*([0, 1]). The Franklin system is also an unconditional Schauder basis for the space *L**p*([0, 1]) when 1 < *p* < ∞. The Franklin system provides a Schauder basis in the disk algebra *A*(*D*). This was proved in 1974 by Bočkarev, after the existence of a basis for the disk algebra had remained open for more than forty years.

Bočkarev's construction of a Schauder basis in *A*(*D*) goes as follows: let *f* be a complex valued Lipschitz function on [0, π]; then *f* is the sum of a cosine series with absolutely summable coefficients. Let *T*(*f*) be the element of *A*(*D*) defined by the complex power series with the same coefficients,

$\left\{f:x\in [0,\pi ]\rightarrow \sum _{n=0}^{\infty }a_{n}\cos(nx)\right\}\longrightarrow \left\{T(f):z\rightarrow \sum _{n=0}^{\infty }a_{n}z^{n},\quad |z|\leq 1\right\}.$

Bočkarev's basis for *A*(*D*) is formed by the images under *T* of the functions in the Franklin system on [0, π]. Bočkarev's equivalent description for the mapping *T* starts by extending *f* to an even Lipschitz function *g*1 on [−π, π], identified with a Lipschitz function on the unit circle **T**. Next, let *g*2 be the conjugate function of *g*1, and define *T*(*f*) to be the function in *A*(*D*) whose value on the boundary **T** of *D* is equal to *g*1 + i*g*2.

When dealing with 1-periodic continuous functions, or rather with continuous functions *f* on [0, 1] such that *f*(0) = *f*(1), one removes the function *s*1(*t*) = *t* from the Faber–Schauder system, in order to obtain the **periodic Faber–Schauder system**. The **periodic Franklin system** is obtained by orthonormalization from the periodic Faber–-Schauder system. One can prove Bočkarev's result on *A*(*D*) by proving that the periodic Franklin system on [0, 2π] is a basis for a Banach space *A**r* isomorphic to *A*(*D*). The space *A**r* consists of complex continuous functions on the unit circle **T** whose conjugate function is also continuous.

## Haar matrix

The 2×2 Haar matrix that is associated with the Haar wavelet is

$H_{2}={\begin{bmatrix}1&1\\1&-1\end{bmatrix}}.$

Using the discrete wavelet transform, one can transform any sequence $(a_{0},a_{1},\dots ,a_{2n},a_{2n+1})$ of even length into a sequence of two-component-vectors $\left(\left(a_{0},a_{1}\right),\left(a_{2},a_{3}\right),\dots ,\left(a_{2n},a_{2n+1}\right)\right)$ . If one right-multiplies each vector with the matrix $H_{2}$ , one gets the result $\left(\left(s_{0},d_{0}\right),\dots ,\left(s_{n},d_{n}\right)\right)$ of one stage of the fast Haar-wavelet transform. Usually one separates the sequences *s* and *d* and continues with transforming the sequence *s*. Sequence *s* is often referred to as the *averages* part, whereas *d* is known as the *details* part.

If one has a sequence of length a multiple of four, one can build blocks of 4 elements and transform them in a similar manner with the 4×4 Haar matrix

$H_{4}={\begin{bmatrix}1&1&1&1\\1&1&-1&-1\\1&-1&0&0\\0&0&1&-1\end{bmatrix}},$

which combines two stages of the fast Haar-wavelet transform.

Compare with a Walsh matrix, which is a non-localized 1/–1 matrix.

Generally, the 2N×2N Haar matrix can be derived by the following equation.

$H_{2N}={\begin{bmatrix}H_{N}\otimes [1,1]\\I_{N}\otimes [1,-1]\end{bmatrix}}$

where

$I_{N}={\begin{bmatrix}1&0&\dots &0\\0&1&\dots &0\\\vdots &\vdots &\ddots &\vdots \\0&0&\dots &1\end{bmatrix}}$

and

$\otimes$

is the

Kronecker product

.

The Kronecker product of $A\otimes B$ , where A is an m×n matrix and B is a p×q matrix, is expressed as

$A\otimes B={\begin{bmatrix}a_{11}B&\dots &a_{1n}B\\\vdots &\ddots &\vdots \\a_{m1}B&\dots &a_{mn}B\end{bmatrix}}.$

An un-normalized 8-point Haar matrix $H_{8}$ is shown below

$H_{8}={\begin{bmatrix}1&1&1&1&1&1&1&1\\1&1&1&1&-1&-1&-1&-1\\1&1&-1&-1&0&0&0&0&\\0&0&0&0&1&1&-1&-1\\1&-1&0&0&0&0&0&0&\\0&0&1&-1&0&0&0&0\\0&0&0&0&1&-1&0&0&\\0&0&0&0&0&0&1&-1\end{bmatrix}}.$

Note that, the above matrix is an un-normalized Haar matrix. The Haar matrix required by the Haar transform should be normalized.

From the definition of the Haar matrix H , one can observe that, unlike the Fourier transform, H has only real elements (i.e., 1, -1 or 0) and is non-symmetric.

Take the 8-point Haar matrix $H_{8}$ as an example. The first row of $H_{8}$ measures the average value, and the second row of $H_{8}$ measures a low frequency component of the input vector. The next two rows are sensitive to the first and second half of the input vector respectively, which corresponds to moderate frequency components. The remaining four rows are sensitive to the four section of the input vector, which corresponds to high frequency components.

## Haar transform

The **Haar transform** is the simplest of the wavelet transforms. This transform cross-multiplies a function against the Haar wavelet with various shifts and stretches, like the Fourier transform cross-multiplies a function against a sine wave with two phases and many stretches.

### Introduction

The Haar transform is one of the oldest transform functions, proposed in 1910 by the Hungarian mathematician Alfréd Haar. It is found effective in applications such as signal and image compression in electrical and computer engineering as it provides a simple and computationally efficient approach for analysing the local aspects of a signal.

The Haar transform is derived from the Haar matrix. An example of a 4×4 Haar transformation matrix is shown below.

$H_{4}={\frac {1}{2}}{\begin{bmatrix}1&1&1&1\\1&1&-1&-1\\{\sqrt {2}}&-{\sqrt {2}}&0&0\\0&0&{\sqrt {2}}&-{\sqrt {2}}\end{bmatrix}}$

The Haar transform can be thought of as a sampling process in which rows of the transformation matrix act as samples of finer and finer resolution.

Compare with the Walsh transform, which is also 1/–1, but is non-localized.

### Property

The Haar transform has the following properties

1. No need for multiplications. It requires only additions and there are many elements with zero value in the Haar matrix, so the computation time is short. It is faster than Walsh transform, whose matrix is composed of +1 and −1.
2. Input and output length are the same. However, the length should be a power of 2, i.e. $N=2^{k},k\in \mathbb {N}$ .
3. It can be used to analyse the localized feature of signals. Due to the orthogonal property of the Haar function, the frequency components of input signal can be analyzed.

### Haar transform and Inverse Haar transform

The Haar transform *y**n* of an n-input function *x**n* is

$y_{n}=H_{n}x_{n}$

The Haar transform matrix is real and orthogonal. Thus, the inverse Haar transform can be derived by the following equations.

$H=H^{*},H^{-1}=H^{T},{\text{ i.e. }}HH^{T}=I$

where

I

is the

identity matrix

. For example, when n = 4

$H_{4}^{T}H_{4}={\frac {1}{2}}{\begin{bmatrix}1&1&{\sqrt {2}}&0\\1&1&-{\sqrt {2}}&0\\1&-1&0&{\sqrt {2}}\\1&-1&0&-{\sqrt {2}}\end{bmatrix}}\cdot \;{\frac {1}{2}}{\begin{bmatrix}1&1&1&1\\1&1&-1&-1\\{\sqrt {2}}&-{\sqrt {2}}&0&0\\0&0&{\sqrt {2}}&-{\sqrt {2}}\end{bmatrix}}={\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&1&0\\0&0&0&1\end{bmatrix}}$

Thus, the inverse Haar transform is

$x_{n}=H^{T}y_{n}$

### Example

The Haar transform coefficients of a n=4-point signal $x_{4}=[1,2,3,4]^{T}$ can be found as

$y_{4}=H_{4}x_{4}={\frac {1}{2}}{\begin{bmatrix}1&1&1&1\\1&1&-1&-1\\{\sqrt {2}}&-{\sqrt {2}}&0&0\\0&0&{\sqrt {2}}&-{\sqrt {2}}\end{bmatrix}}{\begin{bmatrix}1\\2\\3\\4\end{bmatrix}}={\begin{bmatrix}5\\-2\\-1/{\sqrt {2}}\\-1/{\sqrt {2}}\end{bmatrix}}$

The input signal can then be perfectly reconstructed by the inverse Haar transform

${\hat {x_{4}}}=H_{4}^{T}y_{4}={\frac {1}{2}}{\begin{bmatrix}1&1&{\sqrt {2}}&0\\1&1&-{\sqrt {2}}&0\\1&-1&0&{\sqrt {2}}\\1&-1&0&-{\sqrt {2}}\end{bmatrix}}{\begin{bmatrix}5\\-2\\-1/{\sqrt {2}}\\-1/{\sqrt {2}}\end{bmatrix}}={\begin{bmatrix}1\\2\\3\\4\end{bmatrix}}$
