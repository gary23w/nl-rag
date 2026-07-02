---
title: "Modified discrete cosine transform"
source: https://en.wikipedia.org/wiki/Modified_discrete_cosine_transform
domain: audio-codec-mp3
license: CC-BY-SA-4.0
tags: mp3 codec, mpeg audio layer, psychoacoustic model, audio bit rate
fetched: 2026-07-02
---

# Modified discrete cosine transform

The **modified discrete cosine transform** (**MDCT**) is a transform based on the type-IV discrete cosine transform (DCT-IV), with the additional property of being lapped: it is designed to be performed on consecutive blocks of a larger dataset, where subsequent blocks are overlapped so that the last half of one block coincides with the first half of the next block. This overlapping, in addition to the energy-compaction qualities of the DCT, makes the MDCT especially attractive for signal compression applications, since it helps to avoid artifacts stemming from the block boundaries. As a result of these advantages, the MDCT is the most widely used lossy compression technique in audio data compression. It is employed in most modern audio coding standards, including MP3, Dolby Digital (AC-3), Vorbis (Ogg), Windows Media Audio (WMA), ATRAC, Cook, Advanced Audio Coding (AAC), High-Definition Coding (HDC), LDAC, Dolby AC-4, and MPEG-H 3D Audio, as well as speech coding standards such as AAC-LD (LD-MDCT), G.722.1, G.729.1, CELT, and Opus.

The discrete cosine transform (DCT) was first proposed by Nasir Ahmed in 1972, and demonstrated by Ahmed with T. Natarajan and K. R. Rao in 1974. The MDCT was later proposed by John P. Princen, A.W. Johnson and Alan B. Bradley at the University of Surrey in 1987, following earlier work by Princen and Bradley (1986) to develop the MDCT's underlying principle of **time-domain aliasing cancellation** (TDAC), described below. (There also exists an analogous transform, the MDST, based on the discrete sine transform, as well as other, rarely used, forms of the MDCT based on different types of DCT or DCT/DST combinations.)

In MP3, the MDCT is not applied to the audio signal directly, but rather to the output of a 32-band polyphase quadrature filter (PQF) bank. The output of this MDCT is postprocessed by an alias reduction formula to reduce the typical aliasing of the PQF filter bank. Such a combination of a filter bank with an MDCT is called a *hybrid* filter bank or a *subband* MDCT. AAC, on the other hand, normally uses a pure MDCT; only the (rarely used) MPEG-4 AAC-SSR variant (by Sony) uses a four-band PQF bank followed by an MDCT. Similar to MP3, ATRAC uses stacked quadrature mirror filters (QMF) followed by an MDCT.

## Definition

As a lapped transform, the MDCT is somewhat unusual compared to other Fourier-related transforms in that it has half as many outputs as inputs (instead of the same number). In particular, it is a linear function $F\colon \mathbf {R} ^{2N}\to \mathbf {R} ^{N}$ (where **R** denotes the set of real numbers). The 2*N* real numbers *x*0, ..., *x*2*N*−1 are transformed into the *N* real numbers *X*0, ..., *X**N*−1 according to the formula

$X_{k}=\sum _{n=0}^{2N-1}x_{n}\cos \left[{\frac {\pi }{N}}\left(n+{\frac {1}{2}}+{\frac {N}{2}}\right)\left(k+{\frac {1}{2}}\right)\right].$

The normalization coefficient in front of this transform, here unity, is an arbitrary convention and differs between treatments. Only the product of the normalizations of the MDCT and the IMDCT, below, is constrained.

### Inverse transform

The inverse MDCT is known as the **IMDCT**. Because there are different numbers of inputs and outputs, at first glance it might seem that the MDCT should not be invertible. However, perfect invertibility is achieved by *adding* the overlapped IMDCTs of subsequent overlapping blocks, causing the errors to *cancel* and the original data to be retrieved; this technique is known as *time-domain aliasing cancellation* (**TDAC**).

The IMDCT transforms *N* real numbers *X*0, ..., *X**N*−1 into 2*N* real numbers *y*0, ..., *y*2*N*−1 according to the formula

$y_{n}={\frac {1}{N}}\sum _{k=0}^{N-1}X_{k}\cos \left[{\frac {\pi }{N}}\left(n+{\frac {1}{2}}+{\frac {N}{2}}\right)\left(k+{\frac {1}{2}}\right)\right].$

Like for the DCT-IV, an orthogonal transform, the inverse has the same form as the forward transform.

