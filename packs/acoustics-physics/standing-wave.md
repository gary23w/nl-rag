---
title: "Standing wave"
source: https://en.wikipedia.org/wiki/Standing_wave
domain: acoustics-physics
license: CC-BY-SA-4.0
tags: acoustic wave, standing wave, doppler effect, sound resonance
fetched: 2026-07-02
---

# Standing wave

In physics, a **standing wave**, also known as a **stationary wave**, is a wave that oscillates in time but whose peak amplitude profile does not move in space. The peak amplitude of the wave oscillations at any point in space is constant with respect to time, and the oscillations at different points throughout the wave are in phase. The locations at which the absolute value of the amplitude is minimum are called nodes, and the locations where the absolute value of the amplitude is maximum are called antinodes.

Standing waves were first described scientifically by Michael Faraday in 1831. Faraday observed standing waves on the surface of a liquid in a vibrating container. Franz Melde coined the term "standing wave" (German: *stehende Welle* or *Stehwelle*) around 1860 and demonstrated the phenomenon in his classic experiment with vibrating strings.

This phenomenon can occur because the medium is moving in the direction opposite to the movement of the wave, or it can arise in a stationary medium as a result of interference between two waves traveling in opposite directions. The most common cause of standing waves is the phenomenon of resonance, in which standing waves occur inside a resonator due to interference between waves reflected back and forth at the resonator's resonant frequency.

For waves of equal amplitude traveling in opposing directions, there is on average no net propagation of energy.

## Moving medium

- Kayakers surfing a standing wave in Great Falls Park
- Mouth of the Carmel River - Standing waves are formed where the Carmel River meets the Pacific Ocean.

As an example of the first type, under certain meteorological conditions standing waves form in the atmosphere in the lee of mountain ranges. Such waves are often exploited by glider pilots.

Standing waves and hydraulic jumps also form on fast flowing river rapids and tidal currents such as the Saltstraumen maelstrom. A requirement for this in river currents is a flowing water with shallow depth in which the inertia of the water overcomes its gravity due to the supercritical flow speed (Froude number: 1.7 – 4.5, surpassing 4.5 results in direct standing wave) and is therefore neither significantly slowed down by the obstacle nor pushed to the side. Many standing river waves are popular river surfing breaks.

## Opposing waves

| Standing waves |
|---|
| (Standing wave in stationary medium. The red dots represent the wave nodes.) Standing wave in stationary medium. The red dots represent the wave nodes. (A standing wave (black) depicted as the sum of two propagating waves traveling in opposite directions (red and blue).) A standing wave (black) depicted as the sum of two propagating waves traveling in opposite directions (red and blue). |
| (Electric force vector (E) and magnetic force vector (H) of a standing wave.) Electric force vector (E) and magnetic force vector (H) of a standing wave. (Standing waves in a string – the fundamental mode and the first 5 harmonics.) Standing waves in a string – the fundamental mode and the first 5 harmonics. |
| (A standing wave on a circular membrane, an example of standing waves in two dimensions. This is the fundamental mode.) A standing wave on a circular membrane, an example of standing waves in two dimensions. This is the fundamental mode. (A higher harmonic standing wave on a disk with two nodal lines crossing at the center.) A higher harmonic standing wave on a disk with two nodal lines crossing at the center. |

As an example of the second type, a *standing wave* in a transmission line is a wave in which the distribution of current, voltage, or field strength is formed by the superposition of two waves of the same frequency propagating in opposite directions. The effect is a series of nodes (zero displacement) and anti-nodes (maximum displacement) at fixed points along the transmission line. Such a standing wave may be formed when a wave is transmitted into one end of a transmission line and is reflected from the other end by an impedance mismatch, *i.e.*, discontinuity, such as an open circuit or a short. The failure of the line to transfer power at the standing wave frequency will usually result in attenuation distortion.

In practice, losses in the transmission line and other components mean that a perfect reflection and a pure standing wave are never achieved. The result is a *partial standing wave*, which is a superposition of a standing wave and a traveling wave. The degree to which the wave resembles either a pure standing wave or a pure traveling wave is measured by the standing wave ratio (SWR).

