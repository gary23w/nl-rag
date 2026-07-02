---
title: "Discrete-time Fourier transform"
source: https://en.wikipedia.org/wiki/Discrete-time_Fourier_transform
domain: spectral-analysis-stats
license: CC-BY-SA-4.0
tags: spectral density, periodogram, cross-spectral density, wavelet transform
fetched: 2026-07-02
---

# Discrete-time Fourier transform

In mathematics, the **discrete-time Fourier transform** (**DTFT**) is a form of Fourier analysis that is applicable to a sequence of discrete values.

The DTFT is often used to analyze samples of a continuous function. The term *discrete-time* refers to the fact that the transform operates on discrete data, often samples whose interval has units of time. From uniformly spaced samples it produces a function of frequency that is a periodic summation of the continuous Fourier transform of the original continuous function. In simpler terms, when you take the DTFT of regularly-spaced samples of a continuous signal, you get repeating (and possibly overlapping) copies of the signal's frequency spectrum, spaced at intervals corresponding to the sampling frequency. Under certain theoretical conditions, described by the sampling theorem, the original continuous function can be recovered perfectly from the DTFT and thus from the original discrete samples. The DTFT itself is a continuous function of frequency, but discrete samples of it can be readily calculated via the discrete Fourier transform (DFT) (see § Sampling the DTFT), which is by far the most common method of modern Fourier analysis.

Both transforms are invertible. The inverse DTFT reconstructs the original sampled data sequence, while the inverse DFT produces a periodic summation of the original sequence. The fast Fourier transform (FFT) is an algorithm for computing one cycle of the DFT, and its inverse produces one cycle of the inverse DFT.

## Relation to Fourier transform

Let $s(t)$ be a continuous function in the time domain. We begin with a common definition of the continuous Fourier transform, where f represents frequency in hertz and t represents time in seconds:

$S(f)\triangleq \int _{-\infty }^{\infty }s(t)\cdot e^{-i2\pi ft}dt.$

We can reduce the integral into a summation by sampling $s(t)$ at intervals of T seconds (see Fourier transform § Numerical integration of a series of ordered pairs). Specifically, we can replace $s(t)$ with a discrete sequence of its samples, $s(nT)$ , for integer values of n , and replace the differential element $dt$ with the sampling period T . Thus, we obtain one formulation for the discrete-time Fourier transform (DTFT):

$S_{1/T}(f)\triangleq \sum _{n=-\infty }^{\infty }\underbrace {T\cdot s(nT)} _{s[n]}\ e^{-i2\pi fTn}.$

This Fourier series (in frequency) is a continuous periodic function, whose periodicity is the sampling frequency $1/T$ . The subscript $1/T$ distinguishes it from the continuous Fourier transform $S(f)$ , and from the angular frequency form of the DTFT. The latter is obtained by defining an angular frequency variable, $\omega \triangleq 2\pi fT$ (which has normalized units of *radians/sample*), giving us a periodic function of angular frequency, with periodicity $2\pi$ :

| $S_{2\pi }(\omega )=S_{1/T}\left({\tfrac {\omega }{2\pi T}}\right)=\sum _{n=-\infty }^{\infty }s[n]\cdot e^{-i\omega n}.$ |   | Eq.1 |
|---|---|---|

The utility of the DTFT is rooted in the Poisson summation formula, which tells us that the periodic function represented by the Fourier series is a periodic summation of the continuous Fourier transform**:**

Poisson summation

| $S_{1/T}(f)=\sum _{n=-\infty }^{\infty }s[n]\cdot e^{-i2\pi fTn}\;=\sum _{k=-\infty }^{\infty }S\left(f-k/T\right).$ |   | Eq.2 |
|---|---|---|

The components of the periodic summation are centered at integer values (denoted by k ) of a normalized frequency (cycles per sample). Ordinary/physical frequency (cycles per second) is the product of k and the sample-rate, $f_{s}=1/T.$   For sufficiently large $f_{s},$ the $k=0$ term can be observed in the region $[-f_{s}/2,f_{s}/2]$ with little or no distortion (aliasing) from the other terms. **Fig.1** depicts an example where $1/T$ is not large enough to prevent aliasing.

