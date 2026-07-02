---
title: "Short-time Fourier transform"
source: https://en.wikipedia.org/wiki/Short-time_Fourier_transform
domain: pitch-shifting
license: CC-BY-SA-4.0
tags: audio pitch shifting, pitch shift dsp, autotune pitch correction, formant preserving pitch shift
fetched: 2026-07-02
---

# Short-time Fourier transform

The **short-time Fourier transform** (**STFT**) is a Fourier-related transform used to determine the sinusoidal frequency and phase content of local sections of a signal as it changes over time. In practice, the procedure for computing STFTs is to divide a longer time signal into shorter segments of equal length and then compute the Fourier transform separately on each shorter segment. This reveals the Fourier spectrum on each shorter segment. One then usually plots the changing spectra as a function of time, known as a spectrogram or waterfall plot, such as commonly used in software defined radio (SDR) based spectrum displays. Full bandwidth displays covering the whole range of an SDR commonly use fast Fourier transforms (FFTs).

## Forward STFT

### Continuous-time STFT

Simply, in the continuous-time case, the function to be transformed is multiplied by a window function which is nonzero for only a short period of time. The Fourier transform (a one-dimensional function) of the resulting signal is taken, then the window is slid along the time axis until the end resulting in a two-dimensional representation of the signal. Mathematically, this is written as:

$\mathbf {STFT} \{x(t)\}(\tau ,\omega )\equiv X(\tau ,\omega )=\int _{-\infty }^{\infty }x(t)w(t-\tau )e^{-i\omega t}\,dt$

where $w(\tau )$ is the window function, commonly a Hann window or Gaussian window centered around zero, and $x(t)$ is the signal to be transformed (note the difference between the window function w and the frequency $\omega$ ). $X(\tau ,\omega )$ is essentially the Fourier transform of $x(t)w(t-\tau )$ , a complex function representing the phase and magnitude of the signal over time and frequency. Often phase unwrapping is employed along either or both the time axis, $\tau$ , and frequency axis, $\omega$ , to suppress any jump discontinuity of the phase result of the STFT. The time index $\tau$ is normally considered to be "*slow*" time and usually not expressed in as high resolution as time t . Given that the STFT is essentially a Fourier transform times a window function, the STFT is also called windowed Fourier transform or time-dependent Fourier transform.

### Discrete-time STFT

In the discrete time case, the data to be transformed could be broken up into chunks or frames (which usually overlap each other, to reduce artifacts at the boundary). Each chunk is Fourier transformed, and the complex result is added to a matrix, which records magnitude and phase for each point in time and frequency. This can be expressed as:

$\mathbf {STFT} \{x[n]\}(m,\omega )\equiv X(m,\omega )=\sum _{n=-\infty }^{\infty }x[n]w[n-m]e^{-i\omega n}$

likewise, with signal $x[n]$ and window $w[n]$ . In this case, *m* is discrete and ω is continuous, but in most typical applications the STFT is performed on a computer using the fast Fourier transform, so both variables are discrete and quantized.

The magnitude squared of the STFT yields the spectrogram representation of the power spectral density of the function:

$\operatorname {spectrogram} \{x(t)\}(\tau ,\omega )\equiv |X(\tau ,\omega )|^{2}$

See also the modified discrete cosine transform (MDCT), which is also a Fourier-related transform that uses overlapping windows.

#### Sliding DFT

If only a small number of ω are desired, or if the STFT is desired to be evaluated for every shift *m* of the window, then the STFT may be more efficiently evaluated using a sliding DFT algorithm.

## Inverse STFT

The STFT is invertible, that is, the original signal can be recovered from the transform by the inverse STFT. The most widely accepted way of inverting the STFT is by using the overlap-add (OLA) method, which also allows for modifications to the STFT complex spectrum. This makes for a versatile signal processing method, referred to as the *overlap and add with modifications* method.

### Continuous-time STFT

Given the width and definition of the window function *w*(*t*), we initially require the area of the window function to be scaled so that

$\int _{-\infty }^{\infty }w(\tau )\,d\tau =1.$

It easily follows that

$\int _{-\infty }^{\infty }w(t-\tau )\,d\tau =1\quad \forall \ t$

and

$x(t)=x(t)\int _{-\infty }^{\infty }w(t-\tau )\,d\tau =\int _{-\infty }^{\infty }x(t)w(t-\tau )\,d\tau .$

The continuous Fourier transform is

$X(\omega )=\int _{-\infty }^{\infty }x(t)e^{-i\omega t}\,dt.$

Substituting *x*(*t*) from above:

