---
title: "Spacetime (part 2/3)"
source: https://en.wikipedia.org/wiki/Spacetime
domain: general-relativity
license: CC-BY-SA-4.0
tags: general relativity, einstein field equations, spacetime curvature, gravitational wave
fetched: 2026-07-02
part: 2/3
---

## Basic mathematics of spacetime

### Galilean transformations

A basic goal is to be able to compare measurements made by observers in relative motion. If there is an observer O in frame S who has measured the time and space coordinates of an event, assigning this event three Cartesian coordinates and the time as measured on his lattice of synchronized clocks (*x*, *y*, *z*, *t*) (see **Fig. 1-1**). A second observer O′ in a different frame S′ measures the same event in her coordinate system and her lattice of synchronized clocks (*x*′, *y*′, *z*′, *t*′). With inertial frames, neither observer is under acceleration, and a simple set of equations allows us to relate coordinates (*x*, *y*, *z*, *t*) to (*x*′, *y*′, *z*′, *t*′). Given that the two coordinate systems are in standard configuration, meaning that they are aligned with parallel (*x*, *y*, *z*) coordinates and that *t* = 0 when *t*′ = 0, the coordinate transformation is as follows:

$x'=x-vt$

$y'=y$

$z'=z$

$t'=t.$

Fig. 3-1 illustrates that in Newton's theory, time is universal, not the velocity of light. Consider the following thought experiment: The red arrow illustrates a train that is moving at 0.4 c with respect to the platform. Within the train, a passenger shoots a bullet with a speed of 0.4 c in the frame of the train. The blue arrow illustrates that a person standing on the train tracks measures the bullet as traveling at 0.8 c. This is in accordance with our naive expectations.

More generally, assuming that frame S′ is moving at velocity *v* with respect to frame S, then within frame S′, observer O′ measures an object moving with velocity *u*′. Velocity *u* with respect to frame S, since *x* = *ut*, *x*′ = *x* − *vt*, and *t* = *t*′, can be written as *x*′ = *ut* − *vt* = (*u* − *v*)*t* = (*u* − *v*)*t*′. This leads to *u*′ = *x*′/*t*′ and ultimately

$u'=u-v$

or

$u=u'+v,$

which is the common-sense **Galilean law for the addition of velocities**.

### Relativistic composition of velocities

The composition of velocities is quite different in relativistic spacetime. To reduce the complexity of the equations slightly, we introduce a common shorthand for the ratio of the speed of an object relative to light,

$\beta =v/c$

Fig. 3-2a illustrates a red train that is moving forward at a speed given by *v*/*c* = *β* = *s*/*a*. From the primed frame of the train, a passenger shoots a bullet with a speed given by *u*′/*c* = *β*′ = *n*/*m*, where the distance is measured along a line parallel to the red *x*′ axis rather than parallel to the black *x* axis. What is the composite velocity *u* of the bullet relative to the platform, as represented by the blue arrow? Referring to Fig. 3-2b:

1. From the platform, the composite speed of the bullet is given by *u* = *c*(*s* + *r*)/(*a* + *b*).
2. The two yellow triangles are similar because they are right triangles that share a common angle *α*. In the large yellow triangle, the ratio *s*/*a* = *v*/*c* = *β*.
3. The ratios of corresponding sides of the two yellow triangles are constant, so that *r*/*a* = *b*/*s* = *n*/*m* = *β*′. So *b* = *u*′*s*/*c* and *r* = *u*′*a*/*c*.
4. Substitute the expressions for *b* and *r* into the expression for *u* in step 1 to yield Einstein's formula for the addition of velocities: $u={v+u' \over 1+(vu'/c^{2})}.$

The relativistic formula for addition of velocities presented above exhibits several important features:

- If *u*′ and *v* are both very small compared with the speed of light, then the product *vu*′/*c*2 becomes vanishingly small, and the overall result becomes indistinguishable from the Galilean formula (Newton's formula) for the addition of velocities: *u* = *u*′ + *v*. The Galilean formula is a special case of the relativistic formula applicable to low velocities.
- If *u*′ is set equal to *c*, then the formula yields *u* = *c* regardless of the starting value of *v*. The velocity of light is the same for all observers regardless their motions relative to the emitting source.

### Time dilation and length contraction revisited

It is straightforward to obtain quantitative expressions for time dilation and length contraction. Fig. 3-3 is a composite image containing individual frames taken from two previous animations, simplified and relabeled for the purposes of this section.

To reduce the complexity of the equations slightly, there are a variety of different shorthand notations for *ct*:

$\mathrm {T} =ct$

and

$w=ct$

are common.

One also sees very frequently the use of the convention

$c=1.$

In Fig. 3-3a, segments *OA* and *OK* represent equal spacetime intervals. Time dilation is represented by the ratio *OB*/*OK*. The invariant hyperbola has the equation *w* = √*x*2 + *k*2 where *k* = *OK*, and the red line representing the world line of a particle in motion has the equation *w* = *x*/*β* = *xc*/*v*. A bit of algebraic manipulation yields ${\textstyle OB=OK/{\sqrt {1-v^{2}/c^{2}}}.}$