We also note that $e^{-i2\pi fTn}$ is the Fourier transform of $\delta (t-nT).$ Therefore, an alternative definition of DTFT is**:**

| $S_{1/T}(f)={\mathcal {F}}\left\{\sum _{n=-\infty }^{\infty }s[n]\cdot \delta (t-nT)\right\}.$ |   | Eq.3 |
|---|---|---|

The modulated Dirac comb function is a mathematical abstraction sometimes referred to as *impulse sampling*.

## Inverse transform

An operation that recovers the discrete data sequence from the DTFT function is called an *inverse DTFT*. For instance, the inverse continuous Fourier transform of both sides of **Eq.3** produces the sequence in the form of a modulated Dirac comb function**:**

$\sum _{n=-\infty }^{\infty }s[n]\cdot \delta (t-nT)={\mathcal {F}}^{-1}\left\{S_{1/T}(f)\right\}\ \triangleq \int _{-\infty }^{\infty }S_{1/T}(f)\cdot e^{i2\pi ft}df.$

However, noting that $S_{1/T}(f)$ is periodic, all the necessary information is contained within any interval of length $1/T.$   In both **Eq.1** and **Eq.2**, the summations over n are a Fourier series, with coefficients $s[n].$   The standard formulas for the Fourier coefficients are also the inverse transforms**:**

| ${\begin{aligned}s[n]&=T\int _{\frac {1}{T}}S_{1/T}(f)\cdot e^{i2\pi fnT}df\quad \scriptstyle {{\text{(integral over any interval of length }}1/T{\textrm {)}}}\\\displaystyle &={\frac {1}{2\pi }}\int _{2\pi }S_{2\pi }(\omega )\cdot e^{i\omega n}d\omega \quad \scriptstyle {{\text{(integral over any interval of length }}2\pi {\textrm {)}}}\end{aligned}}$ |   | Eq.4 |
|---|---|---|

## Periodic data

When the input data sequence $s[n]$ is N -periodic, **Eq.2** can be computationally reduced to a discrete Fourier transform (DFT), because**:**

- All the available information is contained within N samples.
- $S_{1/T}(f)$ converges to zero everywhere except at integer multiples of $1/(NT),$ known as harmonic frequencies. At those frequencies, the DTFT diverges at different frequency-dependent rates. And those rates are given by the DFT of one cycle of the $s[n]$ sequence.
- The DTFT is periodic, so the maximum number of unique harmonic amplitudes is $(1/T)/(1/(NT))=N.$

The DFT of one cycle of the $s[n]$ sequence is**:**

$S[k]\triangleq \underbrace {\sum _{N}s[n]\cdot e^{-i2\pi {\frac {k}{N}}n}} _{\text{any n-sequence of length N}},\quad k\in \mathbf {Z} .$

And $s[n]$ can be expressed in terms of the inverse transform, which is sometimes referred to as a **discrete Fourier series** (DFS)**:**

$s[n]={\frac {1}{N}}\underbrace {\sum _{N}S[k]\cdot e^{i2\pi {\frac {k}{N}}n}} _{\text{any k-sequence of length N}},\quad n\in \mathbf {Z} .$

With these definitions, we can demonstrate the relationship between the DTFT and the DFT**:**

${\begin{aligned}S_{1/T}(f)&\triangleq \sum _{n=-\infty }^{\infty }s[n]\cdot e^{-i2\pi fnT}\\&=\sum _{n=-\infty }^{\infty }\left[{\frac {1}{N}}\sum _{k=0}^{N-1}S[k]\cdot e^{i2\pi {\frac {k}{N}}n}\right]\cdot e^{-i2\pi fnT}\\&={\frac {1}{N}}\sum _{k=0}^{N-1}S[k]\underbrace {\left[\sum _{n=-\infty }^{\infty }e^{i2\pi {\frac {k}{N}}n}\cdot e^{-i2\pi fnT}\right]} _{\operatorname {DTFT} \left(e^{i2\pi {\frac {k}{N}}n}\right)}\\&={\frac {1}{N}}\sum _{k=0}^{N-1}S[k]\cdot {\frac {1}{T}}\sum _{M=-\infty }^{\infty }\delta \left(f-{\tfrac {k}{NT}}-{\tfrac {M}{T}}\right)\end{aligned}}$

