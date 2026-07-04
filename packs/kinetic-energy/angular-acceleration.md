---
title: "Angular acceleration"
source: https://en.wikipedia.org/wiki/Angular_acceleration
domain: kinetic-energy
license: CC-BY-SA-4.0
tags: kinetic energy
fetched: 2026-07-04
---

# Angular acceleration

In kinematics, **angular acceleration** (symbol ***α***, alpha) is the time derivative of angular velocity. Following the two types of angular velocity, *spin angular velocity* and *orbital angular velocity*, the respective types of angular acceleration are: **spin angular acceleration**, involving a rigid body about an axis of rotation intersecting the body's centroid; and **orbital angular acceleration**, involving a point particle and an external axis.

Angular acceleration has physical dimensions of inverse time squared, with the SI unit **radian per second squared** (**rad⋅s−2**). In two dimensions, angular acceleration is a pseudoscalar whose sign is taken to be positive if the angular speed increases counterclockwise or decreases clockwise, and is taken to be negative if the angular speed increases clockwise or decreases counterclockwise. In three dimensions, angular acceleration is a pseudovector.

## Orbital angular acceleration of a point particle

### Particle in two dimensions

In two dimensions, the orbital angular acceleration is the rate at which the two-dimensional orbital angular velocity of the particle about the origin changes. The instantaneous angular velocity *ω* at any point in time is given by

$\omega ={\frac {v_{\perp }}{r}},$

where r is the distance from the origin and $v_{\perp }$ is the cross-radial component of the instantaneous velocity (i.e. the component perpendicular to the position vector), which by convention is positive for counter-clockwise motion and negative for clockwise motion.

Therefore, the instantaneous angular acceleration *α* of the particle is given by

$\alpha ={\frac {d}{dt}}\left({\frac {v_{\perp }}{r}}\right).$

Expanding the right-hand-side using the product rule from differential calculus, this becomes

$\alpha ={\frac {1}{r}}{\frac {dv_{\perp }}{dt}}-{\frac {v_{\perp }}{r^{2}}}{\frac {dr}{dt}}.$

In the special case where the particle undergoes circular motion about the origin, $\textstyle {\frac {dv_{\perp }}{dt}}$ becomes just the tangential acceleration $a_{\perp }$ , and $\textstyle {\frac {dr}{dt}}$ vanishes (since the distance from the origin stays constant), so the above equation simplifies to

$\alpha ={\frac {a_{\perp }}{r}}.$

In two dimensions, angular acceleration is a number with plus or minus sign indicating orientation, but not pointing in a direction. The sign is conventionally taken to be positive if the angular speed increases in the counter-clockwise direction or decreases in the clockwise direction, and the sign is taken negative if the angular speed increases in the clockwise direction or decreases in the counter-clockwise direction. Angular acceleration then may be termed a pseudoscalar, a numerical quantity which changes sign under a parity inversion, such as inverting one axis or switching the two axes.

### Particle in three dimensions

In three dimensions, the orbital angular acceleration is the rate at which three-dimensional orbital angular velocity vector changes with time. The instantaneous angular velocity vector ${\boldsymbol {\omega }}$ at any point in time is given by

${\boldsymbol {\omega }}={\frac {\mathbf {r} \times \mathbf {v} }{r^{2}}},$

where $\mathbf {r}$ is the particle's position vector, r its distance from the origin, and $\mathbf {v}$ its velocity vector.

Therefore, the orbital angular acceleration is the vector ${\boldsymbol {\alpha }}$ defined by

${\boldsymbol {\alpha }}={\frac {d}{dt}}\left({\frac {\mathbf {r} \times \mathbf {v} }{r^{2}}}\right).$

Expanding this derivative using the product rule for cross-products and the ordinary quotient rule, one gets:

