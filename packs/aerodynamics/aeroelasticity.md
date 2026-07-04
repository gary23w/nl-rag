---
title: "Aeroelasticity"
source: https://en.wikipedia.org/wiki/Aeroelasticity
domain: aerodynamics
license: CC-BY-SA-4.0
tags: aerodynamics
fetched: 2026-07-04
---

# Aeroelasticity

**Aeroelasticity** is the branch of physics and engineering studying the interactions between the inertial, elastic, and aerodynamic forces occurring while an elastic body is exposed to a fluid flow. The study of aeroelasticity may be broadly classified into two fields: *static aeroelasticity* dealing with the static or steady state response of an elastic body to a fluid flow, and *dynamic aeroelasticity* dealing with the body's dynamic (typically vibrational) response.

Aircraft are prone to aeroelastic effects because they need to be lightweight while enduring large aerodynamic loads. Aircraft are designed to avoid the following aeroelastic problems:

1. **divergence** where the aerodynamic forces increase the twist of a wing which further increases forces;
2. **control reversal** where control activation produces an opposite aerodynamic moment that reduces, or in extreme cases reverses, the control effectiveness; and
3. **flutter** which is uncontained vibration that can lead to the destruction of an aircraft.

Aeroelasticity problems can be prevented by adjusting the mass, stiffness or aerodynamics of structures which can be determined and verified through the use of calculations, *ground vibration tests* and *flight flutter trials*. Flutter of control surfaces is usually eliminated by the careful placement of *mass balances*.

The synthesis of aeroelasticity with thermodynamics is known as *aerothermoelasticity*, and its synthesis with control theory is known as *aeroservoelasticity*.

## History

The second failure of Samuel Langley's prototype plane on the Potomac was attributed to aeroelastic effects (specifically, torsional divergence). An early scientific work on the subject was George Bryan's *Theory of the Stability of a Rigid Aeroplane* published in 1906. Problems with torsional divergence plagued aircraft in the First World War and were solved largely by trial-and-error and ad hoc stiffening of the wing. The first recorded and documented case of flutter in an aircraft was that which occurred to a Handley Page O/400 bomber during a flight in 1916, when it suffered a violent tail oscillation, which caused extreme distortion of the rear fuselage and the elevators to move asymmetrically. Although the aircraft landed safely, in the subsequent investigation F. W. Lanchester was consulted. One of his recommendations was that left and right elevators should be rigidly connected by a stiff shaft, which was to subsequently become a design requirement. In addition, the National Physical Laboratory (NPL) was asked to investigate the phenomenon theoretically, which was subsequently carried out by Leonard Bairstow and Arthur Fage.

In 1926, Hans Reissner published a theory of wing divergence, leading to much further theoretical research on the subject. The term *aeroelasticity* itself was coined by Harold Roxbee Cox and Alfred Pugsley at the Royal Aircraft Establishment (RAE), Farnborough in the early 1930s.

In the development of aeronautical engineering at Caltech, Theodore von Kármán started a course "Elasticity applied to Aeronautics". After teaching the course for one term, Kármán passed it over to Ernest Edwin Sechler, who developed aeroelasticity in that course and in publication of textbooks on the subject.

In 1947, Arthur Roderick Collar defined aeroelasticity as "the study of the mutual interaction that takes place within the triangle of the inertial, elastic, and aerodynamic forces acting on structural members exposed to an airstream, and the influence of this study on design".

## Static aeroelasticity

In an aeroplane, two significant static aeroelastic effects may occur. *Divergence* is a phenomenon in which the elastic twist of the wing suddenly becomes theoretically infinite, typically causing the wing to fail. *Control reversal* is a phenomenon occurring only in wings with ailerons or other control surfaces, in which these control surfaces reverse their usual functionality (e.g., the rolling direction associated with a given aileron moment is reversed).

### Divergence

