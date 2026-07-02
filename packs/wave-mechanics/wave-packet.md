---
title: "Wave packet"
source: https://en.wikipedia.org/wiki/Wave_packet
domain: wave-mechanics
license: CC-BY-SA-4.0
tags: wave equation, dispersion relation, group velocity, wave packet
fetched: 2026-07-02
---

# Wave packet

In physics, a **wave packet** (also known as a **wave train** or **wave group**) is a short burst of localized wave action that travels as a unit, outlined by an envelope. A wave packet can be analyzed into, or can be synthesized from, a potentially-infinite set of component sinusoidal waves of different wavenumbers, with phases and amplitudes such that they interfere constructively only over a small region of space, and destructively elsewhere. Any signal of a limited width in time or space requires many frequency components around a center frequency within a bandwidth inversely proportional to that width; even a Gaussian function is considered a wave packet because its Fourier transform is a "packet" of waves of frequencies clustered around a central frequency. Each component wave function, and hence the wave packet, are solutions of a wave equation. Depending on the wave equation, the wave packet's profile may remain constant (no dispersion) or it may change (dispersion) while propagating.

## Historical background

Ideas related to wave packets – modulation, carrier waves, phase velocity, and group velocity – date from the mid-1800s. The idea of a group velocity distinct from a wave's phase velocity was first proposed by W.R. Hamilton in 1839, and the first full treatment was by Rayleigh in his "Theory of Sound" in 1877.

Erwin Schrödinger introduced the idea of wave packets just after publishing his famous wave equation. He solved his wave equation for a quantum harmonic oscillator, introduced the superposition principle, and used it to show that a compact state could persist. While this work did result in the important concept of coherent states, the wave packet concept did not endure. The year after Schrödinger's paper, Werner Heisenberg published his paper on the uncertainty principle, showing in the process, that Schrödinger's results only applied to quantum harmonic oscillators, not for example to Coulomb potential characteristic of atoms.

The following year, 1927, Charles Galton Darwin explored Schrödinger's equation for an unbound electron in free space, assuming an initial Gaussian wave packet. Darwin showed that at time t later the position x of the packet traveling at velocity v would be

$x_{0}+vt\pm {\sqrt {\sigma ^{2}+(ht/2\pi \sigma m)^{2}}}$

where $\sigma$ is the uncertainty in the initial position.

Later in 1927 Paul Ehrenfest showed that the time, T for a matter wave packet of width $\Delta x$ and mass m to spread by a factor of 2 was ${\textstyle T\approx m{\Delta x}^{2}/\hbar }$ . Since $\hbar$ is so small, wave packets on the scale of macroscopic objects, with large width and mass, double only at cosmic time scales.

## Significance in quantum mechanics

Quantum mechanics describes the nature of atomic and subatomic systems using Schrödinger's wave equation. The classical limit of quantum mechanics and many formulations of quantum scattering use wave packets formed from various solutions to this equation. Quantum wave packet profiles change while propagating; they show dispersion. Physicists have concluded that "wave packets would not do as representations of subatomic particles".

### Wave packets and the classical limit

Schrodinger developed wave packets in hopes of interpreting quantum wave solutions as locally compact wave groups. Such packets trade off position localization for spreading momentum. In the coordinate representation of the wave (such as the Cartesian coordinate system), the position of the particle's localized probability is specified by the position of the packet solution. The narrower the spatial wave packet, and therefore the better localized the position of the wave packet, the larger the spread in the momentum of the wave. This trade-off between spread in position and spread in momentum is a characteristic feature of the Heisenberg uncertainty principle.

One kind of optimal tradeoff minimizes the product of position uncertainty $\Delta x$ and momentum uncertainty $\Delta p_{x}$ . If we place such a packet at rest it stays at rest: the average value of the position and momentum match a classical particle. However it spreads out in all directions with a velocity given by the optimal momentum uncertainty $\Delta p_{x}$ . The spread is so fast that in the distance of once around an atom the wave packet is unrecognizable.

### Wave packets and quantum scattering

Particle interactions are called scattering in physics; the wave packet concept plays an important role in quantum scattering approaches. A monochromatic (single momentum) source produces convergence difficulties in the scattering models. Scattering problems also have classical limits. Whenever the scattering target (for example an atom) has a size much smaller than wave packet, the center of the wave packet follows scattering classical trajectories. In other cases, the wave packet distorts and scatters as it interacts with the target.