The expression involving the square root symbol appears very frequently in relativity, and one over the expression is called the Lorentz factor, denoted by the Greek letter gamma $\gamma$ :

$\gamma ={\frac {1}{\sqrt {1-v^{2}/c^{2}}}}={\frac {1}{\sqrt {1-\beta ^{2}}}}$

If *v* is greater than or equal to *c*, the expression for $\gamma$ becomes physically meaningless, implying that *c* is the maximum possible speed in nature. For any *v* greater than zero, the Lorentz factor will be greater than one, although the shape of the curve is such that for low speeds, the Lorentz factor is extremely close to one.

In Fig. 3-3b, segments *OA* and *OK* represent equal spacetime intervals. Length contraction is represented by the ratio *OB*/*OK*. The invariant hyperbola has the equation *x* = √*w*2 + *k*2, where *k* = *OK*, and the edges of the blue band representing the world lines of the endpoints of a rod in motion have slope 1/*β* = *c*/*v*. Event A has coordinates (*x*, *w*) = (*γk*, *γβk*). Since the tangent line through A and B has the equation *w* = (*x* − *OB*)/*β*, we have *γβk* = (*γk* − *OB*)/*β* and

$OB/OK=\gamma (1-\beta ^{2})={\frac {1}{\gamma }}$

### Lorentz transformations

The Galilean transformations and their consequent commonsense law of addition of velocities work well in our ordinary low-speed world of planes, cars and balls. Beginning in the mid-1800s, however, sensitive scientific instrumentation began finding anomalies that did not fit well with the ordinary addition of velocities.

Lorentz transformations are used to transform the coordinates of an event from one frame to another in special relativity.

The Lorentz factor appears in the Lorentz transformations:

${\begin{aligned}t'&=\gamma \left(t-{\frac {vx}{c^{2}}}\right)\\x'&=\gamma \left(x-vt\right)\\y'&=y\\z'&=z\end{aligned}}$

The inverse Lorentz transformations are:

${\begin{aligned}t&=\gamma \left(t'+{\frac {vx'}{c^{2}}}\right)\\x&=\gamma \left(x'+vt'\right)\\y&=y'\\z&=z'\end{aligned}}$

When *v* ≪ *c* and *x* is small enough, the *v*2/*c*2 and *vx*/*c*2 terms approach zero, and the Lorentz transformations approximate to the Galilean transformations.

$t'=\gamma (t-vx/c^{2}),$ $x'=\gamma (x-vt)$ etc., most often really mean $\Delta t'=\gamma (\Delta t-v\Delta x/c^{2}),$ $\Delta x'=\gamma (\Delta x-v\Delta t)$ etc. Although for brevity the Lorentz transformation equations are written without deltas, *x* means Δ*x*, etc. We are, in general, always concerned with the space and time *differences* between events.

Calling one set of transformations the normal Lorentz transformations and the other the inverse transformations is misleading, since there is no intrinsic difference between the frames. Different authors call one or the other set of transformations the "inverse" set. The forwards and inverse transformations are trivially related to each other, since the *S* frame can only be moving forwards or reverse with respect to *S*′. So inverting the equations simply entails switching the primed and unprimed variables and replacing *v* with −*v*.

