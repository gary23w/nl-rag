---
title: "Window function"
source: https://en.wikipedia.org/wiki/Window_function
domain: dsp
license: CC-BY-SA-4.0
tags: dsp, digital signal processing, fft, fourier transform, digital filter, sampling rate
fetched: 2026-07-02
---

# Window function

In signal processing and statistics, a **window function** (also known as an **apodization function** or **tapering function**) is a mathematical function that is zero-valued outside of some chosen interval. Typically, window functions are symmetric around the middle of the interval, approach a maximum in the middle, and taper away from the middle. Mathematically, when another function or waveform/data-sequence is "multiplied" by a window function, the product is also zero-valued outside the interval: all that is left is the part where they overlap, the "view through the window". Equivalently, and in actual practice, the segment of data within the window is first isolated, and then only that data is multiplied by the window function values. Thus, tapering, not segmentation, is the main purpose of window functions.

The reasons for examining segments of a longer function include detection of transient events and time-averaging of frequency spectra. The duration of the segments is determined in each application by requirements like time and frequency resolution. But that method also changes the frequency content of the signal by an effect called spectral leakage. Window functions allow us to distribute the leakage spectrally in different ways, according to the needs of the particular application. There are many choices detailed in this article, but many of the differences are so subtle as to be insignificant in practice.

In typical applications, the window functions used are non-negative, smooth, "bell-shaped" curves. Rectangle, triangle, and other functions can also be used. A more general definition of window functions does not require them to be identically zero outside an interval, as long as the product of the window multiplied by its argument is square integrable, and, more specifically, that the function goes sufficiently rapidly toward zero.

## Applications

Window functions are used in spectral analysis/modification/resynthesis, the design of finite impulse response filters, merging multiscale and multidimensional datasets, as well as beamforming and antenna design.

### Spectral analysis

The Fourier transform of the function cos(*ωt*) is zero, except at frequency ±*ω*. However, many other functions and waveforms do not have convenient closed-form transforms. Alternatively, one might be interested in their spectral content only during a certain time period.

In either case, the Fourier transform (or a similar transform) can be applied on one or more finite intervals of the waveform. In general, the transform is applied to the product of the waveform and a window function. Any window (including rectangular) affects the spectral estimate computed by this method.

### Filter design

Windows are sometimes used in the design of digital filters, in particular to convert an "ideal" impulse response of infinite duration, such as a sinc function, to a finite impulse response (FIR) filter design. That is called the *window method*.

### Statistics and curve fitting

Window functions are sometimes used in the field of statistical analysis to restrict the set of data being analyzed to a range near a given point, with a weighting factor that diminishes the effect of points farther away from the portion of the curve being fit. In the field of Bayesian analysis and curve fitting, this is often referred to as the kernel.

### Rectangular window applications

#### Analysis of transients

When analyzing a transient signal in modal analysis, such as an impulse, a shock response, a sine burst, a chirp burst, or noise burst, where the energy vs time distribution is extremely uneven, the rectangular window may be most appropriate. For instance, when most of the energy is located at the beginning of the recording, a non-rectangular window attenuates most of the energy, degrading the signal-to-noise ratio.

#### Harmonic analysis

One might wish to measure the harmonic content of a musical note from a particular instrument or the harmonic distortion of an amplifier at a given frequency. Referring again to **Figure 2**, we can observe that there is no leakage at a discrete set of harmonically-related frequencies sampled by the discrete Fourier transform (DFT). (The spectral nulls are actually zero-crossings, which cannot be shown on a logarithmic scale such as this.) This property is unique to the rectangular window, and it must be appropriately configured for the signal frequency, as described above.

## Overlapping windows

When the length of a data set to be transformed is larger than necessary to provide the desired frequency resolution, a common practice is to subdivide it into smaller sets and window them individually. To mitigate the "loss" at the edges of the window, the individual sets may overlap in time. See Welch method of power spectral analysis and the modified discrete cosine transform.

## Two-dimensional windows

