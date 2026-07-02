---
title: "Finite impulse response"
source: https://en.wikipedia.org/wiki/Finite_impulse_response
domain: dsp
license: CC-BY-SA-4.0
tags: dsp, digital signal processing, fft, fourier transform, digital filter, sampling rate
fetched: 2026-07-02
---

# Finite impulse response

In signal processing, a **finite impulse response** (**FIR**) **filter** is a filter whose impulse response (or response to any finite length input) is of *finite* duration, because it settles to zero in finite time. This is in contrast to infinite impulse response (IIR) filters, which may have internal feedback and may continue to respond indefinitely (usually decaying).

The impulse response (that is, the output in response to a Kronecker delta input) of an Nth-order discrete-time FIR filter lasts exactly $N+1$ samples (from first nonzero element through last nonzero element) before it then settles to zero.

FIR filters can be discrete-time or continuous-time, and digital or analog.

## Definition

For a causal discrete-time FIR filter of order *N*, each value of the output sequence is a weighted sum of the most recent input values**:**

${\begin{aligned}y[n]&=b_{0}x[n]+b_{1}x[n-1]+\cdots +b_{N}x[n-N]\\&=\sum _{i=0}^{N}b_{i}\cdot x[n-i],\end{aligned}}$

where**:**

- ${\textstyle x[n]}$ is the input signal,
- ${\textstyle y[n]}$ is the output signal,
- ${\textstyle N}$ is the filter order; an ${\textstyle N}$ th-order filter has ${\textstyle N+1}$ terms on the right-hand side
- ${\textstyle b_{i}}$ is the value of the impulse response at the *i'*th instant for ${\textstyle 0\leq i\leq N}$ of an ${\textstyle N^{\text{th}}}$ -order FIR filter. If the filter is a direct form FIR filter then ${\textstyle b_{i}}$ is also a coefficient of the filter.

This computation is also known as discrete convolution.

The ${\textstyle x[n-i]}$ in these terms are commonly referred to as *taps*, based on the structure of a tapped delay line that in many implementations or block diagrams provides the delayed inputs to the multiplication operations. One may speak of a *5th order/6-tap filter*, for instance.

The impulse response of the filter as defined is nonzero over a finite duration. Including zeros, the impulse response is the infinite sequence**:**

$h[n]=\sum _{i=0}^{N}b_{i}\cdot \delta [n-i]={\begin{cases}b_{n}&0\leq n\leq N\\0&{\text{otherwise}}.\end{cases}}$

If an FIR filter is non-causal, the range of nonzero values in its impulse response can start before $n=0$ , with the defining formula appropriately generalized.

## Properties

An FIR filter has a number of useful properties which sometimes make it preferable to an infinite impulse response (IIR) filter. FIR filters:

- Require no feedback. This means that any rounding errors are not compounded by summed iterations. The same relative error occurs in each calculation. This also makes implementation simpler.
- Are inherently stable, since the output is a sum of a finite number of finite multiples of the input values, so can be no greater than ${\textstyle \sum |b_{i}|}$ times the largest value appearing in the input.
- Can easily be designed to be linear phase by making the coefficient sequence symmetric. This property is sometimes desired for phase-sensitive applications, for example data communications, seismology, crossover filters, and mastering.

The main disadvantage of FIR filters is that considerably more computation power in a general purpose processor is required compared to an IIR filter with similar sharpness or selectivity, especially when low frequency (relative to the sample rate) cutoffs are needed. However, many digital signal processors provide specialized hardware features to make FIR filters approximately as efficient as IIR for many applications.

## Frequency response

The filter's effect on the sequence $x[n]$ is described in the frequency domain by the convolution theorem**:**

$\underbrace {{\mathcal {F}}\{x*h\}} _{Y(\omega )}=\underbrace {{\mathcal {F}}\{x\}} _{X(\omega )}\cdot \underbrace {{\mathcal {F}}\{h\}} _{H(\omega )}$

and

$y[n]=x[n]*h[n]={\mathcal {F}}^{-1}{\big \{}X(\omega )\cdot H(\omega ){\big \}},$

where operators ${\mathcal {F}}$ and ${\mathcal {F}}^{-1}$ respectively denote the discrete-time Fourier transform (DTFT) and its inverse. Therefore, the complex-valued, multiplicative function $H(\omega )$ is the filter's frequency response. It is defined by a Fourier series**:**

$H_{2\pi }(\omega )\ \triangleq \sum _{n=-\infty }^{\infty }h[n]\cdot \left({e^{i\omega }}\right)^{-n}=\sum _{n=0}^{N}b_{n}\cdot \left({e^{i\omega }}\right)^{-n},$