**Example:** Terence and Stella are at an Earth-to-Mars space race. Terence is an official at the starting line, while Stella is a participant. At time *t* = *t*′ = 0, Stella's spaceship accelerates instantaneously to a speed of 0.5 *c*. The distance from Earth to Mars is 300 light-seconds (about 90.0×106 km). Terence observes Stella crossing the finish-line clock at *t* = 600.00 s. But Stella observes the time on her ship chronometer to be ⁠ $t^{\prime }=\gamma \left(t-vx/c^{2}\right)=519.62\ {\text{s}}$ ⁠ as she passes the finish line, and she calculates the distance between the starting and finish lines, as measured in her frame, to be 259.81 light-seconds (about 77.9×106 km). 1).

#### Deriving the Lorentz transformations

There have been many dozens of derivations of the Lorentz transformations since Einstein's original work in 1905, each with its particular focus. Although Einstein's derivation was based on the invariance of the speed of light, there are other physical principles that may serve as starting points. Ultimately, these alternative starting points can be considered different expressions of the underlying principle of locality, which states that the influence that one particle exerts on another can not be transmitted instantaneously.

The derivation given here and illustrated in Fig. 3-5 is based on one presented by Bais and makes use of previous results from the Relativistic Composition of Velocities, Time Dilation, and Length Contraction sections. Event P has coordinates (*w*, *x*) in the black "rest system" and coordinates (*w*′, *x*′) in the red frame that is moving with velocity parameter *β* = *v*/*c*. To determine *w*′ and *x*′ in terms of *w* and *x* (or the other way around) it is easier at first to derive the *inverse* Lorentz transformation.

1. There can be no such thing as length expansion/contraction in the transverse directions. *y'* must equal *y* and *z*′ must equal *z*, otherwise whether a fast moving 1 m ball could fit through a 1 m circular hole would depend on the observer. The first postulate of relativity states that all inertial frames are equivalent, and transverse expansion/contraction would violate this law.
2. From the drawing, *w* = *a* + *b* and *x* = *r* + *s*
3. From previous results using similar triangles, we know that *s*/*a* = *b*/*r* = *v*/*c* = *β*.
4. Because of time dilation, *a* = *γw′*
5. Substituting equation (4) into *s*/*a* = *β* yields *s* = *γw′β*.
6. Length contraction and similar triangles give us *r* = *γx′* and *b* = *βr* = *βγx′*
7. Substituting the expressions for *s*, *a*, *r* and *b* into the equations in Step 2 immediately yield ${\begin{aligned}w&=\gamma w'+\beta \gamma x'\\x&=\gamma x'+\beta \gamma w'\end{aligned}}$

The above equations are alternate expressions for the t and x equations of the inverse Lorentz transformation, as can be seen by substituting *ct* for *w*, *ct*′ for *w*′, and *v*/*c* for *β*. From the inverse transformation, the equations of the forwards transformation can be derived by solving for *t*′ and *x*′.

#### Linearity of the Lorentz transformations

The Lorentz transformations have a mathematical property called linearity, since *x*′ and *t*′ are obtained as linear combinations of *x* and *t*, with no higher powers involved. The linearity of the transformation reflects a fundamental property of spacetime that was tacitly assumed in the derivation, namely, that the properties of inertial frames of reference are independent of location and time. In the absence of gravity, spacetime looks the same everywhere. All inertial observers will agree on what constitutes accelerating and non-accelerating motion. Any one observer can use her own measurements of space and time, but there is nothing absolute about them. Another observer's conventions will do just as well.

A result of linearity is that if two Lorentz transformations are applied sequentially, the result is also a Lorentz transformation.

**Example:** Terence observes Stella speeding away from him at 0.500 *c*, and he can use the Lorentz transformations with *β* = 0.500 to relate Stella's measurements to his own. Stella, in her frame, observes Ursula traveling away from her at 0.250 *c*, and she can use the Lorentz transformations with *β* = 0.250 to relate Ursula's measurements with her own. Because of the linearity of the transformations and the relativistic composition of velocities, Terence can use the Lorentz transformations with *β* = 0.666 to relate Ursula's measurements with his own.