Two-dimensional windows are commonly used in image processing to reduce unwanted high-frequencies in the image Fourier transform. They can be constructed from one-dimensional windows in either of two forms. The separable form, $W(m,n)=w(m)w(n)$ is trivial to compute. The radial form, $W(m,n)=w(r)$ , which involves the radius $r={\sqrt {(m-M/2)^{2}+(n-N/2)^{2}}}$ , is isotropic, independent on the orientation of the coordinate axes. Only the Gaussian function is both separable and isotropic. The separable forms of all other window functions have corners that depend on the choice of the coordinate axes. The isotropy/anisotropy of a two-dimensional window function is shared by its two-dimensional Fourier transform. The difference between the separable and radial forms is akin to the result of diffraction from rectangular vs. circular apertures, which can be visualized in terms of the product of two sinc functions vs. an Airy function, respectively.

## Examples of window functions

Conventions**:**

- $w_{0}(x)$ is a zero-phase function (symmetrical about $x=0$ ), continuous for $x\in [-N/2,N/2],$ where N is a positive integer (even or odd).
- The sequence $\{w[n]=w_{0}(n-N/2),\quad 0\leq n\leq N\}$ is *symmetric*, of length $N+1.$
- $\{w[n],\quad 0\leq n\leq N-1\}$ is *DFT-symmetric*, of length $N.$

- The parameter **B** displayed on each spectral plot is the function's noise equivalent bandwidth metric, in units of *DFT bins*.
  - See spectral leakage §§ Discrete-time signals and Some window metrics and Normalized frequency for understanding the use of "bins" for the x-axis in these plots.

The sparse sampling of a discrete-time Fourier transform (DTFT) such as the DFTs in Fig 2 only reveals the leakage into the DFT bins from a sinusoid whose frequency is also an integer DFT bin. The unseen sidelobes reveal the leakage to expect from sinusoids at other frequencies. Therefore, when choosing a window function, it is usually important to sample the DTFT more densely (as we do throughout this section) and choose a window that suppresses the sidelobes to an acceptable level.

### Rectangular window

The rectangular window (sometimes known as the **boxcar** or uniform or **Dirichlet window** or misleadingly as "no window" in some programs) is the simplest window, equivalent to replacing all but *N* consecutive values of a data sequence by zeros, making the waveform suddenly turn on and off:

$w[n]=1.$

Other windows are designed to moderate these sudden changes, to reduce scalloping loss and improve dynamic range (described in § Spectral analysis).

The rectangular window is the 1st-order *B*-spline window as well as the 0th-power power-of-sine window.

The rectangular window provides the minimum mean square error estimate of the Discrete-time Fourier transform, at the cost of other issues discussed.

### *B*-spline windows

*B*-spline windows can be obtained as *k*-fold convolutions of the rectangular window. They include the rectangular window itself (*k* = 1), the § Triangular window (*k* = 2) and the § Parzen window (*k* = 4). Alternative definitions sample the appropriate normalized *B*-spline basis functions instead of convolving discrete-time windows. A *k*th-order *B*-spline basis function is a piece-wise polynomial function of degree *k* − 1 that is obtained by *k*-fold self-convolution of the rectangular function.

#### Triangular window

Triangular windows are given by

$w[n]=1-\left|{\frac {n-{\frac {N}{2}}}{\frac {L}{2}}}\right|,\quad 0\leq n\leq N,$

where *L* can be *N*, *N* + 1, or *N* + 2. The first one is also known as **Bartlett window** or **Fejér window**. All three definitions converge at large *N*.

The triangular window is the 2nd-order *B*-spline window. The *L* = *N* form can be seen as the convolution of two N⁄2-width rectangular windows. The Fourier transform of the result is the squared values of the transform of the half-width rectangular window.

#### Parzen window

Defining *L* ≜ *N* + 1, the Parzen window, also known as the **de la Vallée Poussin window**, is the 4th-order *B*-spline window given by

$w_{0}(n)\triangleq \left\{{\begin{array}{ll}1-6\left({\frac {n}{L/2}}\right)^{2}\left(1-{\frac {|n|}{L/2}}\right),&0\leq |n|\leq {\frac {L}{4}}\\2\left(1-{\frac {|n|}{L/2}}\right)^{3}&{\frac {L}{4}}<|n|\leq {\frac {L}{2}}\\\end{array}}\right\}$

