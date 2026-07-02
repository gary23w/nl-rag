---
title: "Special relativity (part 2/3)"
source: https://en.wikipedia.org/wiki/Special_relativity
domain: special-relativity
license: CC-BY-SA-4.0
tags: special relativity, lorentz transformation, time dilation, mass-energy equivalence
fetched: 2026-07-02
part: 2/3
---

## Consequences derived from the Lorentz transformation

The consequences of special relativity can be derived from the Lorentz transformation equations. These transformations, and hence special relativity, lead to different physical predictions than those of Newtonian mechanics at all relative velocities, and most pronounced when relative velocities become comparable to the speed of light. The speed of light is so much larger than anything most humans encounter that some of the effects predicted by relativity are initially counterintuitive.

### Invariant interval

In Galilean relativity, the spatial separation, (⁠ $\Delta r$ ⁠), and the temporal separation, (⁠ $\Delta t$ ⁠), between two events are independent invariants, the values of which do not change when observed from different frames of reference. In special relativity, however, the interweaving of spatial and temporal coordinates generates the concept of an **invariant interval**, denoted as ⁠ $\Delta s^{2}$ ⁠: $\Delta s^{2}\;{\overset {\text{def}}{=}}\;c^{2}\Delta t^{2}-(\Delta x^{2}+\Delta y^{2}+\Delta z^{2})$ In considering the physical significance of ⁠ $\Delta s^{2}$ ⁠, there are three cases:

- **Δs2 > 0:** In this case, the two events are separated by more time than space, and they are hence said to be *timelike* separated. This implies that ⁠ $\vert \Delta x/\Delta t\vert <c$ ⁠, and given the Lorentz transformation ⁠ $\Delta x'=\gamma \ (\Delta x-v\ \Delta t)$ ⁠, it is evident that there exists a v less than c for which $\Delta x'=0$ (in particular, ⁠ $v=\Delta x/\Delta t$ ⁠). In other words, given two events that are timelike separated, it is possible to find a frame in which the two events happen at the same place. In this frame, the separation in time, ⁠ $\Delta s/c$ ⁠, is called the *proper time*.
- **Δs2 < 0:** In this case, the two events are separated by more space than time, and they are hence said to be *spacelike* separated. This implies that ⁠ $\vert \Delta x/\Delta t\vert >c$ ⁠, and given the Lorentz transformation ⁠ $\Delta t'=\gamma \ (\Delta t-v\Delta x/c^{2})$ ⁠, there exists a v less than c for which $\Delta t'=0$ (in particular, ⁠ $v=c^{2}\Delta t/\Delta x$ ⁠). In other words, given two events that are spacelike separated, it is possible to find a frame in which the two events happen at the same time. In this frame, the separation in space, ⁠ $\textstyle {\sqrt {-\Delta s^{2}}}$ ⁠, is called the *proper distance*, or *proper length*. For values of v greater than and less than ⁠ $c^{2}\Delta t/\Delta x$ ⁠, the sign of $\Delta t'$ changes, meaning that the temporal order of spacelike-separated events changes depending on the frame in which the events are viewed. But the temporal order of timelike-separated events is absolute, since the only way that v could be greater than $c^{2}\Delta t/\Delta x$ would be if ⁠ $v>c$ ⁠.
- **Δs2 = 0:** In this case, the two events are said to be *lightlike* separated. This implies that ⁠ $\vert \Delta x/\Delta t\vert =c$ ⁠, and this relationship is frame independent due to the invariance of ⁠ $s^{2}$ ⁠. From this, we observe that the speed of light is c in every inertial frame. In other words, starting from the assumption of universal Lorentz covariance, the constant speed of light is a derived result, rather than a postulate as in the two-postulates formulation of the special theory.

The interweaving of space and time revokes the implicitly assumed concepts of absolute simultaneity and synchronization across non-comoving frames.

The form of ⁠ $\Delta s^{2}$ ⁠, being the *difference* of the squared time lapse and the squared spatial distance, demonstrates a fundamental discrepancy between Euclidean and spacetime distances. The invariance of Δ*s*2 under standard Lorentz transformation is analogous to the invariance of squared distances Δ*r*2 under rotations in Euclidean space. Although space and time have an equal *footing* in relativity, the minus sign in front of the spatial terms marks space and time as being of essentially different character. They are not the same. Because it treats time differently than it treats the 3 spatial dimensions, Minkowski space differs from four-dimensional Euclidean space. The invariance of this interval is a property of the *general* Lorentz transform (also called the Poincaré transformation), making it an isometry of spacetime. The general Lorentz transform extends the standard Lorentz transform (which deals with translations without rotation, that is, Lorentz boosts, in the x-direction) with all other translations, reflections, and rotations between any Cartesian inertial frame.

