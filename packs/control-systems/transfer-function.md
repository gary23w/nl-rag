---
title: "Transfer function"
source: https://en.wikipedia.org/wiki/Transfer_function
domain: control-systems
license: CC-BY-SA-4.0
tags: control theory, pid controller, feedback loop, control system, kalman filter, servo
fetched: 2026-07-02
---

# Transfer function

In engineering, a **transfer function** (also known as **system function** or **network function**) of a system, sub-system, or component is a mathematical function that models the system's output for each possible input. It is widely used in electronic engineering tools like circuit simulators and control systems and in chemical reaction engineering for the study and modeling of the residence time distribution and stability of a reactor. In simple cases, this function can be represented as a two-dimensional graph of an independent scalar input versus the dependent scalar output (known as a **transfer curve** or **characteristic curve**). Transfer functions for components are used to design and analyze systems assembled from components, particularly using the block diagram technique, in electronics and control theory.

Dimensions and units of the transfer function model the output response of the device for a range of possible inputs. The transfer function of a two-port electronic circuit, such as an amplifier, might be a two-dimensional graph of the scalar voltage at the output as a function of the scalar voltage applied to the input; the transfer function of an electromechanical actuator might be the mechanical displacement of the movable arm as a function of electric current applied to the device; the transfer function of a photodetector might be the output voltage as a function of the luminous intensity of incident light of a given wavelength.

The term *transfer function* is also used in the frequency domain analysis of systems using transform methods, such as the Laplace transform; it is the amplitude of the output as a function of the frequency of the input signal. The transfer function of an electronic filter is the amplitude at the output as a function of the frequency of a constant amplitude sine wave applied to the input. For optical imaging devices, the optical transfer function is the Fourier transform of the point spread function (a function of spatial frequency).

## Linear time-invariant systems

Transfer functions are commonly used in the analysis of systems such as single-input single-output filters in signal processing, communication theory, and control theory. The term is often used exclusively to refer to linear time-invariant (LTI) systems. Most real systems have non-linear input–output characteristics, but many systems operated within nominal parameters (not over-driven) have behavior close enough to linear that LTI system theory is an acceptable representation of their input–output behavior.

### Continuous-time

Descriptions are given in terms of a complex variable, $s=\sigma +j\cdot \omega$ . In many applications it is sufficient to set $\sigma =0$ (thus $s=j\cdot \omega$ ), which reduces the Laplace transforms with complex arguments to Fourier transforms with the real argument ω. This is common in applications primarily interested in the LTI system's steady-state response (often the case in signal processing and communication theory), not the fleeting turn-on and turn-off transient response or stability issues.

For continuous-time input signal $x(t)$ and output $y(t)$ , dividing the Laplace transform of the output, $Y(s)={\mathcal {L}}\left\{y(t)\right\}$ , by the Laplace transform of the input, $X(s)={\mathcal {L}}\left\{x(t)\right\}$ , yields the system's transfer function $H(s)$ :

$H(s)={\frac {Y(s)}{X(s)}}={\frac {{\mathcal {L}}\left\{y(t)\right\}}{{\mathcal {L}}\left\{x(t)\right\}}}$

which can be rearranged as:

$Y(s)=H(s)\;X(s)\,.$

### Discrete-time

Discrete-time signals may be notated as arrays indexed by an integer n (e.g. $x[n]$ for input and $y[n]$ for output). Instead of using the Laplace transform (which is better for continuous-time signals), discrete-time signals are dealt with using the z-transform (notated with a corresponding capital letter, like $X(z)$ and $Y(z)$ ), so a discrete-time system's transfer function can be written as:

$H(z)={\frac {Y(z)}{X(z)}}={\frac {{\mathcal {Z}}\{y[n]\}}{{\mathcal {Z}}\{x[n]\}}}.$

### Direct derivation from differential equations

A linear differential equation with constant coefficients

$L[u]={\frac {d^{n}u}{dt^{n}}}+a_{1}{\frac {d^{n-1}u}{dt^{n-1}}}+\dotsb +a_{n-1}{\frac {du}{dt}}+a_{n}u=r(t)$