## Basic behaviors

### Non-dispersive

Without dispersion the wave packet maintains its shape as it propagates. As an example of propagation *without dispersion*, consider wave solutions to the following wave equation from classical physics ${\partial ^{2}u \over \partial t^{2}}=c^{2}\,\nabla ^{2}u,$

where *c* is the speed of the wave's propagation in a given medium.

Using the physics time convention, *e*−*iωt*, the wave equation has plane-wave solutions $u(\mathbf {x} ,t)=e^{i{(\mathbf {k\cdot x} }-\omega (\mathbf {k} )t)},$

where the relation between the angular frequency *ω* and angular wave vector **k** is given by the dispersion relation: $\omega (\mathbf {k} )=\pm |\mathbf {k} |c=\pm {\frac {2\pi c}{\lambda }},$ such that $\omega ^{2}/|\mathbf {k} |^{2}=c^{2}$ . This relation should be valid so that the plane wave is a solution to the wave equation. As the relation is *linear*, the wave equation is said to be **non-dispersive**.

To simplify, consider the one-dimensional wave equation with *ω(k)*=*±kc*. Then the general solution is $u(x,t)=Ae^{ik(x-ct)}+Be^{ik(x+ct)},$ where the first and second term represent a wave propagating in the positive respectively negative *x*-direction.

A wave packet is a localized disturbance that results from the sum of many different wave forms. If the packet is strongly localized, more frequencies are needed to allow the constructive superposition in the region of localization and destructive superposition outside the region. From the basic one-dimensional plane-wave solutions, a general form of a wave packet can be expressed as $u(x,t)={\frac {1}{\sqrt {2\pi }}}\int _{-\infty }^{\,\infty }A(k)~e^{i(kx-\omega (k)t)}\,dk.$ where the amplitude *A*(*k*), containing the coefficients of the wave superposition, follows from taking the inverse Fourier transform of a "sufficiently nice" initial wave *u*(*x*, *t*) evaluated at *t* = 0: $A(k)={\frac {1}{\sqrt {2\pi }}}\int _{-\infty }^{\,\infty }u(x,0)~e^{-ikx}\,dx.$ and $1/{\sqrt {2\pi }}$ comes from Fourier transform conventions.

For example, choosing $u(x,0)=e^{-x^{2}+ik_{0}x},$

we obtain $A(k)={\frac {1}{\sqrt {2}}}e^{-{\frac {(k-k_{0})^{2}}{4}}},$

and finally ${\begin{aligned}u(x,t)&=e^{-(x-ct)^{2}+ik_{0}(x-ct)}\\&=e^{-(x-ct)^{2}}\left[\cos \left(2\pi {\frac {x-ct}{\lambda }}\right)+i\sin \left(2\pi {\frac {x-ct}{\lambda }}\right)\right].\end{aligned}}$

The nondispersive propagation of the real or imaginary part of this wave packet is presented in the above animation.

### Dispersive

By contrast, in the case of dispersion, a wave changes shape during propagation. For example, the free Schrödinger equation , $i\hbar {\frac {\partial \psi }{\partial t}}=-{\frac {\hbar ^{2}}{2m}}\nabla ^{2}\psi ,$ has plane-wave solutions of the form: $\psi (\mathbf {r} ,t)=Ae^{i{[\mathbf {k\cdot r} }-\omega (\mathbf {k} )t]},$ where A is a constant and the dispersion relation satisfies $\omega (\mathbf {k} )={\frac {\hbar \mathbf {k} ^{2}}{2m}}={\frac {\hbar }{2m}}(k_{x}^{2}+k_{y}^{2}+k_{z}^{2}),$ with the subscripts denoting unit vector notation. As the dispersion relation is non-linear, the free Schrödinger equation is **dispersive**.

In this case, the wave packet is given by: $\psi (\mathbf {r} ,t)={\frac {1}{(2\pi )^{3/2}}}\int g(\mathbf {k} )e^{i{[\mathbf {k\cdot r} }-\omega (\mathbf {k} )t]}d^{3}k$ where once again $g(\mathbf {k} )$ is simply the Fourier transform of $\psi (\mathbf {r} ,0)$ . If $\psi (\mathbf {r} ,0)$ (and therefore $g(\mathbf {k} )$ ) is a Gaussian function, the wave packet is called a **Gaussian wave packet**.