Another example is standing waves in the open ocean formed by waves with the same wave period moving in opposite directions. These may form near storm centres, or from reflection of a swell at the shore, and are the source of microbaroms and microseisms.

## Mathematical description

This section considers representative one- and two-dimensional cases of standing waves. First, an example of an infinite length string shows how identical waves traveling in opposite directions interfere to produce standing waves. Next, two finite length string examples with different boundary conditions demonstrate how the boundary conditions restrict the frequencies that can form standing waves. Next, the example of sound waves in a pipe demonstrates how the same principles can be applied to longitudinal waves with analogous boundary conditions.

Standing waves can also occur in two- or three-dimensional resonators. With standing waves on two-dimensional membranes such as drumheads, illustrated in the animations above, the nodes become nodal lines, lines on the surface at which there is no movement, that separate regions vibrating with opposite phase. These nodal line patterns are called Chladni figures. In three-dimensional resonators, such as musical instrument sound boxes and microwave cavity resonators, there are nodal surfaces. This section includes a two-dimensional standing wave example with a rectangular boundary to illustrate how to extend the concept to higher dimensions.

### Standing wave on an infinite length string

To begin, consider a string of infinite length along the *x*-axis that is free to be stretched transversely in the *y* direction.

For a harmonic wave traveling to the right along the string, the string's displacement in the *y* direction as a function of position *x* and time *t* is

$y_{\text{R}}(x,t)=y_{\text{max}}\sin \left({2\pi x \over \lambda }-\omega t\right).$

The displacement in the *y*-direction for an identical harmonic wave traveling to the left is

$y_{\text{L}}(x,t)=y_{\text{max}}\sin \left({2\pi x \over \lambda }+\omega t\right),$

where

- *y*max is the amplitude of the displacement of the string for each wave,
- *ω* is the angular frequency or equivalently *2π* times the frequency *f*,
- *λ* is the wavelength of the wave.

For identical right- and left-traveling waves on the same string, the total displacement of the string is the sum of *y*R and *y*L,

$y(x,t)=y_{\text{R}}+y_{\text{L}}=y_{\text{max}}\sin \left({2\pi x \over \lambda }-\omega t\right)+y_{\text{max}}\sin \left({2\pi x \over \lambda }+\omega t\right).$

Using the trigonometric sum-to-product identity $\sin a+\sin b=2\sin \left({a+b \over 2}\right)\cos \left({a-b \over 2}\right)$ ,

| $y(x,t)=2y_{\text{max}}\sin \left({2\pi x \over \lambda }\right)\cos(\omega t).$ |   | 1 |
|---|---|---|

Equation (**1**) does not describe a traveling wave. At any position *x*, *y*(*x*,*t*) simply oscillates in time with an amplitude that varies in the *x*-direction as $2y_{\text{max}}\sin \left({2\pi x \over \lambda }\right)$ . The animation at the beginning of this article depicts what is happening. As the left-traveling blue wave and right-traveling green wave interfere, they form the standing red wave that does not travel and instead oscillates in place.

Because the string is of infinite length, it has no boundary condition for its displacement at any point along the *x*-axis. As a result, a standing wave can form at any frequency.

At locations on the *x*-axis that are *even* multiples of a quarter wavelength,

$x=\ldots ,-{3\lambda \over 2},\;-\lambda ,\;-{\lambda \over 2},\;0,\;{\lambda \over 2},\;\lambda ,\;{3\lambda \over 2},\ldots$

the amplitude is always zero. These locations are called nodes. At locations on the *x*-axis that are *odd* multiples of a quarter wavelength

$x=\ldots ,-{5\lambda \over 4},\;-{3\lambda \over 4},\;-{\lambda \over 4},\;{\lambda \over 4},\;{3\lambda \over 4},\;{5\lambda \over 4},\ldots$

the amplitude is maximal, with a value of twice the amplitude of the right- and left-traveling waves that interfere to produce this standing wave pattern. These locations are called anti-nodes. The distance between two consecutive nodes or anti-nodes is half the wavelength, *λ*/2.

### Standing wave on a string with two fixed ends