where *u* and *r* are suitably smooth functions of *t*, has *L* as the operator defined on the relevant function space that transforms *u* into *r*. That kind of equation can be used to constrain the output function *u* in terms of the *forcing* function *r*. The transfer function can be used to define an operator $F[r]=u$ that serves as a right inverse of *L*, meaning that $L[F[r]]=r$ .

Solutions of the homogeneous constant-coefficient differential equation $L[u]=0$ can be found by trying $u=e^{\lambda t}$ . That substitution yields the characteristic polynomial

$p_{L}(\lambda )=\lambda ^{n}+a_{1}\lambda ^{n-1}+\dotsb +a_{n-1}\lambda +a_{n}\,$

The inhomogeneous case can be easily solved if the input function *r* is also of the form $r(t)=e^{st}$ . By substituting $u=H(s)e^{st}$ , $L[H(s)e^{st}]=e^{st}$ if we define

$H(s)={\frac {1}{p_{L}(s)}}\qquad {\text{wherever }}\quad p_{L}(s)\neq 0.$

Other definitions of the transfer function are used, for example $1/p_{L}(ik).$

### Gain, transient behavior and stability

A general sinusoidal input to a system of frequency $\omega _{0}/(2\pi )$ may be written $\exp(j\omega _{0}t)$ . The response of a system to a sinusoidal input beginning at time $t=0$ will consist of the sum of the steady-state response and a transient response. The steady-state response is the output of the system in the limit of infinite time, and the transient response is the difference between the response and the steady-state response; it corresponds to the homogeneous solution of the differential equation. The transfer function for an LTI system may be written as the product:

$H(s)=\prod _{i=1}^{N}{\frac {1}{s-s_{P_{i}}}}$

where *sPi* are the *N* roots of the characteristic polynomial and will be the poles of the transfer function. In a transfer function with a single pole $H(s)={\frac {1}{s-s_{P}}}$ where $s_{P}=\sigma _{P}+j\omega _{P}$ , the Laplace transform of a general sinusoid of unit amplitude will be ${\frac {1}{s-j\omega _{0}}}$ . The Laplace transform of the output will be ${\frac {H(s)}{s-j\omega _{0}}}$ , and the temporal output will be the inverse Laplace transform of that function:

$g(t)={\frac {e^{j\,\omega _{0}\,t}-e^{(\sigma _{P}+j\,\omega _{P})t}}{-\sigma _{P}+j(\omega _{0}-\omega _{P})}}$

The second term in the numerator is the transient response, and in the limit of infinite time it will diverge to infinity if *σP* is positive. For a system to be stable, its transfer function must have no poles whose real parts are positive. If the transfer function is strictly stable, the real parts of all poles will be negative and the transient behavior will tend to zero in the limit of infinite time. The steady-state output will be:

$g(\infty )={\frac {e^{j\,\omega _{0}\,t}}{-\sigma _{P}+j(\omega _{0}-\omega _{P})}}$

The frequency response (or "gain") *G* of the system is defined as the absolute value of the ratio of the output amplitude to the steady-state input amplitude:

$G(\omega _{i})=\left|{\frac {1}{-\sigma _{P}+j(\omega _{0}-\omega _{P})}}\right|={\frac {1}{\sqrt {\sigma _{P}^{2}+(\omega _{P}-\omega _{0})^{2}}}},$

which is the absolute value of the transfer function $H(s)$ evaluated at $j\omega _{i}$ . This result is valid for any number of transfer-function poles.

### Steady state behavior for sinusoidal excitation

The steady state behavior of a linear system

$\sum _{i=0}^{n}a_{i}y^{(i)}+\sum _{j=0}^{m}b_{j}u^{(j)}=0$

for sinusoidal excitation $u(t)=\sin(\omega t)$ can be expressed in terms of its transfer function

$g(s)={\frac {b_{m}s^{m}+...+b_{0}}{a_{n}s^{n}+...+a_{0}}},$

evaluated at $s=j\omega$ , i.e. with real part $\sigma =0$ :

$y(t)=|g(j\omega )|\sin(\omega t+\arg(g(j\omega ))).$

