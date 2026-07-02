---
title: "Discrete Fourier transform (part 3/3)"
source: https://en.wikipedia.org/wiki/Discrete_Fourier_transform
domain: dsp
license: CC-BY-SA-4.0
tags: dsp, digital signal processing, fft, fourier transform, digital filter, sampling rate
fetched: 2026-07-02
part: 3/3
---

## Multidimensional DFT

The ordinary DFT transforms a one-dimensional sequence or array x n {\displaystyle x_{n}} ({\displaystyle x_{n}}) that is a function of exactly one discrete variable *n*. The multidimensional DFT of a multidimensional array x n 1 , n 2 , … , n d {\displaystyle x_{n_{1},n_{2},\dots ,n_{d}}} ({\displaystyle x_{n_{1},n_{2},\dots ,n_{d}}}) that is a function of *d* discrete variables n ℓ = 0 , 1 , … , N ℓ − 1 {\displaystyle n_{\ell }=0,1,\dots ,N_{\ell }-1} ({\displaystyle n_{\ell }=0,1,\dots ,N_{\ell }-1}) for ℓ {\displaystyle \ell } ({\displaystyle \ell }) in 1 , 2 , … , d {\displaystyle 1,2,\dots ,d} ({\displaystyle 1,2,\dots ,d}) is defined by:

X

k

1

,

k

2

,

…

,

k

d

=

∑

n

1

=

0

N

1

−

1

(

ω

N

1

k

1

n

1

∑

n

2

=

0

N

2

−

1

(

ω

N

2

k

2

n

2

⋯

∑

n

d

=

0

N

d

−

1

ω

N

d

k

d

n

d

⋅

x

n

1

,

n

2

,

…

,

n

d

)

)

,

{\displaystyle X_{k_{1},k_{2},\dots ,k_{d}}=\sum _{n_{1}=0}^{N_{1}-1}\left(\omega _{N_{1}}^{~k_{1}n_{1}}\sum _{n_{2}=0}^{N_{2}-1}\left(\omega _{N_{2}}^{~k_{2}n_{2}}\cdots \sum _{n_{d}=0}^{N_{d}-1}\omega _{N_{d}}^{~k_{d}n_{d}}\cdot x_{n_{1},n_{2},\dots ,n_{d}}\right)\right),}

where ω N ℓ = exp ⁡ ( − i 2 π / N ℓ ) {\displaystyle \omega _{N_{\ell }}=\exp(-i2\pi /N_{\ell })} ({\displaystyle \omega _{N_{\ell }}=\exp(-i2\pi /N_{\ell })}) as above and the *d* output indices run from k ℓ = 0 , 1 , … , N ℓ − 1 {\displaystyle k_{\ell }=0,1,\dots ,N_{\ell }-1} ({\displaystyle k_{\ell }=0,1,\dots ,N_{\ell }-1}). This is more compactly expressed in vector notation, where we define n = ( n 1 , n 2 , … , n d ) {\displaystyle \mathbf {n} =(n_{1},n_{2},\dots ,n_{d})} ({\displaystyle \mathbf {n} =(n_{1},n_{2},\dots ,n_{d})}) and k = ( k 1 , k 2 , … , k d ) {\displaystyle \mathbf {k} =(k_{1},k_{2},\dots ,k_{d})} ({\displaystyle \mathbf {k} =(k_{1},k_{2},\dots ,k_{d})}) as *d*-dimensional vectors of indices from 0 to N − 1 {\displaystyle \mathbf {N} -1} ({\displaystyle \mathbf {N} -1}), which we define as N − 1 = ( N 1 − 1 , N 2 − 1 , … , N d − 1 ) {\displaystyle \mathbf {N} -1=(N_{1}-1,N_{2}-1,\dots ,N_{d}-1)} ({\displaystyle \mathbf {N} -1=(N_{1}-1,N_{2}-1,\dots ,N_{d}-1)}):

X

k

=

∑

n

=

0

N

−

1

e

−

i

2

π

k

⋅

(

n

/

N

)

x

n

,

{\displaystyle X_{\mathbf {k} }=\sum _{\mathbf {n} =\mathbf {0} }^{\mathbf {N} -1}e^{-i2\pi \mathbf {k} \cdot (\mathbf {n} /\mathbf {N} )}x_{\mathbf {n} }\,,}