Next, consider a string with fixed ends at *x* = 0 and *x* = *L*. The string will have some damping as it is stretched by traveling waves, but assume the damping is very small. Suppose that at the *x* = 0 fixed end a sinusoidal force is applied that drives the string up and down in the y-direction with a small amplitude at some frequency *f*. In this situation, the driving force produces a right-traveling wave. That wave reflects off the right fixed end and travels back to the left, reflects again off the left fixed end and travels back to the right, and so on. Eventually, a steady state is reached where the string has identical right- and left-traveling waves as in the infinite-length case and the power dissipated by damping in the string equals the power supplied by the driving force so the waves have constant amplitude.

Equation (**1**) still describes the standing wave pattern that can form on this string, but now Equation (**1**) is subject to boundary conditions where *y* = 0 at *x* = 0 and *x* = *L* because the string is fixed at *x* = *L* and because we assume the driving force at the fixed *x* = 0 end has small amplitude. Checking the values of *y* at the two ends,

$y(0,t)=0,$

$y(L,t)=2y_{\text{max}}\sin \left({2\pi L \over \lambda }\right)\cos(\omega t)=0.$

This boundary condition is in the form of the Sturm–Liouville formulation. The latter boundary condition is satisfied when $\sin \left({2\pi L \over \lambda }\right)=0$ . *L* is given, so the boundary condition restricts the wavelength of the standing waves to

| $\lambda ={\frac {2L}{n}},$ |   | 2 |
|---|---|---|

$n=1,2,3,\ldots$

Waves can only form standing waves on this string if they have a wavelength that satisfies this relationship with *L*. If waves travel with speed *v* along the string, then equivalently the frequency of the standing waves is restricted to

$f={\frac {v}{\lambda }}={\frac {nv}{2L}}.$

The standing wave with *n* = 1 oscillates at the fundamental frequency and has a wavelength that is twice the length of the string. Higher integer values of *n* correspond to modes of oscillation called harmonics or overtones. Any standing wave on the string will have *n* + 1 nodes including the fixed ends and *n* anti-nodes.

To compare this example's nodes to the description of nodes for standing waves in the infinite length string, Equation (**2**) can be rewritten as

$\lambda ={\frac {4L}{n}},$

$n=2,4,6,\ldots$

In this variation of the expression for the wavelength, *n* must be even. Cross multiplying we see that because *L* is a node, it is an *even* multiple of a quarter wavelength,

$L={\frac {n\lambda }{4}},$

$n=2,4,6,\ldots$

This example demonstrates a type of resonance and the frequencies that produce standing waves can be referred to as *resonant frequencies*.

### Standing wave on a string with one fixed end

Next, consider the same string of length *L*, but this time it is only fixed at *x* = 0. At *x* = *L*, the string is free to move in the *y* direction. For example, the string might be tied at *x* = *L* to a ring that can slide freely up and down a pole. The string again has small damping and is driven by a small driving force at *x* = 0.

In this case, Equation (**1**) still describes the standing wave pattern that can form on the string, and the string has the same boundary condition of *y* = 0 at *x* = 0. However, at *x* = *L* where the string can move freely there should be an anti-node with maximal amplitude of *y*. Equivalently, this boundary condition of the "free end" can be stated as *∂y/∂x* = 0 at *x* = *L*, which is in the form of the Sturm–Liouville formulation. The intuition for this boundary condition *∂y/∂x* = 0 at *x* = *L* is that the motion of the "free end" will follow that of the point to its left.

Reviewing Equation (**1**), for *x* = *L* the largest amplitude of *y* occurs when *∂y/∂x* = 0, or

$\cos \left({2\pi L \over \lambda }\right)=0.$

This leads to a different set of wavelengths than in the two-fixed-ends example. Here, the wavelength of the standing waves is restricted to

$\lambda ={\frac {4L}{n}},$

$n=1,3,5,\ldots$

Equivalently, the frequency is restricted to

$f={\frac {nv}{4L}}.$

In this example *n* only takes odd values. Because *L* is an anti-node, it is an *odd* multiple of a quarter wavelength. Thus the fundamental mode in this example only has one quarter of a complete sine cycle–zero at *x* = 0 and the first peak at *x* = *L*–the first harmonic has three quarters of a complete sine cycle, and so on.

