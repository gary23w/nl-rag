---
title: "Center of mass"
source: https://en.wikipedia.org/wiki/Centre_of_mass
domain: ship-motions
license: CC-BY-SA-4.0
tags: ship motions
fetched: 2026-07-05
---

# Center of mass

(Redirected from

Centre of mass

)

In physics, the **center of mass** of a distribution of mass in space (sometimes referred to as the **barycenter** or **balance point**) is the unique point at any given time where the weighted relative position of the distributed mass sums to zero. For a rigid body containing its center of mass, this is the point to which a force may be applied to cause a linear acceleration without an angular acceleration. Calculations in mechanics are often simplified when formulated with respect to the center of mass. It is a hypothetical point where the entire mass of an object may be assumed to be concentrated to visualise its motion. In other words, the center of mass is the particle equivalent of a given object for the application of Newton's laws of motion.

In the case of a single rigid body, the center of mass is fixed in relation to the body, and if the body has uniform density, it will be located at the centroid. The center of mass may be located outside the physical body, as is sometimes the case for hollow or open-shaped objects, such as a horseshoe. In the case of a distribution of separate bodies, such as the planets of the Solar System, the center of mass may not correspond to the position of any individual member of the system.

The center of mass is a useful reference point for calculations in mechanics that involve masses distributed in space, such as the linear and angular momentum of planetary bodies and rigid body dynamics. In orbital mechanics, the equations of motion of planets are formulated as point masses located at the centers of mass (see Barycenter (astronomy) for details). The center of mass frame is an inertial frame in which the center of mass of a system is at rest with respect to the origin of the coordinate system.

## History

The origins of the concept of the center of gravity (AKA center of weight, center of mass) are unknown, but it appears to have been a well-known philosophical concept in the ancient Greek world. It is discussed in the works of Hero of Alexandria and Pappus of Alexandria in detail in the 2nd and 3rd century CE, but makes its first known appearance in the 3rd century BCE in the writings of Archimedes of Syracuse, an ancient Greek mathematician, physicist, and engineer. He worked with simplified assumptions about gravity that amount to a uniform field, thus arriving at the mathematical properties of what we now call the center of mass. Archimedes showed that the torque exerted on a lever by weights resting at various points along the lever is the same as what it would be if all of the weights were moved to a single point—their center of mass. In his work *On Floating Bodies*, Archimedes demonstrated that the orientation of a floating object is the one that makes its center of mass as low as possible. He developed mathematical techniques for finding the centers of mass of objects of uniform density of various well-defined shapes. However, the surviving writings of Archimedes treat some form of the center of gravity itself as a preexisting idea, implying that it has earlier origins, either in his own preceding but lost studies, or in unknown works of his contemporaries or predecessors Dijksterhuis argues for pre-Greek origins of the concept, based on contextual clues.

In the Renaissance and Early Modern periods, work by Guido Ubaldi, Francesco Maurolico, Federico Commandino, Evangelista Torricelli, Simon Stevin, Luca Valerio, Jean-Charles de la Faille, Paul Guldin, John Wallis, Christiaan Huygens, Louis Carré, Pierre Varignon, and Alexis Clairaut expanded the concept further.

Newton's second law is reformulated with respect to the center of mass in Euler's first law.

## Definition

The center of mass is the unique point at the center of a distribution of mass in space that has the property that the weighted position vectors relative to this point sum to zero. In analogy to statistics, the center of mass is the mean location of a distribution of mass in space.

### A system of particles

For a system of particles $P_{i}$ , $i=1,...,n$ , the center of mass is defined as $\mathbf {R} ={\sum _{i=1}^{n}m_{i}\mathbf {r} _{i} \over \sum _{i=1}^{n}m_{i}},$ where $m_{i}$ denotes the masses of the particles and $\mathbf {r} _{i}$ denotes the positions of the partices.

In the case of a system of only two particles, this reduces to $\mathbf {R} ={\frac {m_{1}\mathbf {r} _{1}+m_{2}\mathbf {r} _{2}}{m_{1}+m_{2}}}.$

### A continuous volume

In the case of a continuous volume, the sum goes to an integral, so that the equation for the center of mass becomes $\mathbf {R} ={\frac {1}{M}}\int \mathbf {r} \,dm={\frac {1}{M}}\int \rho (\mathbf {r} )\mathbf {r} \,dV,$ where M is the total mass in the volume and $\rho (\mathbf {r} )$ is the density of the volume at position $\mathbf {r}$ .