Due to the N -periodicity of both functions of $k,$ this can be simplified to**:**

$S_{1/T}(f)={\frac {1}{NT}}\sum _{k=-\infty }^{\infty }S[k]\cdot \delta \left(f-{\frac {k}{NT}}\right),$

which satisfies the inverse transform requirement**:**

${\begin{aligned}s[n]&=T\int _{0}^{\frac {1}{T}}S_{1/T}(f)\cdot e^{i2\pi fnT}df\\&={\frac {1}{N}}\sum _{k=-\infty }^{\infty }S[k]\underbrace {\int _{0}^{\frac {1}{T}}\delta \left(f-{\tfrac {k}{NT}}\right)e^{i2\pi fnT}df} _{{\text{zero for }}k\ \notin \ [0,N-1]}\\&={\frac {1}{N}}\sum _{k=0}^{N-1}S[k]\int _{0}^{\frac {1}{T}}\delta \left(f-{\tfrac {k}{NT}}\right)e^{i2\pi fnT}df\\&={\frac {1}{N}}\sum _{k=0}^{N-1}S[k]\cdot e^{i2\pi {\tfrac {k}{NT}}nT}\\&={\frac {1}{N}}\sum _{k=0}^{N-1}S[k]\cdot e^{i2\pi {\tfrac {k}{N}}n}\end{aligned}}$

## Sampling the DTFT

When the DTFT is continuous, a common practice is to compute an arbitrary number of samples $(N)$ of one cycle of the periodic function $S_{1/T}$ **:**

${\begin{aligned}\underbrace {S_{1/T}\left({\frac {k}{NT}}\right)} _{S_{k}}&=\sum _{n=-\infty }^{\infty }s[n]\cdot e^{-i2\pi {\frac {k}{N}}n}\quad \quad k=0,\dots ,N-1\\&=\underbrace {\sum _{N}s_{_{N}}[n]\cdot e^{-i2\pi {\frac {k}{N}}n},} _{\text{DFT}}\quad \scriptstyle {{\text{(sum over any }}n{\text{-sequence of length }}N)}\end{aligned}}$

where $s_{_{N}}$ is a periodic summation**:**

$s_{_{N}}[n]\ \triangleq \ \sum _{m=-\infty }^{\infty }s[n-mN].$

(see

Discrete Fourier series

)

The $s_{_{N}}$ sequence is the inverse DFT. Thus, our sampling of the DTFT causes the inverse transform to become periodic. The array of $|S_{k}|^{2}$ values is known as a *periodogram*, and the parameter N is called NFFT in the Matlab function of the same name.

In order to evaluate one cycle of $s_{_{N}}$ numerically, we require a finite-length $s[n]$ sequence. For instance, a long sequence might be truncated by a window function of length L resulting in three cases worthy of special mention. For notational simplicity, consider the $s[n]$ values below to represent the values modified by the window function.

**Case: Frequency decimation.** $L=N\cdot I,$ for some integer I (typically 6 or 8)

A cycle of $s_{_{N}}$ reduces to a summation of I segments of length $N.$   The DFT then goes by various names, such as**:**

- *window-presum FFT*
- *Weight, overlap, add (WOLA)*
- *polyphase DFT*
- *polyphase filter bank*
- *multiple block windowing* and *time-aliasing*.

Recall that decimation of sampled data in one domain (time or frequency) produces overlap (sometimes known as aliasing) in the other, and vice versa. Compared to an L -length DFT, the $s_{_{N}}$ summation/overlap causes decimation in frequency, leaving only DTFT samples least affected by spectral leakage. That is usually a priority when implementing an FFT filter-bank (channelizer). With a conventional window function of length $L,$ scalloping loss would be unacceptable. So multi-block windows are created using FIR filter design tools.  Their frequency profile is flat at the highest point and falls off quickly at the midpoint between the remaining DTFT samples. The larger the value of parameter $I,$ the better the potential performance.