In the case of a windowed MDCT with the usual window normalization (see below), the normalization coefficient in front of the IMDCT should be multiplied by 2 (i.e., becoming 2/*N*).

### Computation

Although the direct application of the MDCT formula would require O(*N*2) operations, it is possible to compute the same thing with only O(*N* log *N*) complexity by recursively factorizing the computation, as in the fast Fourier transform (FFT). One can also compute MDCTs via other transforms, typically a DFT (FFT) or a DCT, combined with O(*N*) pre- and post-processing steps. Also, as described below, any algorithm for the DCT-IV immediately provides a method to compute the MDCT and IMDCT of even size.

## Window functions

In typical signal-compression applications, the transform properties are further improved by using a window function *w**n* (*n* = 0, ..., 2*N* − 1) that is multiplied with *x**n* in the MDCT and with *y**n* in the IMDCT formulas above, in order to avoid discontinuities at the *n* = 0 and 2*N* boundaries by making the function go smoothly to zero at those points. (That is, the window function is applied to the data *before* the MDCT or *after* the IMDCT.) In principle, *x* and *y* could have different window functions, and the window function could also change from one block to the next (especially for the case where data blocks of different sizes are combined), but for simplicity we consider the common case of identical window functions for equal-sized blocks.

The transform remains invertible (that is, TDAC works), for a symmetric window *w**n* = *w*2*N*−1−*n*, as long as *w* satisfies the Princen–Bradley condition:

$w_{n}^{2}+w_{n+N}^{2}=1.$

Various window functions are used. A window that produces a form known as a modulated lapped transform (MLT) is given by

$w_{n}=\sin \left[{\frac {\pi }{2N}}\left(n+{\frac {1}{2}}\right)\right]$

and is used for MP3 and MPEG-2 AAC, and

$w_{n}=\sin \left({\frac {\pi }{2}}\sin ^{2}\left[{\frac {\pi }{2N}}\left(n+{\frac {1}{2}}\right)\right]\right)$

for Vorbis. AC-3 uses a Kaiser–Bessel derived (KBD) window, and MPEG-4 AAC can also use a KBD window.

Note that windows applied to the MDCT are different from windows used for some other types of signal analysis, since they must fulfill the Princen–Bradley condition. One of the reasons for this difference is that MDCT windows are applied twice, for both the MDCT (analysis) and the IMDCT (synthesis).

## Relationship to DCT-IV and origin of TDAC

As can be seen by inspection of the definitions, for *even* *N* the MDCT is essentially equivalent to a DCT-IV, where the input is shifted by *N*/2 and two *N*-blocks of data are transformed at once. By examining this equivalence more carefully, important properties like TDAC can be easily derived.

In order to define the precise relationship to the DCT-IV, one must realize that the DCT-IV corresponds to alternating even/odd boundary conditions: even at its left boundary (around *n* = −1/2), odd at its right boundary (around *n* = *N* − 1/2), and so on (instead of periodic boundaries as for a DFT). This follows from the identities

$\cos \left[{\frac {\pi }{N}}\left(-n-1+{\frac {1}{2}}\right)\left(k+{\frac {1}{2}}\right)\right]=\cos \left[{\frac {\pi }{N}}\left(n+{\frac {1}{2}}\right)\left(k+{\frac {1}{2}}\right)\right]$

and

$\cos \left[{\frac {\pi }{N}}\left(2N-n-1+{\frac {1}{2}}\right)\left(k+{\frac {1}{2}}\right)\right]=-\cos \left[{\frac {\pi }{N}}\left(n+{\frac {1}{2}}\right)\left(k+{\frac {1}{2}}\right)\right].$

Thus, if its inputs are an array *x* of length *N*, we can imagine extending this array to (*x*, −*x**R*, −*x*, *x**R*, ...) and so on, where *x**R* denotes *x* in reverse order.

Consider an MDCT with 2*N* inputs and *N* outputs, where we divide the inputs into four blocks (*a*, *b*, *c*, *d*) each of size *N*/2. If we shift these to the right by *N*/2 (from the +*N*/2 term in the MDCT definition), then (*b*, *c*, *d*) extend past the end of the *N* DCT-IV inputs, so we must "fold" them back according to the boundary conditions described above.

Thus, the MDCT of 2

N

inputs (

a

,

b

,

c

,

d

) is

exactly

equivalent to a DCT-IV of the

N

inputs: (

−

c

R

−

d

,

a

−

b

R

), where

R

denotes reversal as above.

In this way, any algorithm to compute the DCT-IV can be trivially applied to the MDCT.

Similarly, the IMDCT formula above is precisely 1/2 of the DCT-IV (which is its own inverse), where the output is extended (via the boundary conditions) to a length 2*N* and shifted back to the left by *N*/2. The inverse DCT-IV would simply give back the inputs (−*c**R* − *d*, *a* − *b**R*) from above. When this is extended via the boundary conditions and shifted, one obtains

IMDCT(MDCT(

a

,

b

,

c

,

d

)) = (

a

−

b

R

,

b

−

a

R

,

c

+

d

R

,

d

+

c

R

)/2.

Half of the IMDCT outputs are thus redundant, as *b* − *a**R* = −(*a* − *b**R*)*R*, and likewise for the last two terms. If we group the input into bigger blocks *A*,*B* of size *N*, where *A* = (*a*, *b*) and *B* = (*c*, *d*), we can write this result in a simpler way:

IMDCT(MDCT(

A

,

B

)) = (

A

−

A

R

,

B

+

B

R

)/2.

One can now understand how TDAC works. Suppose that one computes the MDCT of the subsequent, 50% overlapped, 2*N* block (*B*, *C*). The IMDCT will then yield, analogous to the above: (*B* − *B**R*, *C* + *C**R*)/2. When this is added with the previous IMDCT result in the overlapping half, the reversed terms cancel and one obtains simply *B*, recovering the original data.

### Origin of TDAC

The origin of the term "time-domain aliasing cancellation" is now clear. The use of input data that extend beyond the boundaries of the logical DCT-IV causes the data to be *aliased* in the same way that frequencies beyond the Nyquist frequency are aliased to lower frequencies, except that this aliasing occurs in the time domain instead of the frequency domain: we cannot distinguish the contributions of *a* and of *b**R* to the MDCT of (*a*, *b*, *c*, *d*), or equivalently, to the result of

IMDCT(MDCT(

a

,

b

,

c

,

d

))= (

a

−

b

R

,

b

−

a

R

,

c

+

d

R

,

d

+

c

R

)/2.

The combinations *c* − *d**R* and so on have precisely the right signs for the combinations to cancel when they are added.

For *odd* *N* (which are rarely used in practice), *N*/2 is not an integer, so the MDCT is not simply a shift permutation of a DCT-IV. In this case, the additional shift by half a sample means that the MDCT/IMDCT becomes equivalent to the DCT-III/II, and the analysis is analogous to the above.

### Smoothness and discontinuities

We have seen above that the MDCT of 2*N* inputs (*a*, *b*, *c*, *d*) is equivalent to a DCT-IV of the *N* inputs (−*c**R* − *d*, *a* − *b**R*). The DCT-IV is designed for the case where the function at the right boundary is odd, and therefore the values near the right boundary are close to 0. If the input signal is smooth, this is the case: the rightmost components of *a* and *b**R* are consecutive in the input sequence (*a*, *b*, *c*, *d*), and therefore their difference is small. Let us look at the middle of the interval: if we rewrite the above expression as (−*c**R* − *d*, *a* − *b**R*) = (−*d*, *a*) − (*b*, *c*)*R*, the second term, (*b*, *c*)*R*, gives a smooth transition in the middle. However, in the first term, (−*d*, *a*), there is a potential discontinuity where the right end of −*d* meets the left end of *a*. This is the reason for using a window function that reduces the components near the boundaries of the input sequence (*a*, *b*, *c*, *d*) towards 0.

### TDAC for the windowed MDCT

Above, the TDAC property was proved for the ordinary MDCT, showing that adding IMDCTs of subsequent blocks in their overlapping half recovers the original data. The derivation of this inverse property for the windowed MDCT is only slightly more complicated.

Consider two overlapping consecutive sets of 2*N* inputs (*A*,*B*) and (*B*,*C*), for blocks *A*,*B*,*C* of size *N*. Recall from above that when $(A,B)$ and $(B,C)$ are MDCTed, IMDCTed, and added in their overlapping half, we obtain $(B+B_{R})/2+(B-B_{R})/2=B$ , the original data.

Now we suppose that we multiply *both* the MDCT inputs *and* the IMDCT outputs by a window function of length 2*N*. As above, we assume a symmetric window function, which is therefore of the form $(W,W_{R})$ where *W* is a length-*N* vector and *R* denotes reversal as before. Then the Princen-Bradley condition can be written as $W^{2}+W_{R}^{2}=(1,1,\ldots )$ , with the squares and additions performed elementwise.

Therefore, instead of MDCTing $(A,B)$ , we now MDCT $(WA,W_{R}B)$ (with all multiplications performed elementwise). When this is IMDCTed and multiplied again (elementwise) by the window function, the last-*N* half becomes:

$W_{R}\cdot (W_{R}B+(W_{R}B)_{R})=W_{R}\cdot (W_{R}B+WB_{R})=W_{R}^{2}B+WW_{R}B_{R}$

.

(Note that we no longer have the multiplication by 1/2, because the IMDCT normalization differs by a factor of 2 in the windowed case.)

Similarly, the windowed MDCT and IMDCT of $(B,C)$ yields, in its first-*N* half:

$W\cdot (WB-W_{R}B_{R})=W^{2}B-WW_{R}B_{R}$

.

When we add these two halves together, we obtain:

$(W_{R}^{2}B+WW_{R}B_{R})+(W^{2}B-WW_{R}B_{R})=\left(W_{R}^{2}+W^{2}\right)B=B,$

recovering the original data.