For example, the solution to the one-dimensional free Schrödinger equation (with 2Δ*x*, m, and *ħ* set equal to one) satisfying the initial condition $\psi (x,0)={\sqrt[{4}]{2/\pi }}\exp \left({-x^{2}+ik_{0}x}\right),$ representing a wave packet localized in space at the origin as a Gaussian function, is seen to be ${\begin{aligned}\psi (x,t)&={\frac {\sqrt[{4}]{2/\pi }}{\sqrt {1+2it}}}e^{-{\frac {1}{4}}k_{0}^{2}}~e^{-{\frac {1}{1+2it}}\left(x-{\frac {ik_{0}}{2}}\right)^{2}}\\&={\frac {\sqrt[{4}]{2/\pi }}{\sqrt {1+2it}}}e^{-{\frac {1}{1+4t^{2}}}(x-k_{0}t)^{2}}~e^{i{\frac {1}{1+4t^{2}}}\left((k_{0}+2tx)x-{\frac {1}{2}}tk_{0}^{2}\right)}~.\end{aligned}}$

An impression of the dispersive behavior of this wave packet is obtained by looking at the probability density: $|\psi (x,t)|^{2}={\frac {\sqrt {2/\pi }}{\sqrt {1+4t^{2}}}}~e^{-{\frac {2(x-k_{0}t)^{2}}{1+4t^{2}}}}~.$ It is evident that this dispersive wave packet, while moving with constant group velocity *ko*, is delocalizing rapidly: it has a width increasing with time as √ 1 + 4*t*2 → 2*t*, so eventually it diffuses to an unlimited region of space.

## Gaussian wave packets in quantum mechanics

The above dispersive Gaussian wave packet, unnormalized and just centered at the origin, instead, at t=0, can now be written in 3D, now in standard units: $\psi (\mathbf {r} ,0)=e^{-\mathbf {r} \cdot \mathbf {r} /2a},$ The Fourier transform is also a Gaussian in terms of the wavenumber, the **k**-vector, $\psi (\mathbf {k} ,0)=(2\pi a)^{3/2}e^{-a\mathbf {k} \cdot \mathbf {k} /2}.$ With a and its inverse adhering to the uncertainty relation $\Delta x\Delta p_{x}=\hbar /2,$ such that $a=2\langle \mathbf {r} \cdot \mathbf {r} \rangle /3\langle 1\rangle =2(\Delta x)^{2},$ can be considered the *square of the width of the wave packet*, whereas its inverse can be written as $1/a=2\langle \mathbf {k} \cdot \mathbf {k} \rangle /3\langle 1\rangle =2(\Delta p_{x}/\hbar )^{2}.$

Each separate wave only phase-rotates in time, so that the time dependent Fourier-transformed solution is

${\begin{aligned}\Psi (\mathbf {k} ,t)&=(2\pi a)^{3/2}e^{-a\mathbf {k} \cdot \mathbf {k} /2}e^{-iEt/\hbar }\\&=(2\pi a)^{3/2}e^{-a\mathbf {k} \cdot \mathbf {k} /2-i(\hbar ^{2}\mathbf {k} \cdot \mathbf {k} /2m)t/\hbar }\\&=(2\pi a)^{3/2}e^{-(a+i\hbar t/m)\mathbf {k} \cdot \mathbf {k} /2}.\end{aligned}}$

The inverse Fourier transform is still a Gaussian, but now the parameter a has become complex, and there is an overall normalization factor.

$\Psi (\mathbf {r} ,t)=\left({a \over a+i\hbar t/m}\right)^{3/2}e^{-{\mathbf {r} \cdot \mathbf {r} \over 2(a+i\hbar t/m)}}.$

The integral of Ψ over all space is invariant, because it is the inner product of Ψ with the state of zero energy, which is a wave with infinite wavelength, a constant function of space. For any energy eigenstate *η*(*x*), the inner product, $\langle \eta |\psi \rangle =\int \eta (\mathbf {r} )\psi (\mathbf {r} )d^{3}\mathbf {r} ,$ only changes in time in a simple way: its phase rotates with a frequency determined by the energy of *η*. When *η* has zero energy, like the infinite wavelength wave, it doesn't change at all.

