---
title: "Infinite impulse response"
source: https://en.wikipedia.org/wiki/Infinite_impulse_response
domain: audio-equalization
license: CC-BY-SA-4.0
tags: audio equalization, parametric equalizer, iir filter eq, audio filter dsp
fetched: 2026-07-02
---

# Infinite impulse response

**Infinite impulse response** (**IIR**) is a fundamental property applying to many linear time-invariant systems that are distinguished by having an impulse response $h(t)$ that does not become exactly zero past a certain point but continues indefinitely. This is in contrast to a finite impulse response (FIR) system, in which the impulse response *does* become exactly zero at times $t>T$ for some finite T , thus being of finite duration. Common examples of linear time-invariant systems are most electronic and digital filters. Systems with this property are known as *IIR systems* or *IIR filters*.

In practice, the impulse response, even of IIR systems, usually approaches zero and can be neglected past a certain point. However the physical systems which give rise to IIR or FIR responses are dissimilar, and therein lies the importance of the distinction. For instance, analog electronic filters composed of resistors, capacitors, and/or inductors (and perhaps linear amplifiers) are generally IIR filters. On the other hand, discrete-time filters (usually digital filters) based on a tapped delay line *employing no feedback* are necessarily FIR filters. The capacitors (or inductors) in the analog filter have a "memory" and their internal state never completely relaxes following an impulse (assuming the classical model of capacitors and inductors where quantum effects are ignored). But in the latter case, after an impulse has reached the end of the tapped delay line, the system has no further memory of that impulse and has returned to its initial state; its impulse response beyond that point is exactly zero.

## Implementation and design

Although almost all analog electronic filters are IIR, digital filters may be either IIR or FIR. The presence of feedback in the topology of a discrete-time filter (such as the block diagram shown below) generally creates an IIR response. The z domain transfer function of an IIR filter contains a non-trivial denominator, describing those feedback terms. The transfer function of an FIR filter, on the other hand, has only a numerator as expressed in the general form derived below. All of the $a_{i}$ coefficients with $i>0$ (feedback terms) are zero and the filter has no finite poles.

The transfer functions pertaining to IIR analog electronic filters have been extensively studied and optimized for their amplitude and phase characteristics. These continuous-time filter functions are described in the Laplace domain. Desired solutions can be transferred to the case of discrete-time filters whose transfer functions are expressed in the z domain, through the use of certain mathematical techniques such as the bilinear transform, impulse invariance, or pole–zero matching method. Thus digital IIR filters can be based on well-known solutions for analog filters such as the Chebyshev filter, Butterworth filter, and elliptic filter, inheriting the characteristics of those solutions.

## Transfer function derivation

Digital filters are often described and implemented in terms of the difference equation that defines how the output signal is related to the input signal:

${\begin{aligned}y[n]{}=&b_{0}x[n]+b_{1}x[n-1]+\cdots +b_{P}x[n-P]\\&{}+a_{1}y[n-1]+a_{2}y[n-2]+\cdots +a_{Q}y[n-Q]\end{aligned}}$

where:

- $\ P$ is the feedforward filter order
- $\ b_{i}$ are the feedforward filter coefficients
- $\ Q$ is the feedback filter order
- $\ a_{i}$ are the feedback filter coefficients
- $\ x[n]$ is the input signal
- $\ y[n]$ is the output signal.

A more condensed form of the difference equation is:

$\ y[n]=\sum _{i=0}^{P}b_{i}x[n-i]+\sum _{i=1}^{Q}a_{i}y[n-i]$

To find the transfer function of the filter, we first take the Z-transform of each side of the above equation to obtain:

$\ Y(z)=X(z)\sum _{i=0}^{P}b_{i}z^{-i}+Y(z)\sum _{i=1}^{Q}a_{i}z^{-i}$

After rearranging:

$\ Y(z)\left[1-\sum _{i=1}^{Q}a_{i}z^{-i}\right]=X(z)\sum _{i=0}^{P}b_{i}z^{-i}$

We then define the transfer function to be:

$H(z)={\frac {Y(z)}{X(z)}}={\frac {\sum _{i=0}^{P}b_{i}z^{-i}}{1-\sum _{i=1}^{Q}a_{i}z^{-i}}}$

## Stability

