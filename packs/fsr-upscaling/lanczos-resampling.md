---
title: "Lanczos resampling"
source: https://en.wikipedia.org/wiki/Lanczos_resampling
domain: fsr-upscaling
license: CC-BY-SA-4.0
tags: fidelityfx super resolution, fsr upscaling, spatial image upscaling, lanczos resampling upscale
fetched: 2026-07-02
---

# Lanczos resampling

Partial plot of a discrete signal (black dots) and of its Lanczos interpolation (solid blue curve), with size parameter

a

equal to 1 (top), 2 (middle) and 3 (bottom). Also shown are two copies of the Lanczos kernel, shifted and scaled, corresponding to samples 4 and 11 (dashed curves).

**Lanczos filtering** and **Lanczos resampling** are two applications of a certain mathematical formula. It can be used as a low-pass filter or used to smoothly interpolate the value of a digital signal between its samples. In the latter case, it maps each sample of the given signal to a translated and scaled copy of the **Lanczos kernel**, which is a sinc function windowed by the central lobe of a second, longer, sinc function. The sum of these translated and scaled kernels is then evaluated at the desired points.

Lanczos resampling is typically used to increase the sampling rate of a digital signal, or to shift it by a fraction of the sampling interval. It is often used also for multivariate interpolation, for example to resize or rotate a digital image. It has been considered the "best compromise" among several simple filters for this purpose.

The filter was invented by Claude Duchon, who named it after Cornelius Lanczos due to Duchon's use of the sigma approximation in constructing the filter, a technique created by Lanczos.

## Definition

### Lanczos kernel

The effect of each input sample on the interpolated values is defined by the filter's reconstruction kernel *L*(*x*), called the Lanczos kernel. It is the normalized sinc function sinc(*x*), windowed (multiplied) by the **Lanczos window**, or **sinc window**, which is the central lobe of a horizontally stretched sinc function sinc(*x*/*a*) for −*a* ≤ *x* ≤ *a*.

$L(x)={\begin{cases}\operatorname {sinc} (x)\operatorname {sinc} (x/a)&{\text{if}}\ -a<x<a,\\0&{\text{otherwise}}.\end{cases}}$

Equivalently,

$L(x)={\begin{cases}1&{\text{if}}\ x=0,\\{\dfrac {a\sin(\pi x)\sin(\pi x/a)}{\pi ^{2}x^{2}}}&{\text{if}}\ -a\leq x<a\ {\text{and}}\ x\neq 0,\\0&{\text{otherwise}}.\end{cases}}$

The parameter *a* is a positive integer, typically 2 or 3, which determines the size of the kernel. The Lanczos kernel has 2*a* − 1 lobes: a positive one at the center, and *a* − 1 alternating negative and positive lobes on each side.

### Interpolation formula

Given a one-dimensional signal with samples *s**i*, for integer values of *i*, the value *S*(*x*) interpolated at an arbitrary real argument *x* is obtained by the discrete convolution of those samples with the Lanczos kernel:

$S(x)=\sum _{i=\lfloor x\rfloor -a+1}^{\lfloor x\rfloor +a}s_{i}L(x-i),$

where *a* is the filter size parameter, and $\lfloor x\rfloor$ is the floor function. The bounds of this sum are such that the kernel is zero outside of them.

## Properties

As long as the parameter *a* is a positive integer, the Lanczos kernel is continuous everywhere, and its derivative is defined and continuous everywhere (even at *x* = ±*a*, where both sinc functions go to zero). Therefore, the reconstructed signal *S*(*x*) too will be continuous, with continuous derivative.

The Lanczos kernel is zero at every integer argument *x*, except at *x* = 0, where it has value 1. Therefore, the reconstructed signal exactly interpolates the given samples: we will have *S*(*x*) = *s**i* for every integer argument *x* = *i*.

Lanczos resampling is one form of a general method developed by Lanczos to counteract the Gibbs phenomenon by multiplying coefficients of a truncated Fourier series by $\mathrm {sinc} (\pi k/m)$ , where k is the coefficient index and m is how many coefficients we're keeping. The same reasoning applies in the case of truncated functions if we wish to remove Gibbs oscillations in their spectrum.

## Multidimensional interpolation

Lanczos filter's kernel in two dimensions is

$L(x,y)=L(x)L(y).$

## Evaluation

### Advantages

The theoretically optimal reconstruction filter for band-limited signals is the sinc filter, which has infinite support. The Lanczos filter is one of many practical (finitely supported) approximations of the sinc filter. Each interpolated value is the weighted sum of 2*a* consecutive input samples. Thus, by varying the 2*a* parameter one may trade computation speed for improved frequency response. The parameter also allows one to choose between a smoother interpolation or a preservation of sharp transients in the data. For image processing, the trade-off is between the reduction of aliasing artefacts and the preservation of sharp edges. Also as with any such processing, there are no results for the borders of the image. Increasing the length of the kernel increases the cropping of the edges of the image.

The Lanczos filter has been compared with other interpolation methods for discrete signals, particularly other windowed versions of the sinc filter. Turkowski and Gabriel claimed that the Lanczos filter (with *a* = 2) is the "best compromise in terms of reduction of aliasing, sharpness, and minimal ringing", compared with truncated sinc and the Bartlett, cosine-, and Hann-windowed sinc, for decimation and interpolation of 2-dimensional image data. According to Jim Blinn, the Lanczos kernel (with *a* = 3) "keeps low frequencies and rejects high frequencies better than any (achievable) filter we've seen so far."

Lanczos interpolation is a popular filter for "upscaling" videos in various media utilities, such as AviSynth and FFmpeg.

### Limitations

Since the kernel assumes negative values for *a* > 1, the interpolated signal can be negative even if all samples are positive. More generally, the range of values of the interpolated signal may be wider than the range spanned by the discrete sample values. In particular, there may be ringing artifacts just before and after abrupt changes in the sample values, which may lead to clipping artifacts. However, these effects are reduced compared to the (non-windowed) sinc filter. For *a* = 2 (a three-lobed kernel) the ringing is < 1%.

When using the Lanczos filter for image resampling, the ringing effect will create light and dark halos along any strong edges. While these bands may be visually annoying, they help increase the perceived sharpness, and therefore provide a form of edge enhancement. This may improve the subjective quality of the image, given the special role of edge sharpness in vision.

In some applications, the low-end clipping artifacts can be ameliorated by transforming the data to a logarithmic domain prior to filtering. In this case the interpolated values will be a weighted geometric mean, rather than an arithmetic mean, of the input samples.

The Lanczos kernel does not have the partition of unity property. That is, the sum ${\textstyle U(x)=\sum _{i\in \mathbb {Z} }L(x-i)}$ of all integer-translated copies of the kernel is not always 1. Therefore, the Lanczos interpolation of a discrete signal with constant samples does not yield a constant function. This defect is most evident when *a* = 1. Also, for *a* = 1 the interpolated signal has zero derivative at every integer argument. This is rather academic, since using a single-lobe kernel (*a* = 1) loses all the benefits of the Lanczos approach and provides a poor filter. There are many better single-lobe, bell-shaped windowing functions.

The partition of unity can be introduced by a normalization,

$L'(x-i)={\frac {L(x-i)}{\sum _{j=1-a}^{a}L(x-j)}}$

for $0\leq x<1$ .
