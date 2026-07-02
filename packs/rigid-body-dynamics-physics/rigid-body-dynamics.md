---
title: "Rigid body dynamics"
source: https://en.wikipedia.org/wiki/Rigid_body_dynamics
domain: rigid-body-dynamics-physics
license: CC-BY-SA-4.0
tags: rigid body dynamics, moment of inertia, gyroscopic precession, rotational motion
fetched: 2026-07-02
---

# Rigid body dynamics

In classical mechanics, **rigid body dynamics** studies the movement of systems of interconnected bodies under the action of external forces. Along with statics, it forms the field of **rigid body mechanics**. The assumption that the bodies are *rigid* (i.e. they do not deform under the action of applied forces) simplifies analysis, by reducing the parameters that describe the configuration of the system to the translation and rotation of body-fixed frames. This excludes bodies that display fluid, highly elastic, and plastic behavior.

The dynamics of a rigid body system is described by the laws of kinematics and by the application of Newton's second law (kinetics) or their derivative form, Lagrangian mechanics. The solution of these equations of motion provides a description of the position, the motion and the acceleration of the individual components of the system, and overall the system itself, as a function of time. The formulation and solution of rigid body dynamics is an important tool in the computer simulation of mechanical systems.

## Planar rigid body dynamics

If a system of particles moves parallel to a fixed plane, the system is said to be constrained to planar movement. In this case, Newton's laws (kinetics) for a rigid system of N particles, P*i*, *i*=1,...,*N*, simplify because there is no movement in the *k* direction. Determine the resultant force and torque at a reference point **R**, to obtain $\mathbf {F} =\sum _{i=1}^{N}m_{i}\mathbf {A} _{i},\quad \mathbf {T} =\sum _{i=1}^{N}(\mathbf {r} _{i}-\mathbf {R} )\times m_{i}\mathbf {A} _{i},$

where **r**i denotes the planar trajectory of each particle.

The kinematics of a rigid body yields the formula for the acceleration of the particle Pi in terms of the position **R** and acceleration **A** of the reference particle as well as the angular velocity vector ***ω*** and angular acceleration vector ***α*** of the rigid system of particles as, $\mathbf {A} _{i}={\boldsymbol {\alpha }}\times (\mathbf {r} _{i}-\mathbf {R} )+{\boldsymbol {\omega }}\times ({\boldsymbol {\omega }}\times (\mathbf {r} _{i}-\mathbf {R} ))+\mathbf {A} .$

For systems that are constrained to planar movement, the angular velocity and angular acceleration vectors are directed along **k** perpendicular to the plane of movement, which simplifies this acceleration equation. In this case, the acceleration vectors can be simplified by introducing the unit vectors **e**i from the reference point **R** to a point **r**i and the unit vectors ${\textstyle \mathbf {t} _{i}=\mathbf {k} \times \mathbf {e} _{i}}$ , so $\mathbf {A} _{i}=\alpha (\Delta r_{i}\mathbf {t} _{i})-\omega ^{2}(\Delta r_{i}\mathbf {e} _{i})+\mathbf {A} .$

This yields the resultant force on the system as $\mathbf {F} =\alpha \sum _{i=1}^{N}m_{i}\left(\Delta r_{i}\mathbf {t} _{i}\right)-\omega ^{2}\sum _{i=1}^{N}m_{i}\left(\Delta r_{i}\mathbf {e} _{i}\right)+\left(\sum _{i=1}^{N}m_{i}\right)\mathbf {A} ,$ and torque as ${\begin{aligned}\mathbf {T} ={}&\sum _{i=1}^{N}(m_{i}\Delta r_{i}\mathbf {e} _{i})\times \left(\alpha (\Delta r_{i}\mathbf {t} _{i})-\omega ^{2}(\Delta r_{i}\mathbf {e} _{i})+\mathbf {A} \right)\\{}={}&\left(\sum _{i=1}^{N}m_{i}\Delta r_{i}^{2}\right)\alpha \mathbf {k} +\left(\sum _{i=1}^{N}m_{i}\Delta r_{i}\mathbf {e} _{i}\right)\times \mathbf {A} ,\end{aligned}}$

where ${\textstyle \mathbf {e} _{i}\times \mathbf {e} _{i}=0}$ and ${\textstyle \mathbf {e} _{i}\times \mathbf {t} _{i}=\mathbf {k} }$ is the unit vector perpendicular to the plane for all of the particles Pi.