### Doppler effect

The Doppler effect is the change in frequency or wavelength of a wave for a receiver and source in relative motion. For simplicity, we consider here two basic scenarios: (1) The motions of the source and/or receiver are exactly along the line connecting them (longitudinal Doppler effect), and (2) the motions are at right angles to the said line (transverse Doppler effect). We are ignoring scenarios where they move along intermediate angles.

#### Longitudinal Doppler effect

The classical Doppler analysis deals with waves that are propagating in a medium, such as sound waves or water ripples, and which are transmitted between sources and receivers that are moving towards or away from each other. The analysis of such waves depends on whether the source, the receiver, or both are moving relative to the medium. Given the scenario where the receiver is stationary with respect to the medium, and the source is moving directly away from the receiver at a speed of *vs* for a velocity parameter of *βs*, the wavelength is increased, and the observed frequency *f* is given by

$f={\frac {1}{1+\beta _{s}}}f_{0}$

On the other hand, given the scenario where source is stationary, and the receiver is moving directly away from the source at a speed of *vr* for a velocity parameter of *βr*, the wavelength is *not* changed, but the transmission velocity of the waves relative to the receiver is decreased, and the observed frequency *f* is given by

$f=(1-\beta _{r})f_{0}$

Light, unlike sound or water ripples, does not propagate through a medium, and there is no distinction between a source moving away from the receiver or a receiver moving away from the source. Fig. 3-6 illustrates a relativistic spacetime diagram showing a source separating from the receiver with a velocity parameter $\beta ,$ so that the separation between source and receiver at time w is $\beta w$ . Because of time dilation, $w=\gamma w'.$ Since the slope of the green light ray is −1, $T=w+\beta w=\gamma w'(1+\beta ).$ Hence, the relativistic Doppler effect is given by

$f={\sqrt {\frac {1-\beta }{1+\beta }}}\,f_{0}.$

#### Transverse Doppler effect

Suppose that a source and a receiver, both approaching each other in uniform inertial motion along non-intersecting lines, are at their closest approach to each other. It would appear that the classical analysis predicts that the receiver detects no Doppler shift. Due to subtleties in the analysis, that expectation is not necessarily true. Nevertheless, when appropriately defined, transverse Doppler shift is a relativistic effect that has no classical analog. The subtleties are these:

- Fig. 3-7a. What is the frequency measurement when the receiver is geometrically at its closest approach to the source? This scenario is most easily analyzed from the frame S′ of the source.
- Fig. 3-7b. What is the frequency measurement when the receiver *sees* the source as being closest to it? This scenario is most easily analyzed from the frame S of the receiver.

Two other scenarios are commonly examined in discussions of transverse Doppler shift:

- Fig. 3-7c. If the receiver is moving in a circle around the source, what frequency does the receiver measure?
- Fig. 3-7d. If the source is moving in a circle around the receiver, what frequency does the receiver measure?

In scenario (a), the point of closest approach is frame-independent and represents the moment where there is no change in distance versus time (i.e. dr/dt = 0 where *r* is the distance between receiver and source) and hence no longitudinal Doppler shift. The source observes the receiver as being illuminated by light of frequency *f*′, but also observes the receiver as having a time-dilated clock. In frame S, the receiver is therefore illuminated by blueshifted light of frequency

$f=f'\gamma =f'/{\sqrt {1-\beta ^{2}}}$

In scenario (b) the illustration shows the receiver being illuminated by light from when the source was closest to the receiver, even though the source has moved on. Because the source's clocks are time dilated as measured in frame S, and since dr/dt was equal to zero at this point, the light from the source, emitted from this closest point, is redshifted with frequency

$f=f'/\gamma =f'{\sqrt {1-\beta ^{2}}}$

Scenarios (c) and (d) can be analyzed by simple time dilation arguments. In (c), the receiver observes light from the source as being blueshifted by a factor of $\gamma$ , and in (d), the light is redshifted. The only seeming complication is that the orbiting objects are in accelerated motion. However, if an inertial observer looks at an accelerating clock, only the clock's instantaneous speed is important when computing time dilation. (The converse, however, is not true.) Most reports of transverse Doppler shift refer to the effect as a redshift and analyze the effect in terms of scenarios (b) or (d).