$w[n]=\ w_{0}\left(n-{\tfrac {N}{2}}\right),\ 0\leq n\leq N$

### Other polynomial windows

#### Welch window

The Welch window consists of a single parabolic section:

$w[n]=1-\left({\frac {n-{\frac {N}{2}}}{\frac {N}{2}}}\right)^{2},\quad 0\leq n\leq N.$

Alternatively, it can be written as two factors, as in a beta distribution:

$w[n]=\left(1+{\frac {n-{\frac {N}{2}}}{\frac {N}{2}}}\right)\left(1-{\frac {n-{\frac {N}{2}}}{\frac {N}{2}}}\right),\quad 0\leq n\leq N.$

The defining quadratic polynomial reaches a value of zero at the samples just outside the span of the window.

The Welch window is fairly close to the sine window, and just as the power-of-sine windows are a useful parameterized family, the power-of-Welch window family is similarly useful. Powers of the Welch or parabolic window are also symmetric beta distributions, and are purely algebraic functions (if the powers are rational), as opposed to most windows that are transcendental functions. If different exponents are used on the two factors in the Welch polynomial, the result is a general beta distribution, which is useful for making asymmetric window functions.

### Raised-cosine windows

Windows in the form of a cosine function offset by a constant, such as the popular Hamming and Hann windows, are sometimes called raised-cosine windows. The Hann window is particularly like the raised cosine distribution, which goes smoothly to zero at its ends.

The raised-cosine windows have the form:

$w[n]=a_{0}-(1-a_{0})\cdot \cos \left({\tfrac {2\pi n}{N}}\right),\quad 0\leq n\leq N,$

or alternatively as their zero-phase versions:

${\begin{aligned}w_{0}(n)\ &=w\left[n+{\tfrac {N}{2}}\right]\\&=a_{0}+(1-a_{0})\cdot \cos \left({\tfrac {2\pi n}{N}}\right),\quad -{\tfrac {N}{2}}\leq n\leq {\tfrac {N}{2}}.\end{aligned}}$

#### Hann window

Setting $a_{0}=0.5;\quad a_{1}=-0.5$ produces a **Hann window**:

$w[n]=\sum _{l=0}^{L-1}a_{l}\cos \left({\frac {2\pi ln}{N}}\right)=0.5-0.5\cos \left({\frac {2\pi n}{N}}\right)$

named after Julius von Hann, and sometimes referred to as *Hanning*, which derived from the verb "to Hann". It is also known as the **raised cosine**, because of its similarity to a raised-cosine distribution.

This function is a member of both the cosine-sum and power-of-sine families. Unlike the Hamming window, the end points of the Hann window just touch zero. The resulting side-lobes roll off at about 18 dB per octave.

#### Hamming window

Setting $a_{0}$ to approximately 0.54, or more precisely 25/46, produces the **Hamming window**, proposed by Richard W. Hamming. This choice places a zero crossing at frequency 5π/(*N* − 1), which cancels the first sidelobe of the Hann window, giving it a height of about one-fifth that of the Hann window. The Hamming window is often called the **Hamming blip** when used for pulse shaping.

Approximation of the coefficients to two decimal places substantially lowers the level of sidelobes, to a nearly equiripple condition. In the equiripple sense, the optimal values for the coefficients are *a*0 = 0.53836 and *a*1 = 0.46164.

### Cosine-sum windows

This family, which generalizes the raised-cosine windows, is also known as generalized cosine windows.

| $w[n]=\sum _{k=0}^{K}(-1)^{k}a_{k}\;\cos \left({\frac {2\pi kn}{N}}\right),\quad 0\leq n\leq N.$ |   | Eq.1 |
|---|---|---|

In most cases, including the examples below, all coefficients *a**k* ≥ 0. These windows have only 2*K* + 1 non-zero *N*-point DFT coefficients.

#### Blackman window

Blackman windows are defined as

$w[n]=a_{0}-a_{1}\cos \left({\frac {2\pi n}{N}}\right)+a_{2}\cos \left({\frac {4\pi n}{N}}\right),$