Use the center of mass **C** as the reference point, so these equations for Newton's laws simplify to become $\mathbf {F} =M\mathbf {A} ,\quad \mathbf {T} =I_{\textbf {C}}\alpha \mathbf {k} ,$

where M is the total mass and *I***C** is the moment of inertia about an axis perpendicular to the movement of the rigid system and through the center of mass.

## Rigid body in three dimensions

### Orientation or attitude descriptions

Several methods to describe orientations of a rigid body in three dimensions have been developed. They are summarized in the following sections.

#### Euler angles

The first attempt to represent an orientation is attributed to Leonhard Euler. He imagined three reference frames that could rotate one around the other, and realized that by starting with a fixed reference frame and performing three rotations, he could get any other reference frame in the space (using two rotations to fix the vertical axis and another to fix the other two axes). The values of these three rotations are called Euler angles. Commonly, $\psi$ is used to denote precession, $\theta$ nutation, and $\phi$ intrinsic rotation.

- (Diagram of the Euler angles) Diagram of the Euler angles
- (Intrinsic rotation of a ball about a fixed axis) Intrinsic rotation of a ball about a fixed axis
- (Motion of a top in the Euler angles) Motion of a top in the Euler angles

#### Tait–Bryan angles

These are three angles, also known as yaw, pitch and roll, Navigation angles and Cardan angles. Mathematically they constitute a set of six possibilities inside the twelve possible sets of Euler angles, the ordering being the one best used for describing the orientation of a vehicle such as an airplane. In aerospace engineering they are usually referred to as Euler angles.

#### Orientation vector