The transfer function allows one to judge whether or not a system is bounded-input, bounded-output (BIBO) stable. To be specific, the BIBO stability criterion requires that the ROC of the system includes the unit circle. For example, for a causal system to be stable, all poles of the transfer function have to have an absolute value smaller than one. In other words, all poles must be located within a unit circle in the z -plane.

The poles are defined as the values of z which make the denominator of $H(z)$ equal to 0:

$\ 0=\sum _{j=0}^{Q}a_{j}z^{-j}$

Clearly, if $a_{j}\neq 0$ then the poles are not located at the origin of the z -plane. This is in contrast to the FIR filter where all poles are located at the origin, and is therefore always stable.

IIR filters are sometimes preferred over FIR filters because an IIR filter can achieve a much sharper transition region roll-off than an FIR filter of the same order.

## Example

Let the transfer function $H(z)$ of a discrete-time filter be given by:

$H(z)={\frac {B(z)}{A(z)}}={\frac {1}{1-az^{-1}}}$

governed by the parameter a , a real number with $0<|a|<1$ . $H(z)$ is stable and causal with a pole at a . The time-domain impulse response can be shown to be given by:

$h(n)=a^{n}u(n)$

where $u(n)$ is the unit step function. It can be seen that $h(n)$ is non-zero for all $n\geq 0$ , thus an impulse response which continues infinitely.

## Advantages and disadvantages

The main advantage digital IIR filters have over FIR filters is their efficiency in implementation, in order to meet a specification in terms of passband, stopband, ripple, and/or roll-off. Such a set of specifications can be accomplished with a lower order (*Q* in the above formulae) IIR filter than would be required for an FIR filter meeting the same requirements. If implemented in a signal processor, this implies a correspondingly fewer number of calculations per time step; the computational savings is often of a rather large factor.

On the other hand, FIR filters can be easier to design, for instance, to match a particular frequency response requirement. This is particularly true when the requirement is not one of the usual cases (high-pass, low-pass, notch, etc.) which have been studied and optimized for analog filters. Also FIR filters can be easily made to be linear phase (constant group delay vs frequency)—a property that is not easily met using IIR filters and then only as an approximation (for instance with the Bessel filter). Another issue regarding digital IIR filters is the potential for limit cycle behavior when idle, due to the feedback system in conjunction with quantization.

## Design Methods

### Impulse Invariance

Impulse invariance is a technique for designing discrete-time infinite-impulse-response (IIR) filters from continuous-time filters in which the impulse response of the continuous-time system is sampled to produce the impulse response of the discrete-time system. Impulse invariance is one of the commonly used methods to meet the two basic requirements of the mapping from the s-plane to the z-plane. This is obtained by solving the T(z) that has the same output value at the same sampling time as the analog filter, and it is only applicable when the inputs are in a pulse. Note that all inputs of the digital filter generated by this method are approximate values, except for pulse inputs that are very accurate. This is the simplest IIR filter design method. It is the most accurate at low frequencies, so it is usually used in low-pass filters.

For Laplace transform or z-transform, the output after the transformation is just the input multiplied by the corresponding transformation function, T(s) or T(z). Y(s) and Y(z) are the converted output of input X(s) and input X(z), respectively.

$Y(s)=T(s)X(s)$

$Y(z)=T(z)X(z)$

When applying the Laplace transform or z-transform on the unit impulse, the result is 1. Hence, the output results after the conversion are

$Y(s)=T(s)$

$Y(z)=T(z)$

Now the output of the analog filter is just the inverse Laplace transform in the time domain.

$y(t)=L^{-1}[Y(s)]=L^{-1}[T(s)]$

If we use nT instead of t, we can get the output y(nT) derived from the pulse at the sampling time. It can also be expressed as y(n)

$y(n)=y(nT)=y(t)|_{t=sT}$

This discrete time signal can be applied z-transform to get T(z)

$T(z)=Y(z)=Z[y(n)]$

$T(z)=Z[y(n)]=Z[y(nT)]$

$T(z)=Z\left\{L^{-1}[T(s)]_{t=nT}\right\}$

The last equation mathematically describes that a digital IIR filter is to perform z-transform on the analog signal that has been sampled and converted to T(s) by Laplace, which is usually simplified to

$T(z)=Z[T(s)]*T$