If a continuous mass distribution has uniform density, which means that *ρ* is constant, then the center of mass is the same as the centroid of the volume.

### Systems with periodic boundary conditions

For particles in a system with periodic boundary conditions two particles can be neighbours even though they are on opposite sides of the system. This occurs often in molecular dynamics simulations, for example, in which clusters form at random locations and sometimes neighbouring atoms cross the periodic boundary. When a cluster straddles the periodic boundary, a naive calculation of the center of mass will be incorrect. A generalized method for calculating the center of mass for periodic systems is to treat each coordinate, *x* and *y* and/or *z*, as if it were on a circle instead of a line. The calculation takes every particle's *x* coordinate and computes *N* possible centers of mass,

${\bar {x}}_{n}={\bar {x}}_{0}+{\frac {2\pi n}{N}},\;\;\;n=1,2,\ldots ,N,$

where ${\bar {x}}_{0}$ is the naïve mass-weighted average position for all particles. The true center of mass is then the value in the vector ${\bar {\mathbf {x} }}=[{\bar {x}}_{1},{\bar {x}}_{2},\ldots ,{\bar {x}}_{n}]$ , with the lowest sum of squared arc distances between the points.

The process can be repeated for all dimensions of the system to determine the complete center of mass. The utility of the algorithm is that it allows the mathematics to determine where the "best" center of mass is, instead of guessing or using cluster analysis to "unfold" a cluster straddling the periodic boundaries. This approach computes the intrinsic center of mass. The extrinsic circular mean is a popular way to estimate the center of mass, however this approach can be inaccurate.

## Center of gravity

A body's center of gravity is the point around which the resultant torque due to gravity forces vanishes. Where a gravity field can be considered to be uniform, the center of mass and the center of gravity will be the same. However, for satellites in orbit around a planet, in the absence of other torques being applied to a satellite, the slight variation (gradient) in gravitational field between the parts closer to and further from the planet (stronger and weaker gravity respectively) can lead to a torque that will tend to align the satellite such that its long axis is vertical. In such a case, it is important to make the distinction between the center of gravity and the mass center. Any horizontal offset between the two will result in an applied torque.

The mass center is a fixed property for a given rigid body (e.g., with no slosh or articulation), whereas the center of gravity may, in addition, depend upon its orientation in a non-uniform gravitational field. In the latter case, the center of gravity will always be located somewhat closer to the main attractive body as compared to the mass center, and thus will change its position in the body of interest as its orientation is changed.

In the study of the dynamics of aircraft, vehicles and vessels, forces and moments need to be resolved relative to the mass center. That is true independent of whether gravity itself is a consideration. Referring to the mass center as the center of gravity is something of a colloquialism, but it is in common usage and when gravity gradient effects are negligible, center of gravity and mass center are the same and are used interchangeably.

In physics the benefits of using the center of mass to model a mass distribution can be seen by considering the resultant of the gravity forces on a continuous body. Consider a body *Q* of volume *V* with density *ρ*(**r**) at each point **r** in the volume. In a parallel gravity field the force **f** at each point **r** is given by, $\mathbf {f} (\mathbf {r} )=-dm\,g\mathbf {\hat {k}} =-\rho (\mathbf {r} )\,dV\,g\mathbf {\hat {k}} ,$ where *dm* is the mass at the point **r**, *g* is the acceleration of gravity, and ${\textstyle \mathbf {\hat {k}} }$ is a unit vector defining the vertical direction.

Choose a reference point **R** in the volume and compute the resultant force and torque at this point, $\mathbf {F} =\iiint _{Q}\mathbf {f} (\mathbf {r} )\,dV=\iiint _{Q}\rho (\mathbf {r} )\,dV\left(-g\mathbf {\hat {k}} \right)=-Mg\mathbf {\hat {k}} ,$ and $\mathbf {T} =\iiint _{Q}(\mathbf {r} -\mathbf {R} )\times \mathbf {f} (\mathbf {r} )\,dV=\iiint _{Q}(\mathbf {r} -\mathbf {R} )\times \left(-g\rho (\mathbf {r} )\,dV\,\mathbf {\hat {k}} \right)=\left(\iiint _{Q}\rho (\mathbf {r} )\left(\mathbf {r} -\mathbf {R} \right)dV\right)\times \left(-g\mathbf {\hat {k}} \right).$

If the reference point **R** is chosen so that it is the center of mass, then $\iiint _{Q}\rho (\mathbf {r} )\left(\mathbf {r} -\mathbf {R} \right)dV=0,$ which means the resultant torque **T** = 0. Because the resultant torque is zero the body will move as though it is a particle with its mass concentrated at the center of mass.

