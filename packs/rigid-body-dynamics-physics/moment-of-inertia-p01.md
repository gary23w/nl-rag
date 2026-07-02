---
title: "Moment of inertia (part 1/2)"
source: https://en.wikipedia.org/wiki/Moment_of_inertia
domain: rigid-body-dynamics-physics
license: CC-BY-SA-4.0
tags: rigid body dynamics, moment of inertia, gyroscopic precession, rotational motion
fetched: 2026-07-02
part: 1/2
---

# Moment of inertia

To improve their maneuverability, combat aircraft are designed to minimize moments of inertia, while civil aircraft often are not.

The **moment of inertia** (also known as **mass moment of inertia**, **angular/rotational mass**, **second moment of mass**, or **rotational inertia**) is a measure of how difficult it is to change the rotation rate of a rigid body about a given axis. It is the ratio between the torque applied and the resulting angular acceleration about that axis. It plays the same role in rotational motion as mass does in linear motion. A body's moment of inertia about a particular axis depends on both the mass and its distribution relative to the axis, increasing with mass and distance from the axis.

For a point mass, the moment of inertia is simply the mass times the square of the perpendicular distance to the axis of rotation. The moment of inertia of a rigid composite system is the sum of the moments of inertia of its component subsystems (all taken about the same axis). Its simplest definition is the second moment of mass with respect to distance from an axis.

If a body is forced to rotate in a plane, then only the moment of inertia about an axis perpendicular to the plane, a scalar value, matters. If a body is allowed to rotate in all three dimensions, then its moment is described by a symmetric 3-by-3 matrix. This symmetric matrix can be orthogonally diagonalized by a set of mutually perpendicular principal axes. Torques around these principal axes act independently of each other.


## Introduction

When a body is free to rotate around an axis, torque must be applied to change its angular momentum. The amount of torque needed to cause any given angular acceleration (the rate of change in angular velocity) is proportional to the moment of inertia of the body. Moments of inertia may be expressed in units of kilogram metre squared (kg·m2) in SI units and pound-foot-squared (lb·ft2) in imperial or US units.

The moment of inertia plays the role in rotational kinetics that mass (inertia) plays in linear kinetics—both characterize the resistance of a body to changes in its motion. The moment of inertia depends on how mass is distributed around an axis of rotation, and will vary depending on the chosen axis. For a point-like mass, the moment of inertia about some axis is given by $mr^{2}$ , where r is the distance of the point from the axis, and m is the mass. For an extended rigid body, the moment of inertia is just the sum of all the small pieces of mass multiplied by the square of their distances from the axis in rotation. For an extended body of a regular shape and uniform density, this summation sometimes produces a simple expression that depends on the dimensions, shape and total mass of the object.

In 1673, Christiaan Huygens introduced this parameter in his study of the oscillation of a body hanging from a pivot, known as a compound pendulum. The term *moment of inertia* ("momentum inertiae" in Latin) was introduced by Leonhard Euler in his book *Theoria motus corporum solidorum seu rigidorum* in 1765, and it is incorporated into Euler's second law.

The natural frequency of oscillation of a compound pendulum is obtained from the ratio of the torque imposed by gravity on the mass of the pendulum to the resistance to acceleration defined by the moment of inertia. Comparison of this natural frequency to that of a simple pendulum consisting of a single point of mass provides a mathematical formulation for moment of inertia of an extended body.

The moment of inertia also appears in momentum, kinetic energy, and in Newton's laws of motion for a rigid body as a physical parameter that combines its shape and mass. There is an interesting difference in the way moment of inertia appears in planar and spatial movement. Planar movement has a single scalar that defines the moment of inertia, while for spatial movement the same calculations yield a 3 × 3 matrix of moments of inertia, called the inertia matrix or inertia tensor.

The moment of inertia of a rotating flywheel is used in a machine to resist variations in applied torque to smooth its rotational output. The moment of inertia of an airplane about its longitudinal, horizontal and vertical axes determine how steering forces on the control surfaces of its wings, elevators and rudder(s) affect the plane's motions in roll, pitch and yaw.


## Definition

The **moment of inertia** is defined as the product of mass of section and the square of the distance between the reference axis and the centroid of the section. It is denoted with the symbol *I* or *J*.

The moment of inertia I is also defined as the ratio of the net angular momentum L of a system to its angular velocity ω around a principal axis, that is $I={\frac {L}{\omega }}.$