$a_{0}={\frac {1-\alpha }{2}};\quad a_{1}={\frac {1}{2}};\quad a_{2}={\frac {\alpha }{2}}.$

By common convention, the unqualified term *Blackman window* refers to Blackman's "not very serious proposal" of *α* = 0.16 (*a*0 = 0.42, *a*1 = 0.5, *a*2 = 0.08), which closely approximates the **exact Blackman**, with *a*0 = 7938/18608 ≈ 0.42659, *a*1 = 9240/18608 ≈ 0.49656, and *a*2 = 1430/18608 ≈ 0.076849. These exact values place zeros at the third and fourth sidelobes, but result in a discontinuity at the edges and a 6 dB/oct fall-off. The truncated coefficients do not null the sidelobes as well, but have an improved 18 dB/oct fall-off.

#### Nuttall window, continuous first derivative

The continuous form of the Nuttall window, $w_{0}(x),$ and its first derivative are continuous everywhere, like the Hann function. That is, the function goes to 0 at *x* = ±*N*/2, unlike the Blackman–Nuttall, Blackman–Harris, and Hamming windows. The Blackman window (*α* = 0.16) is also continuous with continuous derivative at the edge, but the "exact Blackman window" is not.

$w[n]=a_{0}-a_{1}\cos \left({\frac {2\pi n}{N}}\right)+a_{2}\cos \left({\frac {4\pi n}{N}}\right)-a_{3}\cos \left({\frac {6\pi n}{N}}\right)$

$a_{0}=0.355768;\quad a_{1}=0.487396;\quad a_{2}=0.144232;\quad a_{3}=0.012604.$

#### Blackman–Nuttall window

$w[n]=a_{0}-a_{1}\cos \left({\frac {2\pi n}{N}}\right)+a_{2}\cos \left({\frac {4\pi n}{N}}\right)-a_{3}\cos \left({\frac {6\pi n}{N}}\right)$

$a_{0}=0.3635819;\quad a_{1}=0.4891775;\quad a_{2}=0.1365995;\quad a_{3}=0.0106411.$

#### Blackman–Harris window

A generalization of the Hamming family, produced by adding more shifted cosine functions, meant to minimize side-lobe levels

$w[n]=a_{0}-a_{1}\cos \left({\frac {2\pi n}{N}}\right)+a_{2}\cos \left({\frac {4\pi n}{N}}\right)$

$a_{0}=0.4243801;\quad a_{1}=0.4973406;\quad a_{2}=0.0782793.$

#### Flat top window

A flat top window is a partially negative-valued window that has minimal scalloping loss in the frequency domain. That property is desirable for the measurement of amplitudes of sinusoidal frequency components. However, its broad bandwidth results in high noise bandwidth and wider frequency selection, which depending on the application could be a drawback.

Flat top windows can be designed using low-pass filter design methods, or they may be of the usual cosine-sum variety:

${\begin{aligned}w[n]=a_{0}&{}-a_{1}\cos \left({\frac {2\pi n}{N}}\right)+a_{2}\cos \left({\frac {4\pi n}{N}}\right)\\&{}-a_{3}\cos \left({\frac {6\pi n}{N}}\right)+a_{4}\cos \left({\frac {8\pi n}{N}}\right).\end{aligned}}$

The Matlab variant has these coefficients:

$a_{0}=0.21557895;\quad a_{1}=0.41663158;\quad a_{2}=0.277263158;\quad a_{3}=0.083578947;\quad a_{4}=0.006947368.$

Other variations are available, such as sidelobes that roll off at the cost of higher values near the main lobe.

#### Rife–Vincent windows

Rife–Vincent windows are customarily scaled for unity average value, instead of unity peak value. The coefficient values below, applied to **Eq.1**, reflect that custom.

Class I, Order 1 (*K* = 1): $a_{0}=1;\quad a_{1}=1$ Functionally equivalent to the Hann window and power of sine (*α* = 2).

Class I, Order 2 (*K* = 2): $a_{0}=1;\quad a_{1}={\tfrac {4}{3}};\quad a_{2}={\tfrac {1}{3}}$ Functionally equivalent to the power of sine (*α* = 4).

