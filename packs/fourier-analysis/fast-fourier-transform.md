---
title: "Fast Fourier transform"
source: https://en.wikipedia.org/wiki/Fast_Fourier_transform
domain: fourier-analysis
license: CC-BY-SA-4.0
tags: fourier analysis, fourier transform, fourier series, fast fourier transform
fetched: 2026-07-02
---

# Fast Fourier transform

A **fast Fourier transform** (**FFT**) is an algorithm that computes the discrete Fourier transform (DFT), or its inverse (IDFT), of a sequence. A Fourier transform converts a signal from its original domain (often time or space) to a representation in the frequency domain and vice versa.

The DFT is obtained by decomposing a sequence of values into components of different frequencies. This operation is useful in many fields, but computing it directly from the definition is often too slow to be practical. An FFT rapidly computes such transformations by factorizing the DFT matrix into a product of sparse (mostly zero) factors. As a result, it manages to reduce the complexity of computing the DFT from ${\textstyle O(n^{2})}$ , which arises if one simply applies the definition of DFT, to ${\textstyle O(n\log n)}$ , where n is the length of the sequence. The difference in speed can be enormous, especially for long sequences where n may be in the thousands or millions.

As the FFT is merely an algebraic refactoring of terms within the DFT, the DFT and the FFT both perform mathematically equivalent and interchangeable operations, assuming that all terms are computed with infinite precision. However, in the presence of round-off error, many FFT algorithms are much more accurate than evaluating the DFT definition directly or indirectly. There are many different FFT algorithms based on a wide range of published theories, from simple complex-number arithmetic to group theory and number theory. The best-known FFT algorithms depend upon the factorization of n, but there are FFTs with $O(n\log n)$ complexity for all n, including prime values. Many FFT algorithms depend only on the fact that ${\textstyle e^{-2\pi i/n}}$ is an nth primitive root of unity, and thus can be applied to analogous transforms over any finite field, such as number-theoretic transforms. Since the inverse DFT is the same as the DFT, but with the opposite sign in the exponent and a 1/*n* factor, any FFT algorithm can easily be adapted for it.

Fast Fourier transforms are widely used for applications in engineering, music, science, and mathematics. The basic ideas were popularized in 1965, but some algorithms had been derived as early as 1805. In 1994, Gilbert Strang described the FFT as "the most important numerical algorithm of our lifetime", and it was included in Top 10 Algorithms of 20th Century by the IEEE magazine *Computing in Science & Engineering*.

## History

The development of fast algorithms for DFT was prefigured in Carl Friedrich Gauss's unpublished 1805 work on the orbits of asteroids Pallas and Juno. Gauss wanted to interpolate the orbits from sample observations; his method was very similar to the one that would be published in 1965 by James Cooley and John Tukey, who are generally credited for the invention of the modern generic FFT algorithm. While Gauss's work predated even Joseph Fourier's 1822 results, he did not analyze the method's complexity, and eventually used other methods to achieve the same end.

Between 1805 and 1965, some versions of FFT were published by other authors. Frank Yates in 1932 published his version called *interaction algorithm*, which provided efficient computation of Hadamard and Walsh transforms. Yates' algorithm is still used in the field of statistical design and analysis of experiments. In 1942, G. C. Danielson and Cornelius Lanczos published their version to compute DFT for x-ray crystallography, a field where calculation of Fourier transforms presented a formidable bottleneck. While many methods in the past had focused on reducing the constant factor for ${\textstyle O(n^{2})}$ computation by taking advantage of symmetries, Danielson and Lanczos realized that one could use the periodicity and apply a doubling trick to "double [n] with only slightly more than double the labor", though like Gauss they did not do the analysis to discover that this led to ${\textstyle O(n\log n)}$ scaling. In 1958, I. J. Good published a paper establishing the prime-factor FFT algorithm that applies to discrete Fourier transforms of size ${\textstyle n=n_{1}n_{2}}$ , where $n_{1}$ and $n_{2}$ are coprime.

James Cooley and John Tukey independently rediscovered these earlier algorithms and published a more general FFT in 1965 that is applicable when n is composite and not necessarily a power of 2, as well as analyzing the ${\textstyle O(n\log n)}$ scaling. Tukey came up with the idea during a meeting of President Kennedy's Science Advisory Committee, where a discussion topic involved detecting nuclear tests by the Soviet Union by setting up sensors to surround the country from outside. To analyze the output of these sensors, an FFT algorithm would be needed. In discussion with Tukey, Richard Garwin recognized the general applicability of the algorithm not just to national security problems, but also to a wide range of problems including one of immediate interest to him, determining the periodicities of the spin orientations in a 3-D crystal of Helium-3. Garwin gave Tukey's idea to Cooley (both worked at IBM's Watson labs) for implementation. Cooley and Tukey published the paper in a relatively short time of six months. As Tukey did not work at IBM, the patentability of the idea was doubted and the algorithm went into the public domain, which, through the computing revolution of the next decade, made FFT one of the indispensable algorithms in digital signal processing.

## Definition

Let $x_{0},\ldots ,x_{n-1}$ be complex numbers. The DFT is defined by the formula

$X_{k}=\sum _{m=0}^{n-1}x_{m}e^{-i2\pi km/n}\qquad k=0,\ldots ,n-1,$

where $e^{i2\pi /n}$ is a primitive nth root of 1.

Evaluating this definition directly requires ${\textstyle O(n^{2})}$ operations: there are n outputs Xk , and each output requires a sum of n terms. An FFT is any method to compute the same results in ${\textstyle O(n\log n)}$ operations. All known FFT algorithms require ${\textstyle O(n\log n)}$ operations, although there is no known proof that lower complexity is impossible.

To illustrate the savings of an FFT, consider the count of complex multiplications and additions for ${\textstyle n=4096}$ data points. Evaluating the DFT's sums directly involves ${\textstyle n^{2}}$ complex multiplications and ${\textstyle n(n-1)}$ complex additions, of which ${\textstyle O(n)}$ operations can be saved by eliminating trivial operations such as multiplications by 1, leaving about 30 million operations. In contrast, the radix-2 Cooley–Tukey algorithm, for n a power of 2, can compute the same result with only ${\textstyle (n/2)\log _{2}(n)}$ complex multiplications (again, ignoring simplifications of multiplications by 1 and similar) and ${\textstyle n\log _{2}(n)}$ complex additions, in total about 70,000 operations — more than four-hundred times less than with direct evaluation. In practice, actual performance on modern computers is usually dominated by factors other than the speed of arithmetic operations and the analysis is a complicated subject (for example, see Frigo & Johnson, 2005), but the overall improvement from ${\textstyle O(n^{2})}$ to ${\textstyle O(n\log n)}$ remains.

## Algorithms

### Cooley–Tukey algorithm

By far the most commonly used FFT is the Cooley–Tukey algorithm. This is a divide-and-conquer algorithm that recursively breaks down a DFT of any composite size ${\textstyle n=n_{1}n_{2}}$ into ${\textstyle n_{1}}$ smaller DFTs of size ${\textstyle n_{2}}$ , along with $O(n)$ multiplications by complex roots of unity traditionally called twiddle factors (after Gentleman and Sande, 1966).

This method (and the general idea of an FFT) was popularized by a publication of Cooley and Tukey in 1965, but it was later discovered that those two authors had together independently re-invented an algorithm known to Carl Friedrich Gauss around 1805 (and subsequently rediscovered several times in limited forms).

The best known use of the Cooley–Tukey algorithm is to divide the transform into two pieces of size *n*/2 at each step, and is therefore limited to power-of-two sizes, but any factorization can be used in general (as was known to both Gauss and Cooley/Tukey). These are called the *radix-2* and *mixed-radix* cases, respectively (and other variants such as the split-radix FFT have their own names as well). Although the basic idea is recursive, most traditional implementations rearrange the algorithm to avoid explicit recursion. Also, because the Cooley–Tukey algorithm breaks the DFT into smaller DFTs, it can be combined arbitrarily with any other algorithm for the DFT, such as those described below.