If the angular momentum of a system is constant, then as the moment of inertia gets smaller, the angular velocity must increase. This occurs when spinning figure skaters pull in their outstretched arms or divers curl their bodies into a tuck position during a dive, to spin faster.

If the shape of the body does not change, then its moment of inertia appears in Newton's law of motion as the ratio of an applied torque τ on a body to the angular acceleration α around a principal axis, that is $\tau =I\alpha .$

For a simple pendulum, this definition yields a formula for the moment of inertia I in terms of the mass m of the pendulum and its distance r from the pivot point as, $I=mr^{2}.$

Thus, the moment of inertia of the pendulum depends on both the mass m of a body and its geometry, or shape, as defined by the distance r to the axis of rotation.

This simple formula generalizes to define moment of inertia for an arbitrarily shaped body as the sum of all the elemental point masses *dm* each multiplied by the square of its perpendicular distance r to an axis k. An arbitrary object's moment of inertia thus depends on the spatial distribution of its mass.

In general, given an object of mass m, an effective radius k can be defined, dependent on a particular axis of rotation, with such a value that its moment of inertia around the axis is $I=mk^{2},$ where k is known as the radius of gyration around the axis.


## Examples

### Simple pendulum

Mathematically, the moment of inertia of a simple pendulum is the ratio of the torque due to gravity about the pivot of a pendulum to its angular acceleration about that pivot point. For a simple pendulum, this is found to be the product of the mass of the particle m with the square of its distance r to the pivot, that is $I=mr^{2}.$

This can be shown as follows:

The force of gravity on the mass of a simple pendulum generates a torque ${\boldsymbol {\tau }}=\mathbf {r} \times \mathbf {F}$ around the axis perpendicular to the plane of the pendulum movement. Here $\mathbf {r}$ is the distance vector from the torque axis to the pendulum center of mass, and $\mathbf {F}$ is the net force on the mass. Associated with this torque is an angular acceleration, ${\boldsymbol {\alpha }}$ , of the string and mass around this axis. Since the mass is constrained to a circle the tangential acceleration of the mass is $\mathbf {a} ={\boldsymbol {\alpha }}\times \mathbf {r}$ . Since $\mathbf {F} =m\mathbf {a}$ the torque equation becomes: ${\begin{aligned}{\boldsymbol {\tau }}&=\mathbf {r} \times \mathbf {F} =\mathbf {r} \times (m{\boldsymbol {\alpha }}\times \mathbf {r} )\\&=m\left(\left(\mathbf {r} \cdot \mathbf {r} \right){\boldsymbol {\alpha }}-\left(\mathbf {r} \cdot {\boldsymbol {\alpha }}\right)\mathbf {r} \right)\\&=mr^{2}{\boldsymbol {\alpha }}=I\alpha \mathbf {\hat {k}} ,\end{aligned}}$ where $\mathbf {\hat {k}}$ is a unit vector perpendicular to the plane of the pendulum. (The second to last step uses the vector triple product expansion with the perpendicularity of ${\boldsymbol {\alpha }}$ and $\mathbf {r}$ .) The quantity $I=mr^{2}$ is the *moment of inertia* of this single mass around the pivot point.

The quantity $I=mr^{2}$ also appears in the angular momentum of a simple pendulum, which is calculated from the velocity $\mathbf {v} ={\boldsymbol {\omega }}\times \mathbf {r}$ of the pendulum mass around the pivot, where ${\boldsymbol {\omega }}$ is the angular velocity of the mass about the pivot point. This angular momentum is given by ${\begin{aligned}\mathbf {L} &=\mathbf {r} \times \mathbf {p} =\mathbf {r} \times \left(m{\boldsymbol {\omega }}\times \mathbf {r} \right)\\&=m\left(\left(\mathbf {r} \cdot \mathbf {r} \right){\boldsymbol {\omega }}-\left(\mathbf {r} \cdot {\boldsymbol {\omega }}\right)\mathbf {r} \right)\\&=mr^{2}{\boldsymbol {\omega }}=I\omega \mathbf {\hat {k}} ,\end{aligned}}$ using a similar derivation to the previous equation.

