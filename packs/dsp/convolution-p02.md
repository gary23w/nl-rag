---
title: "Convolution (part 2/2)"
source: https://en.wikipedia.org/wiki/Convolution
domain: dsp
license: CC-BY-SA-4.0
tags: dsp, digital signal processing, fft, fourier transform, digital filter, sampling rate
fetched: 2026-07-02
part: 2/2
---

## Bialgebras

Let (*X*, Δ, ∇, *ε*, *η*) be a bialgebra with comultiplication Δ, multiplication ∇, unit η, and counit *ε*. The convolution is a product defined on the endomorphism algebra End(*X*) as follows. Let *φ*, *ψ* ∈ End(*X*), that is, *φ*, *ψ*: *X* → *X* are functions that respect all algebraic structure of *X*, then the convolution *φ*∗*ψ* is defined as the composition

X

→

Δ

X

⊗

X

→

ϕ

⊗

ψ

X

⊗

X

→

∇

X

.

{\displaystyle X\mathrel {\xrightarrow {\Delta } } X\otimes X\mathrel {\xrightarrow {\phi \otimes \psi } } X\otimes X\mathrel {\xrightarrow {\nabla } } X.}

The convolution appears notably in the definition of Hopf algebras (Kassel 1995, §III.3). A bialgebra is a Hopf algebra if and only if it has an antipode: an endomorphism *S* such that

S

∗

id

X

=

id

X

∗

S

=

η

∘

ε

.

{\displaystyle S*\operatorname {id} _{X}=\operatorname {id} _{X}*S=\eta \circ \varepsilon .}


## Applications

Convolution and related operations are found in many applications in science, engineering and mathematics.

- Convolutional neural networks apply multiple cascaded *convolution* kernels with applications in machine vision and artificial intelligence. Though these are actually **cross-correlations** rather than convolutions.
- In non-neural-network-based image processing
  - In digital image processing convolutional filtering plays an important role in many important algorithms in edge detection and related processes (see Kernel (image processing))
  - In optics, an out-of-focus photograph is a convolution of the sharp image with a lens function. The photographic term for this is bokeh.
  - In image processing applications such as adding blurring.
- In digital data processing
  - In analytical chemistry, Savitzky–Golay smoothing filters are used for the analysis of spectroscopic data. They can improve signal-to-noise ratio with minimal distortion of the spectra
  - In statistics, a weighted moving average is a convolution.
- In acoustics, reverberation is the convolution of the original sound with echoes from objects surrounding the sound source.
  - In digital signal processing, convolution is used to map the impulse response of a real room on a digital audio signal.
  - In electronic music convolution is the imposition of a spectral or rhythmic structure on a sound. Often this envelope or structure is taken from another sound. The convolution of two signals is the filtering of one through the other.
- In electrical engineering, the convolution of one function (the input signal) with a second function (the impulse response) gives the output of a linear time-invariant system (LTI). At any given moment, the output is an accumulated effect of all the prior values of the input function, with the most recent values typically having the most influence (expressed as a multiplicative factor). The impulse response function provides that factor as a function of the elapsed time since each input value occurred.
- In physics, wherever there is a linear system with a "superposition principle", a convolution operation makes an appearance. For instance, in spectroscopy line broadening due to the Doppler effect on its own gives a Gaussian spectral line shape and collision broadening alone gives a Lorentzian line shape. When both effects are operative, the line shape is a convolution of Gaussian and Lorentzian, a Voigt function.
  - In time-resolved fluorescence spectroscopy, the excitation signal can be treated as a chain of delta pulses, and the measured fluorescence is a sum of exponential decays from each delta pulse.
  - In computational fluid dynamics, the large eddy simulation (LES) turbulence model uses the convolution operation to lower the range of length scales necessary in computation thereby reducing computational cost.
- In probability theory, the probability distribution of the sum of two independent random variables is the convolution of their individual distributions.
  - In kernel density estimation, a distribution is estimated from sample points by convolution with a kernel, such as an isotropic Gaussian.
- In radiotherapy treatment planning systems, most part of all modern codes of calculation applies a convolution-superposition algorithm.
- In structural reliability, the reliability index can be defined based on the convolution theorem.
  - The definition of reliability index for limit state functions with nonnormal distributions can be established corresponding to the joint distribution function. In fact, the joint distribution function can be obtained using the convolution theory.
- In Smoothed-particle hydrodynamics, simulations of fluid dynamics are calculated using particles, each with surrounding kernels. For any given particle i {\displaystyle i} ({\displaystyle i}), some physical quantity A i {\displaystyle A_{i}} ({\displaystyle A_{i}}) is calculated as a convolution of A j {\displaystyle A_{j}} ({\displaystyle A_{j}}) with a weighting function, where j {\displaystyle j} ({\displaystyle j}) denotes the neighbors of particle i {\displaystyle i} ({\displaystyle i}): those that are located within its kernel. The convolution is approximated as a summation over each neighbor.
- In Fractional calculus convolution is instrumental in various definitions of fractional integral and fractional derivative.