In the analysis of simplified scenarios, such as spacetime diagrams, a reduced-dimensionality form of the invariant interval is often employed: $\Delta s^{2}\,=\,c^{2}\Delta t^{2}-\Delta x^{2}$

Demonstrating that the interval is invariant is straightforward for the reduced-dimensionality case and with frames in standard configuration: ${\begin{aligned}c^{2}\Delta t^{2}-\Delta x^{2}&=c^{2}\gamma ^{2}\left(\Delta t'+{\dfrac {v\Delta x'}{c^{2}}}\right)^{2}-\gamma ^{2}\ (\Delta x'+v\Delta t')^{2}\\&=\gamma ^{2}\left(c^{2}\Delta t'^{\,2}+2v\Delta x'\Delta t'+{\dfrac {v^{2}\Delta x'^{\,2}}{c^{2}}}\right)-\gamma ^{2}\ (\Delta x'^{\,2}+2v\Delta x'\Delta t'+v^{2}\Delta t'^{\,2})\\&=\gamma ^{2}c^{2}\Delta t'^{\,2}-\gamma ^{2}v^{2}\Delta t'^{\,2}-\gamma ^{2}\Delta x'^{\,2}+\gamma ^{2}{\dfrac {v^{2}\Delta x'^{\,2}}{c^{2}}}\\&=\gamma ^{2}c^{2}\Delta t'^{\,2}\left(1-{\dfrac {v^{2}}{c^{2}}}\right)-\gamma ^{2}\Delta x'^{\,2}\left(1-{\dfrac {v^{2}}{c^{2}}}\right)\\&=c^{2}\Delta t'^{\,2}-\Delta x'^{\,2}\end{aligned}}$

The value of $\Delta s^{2}$ is hence independent of the frame in which it is measured.

### Relativity of simultaneity

Consider two events happening in two different locations that occur simultaneously in the reference frame of one inertial observer. They may occur non-simultaneously in the reference frame of another inertial observer (lack of absolute simultaneity).

From **Equation 3** (the forward Lorentz transformation in terms of coordinate differences) $\Delta t'=\gamma \left(\Delta t-{\frac {v\,\Delta x}{c^{2}}}\right)$

It is clear that the two events that are simultaneous in frame *S* (satisfying Δ*t* = 0), are not necessarily simultaneous in another inertial frame *S*′ (satisfying Δ*t*′ = 0). Only if these events are additionally co-local in frame *S* (satisfying Δ*x* = 0), will they be simultaneous in another frame *S*′.

The Sagnac effect can be considered a manifestation of the relativity of simultaneity for local inertial frames comoving with a rotating Earth. Instruments based on the Sagnac effect for their operation, such as ring laser gyroscopes and fiber optic gyroscopes, are capable of extreme levels of sensitivity.

### Time dilation

The time lapse between two events is not invariant from one observer to another, but is dependent on the relative speeds of the observers' reference frames.

Suppose a clock is at rest in the unprimed system *S*. The location of the clock on two different ticks is then characterized by Δ*x* = 0. To find the relation between the times between these ticks as measured in both systems, **Equation 3** can be used to find:

$\Delta t'=\gamma \,\Delta t$

for events satisfying

$\Delta x=0\ .$

This shows that the time (Δ*t*′) between the two ticks as seen in the frame in which the clock is moving (*S*′), is *longer* than the time (Δ*t*) between these ticks as measured in the rest frame of the clock (*S*). Time dilation explains a number of physical phenomena; for example, the lifetime of high speed muons created by the collision of cosmic rays with particles in the Earth's outer atmosphere and moving towards the surface is greater than the lifetime of slowly moving muons, created and decaying in a laboratory.

Whenever one hears a statement to the effect that "moving clocks run slow", one should envision an inertial reference frame thickly populated with identical, synchronized clocks. As a moving clock travels through this array, its reading at any particular point is compared with a stationary clock at the same point.

The measurements obtained from direct observation of a moving clock would be delayed by the finite speed of light, i.e. the times seen would be distorted by the Doppler effect. Measurements of relativistic effects must always be understood as having been made after finite speed-of-light effects have been factored out.

#### Langevin's light-clock