Similarly, the kinetic energy of the pendulum mass is defined by the velocity of the pendulum around the pivot to yield $E_{\text{K}}={\frac {1}{2}}m\mathbf {v} \cdot \mathbf {v} ={\frac {1}{2}}\left(mr^{2}\right)\omega ^{2}={\frac {1}{2}}I\omega ^{2}.$

This shows that the quantity $I=mr^{2}$ is how mass combines with the shape of a body to define rotational inertia. The moment of inertia of an arbitrarily shaped body is the sum of the values $mr^{2}$ for all of the elements of mass in the body.

### Compound pendulums

A compound pendulum is a body formed from an assembly of particles of continuous shape that rotates rigidly around a pivot. Its moment of inertia is the sum of the moments of inertia of each of the particles that it is composed of. The natural frequency ( $\omega _{\text{n}}$ ) of a compound pendulum depends on its moment of inertia, $I_{P}$ , $\omega _{\text{n}}={\sqrt {\frac {mgr}{I_{P}}}},$ where m is the mass of the object, g is local acceleration of gravity, and r is the distance from the pivot point to the center of mass of the object. Measuring this frequency of oscillation over small angular displacements provides an effective way of measuring moment of inertia of a body.

Thus, to determine the moment of inertia of the body, simply suspend it from a convenient pivot point P so that it swings freely in a plane perpendicular to the direction of the desired moment of inertia, then measure its natural frequency or period of oscillation ( t ), to obtain $I_{P}={\frac {mgr}{\omega _{\text{n}}^{2}}}={\frac {mgrt^{2}}{4\pi ^{2}}},$ where t is the period (duration) of oscillation (usually averaged over multiple periods).

#### Center of oscillation

A simple pendulum that has the same natural frequency as a compound pendulum defines the length L from the pivot to a point called the center of oscillation of the compound pendulum. This point also corresponds to the center of percussion. The length L is determined from the formula, ${\begin{aligned}\omega _{\text{n}}&={\sqrt {\frac {g}{L}}}&&={\sqrt {\frac {mgr}{I_{P}}}}\\L&={\frac {g}{\omega _{\text{n}}^{2}}}&&={\frac {I_{P}}{mr}}\end{aligned}}$

The seconds pendulum, which provides the "tick" and "tock" of a grandfather clock, takes one second to swing from side-to-side. This is a period of two seconds, or a natural frequency of $\pi \ \mathrm {rad/s}$ for the pendulum. In this case, the distance to the center of oscillation, L , can be computed to be $L={\frac {g}{\omega _{\text{n}}^{2}}}\approx {\frac {9.81\ \mathrm {m/s^{2}} }{(3.14\ \mathrm {rad/s} )^{2}}}\approx 0.99\ \mathrm {m} .$

Notice that the distance to the center of oscillation of the seconds pendulum must be adjusted to accommodate different values for the local acceleration of gravity. Kater's pendulum is a compound pendulum that uses this property to measure the local acceleration of gravity, and is called a gravimeter.


## Measuring moment of inertia

The moment of inertia of a complex system such as a vehicle or airplane around its vertical axis can be measured by suspending the system from three points to form a trifilar pendulum. A trifilar pendulum is a platform supported by three wires designed to oscillate in torsion around its vertical centroidal axis. The period of oscillation of the trifilar pendulum yields the moment of inertia of the system.


## Moment of inertia of area

Moment of inertia of area is also known as the second moment of area and its physical meaning is completely different from the mass moment of inertia.

These calculations are commonly used in civil engineering for structural design of beams and columns. Cross-sectional areas calculated for vertical moment of the x-axis $I_{xx}$ and horizontal moment of the y-axis $I_{yy}$ .

Height (*h*) and breadth (*b*) are the linear measures, except for circles, which are effectively half-breadth derived, r

Sectional areas moment formulae:

1. Square: $I_{xx}=I_{yy}={\frac {b^{4}}{12}}$
2. Rectangular: $I_{xx}={\frac {bh^{3}}{12}}$ and; $I_{yy}={\frac {hb^{3}}{12}}$
3. Triangular: $I_{xx}={\frac {bh^{3}}{36}}$
4. Circular: $I_{xx}=I_{yy}={\frac {1}{4}}{\pi }r^{4}={\frac {1}{64}}{\pi }d^{4}$


## Motion in a fixed plane

### Point mass