Class I is defined by minimizing the high-order sidelobe amplitude. Coefficients for orders up to K=4 are tabulated.

Class II minimizes the main-lobe width for a given maximum side-lobe.

Class III is a compromise for which order *K* = 2 resembles the § Blackman window.

### Sine window

$w[n]=\sin \left({\frac {\pi n}{N}}\right)=\cos \left({\frac {\pi n}{N}}-{\frac {\pi }{2}}\right),\quad 0\leq n\leq N.$

The corresponding $w_{0}(n)\,$ function is a cosine without the π/2 phase offset. So the *sine window* is sometimes also called *cosine window*. As it represents half a cycle of a sinusoidal function, it is also known variably as *half-sine window* or *half-cosine window*.

The autocorrelation of a sine window produces a function known as the Bohman window.

#### Power-of-sine/cosine windows

These window functions have the form:

$w[n]=\sin ^{\alpha }\left({\frac {\pi n}{N}}\right)=\cos ^{\alpha }\left({\frac {\pi n}{N}}-{\frac {\pi }{2}}\right),\quad 0\leq n\leq N.$

The rectangular window (*α* = 0), the sine window (*α* = 1), and the Hann window (*α* = 2) are members of this family.

For even-integer values of α these functions can also be expressed in cosine-sum form:

$w[n]=a_{0}-a_{1}\cos \left({\frac {2\pi n}{N}}\right)+a_{2}\cos \left({\frac {4\pi n}{N}}\right)-a_{3}\cos \left({\frac {6\pi n}{N}}\right)+a_{4}\cos \left({\frac {8\pi n}{N}}\right)-...$

${\begin{array}{l|llll}\hline \alpha &a_{0}&a_{1}&a_{2}&a_{3}&a_{4}\\\hline 0&1\\2&0.5&0.5\\4&0.375&0.5&0.125\\6&0.3125&0.46875&0.1875&0.03125\\8&0.2734375&0.4375&0.21875&0.0625&7.8125\times 10^{-3}\\\hline \end{array}}$

### Adjustable windows

#### Gaussian window

The Fourier transform of a Gaussian is also a Gaussian. Since the support of a Gaussian function extends to infinity, it must either be truncated at the ends of the window, or itself windowed with another zero-ended window.

Since the log of a Gaussian produces a parabola, this can be used for nearly exact quadratic interpolation in frequency estimation.

$w[n]=\exp \left(-{\frac {1}{2}}\left({\frac {n-N/2}{\sigma N/2}}\right)^{2}\right),\quad 0\leq n\leq N.$

$\sigma \leq \;0.5\,$

The standard deviation of the Gaussian function is *σ* · *N*/2 sampling periods.

#### Confined Gaussian window

The confined Gaussian window yields the smallest possible root mean square frequency width *σ**ω* for a given temporal width (*N* + 1) *σ**t*. These windows optimize the RMS time-frequency bandwidth products. They are computed as the minimum eigenvectors of a parameter-dependent matrix. The confined Gaussian window family contains the § Sine window and the § Gaussian window in the limiting cases of large and small *σ**t*, respectively.

#### Approximate confined Gaussian window

Defining *L* ≜ *N* + 1, a confined Gaussian window of temporal width *L* × *σ**t* is well approximated by:

$w[n]=G(n)-{\frac {G(-{\tfrac {1}{2}})[G(n+L)+G(n-L)]}{G(-{\tfrac {1}{2}}+L)+G(-{\tfrac {1}{2}}-L)}}$

where G is a Gaussian function:

$G(x)=\exp \left(-\left({\cfrac {x-{\frac {N}{2}}}{2L\sigma _{t}}}\right)^{2}\right)$

The standard deviation of the approximate window is asymptotically equal (i.e. large values of *N*) to *L* × *σ**t* for *σt* < 0.14.

#### Generalized normal window

A more generalized version of the Gaussian window is the generalized normal window. Retaining the notation from the Gaussian window above, we can represent this window as

$w[n,p]=\exp \left(-\left({\frac {n-N/2}{\sigma N/2}}\right)^{p}\right)$