Paul Langevin, an early proponent of the theory of relativity, did much to popularize the theory in the face of resistance by many physicists to Einstein's revolutionary concepts. Among his numerous contributions to the foundations of special relativity were independent work on the mass–energy relationship, a thorough examination of the twin paradox, and investigations into rotating coordinate systems. His name is frequently attached to a hypothetical construct called a "light-clock" (originally developed by Lewis and Tolman in 1909), which he used to perform a novel derivation of the Lorentz transformation.

A light-clock is imagined to be a box of perfectly reflecting walls wherein a light signal reflects back and forth from opposite faces. The concept of time dilation is frequently taught using a light-clock that is traveling in uniform inertial motion perpendicular to a line connecting the two mirrors. (Langevin himself made use of a light-clock oriented parallel to its line of motion.)

Consider the scenario illustrated in Fig. 4-3A. Observer A holds a light-clock of length L as well as an electronic timer with which she measures how long it takes a pulse to make a round trip up and down along the light-clock. Although observer A is traveling rapidly along a train, from her point of view the emission and receipt of the pulse occur at the same place, and she measures the interval using a single clock located at the precise position of these two events. For the interval between these two events, observer A finds ⁠ $t_{\text{A}}=2L/c$ ⁠. A time interval measured using a single clock that is motionless in a particular reference frame is called a *proper time interval*.

Fig. 4-3B illustrates these same two events from the standpoint of observer B, who is parked by the tracks as the train goes by at a speed of ⁠ v ⁠. Instead of making straight up-and-down motions, observer B sees the pulses moving along a zig-zag line. However, because of the postulate of the constancy of the speed of light, the speed of the pulses along these diagonal lines is the same c that observer A saw for her up-and-down pulses. B measures the speed of the vertical component of these pulses as ${\textstyle \pm {\sqrt {c^{2}-v^{2}}},}$ so that the total round-trip time of the pulses is ${\textstyle t_{\text{B}}=2L{\big /}{\sqrt {c^{2}-v^{2}}}={}}$ ⁠ $\textstyle t_{\text{A}}{\big /}{\sqrt {1-v^{2}/c^{2}}}$ ⁠. Note that for observer B, the emission and receipt of the light pulse occurred at different places, and he measured the interval using two stationary and synchronized clocks located at two different positions in his reference frame. The interval that B measured was therefore *not* a proper time interval because he did not measure it with a single resting clock.

#### Reciprocal time dilation

In the above description of the Langevin light-clock, the labeling of one observer as stationary and the other as in motion was completely arbitrary. One could just as well have observer B carrying the light-clock and moving at a speed of v to the left, in which case observer A would perceive B's clock as running slower than her local clock.

There is no paradox here, because there is no independent observer C who will agree with both A and B. Observer C necessarily makes his measurements from his own reference frame. If that reference frame coincides with A's reference frame, then C will agree with A's measurement of time. If C's reference frame coincides with B's reference frame, then C will agree with B's measurement of time. If C's reference frame coincides with neither A's frame nor B's frame, then C's measurement of time will disagree with *both* A's and B's measurement of time.

### Twin paradox

The reciprocity of time dilation between two observers in separate inertial frames leads to the so-called twin paradox, articulated in its present form by Langevin in 1911. Langevin imagined an adventurer wishing to explore the future of the Earth. This traveler boards a projectile capable of traveling at 99.995% of the speed of light. After making a round-trip journey to and from a nearby star lasting only two years of his own life, he returns to an Earth that is two hundred years older.

This result appears puzzling because both the traveler and an Earthbound observer would see the other as moving, and so, because of the reciprocity of time dilation, one might initially expect that each should have found the other to have aged less. In reality, there is no paradox at all, because in order for the two observers to perform side-by-side comparisons of their elapsed proper times, the symmetry of the situation must be broken: At least one of the two observers must change their state of motion to match that of the other.

Knowing the general resolution of the paradox, however, does not immediately yield the ability to calculate correct quantitative results. Many solutions to this puzzle have been provided in the literature and have been reviewed in the Twin paradox article. We will examine in the following one such solution to the paradox.