Divergence occurs when a lifting surface deflects under aerodynamic load in a direction which further increases lift in a positive feedback loop. The increased lift deflects the structure further, which eventually brings the structure to the point of divergence. Unlike flutter, which is another aeroelastic problem, instead of irregular oscillations, divergence causes the lifting surface to move in the same direction and when it comes to point of divergence the structure deforms.

| Equations for divergence of a simple beam |
|---|
| Divergence can be understood as a simple property of the differential equation(s) governing the wing deflection. For example, modelling the airplane wing as an isotropic Euler–Bernoulli beam, the uncoupled torsional equation of motion is $GJ{\frac {d^{2}\theta }{dy^{2}}}=-M',$ where *y* is the spanwise dimension, *θ* is the elastic twist of the beam, *GJ* is the torsional stiffness of the beam, *L* is the beam length, and *M*’ is the aerodynamic moment per unit length. Under a simple lift forcing theory the aerodynamic moment is of the form $M'=CU^{2}(\theta +\alpha _{0}),$ where *C* is a coefficient, *U* is the free-stream fluid velocity, and α0 is the initial angle of attack. This yields an ordinary differential equation of the form ${\frac {d^{2}\theta }{dy^{2}}}+\lambda ^{2}\theta =-\lambda ^{2}\alpha _{0},$ where $\lambda ^{2}=C{\frac {U^{2}}{GJ}}.$ The boundary conditions for a clamped-free beam (i.e., a cantilever wing) are $\theta \|_{y=0}=\left.{\frac {d\theta }{dy}}\right\|_{y=L}=0,$ which yields the solution $\theta =\alpha _{0}[\tan(\lambda L)\sin(\lambda y)+\cos(\lambda y)-1].$ As can be seen, for *λL* = *π*/2 + *nπ*, with arbitrary integer number *n*, tan(*λL*) is infinite. *n* = 0 corresponds to the point of torsional divergence. For given structural parameters, this will correspond to a single value of free-stream velocity *U*. This is the torsional divergence speed. Note that for some special boundary conditions that may be implemented in a wind tunnel test of an airfoil (e.g., a torsional restraint positioned forward of the aerodynamic center) it is possible to eliminate the phenomenon of divergence altogether. |

### Control reversal

Control surface reversal is the loss (or reversal) of the expected response of a control surface, due to deformation of the main lifting surface. For simple models (e.g. single aileron on an Euler-Bernoulli beam), control reversal speeds can be derived analytically as for torsional divergence. Control reversal can be used to aerodynamic advantage, and forms part of the Kaman servo-flap rotor design.

## Dynamic aeroelasticity

Dynamic aeroelasticity studies the interactions among aerodynamic, elastic, and inertial forces. Examples of dynamic aeroelastic phenomena are:

### Flutter

**Flutter** is a dynamic instability of an elastic structure in a fluid flow, caused by positive feedback between the body's deflection and the force exerted by the fluid flow. In a linear system, "flutter point" is the point at which the structure is undergoing simple harmonic motion—zero net damping—and so any further decrease in net damping will result in a self-oscillation and eventual failure. "Net damping" can be understood as the sum of the structure's natural positive damping and the negative damping of the aerodynamic force. Flutter can be classified into two types: *hard flutter*, in which the net damping decreases very suddenly, very close to the flutter point; and *soft flutter*, in which the net damping decreases gradually.

In water the mass ratio of the pitch inertia of the foil to that of the circumscribing cylinder of fluid is generally too low for binary flutter to occur, as shown by explicit solution of the simplest pitch and heave flutter stability determinant.

Structures exposed to aerodynamic forces—including wings and aerofoils, but also chimneys and bridges—are generally designed carefully within known parameters to avoid flutter. Blunt shapes, such as chimneys, can give off a continuous stream of vortices known as a Kármán vortex street, which can induce structural oscillations. Strakes are typically wrapped around chimneys to stop the formation of these vortices.