### Other FFT algorithms

For ${\textstyle n=n_{1}n_{2}}$ with coprime ${\textstyle n_{1}}$ and ${\textstyle n_{2}}$ , one can use the prime-factor (Good–Thomas) algorithm (PFA), based on the Chinese remainder theorem, to factorize the DFT similarly to Cooley–Tukey but without the twiddle factors. The Rader–Brenner algorithm (1976) is a Cooley–Tukey-like factorization but with purely imaginary twiddle factors, reducing multiplications at the cost of increased additions and reduced numerical stability; it was later superseded by the split-radix variant of Cooley–Tukey (which achieves the same multiplication count but with fewer additions and without sacrificing accuracy). Algorithms that recursively factorize the DFT into smaller operations other than DFTs include the Bruun and QFT algorithms. (The Rader–Brenner and QFT algorithms were proposed for power-of-two sizes, but it is possible that they could be adapted to general composite n. Bruun's algorithm applies to arbitrary even composite sizes.) Bruun's algorithm, in particular, is based on interpreting the FFT as a recursive factorization of the polynomial $z^{n}-1$ , here into real-coefficient polynomials of the form $z^{m}-1$ and $z^{2m}+az^{m}+1$ .

Another polynomial viewpoint is exploited by the Winograd FFT algorithm, which factorizes $z^{n}-1$ into cyclotomic polynomials—these often have coefficients of 1, 0, or −1, and therefore require few (if any) multiplications, so Winograd can be used to obtain minimal-multiplication FFTs and is often used to find efficient algorithms for small factors. Indeed, Winograd showed that the DFT can be computed with only $O(n)$ irrational multiplications, leading to a proven achievable lower bound on the number of multiplications for power-of-two sizes; this comes at the cost of many more additions, a tradeoff no longer favorable on modern processors with hardware multipliers. In particular, Winograd also makes use of the PFA as well as an algorithm by Rader for FFTs of *prime* sizes.

Rader's algorithm, exploiting the existence of a generator for the multiplicative group modulo prime n, expresses a DFT of prime size n as a cyclic convolution of (composite) size *n* – 1, which can then be computed by a pair of ordinary FFTs via the convolution theorem (although Winograd uses other convolution methods). Another prime-size FFT is due to L. I. Bluestein, and is sometimes called the chirp-z algorithm; it also re-expresses a DFT as a convolution, but this time of the *same* size (which can be zero-padded to a power of two and evaluated by radix-2 Cooley–Tukey FFTs, for example), via the identity

$nk=-{\frac {(k-n)^{2}}{2}}+{\frac {n^{2}}{2}}+{\frac {k^{2}}{2}}.$

Hexagonal fast Fourier transform (HFFT) aims at computing an efficient FFT for the hexagonally-sampled data by using a new addressing scheme for hexagonal grids, called Array Set Addressing (ASA).

## FFT algorithms specialized for real or symmetric data

In many applications, the input data for the DFT are purely real, in which case the outputs satisfy the symmetry

$X_{n-k}=X_{k}^{*}$

and efficient FFT algorithms have been designed for this situation (see e.g., Sorensen, 1987). One approach consists of taking an ordinary algorithm (e.g., Cooley–Tukey) and removing the redundant parts of the computation, saving roughly a factor of two in time and memory. Alternatively, it is possible to express an *even*-length real-input DFT as a complex DFT of half the length (whose real and imaginary parts are the even/odd elements of the original real data), followed by $O(n)$ post-processing operations.

It was once believed that real-input DFTs could be more efficiently computed by means of the discrete Hartley transform (DHT), but it was subsequently argued that a specialized real-input DFT algorithm (FFT) can typically be found that requires fewer operations than the corresponding DHT algorithm (FHT) for the same number of inputs. Bruun's algorithm (above) is another method that was initially proposed to take advantage of real inputs, but it has not proved popular.

There are further FFT specializations for the cases of real data that have even/odd symmetry, in which case one can gain another factor of roughly two in time and memory and the DFT becomes the discrete cosine/sine transform(s) (DCT/DST). Instead of directly modifying an FFT algorithm for these cases, DCTs/DSTs can also be computed via FFTs of real data combined with $O(n)$ pre- and post-processing.

## Computational issues

### Bounds on complexity and operation counts

Unsolved problem in computer science

What is the lower bound on the complexity of fast Fourier transform algorithms? Can they be faster than

$O(N\log N)$

?

More unsolved problems in computer science

A fundamental question of longstanding theoretical interest is to prove lower bounds on the complexity and exact operation counts of fast Fourier transforms, and many open problems remain. It is not rigorously proved whether DFTs truly require ${\textstyle \Omega (n\log n)}$ (i.e., order *$n\log n$* or greater) operations, even for the simple case of power of two sizes, although no algorithms with lower complexity are known. In particular, the count of arithmetic operations is usually the focus of such questions, although actual performance on modern-day computers is determined by many other factors such as cache or CPU pipeline optimization.

Following work by Shmuel Winograd (1978), a tight $\Theta (n)$ lower bound is known for the number of real multiplications required by an FFT. It can be shown that only ${\textstyle 4n-2\log _{2}^{2}(n)-2\log _{2}(n)-4}$ irrational real multiplications are required to compute a DFT of power-of-two length $n=2^{m}$ . Moreover, explicit algorithms that achieve this count are known (Heideman & Burrus, 1986; Duhamel, 1990). However, these algorithms require too many additions to be practical, at least on modern computers with hardware multipliers (Duhamel, 1990; Frigo & Johnson, 2005).

A tight lower bound is not known on the number of required additions, although lower bounds have been proved under some restrictive assumptions on the algorithms. In 1973, Morgenstern proved an $\Omega (n\log n)$ lower bound on the addition count for algorithms where the multiplicative constants have bounded magnitudes (which is true for most but not all FFT algorithms). Pan (1986) proved an $\Omega (n\log n)$ lower bound assuming a bound on a measure of the FFT algorithm's *asynchronicity*, but the generality of this assumption is unclear. For the case of power-of-two n, Papadimitriou (1979) argued that the number ${\textstyle n\log _{2}n}$ of complex-number additions achieved by Cooley–Tukey algorithms is *optimal* under certain assumptions on the graph of the algorithm (his assumptions imply, among other things, that no additive identities in the roots of unity are exploited). (This argument would imply that at least ${\textstyle 2N\log _{2}N}$ real additions are required, although this is not a tight bound because extra additions are required as part of complex-number multiplications.) Thus far, no published FFT algorithm has achieved fewer than ${\textstyle n\log _{2}n}$ complex-number additions (or their equivalent) for power-of-two n.

A third problem is to minimize the *total* number of real multiplications and additions, sometimes called the *arithmetic complexity* (although in this context it is the exact count and not the asymptotic complexity that is being considered). Again, no tight lower bound has been proven. Since 1968, however, the lowest published count for power-of-two n was long achieved by the split-radix FFT algorithm, which requires ${\textstyle 4n\log _{2}(n)-6n+8}$ real multiplications and additions for *n* > 1. This was further reduced to ${\textstyle \sim {\frac {34}{9}}n\log _{2}n}$ (Johnson and Frigo, 2007; Lundy and Van Buskirk, 2007). A slightly larger count (but still better than split radix for *n* ≥ 256) was shown to be provably optimal for *n* ≤ 512 under additional restrictions on the possible algorithms (split-radix-like flowgraphs with unit-modulus multiplicative factors), by reduction to a satisfiability modulo theories problem solvable by brute force (Haynal & Haynal, 2011).

Most of the attempts to lower or prove the complexity of FFT algorithms have focused on the ordinary complex-data case, because it is the simplest. However, complex-data FFTs are so closely related to algorithms for related problems, such as real-data FFTs, discrete cosine transforms, discrete Hartley transforms, and so on, that any improvement in one of these would immediately lead to improvements in the others (Duhamel & Vetterli, 1990).

### Approximations

All of the FFT algorithms discussed above compute the DFT exactly (i.e., neglecting floating-point errors). A few FFT algorithms have been proposed, however, that compute the DFT *approximately*, with an error that can be made arbitrarily small at the expense of increased computations. Such algorithms trade the approximation error for increased speed or other properties. For example, an approximate FFT algorithm by Edelman et al. (1999) achieves lower communication requirements for parallel computing with the help of a fast multipole method. A wavelet-based approximate FFT by Guo and Burrus (1996) takes sparse inputs/outputs (time/frequency localization) into account more efficiently than is possible with an exact FFT. Another algorithm for approximate computation of a subset of the DFT outputs is due to Shentov et al. (1995). The Edelman algorithm works equally well for sparse and non-sparse data, since it is based on the compressibility (rank deficiency) of the Fourier matrix itself rather than the compressibility (sparsity) of the data. Conversely, if the data are sparse—that is, if only k out of n Fourier coefficients are nonzero—then the complexity can be reduced to $O(k\log n\log n/k)$ , and this has been demonstrated to lead to practical speedups compared to an ordinary FFT for *n*/*k* > 32 in a large-n example (*n* = 222) using a probabilistic approximate algorithm (which estimates the largest k coefficients to several decimal places).

### Accuracy

FFT algorithms have errors when finite-precision floating-point arithmetic is used, but these errors are typically quite small; most FFT algorithms, e.g., Cooley–Tukey, have excellent numerical properties as a consequence of the pairwise summation structure of the algorithms. The upper bound on the relative error for the Cooley–Tukey algorithm is ${\textstyle O(\varepsilon \log n)}$ , compared to ${\textstyle O(\varepsilon n^{3/2})}$ for the naïve DFT formula, where 𝜀 is the machine floating-point relative precision. In fact, the root mean square (rms) errors are much better than these upper bounds, being only ${\textstyle O(\varepsilon {\sqrt {\log n}})}$ for Cooley–Tukey and ${\textstyle O(\varepsilon {\sqrt {n}})}$ for the naïve DFT (Schatzman, 1996). These results, however, are very sensitive to the accuracy of the twiddle factors used in the FFT (i.e. the trigonometric function values), and it is not unusual for incautious FFT implementations to have much worse accuracy, e.g. if they use inaccurate trigonometric recurrence formulas. Some FFTs other than Cooley–Tukey, such as the Rader–Brenner algorithm, are intrinsically less stable.

In fixed-point arithmetic, the finite-precision errors accumulated by FFT algorithms are worse, with rms errors growing as ${\textstyle O({\sqrt {n}})}$ for the Cooley–Tukey algorithm (Welch, 1969). Achieving this accuracy requires careful attention to scaling to minimize loss of precision, and fixed-point FFT algorithms involve rescaling at each intermediate stage of decompositions like Cooley–Tukey.

To verify the correctness of an FFT implementation, rigorous guarantees can be obtained in ${\textstyle O(n\log n)}$ time by a simple procedure checking the linearity, impulse-response, and time-shift properties of the transform on random inputs (Ergün, 1995).

The values for intermediate frequencies may be obtained by various averaging methods.

## Multidimensional FFTs

As defined in the multidimensional DFT article, the multidimensional DFT

$X_{\mathbf {k} }=\sum _{\mathbf {n} =0}^{\mathbf {N} -1}e^{-2\pi i\mathbf {k} \cdot (\mathbf {n} /\mathbf {N} )}x_{\mathbf {n} }$

transforms an array *x***n** with a d-dimensional vector of indices ${\textstyle \mathbf {n} =\left(n_{1},\ldots ,n_{d}\right)}$ by a set of d nested summations (over ${\textstyle n_{j}=0\ldots N_{j}-1}$ for each j), where the division ${\textstyle \mathbf {n} /\mathbf {N} =\left(n_{1}/N_{1},\ldots ,n_{d}/N_{d}\right)}$ is performed element-wise. Equivalently, it is the composition of a sequence of *d* sets of one-dimensional DFTs, performed along one dimension at a time (in any order).

This compositional viewpoint immediately provides the simplest and most common multidimensional DFT algorithm, known as the **row-column** algorithm (after the two-dimensional case, below). That is, one simply performs a sequence of d one-dimensional FFTs (by any of the above algorithms): first you transform along the *n*1 dimension, then along the *n*2 dimension, and so on (actually, any ordering works). This method is easily shown to have the usual ${\textstyle O(n\log n)}$ complexity, where ${\textstyle n=n_{1}\cdot n_{2}\cdots n_{d}}$ is the total number of data points transformed. In particular, there are *n*/*n*1 transforms of size *n*1, etc., so the complexity of the sequence of FFTs is:

${\begin{aligned}&{\frac {n}{n_{1}}}O(n_{1}\log n_{1})+\cdots +{\frac {n}{n_{d}}}O(n_{d}\log n_{d})\\[6pt]={}&O\left(n\left[\log n_{1}+\cdots +\log n_{d}\right]\right)=O(n\log n).\end{aligned}}$

In two dimensions, the *x***k** can be viewed as an $n_{1}\times n_{2}$ matrix, and this algorithm corresponds to first performing the FFT of all the rows (resp. columns), grouping the resulting transformed rows (resp. columns) together as another $n_{1}\times n_{2}$ matrix, and then performing the FFT on each of the columns (resp. rows) of this second matrix, and similarly grouping the results into the final result matrix.

In more than two dimensions, it is often advantageous for cache locality to group the dimensions recursively. For example, a three-dimensional FFT might first perform two-dimensional FFTs of each planar slice for each fixed *n*1, and then perform the one-dimensional FFTs along the *n*1 direction. More generally, an asymptotically optimal cache-oblivious algorithm consists of recursively dividing the dimensions into two groups ${\textstyle (n_{1},\ldots ,n_{d/2})}$ and ${\textstyle (n_{d/2+1},\ldots ,n_{d})}$ that are transformed recursively (rounding if d is not even) (see Frigo and Johnson, 2005). Still, this remains a straightforward variation of the row-column algorithm that ultimately requires only a one-dimensional FFT algorithm as the base case, and still has $O(n\log n)$ complexity. Yet another variation is to perform matrix transpositions in between transforming subsequent dimensions, so that the transforms operate on contiguous data; this is especially important for out-of-core and distributed memory situations where accessing non-contiguous data is extremely time-consuming.

There are other multidimensional FFT algorithms that are distinct from the row-column algorithm, although all of them have ${\textstyle O(n\log n)}$ complexity. Perhaps the simplest non-row-column FFT is the vector-radix FFT algorithm, which is a generalization of the ordinary Cooley–Tukey algorithm where one divides the transform dimensions by a vector ${\textstyle \mathbf {r} =\left(r_{1},r_{2},\ldots ,r_{d}\right)}$ of radices at each step. (This may also have cache benefits.) The simplest case of vector-radix is where all of the radices are equal (e.g., vector-radix-2 divides *all* of the dimensions by two), but this is not necessary. Vector radix with only a single non-unit radix at a time, i.e. ${\textstyle \mathbf {r} =\left(1,\ldots ,1,r,1,\ldots ,1\right)}$ , is essentially a row-column algorithm. Other, more complicated, methods include polynomial transform algorithms due to Nussbaumer (1977), which view the transform in terms of convolutions and polynomial products. See Duhamel and Vetterli (1990) for more information and references.

## Other generalizations

An ${\textstyle O(n^{5/2}\log n)}$ generalization to spherical harmonics on the sphere *S*2 with *n*2 nodes was described by Mohlenkamp, along with an algorithm conjectured (but not proven) to have ${\textstyle O(n^{2}\log ^{2}(n))}$ complexity; Mohlenkamp also provides an implementation in the libftsh library. A spherical-harmonic algorithm with ${\textstyle O(n^{2}\log n)}$ complexity is described by Rokhlin and Tygert.

The fast folding algorithm is analogous to the FFT, except that it operates on a series of binned waveforms rather than a series of real or complex scalar values. Rotation (which in the FFT is multiplication by a complex phasor) is a circular shift of the component waveform .

Various groups have also published FFT algorithms for non-equispaced data, as reviewed in Potts *et al.* (2001). Such algorithms do not strictly compute the DFT (which is only defined for equispaced data), but rather some approximation thereof (a non-uniform discrete Fourier transform, or NDFT, which itself is often computed only approximately). More generally, there are various other methods of spectral estimation.

## Applications

The FFT is used in digital recording, sampling, additive synthesis and pitch correction software.

The FFT's importance derives from the fact that it has made working in the frequency domain equally computationally feasible as working in the temporal or spatial domain. Some of the important applications of the FFT include:

- fast large-integer multiplication algorithms and polynomial multiplication,
- efficient matrix–vector multiplication for Toeplitz, circulant and other structured matrices,
- filtering algorithms (see overlap–add and overlap–save methods),
- fast algorithms for discrete cosine or sine transforms (e.g. fast DCT used for JPEG and MPEG/MP3 encoding and decoding),
- fast Chebyshev approximation,
- solving difference equations,
- computation of isotopic distributions.

### Telecommunications

In modern wireless communication standards, the FFT is a critical component for processing signals. Specifically, it is utilized in Orthogonal frequency-division multiplexing (OFDM) systems, such as 4G LTE and 5G NR. The efficiency of the FFT allows for high-speed data transmission by dividing a wideband signal into multiple closely spaced orthogonal subcarriers. This technology is essential for reducing interference and optimizing power consumption in mobile devices.

## Alternatives

The FFT can be a poor choice for analyzing signals with non-stationary frequency content—where the frequency characteristics change over time. DFTs provide a global frequency estimate, assuming that all frequency components are present throughout the entire signal, which makes it challenging to detect short-lived or transient features within signals.

For cases where frequency information appears briefly in the signal or generally varies over time, alternatives like the short-time Fourier transform, discrete wavelet transforms, or discrete Hilbert transform can be more suitable. These transforms allow for localized frequency analysis by capturing both frequency and time-based information.

## Research areas

**Big FFTs**

With the explosion of big data in fields such as astronomy, the need for 512K FFTs has arisen for certain interferometry calculations. The data collected by projects such as

WMAP

and

LIGO

require FFTs of tens of billions of points. As this size does not fit into main memory, so-called out-of-core FFTs are an active area of research.

**Approximate FFTs**

For applications such as MRI, it is necessary to compute DFTs for nonuniformly spaced grid points and/or frequencies. Multipole-based approaches can compute approximate quantities with factor of runtime increase.

**Group FFTs**

The FFT may also be explained and interpreted using

group representation theory

, allowing for further generalization. A function on any compact group, including non-cyclic, has an expansion in terms of a basis of irreducible matrix elements. It remains an active area of research to find an efficient algorithm for performing this change of basis. Applications including efficient

spherical harmonic

expansion, analyzing certain

Markov processes

, robotics etc.

**Quantum FFTs**

Shor's fast algorithm for

integer factorization

on a quantum computer has a subroutine to compute DFT of a binary vector. This is implemented as a sequence of 1- or 2-bit quantum gates now known as quantum FFT, which is effectively the Cooley–Tukey FFT realized as a particular factorization of the Fourier matrix. Extensions to these ideas are currently being explored.

## Language reference

| Language | Command–method | Prerequisites |
|---|---|---|
| R | stats::fft(x) | None |
| Scilab | fft(x) | None |
| MATLAB, Octave | fft(x) | None |
| Python | fft.fft(x) | numpy or scipy |
| Mathematica | Fourier[x] | None |
| C / C++ | fftw_execute(plan) | FFTW |
| Fortran | fftw_one(plan,in,out) | FFTW |
| Julia | fft(A [,dims]) | FFTW |
| Rust | fft.process(&mut x); | rustfft |
| Haskell | dft x | fft |