This example also demonstrates a type of resonance and the frequencies that produce standing waves are called *resonant frequencies*.

### Standing wave in a pipe

Consider a standing wave in a pipe of length *L*. The air inside the pipe serves as the medium for longitudinal sound waves traveling to the right or left through the pipe. While the transverse waves on the string from the previous examples vary in their displacement perpendicular to the direction of wave motion, the waves traveling through the air in the pipe vary in terms of their pressure and longitudinal displacement along the direction of wave motion. The wave propagates by alternately compressing and expanding air in segments of the pipe, which displaces the air slightly from its rest position and transfers energy to neighboring segments through the forces exerted by the alternating high and low air pressures. Equations resembling those for the wave on a string can be written for the change in pressure Δ*p* due to a right- or left-traveling wave in the pipe.

$\Delta p_{\text{R}}(x,t)=p_{\text{max}}\sin \left({2\pi x \over \lambda }-\omega t\right),$

$\Delta p_{\text{L}}(x,t)=p_{\text{max}}\sin \left({2\pi x \over \lambda }+\omega t\right),$

where

- *p*max is the pressure amplitude or the maximum increase or decrease in air pressure due to each wave,
- *ω* is the angular frequency or equivalently *2π* times the frequency *f*,
- *λ* is the wavelength of the wave.

If identical right- and left-traveling waves travel through the pipe, the resulting superposition is described by the sum

$\Delta p(x,t)=\Delta p_{\text{R}}(x,t)+\Delta p_{\text{L}}(x,t)=2p_{\text{max}}\sin \left({2\pi x \over \lambda }\right)\cos(\omega t).$

This formula for the pressure is of the same form as Equation (**1**), so a stationary pressure wave forms that is fixed in space and oscillates in time.

If the end of a pipe is closed, the pressure is maximal since the closed end of the pipe exerts a force that restricts the movement of air. This corresponds to a pressure anti-node (which is a node for molecular motions, because the molecules near the closed end cannot move). If the end of the pipe is open, the pressure variations are very small, corresponding to a pressure node (which is an anti-node for molecular motions, because the molecules near the open end can move freely). The exact location of the pressure node at an open end is actually slightly beyond the open end of the pipe, so the effective length of the pipe for the purpose of determining resonant frequencies is slightly longer than its physical length. This difference in length is ignored in this example. In terms of reflections, open ends partially reflect waves back into the pipe, allowing some energy to be released into the outside air. Ideally, closed ends reflect the entire wave back in the other direction.

First consider a pipe that is open at both ends, for example an open organ pipe or a recorder. Given that the pressure must be zero at both open ends, the boundary conditions are analogous to the string with two fixed ends,

$\Delta p(0,t)=0,$

$\Delta p(L,t)=2p_{\text{max}}\sin \left({2\pi L \over \lambda }\right)\cos(\omega t)=0,$

which only occurs when the wavelength of standing waves is

$\lambda ={\frac {2L}{n}},$

$n=1,2,3,\ldots ,$

or equivalently when the frequency is

$f={\frac {nv}{2L}},$

where *v* is the speed of sound.

Next, consider a pipe that is open at *x* = 0 (and therefore has a pressure node) and closed at *x* = *L* (and therefore has a pressure anti-node). The closed "free end" boundary condition for the pressure at *x* = *L* can be stated as *∂(Δp)/∂x* = 0, which is in the form of the Sturm–Liouville formulation. The intuition for this boundary condition *∂(Δp)/∂x* = 0 at *x* = *L* is that the pressure of the closed end will follow that of the point to its left. Examples of this setup include a bottle and a clarinet. This pipe has boundary conditions analogous to the string with only one fixed end. Its standing waves have wavelengths restricted to

$\lambda ={\frac {4L}{n}},$

$n=1,3,5,\ldots ,$

or equivalently the frequency of standing waves is restricted to

$f={\frac {nv}{4L}}.$

For the case where one end is closed, *n* only takes odd values just like in the case of the string fixed at only one end.

