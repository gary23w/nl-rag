---
title: "Nyquist–Shannon sampling theorem"
source: https://en.wikipedia.org/wiki/Nyquist%E2%80%93Shannon_sampling_theorem
domain: waveform-audio
license: CC-BY-SA-4.0
tags: wav audio, pulse-code modulation, audio sampling, riff container
fetched: 2026-07-02
---

# Nyquist–Shannon sampling theorem

The **Nyquist–Shannon sampling theorem** is a theorem in the field of signal processing which serves as a fundamental bridge between continuous-time signals and discrete-time signals. In the case of uniformly spaced (periodic) sampling, it establishes a sufficient condition on the sample rate that permits a discrete sequence of *samples* to capture all the information from a continuous-time signal of finite bandwidth, such that the original signal can be reconstructed exactly from those samples.

Strictly speaking, the theorem only applies to a class of mathematical functions having a Fourier transform that is zero outside of a finite region of frequencies. Intuitively we expect that when one reduces a continuous function to a discrete sequence and interpolates back to a continuous function, the fidelity of the result depends on the density (or sample rate) of the original samples. The sampling theorem introduces the concept of a sample rate that is sufficient for perfect fidelity for the class of functions that are band-limited to a given bandwidth, such that no actual information is lost in the sampling process. It expresses the sufficient sample rate in terms of the bandwidth for the class of functions. The theorem also leads to a formula for perfectly reconstructing the original continuous-time function from the samples.

Perfect reconstruction may still be possible when the sample-rate criterion is not satisfied, provided other constraints on the signal are known (see § Sampling of non-baseband signals below and compressed sensing). In some cases (when the sample-rate criterion is not satisfied), utilizing additional constraints allows for approximate reconstructions. The fidelity of these reconstructions can be verified and quantified utilizing Bochner's theorem.

An important consequence of the sampling theorem is the concept of Nyquist frequency, which holds that in order to reconstruct a bandlimited signal free of aliasing, the sampling rate must be at least twice the signal's bandwidth.

The name *Nyquist–Shannon sampling theorem* honours Harry Nyquist and Claude Shannon, but the theorem was also previously discovered by E. T. Whittaker (published in 1915), and Shannon cited Whittaker's paper in his work. The theorem is thus also known by the names *Whittaker–Shannon sampling theorem*, *Whittaker–Shannon*, and *Whittaker–Nyquist–Shannon*, and may also be referred to as the *cardinal theorem of interpolation*.

## Introduction

Sampling is a process of converting a signal (for example, a function of continuous time or space) into a sequence of values (a function of discrete time or space). Shannon's version of the theorem states:

**Theorem**—If a function $x(t)$ contains no frequencies higher than B hertz, then it can be completely determined from its sampled values at a sequence of points spaced less than $1/(2B)$ seconds apart.

A sufficient sample-rate is therefore anything larger than $2B$ samples per second. Equivalently, for a given sample rate $f_{s}$ , perfect reconstruction is guaranteed possible for a bandlimit $B<f_{s}/2$ .

When the bandlimit is too high (or there is no bandlimit), the reconstruction exhibits imperfections known as aliasing. Modern statements of the theorem are sometimes careful to explicitly state that $x(t)$ must contain no sinusoidal component at exactly frequency $B,$ or that B must be strictly less than one half the sample rate. The threshold $2B$ is called the Nyquist rate and is an attribute of the continuous-time input $x(t)$ to be sampled. The sample rate must exceed the Nyquist rate for the samples to suffice to represent $x(t).$ The threshold $f_{s}/2$ is called the Nyquist frequency and is an attribute of the sampling equipment. All meaningful frequency components of the properly sampled $x(t)$ exist below the Nyquist frequency. The condition described by these inequalities is called the *Nyquist criterion*, or sometimes the *Raabe condition*. The theorem is also applicable to functions of other domains, such as space, in the case of a digitized image. The only change, in the case of other domains, is the units of measure attributed to $t,$ $f_{s},$ and $B.$