for any even p . At $p=2$ , this is a Gaussian window and as p approaches $\infty$ , this approximates to a rectangular window. The Fourier transform of this window does not exist in a closed form for a general p . However, it demonstrates the other benefits of being smooth, adjustable bandwidth. Like the § Tukey window, this window naturally offers a "flat top" to control the amplitude attenuation of a time-series (on which we don't have a control with Gaussian window). In essence, it offers a good (controllable) compromise, in terms of spectral leakage, frequency resolution and amplitude attenuation, between the Gaussian window and the rectangular window. See also for a study on time-frequency representation of this window (or function).

#### Tukey window

The Tukey window, also known as the *cosine-tapered window*, can be regarded as a cosine lobe of width *Nα*/2 (spanning *Nα*/2 + 1 observations) that is convolved with a rectangular window of width *N*(1 − *α*/2).

$\left.{\begin{array}{lll}w[n]={\frac {1}{2}}\left[1-\cos \left({\frac {2\pi n}{\alpha N}}\right)\right],\quad &0\leq n<{\frac {\alpha N}{2}}\\w[n]=1,\quad &{\frac {\alpha N}{2}}\leq n\leq {\frac {N}{2}}\\w[N-n]=w[n],\quad &0\leq n\leq {\frac {N}{2}}\end{array}}\right\}$

At *α* = 0 it becomes rectangular, and at *α* = 1 it becomes a Hann window.

#### Planck-taper window

The so-called "Planck-taper" window is a bump function that has been widely used in the theory of partitions of unity in manifolds. It is smooth (a $C^{\infty }$ function) everywhere, but is exactly zero outside of a compact region, exactly one over an interval within that region, and varies smoothly and monotonically between those limits. Its use as a window function in signal processing was first suggested in the context of gravitational-wave astronomy, inspired by the Planck distribution. It is defined as a piecewise function**:**

$\left.{\begin{array}{lll}w[0]=0,\\w[n]=\left(1+\exp \left({\frac {\varepsilon N}{n}}-{\frac {\varepsilon N}{\varepsilon N-n}}\right)\right)^{-1},\quad &1\leq n<\varepsilon N\\w[n]=1,\quad &\varepsilon N\leq n\leq {\frac {N}{2}}\\w[N-n]=w[n],\quad &0\leq n\leq {\frac {N}{2}}\end{array}}\right\}$

The amount of tapering is controlled by the parameter *ε*, with smaller values giving sharper transitions.

#### DPSS or Slepian window

The DPSS (discrete prolate spheroidal sequence) or Slepian function, taper, or window maximizes the energy concentration in the main lobe, and is used in multitaper spectral analysis, which averages out noise in the spectrum and reduces information loss at the edges of the window.

The main lobe ends at a frequency bin given by the parameter *α*.

|   |   |
|---|---|

The Kaiser windows below are created by a simple approximation to the DPSS windows:

|   |   |
|---|---|

#### Kaiser window

The Kaiser, or Kaiser–Bessel, window is a simple approximation of the DPSS window using Bessel functions, discovered by James Kaiser.

$w[n]={\frac {I_{0}\left(\pi \alpha {\sqrt {1-\left({\frac {2n}{N}}-1\right)^{2}}}\right)}{I_{0}(\pi \alpha )}},\quad 0\leq n\leq N$

$w_{0}(n)={\frac {I_{0}\left(\pi \alpha {\sqrt {1-\left({\frac {2n}{N}}\right)^{2}}}\right)}{I_{0}(\pi \alpha )}},\quad -N/2\leq n\leq N/2$

where $I_{0}$ is the 0th-order modified Bessel function of the first kind. Variable parameter $\alpha$ determines the tradeoff between main lobe width and side lobe levels of the spectral leakage pattern. The main lobe width, in between the nulls, is given by $2{\sqrt {1+\alpha ^{2}}},$ in units of DFT bins, and a typical value of $\alpha$ is 3.

#### Dolph–Chebyshev window

Minimizes the Chebyshev norm of the side-lobes for a given main lobe width.

The zero-phase Dolph–Chebyshev window function $w_{0}[n]$ is usually defined in terms of its real-valued discrete Fourier transform, $W_{0}[k]$ :