By selecting the center of gravity as the reference point for a rigid body, the gravity forces will not cause the body to rotate, which means the weight of the body can be considered to be concentrated at the center of mass.

## Linear and angular momentum

The linear and angular momentum of a collection of particles can be simplified by measuring the position and velocity of the particles relative to the center of mass. Let the system of particles *Pi*, *i* = 1, ..., *n* of masses *mi* be located at the coordinates **r***i* with velocities **v***i*. Select a reference point **R** and compute the relative position and velocity vectors, $\mathbf {r} _{i}=(\mathbf {r} _{i}-\mathbf {R} )+\mathbf {R} ,\quad \mathbf {v} _{i}={\frac {d}{dt}}(\mathbf {r} _{i}-\mathbf {R} )+\mathbf {v} .$

The total linear momentum and angular momentum of the system are $\mathbf {p} ={\frac {d}{dt}}\left(\sum _{i=1}^{n}m_{i}(\mathbf {r} _{i}-\mathbf {R} )\right)+\left(\sum _{i=1}^{n}m_{i}\right)\mathbf {v} ,$ and $\mathbf {L} =\sum _{i=1}^{n}m_{i}(\mathbf {r} _{i}-\mathbf {R} )\times {\frac {d}{dt}}(\mathbf {r} _{i}-\mathbf {R} )+\left(\sum _{i=1}^{n}m_{i}\right)\left[\mathbf {R} \times {\frac {d}{dt}}(\mathbf {r} _{i}-\mathbf {R} )+(\mathbf {r} _{i}-\mathbf {R} )\times \mathbf {v} \right]+\left(\sum _{i=1}^{n}m_{i}\right)\mathbf {R} \times \mathbf {v}$

If **R** is chosen as the center of mass these equations simplify to $\mathbf {p} =m\mathbf {v} ,\quad \mathbf {L} =\sum _{i=1}^{n}m_{i}(\mathbf {r} _{i}-\mathbf {R} )\times {\frac {d}{dt}}(\mathbf {r} _{i}-\mathbf {R} )+\sum _{i=1}^{n}m_{i}\mathbf {R} \times \mathbf {v}$ where *m* is the total mass of all the particles, **p** is the linear momentum, and **L** is the angular momentum.

The law of conservation of momentum predicts that for any system not subjected to external forces the momentum of the system will remain constant, which means the center of mass will move with constant velocity. This applies for all systems with classical internal forces, including magnetic fields, electric fields, chemical reactions, and so on. More formally, this is true for any internal forces that cancel in accordance with Newton's third law.

## Determination

The experimental determination of a body's center of mass makes use of gravity forces on the body and is based on the fact that the center of mass is the same as the center of gravity in the parallel gravity field near the earth's surface.

The center of mass of a body with an axis of symmetry and constant density must lie on this axis. Thus, the center of mass of a circular cylinder of constant density has its center of mass on the axis of the cylinder. In the same way, the center of mass of a spherically symmetric body of constant density is at the center of the sphere. In general, for any symmetry of a body, its center of mass will be a fixed point of that symmetry.

### In two dimensions

An experimental method for locating the center of mass is to suspend the object from two different points, in series, and each time to drop a plumb line from the suspension point. The intersection of the two lines is the center of mass.

The shape of an object might already be mathematically determined, but it may be too complex to use a known formula. In this case, one can subdivide the complex shape into simpler, more elementary shapes, whose centers of mass are easy to find. If the total mass and center of mass can be determined for each area, then the center of mass of the whole is the weighted average of the centers. This method can even work for objects with holes, which can be accounted for as negative masses.

A direct development of the planimeter known as an integraph, or integerometer, can be used to establish the position of the centroid or center of mass of an irregular two-dimensional shape. This method can be applied to a shape with an irregular, smooth or complex boundary where other methods are too difficult. It was regularly used by ship builders to compare with the required displacement and center of buoyancy of a ship, and ensure it would not capsize.

### In three dimensions