$X(\omega )=\int _{-\infty }^{\infty }\left[\int _{-\infty }^{\infty }x(t)w(t-\tau )\,d\tau \right]\,e^{-i\omega t}\,dt$

$=\int _{-\infty }^{\infty }\int _{-\infty }^{\infty }x(t)w(t-\tau )\,e^{-i\omega t}\,d\tau \,dt.$

Swapping order of integration:

$X(\omega )=\int _{-\infty }^{\infty }\int _{-\infty }^{\infty }x(t)w(t-\tau )\,e^{-i\omega t}\,dt\,d\tau$

$=\int _{-\infty }^{\infty }\left[\int _{-\infty }^{\infty }x(t)w(t-\tau )\,e^{-i\omega t}\,dt\right]\,d\tau$

$=\int _{-\infty }^{\infty }X(\tau ,\omega )\,d\tau .$

So the Fourier transform can be seen as a sort of phase coherent sum of all of the STFTs of *x*(*t*). Since the inverse Fourier transform is

$x(t)={\frac {1}{2\pi }}\int _{-\infty }^{\infty }X(\omega )e^{+i\omega t}\,d\omega ,$

then *x*(*t*) can be recovered from *X*(τ,ω) as

$x(t)={\frac {1}{2\pi }}\int _{-\infty }^{\infty }\int _{-\infty }^{\infty }X(\tau ,\omega )e^{+i\omega t}\,d\tau \,d\omega .$

or

$x(t)=\int _{-\infty }^{\infty }\left[{\frac {1}{2\pi }}\int _{-\infty }^{\infty }X(\tau ,\omega )e^{+i\omega t}\,d\omega \right]\,d\tau .$

It can be seen, comparing to above that windowed "grain" or "wavelet" of *x*(*t*) is

$x(t)w(t-\tau )={\frac {1}{2\pi }}\int _{-\infty }^{\infty }X(\tau ,\omega )e^{+i\omega t}\,d\omega .$

the inverse Fourier transform of *X*(τ,ω) for τ fixed.

An alternative definition that is valid only in the vicinity of τ, the inverse transform is:

$x(t)={\frac {1}{w(t-\tau )}}{\frac {1}{2\pi }}\int _{-\infty }^{\infty }X(\tau ,\omega )e^{+i\omega t}\,d\omega .$

In general, the window function $w(t)$ has the following properties:

(a) even symmetry:

$w(t)=w(-t)$

;

(b) non-increasing (for positive time):

$w(t)\geq w(s)$

if

$|t|\leq |s|$

;

(c) compact support:

$w(t)$

is equal to zero when |t| is large.

## Resolution issues

One of the pitfalls of the STFT is that it has a fixed resolution. The width of the windowing function relates to how the signal is represented—it determines whether there is good frequency resolution (frequency components close together can be separated) or good time resolution (the time at which frequencies change). A wide window gives better frequency resolution but poor time resolution. A narrower window gives good time resolution but poor frequency resolution. These are called narrowband and wideband transforms, respectively.

This is one of the reasons for the creation of the wavelet transform and multiresolution analysis, which can give good time resolution for high-frequency events and good frequency resolution for low-frequency events, the combination best suited for many real signals.

This property is related to the Heisenberg uncertainty principle, but not directly – see Gabor limit for discussion. The product of the standard deviation in time and frequency is limited. The boundary of the uncertainty principle (best simultaneous resolution of both) is reached with a Gaussian window function (or mask function), as the Gaussian minimizes the Fourier uncertainty principle. This is called the Gabor transform (and with modifications for multiresolution becomes the Morlet wavelet transform).

One can consider the STFT for varying window size as a two-dimensional domain (time and frequency), as illustrated in the example below, which can be calculated by varying the window size. However, this is no longer a strictly time-frequency representation – the kernel is not constant over the entire signal.

### Examples

When the original function is:

$X(t,f)=\int _{-\infty }^{\infty }w(t-\tau )x(\tau )e^{-j2\pi f\tau }d\tau$

We can have a simple example:

w(t) = 1 for |t| smaller than or equal B

w(t) = 0 otherwise

B = window

Now the original function of the Short-time Fourier transform can be changed as

$X(t,f)=\int _{t-B}^{t+B}x(\tau )e^{-j2\pi f\tau }d\tau$

Another example:

Using the following sample signal $x(t)$ that is composed of a set of four sinusoidal waveforms joined together in sequence. Each waveform is only composed of one of four frequencies (10, 25, 50, 100 Hz). The definition of $x(t)$ is:

$x(t)={\begin{cases}\cos(2\pi 10t)&0\,\mathrm {s} \leq t<5\,\mathrm {s} \\\cos(2\pi 25t)&5\,\mathrm {s} \leq t<10\,\mathrm {s} \\\cos(2\pi 50t)&10\,\mathrm {s} \leq t<15\,\mathrm {s} \\\cos(2\pi 100t)&15\,\mathrm {s} \leq t<20\,\mathrm {s} \\\end{cases}}$

Then it is sampled at 400 Hz. The following spectrograms were produced:

|   |   |
|---|---|
|   |   |

The 25 ms window allows us to identify a precise time at which the signals change but the precise frequencies are difficult to identify. At the other end of the scale, the 1000 ms window allows the frequencies to be precisely seen but the time between frequency changes is blurred.

Other examples:

$w(t)=exp(\sigma -t^{2})$

Normally we call $exp(\sigma -t^{2})$ a Gaussian function or Gabor function. When we use it, the short-time Fourier transform is called the "Gabor transform".

### Explanation

It can also be explained with reference to the sampling and Nyquist frequency.

Take a window of *N* samples from an arbitrary real-valued signal at sampling rate *f*s . Taking the Fourier transform produces *N* complex coefficients. Of these coefficients only half are useful (the last *N/2* being the complex conjugate of the first *N/2* in reverse order, as this is a real valued signal).

