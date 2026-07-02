---
title: "Wiener filter"
source: https://en.wikipedia.org/wiki/Wiener_filter
domain: signal-estimation
license: CC-BY-SA-4.0
tags: estimation theory, kalman filter, maximum likelihood estimation, particle filter
fetched: 2026-07-02
---

# Wiener filter

In signal processing, the **Wiener filter** (named after Norbert Wiener) is a filter used to produce an estimate of a desired or target random process by linear time-invariant (LTI) filtering of an observed noisy process, assuming known stationary signal and noise spectra, and additive noise. The Wiener filter minimizes the mean square error between the estimated random process and the desired process.

## Description

The goal of the Wiener filter is to compute a statistical estimate of an unknown signal using a related signal as an input and filtering it to produce the estimate. For example, the known signal might consist of an unknown signal of interest that has been corrupted by additive noise. The Wiener filter can be used to filter out the noise from the corrupted signal to provide an estimate of the underlying signal of interest. The Wiener filter is based on a statistical approach, and a more statistical account of the theory is given in the minimum mean square error (MMSE) estimator article.

Typical deterministic filters are designed for a desired frequency response. However, the design of the Wiener filter takes a different approach. One is assumed to have knowledge of the spectral properties of the original signal and the noise, and one seeks the linear time-invariant filter whose output would come as close to the original signal as possible. Wiener filters are characterized by the following:

1. Assumption: signal and (additive) noise are stationary stochastic processes with known spectral characteristics or known autocorrelation and cross-correlation
2. Requirement: the filter must be physically realizable/causal (this requirement can be dropped, resulting in a non-causal solution)
3. Performance criterion: minimum mean-square error (MMSE)

This filter is frequently used in the process of deconvolution; for this application, see Wiener deconvolution.

## Wiener filter solutions

Let $s(t+\alpha )$ be an unknown signal which must be estimated from a measurement signal $x(t)$ , where $\alpha$ is a tunable parameter. $\alpha >0$ is known as prediction, $\alpha =0$ is known as filtering, and $\alpha <0$ is known as smoothing (see Wiener filtering chapter of for more details).

The Wiener filter problem has solutions for three possible cases: one where a noncausal filter is acceptable (requiring an infinite amount of both past and future data), the case where a causal filter is desired (using an infinite amount of past data), and the finite impulse response (FIR) case where only input data is used (i.e. the result or output is not fed back into the filter as in the IIR case). The first case is simple to solve but is not suited for real-time applications. Wiener's main accomplishment was solving the case where the causality requirement is in effect; Norman Levinson gave the FIR solution in an appendix of Wiener's book.

### Noncausal solution

For the estimation of $s(t+\alpha )$ from $x(t)$ , the (generally non-causal) optimal linear time-invariant (LTI) filter has frequency response $G(\omega )={\frac {S_{xs}(\omega )}{S_{x}(\omega )}}\,e^{j\omega \alpha },$

where $S_{xs}(\omega )$ is the cross power spectral density between $x(t)$ and $s(t)$ , and $S_{x}(\omega )$ is the power spectral density of $x(t)$ .

If $g(t)$ is the optimal impulse response, the minimum mean-square error can be written as

$\operatorname {E} \{e^{2}(t)\}=R_{s}(0)-\int _{-\infty }^{\infty }g(\tau )\,R_{xs}(\tau +\alpha )\,d\tau ,$

where $R_{s}(\tau )$ is the autocorrelation function of $s(t)$ and $R_{xs}(\tau )$ is the cross-correlation between $x(t)$ and $s(t)$ , e.g.

$R_{s}(\tau )=\operatorname {E} \{s(t)\,s^{*}(t-\tau )\},$

$R_{xs}(\tau )=\operatorname {E} \{x(t)\,s^{*}(t-\tau )\},$

with $^{*}$ denoting complex conjugation.

The impulse response $g(t)$ is obtained as the inverse Fourier transform of $G(\omega )$ .

### Causal solution

$G(s)={\frac {H(s)}{S_{x}^{+}(s)}},$

where

- $H(s)$ consists of the causal part of ${\frac {S_{x,s}(s)}{S_{x}^{-}(s)}}e^{\alpha s}$ (that is, that part of this fraction having a positive time solution under the inverse Laplace transform)
- $S_{x}^{+}(s)$ is the causal component of $S_{x}(s)$ (i.e., the inverse Laplace transform of $S_{x}^{+}(s)$ is non-zero only for $t\geq 0$ )
- $S_{x}^{-}(s)$ is the anti-causal component of $S_{x}(s)$ (i.e., the inverse Laplace transform of $S_{x}^{-}(s)$ is non-zero only for $t<0$ )

This general formula is complicated and deserves a more detailed explanation. To write down the solution $G(s)$ in a specific case, one should follow these steps:

1. Start with the spectrum $S_{x}(s)$ in rational form and factor it into causal and anti-causal components: $S_{x}(s)=S_{x}^{+}(s)S_{x}^{-}(s)$ where $S_{x}^{+}$ contains all the zeros and poles in the left half plane (LHP) and $S_{x}^{-}$ contains the zeroes and poles in the right half plane (RHP). This is called the Wiener–Hopf factorization.
2. Divide $S_{x,s}(s)e^{\alpha s}$ by $S_{x}^{-}(s)$ and write out the result as a partial fraction expansion.
3. Select only those terms in this expansion having poles in the LHP. Call these terms $H(s)$ .
4. Divide $H(s)$ by $S_{x}^{+}(s)$ . The result is the desired filter transfer function $G(s)$ .

## Finite impulse response Wiener filter for discrete series

The causal finite impulse response (FIR) Wiener filter, instead of using some given data matrix X and output vector Y, finds optimal tap weights by using the statistics of the input and output signals. It populates the input matrix X with estimates of the auto-correlation of the input signal (T) and populates the output vector Y with estimates of the cross-correlation between the output and input signals (V).

In order to derive the coefficients of the Wiener filter, consider the signal *w*[*n*] being fed to a Wiener filter of order (number of past taps) *N* and with coefficients $\{a_{0},\cdots ,a_{N}\}$ . The output of the filter is denoted *x*[*n*] which is given by the expression

$x[n]=\sum _{i=0}^{N}a_{i}w[n-i].$

The residual error is denoted *e*[*n*] and is defined as *e*[*n*] = *x*[*n*] − *s*[*n*] (see the corresponding block diagram). The Wiener filter is designed so as to minimize the mean square error (MMSE criteria) which can be stated concisely as follows:

$a_{i}=\arg \min E\left[e^{2}[n]\right],$

where $E[\cdot ]$ denotes the expectation operator. In the general case, the coefficients $a_{i}$ may be complex and may be derived for the case where *w*[*n*] and *s*[*n*] are complex as well. With a complex signal, the matrix to be solved is a Hermitian Toeplitz matrix, rather than symmetric Toeplitz matrix. For simplicity, the following considers only the case where all these quantities are real. The mean square error (MSE) may be rewritten as:

${\begin{aligned}E\left[e^{2}[n]\right]&=E\left[(x[n]-s[n])^{2}\right]\\&=E\left[x^{2}[n]\right]+E\left[s^{2}[n]\right]-2E[x[n]s[n]]\\&=E\left[\left(\sum _{i=0}^{N}a_{i}w[n-i]\right)^{2}\right]+E\left[s^{2}[n]\right]-2E\left[\sum _{i=0}^{N}a_{i}w[n-i]s[n]\right]\end{aligned}}$

To find the vector $[a_{0},\,\ldots ,\,a_{N}]$ which minimizes the expression above, calculate its derivative with respect to each $a_{i}$

${\begin{aligned}{\frac {\partial }{\partial a_{i}}}E\left[e^{2}[n]\right]&={\frac {\partial }{\partial a_{i}}}\left\{E\left[\left(\sum _{j=0}^{N}a_{j}w[n-j]\right)^{2}\right]+E\left[s^{2}[n]\right]-2E\left[\sum _{j=0}^{N}a_{j}w[n-j]s[n]\right]\right\}\\&=2E\left[\left(\sum _{j=0}^{N}a_{j}w[n-j]\right)w[n-i]\right]-2E[w[n-i]s[n]]\\&=2\left(\sum _{j=0}^{N}E[w[n-j]w[n-i]]a_{j}\right)-2E[w[n-i]s[n]]\end{aligned}}$

Assuming that *w*[*n*] and *s*[*n*] are each stationary and jointly stationary, the sequences $R_{w}[m]$ and $R_{ws}[m]$ known respectively as the autocorrelation of *w*[*n*] and the cross-correlation between *w*[*n*] and *s*[*n*] can be defined as follows:

${\begin{aligned}R_{w}[m]&=E\{w[n]w[n+m]\}\\R_{ws}[m]&=E\{w[n]s[n+m]\}\end{aligned}}$

The derivative of the MSE may therefore be rewritten as:

${\frac {\partial }{\partial a_{i}}}E\left[e^{2}[n]\right]=2\left(\sum _{j=0}^{N}R_{w}[j-i]a_{j}\right)-2R_{ws}[i]\qquad i=0,\cdots ,N.$

Note that for real $w[n]$ , the autocorrelation is symmetric: $R_{w}[j-i]=R_{w}[i-j]$ Letting the derivative be equal to zero results in:

$\sum _{j=0}^{N}R_{w}[j-i]a_{j}=R_{ws}[i]\qquad i=0,\cdots ,N.$

which can be rewritten (using the above symmetric property) in matrix form

