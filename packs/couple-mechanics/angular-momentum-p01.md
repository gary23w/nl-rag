---
title: "Angular momentum (part 1/2)"
source: https://en.wikipedia.org/wiki/Angular_momentum
domain: couple-mechanics
license: CC-BY-SA-4.0
tags: couple mechanics
fetched: 2026-07-05
part: 1/2
---

# Angular momentum

**Angular momentum** (sometimes called **moment of momentum** or **rotational momentum**) is the rotational analog of linear momentum. It is an important physical quantity because it is a conserved quantity – the total angular momentum of an isolated system remains constant. Angular momentum has both a direction and a magnitude, and both are conserved. Bicycles and motorcycles, flying discs, rifled bullets, and gyroscopes owe their useful properties to conservation of angular momentum. Conservation of angular momentum is also why hurricanes form spirals and neutron stars have high rotational rates. In general, conservation limits the possible motion of a system, but it does not uniquely determine it.

The three-dimensional angular momentum for a point particle is classically represented as a pseudovector **r** × **p**, the cross product of the particle's position vector **r** (relative to some origin) and its momentum vector; the latter is **p** = *m***v** in Newtonian mechanics. Unlike linear momentum, angular momentum depends on where this origin is chosen, since the particle's position is measured from it.

Angular momentum is an extensive quantity; that is, the total angular momentum of any composite system is the sum of the angular momenta of its constituent parts. For a continuous rigid body or a fluid, the total angular momentum is the volume integral of angular momentum density (angular momentum per unit volume in the limit as volume shrinks to zero) over the entire body.