**Case: $L=N+1$**

When a symmetric, L -length window function ( s ) is truncated by 1 coefficient it is called *periodic* or *DFT-even*. That is a common practice, but the truncation affects the DTFT (spectral leakage) by a small amount. It is at least of academic interest to characterize that effect. An N -length DFT of the truncated window produces frequency samples at intervals of $1/N,$ instead of $1/L.$   The samples are real-valued,  but their values do not exactly match the DTFT of the symmetric window. The periodic summation, $s_{_{N}},$ along with an N -length DFT, can also be used to sample the DTFT at intervals of $1/N.$   Those samples are also real-valued and do exactly match the DTFT (example: File:Sampling the Discrete-time Fourier transform.svg). To use the full symmetric window for spectral analysis at the $1/N$ spacing, one would combine the $n=0$ and $n=N$ data samples (by addition, because the symmetrical window weights them equally) and then apply the truncated symmetric window and the N -length DFT.

**Case: Frequency interpolation.** $L\leq N$

In this case, the DFT simplifies to a more familiar form**:**

$S_{k}=\sum _{n=0}^{N-1}s[n]\cdot e^{-i2\pi {\frac {k}{N}}n}.$

In order to take advantage of a fast Fourier transform algorithm for computing the DFT, the summation is usually performed over all N terms, even though $N-L$ of them are zeros. Therefore, the case $L<N$ is often referred to as **zero-padding**.

Spectral leakage, which increases as L decreases, is detrimental to certain important performance metrics, such as resolution of multiple frequency components and the amount of noise measured by each DTFT sample. But those things don't always matter, for instance when the $s[n]$ sequence is a noiseless sinusoid (or a constant), shaped by a window function. Then it is a common practice to use *zero-padding* to graphically display and compare the detailed leakage patterns of window functions. To illustrate that for a rectangular window, consider the sequence:

$s[n]=e^{i2\pi {\frac {1}{8}}n},\quad$

and

$L=64.$

**Figures 2 and 3** are plots of the magnitude of two different sized DFTs, as indicated in their labels. In both cases, the dominant component is at the signal frequency: $f=1/8=0.125$ . Also visible in **Fig 2** is the spectral leakage pattern of the $L=64$ rectangular window. The illusion in **Fig 3** is a result of sampling the DTFT at just its zero-crossings. Rather than the DTFT of a finite-length sequence, it gives the impression of an infinitely long sinusoidal sequence. Contributing factors to the illusion are the use of a rectangular window, and the choice of a frequency (1/8 = 8/64) with exactly 8 (an integer) cycles per 64 samples. A Hann window would produce a similar result, except the peak would be widened to 3 samples (see DFT-even Hann window).

## Convolution

The convolution theorem for sequences is**:**

$s*y\ =\ \scriptstyle {\rm {DTFT}}^{-1}\displaystyle \left[\scriptstyle {\rm {DTFT}}\displaystyle \{s\}\cdot \scriptstyle {\rm {DTFT}}\displaystyle \{y\}\right].$

An important special case is the circular convolution of sequences s and y defined by $s_{_{N}}*y,$ where $s_{_{N}}$ is a periodic summation. The discrete-frequency nature of $\scriptstyle {\rm {DTFT}}\displaystyle \{s_{_{N}}\}$ means that the product with the continuous function $\scriptstyle {\rm {DTFT}}\displaystyle \{y\}$ is also discrete, which results in considerable simplification of the inverse transform**:**

$s_{_{N}}*y\ =\ \scriptstyle {\rm {DTFT}}^{-1}\displaystyle \left[\scriptstyle {\rm {DTFT}}\displaystyle \{s_{_{N}}\}\cdot \scriptstyle {\rm {DTFT}}\displaystyle \{y\}\right]\ =\ \scriptstyle {\rm {DFT}}^{-1}\displaystyle \left[\scriptstyle {\rm {DFT}}\displaystyle \{s_{_{N}}\}\cdot \scriptstyle {\rm {DFT}}\displaystyle \{y_{_{N}}\}\right].$