Euler also realized that the composition of two rotations is equivalent to a single rotation about a different fixed axis (Euler's rotation theorem). Therefore, the composition of the former three angles has to be equal to only one rotation, whose axis was complicated to calculate until matrices were developed.

Based on this fact he introduced a vectorial way to describe any rotation, with a vector on the rotation axis and module equal to the value of the angle. Therefore, any orientation can be represented by a rotation vector (also called Euler vector) that leads to it from the reference frame. When used to represent an orientation, the rotation vector is commonly called orientation vector, or attitude vector.

A similar method, called axis-angle representation, describes a rotation or orientation using a unit vector aligned with the rotation axis, and a separate value to indicate the angle (see figure).

#### Orientation matrix

With the introduction of matrices the Euler theorems were rewritten. The rotations were described by orthogonal matrices referred to as rotation matrices or direction cosine matrices. When used to represent an orientation, a rotation matrix is commonly called orientation matrix, or attitude matrix.

The above-mentioned Euler vector is the eigenvector of a rotation matrix (a rotation matrix has a unique real eigenvalue). The product of two rotation matrices is the composition of rotations. Therefore, as before, the orientation can be given as the rotation from the initial frame to achieve the frame that we want to describe.

The configuration space of a non-symmetrical object in *n*-dimensional space is SO(*n*) × **R***n*. Orientation may be visualized by attaching a basis of tangent vectors to an object. The direction in which each vector points determines its orientation.

#### Orientation quaternion

Another way to describe rotations is using rotation quaternions, also called versors. They are equivalent to rotation matrices and rotation vectors. With respect to rotation vectors, they can be more easily converted to and from matrices. When used to represent orientations, rotation quaternions are typically called orientation quaternions or attitude quaternions.

### Newton's second law in three dimensions

To consider rigid body dynamics in three-dimensional space, Newton's second law must be extended to define the relationship between the movement of a rigid body and the system of forces and torques that act on it.

Newton formulated his second law for a particle as, "The change of motion of an object is proportional to the force impressed and is made in the direction of the straight line in which the force is impressed." Because Newton generally referred to mass times velocity as the "motion" of a particle, the phrase "change of motion" refers to the mass times acceleration of the particle, and so this law is usually written as $\mathbf {F} =m\mathbf {a} ,$ where **F** is understood to be the only external force acting on the particle, *m* is the mass of the particle, and **a** is its acceleration vector. The extension of Newton's second law to rigid bodies is achieved by considering a rigid system of particles.

### Rigid system of particles

If a system of *N* particles, Pi, i=1,...,*N*, are assembled into a rigid body, then Newton's second law can be applied to each of the particles in the body. If **F**i is the external force applied to particle Pi with mass *m*i, then $\mathbf {F} _{i}+\sum _{j=1}^{N}\mathbf {F} _{ij}=m_{i}\mathbf {a} _{i},\quad i=1,\ldots ,N,$ where **F**ij is the internal force of particle Pj acting on particle Pi that maintains the constant distance between these particles.

An important simplification to these force equations is obtained by introducing the resultant force and torque that acts on the rigid system. This resultant force and torque is obtained by choosing one of the particles in the system as a reference point, **R**, where each of the external forces are applied with the addition of an associated torque. The resultant force **F** and torque **T** are given by the formulas, $\mathbf {F} =\sum _{i=1}^{N}\mathbf {F} _{i},\quad \mathbf {T} =\sum _{i=1}^{N}(\mathbf {R} _{i}-\mathbf {R} )\times \mathbf {F} _{i},$ where **R**i is the vector that defines the position of particle Pi.

Newton's second law for a particle combines with these formulas for the resultant force and torque to yield, $\mathbf {F} =\sum _{i=1}^{N}m_{i}\mathbf {a} _{i},\quad \mathbf {T} =\sum _{i=1}^{N}(\mathbf {R} _{i}-\mathbf {R} )\times (m_{i}\mathbf {a} _{i}),$ where the internal forces **F***ij* cancel in pairs. The kinematics of a rigid body yields the formula for the acceleration of the particle Pi in terms of the position **R** and acceleration **a** of the reference particle as well as the angular velocity vector ω and angular acceleration vector α of the rigid system of particles as, $\mathbf {a} _{i}=\alpha \times (\mathbf {R} _{i}-\mathbf {R} )+\omega \times (\omega \times (\mathbf {R} _{i}-\mathbf {R} ))+\mathbf {a} .$

### Mass properties

The mass properties of the rigid body are represented by its center of mass and inertia matrix. Choose the reference point **R** so that it satisfies the condition $\sum _{i=1}^{N}m_{i}(\mathbf {R} _{i}-\mathbf {R} )=0,$

then it is known as the center of mass of the system.

The inertia matrix [IR] of the system relative to the reference point **R** is defined by $[I_{R}]=\sum _{i=1}^{N}m_{i}\left(\mathbf {I} \left(\mathbf {S} _{i}^{\textsf {T}}\mathbf {S} _{i}\right)-\mathbf {S} _{i}\mathbf {S} _{i}^{\textsf {T}}\right),$

where $\mathbf {S} _{i}$ is the column vector **R**i − **R**; $\mathbf {S} _{i}^{\textsf {T}}$ is its transpose, and $\mathbf {I}$ is the 3 by 3 identity matrix.

$\mathbf {S} _{i}^{\textsf {T}}\mathbf {S} _{i}$ is the scalar product of $\mathbf {S} _{i}$ with itself, while $\mathbf {S} _{i}\mathbf {S} _{i}^{\textsf {T}}$ is the tensor product of $\mathbf {S} _{i}$ with itself.

### Force-torque equations

Using the center of mass and inertia matrix, the force and torque equations for a single rigid body take the form $\mathbf {F} =m\mathbf {a} ,\quad \mathbf {T} =[I_{R}]\alpha +\omega \times [I_{R}]\omega ,$ and are known as Newton's second law of motion for a rigid body.

The dynamics of an interconnected system of rigid bodies, *B**i*, *j* = 1, ..., *M*, is formulated by isolating each rigid body and introducing the interaction forces. The resultant of the external and interaction forces on each body, yields the force-torque equations $\mathbf {F} _{j}=m_{j}\mathbf {a} _{j},\quad \mathbf {T} _{j}=[I_{R}]_{j}\alpha _{j}+\omega _{j}\times [I_{R}]_{j}\omega _{j},\quad j=1,\ldots ,M.$

Newton's formulation yields 6*M* equations that define the dynamics of a system of *M* rigid bodies.

### Rotation in three dimensions

A rotating object, whether under the influence of torques or not, may exhibit the behaviours of precession and nutation. The fundamental equation describing the behavior of a rotating solid body is Euler's equation of motion: ${\boldsymbol {\tau }}={\frac {D\mathbf {L} }{Dt}}={\frac {d\mathbf {L} }{dt}}+{\boldsymbol {\omega }}\times \mathbf {L} ={\frac {d(I{\boldsymbol {\omega }})}{dt}}+{\boldsymbol {\omega }}\times {I{\boldsymbol {\omega }}}=I{\boldsymbol {\alpha }}+{\boldsymbol {\omega }}\times {I{\boldsymbol {\omega }}}$ where the pseudovectors **τ** and **L** are, respectively, the torques on the body and its angular momentum, the scalar *I* is its moment of inertia, the vector **ω** is its angular velocity, the vector **α** is its angular acceleration, D is the differential in an inertial reference frame and d is the differential in a relative reference frame fixed with the body.

The solution to this equation when there is no applied torque is discussed in the articles Euler's equation of motion and Poinsot's ellipsoid.

It follows from Euler's equation that a torque **τ** applied perpendicular to the axis of rotation, and therefore perpendicular to **L**, results in a rotation about an axis perpendicular to both **τ** and **L**. This motion is called *precession*. The angular velocity of precession **Ω**P is given by the cross product: ${\boldsymbol {\tau }}={\boldsymbol {\Omega }}_{\mathrm {P} }\times \mathbf {L} .$

Precession can be demonstrated by placing a spinning top with its axis horizontal and supported loosely (frictionless toward precession) at one end. Instead of falling, as might be expected, the top appears to defy gravity by remaining with its axis horizontal, when the other end of the axis is left unsupported and the free end of the axis slowly describes a circle in a horizontal plane, the resulting precession turning. This effect is explained by the above equations. The torque on the top is supplied by a couple of forces: gravity acting downward on the device's centre of mass, and an equal force acting upward to support one end of the device. The rotation resulting from this torque is not downward, as might be intuitively expected, causing the device to fall, but perpendicular to both the gravitational torque (horizontal and perpendicular to the axis of rotation) and the axis of rotation (horizontal and outwards from the point of support), i.e., about a vertical axis, causing the device to rotate slowly about the supporting point.

Under a constant torque of magnitude *τ*, the speed of precession *Ω*P is inversely proportional to *L*, the magnitude of its angular momentum: $\tau ={\mathit {\Omega }}_{\mathrm {P} }L\sin \theta ,$ where *θ* is the angle between the vectors **Ω**P and **L**. Thus, if the top's spin slows down (for example, due to friction), its angular momentum decreases and so the rate of precession increases. This continues until the device is unable to rotate fast enough to support its own weight, when it stops precessing and falls off its support, mostly because friction against precession cause another precession that goes to cause the fall.

By convention, these three vectors – torque, spin, and precession – are all oriented with respect to each other according to the right-hand rule.

## Virtual work of forces acting on a rigid body

An alternate formulation of rigid body dynamics that has a number of convenient features is obtained by considering the virtual work of forces acting on a rigid body.

The virtual work of forces acting at various points on a single rigid body can be calculated using the velocities of their point of application and the resultant force and torque. To see this, let the forces **F**1, **F**2 ... **F***n* act on the points **R**1, **R**2 ... **R***n* in a rigid body.

The trajectories of **R***i*, *i* = 1, ..., *n* are defined by the movement of the rigid body. The velocity of the points **R***i* along their trajectories are $\mathbf {V} _{i}={\boldsymbol {\omega }}\times (\mathbf {R} _{i}-\mathbf {R} )+\mathbf {V} ,$ where **ω** is the angular velocity vector of the body.

### Virtual work

Work is computed from the dot product of each force with the displacement of its point of contact $\delta W=\sum _{i=1}^{n}\mathbf {F} _{i}\cdot \delta \mathbf {r} _{i}.$ If the trajectory of a rigid body is defined by a set of generalized coordinates *q**j*, *j* = 1, ..., *m*, then the virtual displacements *δ***r**i are given by $\delta \mathbf {r} _{i}=\sum _{j=1}^{m}{\frac {\partial \mathbf {r} _{i}}{\partial q_{j}}}\delta q_{j}=\sum _{j=1}^{m}{\frac {\partial \mathbf {V} _{i}}{\partial {\dot {q}}_{j}}}\delta q_{j}.$ The virtual work of this system of forces acting on the body in terms of the generalized coordinates becomes $\delta W=\mathbf {F} _{1}\cdot \left(\sum _{j=1}^{m}{\frac {\partial \mathbf {V} _{1}}{\partial {\dot {q}}_{j}}}\delta q_{j}\right)+\dots +\mathbf {F} _{n}\cdot \left(\sum _{j=1}^{m}{\frac {\partial \mathbf {V} _{n}}{\partial {\dot {q}}_{j}}}\delta q_{j}\right)$

or collecting the coefficients of *δqj* $\delta W=\left(\sum _{i=1}^{n}\mathbf {F} _{i}\cdot {\frac {\partial \mathbf {V} _{i}}{\partial {\dot {q}}_{1}}}\right)\delta q_{1}+\dots +\left(\sum _{1=1}^{n}\mathbf {F} _{i}\cdot {\frac {\partial \mathbf {V} _{i}}{\partial {\dot {q}}_{m}}}\right)\delta q_{m}.$

### Generalized forces

For simplicity consider a trajectory of a rigid body that is specified by a single generalized coordinate q, such as a rotation angle, then the formula becomes $\delta W=\left(\sum _{i=1}^{n}\mathbf {F} _{i}\cdot {\frac {\partial \mathbf {V} _{i}}{\partial {\dot {q}}}}\right)\delta q=\left(\sum _{i=1}^{n}\mathbf {F} _{i}\cdot {\frac {\partial ({\boldsymbol {\omega }}\times (\mathbf {R} _{i}-\mathbf {R} )+\mathbf {V} )}{\partial {\dot {q}}}}\right)\delta q.$

Introduce the resultant force **F** and torque **T** so this equation takes the form $\delta W=\left(\mathbf {F} \cdot {\frac {\partial \mathbf {V} }{\partial {\dot {q}}}}+\mathbf {T} \cdot {\frac {\partial {\boldsymbol {\omega }}}{\partial {\dot {q}}}}\right)\delta q.$

The quantity *Q* defined by $Q=\mathbf {F} \cdot {\frac {\partial \mathbf {V} }{\partial {\dot {q}}}}+\mathbf {T} \cdot {\frac {\partial {\boldsymbol {\omega }}}{\partial {\dot {q}}}},$

is known as the generalized force associated with the virtual displacement δq. This formula generalizes to the movement of a rigid body defined by more than one generalized coordinate, that is $\delta W=\sum _{j=1}^{m}Q_{j}\delta q_{j},$ where $Q_{j}=\mathbf {F} \cdot {\frac {\partial \mathbf {V} }{\partial {\dot {q}}_{j}}}+\mathbf {T} \cdot {\frac {\partial {\boldsymbol {\omega }}}{\partial {\dot {q}}_{j}}},\quad j=1,\ldots ,m.$

It is useful to note that conservative forces such as gravity and spring forces are derivable from a potential function *V*(*q*1, ..., *q**n*), known as a potential energy. In this case the generalized forces are given by $Q_{j}=-{\frac {\partial V}{\partial q_{j}}},\quad j=1,\ldots ,m.$

## D'Alembert's form of the principle of virtual work

The equations of motion for a mechanical system of rigid bodies can be determined using D'Alembert's form of the principle of virtual work. The principle of virtual work is used to study the static equilibrium of a system of rigid bodies; however, by introducing acceleration terms in Newton's laws this approach is generalized to define dynamic equilibrium.

### Static equilibrium

The static equilibrium of a mechanical system rigid bodies is defined by the condition that the virtual work of the applied forces is zero for any virtual displacement of the system. This is known as the *principle of virtual work.* This is equivalent to the requirement that the generalized forces for any virtual displacement are zero, that is *Q**i*=0.

Let a mechanical system be constructed from n rigid bodies, B*i*, *i* = 1, ..., *n*, and let the resultant of the applied forces on each body be the force-torque pairs, **F***i* and **T***i*, *i* = 1, ..., *n*. Notice that these applied forces do not include the reaction forces where the bodies are connected. Finally, assume that the velocity **V***i* and angular velocities ***ω****i*, *i* = 1, ..., *n*, for each rigid body, are defined by a single generalized coordinate q. Such a system of rigid bodies is said to have one degree of freedom.

The virtual work of the forces and torques, **F***i* and **T***i*, applied to this one degree of freedom system is given by $\delta W=\sum _{i=1}^{n}\left(\mathbf {F} _{i}\cdot {\frac {\partial \mathbf {V} _{i}}{\partial {\dot {q}}}}+\mathbf {T} _{i}\cdot {\frac {\partial {\boldsymbol {\omega }}_{i}}{\partial {\dot {q}}}}\right)\delta q=Q\delta q,$ where $Q=\sum _{i=1}^{n}\left(\mathbf {F} _{i}\cdot {\frac {\partial \mathbf {V} _{i}}{\partial {\dot {q}}}}+\mathbf {T} _{i}\cdot {\frac {\partial {\boldsymbol {\omega }}_{i}}{\partial {\dot {q}}}}\right),$ is the generalized force acting on this one degree of freedom system.

If the mechanical system is defined by m generalized coordinates, *q**j*, *j* = 1, ..., *m*, then the system has m degrees of freedom and the virtual work is given by, $\delta W=\sum _{j=1}^{m}Q_{j}\delta q_{j},$ where $Q_{j}=\sum _{i=1}^{n}\left(\mathbf {F} _{i}\cdot {\frac {\partial \mathbf {V} _{i}}{\partial {\dot {q}}_{j}}}+\mathbf {T} _{i}\cdot {\frac {\partial {\boldsymbol {\omega }}_{i}}{\partial {\dot {q}}_{j}}}\right),\quad j=1,\ldots ,m.$ is the generalized force associated with the generalized coordinate *q**j*. The principle of virtual work states that static equilibrium occurs when these generalized forces acting on the system are zero, that is $Q_{j}=0,\quad j=1,\ldots ,m.$

These m equations define the static equilibrium of the system of rigid bodies.

### Generalized inertia forces

Consider a single rigid body which moves under the action of a resultant force **F** and torque **T**, with one degree of freedom defined by the generalized coordinate *q*. Assume the reference point for the resultant force and torque is the center of mass of the body, then the generalized inertia force *Q** associated with the generalized coordinate q is given by $Q^{*}=-(M\mathbf {A} )\cdot {\frac {\partial \mathbf {V} }{\partial {\dot {q}}}}-\left([I_{R}]{\boldsymbol {\alpha }}+{\boldsymbol {\omega }}\times [I_{R}]{\boldsymbol {\omega }}\right)\cdot {\frac {\partial {\boldsymbol {\omega }}}{\partial {\dot {q}}}}.$

This inertia force can be computed from the kinetic energy of the rigid body, $T={\tfrac {1}{2}}M\mathbf {V} \cdot \mathbf {V} +{\tfrac {1}{2}}{\boldsymbol {\omega }}\cdot [I_{R}]{\boldsymbol {\omega }},$ by using the formula $Q^{*}=-\left({\frac {d}{dt}}{\frac {\partial T}{\partial {\dot {q}}}}-{\frac {\partial T}{\partial q}}\right).$

A system of n rigid bodies with m generalized coordinates has the kinetic energy $T=\sum _{i=1}^{n}\left({\tfrac {1}{2}}M\mathbf {V} _{i}\cdot \mathbf {V} _{i}+{\tfrac {1}{2}}{\boldsymbol {\omega }}_{i}\cdot [I_{R}]{\boldsymbol {\omega }}_{i}\right),$ which can be used to calculate the m generalized inertia forces $Q_{j}^{*}=-\left({\frac {d}{dt}}{\frac {\partial T}{\partial {\dot {q}}_{j}}}-{\frac {\partial T}{\partial q_{j}}}\right),\quad j=1,\ldots ,m.$

### Dynamic equilibrium

D'Alembert's form of the principle of virtual work states that a system of rigid bodies is in dynamic equilibrium when the virtual work of the sum of the applied forces and the inertial forces is zero for any virtual displacement of the system. Thus, dynamic equilibrium of a system of n rigid bodies with m generalized coordinates requires that $\delta W=\left(Q_{1}+Q_{1}^{*}\right)\delta q_{1}+\dots +\left(Q_{m}+Q_{m}^{*}\right)\delta q_{m}=0,$ for any set of virtual displacements *δq**j*. This condition yields m equations, $Q_{j}+Q_{j}^{*}=0,\quad j=1,\ldots ,m,$ which can also be written as ${\frac {d}{dt}}{\frac {\partial T}{\partial {\dot {q}}_{j}}}-{\frac {\partial T}{\partial q_{j}}}=Q_{j},\quad j=1,\ldots ,m.$ The result is a set of m equations of motion that define the dynamics of the rigid body system.

### Lagrange's equations

If the generalized forces Q*j* are derivable from a potential energy *V*(*q*1, ..., *q**m*), then these equations of motion take the form ${\frac {d}{dt}}{\frac {\partial T}{\partial {\dot {q}}_{j}}}-{\frac {\partial T}{\partial q_{j}}}=-{\frac {\partial V}{\partial q_{j}}},\quad j=1,\ldots ,m.$

In this case, introduce the Lagrangian, *L* = *T* − *V*, so these equations of motion become ${\frac {d}{dt}}{\frac {\partial L}{\partial {\dot {q}}_{j}}}-{\frac {\partial L}{\partial q_{j}}}=0\quad j=1,\ldots ,m.$ These are known as Lagrange's equations of motion.

## Linear and angular momentum

### System of particles

The linear and angular momentum of a rigid system of particles is formulated by measuring the position and velocity of the particles relative to the center of mass. Let the system of particles Pi, *i* = 1, ..., *n* be located at the coordinates **r***i* and velocities **v***i*. Select a reference point **R** and compute the relative position and velocity vectors, $\mathbf {r} _{i}=\left(\mathbf {r} _{i}-\mathbf {R} \right)+\mathbf {R} ,\quad \mathbf {v} _{i}={\frac {d}{dt}}(\mathbf {r} _{i}-\mathbf {R} )+\mathbf {V} .$

The total linear and angular momentum vectors relative to the reference point **R** are $\mathbf {p} ={\frac {d}{dt}}\left(\sum _{i=1}^{n}m_{i}\left(\mathbf {r} _{i}-\mathbf {R} \right)\right)+\left(\sum _{i=1}^{n}m_{i}\right)\mathbf {V} ,$ and $\mathbf {L} =\sum _{i=1}^{n}m_{i}\left(\mathbf {r} _{i}-\mathbf {R} \right)\times {\frac {d}{dt}}\left(\mathbf {r} _{i}-\mathbf {R} \right)+\left(\sum _{i=1}^{n}m_{i}\left(\mathbf {r} _{i}-\mathbf {R} \right)\right)\times \mathbf {V} .$

If **R** is chosen as the center of mass these equations simplify to $\mathbf {p} =M\mathbf {V} ,\quad \mathbf {L} =\sum _{i=1}^{n}m_{i}\left(\mathbf {r} _{i}-\mathbf {R} \right)\times {\frac {d}{dt}}\left(\mathbf {r} _{i}-\mathbf {R} \right).$

### Rigid system of particles

To specialize these formulas to a rigid body, assume the particles are rigidly connected to each other so Pi, i=1,...,n are located by the coordinates **r**i and velocities **v**i. Select a reference point **R** and compute the relative position and velocity vectors, $\mathbf {r} _{i}=(\mathbf {r} _{i}-\mathbf {R} )+\mathbf {R} ,\quad \mathbf {v} _{i}=\omega \times (\mathbf {r} _{i}-\mathbf {R} )+\mathbf {V} ,$ where ω is the angular velocity of the system.

The linear momentum and angular momentum of this rigid system measured relative to the center of mass **R** is $\mathbf {p} =\left(\sum _{i=1}^{n}m_{i}\right)\mathbf {V} ,\quad \mathbf {L} =\sum _{i=1}^{n}m_{i}(\mathbf {r} _{i}-\mathbf {R} )\times \mathbf {v} _{i}=\sum _{i=1}^{n}m_{i}(\mathbf {r} _{i}-\mathbf {R} )\times (\omega \times (\mathbf {r} _{i}-\mathbf {R} )).$

These equations simplify to become, $\mathbf {p} =M\mathbf {V} ,\quad \mathbf {L} =[I_{R}]\omega ,$ where M is the total mass of the system and [IR] is the moment of inertia matrix defined by $[I_{R}]=-\sum _{i=1}^{n}m_{i}[r_{i}-R][r_{i}-R],$ where [r*i* − R] is the skew-symmetric matrix constructed from the vector **r***i* − **R**.

## Applications

- Analysis of robotic systems
- Biomechanical analysis of animals, humans or humanoid systems
- Analysis of space objects
- Understanding of strange motions of rigid bodies.
- Design and development of dynamics-based sensors, such as gyroscopic sensors.
- Design and development of various stability enhancement applications in automobiles.
- Improving the graphics of video games which involves rigid bodies