These *N/2* coefficients represent the frequencies 0 to *f*s/2 (Nyquist) and two consecutive coefficients are spaced apart by *f*s/*N* Hz.

To increase the frequency resolution of the window the frequency spacing of the coefficients needs to be reduced. There are only two variables, but decreasing *f*s (and keeping *N* constant) will cause the window size to increase — since there are now fewer samples per unit time. The other alternative is to increase *N*, but this again causes the window size to increase. So any attempt to increase the frequency resolution causes a larger window size and therefore a reduction in time resolution—and vice versa.

## Rayleigh frequency

As the Nyquist frequency is a limitation in the maximum frequency that can be meaningfully analysed, so is the Rayleigh frequency a limitation on the minimum frequency.

The Rayleigh frequency is the minimum frequency that can be resolved by a finite duration time window.

Given a time window that is Τ seconds long, the minimum frequency that can be resolved is 1/Τ Hz.

The Rayleigh frequency is an important consideration in applications of the short-time Fourier transform (STFT), as well as any other method of harmonic analysis on a signal of finite record-length.

## Application

STFTs as well as standard Fourier transforms and other tools are frequently used to analyze music. The spectrogram can, for example, show frequency on the horizontal axis, with the lowest frequencies at left, and the highest at the right. The height of each bar (augmented by color) represents the amplitude of the frequencies within that band. The depth dimension represents time, where each new bar was a separate distinct transform. Audio engineers use this kind of visual to gain information about an audio sample, for example, to locate the frequencies of specific noises (especially when used with greater frequency resolution) or to find frequencies which may be more or less resonant in the space where the signal was recorded. This information can be used for equalization or tuning other audio effects.

## Implementation

Original function

$X(t,f)=\int _{-\infty }^{\infty }w(t-\tau )x(\tau )e^{-j2\pi f\tau }d\tau$

Converting into the discrete form:

$t=n\Delta _{t},f=m\Delta _{f},\tau =p\Delta _{t}$

$X(n\Delta _{t},m\Delta _{f})=\sum _{-\infty }^{\infty }w((n-p)\Delta _{t})x(p\Delta _{t})e^{-j2\pi pm\Delta _{t}\Delta _{f}}\Delta _{t}$

Suppose that

$w(t)\cong 0{\text{ for }}|t|>B,{\frac {B}{\Delta _{t}}}=Q$

Then we can write the original function into

$X(n\Delta _{t},m\Delta _{f})=\sum _{p=n-Q}^{n+Q}w((n-p)\Delta _{t})x(p\Delta _{t})e^{-j2\pi pm\Delta _{t}\Delta _{f}}\Delta _{t}$

### Direct implementation

#### Constraints

a. Nyquist criterion (avoiding the aliasing effect):

$\Delta _{t}<{\frac {1}{2\Omega }}$

, where

$\Omega$

is the bandwidth of

$x(\tau )w(t-\tau )$

### FFT-based method

#### Constraint

a. $\Delta _{t}\Delta _{f}={\tfrac {1}{N}}$ , where N is an integer

b. $N\geq 2Q+1$

c. Nyquist criterion (avoiding the aliasing effect):

$\Delta _{t}<{\frac {1}{2\Omega }}$

,

$\Omega$

is the bandwidth of

$x(\tau )w(t-\tau )$

$X(n\Delta _{t},m\Delta _{f})=\sum _{p=n-Q}^{n+Q}w((n-p)\Delta _{t})x(p\Delta _{t})e^{-{\frac {2\pi jpm}{N}}}\Delta _{t}$

${\text{if we have }}q=p-(n-Q),{\text{ then }}p=(n-Q)+q$

$X(n\Delta _{t},m\Delta _{f})=\Delta _{t}e^{\frac {2\pi j(Q-n)m}{N}}\sum _{q=0}^{N-1}x_{1}(q)e^{-{\frac {2\pi jqm}{N}}}$

${\text{where }}x_{1}(q)={\begin{cases}w((Q-q)\Delta _{t})x((n-Q+q)\Delta _{t})&0\leq q\leq 2Q\\0&2Q<q<N\end{cases}}$

### Recursive method

#### Constraint

a. $\Delta _{t}\Delta _{f}={\tfrac {1}{N}}$ , where N is an integer

b. $N\geq 2Q+1$

c. Nyquist criterion (avoiding the aliasing effect):

$\Delta _{t}<{\frac {1}{2\Omega }}$

,

$\Omega$

is the bandwidth of

$x(\tau )w(t-\tau )$

d. Only for implementing the rectangular-STFT

Rectangular window imposes the constraint

$w((n-p)\Delta _{t})=1$

Substitution gives:

${\begin{aligned}X(n\Delta _{t},m\Delta _{f})&=\sum _{p=n-Q}^{n+Q}w((n-p)\Delta _{t})&x(p\Delta _{t})e^{-{\frac {j2\pi pm}{N}}}\Delta _{t}\\&=\sum _{p=n-Q}^{n+Q}&x(p\Delta _{t})e^{-{\frac {j2\pi pm}{N}}}\Delta _{t}\\\end{aligned}}$

Change of variable *n*-1 for *n*:

$X((n-1)\Delta _{t},m\Delta _{f})=\sum _{p=n-1-Q}^{n-1+Q}x(p\Delta _{t})e^{-{\frac {j2\pi pm}{N}}}\Delta _{t}$

Calculate $X(\min {n}\Delta _{t},m\Delta _{f})$ by the *N*-point FFT:

$X(n_{0}\Delta _{t},m\Delta _{f})=\Delta _{t}e^{\frac {j2\pi (Q-n_{0})m}{N}}\sum _{q=0}^{N-1}x_{1}(q)e^{-j{\frac {2\pi qm}{N}}},\qquad n_{0}=\min {(n)}$

where

$x_{1}(q)={\begin{cases}x((n-Q+q)\Delta _{t})&q\leq 2Q\\0&q>2Q\end{cases}}$

Applying the recursive formula to calculate $X(n\Delta _{t},m\Delta _{f})$

$X(n\Delta _{t},m\Delta _{f})=X((n-1)\Delta _{t},m\Delta _{f})-x((n-Q-1)\Delta _{t})e^{-{\frac {j2\pi (n-Q-1)m}{N}}}\Delta _{t}+x((n+Q)\Delta _{t})e^{-{\frac {j2\pi (n+Q)m}{N}}}\Delta _{t}$

### Chirp Z transform

#### Constraint

$\exp {(-j2\pi pm\Delta _{t}\Delta _{f})}=\exp {(-j\pi p^{2}\Delta _{t}\Delta _{f})}\cdot \exp {(j\pi (p-m)^{2}\Delta _{t}\Delta _{f})}\cdot \exp {(-j\pi m^{2}\Delta _{t}\Delta _{f})}$

so

$X(n\Delta _{t},m\Delta _{f})=\Delta _{t}\sum _{p=n-Q}^{n+Q}w((n-p)\Delta _{t})x(p\Delta _{t})e^{-j2\pi pm\Delta _{t}\Delta _{f}}$

$X(n\Delta _{t},m\Delta _{f})=\Delta _{t}e^{-j2\pi m^{2}\Delta _{t}\Delta _{f}}\sum _{p=n-Q}^{n+Q}w((n-p)\Delta _{t})x(p\Delta _{t})e^{-j\pi p^{2}\Delta _{t}\Delta _{f}}e^{j\pi (p-m)^{2}\Delta _{t}\Delta _{f}}$

### Implementation comparison

| Method | Complexity |
|---|---|
| Direct implementation | $O(TFQ)$ |
| FFT-based | $O(TN\log _{2}N)$ |
| Recursive | $O(TF)$ |
| Chirp Z transform | $O(TN\log _{2}N)$ |
