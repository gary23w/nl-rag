---
title: "Grating lobes"
source: https://en.wikipedia.org/wiki/Grating_lobe
domain: antenna-arrays
license: CC-BY-SA-4.0
tags: antenna array, phased array, adaptive beamformer, grating lobe
fetched: 2026-07-02
---

# Grating lobes

(Redirected from

Grating lobe

)

For discrete aperture antennas (such as phased arrays) in which the element spacing is greater than a half wavelength, a spatial aliasing effect allows plane waves incident to the array from visible angles other than the desired direction to be coherently added, causing **grating lobes**. Grating lobes are undesirable and identical to the main lobe. The perceived difference seen in the grating lobes is because of the radiation pattern of non-isotropic antenna elements, which affects main and grating lobes differently. For isotropic antenna elements, the main and grating lobes are identical.

## Definition

In antenna or transducer arrays, a grating lobe is defined as "a lobe other than the main lobe, produced by an array antenna when the inter-element spacing is sufficiently large to permit the in-phase addition of radiated fields in more than one direction."

## Derivation

To illustrate the concept of grating lobes, we will use a simple uniform linear array. The beam pattern (or array factor) of any array can be defined as the dot product of the steering vector and the array manifold vector. For a uniform linear array, the manifold vector is ${\vec {v}}(\psi )=e^{j\left(n-{\frac {N-1}{2}}\right)\psi }$ , where $\psi$ is the phase difference between adjacent elements created by an impinging plane wave from an arbitrary direction, n is the element number, and N is the total number of elements. The ${\frac {N-1}{2}}$ term merely centers the point of reference for phase to the physical center of the array. From simple geometry, $\psi$ can be shown to be $\psi ={\frac {2\pi }{\lambda }}d\times \cos \theta$ , where $\theta$ is defined as the plane wave incident angle where $\theta =90^{\circ }$ is a plane wave incident orthogonal to the array (from boresight).

For a uniformly weighted (un-tapered) uniform linear array, the steering vector is of similar form to the manifold vector, but is "steered" to a target phase, $\psi _{T}$ , that may differ from the actual phase, $\psi$ of the impinging signal. The resulting normalized array factor is a function of the phase difference, $\psi _{\Delta }=\psi -\psi _{T}$ .

$AF={\frac {1}{N}}{\vec {v}}^{H}(\psi _{T}){\vec {v}}(\psi )={\frac {1}{N}}\sum _{n=0}^{N-1}e^{-j\left(n-{\frac {N-1}{2}}\right)\psi _{T}}e^{j\left(n-{\frac {N-1}{2}}\right)\psi }={\frac {1}{N}}e^{-j{\frac {N-1}{2}}\psi _{\Delta }}\sum _{n=0}^{N-1}e^{jn\psi _{\Delta }}={\frac {\sin \left(N{\frac {\psi _{\Delta }}{2}}\right)}{N\sin \left({\frac {\psi _{\Delta }}{2}}\right)}},-\infty <\psi _{\Delta }<\infty$

The array factor is therefore periodic and maximized whenever the numerator and denominator both equal zero, by L'Hôpital's rule. Thus, a maximum of unity is obtained for all integers n , where $\psi _{\Delta }=2\pi n$ . Returning to our definition of $\theta$ , we wish to be able to steer the array electronically over the entire visible region, which extends from $\theta =0^{\circ }$ to $\theta =180^{\circ }$ , without incurring a grating lobe. This requires that the grating lobes be separated by at least $180^{\circ }$ . From the definition of $\psi$ , we see that maxima will occur whenever $2\pi n={\frac {2\pi }{\lambda }}d\times \left(\cos \theta -\cos \theta _{T}\right)$ . The first grating lobe will occur at $|n|=1$ . For a beam steered to $\theta _{T}=180^{\circ }$ , we require the grating lobe to be no closer than $\theta =0^{\circ }$ . Thus $d={\frac {2\pi \lambda }{2\pi \left(1+1\right)}}={\frac {\lambda }{2}}$ .

## Relationship to sampling theorem

Alternatively, one can think of a uniform linear array (ULA) as spatial sampling of a signal in the same sense as time sampling of a signal. Grating lobes are identical to aliasing that occurs in time series analysis for an under-sampled signal. Per Shannon's sampling theorem, the sampling rate must be at least twice the highest frequency of the desired signal in order to preclude spectral aliasing. Because the beam pattern (or array factor) of a linear array is the Fourier transform of the element pattern, the sampling theorem directly applies, but in the spatial instead of spectral domain. The discrete-time Fourier transform (DTFT) of a sampled signal is always periodic, producing "copies" of the spectrum at intervals of the sampling frequency. In the spatial domain, these copies are the grating lobes. The analog of radian frequency in the time domain is wavenumber, $k={\frac {2\pi }{\lambda }}$ radians per meter, in the spatial domain. Therefore the spatial sampling rate, in samples per meter, must be $\geq 2{\frac {samples}{cycle}}\times {\frac {k{\frac {radians}{meter}}}{2\pi {\frac {radians}{cycle}}}}$ . The sampling interval, which is the inverse of the sampling rate, in meters per sample, must be $\leq {\frac {\lambda }{2}}$ .