$W_{0}(k)={\frac {T_{N}{\big (}\beta \cos \left({\frac {\pi k}{N+1}}\right){\big )}}{T_{N}(\beta )}}={\frac {T_{N}{\big (}\beta \cos \left({\frac {\pi k}{N+1}}\right){\big )}}{10^{\alpha }}},\ 0\leq k\leq N.$

*T**n*(*x*) is the *n*-th Chebyshev polynomial of the first kind evaluated in *x*, which can be computed using

$T_{n}(x)={\begin{cases}\cos \!{\big (}n\cos ^{-1}(x){\big )}&{\text{if }}-1\leq x\leq 1\\\cosh \!{\big (}n\cosh ^{-1}(x){\big )}&{\text{if }}x\geq 1\\(-1)^{n}\cosh \!{\big (}n\cosh ^{-1}(-x){\big )}&{\text{if }}x\leq -1,\end{cases}}$

and

$\beta =\cosh \!{\big (}{\tfrac {1}{N}}\cosh ^{-1}(10^{\alpha }){\big )}$

is the unique positive real solution to $T_{N}(\beta )=10^{\alpha }$ , where the parameter *α* sets the Chebyshev norm of the sidelobes to −20*α* decibels.

The window function can be calculated from *W*0(*k*) by an inverse discrete Fourier transform (DFT):

$w_{0}(n)={\frac {1}{N+1}}\sum _{k=0}^{N}W_{0}(k)\cdot e^{i2\pi kn/(N+1)},\ -N/2\leq n\leq N/2.$

The *lagged* version of the window can be obtained by:

$w[n]=w_{0}\left(n-{\frac {N}{2}}\right),\quad 0\leq n\leq N,$

which for even values of *N* must be computed as follows:

${\begin{aligned}w_{0}\left(n-{\frac {N}{2}}\right)={\frac {1}{N+1}}\sum _{k=0}^{N}W_{0}(k)\cdot e^{\frac {i2\pi k(n-N/2)}{N+1}}={\frac {1}{N+1}}\sum _{k=0}^{N}\left[\left(-e^{\frac {i\pi }{N+1}}\right)^{k}\cdot W_{0}(k)\right]e^{\frac {i2\pi kn}{N+1}},\end{aligned}}$

which is an inverse DFT of $\left(-e^{\frac {i\pi }{N+1}}\right)^{k}\cdot W_{0}(k).$

Variations:

- Due to the equiripple condition, the time-domain window has discontinuities at the edges. An approximation that avoids them, by allowing the equiripples to drop off at the edges, is a Taylor window.
- An alternative to the inverse DFT definition is also available.[1].

#### Ultraspherical window

The Ultraspherical window was introduced in 1984 by Roy Streit and has application in antenna array design, non-recursive filter design, and spectrum analysis.

Like other adjustable windows, the Ultraspherical window has parameters that can be used to control its Fourier transform main-lobe width and relative side-lobe amplitude. Uncommon to other windows, it has an additional parameter which can be used to set the rate at which side-lobes decrease (or increase) in amplitude.

The window can be expressed in the time-domain as follows:

$w[n]={\frac {1}{N+1}}\left[C_{N}^{\mu }(x_{0})+\sum _{k=1}^{\frac {N}{2}}C_{N}^{\mu }\left(x_{0}\cos {\frac {k\pi }{N+1}}\right)\cos {\frac {2n\pi k}{N+1}}\right]$

where $C_{N}^{\mu }$ is the Ultraspherical polynomial of degree N, and $x_{0}$ and $\mu$ control the side-lobe patterns.

Certain specific values of $\mu$ yield other well-known windows: $\mu =0$ and $\mu =1$ give the Dolph–Chebyshev and Saramäki windows respectively. See here for illustration of Ultraspherical windows with varied parametrization.

#### Exponential or Poisson window

The Poisson window, or more generically the exponential window increases exponentially towards the center of the window and decreases exponentially in the second half. Since the exponential function never reaches zero, the values of the window at its limits are non-zero (it can be seen as the multiplication of an exponential function by a rectangular window ). It is defined by

