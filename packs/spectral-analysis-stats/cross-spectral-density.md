---
title: "Spectral density"
source: https://en.wikipedia.org/wiki/Cross-spectral_density
domain: spectral-analysis-stats
license: CC-BY-SA-4.0
tags: spectral density, periodogram, cross-spectral density, wavelet transform
fetched: 2026-07-02
---

# Spectral density

(Redirected from

Cross-spectral density

)

In signal processing, the power spectrum $S_{xx}(f)$ of a continuous time signal $x(t)$ describes the distribution of power into frequency components f composing that signal. Fourier analysis shows that any physical signal can be decomposed into a distribution of frequencies over a continuous range, where some of the power may be concentrated at discrete frequencies. The statistical average of the energy or power of any type of signal (including noise) as analyzed in terms of its frequency content, is called its **spectral density**.

When the energy of the signal is concentrated around a finite time interval, especially if its total energy is finite, one may compute the **energy spectral density**. More commonly used is the **power spectral density** (PSD, or simply **power spectrum**), which applies to signals existing over *all* time, or over a time period large enough (especially in relation to the duration of a measurement) that it could as well have been over an infinite time interval. The PSD then refers to the spectral power distribution that would be found, since the total energy of such a signal over all time would generally be infinite. Summation or integration of the spectral components yields the total power (for a physical process) or variance (in a statistical process), identical to what would be obtained by integrating $x^{2}(t)$ over the time domain, as dictated by Parseval's theorem.

The spectrum of a physical process $x(t)$ often contains essential information about the nature of x . For instance, the pitch and timbre of a musical instrument can be determined from a spectral analysis. The color of a light source is determined by the spectrum of the electromagnetic wave's electric field $E(t)$ as it oscillates at an extremely high frequency. Obtaining a spectrum from time series data such as these involves the Fourier transform, and generalizations based on Fourier analysis. In many cases the time domain is not directly captured in practice, such as when a dispersive prism is used to obtain a spectrum of light in a spectrograph, or when a sound is perceived through its effect on the auditory receptors of the inner ear, each of which is sensitive to a particular frequency.

However this article concentrates on situations in which the time series is known (at least in a statistical sense) or directly measured (such as by a microphone sampled by a computer). The power spectrum is important in statistical signal processing and in the statistical study of stochastic processes, as well as in many other branches of physics and engineering. Typically the process is a function of time, but one can similarly discuss data in the spatial domain being decomposed in terms of spatial frequency.

## Units

In physics, the signal might be a wave, such as an electromagnetic wave, an acoustic wave, or the vibration of a mechanism. The *power spectral density* (PSD) of the signal describes the power density of the signal as a function of frequency. Power spectral density is commonly expressed in the SI unit watt per hertz (W/Hz).

When a signal is defined in terms of only a voltage varying in time, for instance, there is no specific power associated with a given voltage. In this case "power" is simply reckoned in terms of the square of the signal, as this would always be *proportional* to the actual power delivered by that signal into a given impedance. So one might use the unit V2⋅Hz−1 for the PSD. *Energy spectral density* (ESD) would have the unit V2⋅s⋅Hz−1, since energy is power multiplied by time (e.g., watt-hour).

In the general case, the unit of PSD will be the ratio of unit of variance per unit of frequency; so, for example, a series of displacement values (in meters) over time (in seconds) will have PSD with the unit m2/Hz. In the analysis of random vibrations, the unit *g*02⋅Hz−1 may be used for the PSD of acceleration, where *g*0 denotes standard gravity.

Mathematically, it is not necessary to assign physical dimensions to the signal or to the independent variable. In the following discussion the meaning of *x*(*t*) will remain unspecified, but the independent variable will be assumed to be that of time.

### One-sided vs. two-sided

A PSD can be either a *one-sided* function of only positive frequencies or a *two-sided* function of both positive and negative frequencies but with only half the amplitude. Noise PSDs are generally one-sided in engineering and two-sided in physics.

## Definition

### Energy spectral density