Pay attention to the fact that there is a multiplier T appearing in the formula. This is because even if the Laplace transform and z-transform for the unit pulse are 1, the pulse itself is not necessarily the same. For analog signals, the pulse has an infinite value but the area is 1 at t=0, but it is 1 at the discrete-time pulse t=0, so the existence of a multiplier T is required.

### Step Invariance

Step invariance is a better design method than impulse invariant. The digital filter has several segments of input with different constants when sampling, which is composed of discrete steps. The step invariant IIR filter is less accurate than the same input step signal to the ADC. However, it is a better approximation for any input than the impulse invariant. Step invariant solves the problem of the same sample values when T(z) and T(s) are both step inputs. The input to the digital filter is u(n), and the input to the analog filter is u(t). Apply z-transform and Laplace transform on these two inputs to obtain the converted output signal. Perform z-transform on step input $Z[u(n)]={\dfrac {z}{z-1}}$ Converted output after z-transform $Y(z)=T(z)U(z)=T(z){\dfrac {z}{z-1}}$ Perform Laplace transform on step input $L[u(t)]={\dfrac {1}{s}}$ Converted output after Laplace transform $Y(s)=T(s)U(s)={\dfrac {T(s)}{s}}$ The output of the analog filter is y(t), which is the inverse Laplace transform of Y(s). If sampled every T seconds, it is y(n), which is the inverse conversion of Y(z).These signals are used to solve for the digital filter and the analog filter and have the same output at the sampling time. The following equation points out the solution of T(z), which is the approximate formula for the analog filter.

$T(z)={\dfrac {z-1}{z}}Y(z)$

$T(z)={\dfrac {z-1}{z}}Z[y(n)]$

$T(z)={\dfrac {z-1}{z}}Z[Y(s)]$

$T(z)={\dfrac {z-1}{z}}Z[{\dfrac {T(s)}{s}}]$

### Bilinear Transform

The bilinear transform is a special case of a conformal mapping, often used to convert a transfer function $H_{a}(s)$ of a linear, time-invariant (LTI) filter in the continuous-time domain (often called an analog filter) to a transfer function $H_{d}(z)$ of a linear, shift-invariant filter in the discrete-time domain. The bilinear transform is a first-order approximation of the natural logarithm function that is an exact mapping of the *z*-plane to the *s*-plane. When the Laplace transform is performed on a discrete-time signal (with each element of the discrete-time sequence attached to a correspondingly delayed unit impulse), the result is precisely the Z transform of the discrete-time sequence with the substitution of

${\begin{aligned}z&=e^{sT}\\&={\frac {e^{sT/2}}{e^{-sT/2}}}\\&\approx {\frac {1+sT/2}{1-sT/2}}\end{aligned}}$

where T is the numerical integration step size of the trapezoidal rule used in the bilinear transform derivation; or, in other words, the sampling period. The above bilinear approximation can be solved for s or a similar approximation for $s=(1/T)\ln(z)$ can be performed.

The inverse of this mapping (and its first-order bilinear approximation) is

${\begin{aligned}s&={\frac {1}{T}}\ln(z)\\&={\frac {2}{T}}\left[{\frac {z-1}{z+1}}+{\frac {1}{3}}\left({\frac {z-1}{z+1}}\right)^{3}+{\frac {1}{5}}\left({\frac {z-1}{z+1}}\right)^{5}+{\frac {1}{7}}\left({\frac {z-1}{z+1}}\right)^{7}+\cdots \right]\\&\approx {\frac {2}{T}}{\frac {z-1}{z+1}}\\&={\frac {2}{T}}{\frac {1-z^{-1}}{1+z^{-1}}}\end{aligned}}$

This relationship is used in the Laplace transfer function of any analog filter or the digital infinite impulse response (IIR) filter T(z) of the analog filter. The bilinear transform essentially uses this first order approximation and substitutes into the continuous-time transfer function, $H_{a}(s)$

$s\leftarrow {\frac {2}{T}}{\frac {z-1}{z+1}}.$

That is

$H_{d}(z)=H_{a}(s){\bigg |}_{s={\frac {2}{T}}{\frac {z-1}{z+1}}}=H_{a}\left({\frac {2}{T}}{\frac {z-1}{z+1}}\right).\$

which is used to calculate the IIR digital filter, starting from the Laplace transfer function of the analog filter.