In complex structures where both the aerodynamics and the mechanical properties of the structure are not fully understood, flutter can be discounted only through detailed testing. Even changing the mass distribution of an aircraft or the stiffness of one component can induce flutter in an apparently unrelated aerodynamic component. At its mildest, this can appear as a "buzz" in the aircraft structure, but at its most violent, it can develop uncontrollably with great speed and cause serious damage to the aircraft or lead to its destruction, as in Northwest Airlines Flight 2 in 1938, Braniff Flight 542 in 1959, or the prototypes for Finland's VL Myrsky fighter aircraft in the early 1940s. Famously, the original Tacoma Narrows Bridge was destroyed as a result of aeroelastic fluttering.

#### Aeroservoelasticity

In some cases, automatic control systems have been demonstrated to help prevent or limit flutter-related structural vibration.

#### Propeller whirl flutter

*Propeller whirl flutter* is a special case of flutter involving the aerodynamic and inertial effects of a rotating propeller and the stiffness of the supporting nacelle structure. Dynamic instability can occur involving pitch and yaw degrees of freedom of the propeller and the engine supports leading to an unstable precession of the propeller. Failure of the engine supports led to whirl flutter occurring on two Lockheed L-188 Electra aircraft, in 1959 on Braniff Flight 542 and again in 1960 on Northwest Orient Airlines Flight 710.

#### Transonic aeroelasticity

Flow is highly non-linear in the transonic regime, dominated by moving shock waves. Avoiding flutter is mission-critical for aircraft that fly through transonic Mach numbers. The role of shock waves was first analyzed by Holt Ashley. A phenomenon that impacts stability of aircraft known as "transonic dip", in which the flutter speed can get close to flight speed, was reported in May 1976 by Farmer and Hanson of the Langley Research Center.

### Buffeting

Buffeting is a high-frequency instability, caused by airflow separation or shock wave oscillations from one object striking another. It is caused by a sudden impulse of load increasing. It is a random forced vibration. Generally it affects the tail unit of the aircraft structure due to air flow downstream of the wing.

The methods for buffet detection are:

1. Pressure coefficient diagram
2. Pressure divergence at trailing edge
3. Computing separation from trailing edge based on Mach number
4. Normal force fluctuating divergence

## Prediction and cure

In the period 1950–1970, AGARD developed the *Manual on Aeroelasticity* which details the processes used in solving and verifying aeroelastic problems along with standard examples that can be used to test numerical solutions.

Aeroelasticity involves not just the external aerodynamic loads and the way they change but also the structural, damping and mass characteristics of the aircraft. Prediction involves making a mathematical model of the aircraft as a series of masses connected by springs and dampers which are tuned to represent the dynamic characteristics of the aircraft structure. The model also includes details of applied aerodynamic forces and how they vary.

The model can be used to predict the flutter margin and, if necessary, test fixes to potential problems. Small carefully chosen changes to mass distribution and local structural stiffness can be very effective in solving aeroelastic problems.

Methods of predicting flutter in linear structures include the *p-method*, the *k-method* and the *p-k method*.

For nonlinear systems, flutter is usually interpreted as a limit cycle oscillation (LCO), and methods from the study of dynamical systems can be used to determine the speed at which flutter will occur.

## Media

These videos detail the Active Aeroelastic Wing two-phase NASA-Air Force flight research program to investigate the potential of aerodynamically twisting flexible wings to improve maneuverability of high-performance aircraft at transonic and supersonic speeds, with traditional control surfaces such as ailerons and leading-edge flaps used to induce the twist.

- Time lapsed film of Active Aeroelastic Wing (AAW) Wing loads test, December, 2002
- F/A-18A (now X-53) Active Aeroelastic Wing (AAW) flight test, December, 2002

## Notable aeroelastic failures

- The original Tacoma Narrows Bridge was destroyed as a result of aeroelastic flutter.
- Propeller whirl flutter of the Lockheed L-188 Electra on Braniff Flight 542.
- 1931 Transcontinental & Western Air Fokker F-10 crash.
- Body freedom flutter of the GAF Jindivik drone.