where the division n / N {\displaystyle \mathbf {n} /\mathbf {N} } ({\displaystyle \mathbf {n} /\mathbf {N} }) is defined as n / N = ( n 1 / N 1 , … , n d / N d ) {\displaystyle \mathbf {n} /\mathbf {N} =(n_{1}/N_{1},\dots ,n_{d}/N_{d})} ({\displaystyle \mathbf {n} /\mathbf {N} =(n_{1}/N_{1},\dots ,n_{d}/N_{d})}) to be performed element-wise, and the sum denotes the set of nested summations above.

The inverse of the multi-dimensional DFT is, analogous to the one-dimensional case, given by:

x

n

=

1

∏

ℓ

=

1

d

N

ℓ

∑

k

=

0

N

−

1

e

i

2

π

n

⋅

(

k

/

N

)

X

k

.

{\displaystyle x_{\mathbf {n} }={\frac {1}{\prod _{\ell =1}^{d}N_{\ell }}}\sum _{\mathbf {k} =\mathbf {0} }^{\mathbf {N} -1}e^{i2\pi \mathbf {n} \cdot (\mathbf {k} /\mathbf {N} )}X_{\mathbf {k} }\,.}

As the one-dimensional DFT expresses the input x n {\displaystyle x_{n}} ({\displaystyle x_{n}}) as a superposition of sinusoids, the multidimensional DFT expresses the input as a superposition of plane waves, or multidimensional sinusoids. The direction of oscillation in space is k / N {\displaystyle \mathbf {k} /\mathbf {N} } ({\displaystyle \mathbf {k} /\mathbf {N} }). The amplitudes are X k {\displaystyle X_{\mathbf {k} }} ({\displaystyle X_{\mathbf {k} }}). This decomposition is of great importance for everything from digital image processing (two-dimensional) to solving partial differential equations. The solution is broken up into plane waves.

The multidimensional DFT can be computed by the composition of a sequence of one-dimensional DFTs along each dimension. In the two-dimensional case x n 1 , n 2 {\displaystyle x_{n_{1},n_{2}}} ({\displaystyle x_{n_{1},n_{2}}}) the N 1 {\displaystyle N_{1}} ({\displaystyle N_{1}}) independent DFTs of the rows (i.e., along n 2 {\displaystyle n_{2}} ({\displaystyle n_{2}})) are computed first to form a new array y n 1 , k 2 {\displaystyle y_{n_{1},k_{2}}} ({\displaystyle y_{n_{1},k_{2}}}). Then the N 2 {\displaystyle N_{2}} ({\displaystyle N_{2}}) independent DFTs of *y* along the columns (along n 1 {\displaystyle n_{1}} ({\displaystyle n_{1}})) are computed to form the final result X k 1 , k 2 {\displaystyle X_{k_{1},k_{2}}} ({\displaystyle X_{k_{1},k_{2}}}). Alternatively the columns can be computed first and then the rows. The order is immaterial because the nested summations above commute.

An algorithm to compute a one-dimensional DFT is thus sufficient to efficiently compute a multidimensional DFT. This approach is known as the *row-column* algorithm. There are also intrinsically multidimensional FFT algorithms.

### The real-input multidimensional DFT

For input data x n 1 , n 2 , … , n d {\displaystyle x_{n_{1},n_{2},\dots ,n_{d}}} ({\displaystyle x_{n_{1},n_{2},\dots ,n_{d}}}) consisting of real numbers, the DFT outputs have a conjugate symmetry similar to the one-dimensional case above:

X

k

1

,

k

2

,

…

,

k

d

=

X

N

1

−

k

1

,

N

2

−

k

2

,

…

,

N

d

−

k

d

∗

,

{\displaystyle X_{k_{1},k_{2},\dots ,k_{d}}=X_{N_{1}-k_{1},N_{2}-k_{2},\dots ,N_{d}-k_{d}}^{*},}

where the star again denotes complex conjugation and the ℓ {\displaystyle \ell } ({\displaystyle \ell })-th subscript is again interpreted modulo N ℓ {\displaystyle N_{\ell }} ({\displaystyle N_{\ell }}) (for ℓ = 1 , 2 , … , d {\displaystyle \ell =1,2,\ldots ,d} ({\displaystyle \ell =1,2,\ldots ,d})).


## Applications

The DFT has seen wide usage across a large number of fields; we only sketch a few examples below (see also the references at the end). All applications of the DFT depend crucially on the availability of a fast algorithm to compute discrete Fourier transforms and their inverses, a fast Fourier transform.

### Spectral analysis