The moment of inertia about an axis of a body is calculated by summing $mr^{2}$ for every particle in the body, where r is the perpendicular distance to the specified axis. To see how moment of inertia arises in the study of the movement of an extended body, it is convenient to consider a rigid assembly of point masses. (This equation can be used for axes that are not principal axes provided that it is understood that this does not fully describe the moment of inertia.)

Consider the kinetic energy of an assembly of N masses $m_{i}$ that lie at the distances $r_{i}$ from the pivot point P , which is the nearest point on the axis of rotation. It is the sum of the kinetic energy of the individual masses, $E_{\text{K}}=\sum _{i=1}^{N}{\frac {1}{2}}\,m_{i}\mathbf {v} _{i}\cdot \mathbf {v} _{i}=\sum _{i=1}^{N}{\frac {1}{2}}\,m_{i}\left(\omega r_{i}\right)^{2}={\frac {1}{2}}\,\omega ^{2}\sum _{i=1}^{N}m_{i}r_{i}^{2}.$

This shows that the moment of inertia of the body is the sum of each of the $mr^{2}$ terms, that is $I_{P}=\sum _{i=1}^{N}m_{i}r_{i}^{2}.$

Thus, moment of inertia is a physical property that combines the mass and distribution of the particles around the rotation axis. Notice that rotation about different axes of the same body yield different moments of inertia.

The moment of inertia of a continuous body rotating about a specified axis is calculated in the same way, except with infinitely many point particles. Thus the limits of summation are removed, and the sum is written as follows: $I_{P}=\sum _{i}m_{i}r_{i}^{2}$

Another expression replaces the summation with an integral, $I_{P}=\iiint _{Q}\rho (x,y,z)\left\|\mathbf {r} \right\|^{2}dV$

Here, the function $\rho$ gives the mass density at each point $(x,y,z)$ , $\mathbf {r}$ is a vector perpendicular to the axis of rotation and extending from a point on the rotation axis to a point $(x,y,z)$ in the solid, and the integration is evaluated over the volume V of the body Q . The moment of inertia of a flat surface is similar with the mass density being replaced by its areal mass density with the integral evaluated over its area.

**Note on second moment of area**: The moment of inertia of a body moving in a plane and the second moment of area of a beam's cross-section are often confused. The moment of inertia of a body with the shape of the cross-section is the second moment of this area about the z -axis perpendicular to the cross-section, weighted by its density. This is also called the *polar moment of the area*, and is the sum of the second moments about the x - and y -axes. The stresses in a beam are calculated using the second moment of the cross-sectional area around either the x -axis or y -axis depending on the load.

#### Examples

The moment of inertia of a **compound pendulum** constructed from a thin disc mounted at the end of a thin rod that oscillates around a pivot at the other end of the rod, begins with the calculation of the moment of inertia of the thin rod and thin disc about their respective centers of mass.

- The moment of inertia of a **thin rod** with constant cross-section s and density $\rho$ and with length $\ell$ about a perpendicular axis through its center of mass is determined by integration. Align the x -axis with the rod and locate the origin at its center of mass at the center of the rod, then $I_{C,{\text{rod}}}=\iiint _{Q}\rho \,x^{2}\,dV=\int _{-{\frac {\ell }{2}}}^{\frac {\ell }{2}}\rho \,x^{2}s\,dx=\left.\rho s{\frac {x^{3}}{3}}\right|_{-{\frac {\ell }{2}}}^{\frac {\ell }{2}}={\frac {\rho s}{3}}\left({\frac {\ell ^{3}}{8}}+{\frac {\ell ^{3}}{8}}\right)={\frac {m\ell ^{2}}{12}},$ where $m=\rho s\ell$ is the mass of the rod.
- The moment of inertia of a **thin disc** of constant thickness s , radius R , and density $\rho$ about an axis through its center and perpendicular to its face (parallel to its axis of rotational symmetry) is determined by integration. Align the z -axis with the axis of the disc and define a volume element as $dV=sr\,dr\,d\theta$ , then $I_{C,{\text{disc}}}=\iiint _{Q}\rho \,r^{2}\,dV=\int _{0}^{2\pi }\int _{0}^{R}\rho r^{2}sr\,dr\,d\theta =\pi \rho s{\frac {R^{4}}{2}}={\frac {1}{2}}mR^{2},$ where $m=\pi R^{2}\rho s$ is its mass.
- The moment of inertia of the compound pendulum is now obtained by adding the moment of inertia of the rod and the disc around the pivot point P as, $I_{P}=I_{C,{\text{rod}}}+M_{\text{rod}}\left({\frac {L}{2}}\right)^{2}+I_{C,{\text{disc}}}+M_{\text{disc}}(L+R)^{2},$ where L is the length of the pendulum. Notice that the parallel axis theorem is used to shift the moment of inertia from the center of mass to the pivot point of the pendulum.