For s and y sequences whose non-zero duration is less than or equal to N, a final simplification is**:**

$s_{_{N}}*y\ =\ \scriptstyle {\rm {DFT}}^{-1}\displaystyle \left[\scriptstyle {\rm {DFT}}\displaystyle \{s\}\cdot \scriptstyle {\rm {DFT}}\displaystyle \{y\}\right].$

The significance of this result is explained at circular convolution and fast convolution algorithms.

## Relationship to the Z-transform

$S_{2\pi }(\omega )$ is a Fourier series that can also be expressed in terms of the bilateral Z-transform. I.e.**:**

$S_{2\pi }(\omega )=\left.S_{z}(z)\,\right|_{z=e^{i\omega }}=S_{z}(e^{i\omega }),$

where the $S_{z}$ notation distinguishes the Z-transform from the Fourier transform. Therefore, we can also express a portion of the Z-transform in terms of the Fourier transform**:**

${\begin{aligned}S_{z}(e^{i\omega })&=\ S_{1/T}\left({\tfrac {\omega }{2\pi T}}\right)\ =\ \sum _{k=-\infty }^{\infty }S\left({\tfrac {\omega }{2\pi T}}-k/T\right)\\&=\sum _{k=-\infty }^{\infty }S\left({\tfrac {\omega -2\pi k}{2\pi T}}\right).\end{aligned}}$