When the DFT is used for signal spectral analysis, the { x n } {\displaystyle \{x_{n}\}} ({\displaystyle \{x_{n}\}}) sequence usually represents a finite set of uniformly spaced time-samples of some signal x ( t ) {\displaystyle x(t)\,} ({\displaystyle x(t)\,}), where t {\displaystyle t} ({\displaystyle t}) represents time. The conversion from continuous time to samples (discrete-time) changes the underlying Fourier transform of x ( t ) {\displaystyle x(t)} ({\displaystyle x(t)}) into a discrete-time Fourier transform (DTFT), which generally entails a type of distortion called aliasing. Choice of an appropriate sample-rate (see *Nyquist rate*) is the key to minimizing that distortion. Similarly, the conversion from a very long (or infinite) sequence to a manageable size entails a type of distortion called *leakage*, which is manifested as a loss of detail (a.k.a. resolution) in the DTFT. Choice of an appropriate sub-sequence length is the primary key to minimizing that effect. When the available data (and time to process it) is more than the amount needed to attain the desired frequency resolution, a standard technique is to perform multiple DFTs, for example to create a spectrogram. If the desired result is a power spectrum and noise or randomness is present in the data, averaging the magnitude components of the multiple DFTs is a useful procedure to reduce the variance of the spectrum (also called a periodogram in this context); two examples of such techniques are the Welch method and the Bartlett method; the general subject of estimating the power spectrum of a noisy signal is called spectral estimation.

A final source of distortion (or perhaps *illusion*) is the DFT itself, because it is just a discrete sampling of the DTFT, which is a function of a continuous frequency domain. That can be mitigated by increasing the resolution of the DFT. That procedure is illustrated at § Sampling the DTFT.

- The procedure is sometimes referred to as *zero-padding*, which is a particular implementation used in conjunction with the fast Fourier transform (FFT) algorithm. The inefficiency of performing multiplications and additions with zero-valued "samples" is more than offset by the inherent efficiency of the FFT.
- As already stated, leakage imposes a limit on the inherent resolution of the DTFT, so there is a practical limit to the benefit that can be obtained from a fine-grained DFT.

### Optics, diffraction, and tomography

The discrete Fourier transform is widely used with spatial frequencies in modeling the way that light, electrons, and other probes travel through optical systems and scatter from objects in two and three dimensions. The dual (direct/reciprocal) vector space of three dimensional objects further makes available a three dimensional reciprocal lattice, whose construction from translucent object shadows (via the Fourier slice theorem) allows tomographic reconstruction of three dimensional objects with a wide range of applications e.g. in modern medicine.

### Filter bank

See § FFT filter banks and § Sampling the DTFT.

### Data compression

The field of digital signal processing relies heavily on operations in the frequency domain (i.e. on the Fourier transform). For example, several lossy image and sound compression methods employ the discrete Fourier transform: the signal is cut into short segments, each is transformed, and then the Fourier coefficients of high frequencies, which are assumed to be unnoticeable, are discarded. The decompressor computes the inverse transform based on this reduced number of Fourier coefficients. (Compression applications often use a specialized form of the DFT, the discrete cosine transform or sometimes the modified discrete cosine transform.)

Some relatively recent compression algorithms, however, use wavelet transforms, which give a more uniform compromise between time and frequency domain than obtained by chopping data into segments and transforming each segment. In the case of JPEG2000, this avoids the spurious image features that appear when images are highly compressed with the original JPEG.

### Partial differential equations

Discrete Fourier transforms are often used to solve partial differential equations, where again the DFT is used as an approximation for the Fourier series (which is recovered in the limit of infinite *N*). The advantage of this approach is that it expands the signal in complex exponentials e i n x {\displaystyle e^{inx}} ({\displaystyle e^{inx}}), which are eigenfunctions of differentiation: d ( e i n x ) / d x = i n e i n x {\displaystyle {{\text{d}}{\big (}e^{inx}{\big )}}/{\text{d}}x=ine^{inx}} ({\displaystyle {{\text{d}}{\big (}e^{inx}{\big )}}/{\text{d}}x=ine^{inx}}). Thus, in the Fourier representation, differentiation is simple—we just multiply by i n {\displaystyle in} ({\displaystyle in}). (However, the choice of n {\displaystyle n} ({\displaystyle n}) is not unique due to aliasing; for the method to be convergent, a choice similar to that in the trigonometric interpolation section above should be used.) A linear differential equation with constant coefficients is transformed into an easily solvable algebraic equation. One then uses the inverse DFT to transform the result back into the ordinary spatial representation. Such an approach is called a spectral method.

