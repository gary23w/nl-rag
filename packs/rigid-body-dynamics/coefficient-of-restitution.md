---
title: "Coefficient of restitution"
source: https://en.wikipedia.org/wiki/Coefficient_of_restitution
domain: rigid-body-dynamics
license: CC-BY-SA-4.0
tags: rigid body dynamics, rigid body simulation, angular velocity, moment of inertia
fetched: 2026-07-02
---

# Coefficient of restitution

In classical mechanics, the **coefficient of restitution** (**COR**, also denoted by ***e***), is a measure of the springiness of collisions between two surfaces. **Newton's law of restitution** states that the relative speed of separation of two surfaces immediately after a collision is directly proportional to the relative speed of approach of the surfaces immediately before the collision, the constant of proportionality called the coefficient of restitution, a dimensionless parameter that is a property of a pair of surfaces. In most real-world collisions, the coefficient of restitution is between 0 and 1, where 1 represents a perfectly elastic collision (in which the objects rebound with no loss of kinetic energy but in the opposite directions) and 0 a perfectly inelastic collision (in which the objects do not rebound at all, and end up coalescing). The basic equation, sometimes known as Newton's **restitution equation**, was developed by Sir Isaac Newton in 1687. ${\text{Coefficient of restitution }}(e)={\frac {\left|{\text{Relative velocity of separation after collision}}\right|}{\left|{\text{Relative velocity of approach before collision}}\right|}}$

## Introduction

### As a property of paired objects

The COR is a property of a *pair* of objects in a collision, not a single object. If a given object collides with two different objects, each collision has its own COR. When a single object is described as having a given coefficient of restitution, as if it were an intrinsic property without reference to a second object, some assumptions have been made – for example that the collision is with another identical object, or with a perfectly rigid wall.

### Treated as a constant

In a basic analysis of collisions, *e* is generally treated as a dimensionless constant, independent of the mass and relative velocities of the two objects, with the collision being treated as effectively instantaneous. An example often used for teaching is the collision of two idealised billiard balls. Real world interactions may be more complicated, for example where the internal structure of the objects needs to be taken into account, or where there are more complex effects happening during the time between initial contact and final separation.

### Range of values for *e*

***e*** is usually a positive, real number between 0 and 1:

- ***e* = 0**: This is a perfectly *inelastic* collision in which the objects do not rebound at all and end up touching.
- **0 < *e* < 1**: This is a real-world *inelastic* collision, in which some kinetic energy is dissipated. The objects rebound with a lower separation speed than the speed of approach.
- ***e* = 1**: This is a perfectly *elastic* collision, in which no kinetic energy is dissipated. The objects rebound with the same relative speed with which they approached.

Values outside that range are in principle possible, though in practice they would not normally be analysed with a basic analysis that takes *e* to be a constant:

- ***e* < 0**: A COR less than zero implies a collision in which the objects pass through one another, for example a bullet passing through a target.
- ***e* > 1**: This implies a superelastic collision in which the objects rebound with a greater relative speed than the speed of approach, due to some additional stored energy being released during the collision.

## Equations

In the case of a one-dimensional collision involving two idealised objects, A and B, the coefficient of restitution is given by: $e={\frac {\left|v_{\text{b}}-v_{\text{a}}\right|}{\left|u_{\text{a}}-u_{\text{b}}\right|}},$ where:

- $v_{\text{a}}$ is the final velocity of object A after impact
- $v_{\text{b}}$ is the final velocity of object B after impact
- $u_{\text{a}}$ is the initial velocity of object A before impact
- $u_{\text{b}}$ is the initial velocity of object B before impact

This is sometimes known as the **restitution equation**. For a perfectly elastic collision, *e = 1* and the objects rebound with the same relative speed with which they approached. For a perfectly inelastic collision *e = 0* and the objects do not rebound at all.

For an object bouncing off a stationary target, *e* is defined as the ratio of the object's rebound speed after the impact to that prior to impact: $e={\frac {v}{u}},$ where

- u is the speed of the object before impact
- v is the speed of the rebounding object (in the opposite direction) after impact

In a case where frictional forces can be neglected and the object is dropped from rest onto a horizontal surface, this is equivalent to: $e={\sqrt {\frac {h}{H}}},$ where

- H is the drop height
- h is the bounce height