where the added subscript denotes $2\pi$ -periodicity. Here $\omega$ represents frequency in normalized units (*radians per sample*). The function $H_{2\pi }(2\pi f')$ has a periodicity of 1 with $f'$ in units of *cycles per sample*, which is favored by many filter design applications.  The value $\omega =\pi$ , called Nyquist frequency, corresponds to $f'={\tfrac {1}{2}}.$   When the sequence $x[n]$ has a known sampling-rate $f_{s}$ (in *samples per second*), ordinary frequency is related to normalized frequency by $f=f'\cdot f_{s}={\tfrac {\omega }{2\pi }}\cdot f_{s}$ *cycles per second* (Hz). Conversely, if one wants to design a filter for ordinary frequencies $f_{1},$ $f_{2},$ etc., using an application that expects *cycles per sample*, one would enter $f_{1}/f_{s},$   $f_{2}/f_{s},$   etc.

$H_{2\pi }(\omega )$ can also be expressed in terms of the Z-transform of the filter impulse response:

${\widehat {H}}(z)\ \triangleq \sum _{n=-\infty }^{\infty }h[n]\cdot z^{-n}.$

$H_{2\pi }(\omega )=\left.{\widehat {H}}(z)\,\right|_{z=e^{j\omega }}={\widehat {H}}(e^{j\omega }).$

## Filter design

FIR filters are designed by finding the coefficients and filter order that meet certain specifications, which can be in the time domain (e.g. a matched filter) or the frequency domain (most common). Matched filters perform a cross-correlation between the input signal and a known pulse shape. The FIR convolution is a cross-correlation between the input signal and a time-reversed copy of the impulse response. Therefore, the matched filter's impulse response is "designed" by sampling the known pulse-shape and using those samples in reverse order as the coefficients of the filter.

When a particular frequency response is desired, several different design methods are common:

1. Window design method
2. Frequency sampling method
3. Least MSE (mean square error) method
4. Parks–McClellan method (also known as the equiripple, optimal, or minimax method). The Remez exchange algorithm is commonly used to find an optimal equiripple set of coefficients. Here the user specifies a desired frequency response, a weighting function for errors from this response, and a filter order *N*. The algorithm then finds the set of ${\textstyle N+1}$ coefficients that minimize the maximum deviation from the ideal. Intuitively, this finds the filter that is as close as possible to the desired response given that only ${\textstyle N+1}$ coefficients can be used. This method is particularly easy in practice since at least one text includes a program that takes the desired filter and *N*, and returns the optimum coefficients.
5. Equiripple FIR filters can be designed using the DFT algorithms as well. The algorithm is iterative in nature. The DFT of an initial filter design is computed using the FFT algorithm (if an initial estimate is not available, h[n]=delta[n] can be used). In the Fourier domain, or DFT domain, the frequency response is corrected according to the desired specs, and the inverse DFT is then computed. In the time-domain, only the first N coefficients are kept (the other coefficients are set to zero). The process is then repeated iteratively: the DFT is computed once again, correction applied in the frequency domain and so on.

Software packages such as MATLAB, GNU Octave, Scilab, and SciPy provide convenient ways to apply these different methods.

### Window design method

In the window design method, one first designs an ideal IIR filter and then truncates the infinite impulse response by multiplying it with a finite length window function. The result is a finite impulse response filter whose frequency response is modified from that of the IIR filter. Multiplying the infinite impulse by the window function in the time domain results in the frequency response of the IIR being convolved with the Fourier transform (or DTFT) of the window function. If the window's main lobe is narrow, the composite frequency response remains close to that of the ideal IIR filter.

The ideal frequency response is often an ideal, rectangular low-pass, and the corresponding IIR is a sinc function. The result of the frequency domain convolution is that the edges of the rectangle are tapered, and ripples appear in the passband and stopband. Working backward, one can specify the slope (or width) of the tapered region (*transition band*) and the height of the ripples, and thereby derive the frequency-domain parameters of an appropriate window function. Continuing backward to an impulse response can be done by iterating a filter design program to find the minimum filter order. Another method is to restrict the solution set to the parametric family of Kaiser windows, which provides closed form relationships between the time-domain and frequency domain parameters. In general, that method will not achieve the minimum possible filter order, but it is particularly convenient for automated applications that require dynamic, on-the-fly, filter design.

The window design method is also advantageous for creating efficient half-band filters, because the corresponding sinc function is zero at every other sample point (except the center one). The product with the window function does not alter the zeros, so almost half of the coefficients of the final impulse response are zero. An appropriate implementation of the FIR calculations can exploit that property to double the filter's efficiency.

### Least mean square error (MSE) method

**Goal:**

To design FIR filter in the MSE sense, we minimize the mean square error between the filter we obtained and the desired filter.

${\text{MSE}}=f_{s}^{-1}\int _{-f_{s}/2}^{f_{s}/2}|H(f)-H_{d}(f)|^{2}\,df$

, where

$f_{s}\,$

is sampling frequency,

$H(f)\,$

is the spectrum of the filter we obtained, and

$H_{d}(f)\,$

is the spectrum of the desired filter.

**Method:**

Given an

N

-point FIR filter

$h[n]$

, and

$r[n]=h[n+k],k={\frac {(N-1)}{2}}$

.

Step 1: Suppose

$h[n]$

even symmetric. Then, the discrete time Fourier transform of

$r[n]$

is defined as

$R(F)=e^{j2\pi Fk}H(F)=\sum _{n=0}^{k}s[n]\cos(2\pi nF)$

Step 2: Calculate mean square error.

${\text{MSE}}=\int _{-1/2}^{1/2}|R(F)-H_{d}(F)|^{2}\,dF$

Therefore,

${\text{MSE}}=\int _{-1/2}^{1/2}\sum _{n=0}^{k}s[n]\cos(2\pi nF)\sum _{\tau =0}^{k}s[\tau ]\cos(2\pi \tau F)\,dF-2\int _{-1/2}^{1/2}\sum _{n=0}^{k}s[n]\cos(2\pi nF)H_{d}\,dF+\int _{-1/2}^{1/2}H_{d}(F)^{2}\,dF$

Step 3: Minimize the mean square error by doing partial derivative of MSE with respect to

$s[n]$

${\frac {\partial {\text{MSE}}}{\partial s[n]}}=2\sum _{\tau =0}^{k}s[\tau ]\int _{-1/2}^{1/2}\cos(2\pi nF)\cos(2\pi \tau F)\,dF-2\int _{-1/2}^{1/2}H_{d}(F)^{2}\cos(2\pi nF)\,dF=0$

After organization, we have

$s[0]=\int _{-1/2}^{1/2}H_{d}(F)\,dF$

$s[n]=\int _{-1/2}^{1/2}\cos(2\pi nF)H_{d}(F)\,dF,\ {\text{ for }}n\neq 0$

Step 4: Change

$s[n]$

back to the presentation of

$h[n]$

$h[k]=s[0],h[k+n]=s[n]/2,h[k-n]=s[n]/2,\;for\;n=1,2,3,\ldots ,k,{\text{ where }}k=(N-1)/2$

and

$h[n]=0{\text{ for }}n<0{\text{ and }}n\geq N$

In addition, we can treat the importance of passband and stopband differently according to our needs by adding a weighted function, $W(f)$ Then, the MSE error becomes

${\text{MSE}}=\int _{-1/2}^{1/2}W(F)|R(F)-H_{d}(F)|^{2}\,dF$

## Moving average example

Block diagram of a simple FIR filter (second-order/3-tap filter in this case, implementing a moving average smoothing filter)

Pole–zero diagram

of the example second-order FIR smoothing filter

Magnitude and phase responses of the example second-order FIR smoothing filter

Amplitude and phase responses of the example second-order FIR smoothing filter

A moving average filter is a very simple FIR filter. It is sometimes called a boxcar filter, especially when followed by decimation, or a sinc-in-frequency. The filter coefficients, ${\textstyle b_{0},\ldots ,b_{N}}$ , are found via the following equation:

$b_{i}={\frac {1}{N+1}}$

To provide a more specific example, we select the filter order:

$N=2$

The impulse response of the resulting filter is**:**

$h[n]={\frac {1}{3}}\delta [n]+{\frac {1}{3}}\delta [n-1]+{\frac {1}{3}}\delta [n-2]$

The block diagram on the right shows the second-order moving-average filter discussed below. The transfer function is**:**

$H(z)={\frac {1}{3}}+{\frac {1}{3}}z^{-1}+{\frac {1}{3}}z^{-2}={\frac {1}{3}}{\frac {z^{2}+z+1}{z^{2}}}.$

The next figure shows the corresponding pole–zero diagram. Zero frequency (DC) corresponds to (1, 0), positive frequencies advancing counterclockwise around the circle to the Nyquist frequency at (−1, 0). Two poles are located at the origin, and two zeros are located at ${\textstyle z_{1}=-{\frac {1}{2}}+j{\frac {\sqrt {3}}{2}}}$ , ${\textstyle z_{2}=-{\frac {1}{2}}-j{\frac {\sqrt {3}}{2}}}$ .

The frequency response, in terms of normalized frequency *ω*, is**:**

${\begin{aligned}H\left(e^{j\omega }\right)&={\frac {1}{3}}+{\frac {1}{3}}e^{-j\omega }+{\frac {1}{3}}e^{-j2\omega }\\&={\frac {1}{3}}e^{-j\omega }\left(1+2\cos(\omega )\right).\end{aligned}}$

The magnitude and phase components of ${\textstyle H\left(e^{j\omega }\right)}$ are plotted in the figure. But plots like these can also be generated by doing a discrete Fourier transform (DFT) of the impulse response. And because of symmetry, filter design or viewing software often displays only the [0, π] region. The magnitude plot indicates that the moving-average filter passes low frequencies with a gain near 1 and attenuates high frequencies, and is thus a crude low-pass filter. The phase plot is linear except for discontinuities at the two frequencies where the magnitude goes to zero. The size of the discontinuities is π, representing a sign reversal. They do not affect the property of linear phase, as illustrated in the final figure.