For a given t , the phase of the wave function varies with position as ${\frac {\hbar t/m}{2(a^{2}+(\hbar t/m)^{2})}}\|\mathbf {r} \|^{2}$ . It varies *quadratically* with position, which means that it is different from multiplication by a linear phase factor $e^{i\mathbf {k} \cdot \mathbf {r} }$ as is the case of imparting a constant momentum to the wave packet. In general, the phase of a gaussian wave packet has both a linear term and a quadratic term. The coefficient of the quadratic term begins by increasing from $-\infty$ towards 0 as the gaussian wave packet becomes sharper, then at the moment of maximum sharpness, the phase of the wave function varies linearly with position. Then the coefficient of the quadratic term increases from 0 towards $+\infty$ , as the gaussian wave packet spreads out again.

The integral ∫ |Ψ|2*d*3*r* is also invariant, which is a statement of the conservation of probability. Explicitly, $P(r)=|\Psi |^{2}=\Psi ^{*}\Psi =\left({a \over {\sqrt {a^{2}+(\hbar t/m)^{2}}}}\right)^{3}~e^{-{a\,\mathbf {r} \cdot \mathbf {r} \over a^{2}+(\hbar t/m)^{2}}},$ where *r* is the distance from the origin, the speed of the particle is zero, and width given by ${\sqrt {a^{2}+(\hbar t/m)^{2} \over a}},$ which is √*a* at (arbitrarily chosen) time *t* = 0 while eventually growing linearly in time, as *ħt*/(*m*√*a*), indicating **wave-packet spreading**.

For example, if an electron wave packet is initially localized in a region of atomic dimensions (i.e., 10−10 m) then the width of the packet doubles in about 10−16 s. Clearly, particle wave packets spread out very rapidly indeed (in free space): For instance, after 1 ms, the width will have grown to about a kilometer.

This linear growth is a reflection of the (time-invariant) momentum uncertainty: the wave packet is confined to a narrow Δ*x* = √*a*/2, and so has a momentum which is uncertain (according to the uncertainty principle) by the amount *ħ*/√2*a*, a spread in velocity of *ħ/m*√2*a*, and thus in the future position by *ħt /m*√2*a*. The uncertainty relation is then a strict inequality, very far from saturation, indeed! The initial uncertainty Δ*x*Δ*p* = *ħ*/2 has now increased by a factor of *ħt/ma* (for large *t*).

### The 2D case

A gaussian 2D quantum wave function:

$\psi (x,y,t)=\psi (x,t)\psi (y,t)$

$\psi (x,t)=\left({\frac {2a^{2}}{\pi }}\right)^{1/4}{\frac {e^{i\phi }}{\left(a^{4}+{\frac {4\hbar ^{2}t^{2}}{m^{2}}}\right)^{1/4}}}e^{ik_{0}x}\exp \left[-{\frac {\left(x-{\frac {\hbar k_{0}}{m}}t\right)^{2}}{a^{2}+{\frac {2i\hbar t}{m}}}}\right]$

where

$\phi =-\theta -{\frac {\hbar k_{0}^{2}}{2m}}t$

$\tan(2\theta )={\frac {2\hbar t}{ma^{2}}}$

## The Airy wave train

In contrast to the above Gaussian wave packet, which moves at constant group velocity, and always disperses, there exists a wave function based on Airy functions, that propagates freely without envelope dispersion, maintaining its shape, and accelerates in free space: $\psi =\operatorname {Ai} \left[{\frac {B}{\hbar ^{2/3}}}\left(x-{\frac {B^{3}t^{2}}{4m^{2}}}\right)\right]e^{(iB^{3}t/2m\hbar )[x-(B^{3}t^{2}/6m^{2})]},$ where, for simplicity (and nondimensionalization), choosing *ħ* = 1, *m* = 1/2, and *B* an arbitrary constant results in $\psi =\operatorname {Ai} [B(x-B^{3}t^{2})]\,e^{iB^{3}t(x-{\tfrac {2}{3}}B^{3}t^{2})}\,.$

There is no dissonance with Ehrenfest's theorem in this force-free situation, because the state is both non-normalizable and has an undefined (infinite) ⟨*x*⟩ for all times. (To the extent that it could be defined, ⟨*p*⟩ = 0 for all times, despite the apparent acceleration of the front.)

The Airy wave train is the only dispersionless wave in one dimensional free space. In higher dimensions, other dispersionless waves are possible.