The coefficient of restitution can be thought of as a measure of the extent to which energy is conserved when an object bounces off a surface. In the case of an object bouncing off a stationary target, the change in gravitational potential energy, *E*p, during the course of the impact is essentially zero; thus, *e* is a comparison between the kinetic energy, *E*k, of the object immediately before impact with that immediately after impact: $e={\sqrt {\frac {E_{\text{k, (after impact)}}}{E_{\text{k, (before impact)}}}}}={\sqrt {\frac {{\frac {1}{2}}mv^{2}}{{\frac {1}{2}}mu^{2}}}}={\sqrt {\frac {v^{2}}{u^{2}}}}={\frac {v}{u}}$ In a case where frictional forces can be neglected (nearly every student laboratory on this subject), and the object is dropped from rest onto a horizontal surface, the above is equivalent to a comparison between the *E*p of the object at the drop height with that at the bounce height. In this case, the change in *E*k is zero (the object is essentially at rest during the course of the impact and is also at rest at the apex of the bounce); thus: $e={\sqrt {\frac {E_{\text{p, (at bounce height)}}}{E_{\text{p, (at drop height)}}}}}={\sqrt {\frac {mgh}{mgH}}}={\sqrt {\frac {h}{H}}}$

## Velocity and energy after impact

### Velocity

Although *e* does not vary with the masses of the colliding objects, their final velocities are mass-dependent due to conservation of momentum: $v_{\text{a}}={\frac {m_{\text{a}}u_{\text{a}}+m_{\text{b}}u_{\text{b}}+m_{\text{b}}e(u_{\text{b}}-u_{\text{a}})}{m_{\text{a}}+m_{\text{b}}}}$ and $v_{\text{b}}={\frac {m_{\text{a}}u_{\text{a}}+m_{\text{b}}u_{\text{b}}+m_{\text{a}}e(u_{\text{a}}-u_{\text{b}})}{m_{\text{a}}+m_{\text{b}}}}$ where

- $v_{\text{a}}$ is the velocity of A after impact
- $v_{\text{b}}$ is the velocity of B after impact
- $u_{\text{a}}$ is the velocity of A before impact
- $u_{\text{b}}$ is the velocity of B before impact
- $m_{\text{a}}$ is the mass of A
- $m_{\text{b}}$ is the mass of B

### Energy

Kinetic energy loss in CM frame: $\Delta T=-(1-e^{2})\cdot \Delta T_{0,{\text{CM}}}=-(1-e^{2})\cdot {\frac {1}{2}}\cdot {\frac {m_{\text{a}}m_{\text{b}}}{m_{\text{a}}+m_{\text{b}}}}\cdot (u_{\text{a}}-u_{\text{b}})^{2}$

where

- $\Delta T$ is the kinetic energy lost during the collision
- e is the coefficient of restitution
- $\Delta T_{0,{\text{CM}}}$ is the initial kinetic energy in the center of mass frame
- $m_{\text{a}}$ is the mass of object A
- $m_{\text{b}}$ is the mass of object B
- $u_{\text{a}}$ is the velocity of A before collision
- $u_{\text{b}}$ is the velocity of B before collision

## Practical issues

### Measurement

In practical situations, the coefficient of restitution between two bodies may have to be determined experimentally, for example using the Leeb rebound hardness test. This uses a tip of tungsten carbide, one of the hardest substances available, dropped onto test samples from a specific height.

A comprehensive study of coefficients of restitution in dependence on material properties (elastic moduli, rheology), direction of impact, coefficient of friction and adhesive properties of impacting bodies can be found in Willert (2020).

### Application in sports

Thin-faced golf club drivers utilize a "trampoline effect" that creates drives of a greater distance as a result of the flexing and subsequent release of stored energy which imparts greater impulse to the ball. The USGA (America's governing golfing body) tests drivers for COR and has placed the upper limit at 0.83. COR is a function of rates of clubhead speeds and diminish as clubhead speed increase. In the report COR ranges from 0.845 for 90 mph to as low as 0.797 at 130 mph. The above-mentioned "trampoline effect" shows this since it reduces the rate of stress of the collision by increasing the time of the collision. According to one article (addressing COR in tennis racquets), "for the Benchmark Conditions, the coefficient of restitution used is 0.85 for all racquets, eliminating the variables of string tension and frame stiffness which could add or subtract from the coefficient of restitution."

The International Table Tennis Federation specifies that the ball shall bounce up 24–26 cm when dropped from a height of 30.5 cm on to a standard steel block, implying a COR of 0.887 to 0.923.

The International Basketball Federation (FIBA) rules require that the ball rebound to a height of between 1035 and 1085 mm when dropped from a height of 1800 mm, implying a COR between 0.758 and 0.776.
