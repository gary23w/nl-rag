---
title: "Simple harmonic motion"
source: https://en.wikipedia.org/wiki/Simple_harmonic_motion
domain: oscillations-resonance
license: CC-BY-SA-4.0
tags: harmonic oscillator, simple harmonic motion, damped oscillation, normal mode
fetched: 2026-07-02
---

# Simple harmonic motion

In mechanics and physics, **simple harmonic motion** (sometimes abbreviated as **SHM**) is a special type of periodic motion an object experiences by means of a restoring force whose magnitude is directly proportional to the distance of the object from an equilibrium position and acts towards the equilibrium position. It results in an oscillation that is described by a sinusoid which continues indefinitely (if uninhibited by friction or any other dissipation of energy).

Simple harmonic motion can serve as a mathematical model for a variety of motions, but is typified by the oscillation of a mass on a spring when it is subject to the linear elastic restoring force given by Hooke's law. The motion is sinusoidal in time and demonstrates a single resonant frequency. Other phenomena can be modeled by simple harmonic motion, including the motion of a simple pendulum, although for it to be an accurate model, the net force on the object at the end of the pendulum must be proportional to the displacement (and even so, it is only a good approximation when the angle of the swing is small; see small-angle approximation). Simple harmonic motion can also be used to model molecular vibration.

Simple harmonic motion provides a basis for the characterization of more complicated periodic motion through the techniques of Fourier analysis.

## Introduction

The motion of a particle moving along a straight line with an acceleration whose direction is always toward a fixed point on the line and whose magnitude is proportional to the displacement from the fixed point is called simple harmonic motion.

In the diagram, a simple harmonic oscillator, consisting of a weight attached to one end of a spring, is shown. The other end of the spring is connected to a rigid support such as a wall. If the system is left at rest at the equilibrium position then there is no net force acting on the mass. However, if the mass is displaced from the equilibrium position, the spring exerts a restoring elastic force that obeys Hooke's law.

Mathematically, $\mathbf {F} =-k\mathbf {x} ,$ where **F** is the restoring elastic force exerted by the spring (in SI units: N), *k* is the spring constant (N·m−1), and **x** is the displacement from the equilibrium position (in metres).

For any simple mechanical harmonic oscillator:

- When the system is displaced from its equilibrium position, a restoring force that obeys Hooke's law tends to restore the system to linear motion.

Once the mass is displaced from its equilibrium position, it experiences a net restoring force. As a result, it accelerates and starts going back to the equilibrium position. When the mass moves closer to the equilibrium position, the restoring force decreases. At the equilibrium position, the net restoring force vanishes. However, at *x* = 0, the mass has momentum because of the acceleration that the restoring force has imparted. Therefore, the mass continues past the equilibrium position, compressing the spring. A net restoring force then slows it down until its velocity reaches zero, whereupon it is accelerated back to the equilibrium position again.

As long as the system has no energy loss, the mass continues to oscillate. Thus simple harmonic motion is a type of periodic motion. If energy is lost in the system, then the mass exhibits damped oscillation.

Note if the real space and phase space plot are not co-linear, the phase space motion becomes elliptical. The area enclosed depends on the amplitude and the maximum momentum.

## Dynamics

In Newtonian mechanics, for one-dimensional simple harmonic motion, the equation of motion, which is a second-order linear ordinary differential equation with **constant** coefficients, can be obtained by means of Newton's second law and Hooke's law for a mass on a spring.

$F_{\mathrm {net} }=m{\frac {\mathrm {d} ^{2}x}{\mathrm {d} t^{2}}}=-kx,$ where m is the inertial mass of the oscillating body, x is its displacement from the equilibrium (or mean) position, and *k* is a constant (the spring constant for a mass on a spring).

Therefore, ${\frac {\mathrm {d} ^{2}x}{\mathrm {d} t^{2}}}=-{\frac {k}{m}}x$

Solving the differential equation above produces a solution that is a sinusoidal function: $x(t)=c_{1}\cos \left(\omega t\right)+c_{2}\sin \left(\omega t\right),$ where ${\textstyle {\omega }={\sqrt {{k}/{m}}}.}$ The meaning of the constants $c_{1}$ and $c_{2}$ can be easily found: setting $t=0$ on the equation above we see that $x(0)=c_{1}$ , so that $c_{1}$ is the initial position of the particle, $c_{1}=x_{0}$ ; taking the derivative of that equation and evaluating at zero we get that ${\dot {x}}(0)=\omega c_{2}$ , so that $c_{2}$ is the initial speed of the particle divided by the angular frequency, $c_{2}={\frac {v_{0}}{\omega }}$ . Thus we can write: $x(t)=x_{0}\cos \left({\sqrt {\frac {k}{m}}}t\right)+{\frac {v_{0}}{\sqrt {\frac {k}{m}}}}\sin \left({\sqrt {\frac {k}{m}}}t\right).$

This equation can also be written in the form: $x(t)=A\cos \left(\omega t-\varphi \right),$ where