So far, the wave has been written in terms of its pressure as a function of position *x* and time. Alternatively, the wave can be written in terms of its longitudinal displacement of air, where air in a segment of the pipe moves back and forth slightly in the *x*-direction as the pressure varies and waves travel in either or both directions. The change in pressure Δ*p* and longitudinal displacement *s* are related as

$\Delta p=-\rho v^{2}{\frac {\partial s}{\partial x}},$

where *ρ* is the density of the air. In terms of longitudinal displacement, closed ends of pipes correspond to nodes since air movement is restricted and open ends correspond to anti-nodes since the air is free to move. A similar, easier to visualize phenomenon occurs in longitudinal waves propagating along a spring.

We can also consider a pipe that is closed at both ends. In this case, both ends will be pressure anti-nodes or equivalently both ends will be displacement nodes. This example is analogous to the case where both ends are open, except the standing wave pattern has a π⁄2 phase shift along the *x*-direction to shift the location of the nodes and anti-nodes. For example, the longest wavelength that resonates–the fundamental mode–is again twice the length of the pipe, except that the ends of the pipe have pressure anti-nodes instead of pressure nodes. Between the ends there is one pressure node. In the case of two closed ends, the wavelength is again restricted to

$\lambda ={\frac {2L}{n}},$

$n=1,2,3,\ldots ,$

and the frequency is again restricted to

$f={\frac {nv}{2L}}.$

A Rubens tube provides a way to visualize the pressure variations of the standing waves in a tube with two closed ends.

### 2D standing wave with a rectangular boundary

Next, consider transverse waves that can move along a two dimensional surface within a rectangular boundary of length *Lx* in the *x*-direction and length *Ly* in the *y*-direction. Examples of this type of wave are water waves in a pool or waves on a rectangular sheet that has been pulled taut. The waves displace the surface in the *z*-direction, with *z* = 0 defined as the height of the surface when it is still.

In two dimensions and Cartesian coordinates, the wave equation is

${\frac {\partial ^{2}z}{\partial t^{2}}}\;=\;c^{2}\left({\frac {\partial ^{2}z}{\partial x^{2}}}+{\frac {\partial ^{2}z}{\partial y^{2}}}\right),$

where

- *z*(*x*,*y*,*t*) is the displacement of the surface,
- *c* is the speed of the wave.

To solve this differential equation, let's first solve for its Fourier transform, with

$Z(x,y,\omega )=\int _{-\infty }^{\infty }z(x,y,t)e^{-i\omega t}dt.$

Taking the Fourier transform of the wave equation,

${\frac {\partial ^{2}Z}{\partial x^{2}}}+{\frac {\partial ^{2}Z}{\partial y^{2}}}=-{\frac {\omega ^{2}}{c^{2}}}Z(x,y,\omega ).$

This is an eigenvalue problem where the frequencies correspond to eigenvalues that then correspond to frequency-specific modes or eigenfunctions. Specifically, this is a form of the Helmholtz equation and it can be solved using separation of variables. Assume

$Z=X(x)Y(y).$

Dividing the Helmholtz equation by *Z*,

${\frac {1}{X(x)}}{\frac {\partial ^{2}X}{\partial x^{2}}}+{\frac {1}{Y(y)}}{\frac {\partial ^{2}Y}{\partial y^{2}}}+{\frac {\omega ^{2}}{c^{2}}}=0.$

This leads to two coupled ordinary differential equations. The *x* term equals a constant with respect to *x* that we can define as

${\frac {1}{X(x)}}{\frac {\partial ^{2}X}{\partial x^{2}}}=(ik_{x})^{2}.$

Solving for *X*(*x*),

$X(x)=A_{k_{x}}e^{ik_{x}x}+B_{k_{x}}e^{-ik_{x}x}.$

This *x*-dependence is sinusoidal–recalling Euler's formula–with constants *A**k**x* and *B**k**x* determined by the boundary conditions. Likewise, the *y* term equals a constant with respect to *y* that we can define as

${\frac {1}{Y(y)}}{\frac {\partial ^{2}Y}{\partial y^{2}}}=(ik_{y})^{2}=k_{x}^{2}-{\frac {\omega ^{2}}{c^{2}}},$