### Polynomial multiplication

Suppose we wish to compute the polynomial product *c*(*x*) = *a*(*x*) · *b*(*x*). The ordinary product expression for the coefficients of *c* involves a linear (acyclic) convolution, where indices do not "wrap around." This can be rewritten as a cyclic convolution by taking the coefficient vectors for *a*(*x*) and *b*(*x*) with constant term first, then appending zeros so that the resultant coefficient vectors **a** and **b** have dimension *d* > deg(*a*(*x*)) + deg(*b*(*x*)). Then,

c

=

a

∗

b

{\displaystyle \mathbf {c} =\mathbf {a} *\mathbf {b} }

Where **c** is the vector of coefficients for *c*(*x*), and the convolution operator ∗ {\displaystyle *\,} ({\displaystyle *\,}) is defined so

c

n

=

∑

m

=

0

d

−

1

a

m

b

n

−

m

m

o

d

d

n

=

0

,

1

,

…

,

d

−

1

{\displaystyle c_{n}=\sum _{m=0}^{d-1}a_{m}b_{n-m\ \mathrm {mod} \ d}\qquad \qquad \qquad n=0,1,\dots ,d-1}

But convolution becomes multiplication under the DFT:

F

(

c

)

=

F

(

a

)

F

(

b

)

{\displaystyle {\mathcal {F}}(\mathbf {c} )={\mathcal {F}}(\mathbf {a} ){\mathcal {F}}(\mathbf {b} )}

Here the vector product is taken elementwise. Thus the coefficients of the product polynomial *c*(*x*) are just the terms 0, ..., deg(*a*(*x*)) + deg(*b*(*x*)) of the coefficient vector

c

=

F

−

1

(

F

(

a

)

F

(

b

)

)

.

{\displaystyle \mathbf {c} ={\mathcal {F}}^{-1}({\mathcal {F}}(\mathbf {a} ){\mathcal {F}}(\mathbf {b} )).}

With a fast Fourier transform, the resulting algorithm takes *O*(*N* log *N*) arithmetic operations. Due to its simplicity and speed, the Cooley–Tukey FFT algorithm, which is limited to composite sizes, is often chosen for the transform operation. In this case, *d* should be chosen as the smallest integer greater than the sum of the input polynomial degrees that is factorizable into small prime factors (e.g. 2, 3, and 5, depending upon the FFT implementation).

#### Multiplication of large integers

The fastest known algorithms for the multiplication of very large integers use the polynomial multiplication method outlined above. Integers can be treated as the value of a polynomial evaluated specifically at the number base, with the coefficients of the polynomial corresponding to the digits in that base (ex. 123 = 1 ⋅ 10 2 + 2 ⋅ 10 1 + 3 ⋅ 10 0 {\displaystyle 123=1\cdot 10^{2}+2\cdot 10^{1}+3\cdot 10^{0}} ({\displaystyle 123=1\cdot 10^{2}+2\cdot 10^{1}+3\cdot 10^{0}})). After polynomial multiplication, a relatively low-complexity carry-propagation step completes the multiplication.

#### Convolution

When data is convolved with a function with wide support, such as for downsampling by a large sampling ratio, because of the Convolution theorem and the FFT algorithm, it may be faster to transform it, multiply pointwise by the transform of the filter and then reverse transform it. Alternatively, a good filter is obtained by simply truncating the transformed data and re-transforming the shortened data set.


## Some discrete Fourier transform pairs