### Energy and momentum

#### Extending momentum to four dimensions

In classical mechanics, the state of motion of a particle is characterized by its mass and its velocity. Linear momentum, the product of a particle's mass and velocity, is a vector quantity, possessing the same direction as the velocity: ***p*** = *m**v***. It is a *conserved* quantity, meaning that if a closed system is not affected by external forces, its total linear momentum cannot change.

In relativistic mechanics, the momentum vector is extended to four dimensions. Added to the momentum vector is a time component that allows the spacetime momentum vector to transform like the spacetime position vector ⁠ $(x,t)$ ⁠. In exploring the properties of the spacetime momentum, we start, in Fig. 3-8a, by examining what a particle looks like at rest. In the rest frame, the spatial component of the momentum is zero, i.e. *p* = 0, but the time component equals *mc*.

We can obtain the transformed components of this vector in the moving frame by using the Lorentz transformations, or we can read it directly from the figure because we know that ⁠ $(mc)^{\prime }=\gamma mc$ ⁠ and ⁠ $p^{\prime }=-\beta \gamma mc$ ⁠, since the red axes are rescaled by gamma. Fig. 3-8b illustrates the situation as it appears in the moving frame. It is apparent that the space and time components of the four-momentum go to infinity as the velocity of the moving frame approaches *c*.

We will use this information shortly to obtain an expression for the four-momentum.

#### Momentum of light

Light particles, or photons, travel at the speed of *c*, the constant that is conventionally known as the *speed of light*. This statement is not a tautology, since many modern formulations of relativity do not start with constant speed of light as a postulate. Photons therefore propagate along a lightlike world line and, in appropriate units, have equal space and time components for every observer.

A consequence of Maxwell's theory of electromagnetism is that light carries energy and momentum, and that their ratio is a constant: ⁠ $E/p=c$ ⁠. Rearranging, ⁠ $E/c=p$ ⁠, and since for photons, the space and time components are equal, *E*/*c* must therefore be equated with the time component of the spacetime momentum vector.

Photons travel at the speed of light, yet have finite momentum and energy. For this to be so, the mass term in *γmc* must be zero, meaning that photons are massless particles. Infinity times zero is an ill-defined quantity, but *E*/*c* is well-defined.

By this analysis, if the energy of a photon equals *E* in the rest frame, it equals ⁠ $E^{\prime }=(1-\beta )\gamma E$ ⁠ in a moving frame. This result can be derived by inspection of Fig. 3-9 or by application of the Lorentz transformations, and is consistent with the analysis of Doppler effect given previously.

#### Mass–energy relationship

Consideration of the interrelationships between the various components of the relativistic momentum vector led Einstein to several important conclusions.

- In the low speed limit as *β* = *v*/*c* approaches zero, γ approaches 1, so the spatial component of the relativistic momentum ⁠ $\beta \gamma mc=\gamma mv$ ⁠ approaches *mv*, the classical term for momentum. Following this perspective, *γm* can be interpreted as a relativistic generalization of *m*. Einstein proposed that the *relativistic mass* of an object increases with velocity according to the formula ⁠ $m_{\text{rel}}=\gamma m$ ⁠.
- Likewise, comparing the time component of the relativistic momentum with that of the photon, ⁠ $\gamma mc=m_{\text{rel}}c=E/c$ ⁠, so that Einstein arrived at the relationship ⁠ $E=m_{\text{rel}}c^{2}$ ⁠. Simplified to the case of zero velocity, this is Einstein's equation relating energy and mass.

Another way of looking at the relationship between mass and energy is to consider a series expansion of *γmc*2 at low velocity: ${\begin{aligned}E&=\gamma mc^{2}={\frac {mc^{2}}{\sqrt {1-\beta ^{2}}}}\\&=mc^{2}+{\frac {1}{2}}mv^{2}+\cdots \end{aligned}}$ The second term is just an expression for the kinetic energy of the particle. Mass indeed appears to be another form of energy.