Note that when parameter T changes, the terms of $S_{2\pi }(\omega )$ remain a constant separation $2\pi$ apart, and their width scales up or down. The terms of *S*1/*T*(*f*) remain a constant width and their separation 1/*T* scales up or down.

## Table of discrete-time Fourier transforms

Some common transform pairs are shown in the table below. The following notation applies**:**

- $\omega =2\pi fT$ is a real number representing continuous angular frequency (in radians per sample). ( f is in cycles/sec, and T is in sec/sample.) In all cases in the table, the DTFT is 2π-periodic (in $\omega$ ).
- $S_{2\pi }(\omega )$ designates a function defined on $-\infty <\omega <\infty$ .
- $S_{o}(\omega )$ designates a function defined on $-\pi <\omega \leq \pi$ , and zero elsewhere. Then: $S_{2\pi }(\omega )\ \triangleq \sum _{k=-\infty }^{\infty }S_{o}(\omega -2\pi k).$
- $\delta (\omega )$ is the Dirac delta function
- $\operatorname {sinc} (t)$ is the normalized sinc function
- $\operatorname {rect} \left[{n \over L}\right]\triangleq {\begin{cases}1&|n|\leq L/2\\0&|n|>L/2\end{cases}}$
- $\operatorname {tri} (t)$ is the triangle function
- n is an integer representing the discrete-time domain (in samples)
- $u[n]$ is the discrete-time unit step function
- $\delta [n]$ is the Kronecker delta $\delta _{n,0}$

| Time domain *s*[*n*] | Frequency domain *S*2*π*(*ω*) | Remarks | Reference |
|---|---|---|---|
| $\delta [n]$ | $S_{2\pi }(\omega )=1$ |   |   |
| $\delta [n-M]$ | $S_{2\pi }(\omega )=e^{-i\omega M}$ | integer M |   |
| $\sum _{m=-\infty }^{\infty }\delta [n-Mm]\!$ | $S_{2\pi }(\omega )=\sum _{m=-\infty }^{\infty }e^{-i\omega Mm}={\frac {2\pi }{M}}\sum _{k=-\infty }^{\infty }\delta \left(\omega -{\frac {2\pi k}{M}}\right)\,$ $S_{o}(\omega )={\frac {2\pi }{M}}\sum _{k=-(M-1)/2}^{(M-1)/2}\delta \left(\omega -{\frac {2\pi k}{M}}\right)\,$     odd *M* $S_{o}(\omega )={\frac {2\pi }{M}}\sum _{k=-M/2+1}^{M/2}\delta \left(\omega -{\frac {2\pi k}{M}}\right)\,$     even *M* | integer $M>0$ |   |
| $u[n]$ | $S_{2\pi }(\omega )={\frac {1}{1-e^{-i\omega }}}+\pi \sum _{k=-\infty }^{\infty }\delta (\omega -2\pi k)\!$ $S_{o}(\omega )={\frac {1}{1-e^{-i\omega }}}+\pi \cdot \delta (\omega )\!$ | The $1/(1-e^{-i\omega })$ term must be interpreted as a distribution in the sense of a Cauchy principal value around its poles at $\omega =2\pi k$ . |   |
| $a^{n}u[n]$ | $S_{2\pi }(\omega )={\frac {1}{1-ae^{-i\omega }}}\!$ | $0<\|a\|<1$ |   |
| $e^{-ian}$ | $S_{o}(\omega )=2\pi \cdot \delta (\omega +a),$     -π < a < π $S_{2\pi }(\omega )=2\pi \sum _{k=-\infty }^{\infty }\delta (\omega +a-2\pi k)$ | real number a |   |
| $\cos(a\cdot n)$ | $S_{o}(\omega )=\pi \left[\delta \left(\omega -a\right)+\delta \left(\omega +a\right)\right],$ $S_{2\pi }(\omega )\ \triangleq \sum _{k=-\infty }^{\infty }S_{o}(\omega -2\pi k)$ | real number a with $-\pi <a<\pi$ |   |
| $\sin(a\cdot n)$ | $S_{o}(\omega )={\frac {\pi }{i}}\left[\delta \left(\omega -a\right)-\delta \left(\omega +a\right)\right]$ | real number a with $-\pi <a<\pi$ |   |
| $\operatorname {rect} \left[{n-M \over N}\right]\equiv \operatorname {rect} \left[{n-M \over N-1}\right]$ | $S_{o}(\omega )={\sin(N\omega /2) \over \sin(\omega /2)}\,e^{-i\omega M}\!$ | integer $M,$ and odd integer N |   |
| $\operatorname {sinc} (W(n+a))$ | $S_{o}(\omega )={\frac {1}{W}}\operatorname {rect} \left({\omega \over 2\pi W}\right)e^{ia\omega }$ | real numbers $W,a$ with $0<W<1$ |   |
| $\operatorname {sinc} ^{2}(Wn)\,$ | $S_{o}(\omega )={\frac {1}{W}}\operatorname {tri} \left({\omega \over 2\pi W}\right)$ | real number W , $0<W<0.5$ |   |
| ${\begin{cases}0&n=0\\{\frac {(-1)^{n}}{n}}&{\text{elsewhere}}\end{cases}}$ | $S_{o}(\omega )=j\omega$ | it works as a differentiator filter |   |
| ${\frac {1}{(n+a)}}\left\{\cos[\pi W(n+a)]-\operatorname {sinc} [W(n+a)]\right\}$ | $S_{o}(\omega )={\frac {j\omega }{W}}\cdot \operatorname {rect} \left({\omega \over \pi W}\right)e^{ja\omega }$ | real numbers $W,a$ with $0<W<1$ |   |
| ${\begin{cases}{\frac {\pi }{2}}&n=0\\{\frac {(-1)^{n}-1}{\pi n^{2}}}&{\text{ otherwise}}\end{cases}}$ | $S_{o}(\omega )=\|\omega \|$ |   |   |
| ${\begin{cases}0;&n{\text{ even}}\\{\frac {2}{\pi n}};&n{\text{ odd}}\end{cases}}$ | $S_{o}(\omega )={\begin{cases}j&\omega <0\\0&\omega =0\\-j&\omega >0\end{cases}}$ | Hilbert transform |   |
| ${\frac {C(A+B)}{2\pi }}\cdot \operatorname {sinc} \left[{\frac {A-B}{2\pi }}n\right]\cdot \operatorname {sinc} \left[{\frac {A+B}{2\pi }}n\right]$ | $S_{o}(\omega )=$ | real numbers $A,B$ complex C |   |

## Properties

This table shows some mathematical operations in the time domain and the corresponding effects in the frequency domain.

- $*\!$ is the discrete convolution of two sequences
- $s^{*}[n]$ is the complex conjugate of $s[n].$

| Property | Time domain *s*[*n*] | Frequency domain $S_{2\pi }(\omega )$ | Remarks | Reference |
|---|---|---|---|---|
| Linearity | $a\cdot s[n]+b\cdot y[n]$ | $a\cdot S_{2\pi }(\omega )+b\cdot Y_{2\pi }(\omega )$ | complex numbers $a,b$ |   |
| Time reversal / frequency reversal | $s[-n]$ | $S_{2\pi }(-\omega )\!$ |   |   |
| Time conjugation | $s^{*}[n]$ | $S_{2\pi }^{*}(-\omega )\!$ |   |   |
| Time reversal & conjugation | $s^{*}[-n]$ | $S_{2\pi }^{*}(\omega )\!$ |   |   |
| Real part in time | $\operatorname {Re} {(s[n])}$ | ${\frac {1}{2}}(S_{2\pi }(\omega )+S_{2\pi }^{*}(-\omega ))$ |   |   |
| Imaginary part in time | $\operatorname {Im} {(s[n])}$ | ${\frac {1}{2i}}(S_{2\pi }(\omega )-S_{2\pi }^{*}(-\omega ))$ |   |   |
| Real part in frequency | ${\frac {1}{2}}(s[n]+s^{*}[-n])$ | $\operatorname {Re} {(S_{2\pi }(\omega ))}$ |   |   |
| Imaginary part in frequency | ${\frac {1}{2i}}(s[n]-s^{*}[-n])$ | $\operatorname {Im} {(S_{2\pi }(\omega ))}$ |   |   |
| Shift in time / modulation in frequency | $s[n-k]$ | $S_{2\pi }(\omega )\cdot e^{-i\omega k}$ | integer k |   |
| Shift in frequency / modulation in time | $s[n]\cdot e^{ian}\!$ | $S_{2\pi }(\omega -a)\!$ | real number a |   |
| Decimation | $s[nM]$ | ${\frac {1}{M}}\sum _{m=0}^{M-1}S_{2\pi }\left({\tfrac {\omega -2\pi m}{M}}\right)\!$ | integer M |   |
| Time expansion | $\scriptstyle {\begin{cases}s[n/M]&n={\text{multiple of M}}\\0&{\text{otherwise}}\end{cases}}$ | $S_{2\pi }(M\omega )\!$ | integer M |   |
| Derivative in frequency | ${\frac {n}{i}}s[n]\!$ | ${\frac {dS_{2\pi }(\omega )}{d\omega }}\!$ |   |   |
| Integration in frequency | $\!$ | $\!$ |   |   |
| Differencing in time | $s[n]-s[n-1]\!$ | $\left(1-e^{-i\omega }\right)S_{2\pi }(\omega )\!$ |   |   |
| Summation in time | $\sum _{m=-\infty }^{n}s[m]\!$ | ${\frac {1}{\left(1-e^{-i\omega }\right)}}S_{2\pi }(\omega )+\pi S(0)\sum _{k=-\infty }^{\infty }\delta (\omega -2\pi k)\!$ |   |   |
| Convolution in time / multiplication in frequency | $s[n]*y[n]\!$ | $S_{2\pi }(\omega )\cdot Y_{2\pi }(\omega )\!$ |   |   |
| Multiplication in time / convolution in frequency | $s[n]\cdot y[n]\!$ | ${\frac {1}{2\pi }}\int _{-\pi }^{\pi }S_{2\pi }(\nu )\cdot Y_{2\pi }(\omega -\nu )d\nu \!$ | Periodic convolution |   |
| Cross correlation | $\rho _{sy}[n]=s^{*}[-n]*y[n]\!$ | $R_{sy}(\omega )=S_{2\pi }^{*}(\omega )\cdot Y_{2\pi }(\omega )\!$ |   |   |
| Parseval's theorem | $E_{sy}=\sum _{n=-\infty }^{\infty }{s[n]\cdot y^{*}[n]}\!$ | $E_{sy}={\frac {1}{2\pi }}\int _{-\pi }^{\pi }{S_{2\pi }(\omega )\cdot Y_{2\pi }^{*}(\omega )d\omega }\!$ |   |   |