A list of moments of inertia formulas for standard body shapes provides a way to obtain the moment of inertia of a complex body as an assembly of simpler shaped bodies. The parallel axis theorem is used to shift the reference point of the individual bodies to the reference point of the assembly.

As one more example, consider the moment of inertia of a solid sphere of constant density about an axis through its center of mass. This is determined by summing the moments of inertia of the thin discs that can form the sphere whose centers are along the axis chosen for consideration. If the surface of the sphere is defined by the equation $x^{2}+y^{2}+z^{2}=R^{2},$

then the square of the radius r of the disc at the cross-section z along the z -axis is $r(z)^{2}=x^{2}+y^{2}=R^{2}-z^{2}.$

Therefore, the moment of inertia of the sphere is the sum of the moments of inertia of the discs along the z -axis, ${\begin{aligned}I_{C,{\text{sphere}}}&=\int _{-R}^{R}{\tfrac {1}{2}}\pi \rho r(z)^{4}\,dz=\int _{-R}^{R}{\tfrac {1}{2}}\pi \rho \left(R^{2}-z^{2}\right)^{2}\,dz\\[1ex]&={\tfrac {1}{2}}\pi \rho \left[R^{4}z-{\tfrac {2}{3}}R^{2}z^{3}+{\tfrac {1}{5}}z^{5}\right]_{-R}^{R}\\[1ex]&=\pi \rho \left(1-{\tfrac {2}{3}}+{\tfrac {1}{5}}\right)R^{5}\\[1ex]&={\tfrac {2}{5}}mR^{2},\end{aligned}}$ where ${\textstyle m={\frac {4}{3}}\pi R^{3}\rho }$ is the mass of the sphere.

### Rigid body

If a mechanical system is constrained to move parallel to a fixed plane, then the rotation of a body in the system occurs around an axis $\mathbf {\hat {k}}$ perpendicular to this plane. In this case, the moment of inertia of the mass in this system is a scalar known as the *polar moment of inertia*. The definition of the polar moment of inertia can be obtained by considering momentum, kinetic energy and Newton's laws for the planar movement of a rigid system of particles.

If a system of n particles, $P_{i},i=1,\dots ,n$ , are assembled into a rigid body, then the momentum of the system can be written in terms of positions relative to a reference point $\mathbf {R}$ , and absolute velocities $\mathbf {v} _{i}$ : ${\begin{aligned}\Delta \mathbf {r} _{i}&=\mathbf {r} _{i}-\mathbf {R} ,\\\mathbf {v} _{i}&={\boldsymbol {\omega }}\times \left(\mathbf {r} _{i}-\mathbf {R} \right)+\mathbf {V} ={\boldsymbol {\omega }}\times \Delta \mathbf {r} _{i}+\mathbf {V} ,\end{aligned}}$ where ${\boldsymbol {\omega }}$ is the angular velocity of the system and $\mathbf {V}$ is the velocity of $\mathbf {R}$ .

For planar movement the angular velocity vector is directed along the unit vector $\mathbf {k}$ which is perpendicular to the plane of movement. Introduce the unit vectors $\mathbf {e} _{i}$ from the reference point $\mathbf {R}$ to a point $\mathbf {r} _{i}$ , and the unit vector $\mathbf {\hat {t}} _{i}=\mathbf {\hat {k}} \times \mathbf {\hat {e}} _{i}$ , so ${\begin{aligned}\mathbf {\hat {e}} _{i}&={\frac {\Delta \mathbf {r} _{i}}{\Delta r_{i}}},\quad \mathbf {\hat {k}} ={\frac {\boldsymbol {\omega }}{\omega }},\quad \mathbf {\hat {t}} _{i}=\mathbf {\hat {k}} \times \mathbf {\hat {e}} _{i},\\\mathbf {v} _{i}&={\boldsymbol {\omega }}\times \Delta \mathbf {r} _{i}+\mathbf {V} =\omega \mathbf {\hat {k}} \times \Delta r_{i}\mathbf {\hat {e}} _{i}+\mathbf {V} =\omega \,\Delta r_{i}\mathbf {\hat {t}} _{i}+\mathbf {V} \end{aligned}}$