In phase space, this is evident in the pure state Wigner quasiprobability distribution of this wavetrain, whose shape in *x* and *p* is invariant as time progresses, but whose features accelerate to the right, in accelerating parabolas. The Wigner function satisfies ${\begin{aligned}W(x,p;t)&=W(x-B^{3}t^{2},p-B^{3}t;0)\\&={\frac {1}{2^{1/3}\pi B}}\,\mathrm {Ai} \left(2^{2/3}\left(B(x-B^{3}t^{2}\right)+\left(p/B-tB^{2})^{2}\right)\right)\\&=W(x-2pt,p;0).\end{aligned}}$ The three equalities demonstrate three facts:

1. Time-evolution is equivalent to a translation in phase-space by $(B^{3}t^{2},B^{3}t)$ .
2. The contour lines of the Wigner function are parabolas of form ${\textstyle B\left(x-B^{3}t^{2}\right)+\left(p/B-tB^{2}\right)^{2}=C}$ .
3. Time-evolution is equivalent to a shearing in phase space along the x -direction at speed $p/m=2p$ .

Note the momentum distribution obtained by integrating over all x is constant. Since this is the probability density in momentum space, it is evident that the wave function itself is not normalizable.

## Free propagator

The narrow-width limit of the Gaussian wave packet solution discussed is the free propagator kernel K. For other differential equations, this is usually called the Green's function, but in quantum mechanics it is traditional to reserve the name Green's function for the time Fourier transform of K.

Returning to one dimension for simplicity, with *m* and ħ set equal to one, when a is the infinitesimal quantity ε, the Gaussian initial condition, rescaled so that its integral is one, $\psi _{0}(x)={1 \over {\sqrt {2\pi \varepsilon }}}e^{-{x^{2} \over 2\varepsilon }}\,$ becomes a delta function, *δ*(*x*), so that its time evolution, $K_{t}(x)={1 \over {\sqrt {2\pi (it+\varepsilon )}}}e^{-x^{2} \over 2(it+\varepsilon )}\,$ yields the propagator.

Note that a very narrow initial wave packet instantly becomes infinitely wide, but with a phase which is more rapidly oscillatory at large values of *x*. This might seem strange—the solution goes from being localized at one point to being "everywhere" at *all later times*, but it is a reflection of the enormous momentum uncertainty of a localized particle, as explained above.

Further note that the norm of the wave function is infinite, which is also correct, since the square of a delta function is divergent in the same way.

The factor involving ε is an infinitesimal quantity which is there to make sure that integrals over K are well defined. In the limit that *ε* → 0, K becomes purely oscillatory, and integrals of K are not absolutely convergent. In the remainder of this section, it *will* be set to zero, but in order for all the integrations over intermediate states to be well defined, the limit *ε*→0 is to be only taken after the final state is calculated.

The propagator is the amplitude for reaching point *x* at time *t*, when starting at the origin, *x*=0. By translation invariance, the amplitude for reaching a point *x* when starting at point *y* is the same function, only now translated, $K_{t}(x,y)=K_{t}(x-y)={1 \over {\sqrt {2\pi it}}}e^{i(x-y)^{2} \over 2t}\,.$

In the limit when *t* is small, the propagator goes to a delta function $\lim _{t\to 0}K_{t}(x-y)=\delta (x-y)~,$ but only in the sense of distributions: The integral of this quantity multiplied by an arbitrary differentiable test function gives the value of the test function at zero.

To see this, note that the integral over all space of K equals 1 at all times, $\int K_{t}(x)dx=1\,,$ since this integral is the inner-product of *K* with the uniform wave function. But the phase factor in the exponent has a nonzero spatial derivative everywhere except at the origin, and so when the time is small there are fast phase cancellations at all but one point. This is rigorously true when the limit *ε*→0 is taken at the very end.

So the propagation kernel is the (future) time evolution of a delta function, and it is continuous, in a sense: it goes to the initial delta function at small times. If the initial wave function is an infinitely narrow spike at position y, $\psi _{0}(x)=\delta (x-y)\,,$ it becomes the oscillatory wave, $\psi _{t}(x)={1 \over {\sqrt {2\pi it}}}e^{i(x-y)^{2}/2t}\,.$

Now, since every function can be written as a weighted sum of such narrow spikes, $\psi _{0}(x)=\int \psi _{0}(y)\delta (x-y)dy\,,$ the time evolution of *every function* ψ0 is determined by this propagation kernel K,