In signal processing, the energy of a signal $x(t)$ is given by $E\triangleq \int _{-\infty }^{\infty }\left|x(t)\right|^{2}\ dt.$ Assuming the total energy is finite (i.e. $x(t)$ is a square-integrable function) allows applying Parseval's theorem (or Plancherel's theorem). That is, $\int _{-\infty }^{\infty }|x(t)|^{2}\,dt=\int _{-\infty }^{\infty }\left|{\hat {x}}(f)\right|^{2}\,df,$ where ${\hat {x}}(f)=\int _{-\infty }^{\infty }e^{-i2\pi ft}x(t)\ dt,$ is the Fourier transform of $x(t)$ at frequency f (in Hz). The theorem also holds true in the discrete-time cases. Since the integral on the left-hand side is the energy of the signal, the value of $\left|{\hat {x}}(f)\right|^{2}df$ can be interpreted as a density function multiplied by an infinitesimally small frequency interval, describing the energy contained in the signal at frequency f in the frequency interval $f+df$ .

Therefore, the **energy spectral density** of $x(t)$ is defined as

| ${\bar {S}}_{xx}(f)\triangleq \left\|{\hat {x}}(f)\right\|^{2}$ |   | Eq.1 |
|---|---|---|

The function ${\bar {S}}_{xx}(f)$ and the autocorrelation of $x(t)$ form a Fourier transform pair, a result also known as the Wiener–Khinchin theorem (see also Periodogram).

As a physical example of how one might measure the energy spectral density of a signal, suppose $V(t)$ represents the potential (in volts) of an electrical pulse propagating along a transmission line of impedance Z , and suppose the line is terminated with a matched resistor (so that all of the pulse energy is delivered to the resistor and none is reflected back). By Ohm's law, the power delivered to the resistor at time t is equal to $V(t)^{2}/Z$ , so the total energy is found by integrating $V(t)^{2}/Z$ with respect to time over the duration of the pulse. To find the value of the energy spectral density ${\bar {S}}_{xx}(f)$ at frequency f , one could insert between the transmission line and the resistor a bandpass filter which passes only a narrow range of frequencies ( $\Delta f$ , say) near the frequency of interest and then measure the total energy $E(f)$ dissipated across the resistor. The value of the energy spectral density at f is then estimated to be $E(f)/\Delta f$ . In this example, since the power $V(t)^{2}/Z$ has the unit V2⋅Ω−1, the energy $E(f)$ has the unit V2⋅s⋅Ω−1 = J, and hence the estimate $E(f)/\Delta f$ of the energy spectral density has the unit J⋅Hz−1. In many situations, it is common to omit the step of dividing by Z so that the energy spectral density instead has the unit V2⋅s·Hz−1.

This definition generalizes in a straightforward manner to a discrete signal with a countably infinite number of values $x_{n}$ such as a signal sampled at discrete times $t_{n}=t_{0}+(n\,\Delta t)$ : ${\bar {S}}_{xx}(f)=\lim _{N\to \infty }(\Delta t)^{2}\underbrace {\left|\sum _{n=-N}^{N}x_{n}e^{-i2\pi fn\,\Delta t}\right|^{2}} _{\left|{\hat {x}}_{d}(f)\right|^{2}},$ where ${\hat {x}}_{d}(f)$ is the discrete-time Fourier transform of $x_{n}.$   The sampling interval $\Delta t$ is needed to keep the correct physical unit and to ensure that we recover the continuous case in the limit $\Delta t\to 0$ . But in the mathematical sciences the interval is often set to 1, which simplifies the results at the expense of generality. (Also see *Normalized frequency (unit)*)

### Power spectral density

The above definition of energy spectral density is suitable for transients (pulse-like signals) whose energy is concentrated around one time window; then the Fourier transforms of the signals generally exist. For continuous signals over all time, one must rather define the *power spectral density* (PSD) which exists for stationary processes; this describes how the power of a signal or time series is distributed over frequency, as in the simple example given previously. Here, power can be the actual physical power, or more often, for convenience with abstract signals, is simply identified with the squared value of the signal. For example, statisticians study the variance of a function over time $x(t)$ (or over another independent variable), and using an analogy with electrical signals (among other physical processes), it is customary to refer to it as the *power spectrum* even when there is no physical power involved. If one were to create a physical voltage source which followed $x(t)$ and applied it to the terminals of a one ohm resistor, then indeed the instantaneous power dissipated in that resistor would be given by $x^{2}(t)$ watts.

The average power P of a signal $x(t)$ over all time is therefore given by the following time average, where the period T is centered about some arbitrary time $t=t_{0}$ : $P=\lim _{T\to \infty }{\frac {1}{T}}\int _{t_{0}-T/2}^{t_{0}+T/2}\left|x(t)\right|^{2}\,dt$