The concept of relativistic mass that Einstein introduced in 1905, *m*rel, although amply validated every day in particle accelerators around the globe (or indeed in any instrumentation whose use depends on high velocity particles, such as electron microscopes, old-fashioned color television sets, etc.), has nevertheless not proven to be a *fruitful* concept in physics in the sense that it is not a concept that has served as a basis for other theoretical development. Relativistic mass, for instance, plays no role in general relativity.

For this reason, as well as for pedagogical concerns, most physicists currently prefer a different terminology when referring to the relationship between mass and energy. "Relativistic mass" is a deprecated term. The term "mass" by itself refers to the rest mass or invariant mass, and is equal to the invariant length of the relativistic momentum vector. Expressed as a formula,

$E^{2}-p^{2}c^{2}=m_{\text{rest}}^{2}c^{4}$

This formula applies to all particles, massless as well as massive. For photons where *m*rest equals zero, it yields, ⁠ $E=\pm pc$ ⁠.

#### Four-momentum

Because of the close relationship between mass and energy, the four-momentum (also called 4-momentum) is also called the energy–momentum 4-vector. Using an uppercase *P* to represent the four-momentum and a lowercase ***p*** to denote the spatial momentum, the four-momentum may be written as

$P\equiv (E/c,{\vec {p}})=(E/c,p_{x},p_{y},p_{z})$

or alternatively,

$P\equiv (E,{\vec {p}})=(E,p_{x},p_{y},p_{z})$

using the convention that

$c=1.$

### Conservation laws

In physics, conservation laws state that certain particular measurable properties of an isolated physical system do not change as the system evolves over time. In 1915, Emmy Noether discovered that underlying each conservation law is a fundamental symmetry of nature. The fact that physical processes do not care *where* in space they take place (space translation symmetry) yields conservation of momentum, the fact that such processes do not care *when* they take place (time translation symmetry) yields conservation of energy, and so on. In this section, we examine the Newtonian views of conservation of mass, momentum and energy from a relativistic perspective.

#### Total momentum

To understand how the Newtonian view of conservation of momentum needs to be modified in a relativistic context, we examine the problem of two colliding bodies limited to a single dimension.

In Newtonian mechanics, two extreme cases of this problem may be distinguished yielding mathematics of minimum complexity:

1. The two bodies rebound from each other in a completely elastic collision.
2. The two bodies stick together and continue moving as a single particle. This second case is the case of completely inelastic collision.

For both cases (1) and (2), momentum, mass, and total energy are conserved. However, kinetic energy is not conserved in cases of inelastic collision. A certain fraction of the initial kinetic energy is converted to heat.

In case (2), two masses with momentums ⁠ ${\boldsymbol {p}}_{\boldsymbol {1}}=m_{1}{\boldsymbol {v}}_{\boldsymbol {1}}$ ⁠ and ⁠ ${\boldsymbol {p}}_{\boldsymbol {2}}=m_{2}{\boldsymbol {v}}_{\boldsymbol {2}}$ ⁠ collide to produce a single particle of conserved mass ⁠ $m=m_{1}+m_{2}$ ⁠ traveling at the center of mass velocity of the original system, ${\boldsymbol {v_{cm}}}=\left(m_{1}{\boldsymbol {v_{1}}}+m_{2}{\boldsymbol {v_{2}}}\right)/\left(m_{1}+m_{2}\right)$ . The total momentum ⁠ ${\boldsymbol {p=p_{1}+p_{2}}}$ ⁠ is conserved.

Fig. 3-10 illustrates the inelastic collision of two particles from a relativistic perspective. The time components ⁠ $E_{1}/c$ ⁠ and ⁠ $E_{2}/c$ ⁠ add up to total *E/c* of the resultant vector, meaning that energy is conserved. Likewise, the space components ⁠ ${\boldsymbol {p_{1}}}$ ⁠ and ⁠ ${\boldsymbol {p_{2}}}$ ⁠ add up to form *p* of the resultant vector. The four-momentum is, as expected, a conserved quantity. However, the invariant mass of the fused particle, given by the point where the invariant hyperbola of the total momentum intersects the energy axis, is not equal to the sum of the invariant masses of the individual particles that collided. Indeed, it is larger than the sum of the individual masses: ⁠ $m>m_{1}+m_{2}$ ⁠.