${\begin{aligned}{\boldsymbol {\alpha }}&={\frac {1}{r^{2}}}\left(\mathbf {r} \times {\frac {d\mathbf {v} }{dt}}+{\frac {d\mathbf {r} }{dt}}\times \mathbf {v} \right)-{\frac {2}{r^{3}}}{\frac {dr}{dt}}\left(\mathbf {r} \times \mathbf {v} \right)\\\\&={\frac {1}{r^{2}}}\left(\mathbf {r} \times \mathbf {a} +\mathbf {v} \times \mathbf {v} \right)-{\frac {2}{r^{3}}}{\frac {dr}{dt}}\left(\mathbf {r} \times \mathbf {v} \right)\\\\&={\frac {\mathbf {r} \times \mathbf {a} }{r^{2}}}-{\frac {2}{r^{3}}}{\frac {dr}{dt}}\left(\mathbf {r} \times \mathbf {v} \right).\end{aligned}}$

Since $\mathbf {r} \times \mathbf {v}$ is just $r^{2}{\boldsymbol {\omega }}$ , the second term may be rewritten as $\textstyle -{\frac {2}{r}}{\frac {dr}{dt}}{\boldsymbol {\omega }}$ . In the case where the distance r of the particle from the origin does not change with time (which includes circular motion as a subcase), the second term vanishes and the above formula simplifies to

${\boldsymbol {\alpha }}={\frac {\mathbf {r} \times \mathbf {a} }{r^{2}}}.$

From the above equation, one can recover the cross-radial acceleration in this special case as:

$\mathbf {a} _{\perp }={\boldsymbol {\alpha }}\times \mathbf {r} .$

Unlike in two dimensions, the angular acceleration in three dimensions need not be associated with a change in the angular *speed* $\omega =|{\boldsymbol {\omega }}|$ : If the particle's position vector "twists" in space, changing its instantaneous plane of angular displacement, the change in the *direction* of the angular velocity ${\boldsymbol {\omega }}$ will still produce a nonzero angular acceleration. This cannot not happen if the position vector is restricted to a fixed plane, in which case ${\boldsymbol {\omega }}$ has a fixed direction perpendicular to the plane.

The angular acceleration vector is more properly called a pseudovector: It has three components which transform under rotations in the same way as the Cartesian coordinates of a point do, but which do not transform like Cartesian coordinates under reflections.

### Relation to torque

The net *torque* on a point particle is defined to be the pseudovector

${\boldsymbol {\tau }}=\mathbf {r} \times \mathbf {F} ,$

where $\mathbf {F}$ is the net force on the particle.

Torque is the rotational analogue of force: it induces change in the rotational state of a system, just as force induces change in the translational state of a system. As force on a particle is connected to acceleration by the equation $\mathbf {F} =m\mathbf {a}$ , one may write a similar equation connecting torque on a particle to angular acceleration, though this relation is necessarily more complicated.

First, substituting $\mathbf {F} =m\mathbf {a}$ into the above equation for torque, one gets

${\boldsymbol {\tau }}=m\left(\mathbf {r} \times \mathbf {a} \right)=mr^{2}\left({\frac {\mathbf {r} \times \mathbf {a} }{r^{2}}}\right).$

From the previous section:

${\boldsymbol {\alpha }}={\frac {\mathbf {r} \times \mathbf {a} }{r^{2}}}-{\frac {2}{r}}{\frac {dr}{dt}}{\boldsymbol {\omega }},$

where ${\boldsymbol {\alpha }}$ is orbital angular acceleration and ${\boldsymbol {\omega }}$ is orbital angular velocity. Therefore:

${\boldsymbol {\tau }}=mr^{2}\left({\boldsymbol {\alpha }}+{\frac {2}{r}}{\frac {dr}{dt}}{\boldsymbol {\omega }}\right)=mr^{2}{\boldsymbol {\alpha }}+2mr{\frac {dr}{dt}}{\boldsymbol {\omega }}.$

In the special case of constant distance r of the particle from the origin ( ${\tfrac {dr}{dt}}=0$ ), the second term in the above equation vanishes and the above equation simplifies to

${\boldsymbol {\tau }}=mr^{2}{\boldsymbol {\alpha }},$

which can be interpreted as a "rotational analogue" to $\mathbf {F} =m\mathbf {a}$ , where the quantity $mr^{2}$ (known as the moment of inertia of the particle) plays the role of the mass m . However, unlike $\mathbf {F} =m\mathbf {a}$ , this equation does *not* apply to an arbitrary trajectory, only to a trajectory contained within a spherical shell about the origin.