Whenever it is more convenient to deal with time limits in the signal itself rather than time limits in the bounds of the integral, the average power can also be written as $P=\lim _{T\to \infty }{\frac {1}{T}}\int _{-\infty }^{\infty }\left|x_{T}(t)\right|^{2}\,dt,$ where $x_{T}(t)=x(t)w_{T}(t)$ and $w_{T}(t)$ is unity within the arbitrary period and zero elsewhere.

When P is non-zero, the integral must grow to infinity at least as fast as T does. That is the reason why we cannot use the energy of the signal, which is that diverging integral.

In analyzing the frequency content of the signal $x(t)$ , one might like to compute the ordinary Fourier transform ${\hat {x}}(f)$ ; however, for many signals of interest the ordinary Fourier transform does not formally exist. However, under suitable conditions, certain generalizations of the Fourier transform (e.g. the Fourier–Stieltjes transform) still adhere to Parseval's theorem. As such, $P=\lim _{T\to \infty }{\frac {1}{T}}\int _{-\infty }^{\infty }|{\hat {x}}_{T}(f)|^{2}\,df,$ where the integrand defines the **power spectral density**:

| $S_{xx}(f)=\lim _{T\to \infty }{\frac {1}{T}}\|{\hat {x}}_{T}(f)\|^{2}\,$ |   | Eq.2 |
|---|---|---|

The convolution theorem then allows regarding $|{\hat {x}}_{T}(f)|^{2}$ as the Fourier transform of the time convolution of $x_{T}^{*}(-t)$ and $x_{T}(t)$ , where * represents the complex conjugate.

In order to prove the claim below Eq.2, we will find an expression for $[{\hat {x}}_{T}(f)]^{*}$ that will be useful for the purpose. In fact, we will demonstrate that $[{\hat {x}}_{T}(f)]^{*}={\mathcal {F}}\left\{x_{T}^{*}(-t)\right\}$ . Start by noting that ${\begin{aligned}{\mathcal {F}}\left\{x_{T}^{*}(-t)\right\}&=\int _{-\infty }^{\infty }x_{T}^{*}(-t)e^{-i2\pi ft}dt\end{aligned}}$ and let $z=-t$ , so that $z\rightarrow -\infty$ when $t\rightarrow \infty$ and vice versa. So ${\begin{aligned}\int _{-\infty }^{\infty }x_{T}^{*}(-t)e^{-i2\pi ft}dt&=\int _{\infty }^{-\infty }x_{T}^{*}(z)e^{i2\pi fz}\left(-dz\right)\\&=\int _{-\infty }^{\infty }x_{T}^{*}(z)e^{i2\pi fz}dz\\&=\int _{-\infty }^{\infty }x_{T}^{*}(t)e^{i2\pi ft}dt\end{aligned}}$ where, in the last line, use has been made of z and t being dummy variables. So, we have ${\begin{aligned}{\mathcal {F}}\left\{x_{T}^{*}(-t)\right\}&=\int _{-\infty }^{\infty }x_{T}^{*}(-t)e^{-i2\pi ft}dt\\&=\int _{-\infty }^{\infty }x_{T}^{*}(t)e^{i2\pi ft}dt\\&=\int _{-\infty }^{\infty }x_{T}^{*}(t)[e^{-i2\pi ft}]^{*}dt\\&=\left[\int _{-\infty }^{\infty }x_{T}(t)e^{-i2\pi ft}dt\right]^{*}\\&=\left[{\mathcal {F}}\left\{x_{T}(t)\right\}\right]^{*}\\&=\left[{\hat {x}}_{T}(f)\right]^{*}\end{aligned}}$ q.e.d.

Now, let's demonstrate the claim below eq.2 by using the demonstrated identity. In addition, we will make the substitution $u(t)=x_{T}^{*}(-t)$ . In this way, we have: ${\begin{aligned}\left|{\hat {x}}_{T}(f)\right|^{2}&=[{\hat {x}}_{T}(f)]^{*}\cdot {\hat {x}}_{T}(f)\\&={\mathcal {F}}\left\{x_{T}^{*}(-t)\right\}\cdot {\mathcal {F}}\left\{x_{T}(t)\right\}\\&={\mathcal {F}}\left\{u(t)\right\}\cdot {\mathcal {F}}\left\{x_{T}(t)\right\}\\&={\mathcal {F}}\left\{u(t)\mathbin {\mathbf {*} } x_{T}(t)\right\}\\&=\int _{-\infty }^{\infty }\left[\int _{-\infty }^{\infty }u(\tau -t)x_{T}(t)dt\right]e^{-i2\pi f\tau }d\tau \\&=\int _{-\infty }^{\infty }\left[\int _{-\infty }^{\infty }x_{T}^{*}(t-\tau )x_{T}(t)dt\right]e^{-i2\pi f\tau }\ d\tau ,\end{aligned}}$ where the convolution theorem has been used when passing from the 3rd to the 4th line.