and the dispersion relation for this wave is therefore

$\omega =c{\sqrt {k_{x}^{2}+k_{y}^{2}}}.$

Solving the differential equation for the *y* term,

$Y(y)=C_{k_{y}}e^{ik_{y}y}+D_{k_{y}}e^{-ik_{y}y}.$

Multiplying these functions together and applying the inverse Fourier transform, *z*(*x*,*y*,*t*) is a superposition of modes where each mode is the product of sinusoidal functions for *x*, *y*, and *t*,

$z(x,y,t)\sim e^{\pm ik_{x}x}e^{\pm ik_{y}y}e^{\pm i\omega t}.$

The constants that determine the exact sinusoidal functions depend on the boundary conditions and initial conditions. To see how the boundary conditions apply, consider an example like the sheet that has been pulled taut where *z*(*x*,*y*,*t*) must be zero all around the rectangular boundary. For the *x* dependence, *z*(*x*,*y*,*t*) must vary in a way that it can be zero at both *x* = 0 and *x* = *L**x* for all values of *y* and *t*. As in the one dimensional example of the string fixed at both ends, the sinusoidal function that satisfies this boundary condition is

$\sin {k_{x}x},$

with *k**x* restricted to

$k_{x}={\frac {n\pi }{L_{x}}},\quad n=1,2,3,\dots$

Likewise, the *y* dependence of *z*(*x*,*y*,*t*) must be zero at both *y* = 0 and *y* = *L**y*, which is satisfied by

$\sin {k_{y}y},\quad k_{y}={\frac {m\pi }{L_{y}}},\quad m=1,2,3,\dots$

Restricting the wave numbers to these values also restricts the frequencies that resonate to

$\omega =c\pi {\sqrt {\left({\frac {n}{L_{x}}}\right)^{2}+\left({\frac {m}{L_{y}}}\right)^{2}}}.$

If the initial conditions for *z*(*x*,*y*,0) and its time derivative *ż*(*x*,*y*,0) are chosen so the *t*-dependence is a cosine function, then standing waves for this system take the form

$z(x,y,t)=z_{\text{max}}\sin \left({\frac {n\pi x}{L_{x}}}\right)\sin \left({\frac {m\pi y}{L_{y}}}\right)\cos \left(\omega t\right).$

$n=1,2,3,\dots \quad m=1,2,3,\dots$

So, standing waves inside this fixed rectangular boundary oscillate in time at certain resonant frequencies parameterized by the integers *n* and *m*. As they oscillate in time, they do not travel and their spatial variation is sinusoidal in both the *x*- and *y*-directions such that they satisfy the boundary conditions. The fundamental mode, *n* = 1 and *m* = 1, has a single antinode in the middle of the rectangle. Varying *n* and *m* gives complicated but predictable two-dimensional patterns of nodes and antinodes inside the rectangle.

From the dispersion relation, in certain situations different modes–meaning different combinations of *n* and *m*–may resonate at the same frequency even though they have different shapes for their *x*- and *y*-dependence. For example, if the boundary is square, *L**x* = *L**y*, the modes *n* = 1 and *m* = 7, *n* = 7 and *m* = 1, and *n* = 5 and *m* = 5 all resonate at

$\omega ={\frac {c\pi }{L_{x}}}{\sqrt {50}}.$

Recalling that *ω* determines the eigenvalue in the Helmholtz equation above, the number of modes corresponding to each frequency relates to the frequency's multiplicity as an eigenvalue.

## Standing wave ratio, phase, and energy transfer

If the two oppositely moving traveling waves are not of the same amplitude, they will not cancel completely at the nodes, the points where the waves are 180° out of phase, so the amplitude of the standing wave will not be zero at the nodes, but merely a minimum. Standing wave ratio (SWR) is the ratio of the amplitude at the antinode (maximum) to the amplitude at the node (minimum). A pure standing wave will have an infinite SWR. It will also have a constant phase at any point in space (but it may undergo a 180° inversion every half cycle). A finite, non-zero SWR indicates a wave that is partially stationary and partially travelling. Such waves can be decomposed into a superposition of two waves: a travelling wave component and a stationary wave component. An SWR of one indicates that the wave does not have a stationary component – it is purely a travelling wave, since the ratio of amplitudes is equal to 1.