- $A={\sqrt {{c_{1}}^{2}+{c_{2}}^{2}}}$
- $\tan \varphi ={\frac {c_{2}}{c_{1}}},$
- $\sin \varphi ={\frac {c_{2}}{A}},\;\cos \varphi ={\frac {c_{1}}{A}}$

or equivalently

- $A=|c_{1}+c_{2}i|,$
- $\varphi =\arg(c_{1}+c_{2}i)$

In the solution, *c*1 and *c*2 are two constants determined by the initial conditions (specifically, the initial position at time *t* = 0 is *c*1, while the initial velocity is *c*2*ω*), and the origin is set to be the equilibrium position. Each of these constants carries a physical meaning of the motion: *A* is the amplitude (maximum displacement from the equilibrium position), *ω* = 2*πf* is the angular frequency, and *φ* is the initial phase.

Using the techniques of calculus, the velocity and acceleration as a function of time can be found: $v(t)={\frac {\mathrm {d} x}{\mathrm {d} t}}=-A\omega \sin(\omega t-\varphi ),$

- Speed: ${\omega }{\sqrt {A^{2}-x^{2}}}$
- Maximum speed: *v* = *ωA* (at equilibrium point)

$a(t)={\frac {\mathrm {d} ^{2}x}{\mathrm {d} t^{2}}}=-A\omega ^{2}\cos(\omega t-\varphi ).$

- Maximum acceleration: *Aω*2 (at extreme points)

By definition, if a mass *m* is under SHM its acceleration is directly proportional to displacement. $a(x)=-\omega ^{2}x.$ where $\omega ^{2}={\frac {k}{m}}$

Since *ω* = 2*πf*, $f={\frac {1}{2\pi }}{\sqrt {\frac {k}{m}}},$ and, since *T* = ⁠1/*f*⁠ where *T* is the time period, $T=2\pi {\sqrt {\frac {m}{k}}}.$

These equations demonstrate that the simple harmonic motion is isochronous (the period and frequency are independent of the amplitude and the initial phase of the motion).

## Energy

Substituting *ω*2 with *⁠k/m⁠*, the kinetic energy *K* of the system at time *t* is $K(t)={\tfrac {1}{2}}mv^{2}(t)={\tfrac {1}{2}}m\omega ^{2}A^{2}\sin ^{2}(\omega t-\varphi )={\tfrac {1}{2}}kA^{2}\sin ^{2}(\omega t-\varphi ),$ and the potential energy is $U(t)={\tfrac {1}{2}}kx^{2}(t)={\tfrac {1}{2}}kA^{2}\cos ^{2}(\omega t-\varphi ).$ In the absence of friction and other energy loss, the total mechanical energy has a constant value $E=K+U={\tfrac {1}{2}}kA^{2}.$

## Examples

The following physical systems are some examples of simple harmonic oscillator.

### Mass on a spring

A mass *m* attached to a spring of spring constant *k* exhibits simple harmonic motion in closed space. The equation for describing the period: $T=2\pi {\sqrt {\frac {m}{k}}}$ shows the period of oscillation is independent of the amplitude, though in practice the amplitude should be small. The above equation is also valid in the case when an additional constant force is being applied on the mass, i.e. the additional constant force cannot change the period of oscillation.

### Uniform circular motion

Simple harmonic motion can be considered the one-dimensional projection of uniform circular motion. If an object moves with angular speed *ω* around a circle of radius *r* centered at the origin of the *xy*-plane, then its motion along each coordinate is simple harmonic motion with amplitude *r* and angular frequency *ω*.

### Oscillatory motion

The motion of a body in which it moves to-and-fro about a definite point is also called oscillatory motion or vibratory motion. The time period is able to be calculated by $T=2\pi {\sqrt {\frac {l}{g}}}$ where *l* is the distance from rotation to the object's center of mass undergoing SHM and *g* is acceleration due to gravity. This is analogous to the mass-spring system.

### Mass of a simple pendulum

In the small-angle approximation, the motion of a simple pendulum is approximated by simple harmonic motion. The period of a mass attached to a pendulum of length *l* with gravitational acceleration g is given by $T=2\pi {\sqrt {\frac {l}{g}}}$

This shows that the period of oscillation is independent of the amplitude and mass of the pendulum but not of the acceleration due to gravity, g , therefore a pendulum of the same length on the Moon would swing more slowly due to the Moon's lower gravitational field strength. Because the value of g varies slightly over the surface of the earth, the time period will vary slightly from place to place and will also vary with height above sea level.

This approximation is accurate only for small angles because of the expression for angular acceleration *α* being proportional to the sine of the displacement angle:

$-mgl\sin \theta =I\alpha ,$

where *I* is the moment of inertia. When *θ* is small, sin *θ* ≈ *θ* and therefore the expression becomes

$-mgl\theta =I\alpha$

which makes angular acceleration directly proportional and opposite to *θ*, satisfying the definition of simple harmonic motion (that net force is directly proportional to the displacement from the mean position and is directed towards the mean position).

### Scotch yoke

A Scotch yoke mechanism can be used to convert between rotational motion and linear reciprocating motion. The linear motion can take various forms depending on the shape of the slot, but the basic yoke with a constant rotation speed produces a linear motion that is simple harmonic in form.