Similar to conservation of linear momentum, where it is conserved if there is no external force, angular momentum is conserved if there is no external torque. Torque can be defined as the rate of change of angular momentum, analogous to force. The net *external* torque on any system is always equal to the *total* torque on the system; the sum of all internal torques of any system is always 0 (this is the rotational analogue of Newton's third law of motion). Therefore, for an isolated system (where there is no net external torque), the *total* torque on the system must be 0, which means that the total angular momentum of the system is constant.

The change in angular momentum for a particular interaction is called **angular impulse**, sometimes **twirl**. Angular impulse is the angular analog of (linear) impulse.


## Examples

The trivial case of the angular momentum L of a body in an orbit is given by $L=2\pi Mfr^{2}$ where M is the mass of the orbiting object, f is the orbit's frequency and r is the orbit's radius.

The angular momentum L of a uniform rigid sphere rotating around its axis, instead, is given by $L={\frac {4}{5}}\pi Mfr^{2}$ where M is the sphere's mass, f is the frequency of rotation and r is the sphere's radius.

Thus, for example, the orbital angular momentum of the Earth with respect to the Sun is about 2.66 × 1040 kg⋅m2⋅s−1, while its rotational angular momentum is about 7.05 × 1033 kg⋅m2⋅s−1.

In the case of a uniform rigid sphere rotating around its axis, if, instead of its mass, its density is known, the angular momentum L is given by $L={\frac {16}{15}}\pi ^{2}\rho fr^{5}$ where $\rho$ is the sphere's density, f is the frequency of rotation and r is the sphere's radius.

In the simplest case of a spinning disk, the angular momentum L is given by $L=\pi Mfr^{2}$ where M is the disk's mass, f is the frequency of rotation and r is the disk's radius.

If instead the disk rotates about its diameter (e.g. coin toss), its angular momentum L is given by $L={\frac {1}{2}}\pi Mfr^{2}$


## Definition in classical mechanics

Just as for angular velocity, there are two special types of angular momentum of an object: the **spin angular momentum** is the angular momentum about the object's center of mass, while the **orbital angular momentum** is the angular momentum about a chosen center of rotation. The Earth has an orbital angular momentum by nature of revolving around the Sun, and a spin angular momentum by nature of its daily rotation around the polar axis. The total angular momentum is the sum of the spin and orbital angular momenta. In the case of the Earth the primary conserved quantity is the total angular momentum of the Solar System because angular momentum is exchanged to a small but important extent among the planets and the Sun. The orbital angular momentum vector of a point particle is always parallel and directly proportional to its orbital angular velocity vector **ω**, where the constant of proportionality depends on both the mass of the particle and its distance from origin. The spin angular momentum vector of a rigid body is proportional but not always parallel to the spin angular velocity vector **Ω**, making the constant of proportionality a second-rank tensor rather than a scalar.

### Orbital angular momentum in two dimensions

Angular momentum is a vector quantity (more precisely, a pseudovector) that represents the product of a body's rotational inertia and rotational velocity (in radians/sec) about a particular axis. However, if the particle's trajectory lies in a single plane, it is sufficient to discard the vector nature of angular momentum, and treat it as a scalar (more precisely, a pseudoscalar). Angular momentum can be considered a rotational analog of linear momentum. Thus, where linear momentum p is proportional to mass m and linear speed v, $p=mv,$ angular momentum L is proportional to moment of inertia I and angular speed ω measured in radians per second. $L=I\omega .$

Unlike mass, which depends only on amount of matter, moment of inertia depends also on the position of the axis of rotation and the distribution of the matter. Unlike linear velocity, which does not depend upon the choice of origin, orbital angular velocity is always measured with respect to a fixed origin. Therefore, strictly speaking, L should be referred to as the angular momentum *relative to that center*.

In the case of circular motion of a single particle, we can use $I=r^{2}m$ and $\omega ={v}/{r}$ to expand angular momentum as $L=r^{2}m\cdot {v}/{r},$ reducing to: $L=rmv,$

the product of the radius of rotation r and the linear momentum of the particle $p=mv$ , where $v=r\omega$ is the linear (tangential) speed.

This simple analysis can also apply to non-circular motion if one uses the component of the motion perpendicular to the radius vector: $L=rmv_{\perp },$ where $v_{\perp }=v\sin(\theta )$ is the perpendicular component of the motion. Expanding, $L=rmv\sin(\theta ),$ rearranging, $L=r\sin(\theta )mv,$ and reducing, angular momentum can also be expressed, $L=r_{\perp }mv,$ where $r_{\perp }=r\sin(\theta )$ is the length of the *moment arm*, a line dropped perpendicularly from the origin onto the path of the particle. It is this definition, (length of moment arm) × (linear momentum), to which the term *moment of momentum* refers.

### Scalar angular momentum from Lagrangian mechanics

Another approach is to define angular momentum as the conjugate momentum (also called **canonical momentum**) of the angular coordinate $\phi$ expressed in the Lagrangian of the mechanical system. Consider a mechanical system with a mass m constrained to move in a circle of radius r in the absence of any external force field. The kinetic energy of the system is $T={\tfrac {1}{2}}mr^{2}\omega ^{2}={\tfrac {1}{2}}mr^{2}{\dot {\phi }}^{2}.$

And the potential energy is $U=0.$

Then the Lagrangian is ${\mathcal {L}}{\left(\phi ,{\dot {\phi }}\right)}=T-U={\tfrac {1}{2}}mr^{2}{\dot {\phi }}^{2}.$

The *generalized momentum* "canonically conjugate to" the coordinate $\phi$ is defined by $p_{\phi }={\frac {\partial {\mathcal {L}}}{\partial {\dot {\phi }}}}=mr^{2}{\dot {\phi }}=I\omega =L.$

### Orbital angular momentum in three dimensions

To completely define orbital angular momentum in three dimensions, it is required to know the rate at which the position vector sweeps out an angle, the direction perpendicular to the instantaneous plane of angular displacement, and the mass involved, as well as how this mass is distributed in space. By retaining this vector nature of angular momentum, the general nature of the equations is also retained, and can describe any sort of three-dimensional motion about the center of rotation – circular, linear, or otherwise. In vector notation, the orbital angular momentum of a point particle in motion about the origin can be expressed as: $\mathbf {L} =I{\boldsymbol {\omega }},$ where

- $I=r^{2}m$ is the moment of inertia for a point mass,
- ${\boldsymbol {\omega }}={\frac {\mathbf {r} \times \mathbf {v} }{r^{2}}}$ is the orbital angular velocity of the particle about the origin,
- $\mathbf {r}$ is the position vector of the particle relative to the origin, and $r=\left\vert \mathbf {r} \right\vert$ ,
- $\mathbf {v}$ is the linear velocity of the particle relative to the origin, and
- m is the mass of the particle.

This can be expanded, reduced, and by the rules of vector algebra, rearranged: ${\begin{aligned}\mathbf {L} &=\left(r^{2}m\right)\left({\frac {\mathbf {r} \times \mathbf {v} }{r^{2}}}\right)\\&=m\left(\mathbf {r} \times \mathbf {v} \right)\\&=\mathbf {r} \times m\mathbf {v} \\&=\mathbf {r} \times \mathbf {p} ,\end{aligned}}$ which is the cross product of the position vector $\mathbf {r}$ and the linear momentum $\mathbf {p} =m\mathbf {v}$ of the particle. By the definition of the cross product, the $\mathbf {L}$ vector is perpendicular to both $\mathbf {r}$ and $\mathbf {p}$ . It is directed perpendicular to the plane of angular displacement, as indicated by the right-hand rule – so that the angular velocity is seen as counter-clockwise from the head of the vector. Conversely, the $\mathbf {L}$ vector defines the plane in which $\mathbf {r}$ and $\mathbf {p}$ lie.

By defining a unit vector $\mathbf {\hat {u}}$ perpendicular to the plane of angular displacement, a scalar angular speed $\omega$ results, where $\omega \mathbf {\hat {u}} ={\boldsymbol {\omega }},$ and $\omega ={\frac {v_{\perp }}{r}},$ where $v_{\perp }$ is the perpendicular component of the motion, as above.

The two-dimensional scalar equations of the previous section can thus be given direction: ${\begin{aligned}\mathbf {L} &=I{\boldsymbol {\omega }}\\&=I\omega \mathbf {\hat {u}} \\&=\left(r^{2}m\right)\omega \mathbf {\hat {u}} \\&=rmv_{\perp }\mathbf {\hat {u}} \\&=r_{\perp }mv\mathbf {\hat {u}} ,\end{aligned}}$ and $\mathbf {L} =rmv\mathbf {\hat {u}}$ for circular motion, where all of the motion is perpendicular to the radius r .

In the spherical coordinate system the angular momentum vector expresses as

$\mathbf {L} =m\mathbf {r} \times \mathbf {v} =mr^{2}\left({\dot {\theta }}\,{\hat {\boldsymbol {\varphi }}}-{\dot {\varphi }}\sin \theta \,\mathbf {\hat {\boldsymbol {\theta }}} \right).$


## Analogy to linear momentum

Angular momentum can be described as the rotational analog of linear momentum. Like linear momentum it involves elements of mass and displacement. Unlike linear momentum it also involves elements of position and shape.

Many problems in physics involve matter in motion about some certain point in space, be it in actual rotation about it, or simply moving past it, where it is desired to know what effect the moving matter has on the point—can it exert energy upon it or perform work about it? Energy, the ability to do work, can be stored in matter by setting it in motion—a combination of its inertia and its displacement. Inertia is measured by its mass, and displacement by its velocity. Their product, ${\begin{aligned}({\text{amount of inertia}})\times ({\text{amount of displacement}})&={\text{amount of (inertia⋅displacement)}}\\{\text{mass}}\times {\text{velocity}}&={\text{momentum}}\\m\times v&=p\\\end{aligned}}$ is the matter's momentum. Referring this momentum to a central point introduces a complication: the momentum is not applied to the point directly. For instance, a particle of matter at the outer edge of a wheel is, in effect, at the end of a lever of the same length as the wheel's radius, its momentum turning the lever about the center point. This imaginary lever is known as the *moment arm*. It has the effect of multiplying the momentum's effort in proportion to its length, an effect known as a *moment*. Hence, the particle's momentum referred to a particular point, ${\begin{aligned}({\text{moment arm}})\times ({\text{amount of inertia}})\times ({\text{amount of displacement}})&={\text{moment of (inertia⋅displacement)}}\\{\text{length}}\times {\text{mass}}\times {\text{velocity}}&={\text{moment of momentum}}\\r\times m\times v&=L\\\end{aligned}}$ is the *angular momentum*, sometimes called, as here, the *moment of momentum* of the particle versus that particular center point. The equation $L=rmv$ combines a moment (a mass m turning moment arm r ) with a linear (straight-line equivalent) speed v . Linear speed referred to the central point is simply the product of the distance r and the angular speed $\omega$ versus the point: $v=r\omega ,$ another moment. Hence, angular momentum contains a double moment: $L=rmr\omega .$ Simplifying slightly, $L=r^{2}m\omega ,$ the quantity $r^{2}m$ is the particle's moment of inertia, sometimes called the second moment of mass. It is a measure of rotational inertia.

The above analogy of the translational momentum and rotational momentum can be expressed in vector form:

- ${\textstyle \mathbf {p} =m\mathbf {v} }$ for linear motion
- $\mathbf {L} =I{\boldsymbol {\omega }}$ for rotation

The direction of momentum is related to the direction of the velocity for linear movement. The direction of angular momentum is related to the angular velocity of the rotation.

Because moment of inertia is a crucial part of the spin angular momentum, the latter necessarily includes all of the complications of the former, which is calculated by multiplying elementary bits of the mass by the squares of their distances from the center of rotation. Therefore, the total moment of inertia, and the angular momentum, is a complex function of the configuration of the matter about the center of rotation and the orientation of the rotation for the various bits.

For a rigid body, for instance a wheel or an asteroid, the orientation of rotation is simply the position of the rotation axis versus the matter of the body. It may or may not pass through the center of mass, or it may lie completely outside of the body. For the same body, angular momentum may take a different value for every possible axis about which rotation may take place. It reaches a minimum when the axis passes through the center of mass.

For a collection of objects revolving about a center, for instance all of the bodies of the Solar System, the orientations may be somewhat organized, as is the Solar System, with most of the bodies' axes lying close to the system's axis. Their orientations may also be completely random.

In brief, the more mass and the farther it is from the center of rotation (the longer the moment arm), the greater the moment of inertia, and therefore the greater the angular momentum for a given angular velocity. In many cases the moment of inertia, and hence the angular momentum, can be simplified by, $I=k^{2}m,$ where k is the radius of gyration, the distance from the axis at which the entire mass m may be considered as concentrated.

Similarly, for a point mass m the moment of inertia is defined as, $I=r^{2}m$ where r is the radius of the point mass from the center of rotation, and for any collection of particles $m_{i}$ as the sum, $\sum _{i}I_{i}=\sum _{i}r_{i}^{2}m_{i}.$

Angular momentum's dependence on position and shape is reflected in its units versus linear momentum: kg⋅m2/s or N⋅m⋅s for angular momentum versus kg⋅m/s or N⋅s for linear momentum. When calculating angular momentum as the product of the moment of inertia times the angular velocity, the angular velocity must be expressed in radians per second, where the radian assumes the dimensionless value of unity. (When performing dimensional analysis, it may be productive to use orientational analysis which treats radians as a base unit, but this is not done in the International system of units). The units of angular momentum can be interpreted as torque⋅time. An object with angular momentum of *L* N⋅m⋅s can be reduced to zero angular velocity by an angular impulse of *L* N⋅m⋅s.

The plane perpendicular to the axis of angular momentum and passing through the center of mass is sometimes called the *invariable plane*, because the direction of the axis remains fixed if only the interactions of the bodies within the system, free from outside influences, are considered. One such plane is the invariable plane of the Solar System.

### Angular momentum and torque

Newton's second law of motion can be expressed mathematically, $\mathbf {F} =m\mathbf {a} ,$ or force = mass × acceleration. The rotational equivalent for point particles may be derived as follows: $\mathbf {L} =I{\boldsymbol {\omega }}$ which means that the torque (i.e. the time derivative of the angular momentum) is ${\boldsymbol {\tau }}={\frac {dI}{dt}}{\boldsymbol {\omega }}+I{\frac {d{\boldsymbol {\omega }}}{dt}}.$

Because the moment of inertia is $mr^{2}$ , it follows that ${\frac {dI}{dt}}=2mr{\frac {dr}{dt}}=2rp_{||}$ , and ${\frac {d\mathbf {L} }{dt}}=I{\frac {d{\boldsymbol {\omega }}}{dt}}+2rp_{||}{\boldsymbol {\omega }},$ which, reduces to ${\boldsymbol {\tau }}=I{\boldsymbol {\alpha }}+2rp_{||}{\boldsymbol {\omega }}.$ This is the rotational analog of Newton's second law. Note that the torque is not necessarily proportional or parallel to the angular acceleration (as one might expect). The reason for this is that the moment of inertia of a particle can change with time, something that cannot occur for ordinary mass.


## Conservation of angular momentum

### General considerations

A rotational analog of Newton's third law of motion might be written, "In an isolated system, no torque can be exerted on any matter without the exertion on some other matter of an equal and opposite torque about the same axis." Hence, *angular momentum can be exchanged between objects in an isolated system, but total angular momentum before and after an exchange remains constant (is conserved)*.

Seen another way, a rotational analogue of Newton's first law of motion might be written, "A rigid body continues in a state of uniform rotation unless acted upon by an external influence." Thus *with no external influence to act upon it, the original angular momentum of the system remains constant*.

The conservation of angular momentum is used in analyzing *central force motion*. If the net force on some body is directed always toward some point, the *center*, then there is no torque on the body with respect to the center, as all of the force is directed along the radius vector, and none is perpendicular to the radius. Mathematically, torque ${\boldsymbol {\tau }}=\mathbf {r} \times \mathbf {F} =\mathbf {0} ,$ because in this case $\mathbf {r}$ and $\mathbf {F}$ are parallel vectors. Therefore, the angular momentum of the body about the center is constant. This is the case with gravitational attraction in the orbits of planets and satellites, where the gravitational force is always directed toward the primary body and orbiting bodies conserve angular momentum by exchanging distance and velocity as they move about the primary. Central force motion is also used in the analysis of the Bohr model of the atom.

For a planet, angular momentum is distributed between the spin of the planet and its revolution in its orbit, and these are often exchanged by various mechanisms. The conservation of angular momentum in the Earth–Moon system results in the transfer of angular momentum from Earth to Moon, due to tidal torque the Moon exerts on the Earth. This in turn results in the slowing down of the rotation rate of Earth, at about 65.7 nanoseconds per day, and in gradual increase of the radius of Moon's orbit, at about 3.82 centimeters per year.

The conservation of angular momentum explains the angular acceleration of an ice skater as they bring their arms and legs close to the vertical axis of rotation. By bringing part of the mass of their body closer to the axis, they decrease their body's moment of inertia. Because angular momentum is the product of moment of inertia and angular velocity, if the angular momentum remains constant (is conserved), then the angular velocity (rotational speed) of the skater must increase.

The same phenomenon results in extremely fast spin of compact stars (like white dwarfs, neutron stars and black holes) when they are formed out of much larger and slower rotating stars.

Conservation is not always a full explanation for the dynamics of a system but is a key constraint. For example, a spinning top is subject to gravitational torque making it lean over and change the angular momentum about the nutation axis, but neglecting friction at the point of spinning contact, it has a conserved angular momentum about its spinning axis, and another about its precession axis. Also, in any planetary system, the planets, star(s), comets, and asteroids can all move in numerous complicated ways, but only so that the angular momentum of the system is conserved.

Noether's theorem states that every conservation law is associated with a symmetry (invariant) of the underlying physics. The symmetry associated with conservation of angular momentum is rotational invariance. The fact that the physics of a system is unchanged if it is rotated by any angle about an axis implies that angular momentum is conserved.

### Relation to Newton's second law of motion

While angular momentum total conservation can be understood separately from Newton's laws of motion as stemming from Noether's theorem in systems symmetric under rotations, it can also be understood simply as an efficient method of calculation of results that can also be otherwise arrived at directly from Newton's second law, together with laws governing the forces of nature (such as Newton's third law, Maxwell's equations and Lorentz force). Indeed, given initial conditions of position and velocity for every point, and the forces at such a condition, one may use Newton's second law to calculate the second derivative of position, and solving for this gives full information on the development of the physical system with time. Note, however, that this is no longer true in quantum mechanics, due to the existence of particle spin, which is an angular momentum that cannot be described by the cumulative effect of point-like motions in space.

As an example, consider decreasing of the moment of inertia, e.g. when a figure skater is pulling in their hands, speeding up the circular motion. In terms of angular momentum conservation, we have, for angular momentum *L*, moment of inertia *I* and angular velocity *ω*: $0=dL=d(I\cdot \omega )=dI\cdot \omega +I\cdot d\omega$

Using this, we see that the change requires an energy of: $dE=d\left({\tfrac {1}{2}}I\cdot \omega ^{2}\right)={\tfrac {1}{2}}dI\cdot \omega ^{2}+I\cdot \omega \cdot d\omega =-{\tfrac {1}{2}}dI\cdot \omega ^{2}$ so that a decrease in the moment of inertia requires investing energy.

This can be compared to the work done as calculated using Newton's laws. Each point in the rotating body is accelerating, at each point of time, with radial acceleration of: $-r\cdot \omega ^{2}$

Let us observe a point of mass *m*, whose position vector relative to the center of motion is perpendicular to the z-axis at a given point of time, and is at a distance *z*. The centripetal force on this point, keeping the circular motion, is: $-m\cdot z\cdot \omega ^{2}$

Thus the work required for moving this point to a distance *dz* farther from the center of motion is: $dW=-m\cdot z\cdot \omega ^{2}\cdot dz=-m\cdot \omega ^{2}\cdot d\left({\tfrac {1}{2}}z^{2}\right)$

For a non-pointlike body one must integrate over this, with *m* replaced by the mass density per unit *z*. This gives: $dW=-{\tfrac {1}{2}}dI\cdot \omega ^{2}$ which is exactly the energy required for keeping the angular momentum conserved.

Note, that the above calculation can also be performed per mass, using kinematics only. Thus the phenomena of figure skater accelerating tangential velocity while pulling their hands in, can be understood as follows in layman's language: The skater's palms are not moving in a straight line, so they are constantly accelerating inwards, but do not gain additional speed because the accelerating is always done when their motion inwards is zero. However, this is different when pulling the palms closer to the body: The acceleration due to rotation now increases the speed; but because of the rotation, the increase in speed does not translate to a significant speed inwards, but to an increase of the rotation speed.

### Stationary-action principle

In classical mechanics it can be shown that the rotational invariance of action functionals implies conservation of angular momentum. The action is defined in classical physics as a functional of positions, $x_{i}(t)$ often represented by the use of square brackets, and the final and initial times. It assumes the following form in cartesian coordinates: $S\left([x_{i}];t_{1},t_{2}\right)\equiv \int _{t_{1}}^{t_{2}}dt\left({\frac {1}{2}}m{\frac {dx_{i}}{dt}}\ {\frac {dx_{i}}{dt}}-V(x_{i})\right)$ where the repeated indices indicate summation over the index. If the action is invariant of an infinitesimal transformation, it can be mathematically stated as: ${\textstyle \delta S=S\left([x_{i}+\delta x_{i}];t_{1},t_{2}\right)-S\left([x_{i}];t_{1},t_{2}\right)=0}$ .

Under the transformation, $x_{i}\rightarrow x_{i}+\delta x_{i}$ , the action becomes: $S\left([x_{i}+\delta x_{i}];t_{1},t_{2}\right)=\!\int _{t_{1}}^{t_{2}}dt\left({\frac {1}{2}}m{\frac {d(x_{i}+\delta x_{i})}{dt}}{\frac {d(x_{i}+\delta x_{i})}{dt}}-V(x_{i}+\delta x_{i})\right)$ where we can employ the expansion of the terms up-to first order in ${\textstyle \delta x_{i}}$ : ${\begin{aligned}{\frac {d(x_{i}+\delta x_{i})}{dt}}{\frac {d(x_{i}+\delta x_{i})}{dt}}&\simeq {\frac {dx_{i}}{dt}}{\frac {dx_{i}}{dt}}-2{\frac {d^{2}x_{i}}{dt^{2}}}\delta x_{i}+2{\frac {d}{dt}}\left(\delta x_{i}{\frac {dx_{i}}{dt}}\right)\\V(x_{i}+\delta x_{i})&\simeq V(x_{i})+\delta x_{i}{\frac {\partial V}{\partial x_{i}}}\\\end{aligned}}$ giving the following change in action: $S[x_{i}+\delta x_{i}]\simeq S[x_{i}]+\int _{t_{1}}^{t_{2}}dt\,\delta x_{i}\left(-{\frac {\partial V}{\partial x_{i}}}-m{\frac {d^{2}x_{i}}{dt^{2}}}\right)+m\int _{t_{1}}^{t_{2}}dt{\frac {d}{dt}}\left(\delta x_{i}{\frac {dx_{i}}{dt}}\right).$

Since all rotations can be expressed as matrix exponential of skew-symmetric matrices, i.e. as $R({\hat {n}},\theta )=e^{M\theta }$ where M is a skew-symmetric matrix and $\theta$ is angle of rotation, we can express the change of coordinates due to the rotation $R({\hat {n}},\delta \theta )$ , up-to first order of infinitesimal angle of rotation, $\delta \theta$ as: $\delta x_{i}=M_{ij}x_{j}\delta \theta .$

Combining the equation of motion and **rotational invariance of action**, we get from the above equations that: $0=\delta S=\int _{t_{1}}^{t_{2}}dt{\frac {d}{dt}}\left(m{\frac {dx_{i}}{dt}}\delta x_{i}\right)=M_{ij}\,\delta \theta \,m\,x_{j}{\frac {dx_{i}}{dt}}{\Bigg \vert }_{t_{1}}^{t_{2}}$ Since this is true for any matrix $M_{ij}$ that satisfies $M_{ij}=-M_{ji},$ it results in the conservation of the following quantity: $\ell _{ij}(t):=m\left(x_{i}{\frac {dx_{j}}{dt}}-x_{j}{\frac {dx_{i}}{dt}}\right),$ as $\ell _{ij}(t_{1})=\ell _{ij}(t_{2})$ . This corresponds to the conservation of angular momentum throughout the motion.

### Lagrangian formalism

In Lagrangian mechanics, angular momentum for rotation around a given axis, is the conjugate momentum of the generalized coordinate of the angle around the same axis. For example, $L_{z}$ , the angular momentum around the z axis, is: $L_{z}={\frac {\partial {\cal {L}}}{\partial {\dot {\theta }}_{z}}}$ where ${\cal {L}}$ is the Lagrangian and $\theta _{z}$ is the angle around the z axis.

Note that ${\dot {\theta }}_{z}$ , the time derivative of the angle, is the angular velocity $\omega _{z}$ . Ordinarily, the Lagrangian depends on the angular velocity through the kinetic energy: The latter can be written by separating the velocity to its radial and tangential part, with the tangential part at the x-y plane, around the z-axis, being equal to: $\sum _{i}{\tfrac {1}{2}}m_{i}{v_{T}}_{i}^{2}=\sum _{i}{\tfrac {1}{2}}m_{i}\left(x_{i}^{2}+y_{i}^{2}\right){{\omega _{z}}_{i}}^{2}$ where the subscript i stands for the i-th body, and m , $v_{T}$ and $\omega _{z}$ stand for mass, tangential velocity around the z-axis and angular velocity around that axis, respectively.

For a body that is not point-like, with density *ρ*, we have instead: ${\frac {1}{2}}\int \rho (x,y,z)\left(x_{i}^{2}+y_{i}^{2}\right){{\omega _{z}}_{i}}^{2}\,dx\,dy={\frac {1}{2}}{I_{z}}_{i}{{\omega _{z}}_{i}}^{2}$ where integration runs over the area of the body, and *I*z is the moment of inertia around the z-axis.

Thus, assuming the potential energy does not depend on *ω**z* (this assumption may fail for electromagnetic systems), we have the angular momentum of the *i*th object: ${\begin{aligned}{L_{z}}_{i}&={\frac {\partial {\cal {L}}}{\partial {{\omega _{z}}_{i}}}}={\frac {\partial E_{k}}{\partial {{\omega _{z}}_{i}}}}\\&={I_{z}}_{i}\cdot {\omega _{z}}_{i}\end{aligned}}$

We have thus far rotated each object by a separate angle; we may also define an overall angle *θ*z by which we rotate the whole system, thus rotating also each object around the z-axis, and have the overall angular momentum: $L_{z}=\sum _{i}{I_{z}}_{i}\cdot {\omega _{z}}_{i}$

From Euler–Lagrange equations it then follows that: $0={\frac {\partial {\cal {L}}}{\partial {{\theta _{z}}_{i}}}}-{\frac {d}{dt}}\left({\frac {\partial {\cal {L}}}{\partial {{{\dot {\theta }}_{z}}_{i}}}}\right)={\frac {\partial {\cal {L}}}{\partial {{\theta _{z}}_{i}}}}-{\frac {d{L_{z}}_{i}}{dt}}$

Since the lagrangian is dependent upon the angles of the object only through the potential, we have: ${\frac {d{L_{z}}_{i}}{dt}}={\frac {\partial {\cal {L}}}{\partial {{\theta _{z}}_{i}}}}=-{\frac {\partial V}{\partial {{\theta _{z}}_{i}}}}$ which is the torque on the *i*th object.

Suppose the system is invariant to rotations, so that the potential is independent of an overall rotation by the angle *θ*z (thus it may depend on the angles of objects only through their differences, in the form $V({\theta _{z}}_{i},{\theta _{z}}_{j})=V({\theta _{z}}_{i}-{\theta _{z}}_{j})$ ). We therefore get for the total angular momentum: ${\frac {dL_{z}}{dt}}=-{\frac {\partial V}{\partial {\theta _{z}}}}=0$ And thus the angular momentum around the z-axis is conserved.

This analysis can be repeated separately for each axis, giving conservation of the angular momentum vector. However, the angles around the three axes cannot be treated simultaneously as generalized coordinates, since they are not independent; in particular, two angles per point suffice to determine its position. While it is true that in the case of a rigid body, fully describing it requires, in addition to three translational degrees of freedom, also specification of three rotational degrees of freedom; however these cannot be defined as rotations around the Cartesian axes (see Euler angles). This caveat is reflected in quantum mechanics in the non-trivial commutation relations of the different components of the angular momentum operator.

### Hamiltonian formalism

Equivalently, in Hamiltonian mechanics the Hamiltonian can be described as a function of the angular momentum. As before, the part of the kinetic energy related to rotation around the z-axis for the *i*th object is: ${\frac {1}{2}}{I_{z}}_{i}{{\omega _{z}}_{i}}^{2}={\frac {{{L_{z}}_{i}}^{2}}{2{I_{z}}_{i}}}$ which is analogous to the energy dependence upon momentum along the z-axis, ${\frac {{{p_{z}}_{i}}^{2}}{{2m}_{i}}}$ .

Hamilton's equations relate the angle around the z-axis to its conjugate momentum, the angular momentum around the same axis: ${\begin{aligned}{\frac {d{\theta _{z}}_{i}}{dt}}&={\frac {\partial {\mathcal {H}}}{\partial {L_{z}}_{i}}}={\frac {{L_{z}}_{i}}{{I_{z}}_{i}}}\\{\frac {d{L_{z}}_{i}}{dt}}&=-{\frac {\partial {\mathcal {H}}}{\partial {\theta _{z}}_{i}}}=-{\frac {\partial V}{\partial {\theta _{z}}_{i}}}\end{aligned}}$

The first equation gives ${L_{z}}_{i}={I_{z}}_{i}\cdot {{{\dot {\theta }}_{z}}_{i}}={I_{z}}_{i}\cdot {\omega _{z}}_{i}$

And so we get the same results as in the Lagrangian formalism.

Note, that for combining all axes together, we write the kinetic energy as: $E_{k}={\frac {1}{2}}\sum _{i}{\frac {|\mathbf {p} _{i}|^{2}}{2m_{i}}}=\sum _{i}\left({\frac {{p_{r}}_{i}^{2}}{2m_{i}}}+{\frac {1}{2}}{\mathbf {L} _{i}}^{\textsf {T}}{I_{i}}^{-1}\mathbf {L} _{i}\right)$ where *p*r is the momentum in the radial direction, and the moment of inertia is a 3-dimensional matrix; bold letters stand for 3-dimensional vectors.

For point-like bodies we have: $E_{k}=\sum _{i}\left({\frac {{p_{r}}_{i}^{2}}{2m_{i}}}+{\frac {|{\mathbf {L} _{i}}|^{2}}{2m_{i}{r_{i}}^{2}}}\right)$

This form of the kinetic energy part of the Hamiltonian is useful in analyzing central potential problems, and is easily transformed to a quantum mechanical work frame (e.g. in the hydrogen atom problem).


## Angular momentum in orbital mechanics

While in classical mechanics the language of angular momentum can be replaced by Newton's laws of motion, it is particularly useful for motion in central potential such as planetary motion in the solar system. Thus, the orbit of a planet in the solar system is defined by its energy, angular momentum and angles of the orbit major axis relative to a coordinate frame.

In astrodynamics and celestial mechanics, a quantity closely related to angular momentum is defined as $\mathbf {h} =\mathbf {r} \times \mathbf {v} ,$ called *specific angular momentum*. Note that $\mathbf {L} =m\mathbf {h} .$ Mass is often unimportant in orbital mechanics calculations, because motion of a body is determined by gravity. The primary body of the system is often so much larger than any bodies in motion about it that the gravitational effect of the smaller bodies on it can be neglected; it maintains, in effect, constant velocity. The motion of all bodies is affected by its gravity in the same way, regardless of mass, and therefore all move approximately the same way under the same conditions.


## Solid bodies

Angular momentum is also an extremely useful concept for describing rotating rigid bodies such as a gyroscope or a rocky planet. For a continuous mass distribution with density function *ρ*(**r**), a differential volume element *dV* with position vector **r** within the mass has a mass element *dm* = *ρ*(**r**)*dV*. Therefore, the infinitesimal angular momentum of this element is: $d\mathbf {L} =\mathbf {r} \times dm\mathbf {v} =\mathbf {r} \times \rho (\mathbf {r} )dV\mathbf {v} =dV\mathbf {r} \times \rho (\mathbf {r} )\mathbf {v}$ and integrating this differential over the volume of the entire mass gives its total angular momentum: $\mathbf {L} =\int _{V}dV\mathbf {r} \times \rho (\mathbf {r} )\mathbf {v}$

In the derivation which follows, integrals similar to this can replace the sums for the case of continuous mass.

### Collection of particles

For a collection of particles in motion about an arbitrary origin, it is informative to develop the equation of angular momentum by resolving their motion into components about their own center of mass and about the origin. Given,

- $m_{i}$ is the mass of particle i ,
- $\mathbf {R} _{i}$ is the position vector of particle i w.r.t. the origin,
- $\mathbf {V} _{i}$ is the velocity of particle i w.r.t. the origin,
- $\mathbf {R}$ is the position vector of the center of mass w.r.t. the origin,
- $\mathbf {V}$ is the velocity of the center of mass w.r.t. the origin,
- $\mathbf {r} _{i}$ is the position vector of particle i w.r.t. the center of mass,
- $\mathbf {v} _{i}$ is the velocity of particle i w.r.t. the center of mass,

The total mass of the particles is simply their sum, $M=\sum _{i}m_{i}.$

The position vector of the center of mass is defined by, $M\mathbf {R} =\sum _{i}m_{i}\mathbf {R} _{i}.$

By inspection,

$\mathbf {R} _{i}=\mathbf {R} +\mathbf {r} _{i}$

and

$\mathbf {V} _{i}=\mathbf {V} +\mathbf {v} _{i}.$

The total angular momentum of the collection of particles is the sum of the angular momentum of each particle,

$\mathbf {L} =\sum _{i}\left(\mathbf {R} _{i}\times m_{i}\mathbf {V} _{i}\right)$     (1)

Expanding $\mathbf {R} _{i}$ ,

${\begin{aligned}\mathbf {L} &=\sum _{i}\left[\left(\mathbf {R} +\mathbf {r} _{i}\right)\times m_{i}\mathbf {V} _{i}\right]\\&=\sum _{i}\left[\mathbf {R} \times m_{i}\mathbf {V} _{i}+\mathbf {r} _{i}\times m_{i}\mathbf {V} _{i}\right]\end{aligned}}$

Expanding $\mathbf {V} _{i}$ ,

${\begin{aligned}\mathbf {L} &=\sum _{i}\left[\mathbf {R} \times m_{i}\left(\mathbf {V} +\mathbf {v} _{i}\right)+\mathbf {r} _{i}\times m_{i}(\mathbf {V} +\mathbf {v} _{i})\right]\\&=\sum _{i}\left[\mathbf {R} \times m_{i}\mathbf {V} +\mathbf {R} \times m_{i}\mathbf {v} _{i}+\mathbf {r} _{i}\times m_{i}\mathbf {V} +\mathbf {r} _{i}\times m_{i}\mathbf {v} _{i}\right]\\&=\sum _{i}\mathbf {R} \times m_{i}\mathbf {V} +\sum _{i}\mathbf {R} \times m_{i}\mathbf {v} _{i}+\sum _{i}\mathbf {r} _{i}\times m_{i}\mathbf {V} +\sum _{i}\mathbf {r} _{i}\times m_{i}\mathbf {v} _{i}\end{aligned}}$

It can be shown that (see sidebar),

| **Prove that** $\sum _{i}m_{i}\mathbf {r} _{i}=\mathbf {0}$ ${\begin{aligned}\mathbf {r} _{i}&=\mathbf {R} _{i}-\mathbf {R} \\m_{i}\mathbf {r} _{i}&=m_{i}\left(\mathbf {R} _{i}-\mathbf {R} \right)\\\sum _{i}m_{i}\mathbf {r} _{i}&=\sum _{i}m_{i}\left(\mathbf {R} _{i}-\mathbf {R} \right)\\&=\sum _{i}(m_{i}\mathbf {R} _{i}-m_{i}\mathbf {R} )\\&=\sum _{i}m_{i}\mathbf {R} _{i}-\sum _{i}m_{i}\mathbf {R} \\&=\sum _{i}m_{i}\mathbf {R} _{i}-\left(\sum _{i}m_{i}\right)\mathbf {R} \\&=\sum _{i}m_{i}\mathbf {R} _{i}-M\mathbf {R} \end{aligned}}$ which, by the definition of the center of mass, is $\mathbf {0} ,$ and similarly for ${\textstyle \sum _{i}m_{i}\mathbf {v} _{i}.}$ |
|---|

$\sum _{i}m_{i}\mathbf {r} _{i}=\mathbf {0}$

and

$\sum _{i}m_{i}\mathbf {v} _{i}=\mathbf {0} ,$

therefore the second and third terms vanish,

$\mathbf {L} =\sum _{i}\mathbf {R} \times m_{i}\mathbf {V} +\sum _{i}\mathbf {r} _{i}\times m_{i}\mathbf {v} _{i}.$

The first term can be rearranged,

$\sum _{i}\mathbf {R} \times m_{i}\mathbf {V} =\mathbf {R} \times \sum _{i}m_{i}\mathbf {V} =\mathbf {R} \times M\mathbf {V} ,$

and total angular momentum for the collection of particles is finally,

$\mathbf {L} =\mathbf {R} \times M\mathbf {V} +\sum _{i}\mathbf {r} _{i}\times m_{i}\mathbf {v} _{i}$     (2)

The first term is the angular momentum of the center of mass relative to the origin. Similar to *§ Single particle*, below, it is the angular momentum of one particle of mass *M* at the center of mass moving with velocity **V**. The second term is the angular momentum of the particles moving relative to the center of mass, similar to *§ Fixed center of mass*, below. The result is general—the motion of the particles is not restricted to rotation or revolution about the origin or center of mass. The particles need not be individual masses, but can be elements of a continuous distribution, such as a solid body.

Rearranging equation (**2**) by vector identities, multiplying both terms by "one", and grouping appropriately, ${\begin{aligned}\mathbf {L} &=M(\mathbf {R} \times \mathbf {V} )+\sum _{i}\left[m_{i}\left(\mathbf {r} _{i}\times \mathbf {v} _{i}\right)\right],\\&={\frac {R^{2}}{R^{2}}}M\left(\mathbf {R} \times \mathbf {V} \right)+\sum _{i}\left[{\frac {r_{i}^{2}}{r_{i}^{2}}}m_{i}\left(\mathbf {r} _{i}\times \mathbf {v} _{i}\right)\right],\\&=R^{2}M\left({\frac {\mathbf {R} \times \mathbf {V} }{R^{2}}}\right)+\sum _{i}\left[r_{i}^{2}m_{i}\left({\frac {\mathbf {r} _{i}\times \mathbf {v} _{i}}{r_{i}^{2}}}\right)\right],\\\end{aligned}}$ gives the total angular momentum of the system of particles in terms of moment of inertia I and angular velocity ${\boldsymbol {\omega }}$ ,

$\mathbf {L} =I_{R}{\boldsymbol {\omega }}_{R}+\sum _{i}I_{i}{\boldsymbol {\omega }}_{i}.$     (3)

#### Single particle case

In the case of a single particle moving about the arbitrary origin, ${\begin{aligned}\mathbf {r} _{i}&=\mathbf {v} _{i}=\mathbf {0} ,\\\mathbf {r} &=\mathbf {R} ,\\\mathbf {v} &=\mathbf {V} ,\\m&=M,\end{aligned}}$ $\sum _{i}\mathbf {r} _{i}\times m_{i}\mathbf {v} _{i}=\mathbf {0} ,$ $\sum _{i}I_{i}{\boldsymbol {\omega }}_{i}=\mathbf {0} ,$ and equations (**2**) and (**3**) for total angular momentum reduce to, $\mathbf {L} =\mathbf {R} \times m\mathbf {V} =I_{R}{\boldsymbol {\omega }}_{R}.$

#### Case of a fixed center of mass

For the case of the center of mass fixed in space with respect to the origin, $\mathbf {V} =\mathbf {0} ,$ $\mathbf {R} \times M\mathbf {V} =\mathbf {0} ,$ $I_{R}{\boldsymbol {\omega }}_{R}=\mathbf {0} ,$ and equations (**2**) and (**3**) for total angular momentum reduce to, $\mathbf {L} =\sum _{i}\mathbf {r} _{i}\times m_{i}\mathbf {v} _{i}=\sum _{i}I_{i}{\boldsymbol {\omega }}_{i}.$


## Angular momentum in general relativity

In modern (20th century) theoretical physics, angular momentum (not including any intrinsic angular momentum – see below) is described using a different formalism, instead of a classical pseudovector. In this formalism, angular momentum is the 2-form Noether charge associated with rotational invariance. As a result, angular momentum is generally not conserved locally for general curved spacetimes, unless they have rotational symmetry; whereas globally the notion of angular momentum itself only makes sense if the spacetime is asymptotically flat. If the spacetime is only axially symmetric like for the Kerr metric, the total angular momentum is not conserved but $p_{\phi }$ is conserved which is related to the invariance of rotating around the symmetry-axis, where note that $p_{\phi }=g_{\phi \mu }p^{\mu }=mg_{\mu \phi }dX^{\mu }/d\tau$ where $g_{\mu \nu }$ is the metric, $m={\sqrt {|p_{\mu }p^{\mu }|}}$ is the rest mass, $dX^{\mu }/d\tau$ is the four-velocity, and $X^{\mu }=(t,r,\theta ,\phi )$ is the four-position in spherical coordinates.

In classical mechanics, the angular momentum of a particle can be reinterpreted as a plane element: $\mathbf {L} =\mathbf {r} \wedge \mathbf {p} \,,$ in which the exterior product (∧) replaces the cross product (×) (these products have similar characteristics but are nonequivalent). This has the advantage of a clearer geometric interpretation as a plane element, defined using the vectors **x** and **p**, and the expression is true in any number of dimensions. In Cartesian coordinates: ${\begin{aligned}\mathbf {L} &=\left(xp_{y}-yp_{x}\right)\mathbf {e} _{x}\wedge \mathbf {e} _{y}+\left(yp_{z}-zp_{y}\right)\mathbf {e} _{y}\wedge \mathbf {e} _{z}+\left(zp_{x}-xp_{z}\right)\mathbf {e} _{z}\wedge \mathbf {e} _{x}\\&=L_{xy}\mathbf {e} _{x}\wedge \mathbf {e} _{y}+L_{yz}\mathbf {e} _{y}\wedge \mathbf {e} _{z}+L_{zx}\mathbf {e} _{z}\wedge \mathbf {e} _{x}\,,\end{aligned}}$ or more compactly in index notation: $L_{ij}=x_{i}p_{j}-x_{j}p_{i}\,.$

The angular velocity can also be defined as an anti-symmetric second order tensor, with components *ωij*. The relation between the two anti-symmetric tensors is given by the moment of inertia which must now be a fourth order tensor: $L_{ij}=I_{ijk\ell }\omega _{k\ell }\,.$

Again, this equation in **L** and ***ω*** as tensors is true in any number of dimensions. This equation also appears in the geometric algebra formalism, in which **L** and ***ω*** are bivectors, and the moment of inertia is a mapping between them.

In relativistic mechanics, the relativistic angular momentum of a particle is expressed as an anti-symmetric tensor of second order: $M_{\alpha \beta }=X_{\alpha }P_{\beta }-X_{\beta }P_{\alpha }$ in terms of four-vectors, namely the four-position *X* and the four-momentum *P*, and absorbs the above **L** together with the moment of mass, i.e., the product of the relativistic mass of the particle and its center of mass, which can be thought of as describing the motion of its center of mass, since mass–energy is conserved.

In each of the above cases, for a system of particles the total angular momentum is just the sum of the individual particle angular momenta, and the center of mass is for the system.