Now, if we divide the time convolution above by the period T and take the limit as $T\rightarrow \infty$ , it becomes the autocorrelation function of the non-windowed signal $x(t)$ , which is denoted as $R_{xx}(\tau )$ , provided that $x(t)$ is ergodic, which is true in most, but not all, practical cases. $\lim _{T\to \infty }{\frac {1}{T}}\left|{\hat {x}}_{T}(f)\right|^{2}=\int _{-\infty }^{\infty }\left[\lim _{T\to \infty }{\frac {1}{T}}\int _{-\infty }^{\infty }x_{T}^{*}(t-\tau )x_{T}(t)dt\right]e^{-i2\pi f\tau }\ d\tau =\int _{-\infty }^{\infty }R_{xx}(\tau )e^{-i2\pi f\tau }d\tau$

Assuming the ergodicity of $x(t)$ , the power spectral density can be found once more as the Fourier transform of the autocorrelation function $R_{xx}$ , a property known as the Wiener–Khinchin theorem.

| $S_{xx}(f)=\int _{-\infty }^{\infty }R_{xx}(\tau )e^{-i2\pi f\tau }\,d\tau ={\hat {R}}_{xx}(f)$ |   | Eq.3 |
|---|---|---|

Many authors use this relationship to define the power spectral density in terms of the autocorrelation function instead of the Fourier transform of the signal as we have done.

The power of the signal in a given frequency band $[f_{1},f_{2}]$ , where $0<f_{1}<f_{2}$ , can be calculated by integrating over frequency. Since $S_{xx}(-f)=S_{xx}(f)$ , an equal amount of power can be attributed to positive and negative frequency bands, which accounts for the factor of 2 in the following form (such trivial factors depend on the conventions used): $P_{\textsf {band-limited}}=2\int _{f_{1}}^{f_{2}}S_{xx}(f)\,df$ More generally, similar techniques may be used to estimate a time-varying spectral density. In this case the time interval T is finite rather than approaching infinity. This results in decreased spectral coverage and resolution since frequencies of less than $1/T$ are not sampled, and results at frequencies which are not an integer multiple of $1/T$ are not independent. Just using a single such time series, the estimated power spectrum will be very "noisy"; however this can be alleviated if it is possible to evaluate the expected value (in the above equation) using a large (or infinite) number of short-term spectra corresponding to statistical ensembles of realizations of $x(t)$ evaluated over the specified time window.

Just as with the energy spectral density, the definition of the power spectral density can be generalized to discrete time variables $x_{n}$ . As before, we can consider a window of $-N\leq n\leq N$ with the signal sampled at discrete times $t_{n}=t_{0}+(n\,\Delta t)$ for a total measurement period $T=(2N+1)\,\Delta t$ . $S_{xx}(f)=\lim _{N\to \infty }{\frac {(\Delta t)^{2}}{T}}\left|\sum _{n=-N}^{N}x_{n}e^{-i2\pi fn\,\Delta t}\right|^{2}$ Note that a single estimate of the PSD can be obtained through a finite number of samplings. As before, the actual PSD is achieved when N (and thus T ) approaches infinity and the expected value is formally applied. In a real-world application, one would typically average a finite-measurement PSD over many trials to obtain a more accurate estimate of the theoretical PSD of the physical process underlying the individual measurements. This computed PSD is sometimes called a periodogram. This periodogram converges to the true PSD as the number of estimates as well as the averaging time interval T approach infinity.

If two signals both possess power spectral densities, then the cross-spectral density can similarly be calculated; as the PSD is related to the autocorrelation, so is the cross-spectral density related to the cross-correlation.

#### Properties of the power spectral density

Some properties of the PSD include:

- The power spectrum is always real and non-negative, and the spectrum of a real valued process is also an even function of frequency: $S_{xx}(-f)=S_{xx}(f)$ .
- For a continuous stochastic process x(t), the autocorrelation function *R**xx*(*t*) can be reconstructed from its power spectrum Sxx(f) by using the inverse Fourier transform
- Using Parseval's theorem, one can compute the second moment (average power) of a process by integrating the power spectrum over all frequency: $P=\operatorname {E} (x^{2})=\int _{-\infty }^{\infty }\!S_{xx}(f)\,df$
- For a real process *x*(*t*) with power spectral density $S_{xx}(f)$ , one can compute the *integrated spectrum* or *power spectral distribution* $F(f)$ , which specifies the average *bandlimited* power contained in frequencies from DC to f using: $F(f)=2\int _{0}^{f}S_{xx}(f')\,df'.$ Note that the previous expression for total power (signal variance) is a special case where *f* → ∞.

### Cross power spectral density

Given two signals $x(t)$ and $y(t)$ , each of which possess power spectral densities $S_{xx}(f)$ and $S_{yy}(f)$ , it is possible to define a **cross power spectral density** (**CPSD**) or **cross spectral density** (**CSD**). To begin, let us consider the average power of such a combined signal. ${\begin{aligned}P&=\lim _{T\to \infty }{\frac {1}{T}}\int _{-\infty }^{\infty }\left[x_{T}(t)+y_{T}(t)\right]^{*}\left[x_{T}(t)+y_{T}(t)\right]dt\\&=\lim _{T\to \infty }{\frac {1}{T}}\int _{-\infty }^{\infty }|x_{T}(t)|^{2}+x_{T}^{*}(t)y_{T}(t)+y_{T}^{*}(t)x_{T}(t)+|y_{T}(t)|^{2}dt\\\end{aligned}}$

Using the same notation and methods as used for the power spectral density derivation, we exploit Parseval's theorem and obtain ${\begin{aligned}S_{xy}(f)&=\lim _{T\to \infty }{\frac {1}{T}}\left[{\hat {x}}_{T}^{*}(f){\hat {y}}_{T}(f)\right]&S_{yx}(f)&=\lim _{T\to \infty }{\frac {1}{T}}\left[{\hat {y}}_{T}^{*}(f){\hat {x}}_{T}(f)\right]\end{aligned}}$ where, again, the contributions of $S_{xx}(f)$ and $S_{yy}(f)$ are already understood. Note that $S_{xy}^{*}(f)=S_{yx}(f)$ , so the full contribution to the cross power is, generally, from twice the real part of either individual **CPSD**. Just as before, from here we recast these products as the Fourier transform of a time convolution, which when divided by the period and taken to the limit $T\to \infty$ becomes the Fourier transform of a cross-correlation function. ${\begin{aligned}S_{xy}(f)&=\int _{-\infty }^{\infty }\left[\lim _{T\to \infty }{\frac {1}{T}}\int _{-\infty }^{\infty }x_{T}^{*}(t-\tau )y_{T}(t)dt\right]e^{-i2\pi f\tau }d\tau =\int _{-\infty }^{\infty }R_{xy}(\tau )e^{-i2\pi f\tau }d\tau \\S_{yx}(f)&=\int _{-\infty }^{\infty }\left[\lim _{T\to \infty }{\frac {1}{T}}\int _{-\infty }^{\infty }y_{T}^{*}(t-\tau )x_{T}(t)dt\right]e^{-i2\pi f\tau }d\tau =\int _{-\infty }^{\infty }R_{yx}(\tau )e^{-i2\pi f\tau }d\tau ,\end{aligned}}$ where $R_{xy}(\tau )$ is the cross-correlation of $x(t)$ with $y(t)$ and $R_{yx}(\tau )$ is the cross-correlation of $y(t)$ with $x(t)$ . In light of this, the PSD is seen to be a special case of the CSD for $x(t)=y(t)$ . If $x(t)$ and $y(t)$ are real signals (e.g. voltage or current), their Fourier transforms ${\hat {x}}(f)$ and ${\hat {y}}(f)$ are usually restricted to positive frequencies by convention. Therefore, in typical signal processing, the full **CPSD** is just one of the **CPSD**s scaled by a factor of two. $\operatorname {CPSD} _{\text{Full}}=2S_{xy}(f)=2S_{yx}(f)$

For discrete signals *xn* and *yn*, the relationship between the cross-spectral density and the cross-covariance is $S_{xy}(f)=\sum _{n=-\infty }^{\infty }R_{xy}(\tau _{n})e^{-i2\pi f\tau _{n}}\,\Delta \tau$

## Estimation

The goal of spectral density estimation is to estimate the spectral density of a random signal from a sequence of time samples. Depending on what is known about the signal, estimation techniques can involve parametric or non-parametric approaches, and may be based on time-domain or frequency-domain analysis. For example, a common parametric technique involves fitting the observations to an autoregressive model. A common non-parametric technique is the periodogram.

The spectral density is usually estimated using Fourier transform methods (such as the Welch method), but other techniques such as the maximum entropy method can also be used. In 2026, the unbiased estimation of spectral densities and their higher-order generalisations has been established in the context of polyspectra based on windowed Fourier-transforms and K-statistic.

- The *spectral centroid* of a signal is the midpoint of its spectral density function, i.e. the frequency that divides the distribution into two equal parts.
- The **spectral edge frequency** (**SEF**), usually expressed as "SEF *x*", represents the frequency below which *x* percent of the total power of a given signal are located; typically, *x* is in the range 75 to 95. It is more particularly a popular measure used in EEG monitoring, in which case SEF has variously been used to estimate the depth of anesthesia and stages of sleep.
- A **spectral envelope** is the envelope curve of the spectrum density. It describes one point in time (one window, to be precise). For example, in remote sensing using a spectrometer, the spectral envelope of a feature is the boundary of its spectral properties, as defined by the range of brightness levels in each of the spectral bands of interest.
- The spectral density is a function of frequency, not a function of time. However, the spectral density of a small window of a longer signal may be calculated, and plotted versus time associated with the window. Such a graph is called a *spectrogram*. This is the basis of a number of spectral analysis techniques such as the short-time Fourier transform and wavelets.
- A "spectrum" generally means the power spectral density, as discussed above, which depicts the distribution of signal content over frequency. For transfer functions (e.g., Bode plot, chirp) the complete frequency response may be graphed in two parts: power versus frequency and phase versus frequency—the **phase spectral density**, **phase spectrum**, or **spectral phase**. Less commonly, the two parts may be the real and imaginary parts of the transfer function. This is not to be confused with the *frequency response* of a transfer function, which also includes a phase (or equivalently, a real and imaginary part) as a function of frequency. The time-domain impulse response $h(t)$ cannot generally be uniquely recovered from the power spectral density alone without the phase part. Although these are also Fourier transform pairs, there is no symmetry (as there is for the autocorrelation) forcing the Fourier transform to be real-valued. See Ultrashort pulse#Spectral phase, phase noise, group delay.
- Sometimes one encounters an **amplitude spectral density** (**ASD**), which is the square root of the PSD; the ASD of a voltage signal has the unit V⋅Hz−1/2. This is useful when the *shape* of the spectrum is rather constant, since variations in the ASD will then be proportional to variations in the signal's voltage level itself. But it is mathematically preferred to use the PSD, since only in that case is the area under the curve meaningful in terms of actual power over all frequency or over a specified bandwidth.

## Applications

Any signal that can be represented as a variable that varies in time has a corresponding frequency spectrum. This includes familiar entities such as visible light (perceived as color), musical notes (perceived as pitch), radio/TV (specified by their frequency, or sometimes wavelength) and even the regular rotation of the earth. When these signals are viewed in the form of a frequency spectrum, certain aspects of the received signals or the underlying processes producing them are revealed. In some cases the frequency spectrum may include a distinct peak corresponding to a sine wave component. And additionally there may be peaks corresponding to harmonics of a fundamental peak, indicating a periodic signal which is *not* simply sinusoidal. Or a continuous spectrum may show narrow frequency intervals which are strongly enhanced corresponding to resonances, or frequency intervals containing almost zero power as would be produced by a notch filter.

### Electrical engineering

The concept and use of the power spectrum of a signal is fundamental in electrical engineering, especially in electronic communication systems, including radio communications, radars, and related systems, plus passive remote sensing technology. Electronic instruments called spectrum analyzers are used to observe and measure the ***power spectra*** of signals.

The spectrum analyzer measures the magnitude of the short-time Fourier transform (STFT) of an input signal. If the signal being analyzed can be considered a stationary process, the STFT is a good smoothed estimate of its power spectral density.

### Cosmology

Primordial fluctuations, density variations in the early universe, are quantified by a power spectrum which gives the power of the variations as a function of spatial scale.