$\underbrace {\begin{bmatrix}R_{w}[0]&R_{w}[1]&\cdots &R_{w}[N]\\R_{w}[1]&R_{w}[0]&\cdots &R_{w}[N-1]\\\vdots &\vdots &\ddots &\vdots \\R_{w}[N]&R_{w}[N-1]&\cdots &R_{w}[0]\end{bmatrix}} _{\mathbf {T} }\underbrace {\begin{bmatrix}a_{0}\\a_{1}\\\vdots \\a_{N}\end{bmatrix}} _{\mathbf {a} }=\underbrace {\begin{bmatrix}R_{ws}[0]\\R_{ws}[1]\\\vdots \\R_{ws}[N]\end{bmatrix}} _{\mathbf {v} }$

These equations are known as the Wiener–Hopf equations. The matrix **T** appearing in the equation is a symmetric Toeplitz matrix. Under suitable conditions on R , these matrices are known to be positive definite and therefore non-singular yielding a unique solution to the determination of the Wiener filter coefficient vector, $\mathbf {a} =\mathbf {T} ^{-1}\mathbf {v}$ . Furthermore, there exists an efficient algorithm to solve such Wiener–Hopf equations known as the Levinson-Durbin algorithm so an explicit inversion of **T** is not required.

In some articles, the cross correlation function is defined in the opposite way: $R_{sw}[m]=E\{w[n]s[n+m]\}$ Then, the $\mathbf {v}$ matrix will contain $R_{sw}[0]\ldots R_{sw}[N]$ ; this is just a difference in notation.

Whichever notation is used, note that for real $w[n],s[n]$ : $R_{sw}[k]=R_{ws}[-k]$

### Relationship to the least squares filter

The realization of the causal Wiener filter looks a lot like the solution to the least squares estimate, except in the signal processing domain. The least squares solution, for input matrix $\mathbf {X}$ and output vector $\mathbf {y}$ is

${\boldsymbol {\hat {\beta }}}=(\mathbf {X} ^{\mathbf {T} }\mathbf {X} )^{-1}\mathbf {X} ^{\mathbf {T} }{\boldsymbol {y}}.$

The FIR Wiener filter is related to the least mean squares filter, but minimizing the error criterion of the latter does not rely on cross-correlations or auto-correlations. Its solution converges to the Wiener filter solution.

### Complex signals

For complex signals, the derivation of the complex Wiener filter is performed by minimizing $E\left[|e[n]|^{2}\right]$ = $E\left[e[n]e^{*}[n]\right]$ . This involves computing partial derivatives with respect to both the real and imaginary parts of $a_{i}$ , and requiring them both to be zero.

The resulting Wiener-Hopf equations are:

$\sum _{j=0}^{N}R_{w}[j-i]a_{j}^{*}=R_{ws}[i]\qquad i=0,\cdots ,N.$

which can be rewritten in matrix form:

$\underbrace {\begin{bmatrix}R_{w}[0]&R_{w}^{*}[1]&\cdots &R_{w}^{*}[N-1]&R_{w}^{*}[N]\\R_{w}[1]&R_{w}[0]&\cdots &R_{w}^{*}[N-2]&R_{w}^{*}[N-1]\\\vdots &\vdots &\ddots &\vdots &\vdots \\R_{w}[N-1]&R_{w}[N-2]&\cdots &R_{w}[0]&R_{w}^{*}[1]\\R_{w}[N]&R_{w}[N-1]&\cdots &R_{w}[1]&R_{w}[0]\end{bmatrix}} _{\mathbf {T} }\underbrace {\begin{bmatrix}a_{0}^{*}\\a_{1}^{*}\\\vdots \\a_{N-1}^{*}\\a_{N}^{*}\end{bmatrix}} _{\mathbf {a^{*}} }=\underbrace {\begin{bmatrix}R_{ws}[0]\\R_{ws}[1]\\\vdots \\R_{ws}[N-1]\\R_{ws}[N]\end{bmatrix}} _{\mathbf {v} }$

Note here that: ${\begin{aligned}R_{w}[-k]&=R_{w}^{*}[k]\\R_{sw}[k]&=R_{ws}^{*}[-k]\end{aligned}}$

The Wiener coefficient vector is then computed as: $\mathbf {a} ={(\mathbf {T} ^{-1}\mathbf {v} )}^{*}$

## Applications

The Wiener filter has a variety of applications in signal processing, image processing, control systems, and digital communications. These applications generally fall into one of four main categories:

- System identification
- Deconvolution
- Noise reduction
- Signal detection

Noisy image of an astronaut

The image after a Wiener filter is applied (full-view recommended)

For example, the Wiener filter can be used in image processing to remove noise from a picture. For example, using the Mathematica function: `WienerFilter[image,2]` on the first image on the right, produces the filtered image below it.

It is commonly used to denoise audio signals, especially speech, as a preprocessor before speech recognition.

It's used by SVT-AV1 for film grain synthesis.

## History

The filter was proposed by Norbert Wiener during the 1940s and published in 1949. The discrete-time equivalent of Wiener's work was derived independently by Andrey Kolmogorov and published in 1941. Hence the theory is often called the *Wiener–Kolmogorov* filtering theory (*cf.* Kriging). The Wiener filter was the first statistically designed filter to be proposed and subsequently gave rise to many others including the Kalman filter.