| x n = 1 N ∑ k = 0 N − 1 X k e i 2 π k n / N {\displaystyle x_{n}={\frac {1}{N}}\sum _{k=0}^{N-1}X_{k}e^{i2\pi kn/N}} ({\displaystyle x_{n}={\frac {1}{N}}\sum _{k=0}^{N-1}X_{k}e^{i2\pi kn/N}}) | X k = ∑ n = 0 N − 1 x n e − i 2 π k n / N {\displaystyle X_{k}=\sum _{n=0}^{N-1}x_{n}e^{-i2\pi kn/N}} ({\displaystyle X_{k}=\sum _{n=0}^{N-1}x_{n}e^{-i2\pi kn/N}}) | Note |
|---|---|---|
| x n e i 2 π n ℓ / N {\displaystyle x_{n}e^{i2\pi n\ell /N}\,} ({\displaystyle x_{n}e^{i2\pi n\ell /N}\,}) | X k − ℓ {\displaystyle X_{k-\ell }\,} ({\displaystyle X_{k-\ell }\,}) | Frequency shift theorem |
| x n − ℓ {\displaystyle x_{n-\ell }\,} ({\displaystyle x_{n-\ell }\,}) | X k e − i 2 π k ℓ / N {\displaystyle X_{k}e^{-i2\pi k\ell /N}\,} ({\displaystyle X_{k}e^{-i2\pi k\ell /N}\,}) | Time shift theorem |
| x n ∈ R {\displaystyle x_{n}\in \mathbb {R} } ({\displaystyle x_{n}\in \mathbb {R} }) | X k = X N − k ∗ {\displaystyle X_{k}=X_{N-k}^{*}\,} ({\displaystyle X_{k}=X_{N-k}^{*}\,}) | Real DFT |
| a n {\displaystyle a^{n}\,} ({\displaystyle a^{n}\,}) | { N if  a = e i 2 π k / N 1 − a N 1 − a e − i 2 π k / N otherwise {\displaystyle \left\{{\begin{matrix}N&{\mbox{if }}a=e^{i2\pi k/N}\\{\frac {1-a^{N}}{1-a\,e^{-i2\pi k/N}}}&{\mbox{otherwise}}\end{matrix}}\right.} ({\displaystyle \left\{{\begin{matrix}N&{\mbox{if }}a=e^{i2\pi k/N}\\{\frac {1-a^{N}}{1-a\,e^{-i2\pi k/N}}}&{\mbox{otherwise}}\end{matrix}}\right.}) | from the geometric progression formula |
| ( N − 1 n ) {\displaystyle {N-1 \choose n}\,} ({\displaystyle {N-1 \choose n}\,}) | ( 1 + e − i 2 π k / N ) N − 1 {\displaystyle \left(1+e^{-i2\pi k/N}\right)^{N-1}\,} ({\displaystyle \left(1+e^{-i2\pi k/N}\right)^{N-1}\,}) | from the binomial theorem |
| { 1 W if  2 n < W  or  2 ( N − n ) < W 0 otherwise {\displaystyle \left\{{\begin{matrix}{\frac {1}{W}}&{\mbox{if }}2n<W{\mbox{ or }}2(N-n)<W\\0&{\mbox{otherwise}}\end{matrix}}\right.} ({\displaystyle \left\{{\begin{matrix}{\frac {1}{W}}&{\mbox{if }}2n<W{\mbox{ or }}2(N-n)<W\\0&{\mbox{otherwise}}\end{matrix}}\right.}) | { 1 if  k = 0 sin ⁡ ( π W k N ) W sin ⁡ ( π k N ) otherwise {\displaystyle \left\{{\begin{matrix}1&{\mbox{if }}k=0\\{\frac {\sin \left({\frac {\pi Wk}{N}}\right)}{W\sin \left({\frac {\pi k}{N}}\right)}}&{\mbox{otherwise}}\end{matrix}}\right.} ({\displaystyle \left\{{\begin{matrix}1&{\mbox{if }}k=0\\{\frac {\sin \left({\frac {\pi Wk}{N}}\right)}{W\sin \left({\frac {\pi k}{N}}\right)}}&{\mbox{otherwise}}\end{matrix}}\right.}) | x n {\displaystyle x_{n}} ({\displaystyle x_{n}}) is a rectangular window function of *W* points centered on *n*=0, where *W* is an odd integer, and X k {\displaystyle X_{k}} ({\displaystyle X_{k}}) is a sinc-like function (specifically, X k {\displaystyle X_{k}} ({\displaystyle X_{k}}) is a Dirichlet kernel) |
| ∑ j ∈ Z exp ⁡ ( − π c N ⋅ ( n + N ⋅ j ) 2 ) {\displaystyle \sum _{j\in \mathbb {Z} }\exp \left(-{\frac {\pi }{cN}}\cdot (n+N\cdot j)^{2}\right)} ({\displaystyle \sum _{j\in \mathbb {Z} }\exp \left(-{\frac {\pi }{cN}}\cdot (n+N\cdot j)^{2}\right)}) | c N ⋅ ∑ j ∈ Z exp ⁡ ( − π c N ⋅ ( k + N ⋅ j ) 2 ) {\displaystyle {\sqrt {cN}}\cdot \sum _{j\in \mathbb {Z} }\exp \left(-{\frac {\pi c}{N}}\cdot (k+N\cdot j)^{2}\right)} ({\displaystyle {\sqrt {cN}}\cdot \sum _{j\in \mathbb {Z} }\exp \left(-{\frac {\pi c}{N}}\cdot (k+N\cdot j)^{2}\right)}) | Discretization and periodic summation of the scaled Gaussian functions for c > 0 {\displaystyle c>0} ({\displaystyle c>0}). Since either c {\displaystyle c} ({\displaystyle c}) or 1 c {\displaystyle {\frac {1}{c}}} ({\displaystyle {\frac {1}{c}}}) is larger than one and thus warrants fast convergence of one of the two series, for large c {\displaystyle c} ({\displaystyle c}) you may choose to compute the frequency spectrum and convert to the time domain using the discrete Fourier transform. |


## Generalizations

### Representation theory

The DFT can be interpreted as a complex-valued representation of the finite cyclic group. In other words, a sequence of n {\displaystyle n} ({\displaystyle n}) complex numbers can be thought of as an element of n {\displaystyle n} ({\displaystyle n})-dimensional complex space C n {\displaystyle \mathbb {C} ^{n}} ({\displaystyle \mathbb {C} ^{n}}) or equivalently a function f {\displaystyle f} ({\displaystyle f}) from the finite cyclic group of order n {\displaystyle n} ({\displaystyle n}) to the complex numbers, Z n ↦ C {\displaystyle \mathbb {Z} _{n}\mapsto \mathbb {C} } ({\displaystyle \mathbb {Z} _{n}\mapsto \mathbb {C} }). So f {\displaystyle f} ({\displaystyle f}) is a class function on the finite cyclic group, and thus can be expressed as a linear combination of the irreducible characters of this group, which are the roots of unity.

From this point of view, one may generalize the DFT to representation theory generally, or more narrowly to the representation theory of finite groups.

More narrowly still, one may generalize the DFT by either changing the target (taking values in a field other than the complex numbers), or the domain (a group other than a finite cyclic group), as detailed in the sequel.

### Other fields

Many of the properties of the DFT only depend on the fact that e − i 2 π N {\displaystyle e^{-{\frac {i2\pi }{N}}}} ({\displaystyle e^{-{\frac {i2\pi }{N}}}}) is a primitive root of unity, sometimes denoted ω N {\displaystyle \omega _{N}} ({\displaystyle \omega _{N}}) or W N {\displaystyle W_{N}} ({\displaystyle W_{N}}) (so that ω N N = 1 {\displaystyle \omega _{N}^{N}=1} ({\displaystyle \omega _{N}^{N}=1})). Such properties include the completeness, orthogonality, Plancherel/Parseval, periodicity, shift, convolution, and unitarity properties above, as well as many FFT algorithms. For this reason, the discrete Fourier transform can be defined by using roots of unity in fields other than the complex numbers, and such generalizations are commonly called *number-theoretic transforms* (NTTs) in the case of finite fields. For more information, see number-theoretic transform and discrete Fourier transform (general).

### Other finite groups

The standard DFT acts on a sequence *x*0, *x*1, ..., *x**N*−1 of complex numbers, which can be viewed as a function {0, 1, ..., *N* − 1} → **C**. The multidimensional DFT acts on multidimensional sequences, which can be viewed as functions

{

0

,

1

,

…

,

N

1

−

1

}

×

⋯

×

{

0

,

1

,

…

,

N

d

−

1

}

→

C

.

{\displaystyle \{0,1,\ldots ,N_{1}-1\}\times \cdots \times \{0,1,\ldots ,N_{d}-1\}\to \mathbb {C} .}

This suggests the generalization to Fourier transforms on arbitrary finite groups, which act on functions *G* → **C** where *G* is a finite group. In this framework, the standard DFT is seen as the Fourier transform on a cyclic group, while the multidimensional DFT is a Fourier transform on a direct sum of cyclic groups.

Further, Fourier transform can be on cosets of a group.


## Alternatives

There are various alternatives to the DFT for various applications, prominent among which are wavelets. The analog of the DFT is the discrete wavelet transform (DWT). From the point of view of time–frequency analysis, a key limitation of the Fourier transform is that it does not include *location* information, only *frequency* information, and thus has difficulty in representing transients. As wavelets have location as well as frequency, they are better able to represent location, at the expense of greater difficulty representing frequency. For details, see comparison of the discrete wavelet transform with the discrete Fourier transform.