Looking at the events of this scenario in reverse sequence, we see that non-conservation of mass is a common occurrence: when an unstable elementary particle spontaneously decays into two lighter particles, total energy is conserved, but the mass is not. Part of the mass is converted into kinetic energy.

#### Choice of reference frames

Figure 3-11.

(above)

Lab Frame

.

(right)

Center of Momentum Frame

.

The freedom to choose any frame in which to perform an analysis allows us to pick one which may be particularly convenient. For analysis of momentum and energy problems, the most convenient frame is usually the "center-of-momentum frame" (also called the zero-momentum frame, or COM frame). This is the frame in which the space component of the system's total momentum is zero. Fig. 3-11 illustrates the breakup of a high speed particle into two daughter particles. In the lab frame, the daughter particles are preferentially emitted in a direction oriented along the original particle's trajectory. In the COM frame, however, the two daughter particles are emitted in opposite directions, although their masses and the magnitude of their velocities are generally not the same.

#### Energy and momentum conservation

In a Newtonian analysis of interacting particles, transformation between frames is simple because all that is necessary is to apply the Galilean transformation to all velocities. Since ⁠ $v'=v-u$ ⁠, the momentum ⁠ $p'=p-mu$ ⁠. If the total momentum of an interacting system of particles is observed to be conserved in one frame, it will likewise be observed to be conserved in any other frame.

Conservation of momentum in the COM frame amounts to the requirement that *p* = 0 both before and after collision. In the Newtonian analysis, conservation of mass dictates that ⁠ $m=m_{1}+m_{2}$ ⁠. In the simplified, one-dimensional scenarios that we have been considering, only one additional constraint is necessary before the outgoing momenta of the particles can be determined—an energy condition. In the one-dimensional case of a completely elastic collision with no loss of kinetic energy, the outgoing velocities of the rebounding particles in the COM frame will be precisely equal and opposite to their incoming velocities. In the case of a completely inelastic collision with total loss of kinetic energy, the outgoing velocities of the rebounding particles will be zero.

Newtonian momenta, calculated as ⁠ $p=mv$ ⁠, fail to behave properly under Lorentzian transformation. The linear transformation of velocities ⁠ $v'=v-u$ ⁠ is replaced by the highly nonlinear ⁠ $v^{\prime }=(v-u)/(1-{vu}/{c^{2}})$ ⁠ so that a calculation demonstrating conservation of momentum in one frame will be invalid in other frames. Einstein was faced with either having to give up conservation of momentum, or to change the definition of momentum. This second option was what he chose.

Figure 3-12a. Energy–momentum diagram for decay of a charged pion.

Figure 3-12b. Graphing calculator analysis of charged pion decay.

The relativistic conservation law for energy and momentum replaces the three classical conservation laws for energy, momentum and mass. Mass is no longer conserved independently, because it has been subsumed into the total relativistic energy. This makes the relativistic conservation of energy a simpler concept than in nonrelativistic mechanics, because the total energy is conserved without any qualifications. Kinetic energy converted into heat or internal potential energy shows up as an increase in mass.

Example:

Because of the equivalence of mass and energy, elementary particle masses are customarily stated in energy units, where

1 MeV = 10

6

electron volts. A charged pion is a particle of mass 139.57 MeV (approx. 273 times the electron mass). It is unstable, and decays into a muon of mass 105.66 MeV (approx. 207 times the electron mass) and an antineutrino, which has an almost negligible mass. The difference between the pion mass and the muon mass is 33.91 MeV.

π

−

→

μ

−

+

ν

μ

Fig. 3-12a illustrates the energy–momentum diagram for this decay reaction in the rest frame of the pion. Because of its negligible mass, a neutrino travels at very nearly the speed of light. The relativistic expression for its energy, like that of the photon, is ⁠ $E_{v}=pc,$ ⁠ which is also the value of the space component of its momentum. To conserve momentum, the muon has the same value of the space component of the neutrino's momentum, but in the opposite direction.