A pure standing wave does not transfer energy from the source to the destination. However, the wave is still subject to losses in the medium. Such losses will manifest as a finite SWR, indicating a travelling wave component leaving the source to supply the losses. Even though the SWR is now finite, it may still be the case that no energy reaches the destination because the travelling component is purely supplying the losses. However, in a lossless medium, a finite SWR implies a definite transfer of energy to the destination.

## Examples

One easy example to understand standing waves is two people shaking either end of a jump rope. If they shake in sync the rope can form a regular pattern of waves oscillating up and down, with stationary points along the rope where the rope is almost still (nodes) and points where the arc of the rope is maximum (antinodes).

### Acoustic resonance

Standing waves are also observed in physical media such as strings and columns of air. Any waves traveling along the medium will reflect back when they reach the end. This effect is most noticeable in musical instruments where, at various multiples of a vibrating string or air column's natural frequency, a standing wave is created, allowing harmonics to be identified. Nodes occur at fixed ends and anti-nodes at open ends. If fixed at only one end, only odd-numbered harmonics are available. At the open end of a pipe the anti-node will not be exactly at the end as it is altered by its contact with the air and so end correction is used to place it exactly. The density of a string will affect the frequency at which harmonics will be produced; the greater the density the lower the frequency needs to be to produce a standing wave of the same harmonic.

### Visible light

Standing waves are also observed in optical media such as optical waveguides and optical cavities. Lasers use optical cavities in the form of a pair of facing mirrors, which constitute a Fabry–Pérot interferometer. The gain medium in the cavity (such as a crystal) emits light coherently, exciting standing waves of light in the cavity. The wavelength of light is very short (in the range of nanometers, 10−9 m) so the standing waves are microscopic in size. One use for standing light waves is to measure small distances, using optical flats.

### X-rays

Interference between X-ray beams can form an X-ray standing wave (XSW) field. Because of the short wavelength of X-rays (less than 1 nanometer), this phenomenon can be exploited for measuring atomic-scale events at material surfaces. The XSW is generated in the region where an X-ray beam interferes with a diffracted beam from a nearly perfect single crystal surface or a reflection from an X-ray mirror. By tuning the crystal geometry or X-ray wavelength, the XSW can be translated in space, causing a shift in the X-ray fluorescence or photoelectron yield from the atoms near the surface. This shift can be analyzed to pinpoint the location of a particular atomic species relative to the underlying crystal structure or mirror surface. The XSW method has been used to clarify the atomic-scale details of dopants in semiconductors, atomic and molecular adsorption on surfaces, and chemical transformations involved in catalysis.

### Mechanical waves

Standing waves can be mechanically induced into a solid medium using resonance. One easy to understand example is two people shaking either end of a jump rope. If they shake in sync, the rope will form a regular pattern with nodes and antinodes and appear to be stationary, hence the name standing wave. Similarly a cantilever beam can have a standing wave imposed on it by applying a base excitation. In this case the free end moves the greatest distance laterally compared to any location along the beam. Such a device can be used as a sensor to track changes in frequency or phase of the resonance of the fiber. One application is as a measurement device for dimensional metrology.

### Seismic waves

Standing surface waves on the Earth are observed as free oscillations of the Earth.

### Faraday waves

The Faraday wave is a non-linear standing wave at the air-liquid interface induced by hydrodynamic instability. It can be used as a liquid-based template to assemble microscale materials.

### Seiches

A seiche is an example of a standing wave in an enclosed body of water. It is characterised by the oscillatory behaviour of the water level at either end of the body and typically has a nodal point near the middle of the body where very little change in water level is observed. It should be distinguished from a simple storm surge where no oscillation is present. In sizeable lakes, the period of such oscillations may be between minutes and hours, for example Lake Geneva's longitudinal period is 73 minutes and its transversal seiche has a period of around 10 minutes, while Lake Huron can be seen to have resonances with periods between 1 and 2 hours. See Lake seiches.