$w[n]=e^{-\left|n-{\frac {N}{2}}\right|{\frac {1}{\tau }}},$

where *τ* is the time constant of the function. The exponential function decays as *e* ≃ 2.71828 or approximately 8.69 dB per time constant. This means that for a targeted decay of *D* dB over half of the window length, the time constant *τ* is given by

$\tau ={\frac {N}{2}}{\frac {8.69}{D}}.$

### Hybrid windows

Window functions have also been constructed as multiplicative or additive combinations of other windows.

#### Bartlett–Hann window

$w[n]=a_{0}-a_{1}\left|{\frac {n}{N}}-{\frac {1}{2}}\right|-a_{2}\cos \left({\frac {2\pi n}{N}}\right)$

$a_{0}=0.62;\quad a_{1}=0.48;\quad a_{2}=0.38\,$

#### Planck–Bessel window

A § Planck-taper window multiplied by a Kaiser window which is defined in terms of a modified Bessel function. This hybrid window function was introduced to decrease the peak side-lobe level of the Planck-taper window while still exploiting its good asymptotic decay. It has two tunable parameters, *ε* from the Planck-taper and *α* from the Kaiser window, so it can be adjusted to fit the requirements of a given signal.

#### Hann–Poisson window

A Hann window multiplied by a Poisson window. For $\alpha \geqslant 2$ it has no side-lobes, as its Fourier transform drops off forever away from the main lobe without local minima. It can thus be used in hill climbing algorithms like Newton's method. The Hann–Poisson window is defined by:

$w[n]={\frac {1}{2}}\left(1-\cos \left({\frac {2\pi n}{N}}\right)\right)e^{\frac {-\alpha \left|N-2n\right|}{N}}\,$

where *α* is a parameter that controls the slope of the exponential.

### Other windows

#### Generalized adaptive polynomial (GAP) window

The GAP window is a family of adjustable window functions that are based on a symmetrical polynomial expansion of order K . It is continuous with continuous derivative everywhere. With the appropriate set of expansion coefficients and expansion order, the GAP window can mimic all the known window functions, reproducing accurately their spectral properties.

$w_{0}[n]=a_{0}+\sum _{k=1}^{K}a_{2k}\left({\frac {n}{\sigma }}\right)^{2k},\quad -{\frac {N}{2}}\leq n\leq {\frac {N}{2}},$

where $\sigma$ is the standard deviation of the $\{n\}$ sequence.

Additionally, starting with a set of expansion coefficients $a_{2k}$ that mimics a certain known window function, the GAP window can be optimized by minimization procedures to get a new set of coefficients that improve one or more spectral properties, such as the main lobe width, side lobe attenuation, and side lobe falloff rate. Therefore, a GAP window function can be developed with designed spectral properties depending on the specific application.

#### Lanczos window

$w[n]=\operatorname {sinc} \left({\frac {2n}{N}}-1\right)$

- used in Lanczos resampling
- for the Lanczos window, $\operatorname {sinc} (x)$ is defined as $\sin(\pi x)/\pi x$
- also known as a *sinc window*, because: $w_{0}(n)=\operatorname {sinc} \left({\frac {2n}{N}}\right)\,$ is the main lobe of a normalized sinc function

### Asymmetric window functions

The $w_{0}(x)$ form, according to the convention above, is symmetric around $x=0$ . However, there are window functions that are asymmetric, such as the gamma distribution used in FIR implementations of gammatone filters, or the beta distribution for a bounded-support approximation to the gamma distribution. These asymmetries are used to reduce the delay when using large window sizes, or to emphasize the initial transient of a decaying pulse.

Any bounded function with compact support, including asymmetric ones, can be readily used as a window function. Additionally, there are ways to transform symmetric windows into asymmetric windows by transforming the time coordinate, such as with the below formula

$x\leftarrow N\left({\frac {x}{N}}+{\frac {1}{2}}\right)^{\alpha }-{\frac {N}{2}}\,,$

where the window weights more highly the earliest samples when $\alpha >1$ , and conversely weights more highly the latest samples when $\alpha <1$ .