Our basic aim will be to demonstrate that, after the trip, both twins are in perfect agreement about who aged by how much, regardless of their different experiences. Fig 4-4 illustrates a scenario where the traveling twin flies at 0.6 c to and from a star 3 ly distant. During the trip, each twin sends yearly time signals (measured in their own proper times) to the other. After the trip, the cumulative counts are compared. On the outward phase of the trip, each twin receives the other's signals at the lowered rate of ⁠ $\textstyle f'=f{\sqrt {(1-\beta )/(1+\beta )}}$ ⁠. Initially, the situation is perfectly symmetric: note that each twin receives the other's one-year signal at two years measured on their own clock. The symmetry is broken when the traveling twin turns around at the four-year mark as measured by her clock. During the remaining four years of her trip, she receives signals at the enhanced rate of ⁠ $\textstyle f''=f{\sqrt {(1+\beta )/(1-\beta )}}$ ⁠. The situation is quite different with the stationary twin. Because of light-speed delay, he does not see his sister turn around until eight years have passed on his own clock. Thus, he receives enhanced-rate signals from his sister for only a relatively brief period. Although the twins disagree in their respective measures of total time, we see in the following table, as well as by simple observation of the Minkowski diagram, that each twin is in total agreement with the other as to the total number of signals sent from one to the other. There is hence no paradox.

| Item | Measured by the stay-at-home | Fig 4-4 | Measured by the traveler | Fig 4-4 |
|---|---|---|---|---|
| Total time of trip | $T={\frac {2L}{v}}$ | 10 yr | $T'={\frac {2L}{\gamma v}}$ | 8 yr |
| Total number of pulses sent | $fT={\frac {2fL}{v}}$ | 10 | $fT'={\frac {2fL}{\gamma v}}$ | 8 |
| Time when traveler's turnaround is **detected** | $t_{1}={\frac {L}{v}}+{\frac {L}{c}}$ | 8 yr | $t_{1}'={\frac {L}{\gamma v}}$ | 4 yr |
| Number of pulses received at initial $f'$ rate | $f't_{1}$ $={\frac {fL}{v}}(1+\beta )\left({\frac {1-\beta }{1+\beta }}\right)^{1/2}$ $={\frac {fL}{v}}(1-\beta ^{2})^{1/2}$ | 4 | $f't_{1}'$ $={\frac {fL}{v}}(1-\beta ^{2})^{1/2}\left({\frac {1-\beta }{1+\beta }}\right)^{1/2}$ $={\frac {fL}{v}}(1-\beta )$ | 2 |
| Time for remainder of trip | $t_{2}={\frac {L}{v}}-{\frac {L}{c}}$ | 2 yr | $t_{2}'={\frac {L}{\gamma v}}$ | 4 yr |
| Number of signals received at final $f''$ rate | $f''t_{2}$ $={\frac {fL}{v}}(1-\beta )\left({\frac {1+\beta }{1-\beta }}\right)^{1/2}$ $={\frac {fL}{v}}(1-\beta ^{2})^{1/2}$ | 4 | $f''t_{2}'$ $={\frac {fL}{v}}(1-\beta ^{2})^{1/2}\left({\frac {1+\beta }{1-\beta }}\right)^{1/2}$ $={\frac {fL}{v}}(1+\beta )$ | 8 |
| Total number of received pulses | ${\frac {2fL}{v}}(1-\beta ^{2})^{1/2}$ $={\frac {2fL}{\gamma v}}$ | 8 | ${\frac {2fL}{v}}$ | 10 |
| Twin's calculation as to how much the ***other*** twin should have aged | $T'={\frac {2L}{\gamma v}}$ | 8 yr | $T={\frac {2L}{v}}$ | 10 yr |

### Length contraction

The dimensions (e.g., length) of an object as measured by one observer may be smaller than the results of measurements of the same object made by another observer (e.g., the ladder paradox involves a long ladder traveling near the speed of light and being contained within a smaller garage).

Similarly, suppose a measuring rod is at rest and aligned along the *x*-axis in the unprimed system *S*. In this system, the length of this rod is written as Δ*x*. To measure the length of this rod in the system *S*′, in which the rod is moving, the distances *x′* to the end points of the rod must be measured simultaneously in that system *S*′. In other words, the measurement is characterized by Δ*t*′ = 0, which can be combined with **Equation 4** to find the relation between the lengths Δ*x* and Δ*x*′:

$\Delta x'={\frac {\Delta x}{\gamma }}$

for events satisfying

$\Delta t'=0\ .$

This shows that the length (Δ*x*′) of the rod as measured in the frame in which it is moving (*S*′), is *shorter* than its length (Δ*x*) in its own rest frame (*S*).