Algebraic analyses of the energetics of this decay reaction are available online,

so Fig. 3-12b presents instead a graphing calculator solution. The energy of the neutrino is 29.79 MeV, and the energy of the muon is

33.91 MeV − 29.79 MeV = 4.12 MeV

. Most of the energy is carried off by the near-zero-mass neutrino.


## Introduction to curved spacetime

Newton's theories assumed that motion takes place against the backdrop of a rigid Euclidean reference frame that extends throughout all space and all time. Gravity is mediated by a mysterious force, acting instantaneously across a distance, whose actions are independent of the intervening space. In contrast, Einstein denied that there is any background Euclidean reference frame that extends throughout space. Nor is there any such thing as a force of gravitation, only the structure of spacetime itself.

In spacetime terms, the path of a satellite orbiting the Earth is not dictated by the distant influences of the Earth, Moon and Sun. Instead, the satellite moves through space only in response to local conditions. Since spacetime is everywhere locally flat when considered on a sufficiently small scale, the satellite is always following a straight line in its local inertial frame. We say that the satellite always follows along the path of a geodesic. No evidence of gravitation can be discovered following alongside the motions of a single particle.

In any analysis of spacetime, evidence of gravitation requires that one observe the relative accelerations of *two* bodies or two separated particles. In Fig. 1, two separated particles, free-falling in the gravitational field of the Earth, exhibit tidal accelerations due to local inhomogeneities in the gravitational field such that each particle follows a different path through spacetime. The tidal accelerations that these particles exhibit with respect to each other do not require forces for their explanation. Rather, Einstein described them in terms of the geometry of spacetime, i.e. the curvature of spacetime. These tidal accelerations are strictly local. It is the cumulative total effect of many local manifestations of curvature that result in the *appearance* of a gravitational force acting at a long range from Earth.

Different observers viewing the scenarios presented in this figure interpret the scenarios differently depending on their knowledge of the situation. (i) A first observer, at the

center of mass

of particles 2 and 3 but unaware of the large mass 1, concludes that a force of repulsion exists between the particles in scenario A while a force of attraction exists between the particles in scenario B. (ii) A second observer, aware of the large mass 1, smiles at the first reporter's naiveté. This second observer knows that in reality, the apparent forces between particles 2 and 3 really represent tidal effects resulting from their differential attraction by mass 1. (iii) A third observer, trained in general relativity, knows that there are, in fact, no forces at all acting between the three objects. Rather, all three objects move along geodesics in spacetime.

Two central propositions underlie general relativity.

- The first crucial concept is coordinate independence: The laws of physics cannot depend on what coordinate system one uses. This is a major extension of the principle of relativity from the version used in special relativity, which states that the laws of physics must be the same for every observer moving in non-accelerated (inertial) reference frames. In general relativity, to use Einstein's own (translated) words, "the laws of physics must be of such a nature that they apply to systems of reference in any kind of motion." This leads to an immediate issue: In accelerated frames, one feels forces that seemingly would enable one to assess one's state of acceleration in an absolute sense. Einstein resolved this problem through the principle of equivalence.

- The equivalence principle states that in any sufficiently small region of space, the effects of gravitation are the same as those from acceleration. In Fig. 2, person A is in a spaceship, far from any massive objects, that undergoes a uniform acceleration of *g*. Person B is in a box resting on Earth. Provided that the spaceship is sufficiently small so that tidal effects are non-measurable (given the sensitivity of current gravity measurement instrumentation, A and B presumably should be Lilliputians), there are no experiments that A and B can perform which will enable them to tell which setting they are in. An alternative expression of the equivalence principle is to note that in Newton's universal law of gravitation, *F = GMm*g*/r*2 = *m*g*g* and in Newton's second law, *F = m*i*a*, there is no *a priori* reason why the gravitational mass *m*g should be equal to the inertial mass *m*i. The equivalence principle states that these two masses are identical.

To go from the elementary description above of curved spacetime to a complete description of gravitation requires tensor calculus and differential geometry, topics both requiring considerable study. Without these mathematical tools, it is possible to write *about* general relativity, but it is not possible to demonstrate any non-trivial derivations.