$\psi _{t}(x)=\int \psi _{0}(y){1 \over {\sqrt {2\pi it}}}e^{i(x-y)^{2}/2t}dy\,.$

Thus, this is a formal way to express the fundamental solution or ***general solution***. The interpretation of this expression is that the amplitude for a particle to be found at point x at time t is the amplitude that it started at y, times the amplitude that it went from y to x, *summed over all the possible starting points*. In other words, it is a convolution of the kernel K with the arbitrary initial condition *ψ*0, $\psi _{t}=K*\psi _{0}\,.$

Since the amplitude to travel from x to y after a time t+t' can be considered in two steps, the propagator obeys the composition identity, $\int K(x-y;t)K(y-z;t')dy=K(x-z;t+t')~,$ which can be interpreted as follows: the amplitude to travel from x to z in time t+t' is the sum of the amplitude to travel from x to y in time t, multiplied by the amplitude to travel from y to z in time t', summed over *all possible intermediate states y*. This is a property of an arbitrary quantum system, and by subdividing the time into many segments, it allows the time evolution to be expressed as a path integral.

## Analytic continuation to diffusion

The spreading of wave packets in quantum mechanics is directly related to the spreading of probability densities in diffusion. For a particle which is randomly walking, the probability density function satisfies the diffusion equation ${\partial \over \partial t}\rho ={1 \over 2}{\partial ^{2} \over \partial x^{2}}\rho ,$ where the factor of 2, which can be removed by rescaling either time or space, is only for convenience.

A solution of this equation is the time-varying Gaussian function $\rho _{t}(x)={1 \over {\sqrt {2\pi t}}}e^{-x^{2} \over 2t},$ which is a form of the heat kernel. Since the integral of *ρt* is constant while the width is becoming narrow at small times, this function approaches a delta function at *t*=0, $\lim _{t\to 0}\rho _{t}(x)=\delta (x)$ again only in the sense of distributions, so that $\lim _{t\to 0}\int _{x}f(x)\rho _{t}(x)=f(0)$ for any test function f.

The time-varying Gaussian is the propagation kernel for the diffusion equation and it obeys the convolution identity, $K_{t+t'}=K_{t}*K_{t'}\,,$ which allows diffusion to be expressed as a path integral. The propagator is the exponential of an operator H, $K_{t}(x)=e^{-tH}\,,$ which is the infinitesimal diffusion operator, $H=-{\nabla ^{2} \over 2}\,.$

A matrix has two indices, which in continuous space makes it a function of x and x'. In this case, because of translation invariance, the matrix element K only depend on the difference of the position, and a convenient abuse of notation is to refer to the operator, the matrix elements, and the function of the difference by the same name: $K_{t}(x,x')=K_{t}(x-x')\,.$

Translation invariance means that continuous matrix multiplication, $C(x,x'')=\int _{x'}A(x,x')B(x',x'')\,,$ is essentially convolution, $C(\Delta )=C(x-x'')=\int _{x'}A(x-x')B(x'-x'')=\int _{y}A(\Delta -y)B(y)\,.$

The exponential can be defined over a range of *t*s which include complex values, so long as integrals over the propagation kernel stay convergent, $K_{z}(x)=e^{-zH}\,.$ As long as the real part of z is positive, for large values of x, K is exponentially decreasing, and integrals over K are indeed absolutely convergent.

The limit of this expression for z approaching the pure imaginary axis is the above Schrödinger propagator encountered, $K_{t}^{\rm {Schr}}=K_{it+\varepsilon }=e^{-(it+\varepsilon )H}\,,$ which illustrates the above time evolution of Gaussians.

From the fundamental identity of exponentiation, or path integration, $K_{z}*K_{z'}=K_{z+z'}\,$ holds for all complex *z* values, where the integrals are absolutely convergent so that the operators are well defined.

Thus, quantum evolution of a Gaussian, which is the complex diffusion kernel *K*, $\psi _{0}(x)=K_{a}(x)=K_{a}*\delta (x)\,$ amounts to the time-evolved state, $\psi _{t}=K_{it}*K_{a}=K_{a+it}\,.$

This illustrates the above diffusive form of the complex Gaussian solutions, $\psi _{t}(x)={1 \over {\sqrt {2\pi (a+it)}}}e^{-{x^{2} \over 2(a+it)}}\,.$