To show this, use the ansatz function

$y(t)=ce^{j\omega t},$

plug it into the above given differential equation, solve for c , and note that $c=g(j\omega )$ .

From the complex identity $z=|z|e^{j\arg(z)}$ , the argument follows.

## Signal processing

If $x(t)$ is the input to a general linear time-invariant system, and $y(t)$ is the output, and the bilateral Laplace transform of $x(t)$ and $y(t)$ is

${\begin{aligned}X(s)&={\mathcal {L}}\left\{x(t)\right\}\ {\stackrel {\mathrm {def} }{=}}\ \int _{-\infty }^{\infty }x(t)e^{-st}\,dt,\\Y(s)&={\mathcal {L}}\left\{y(t)\right\}\ {\stackrel {\mathrm {def} }{=}}\ \int _{-\infty }^{\infty }y(t)e^{-st}\,dt.\end{aligned}}$

The output is related to the input by the transfer function $H(s)$ as

$Y(s)=H(s)X(s)$

and the transfer function itself is

$H(s)={\frac {Y(s)}{X(s)}}.$

If a complex harmonic signal with a sinusoidal component with amplitude $|X|$ , angular frequency $\omega$ and phase $\arg(X)$ , where arg is the argument

$x(t)=Xe^{j\omega t}=|X|e^{j(\omega t+\arg(X))}$

where

$X=|X|e^{j\arg(X)}$

is input to a linear time-invariant system, the corresponding component in the output is:

${\begin{aligned}y(t)&=Ye^{j\omega t}=|Y|e^{j(\omega t+\arg(Y))},\\Y&=|Y|e^{j\arg(Y)}.\end{aligned}}$

In a linear time-invariant system, the input frequency $\omega$ has not changed; only the amplitude and phase angle of the sinusoid have been changed by the system. The frequency response $H(j\omega )$ describes this change for every frequency $\omega$ in terms of gain

$G(\omega )={\frac {|Y|}{|X|}}=|H(j\omega )|$

and phase shift

$\phi (\omega )=\arg(Y)-\arg(X)=\arg(H(j\omega )).$

The phase delay (the frequency-dependent amount of delay introduced to the sinusoid by the transfer function) is

$\tau _{\phi }(\omega )=-{\frac {\phi (\omega )}{\omega }}.$

The group delay (the frequency-dependent amount of delay introduced to the envelope of the sinusoid by the transfer function) is found by computing the derivative of the phase shift with respect to angular frequency $\omega$ ,

$\tau _{g}(\omega )=-{\frac {d\phi (\omega )}{d\omega }}.$

The transfer function can also be shown using the Fourier transform, a special case of bilateral Laplace transform where $s=j\omega$ .

### Common transfer-function families

Although any LTI system can be described by some transfer function, "families" of special transfer functions are commonly used:

- Butterworth filter – maximally flat in passband and stopband for the given order
- Chebyshev filter (Type I) – maximally flat in stopband, sharper cutoff than a Butterworth filter of the same order
- Chebyshev filter (Type II) – maximally flat in passband, sharper cutoff than a Butterworth filter of the same order
- Bessel filter – maximally constant group delay for a given order
- Elliptic filter – sharpest cutoff (narrowest transition between passband and stopband) for the given order
- Optimum "L" filter
- Gaussian filter – minimum group delay; gives no overshoot to a step function
- Raised-cosine filter

## Control engineering

In control engineering and control theory, the transfer function is derived with the Laplace transform. The transfer function was the primary tool used in classical control engineering. A transfer matrix can be obtained for any linear system to analyze its dynamics and other properties; each element of a transfer matrix is a transfer function relating a particular input variable to an output variable. A representation bridging state space and transfer function methods was proposed by Howard H. Rosenbrock, and is known as the Rosenbrock system matrix.

## Imaging

In imaging, transfer functions are used to describe the relationship between the scene light, the image signal and the displayed light.

## Non-linear systems

Transfer functions do not exist for many non-linear systems, such as relaxation oscillators; however, describing functions can sometimes be used to approximate such nonlinear time-invariant systems.