Time dilation and length contraction are not merely appearances. Time dilation is explicitly related to our way of measuring *time intervals* between events that occur at the same place in a given coordinate system (called "co-local" events). These time intervals are *different* in another coordinate system moving with respect to the first, unless the events, in addition to being co-local, are also simultaneous. Similarly, length contraction relates to our measured distances between separated but simultaneous events in a given coordinate system of choice. If these events are not co-local, but are separated by distance (space), they will *not* occur at the same *spatial distance* from each other when seen from another moving coordinate system.

### Lorentz transformation of velocities

Consider two frames *S* and *S*′ in standard configuration. A particle in *S* moves in the x direction with velocity vector ⁠ $\mathbf {u}$ ⁠. What is its velocity $\mathbf {u'}$ in frame *S*′?

We can write

| $\mathbf {\|u\|} =u=dx/dt\,.$ |   | 7 |
|---|---|---|

| $\mathbf {\|u'\|} =u'=dx'/dt'\,.$ |   | 8 |
|---|---|---|

Substituting expressions for $dx'$ and $dt'$ from **Equation 5** into **Equation 8**, followed by straightforward mathematical manipulations and back-substitution from **Equation 7** yields the Lorentz transformation of the speed u to ⁠ $u'$ ⁠:

| $u'={\frac {dx'}{dt'}}={\frac {\gamma (dx-v\,dt)}{\gamma \left(dt-{\dfrac {v\,dx}{c^{2}}}\right)}}={\frac {{\dfrac {dx}{dt}}-v}{1-{\dfrac {v}{c^{2}}}\,{\dfrac {dx}{dt}}}}={\frac {u-v}{1-{\dfrac {uv}{c^{2}}}}}.$ |   | 9 |
|---|---|---|

The inverse relation is obtained by interchanging the primed and unprimed symbols and replacing v with ⁠ $-v$ ⁠.

| $u={\frac {u'+v}{1+u'v/c^{2}}}.$ |   | 10 |
|---|---|---|

For $\mathbf {u}$ not aligned along the x-axis, we write:

| $\mathbf {u} =(u_{1},\ u_{2},\ u_{3})=(dx/dt,\ dy/dt,\ dz/dt)\ .$ |   | 11 |
|---|---|---|

| $\mathbf {u'} =(u_{1}',\ u_{2}',\ u_{3}')=(dx'/dt',\ dy'/dt',\ dz'/dt')\ .$ |   | 12 |
|---|---|---|

The forward and inverse transformations for this case are:

| $u_{1}'={\frac {u_{1}-v}{1-u_{1}v/c^{2}}}\ ,\qquad u_{2}'={\frac {u_{2}}{\gamma \left(1-u_{1}v/c^{2}\right)}}\ ,\qquad u_{3}'={\frac {u_{3}}{\gamma \left(1-u_{1}v/c^{2}\right)}}\ .$ |   | 13 |
|---|---|---|

| $u_{1}={\frac {u_{1}'+v}{1+u_{1}'v/c^{2}}}\ ,\qquad u_{2}={\frac {u_{2}'}{\gamma \left(1+u_{1}'v/c^{2}\right)}}\ ,\qquad u_{3}={\frac {u_{3}'}{\gamma \left(1+u_{1}'v/c^{2}\right)}}\ .$ |   | 14 |
|---|---|---|

**Equation 10** and **Equation 14** can be interpreted as giving the *resultant* $\mathbf {u}$ of the two velocities $\mathbf {v}$ and ⁠ $\mathbf {u'}$ ⁠, and they replace the formula ⁠ $\mathbf {u=u'+v}$ ⁠. which is valid in Galilean relativity. Interpreted in such a fashion, they are commonly referred to as the *relativistic velocity addition (or composition) formulas*, valid for the three axes of *S* and *S*′ being aligned with each other (although not necessarily in standard configuration).

We note the following points:

- If an object (e.g., a photon) were moving at the speed of light in one frame (i.e., *u* = ±*c* or *u*′ = ±*c*), then it would also be moving at the speed of light in any other frame, moving at |*v*| < *c*.
- The resultant speed of two velocities with magnitude less than *c* is always a velocity with magnitude less than *c*.
- If both |*u*| and |*v*| (and then also |*u*′| and |*v*′|) are small with respect to the speed of light (that is, e.g., |⁠*u*/*c*⁠| ≪ 1), then the intuitive Galilean transformations are recovered from the transformation equations for special relativity
- Attaching a frame to a photon (*riding a light beam* like Einstein considers) requires special treatment of the transformations.

There is nothing special about the *x* direction in the standard configuration. The above formalism applies to any direction; and three orthogonal directions allow dealing with all directions in space by decomposing the velocity vectors to their components in these directions. See *Velocity-addition formula* for details.

### Thomas rotation

Figure 4-5. Thomas–Wigner rotation

The composition of two non-collinear Lorentz boosts (i.e., two non-collinear Lorentz transformations, neither of which involve rotation) results in a Lorentz transformation that is not a pure boost but is the composition of a boost and a rotation.

Thomas rotation results from the relativity of simultaneity. In Fig. 4-5a, a rod of length L in its rest frame (i.e., having a proper length of ⁠ L ⁠) rises vertically along the y-axis in the ground frame.

In Fig. 4-5b, the same rod is observed from the frame of a rocket moving at speed v to the right. If we imagine two clocks situated at the left and right ends of the rod that are synchronized *in the frame of the rod*, relativity of simultaneity causes the observer in the rocket frame to observe (not *see*) the clock at the right end of the rod as being advanced in time by ⁠ $Lv/c^{2}$ ⁠, and the rod is correspondingly observed as tilted.

Unlike second-order relativistic effects such as length contraction or time dilation, this effect becomes quite significant even at fairly low velocities. For example, this can be seen in the spin of moving particles, where Thomas precession is a relativistic correction that applies to the spin of an elementary particle or the rotation of a macroscopic gyroscope, relating the angular velocity of the spin of a particle following a curvilinear orbit to the angular velocity of the orbital motion.

Thomas rotation provides the resolution to the well-known "meter stick and hole paradox".

### Causality and prohibition of motion faster than light

In Fig. 4-6, the time interval between the events A (the "cause") and B (the "effect") is 'timelike'; that is, there is a frame of reference in which events A and B occur at the *same location in space*, separated only by occurring at different times. If A precedes B in that frame, then A precedes B in all frames accessible by a Lorentz transformation. It is possible for matter (or information) to travel (below light speed) from the location of A, starting at the time of A, to the location of B, arriving at the time of B, so there can be a causal relationship (with A the cause and B the effect).

The interval AC in the diagram is 'spacelike'; that is, there is a frame of reference in which events A and C occur simultaneously, separated only in space. There are also frames in which A precedes C (as shown) and frames in which C precedes A. But no frames are accessible by a Lorentz transformation, in which events A and C occur at the same location. If it were possible for a cause-and-effect relationship to exist between events A and C, paradoxes of causality would result.

For example, if signals could be sent faster than light, then signals could be sent into the sender's past (observer B in the diagrams). A variety of causal paradoxes could then be constructed.

Figure 4-7. Causality violation by the use of fictitious

"instantaneous communicators"

Consider the spacetime diagrams in Fig. 4-7. A and B stand alongside a railroad track, when a high-speed train passes by, with C riding in the last car of the train and D riding in the leading car. The world lines of A and B are vertical (*ct*), distinguishing the stationary position of these observers on the ground, while the world lines of C and D are tilted forwards (*ct′*), reflecting the rapid motion of the observers C and D stationary in their train, as observed from the ground.

1. Fig. 4-7a. The event of "B passing a message to D", as the leading car passes by, is at the origin of D's frame. D sends the message along the train to C in the rear car, using a fictitious "instantaneous communicator". The worldline of this message is the fat red arrow along the $-x'$ axis, which is a line of simultaneity in the primed frames of C and D. In the (unprimed) ground frame the signal arrives *earlier* than it was sent.
2. Fig. 4-7b. The event of "C passing the message to A", who is standing by the railroad tracks, is at the origin of their frames. Now A sends the message along the tracks to B via an "instantaneous communicator". The worldline of this message is the blue fat arrow, along the $+x$ axis, which is a line of simultaneity for the frames of A and B. As seen from the spacetime diagram, in the primed frames of C and D, B will receive the message before it was sent out, a violation of causality.

It is not necessary for signals to be instantaneous to violate causality. Even if the signal from D to C were slightly shallower than the $x'$ axis (and the signal from A to B slightly steeper than the x axis), it would still be possible for B to receive his message before he had sent it. By increasing the speed of the train to near light speeds, the $ct'$ and $x'$ axes can be squeezed very close to the dashed line representing the speed of light. With this modified setup, it can be demonstrated that even signals only *slightly* faster than the speed of light will result in causality violation.

Therefore, **if** causality is to be preserved, one of the consequences of special relativity is that no information signal or material object can travel faster than light in vacuum.

Only matter and energy are limited by the speed of light. Various trivial situations can be described where some imaginary points move faster than light. For example, the location where the beam of a search light hits the bottom of a cloud can move faster than light when the search light is turned rapidly. The light beam is not solid and it does not instantly follow the motion of the search light and thus does not violate causality or any other relativistic phenomenon.


## Optical effects

### Dragging effects

In 1850, Hippolyte Fizeau and Léon Foucault independently established that light travels more slowly in water than in air, thus validating a prediction of Fresnel's wave theory of light and invalidating the corresponding prediction of Newton's corpuscular theory. The speed of light was measured in still water. What would be the speed of light in flowing water?

In 1851, Fizeau conducted an experiment to answer this question, a simplified representation of which is illustrated in Fig. 5-1. A beam of light is divided by a beam splitter, and the split beams are passed in opposite directions through a tube of flowing water. They are recombined to form interference fringes, indicating a difference in optical path length, that an observer can view. The experiment demonstrated that dragging of the light by the flowing water caused a displacement of the fringes, showing that the motion of the water had affected the speed of the light.

According to the theories prevailing at the time, light traveling through a moving medium would be a simple sum of its speed *through* the medium plus the speed *of* the medium. Contrary to expectation, Fizeau found that although light appeared to be dragged by the water, the magnitude of the dragging was much lower than expected. If $u'=c/n$ is the speed of light in still water, and v is the speed of the water, and $u_{\pm }$ is the water-borne speed of light in the lab frame with the flow of water adding to or subtracting from the speed of light, then $u_{\pm }={\frac {c}{n}}\pm v\left(1-{\frac {1}{n^{2}}}\right)\ .$

Fizeau's results, although consistent with Fresnel's earlier hypothesis of partial aether dragging, were extremely disconcerting to physicists of the time. Among other things, the presence of an index of refraction term meant that, since n depends on wavelength, *the aether must be capable of sustaining different motions at the same time*. A variety of theoretical explanations were proposed to explain Fresnel's dragging coefficient, that were completely at odds with each other. Even before the Michelson–Morley experiment, Fizeau's experimental results were among a number of observations that created a critical situation in explaining the optics of moving bodies.

From the point of view of special relativity, Fizeau's result is nothing but an approximation to **Equation 10**, the relativistic formula for composition of velocities.

$u_{\pm }={\frac {u'\pm v}{1\pm u'v/c^{2}}}=$

${\frac {c/n\pm v}{1\pm v/cn}}\approx$

$c\left({\frac {1}{n}}\pm {\frac {v}{c}}\right)\left(1\mp {\frac {v}{cn}}\right)\approx$

${\frac {c}{n}}\pm v\left(1-{\frac {1}{n^{2}}}\right)$

### Relativistic aberration of light

Because of the finite speed of light, if the relative motions of a source and receiver include a transverse component, then the direction from which light arrives at the receiver will be displaced from the geometric position in space of the source relative to the receiver. The classical calculation of the displacement takes two forms and makes different predictions depending on whether the receiver, the source, or both are in motion with respect to the medium. (1) If the receiver is in motion, the displacement would be the consequence of the aberration of light. The incident angle of the beam relative to the receiver would be calculable from the vector sum of the receiver's motions and the velocity of the incident light. (2) If the source is in motion, the displacement would be the consequence of light-time correction. The displacement of the apparent position of the source from its geometric position would be the result of the source's motion during the time that its light takes to reach the receiver.

The classical explanation failed experimental test. Since the aberration angle depends on the relationship between the velocity of the receiver and the speed of the incident light, passage of the incident light through a refractive medium should change the aberration angle. In 1810, Arago used this expected phenomenon in a failed attempt to measure the speed of light, and in 1870, George Airy tested the hypothesis using a water-filled telescope, finding that, against expectation, the measured aberration was identical to the aberration measured with an air-filled telescope. A "cumbrous" attempt to explain these results used the hypothesis of partial aether-drag, but was incompatible with the results of the Michelson–Morley experiment, which apparently demanded *complete* aether-drag.

Assuming inertial frames, the relativistic expression for the aberration of light is applicable to both the receiver moving and source moving cases. A variety of trigonometrically equivalent formulas have been published. Expressed in terms of the variables in Fig. 5-2, these include

$\cos \theta '={\frac {\cos \theta +v/c}{1+(v/c)\cos \theta }}$

OR

$\sin \theta '={\frac {\sin \theta }{\gamma [1+(v/c)\cos \theta ]}}$

OR

$\tan {\frac {\theta '}{2}}=\left({\frac {c-v}{c+v}}\right)^{1/2}\tan {\frac {\theta }{2}}$

### Relativistic Doppler effect

#### Relativistic longitudinal Doppler effect

The classical Doppler effect depends on whether the source, receiver, or both are in motion with respect to the medium. The relativistic Doppler effect is independent of any medium. Nevertheless, relativistic Doppler shift for the longitudinal case, with source and receiver moving directly towards or away from each other, can be derived as if it were the classical phenomenon, but modified by the addition of a time dilation term, and that is the treatment described here.

Assume the receiver and the source are moving *away* from each other with a relative speed v as measured by an observer on the receiver or the source (The sign convention adopted here is that v is *negative* if the receiver and the source are moving *towards* each other). Assume that the source is stationary in the medium. Then $f_{r}=\left(1-{\frac {v}{c_{s}}}\right)f_{s}$ where $c_{s}$ is the speed of sound.

For light, and with the receiver moving at relativistic speeds, clocks on the receiver are time dilated relative to clocks at the source. The receiver will measure the received frequency to be $f_{r}=\gamma \left(1-\beta \right)f_{s}={\sqrt {\frac {1-\beta }{1+\beta }}}\,f_{s}.$ where

- $\beta =v/c$   and
- $\gamma ={\frac {1}{\sqrt {1-\beta ^{2}}}}$ is the Lorentz factor.

An identical expression for relativistic Doppler shift is obtained when performing the analysis in the reference frame of the *receiver* with a moving source.

#### Transverse Doppler effect

The transverse Doppler effect is one of the main novel predictions of the special theory of relativity.

Classically, one might expect that if source and receiver are moving transversely with respect to each other with no longitudinal component to their relative motions, that there should be no Doppler shift in the light arriving at the receiver.

Special relativity predicts otherwise. Fig. 5-3 illustrates two common variants of this scenario. Both variants can be analyzed using simple time dilation arguments. In Fig. 5-3a, the receiver observes light from the source as being blueshifted by a factor of ⁠ $\gamma$ ⁠. In Fig. 5-3b, the light is redshifted by the same factor.

### Measurement versus visual appearance

Time dilation and length contraction are not optical illusions, but genuine effects. Measurements of these effects are not an artifact of Doppler shift, nor are they the result of neglecting to take into account the time it takes light to travel from an event to an observer.

Scientists make a fundamental distinction between *measurement* or *observation* on the one hand, versus *visual appearance*, or what one *sees*. The measured shape of an object is a hypothetical snapshot of all of the object's points as they exist at a single moment in time. But the visual appearance of an object is affected by the varying lengths of time that light takes to travel from different points on the object to one's eye.

For many years, the distinction between the two had not been generally appreciated, and it had generally been thought that a length contracted object passing by an observer would be observed as length contracted. In 1959, James Terrell and Roger Penrose independently pointed out that differential time lag effects in signals reaching the observer from the different parts of a moving object result in a fast moving object's visual appearance being quite different from its measured shape. For example, a receding object would *appear* contracted, an approaching object would *appear* elongated, and a passing object would have a skew appearance that has been likened to a rotation. A sphere in motion retains the circular outline for all speeds, for any distance, and for all view angles, although the surface of the sphere and the images on it will appear distorted.

Both Fig. 5-4 and Fig. 5-5 illustrate objects moving transversely to the line of sight. In Fig. 5-4, a cube is viewed from a distance of four times the length of its sides. At high speeds, the sides of the cube that are perpendicular to the direction of motion appear hyperbolic in shape. The cube is not rotated. Rather, light from the rear of the cube takes longer to reach one's eyes compared with light from the front, during which time the cube has moved to the right. At high speeds, the sphere in Fig. 5-5 takes on the appearance of a flattened disk tilted up to 45° from the line of sight. If the objects' motions are not strictly transverse but instead include a longitudinal component, exaggerated distortions in perspective may be seen. This illusion has come to be known as *Terrell rotation* or the *Terrell–Penrose effect*.

Another example where visual appearance is at odds with measurement comes from the observation of apparent superluminal motion in various radio galaxies, BL Lac objects, quasars, and other astronomical objects that eject relativistic-speed jets of matter at narrow angles with respect to the viewer. An apparent optical illusion results giving the appearance of faster than light travel. In Fig. 5-6, galaxy M87 streams out a high-speed jet of subatomic particles almost directly towards us, but Penrose–Terrell rotation causes the jet to appear to be moving laterally in the same manner that the appearance of the cube in Fig. 5-4 has been stretched out.