An experimental method to locate the three-dimensional coordinates of the center of mass begins by supporting the object at three points and measuring the forces, **F**1, **F**2, and **F**3 that resist the weight of the object, $\mathbf {W} =-W\mathbf {\hat {k}}$ ( $\mathbf {\hat {k}}$ is the unit vector in the vertical direction). Let **r**1, **r**2, and **r**3 be the position coordinates of the support points, then the coordinates **R** of the center of mass satisfy the condition that the resultant torque is zero, $\mathbf {T} =(\mathbf {r} _{1}-\mathbf {R} )\times \mathbf {F} _{1}+(\mathbf {r} _{2}-\mathbf {R} )\times \mathbf {F} _{2}+(\mathbf {r} _{3}-\mathbf {R} )\times \mathbf {F} _{3}=0,$ or $\mathbf {R} \times \left(-W\mathbf {\hat {k}} \right)=\mathbf {r} _{1}\times \mathbf {F} _{1}+\mathbf {r} _{2}\times \mathbf {F} _{2}+\mathbf {r} _{3}\times \mathbf {F} _{3}.$

This equation yields the coordinates of the center of mass **R*** in the horizontal plane as, $\mathbf {R} ^{*}=-{\frac {1}{W}}\mathbf {\hat {k}} \times (\mathbf {r} _{1}\times \mathbf {F} _{1}+\mathbf {r} _{2}\times \mathbf {F} _{2}+\mathbf {r} _{3}\times \mathbf {F} _{3}).$

The center of mass lies on the vertical line **L**, given by $\mathbf {L} (t)=\mathbf {R} ^{*}+t\mathbf {\hat {k}} .$

The three-dimensional coordinates of the center of mass are determined by performing this experiment twice with the object positioned so that these forces are measured for two different horizontal planes through the object. The center of mass will be the intersection of the two lines **L**1 and **L**2 obtained from the two experiments.

## Applications

### Engineering designs

#### Automotive applications

Engineers try to design a sports car so that its center of mass is lowered to make the car handle better, which is to say, maintain traction while executing relatively sharp turns.

The characteristic low profile of the U.S. military Humvee was designed in part to allow it to tilt farther than taller vehicles without rolling over, by ensuring its low center of mass stays over the space bounded by the four wheels even at angles far from the horizontal.

#### Aeronautics

The center of mass is an important point on an aircraft, which significantly affects the stability of the aircraft. To ensure the aircraft is stable enough to be safe to fly, the center of mass must fall within specified limits. If the center of mass is ahead of the forward limit, the aircraft will be less maneuverable, possibly to the point of being unable to rotate for takeoff or flare for landing. If the center of mass is behind the aft limit, the aircraft will be more maneuverable, but also less stable, and possibly unstable enough so as to be impossible to fly. The moment arm of the elevator will also be reduced, which makes it more difficult to recover from a stalled condition.

For helicopters in hover, the center of mass is always directly below the rotorhead. In forward flight, the center of mass will move forward to balance the negative pitch torque produced by applying cyclic control to propel the helicopter forward; consequently a cruising helicopter flies "nose-down" in level flight.

### Astronomy

The center of mass plays an important role in astronomy and astrophysics, where it is commonly referred to as the *barycenter*. The barycenter is the point between two objects where they balance each other; it is the center of mass where two or more celestial bodies orbit each other. When a moon orbits a planet, or a planet orbits a star, both bodies are actually orbiting a point that lies away from the center of the primary (larger) body. For example, the Moon does not orbit the exact center of the Earth, but a point on a line between the center of the Earth and the Moon, approximately 1,710 km (1,062 miles) below the surface of the Earth, where their respective masses balance. This is the point about which the Earth and Moon orbit as they travel around the Sun. If the masses are more similar, e.g., Pluto and Charon, the barycenter will fall outside both bodies.

### Rigging and safety

Knowing the location of the center of gravity when rigging is crucial, possibly resulting in severe injury or death if assumed incorrectly. A center of gravity that is at or above the lift point will most likely result in a tip-over incident. In general, the further the center of gravity below the pick point, the safer the lift. There are other things to consider, such as shifting loads, strength of the load and mass, distance between pick points, and number of pick points. Specifically, when selecting lift points, it is very important to place the center of gravity at the center and well below the lift points.

### Body motion

The center of mass of the adult human body vertically is 10 cm above the trochanter (where the femur joins the hip), 1.4 cm forward of the knee and 1.0 cm behind the trochanter. In kinesiology and biomechanics, the center of mass is an important parameter that assists people in understanding their human locomotion. Typically, a human's center of mass is detected with one of two methods: the reaction board method is a static analysis that involves the person lying down on that instrument, and use of their static equilibrium equation to find their center of mass; the segmentation method relies on a mathematical solution based on the physical principle that the summation of the torques of individual body sections, relative to a specified axis, must equal the torque of the whole system that constitutes the body, measured relative to the same axis.

### Optimization

The center-of-gravity method is a method for convex optimization which uses the center of gravity of the feasible region.