The symbol $T\triangleq 1/f_{s}$ is customarily used to represent the interval between adjacent samples and is called the *sample period* or *sampling interval*. The samples of function $x(t)$ are commonly denoted by $x[n]\triangleq T\cdot x(nT)$ (alternatively $x_{n}$ in older signal processing literature), for all integer values of $n.$ The multiplier T is a result of the transition from continuous time to discrete time (see Discrete-time Fourier transform#Relation to Fourier Transform), and it is needed to preserve the energy of the signal as T varies.

A mathematically ideal way to interpolate the sequence involves the use of sinc functions. Each sample in the sequence is replaced by a sinc function, centered on the time axis at the original location of the sample $nT,$ with the amplitude of the sinc function scaled to the sample value, $x(nT).$ Subsequently, the sinc functions are summed into a continuous function. A mathematically equivalent method uses the Dirac comb and proceeds by convolving one sinc function with a series of Dirac delta pulses, weighted by the sample values. Neither method is numerically practical. Instead, some type of approximation of the sinc functions, finite in length, is used. The imperfections attributable to the approximation are known as *interpolation error*.

Practical digital-to-analog converters produce neither scaled and delayed sinc functions, nor ideal Dirac pulses. Instead they produce a piecewise-constant sequence of scaled and delayed rectangular pulses (the zero-order hold), usually followed by a lowpass filter (called an "anti-imaging filter") to remove spurious high-frequency replicas (images) of the original baseband signal.

## Aliasing

When $x(t)$ is a function with a Fourier transform $X(f)$ **:**

$X(f)\ \triangleq \ \int _{-\infty }^{\infty }x(t)\ e^{-i2\pi ft}\ {\rm {d}}t,$

Then the samples $x[n]$ of $x(t)$ are sufficient to create a periodic summation of $X(f).$ (see Discrete-time Fourier transform#Relation to Fourier Transform)**:**

| $X_{1/T}(f)\ \triangleq \sum _{k=-\infty }^{\infty }X\left(f-k/T\right)=\sum _{n=-\infty }^{\infty }x[n]\ e^{-i2\pi fnT},$ |   | Eq.1 |
|---|---|---|

which is a periodic function and its equivalent representation as a Fourier series, whose coefficients are $x[n]$ . This function is also known as the discrete-time Fourier transform (DTFT) of the sample sequence.

As depicted, copies of $X(f)$ are shifted by multiples of the sampling rate $f_{s}=1/T$ and combined by addition. For a band-limited function $(X(f)=0,{\text{ for all }}|f|\geq B)$ and sufficiently large $f_{s},$ it is possible for the copies to remain distinct from each other. But if the Nyquist criterion is not satisfied, adjacent copies overlap, and it is not possible in general to discern an unambiguous $X(f).$ Any frequency component above $f_{s}/2$ is indistinguishable from a lower-frequency component, called an *alias*, associated with one of the copies. In such cases, the customary interpolation techniques produce the alias, rather than the original component. When the sample-rate is pre-determined by other considerations (such as an industry standard), $x(t)$ is usually filtered to reduce its high frequencies to acceptable levels before it is sampled. The type of filter required is a lowpass filter, and in this application it is called an anti-aliasing filter.

## Derivation as a special case of Poisson summation

When there is no overlap of the copies (also known as "images") of $X(f)$ , the $k=0$ term of **Eq.1** can be recovered by the product:

$X(f)=H(f)\cdot X_{1/T}(f),$

where:

$H(f)\ \triangleq \ {\begin{cases}1&|f|<B\\0&|f|>f_{s}-B.\end{cases}}$

The sampling theorem is proved since $X(f)$ uniquely determines $x(t)$ .

All that remains is to derive the formula for reconstruction. $H(f)$ need not be precisely defined in the region $[B,\ f_{s}-B]$ because $X_{1/T}(f)$ is zero in that region. However, the worst case is when $B=f_{s}/2,$ the Nyquist frequency. A function that is sufficient for that and all less severe cases is**:**

$H(f)=\mathrm {rect} \left({\frac {f}{f_{s}}}\right)={\begin{cases}1&|f|<{\frac {f_{s}}{2}}\\0&|f|>{\frac {f_{s}}{2}},\end{cases}}$

where $\mathrm {rect}$ is the rectangular function. Therefore:

$X(f)=\mathrm {rect} \left({\frac {f}{f_{s}}}\right)\cdot X_{1/T}(f)$

$=\mathrm {rect} (Tf)\cdot \sum _{n=-\infty }^{\infty }T\cdot x(nT)\ e^{-i2\pi nTf}$

(from

Eq.1

, above).

$=\sum _{n=-\infty }^{\infty }x(nT)\cdot \underbrace {T\cdot \mathrm {rect} (Tf)\cdot e^{-i2\pi nTf}} _{{\mathcal {F}}\left\{\mathrm {sinc} \left({\frac {t-nT}{T}}\right)\right\}}.$

The inverse transform of both sides produces the Whittaker–Shannon interpolation formula:

$x(t)=\sum _{n=-\infty }^{\infty }x(nT)\cdot \mathrm {sinc} \left({\frac {t-nT}{T}}\right),$

which shows how the samples, $x(nT)$ , can be combined to reconstruct $x(t)$ .

- Larger-than-necessary values of $f_{s}$ (smaller values of T ), called *oversampling*, have no effect on the outcome of the reconstruction and have the benefit of leaving room for a *transition band* in which $H(f)$ is free to take intermediate values. Undersampling, which causes aliasing, is not in general a reversible operation.
- Theoretically, the interpolation formula can be implemented as a low-pass filter, whose impulse response is $\mathrm {sinc} (t/T)$ and whose input is $\textstyle \sum _{n=-\infty }^{\infty }x(nT)\cdot \delta (t-nT),$ which is a Dirac comb function modulated by the signal samples. Practical digital-to-analog converters (DAC) implement an approximation like the zero-order hold. In that case, oversampling can reduce the approximation error.

## Shannon's original proof

Poisson shows that the Fourier series in **Eq.1** produces the periodic summation of $X(f)$ , regardless of $f_{s}$ and B . Shannon, however, only derives the series coefficients for the case $f_{s}=2B$ . Virtually quoting Shannon's original paper:

Let

$X(\omega )$

be the spectrum of

$x(t).$

Then

$x(t)={1 \over 2\pi }\int _{-\infty }^{\infty }X(\omega )e^{i\omega t}\;{\rm {d}}\omega ={1 \over 2\pi }\int _{-2\pi B}^{2\pi B}X(\omega )e^{i\omega t}\;{\rm {d}}\omega ,$

because

$X(\omega )$

is assumed to be zero outside the band

$\left|{\tfrac {\omega }{2\pi }}\right|<B.$

If we let

$t={\tfrac {n}{2B}},$

where

n

is any positive or negative integer, we obtain:

| $x\left({\tfrac {n}{2B}}\right)={1 \over 2\pi }\int _{-2\pi B}^{2\pi B}X(\omega )e^{i\omega {n \over {2B}}}\;{\rm {d}}\omega .$ |   | Eq.2 |
|---|---|---|

On the left are values of

$x(t)$

at the sampling points. The integral on the right will be recognized as essentially

the

$n^{th}$

coefficient in a Fourier-series expansion of the function

$X(\omega ),$

taking the interval

$-B$

to

B

as a fundamental period. This means that the values of the samples

$x(n/2B)$

determine the Fourier coefficients in the series expansion of

$X(\omega ).$

Thus they determine

$X(\omega ),$

since

$X(\omega )$

is zero for frequencies greater than

$B,$

and for lower frequencies

$X(\omega )$

is determined if its Fourier coefficients are determined. But

$X(\omega )$

determines the original function

$x(t)$

completely, since a function is determined if its spectrum is known. Therefore the original samples determine the function

$x(t)$

completely.

Shannon's proof of the theorem is complete at that point, but he goes on to discuss reconstruction via sinc functions, what we now call the Whittaker–Shannon interpolation formula as discussed above. He does not derive or prove the properties of the sinc function, as the Fourier pair relationship between the rect (the rectangular function) and sinc functions was well known by that time.

> Let $x_{n}$ be the $n^{th}$ sample. Then the function $x(t)$ is represented by:
> 
> $x(t)=\sum _{n=-\infty }^{\infty }x_{n}{\sin(\pi (2Bt-n)) \over \pi (2Bt-n)}.$

As in the other proof, the existence of the Fourier transform of the original signal is assumed, so the proof does not say whether the sampling theorem extends to bandlimited stationary random processes.