This defines the relative position vector and the velocity vector for the rigid system of the particles moving in a plane.

**Note on the cross product**: When a body moves parallel to a ground plane, the trajectories of all the points in the body lie in planes parallel to this ground plane. This means that any rotation that the body undergoes must be around an axis perpendicular to this plane. Planar movement is often presented as projected onto this ground plane so that the axis of rotation appears as a point. In this case, the angular velocity and angular acceleration of the body are scalars and the fact that they are vectors along the rotation axis is ignored. This is usually preferred for introductions to the topic. But in the case of moment of inertia, the combination of mass and geometry benefits from the geometric properties of the cross product. For this reason, in this section on planar movement the angular velocity and accelerations of the body are vectors perpendicular to the ground plane, and the cross product operations are the same as used for the study of spatial rigid body movement.

#### Angular momentum

The angular momentum vector for the planar movement of a rigid system of particles is given by ${\begin{aligned}\mathbf {L} &=\sum _{i=1}^{n}m_{i}\Delta \mathbf {r} _{i}\times \mathbf {v} _{i}\\&=\sum _{i=1}^{n}m_{i}\,\Delta r_{i}\mathbf {\hat {e}} _{i}\times \left(\omega \,\Delta r_{i}\mathbf {\hat {t}} _{i}+\mathbf {V} \right)\\&=\left(\sum _{i=1}^{n}m_{i}\,\Delta r_{i}^{2}\right)\omega \mathbf {\hat {k}} +\left(\sum _{i=1}^{n}m_{i}\,\Delta r_{i}\mathbf {\hat {e}} _{i}\right)\times \mathbf {V} .\end{aligned}}$

Use the center of mass $\mathbf {C}$ as the reference point so ${\begin{aligned}\Delta r_{i}\mathbf {\hat {e}} _{i}&=\mathbf {r} _{i}-\mathbf {C} ,\\\sum _{i=1}^{n}m_{i}\,\Delta r_{i}\mathbf {\hat {e}} _{i}&=0,\end{aligned}}$

and define the moment of inertia relative to the center of mass $I_{\mathbf {C} }$ as $I_{\mathbf {C} }=\sum _{i}m_{i}\,\Delta r_{i}^{2},$

then the equation for angular momentum simplifies to $\mathbf {L} =I_{\mathbf {C} }\omega \mathbf {\hat {k}} .$

The moment of inertia $I_{\mathbf {C} }$ about an axis perpendicular to the movement of the rigid system and through the center of mass is known as the *polar moment of inertia*. Specifically, it is the second moment of mass with respect to the orthogonal distance from an axis (or pole).

For a given amount of angular momentum, a decrease in the moment of inertia results in an increase in the angular velocity. Figure skaters can change their moment of inertia by pulling in their arms. Thus, the angular velocity achieved by a skater with outstretched arms results in a greater angular velocity when the arms are pulled in, because of the reduced moment of inertia. A figure skater is not, however, a rigid body.

#### Kinetic energy

The kinetic energy of a rigid system of particles moving in the plane is given by ${\begin{aligned}E_{\text{K}}&={\frac {1}{2}}\sum _{i=1}^{n}m_{i}\mathbf {v} _{i}\cdot \mathbf {v} _{i},\\&={\frac {1}{2}}\sum _{i=1}^{n}m_{i}\left(\omega \,\Delta r_{i}\mathbf {\hat {t}} _{i}+\mathbf {V} \right)\cdot \left(\omega \,\Delta r_{i}\mathbf {\hat {t}} _{i}+\mathbf {V} \right),\\&={\frac {1}{2}}\omega ^{2}\left(\sum _{i=1}^{n}m_{i}\,\Delta r_{i}^{2}\mathbf {\hat {t}} _{i}\cdot \mathbf {\hat {t}} _{i}\right)+\omega \mathbf {V} \cdot \left(\sum _{i=1}^{n}m_{i}\,\Delta r_{i}\mathbf {\hat {t}} _{i}\right)+{\frac {1}{2}}\left(\sum _{i=1}^{n}m_{i}\right)\mathbf {V} \cdot \mathbf {V} .\end{aligned}}$

