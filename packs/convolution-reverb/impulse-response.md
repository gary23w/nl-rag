---
title: "Impulse response"
source: https://en.wikipedia.org/wiki/Impulse_response
domain: convolution-reverb
license: CC-BY-SA-4.0
tags: convolution reverb, impulse response reverb, fir convolution audio, overlap add convolution
fetched: 2026-07-02
---

# Impulse response

In signal processing and control theory, the **impulse response**, or **impulse response function** (**IRF**), of a dynamic system is its output when presented with a brief input signal, called an impulse (δ(*t*)). More generally, an impulse response is the reaction of any dynamic system in response to some external change. In both cases, the impulse response describes the reaction of the system as a function of time (or possibly as a function of some other independent variable that parameterizes the dynamic behavior of the system).

In all these cases, the dynamic system and its impulse response may be actual physical objects, or may be mathematical systems of equations describing such objects.

Since the impulse function contains all frequencies (see the Fourier transform of the Dirac delta function, showing infinite frequency bandwidth that the Dirac delta function has), the impulse response defines the response of a linear time-invariant system for all frequencies.

## Mathematical considerations

Mathematically, how the impulse is described depends on whether the system is modeled in discrete or continuous time. The impulse can be modeled as a Dirac delta function for continuous-time systems, or as the discrete unit sample function for discrete-time systems. The Dirac delta represents the limiting case of a pulse made very short in time while maintaining its area or integral (thus giving an infinitely high peak). While this is impossible in any real system, it is a useful idealization. In Fourier analysis theory, such an impulse comprises equal portions of all possible excitation frequencies, which makes it a convenient test probe.

Any system in a large class known as *linear, time-invariant* (LTI) is completely characterized by its impulse response. That is, for any input, the output can be calculated in terms of the input and the impulse response. (See LTI system theory.) The impulse response of a linear transformation is the image of Dirac's delta function under the transformation, analogous to the fundamental solution of a partial differential operator.

It is usually easier to analyze systems using transfer functions as opposed to impulse responses. The transfer function is the Laplace transform of the impulse response. The Laplace transform of a system's output may be determined by the multiplication of the transfer function with the input's Laplace transform in the complex plane, also known as the frequency domain. An inverse Laplace transform of this result will yield the output in the time domain.

To determine an output directly in the time domain requires the convolution of the input with the impulse response. When the transfer function and the Laplace transform of the input are known, this convolution may be more complicated than the alternative of multiplying two functions in the frequency domain.

The impulse response, considered as a Green's function, can be thought of as an "influence function": how a point of input influences output.

## Practical applications

In practice, it is not possible to perturb a system with a perfect impulse. One can use a brief pulse as a first approximation. Limitations of this approach include the duration of the pulse and its magnitude. The response can be close, compared to the ideal case, provided the pulse is short enough. Additionally, in many systems, a pulse of large intensity may drive the system into the nonlinear regime. Other methods exist to construct an impulse response. The impulse response can be calculated from the input and output of a system driven with a pseudo-random sequence, such as maximum length sequences. Another approach is to take a sine sweep measurement and process the result to get the impulse response.

### Loudspeakers

Impulse response loudspeaker testing was first developed in the 1970s. Loudspeakers suffer from phase inaccuracy (delayed frequencies) which can be caused by passive crossovers, resonance, cone momentum, the internal volume, and vibrating enclosure panels. The impulse response can be used to indicate when such inaccuracies can be improved by different materials, enclosures or crossovers.

Loudspeakers have a physical limit to their power output, thus the input amplitude must be limited to maintain linearity. This limitation led to the use of inputs like maximum length sequences in obtaining the impulse response.

### Electronic processing

Impulse response analysis is a major facet of radar, ultrasound imaging, and many areas of digital signal processing. An interesting example is found in broadband internet connections. Digital subscriber line service providers use adaptive equalization to compensate for signal distortion and interference from using copper phone lines for transmission.

### Control systems

In control theory the impulse response is the response of a system to a Dirac delta input. This proves useful in the analysis of dynamic systems; the Laplace transform of the delta function is 1, so the impulse response is equivalent to the inverse Laplace transform of the system's transfer function.

### Acoustic and audio applications

In acoustic and audio settings, impulse responses can be used to capture the acoustic characteristics of many things. The reverb at a location, the body of an instrument, certain analog audio equipment, and amplifiers are all emulated by impulse responses. The impulse is convolved with a dry signal in software, often to create the effect of a physical recording. Various packages containing impulse responses from specific locations are available online.

### Economics

In economics, and especially in contemporary macroeconomic modeling, impulse response functions are used to describe how the economy reacts over time to exogenous impulses, which economists usually call shocks, and are often modeled in the context of a vector autoregression. Impulses that are often treated as exogenous from a macroeconomic point of view include changes in government spending, tax rates, and other fiscal policy parameters; changes in the monetary base or other monetary policy parameters; changes in productivity or other technological parameters; and changes in preferences, such as the degree of impatience. Impulse response functions describe the reaction of endogenous macroeconomic variables such as output, consumption, investment, and employment at the time of the shock and over subsequent points in time. Recently, asymmetric impulse response functions have been suggested in the literature that separate the impact of a positive shock from a negative one.