Let the reference point be the center of mass $\mathbf {C}$ of the system so the second term becomes zero, and introduce the moment of inertia $I_{\mathbf {C} }$ so the kinetic energy is given by $E_{\text{K}}={\frac {1}{2}}I_{\mathbf {C} }\omega ^{2}+{\frac {1}{2}}M\mathbf {V} \cdot \mathbf {V} .$

The moment of inertia $I_{\mathbf {C} }$ is the *polar moment of inertia* of the body.

#### Newton's laws

Newton's laws for a rigid system of n particles, $P_{i},i=1,\dots ,n$ , can be written in terms of a resultant force and torque at a reference point $\mathbf {R}$ , to yield ${\begin{aligned}\mathbf {F} &=\sum _{i=1}^{n}m_{i}\mathbf {A} _{i},\\{\boldsymbol {\tau }}&=\sum _{i=1}^{n}\Delta \mathbf {r} _{i}\times m_{i}\mathbf {A} _{i},\end{aligned}}$ where $\mathbf {r} _{i}$ denotes the trajectory of each particle.

The kinematics of a rigid body yields the formula for the acceleration of the particle $P_{i}$ in terms of the position $\mathbf {R}$ and acceleration $\mathbf {A}$ of the reference particle as well as the angular velocity vector ${\boldsymbol {\omega }}$ and angular acceleration vector ${\boldsymbol {\alpha }}$ of the rigid system of particles as, $\mathbf {A} _{i}={\boldsymbol {\alpha }}\times \Delta \mathbf {r} _{i}+{\boldsymbol {\omega }}\times {\boldsymbol {\omega }}\times \Delta \mathbf {r} _{i}+\mathbf {A} .$

For systems that are constrained to planar movement, the angular velocity and angular acceleration vectors are directed along $\mathbf {\hat {k}}$ perpendicular to the plane of movement, which simplifies this acceleration equation. In this case, the acceleration vectors can be simplified by introducing the unit vectors $\mathbf {\hat {e}} _{i}$ from the reference point $\mathbf {R}$ to a point $\mathbf {r} _{i}$ and the unit vectors $\mathbf {\hat {t}} _{i}=\mathbf {\hat {k}} \times \mathbf {\hat {e}} _{i}$ , so ${\begin{aligned}\mathbf {A} _{i}&=\alpha \mathbf {\hat {k}} \times \Delta r_{i}\mathbf {\hat {e}} _{i}-\omega \mathbf {\hat {k}} \times \omega \mathbf {\hat {k}} \times \Delta r_{i}\mathbf {\hat {e}} _{i}+\mathbf {A} \\&=\alpha \Delta r_{i}\mathbf {\hat {t}} _{i}-\omega ^{2}\Delta r_{i}\mathbf {\hat {e}} _{i}+\mathbf {A} .\end{aligned}}$

This yields the resultant torque on the system as ${\begin{aligned}{\boldsymbol {\tau }}&=\sum _{i=1}^{n}m_{i}\,\Delta r_{i}\mathbf {\hat {e}} _{i}\times \left(\alpha \Delta r_{i}\mathbf {\hat {t}} _{i}-\omega ^{2}\Delta r_{i}\mathbf {\hat {e}} _{i}+\mathbf {A} \right)\\&=\left(\sum _{i=1}^{n}m_{i}\,\Delta r_{i}^{2}\right)\alpha \mathbf {\hat {k}} +\left(\sum _{i=1}^{n}m_{i}\,\Delta r_{i}\mathbf {\hat {e}} _{i}\right)\times \mathbf {A} ,\end{aligned}}$

where $\mathbf {\hat {e}} _{i}\times \mathbf {\hat {e}} _{i}=\mathbf {0}$ , and $\mathbf {\hat {e}} _{i}\times \mathbf {\hat {t}} _{i}=\mathbf {\hat {k}}$ is the unit vector perpendicular to the plane for all of the particles $P_{i}$ .

Use the center of mass $\mathbf {C}$ as the reference point and define the moment of inertia relative to the center of mass $I_{\mathbf {C} }$ , then the equation for the resultant torque simplifies to ${\boldsymbol {\tau }}=I_{\mathbf {C} }\alpha \mathbf {\hat {k}} .$
