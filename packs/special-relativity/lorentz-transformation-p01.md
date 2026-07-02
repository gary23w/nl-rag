---
title: "Lorentz transformation (part 1/2)"
source: https://en.wikipedia.org/wiki/Lorentz_transformation
domain: special-relativity
license: CC-BY-SA-4.0
tags: special relativity, lorentz transformation, time dilation, mass-energy equivalence
fetched: 2026-07-02
part: 1/2
---

# Lorentz transformation

In physics, the **Lorentz transformations** are a six-parameter family of linear transformations from a coordinate frame in spacetime to another frame that moves at a constant velocity relative to the former. The respective inverse transformation is then parameterized by the negative of this velocity. The transformations are named after the Dutch physicist Hendrik Lorentz.

The most common form of the transformation, parametrized by the real constant $v,$ representing a velocity confined to the x-direction, is expressed as ${\begin{aligned}t'&=\gamma \left(t-{\frac {vx}{c^{2}}}\right)\\x'&=\gamma \left(x-vt\right)\\y'&=y\\z'&=z\end{aligned}}$ where (*t*, *x*, *y*, *z*) and (*t*′, *x*′, *y*′, *z*′) are the coordinates of an event in two frames with the spatial origins coinciding at *t* = *t*′ = 0, where the primed frame is seen from the unprimed frame as moving with speed v along the x-axis, where c is the speed of light, and $\gamma ={\frac {1}{\sqrt {1-v^{2}/c^{2}}}}$ is the Lorentz factor. When speed v is much smaller than c, the Lorentz factor is negligibly different from 1, but as v approaches c, $\gamma$ grows without bound. The value of v must be smaller than c for the transformation to make sense.

Expressing the speed as a fraction of the speed of light, ${\textstyle \beta =v/c,}$ an equivalent form of the transformation is ${\begin{aligned}ct'&=\gamma \left(ct-\beta x\right)\\x'&=\gamma \left(x-\beta ct\right)\\y'&=y\\z'&=z.\end{aligned}}$

Frames of reference can be divided into two groups: inertial (relative motion with constant velocity) and non-inertial (accelerating, moving in curved paths, rotational motion with constant angular velocity, etc.). The term "Lorentz transformations" only refers to transformations between *inertial* frames, usually in the context of special relativity.

In each reference frame, an observer can use a local coordinate system (usually Cartesian coordinates in this context) to measure lengths, and a clock to measure time intervals. An event is something that happens at a point in space at an instant of time, or more formally a point in spacetime. The transformations connect the space and time coordinates of an event as measured by an observer in each frame.

They supersede the Galilean transformation of Newtonian physics, which assumes an absolute space and time (see *Galilean relativity*). The Galilean transformation is a good approximation only at relative speeds much less than the speed of light. Lorentz transformations have a number of unintuitive features that do not appear in Galilean transformations. For example, they reflect the fact that observers moving at different velocities may measure different distances, elapsed times, and even different orderings of events, but always such that the speed of light is the same in all inertial reference frames. The invariance of light speed is one of the postulates of special relativity.

Historically, the transformations were the result of attempts by Lorentz and others to explain how the speed of light was observed to be independent of the reference frame, and to understand the symmetries of the laws of electromagnetism. The transformations later became a cornerstone for special relativity.

The Lorentz transformation is a linear transformation. It may include a rotation of space; a rotation-free Lorentz transformation is called a **Lorentz boost**. In Minkowski space—the mathematical model of spacetime in special relativity—the Lorentz transformations preserve the spacetime interval between any two events. They describe only the transformations in which the spacetime event at the origin is left fixed. They can be considered as a hyperbolic rotation of Minkowski space. The more general set of transformations that also includes translations is known as the Poincaré group.


## History

In the 1890s, Hendrik Lorentz began to develop theories of electrodynamics based on a pervasive luminiferous aether uncoupled from matter. In a series of paper from 1892 to 1904 he used transformations which would come to bear his name as mathematical aids in analyzing these theories. Woldemar Voigt had developed similar transformations when studying Doppler shift physics in 1887. In that year, the aether-wind experiment of Michelson and Morley was repeated with better accuracy, leading George FitzGerald to conjecture that bodies in motion through aether are being contracted. In 1892, Lorentz independently presented the same idea in a more detailed manner, which was subsequently called FitzGerald–Lorentz contraction hypothesis. This hypothesis was widely known before 1905.

Many other physicists were also involved in the development and understanding of these transformation. Lorentz indirectly discovered time dilation in 1892, but Joseph Larmor was the first to explicit mention that the 'scale of time is enlarged'. The time coordinate in these transformation came to be called ("local time"). Henri Poincaré gave a physical interpretation to local time (to first order in *v*/*c*, the relative velocity of the two reference frames normalized to the speed of light) as the consequence of clock synchronization, under the assumption that the speed of light is constant in moving frames.

In 1905, Poincaré was the first to recognize that the transformation has the properties of a mathematical group, and he named it after Lorentz. All of the work up to 1905 assumed that the constant speed of light was a consequence of an aether and hypothesized the transformation. In that year Albert Einstein published what is now called special relativity, by deriving the Lorentz transformation under the assumptions of the principle of relativity and the constancy of the speed of light in any inertial reference frame, and by abandoning the mechanistic aether as unnecessary.


## Derivation of the group of Lorentz transformations

An *event* is something that happens at a certain point in spacetime, or more generally, the point in spacetime itself. In any inertial frame an event is specified by a time coordinate *ct* and a set of Cartesian coordinates x, y, z to specify position in space in that frame. Subscripts label individual events.

From Einstein's second postulate of relativity (invariance of c) it follows that:

| $c^{2}(t_{2}-t_{1})^{2}-(x_{2}-x_{1})^{2}-(y_{2}-y_{1})^{2}-(z_{2}-z_{1})^{2}=0\quad {\text{(lightlike separated events 1, 2)}}$ |   | D1 |
|---|---|---|

in all inertial frames for events connected by *light signals*. The quantity on the left is called the spacetime interval between events *a*1 = (*t*1, *x*1, *y*1, *z*1) and *a*2 = (*t*2, *x*2, *y*2, *z*2). The interval between *any two* events, not necessarily separated by light signals, is in fact invariant, i.e., independent of the state of relative motion of observers in different inertial frames, as is shown using homogeneity and isotropy of space. The transformation sought after thus must possess the property that:

| ${\begin{aligned}c^{2}(t_{2}-t_{1})^{2}-(x_{2}-x_{1})^{2}-(y_{2}-y_{1})^{2}-(z_{2}-z_{1})^{2}&=&\\[6pt]c^{2}(t_{2}'-t_{1}')^{2}-(x_{2}'-x_{1}')^{2}-(y_{2}'-y_{1}')^{2}-(z_{2}'-z_{1}')^{2}&&\quad {\text{(all events 1, 2)}}.\end{aligned}}$ |   | D2 |
|---|---|---|

where (*t*, *x*, *y*, *z*) are the spacetime coordinates used to define events in one frame, and (*t*′, *x*′, *y*′, *z*′) are the coordinates in another frame. First one observes that (**D2**) is satisfied if an arbitrary 4-tuple b of numbers are added to events *a*1 and *a*2. Such transformations are called *spacetime translations* and are not dealt with further here. Then one observes that a *linear* solution preserving the origin of the simpler problem solves the general problem too:

| ${\begin{aligned}c^{2}t^{2}-x^{2}-y^{2}-z^{2}&=c^{2}t'^{2}-x'^{2}-y'^{2}-z'^{2}&\quad {\text{or}}\\[6pt]c^{2}t_{1}t_{2}-x_{1}x_{2}-y_{1}y_{2}-z_{1}z_{2}&=c^{2}t'_{1}t'_{2}-x'_{1}x'_{2}-y'_{1}y'_{2}-z'_{1}z'_{2}&\end{aligned}}$ |   | D3 |
|---|---|---|

(a solution satisfying the first formula automatically satisfies the second one as well; see *Polarization identity*). Finding the solution to the simpler problem is just a matter of look-up in the theory of classical groups that preserve bilinear forms of various signature. First equation in (**D3**) can be written more compactly as:

| $(a,a)=(a',a')\quad {\text{or}}\quad a\cdot a=a'\cdot a',$ |   | D4 |
|---|---|---|

where (·, ·) refers to the bilinear form of signature (1, 3) on **R**4 exposed by the right hand side formula in (**D3**). The alternative notation defined on the right is referred to as the *relativistic dot product*. Spacetime mathematically viewed as **R**4 endowed with this bilinear form is known as Minkowski space M. The Lorentz transformation is thus an element of the group O(1, 3), the Lorentz group or, for those that prefer the other metric signature, O(3, 1) (also called the Lorentz group). One has:

| $(a,a)=(\Lambda a,\Lambda a)=(a',a'),\quad \Lambda \in \mathrm {O} (1,3),\quad a,a'\in M,$ |   | D5 |
|---|---|---|

which is precisely preservation of the bilinear form (**D3**) which implies (by linearity of Λ and bilinearity of the form) that (**D2**) is satisfied. The elements of the Lorentz group are rotations and *boosts* and mixes thereof. If the spacetime translations are included, then one obtains the *inhomogeneous Lorentz group* or the Poincaré group.


## Generalities

The relations between the primed and unprimed spacetime coordinates are the **Lorentz transformations**, each coordinate in one frame is a linear function of all the coordinates in the other frame, and the inverse functions are the inverse transformation. Depending on how the frames move relative to each other, and how they are oriented in space relative to each other, other parameters that describe direction, speed, and orientation enter the transformation equations.

Transformations describing relative motion with constant (uniform) velocity and without rotation of the space coordinate axes are called **Lorentz boosts** or simply *boosts*, and the relative velocity between the frames is the parameter of the transformation. The other basic type of Lorentz transformation is only a rotation in the spatial coordinates. Unlike boosts, these are inertial transformations since there is no relative motion, the frames are simply tilted (and not continuously rotating), and in this case quantities defining the rotation are the parameters of the transformation (e.g., axis–angle representation, or Euler angles, etc.). A combination of a rotation and a boost is a *homogeneous transformation*, which transforms the origin back to the origin.

The full Lorentz group O(3, 1) also contains special transformations that are neither rotations nor boosts, but rather reflections in a plane through the origin. Two of these can be singled out; spatial inversion in which the spatial coordinates of all events are reversed in sign and temporal inversion in which the time coordinate for each event gets its sign reversed.

Boosts should not be conflated with mere displacements in spacetime; in this case, the coordinate systems are simply shifted and there is no relative motion. However, these also count as symmetries forced by special relativity since they leave the spacetime interval invariant. A combination of a rotation with a boost, followed by a shift in spacetime, is an *inhomogeneous Lorentz transformation*, an element of the Poincaré group, which is also called the inhomogeneous Lorentz group.


## Physical formulation of Lorentz boosts

### Coordinate transformation

A "stationary" observer in frame F defines events with coordinates t, x, y, z. Another frame *F*′ moves with velocity v relative to F, and an observer in this "moving" frame *F*′ defines events using the coordinates *t*′, *x*′, *y*′, *z*′.

The coordinate axes in each frame are parallel (the x and *x*′ axes are parallel, the y and *y*′ axes are parallel, and the z and *z*′ axes are parallel), remain mutually perpendicular, and relative motion is along the coincident *xx*′ axes. At *t* = *t*′ = 0, the origins of both coordinate systems are the same, (*x*, *y*, *z*) = (*x*′, *y*′, *z*′) = (0, 0, 0). In other words, the times and positions are coincident at this event. If all these hold, then the coordinate systems are said to be in **standard configuration**, or **synchronized**.

If an observer in F records an event t, x, y, z, then an observer in *F*′ records the *same* event with coordinates

Lorentz boost

(

x

direction

)

${\begin{aligned}t'&=\gamma \left(t-{\frac {vx}{c^{2}}}\right)\\x'&=\gamma \left(x-vt\right)\\y'&=y\\z'&=z\end{aligned}}$

where v is the relative velocity between frames in the x-direction, c is the speed of light, and $\gamma ={\frac {1}{\sqrt {1-{\frac {v^{2}}{c^{2}}}}}}$ (lowercase gamma) is the Lorentz factor.

Here, v is the *parameter* of the transformation, for a given boost it is a constant number, but can take a continuous range of values. In the setup used here, positive relative velocity *v* > 0 is motion along the positive directions of the *xx*′ axes, zero relative velocity *v* = 0 is no relative motion, while negative relative velocity *v* < 0 is relative motion along the negative directions of the *xx*′ axes. The magnitude of relative velocity v cannot equal or exceed c, so only subluminal speeds −*c* < *v* < *c* are allowed. The corresponding range of γ is 1 ≤ *γ* < ∞.

The transformations are not defined if v is outside these limits. At the speed of light (*v* = *c*) γ is infinite, and faster than light (*v* > *c*) γ is a complex number, each of which make the transformations unphysical. The space and time coordinates are measurable quantities and numerically must be real numbers.

As an active transformation, an observer in *F*′ notices the coordinates of the event to be "boosted" in the negative directions of the *xx*′ axes, because of the −*v* in the transformations. This has the equivalent effect of the *coordinate system* *F*′ boosted in the positive directions of the *xx*′ axes, while the event does not change and is simply represented in another coordinate system, a passive transformation.

The inverse relations (t, x, y, z in terms of *t*′, *x*′, *y*′, *z*′) can be found by algebraically solving the original set of equations. A more efficient way is to use physical principles. Here *F*′ is the "stationary" frame while F is the "moving" frame. According to the principle of relativity, there is no privileged frame of reference, so the transformations from *F*′ to F must take exactly the same form as the transformations from F to *F*′. The only difference is F moves with velocity −*v* relative to *F*′ (i.e., the relative velocity has the same magnitude but is oppositely directed). Thus if an observer in *F*′ notes an event *t*′, *x*′, *y*′, *z*′, then an observer in F notes the *same* event with coordinates

Inverse Lorentz boost

(

x

direction

)

${\begin{aligned}t&=\gamma \left(t'+{\frac {vx'}{c^{2}}}\right)\\x&=\gamma \left(x'+vt'\right)\\y&=y'\\z&=z',\end{aligned}}$

and the value of γ remains unchanged. This "trick" of simply reversing the direction of relative velocity while preserving its magnitude, and exchanging primed and unprimed variables, always applies to finding the inverse transformation of every boost in any direction.

Sometimes it is more convenient to use *β* = *v*/*c* (lowercase beta) instead of v, so that ${\begin{aligned}ct'&=\gamma \left(ct-\beta x\right)\,,\\x'&=\gamma \left(x-\beta ct\right)\,,\\\end{aligned}}$ which shows much more clearly the symmetry in the transformation. From the allowed ranges of v and the definition of β, it follows −1 < *β* < 1. The use of β and γ is standard throughout the literature. In the case of three spatial dimensions [*ct*, *x*, *y*, *z*], where the boost $\beta$ is in the *x* direction, the eigenstates of the transformation are [1, 1, 0, 0] with eigenvalue ${\sqrt {(1-\beta )/(1+\beta )}}$ , [1, −1, 0, 0] with eigenvalue ${\sqrt {(1+\beta )/(1-\beta )}}$ , and [0, 0, 1, 0] and [0, 0, 0, 1], the latter two with eigenvalue 1.

When the boost velocity ${\boldsymbol {v}}$ is in an arbitrary vector direction with the boost vector ${\boldsymbol {\beta }}={\boldsymbol {v}}/c$ , then the transformation from an unprimed spacetime coordinate system to a primed coordinate system is given by

${\begin{bmatrix}ct'{\vphantom {-\gamma \beta _{\text{x}}}}\\x'{\vphantom {1+{\frac {\gamma ^{2}}{1+\gamma }}\beta _{\text{x}}^{2}}}\\y'{\vphantom {{\frac {\gamma ^{2}}{1+\gamma }}\beta _{\text{x}}\beta _{\text{y}}}}\\z'{\vphantom {{\frac {\gamma ^{2}}{1+\gamma }}\beta _{\text{y}}\beta _{\text{z}}}}\end{bmatrix}}={\begin{bmatrix}\gamma &-\gamma \beta _{\text{x}}&-\gamma \beta _{\text{y}}&-\gamma \beta _{\text{z}}\\-\gamma \beta _{\text{x}}&1+{\frac {\gamma ^{2}}{1+\gamma }}\beta _{\text{x}}^{2}&{\frac {\gamma ^{2}}{1+\gamma }}\beta _{\text{x}}\beta _{\text{y}}&{\frac {\gamma ^{2}}{1+\gamma }}\beta _{\text{x}}\beta _{\text{z}}\\-\gamma \beta _{\text{y}}&{\frac {\gamma ^{2}}{1+\gamma }}\beta _{\text{x}}\beta _{\text{y}}&1+{\frac {\gamma ^{2}}{1+\gamma }}\beta _{\text{y}}^{2}&{\frac {\gamma ^{2}}{1+\gamma }}\beta _{\text{y}}\beta _{\text{z}}\\-\gamma \beta _{\text{z}}&{\frac {\gamma ^{2}}{1+\gamma }}\beta _{\text{x}}\beta _{\text{z}}&{\frac {\gamma ^{2}}{1+\gamma }}\beta _{\text{y}}\beta _{\text{z}}&1+{\frac {\gamma ^{2}}{1+\gamma }}\beta _{\text{z}}^{2}\\\end{bmatrix}}{\begin{bmatrix}ct{\vphantom {-\gamma \beta _{\text{x}}}}\\x{\vphantom {1+{\frac {\gamma ^{2}}{1+\gamma }}\beta _{\text{x}}^{2}}}\\y{\vphantom {{\frac {\gamma ^{2}}{1+\gamma }}\beta _{\text{x}}\beta _{\text{y}}}}\\z{\vphantom {{\frac {\gamma ^{2}}{1+\gamma }}\beta _{\text{y}}\beta _{\text{z}}}}\end{bmatrix}},$

where the Lorentz factor is $\gamma =1/{\sqrt {1-{\boldsymbol {\beta }}^{2}}}$ . The determinant of the transformation matrix is +1 and its trace is $2(1+\gamma )$ . The inverse of the transformation is given by reversing the sign of ${\boldsymbol {\beta }}$ . The quantity $c^{2}t^{2}-x^{2}-y^{2}-z^{2}$ is invariant under the transformation: namely $(c^{2}t'^{2}-x'^{2}-y'^{2}-z'^{2})=(c^{2}t^{2}-x^{2}-y^{2}-z^{2})$ .

The Lorentz transformations can also be derived in a way that resembles circular rotations in 3-dimensional space using the hyperbolic functions. For the boost in the x direction, the results are

Lorentz boost

(

x

direction with rapidity

ζ

)

${\begin{aligned}ct'&=ct\cosh \zeta -x\sinh \zeta \\x'&=x\cosh \zeta -ct\sinh \zeta \\y'&=y\\z'&=z\end{aligned}}$

where ζ (lowercase zeta) is a parameter called *rapidity* (many other symbols are used, including θ, ϕ, φ, η, ψ, ξ). Given the strong resemblance to rotations of spatial coordinates in 3-dimensional space in the Cartesian *xy*, *yz*, and *zx* planes, a Lorentz boost can be thought of as a hyperbolic rotation of spacetime coordinates in the xt, yt, and zt Cartesian-time planes of 4-dimensional Minkowski space. The parameter ζ is the hyperbolic angle of rotation, analogous to the ordinary angle for circular rotations. This transformation can be illustrated with a Minkowski diagram.

The hyperbolic functions arise from the *difference* between the squares of the time and spatial coordinates in the spacetime interval, rather than a sum. The geometric significance of the hyperbolic functions can be visualized by taking *x* = 0 or *ct* = 0 in the transformations. Squaring and subtracting the results, one can derive hyperbolic curves of constant coordinate values but varying ζ, which parametrizes the curves according to the identity $\cosh ^{2}\zeta -\sinh ^{2}\zeta =1\,.$

Conversely the *ct* and x axes can be constructed for varying coordinates but constant ζ. The definition $\tanh \zeta ={\frac {\sinh \zeta }{\cosh \zeta }}\,,$ provides the link between a constant value of rapidity, and the slope of the *ct* axis in spacetime. A consequence these two hyperbolic formulae is an identity that matches the Lorentz factor $\cosh \zeta ={\frac {1}{\sqrt {1-\tanh ^{2}\zeta }}}\,.$

Comparing the Lorentz transformations in terms of the relative velocity and rapidity, or using the above formulae, the connections between β, γ, and ζ are ${\begin{aligned}\beta &=\tanh \zeta \,,\\\gamma &=\cosh \zeta \,,\\\beta \gamma &=\sinh \zeta \,.\end{aligned}}$

Taking the inverse hyperbolic tangent gives the rapidity $\zeta =\tanh ^{-1}\beta \,.$

Since −1 < *β* < 1, it follows −∞ < *ζ* < ∞. From the relation between ζ and β, positive rapidity *ζ* > 0 is motion along the positive directions of the *xx*′ axes, zero rapidity *ζ* = 0 is no relative motion, while negative rapidity *ζ* < 0 is relative motion along the negative directions of the *xx*′ axes.

The inverse transformations are obtained by exchanging primed and unprimed quantities to switch the coordinate frames, and negating rapidity *ζ* → −*ζ* since this is equivalent to negating the relative velocity. Therefore,

Inverse Lorentz boost

(

x

direction with rapidity

ζ

)

${\begin{aligned}ct&=ct'\cosh \zeta +x'\sinh \zeta \\x&=x'\cosh \zeta +ct'\sinh \zeta \\y&=y'\\z&=z'\end{aligned}}$

The inverse transformations can be similarly visualized by considering the cases when *x*′ = 0 and *ct*′ = 0.

So far the Lorentz transformations have been applied to *one event*. If there are two events, there is a spatial separation and time interval between them. It follows from the linearity of the Lorentz transformations that two values of space and time coordinates can be chosen, the Lorentz transformations can be applied to each, then subtracted to get the Lorentz transformations of the differences: ${\begin{aligned}\Delta t'&=\gamma \left(\Delta t-{\frac {v\,\Delta x}{c^{2}}}\right)\,,\\\Delta x'&=\gamma \left(\Delta x-v\,\Delta t\right)\,,\end{aligned}}$ with inverse relations ${\begin{aligned}\Delta t&=\gamma \left(\Delta t'+{\frac {v\,\Delta x'}{c^{2}}}\right)\,,\\\Delta x&=\gamma \left(\Delta x'+v\,\Delta t'\right)\,.\end{aligned}}$ where Δ (uppercase delta) indicates a difference of quantities; e.g., Δ*x* = *x*2 − *x*1 for two values of x coordinates, and so on.

These transformations on *differences* rather than spatial points or instants of time are useful for a number of reasons:

- in calculations and experiments, it is lengths between two points or time intervals that are measured or of interest (e.g., the length of a moving vehicle, or time duration it takes to travel from one place to another),
- the transformations of velocity can be readily derived by making the difference infinitesimally small and dividing the equations, and the process repeated for the transformation of acceleration,
- if the coordinate systems are never coincident (i.e., not in standard configuration), and if both observers can agree on an event *t*0, *x*0, *y*0, *z*0 in F and *t*′0, *x*′0, *y*′0, *z*′0 in *F*′, then they can use that event as the origin, and the spacetime coordinate differences are the differences between their coordinates and this origin, e.g., Δ*x* = *x* − *x*0, Δ*x*′ = *x*′ − *x*′0, etc.

### Physical implications

A critical requirement of the Lorentz transformations is the invariance of the speed of light, a fact used in their derivation, and contained in the transformations themselves. If in F the equation for a pulse of light along the x direction is *x* = *ct*, then in F′ the Lorentz transformations give *x*′ = *ct*′, and vice versa, for any −*c* < *v* < *c*.

For relative speeds much less than the speed of light, the Lorentz transformations reduce to the Galilean transformation: ${\begin{aligned}t'&\approx t\\x'&\approx x-vt\end{aligned}}$ in accordance with the correspondence principle. It is sometimes said that nonrelativistic physics is a physics of "instantaneous action at a distance".

Three counterintuitive, but correct, predictions of the transformations are:

**Relativity of simultaneity**

Suppose two events occur along the x axis simultaneously (

Δ

t

= 0

) in

F

, but separated by a nonzero displacement

Δ

x

. Then in

F′

, we find that

$\Delta t'=-\gamma {v\,\Delta x}/{c^{2}}$

, so the events are no longer simultaneous according to a moving observer.

**Time dilation**

Suppose there is a clock at rest in

F

. If a time interval is measured at the same point in that frame, so that

Δ

x

= 0

, then the transformations give this interval in

F

′

by

Δ

t

′ =

γ

Δ

t

. Conversely, suppose there is a clock at rest in

F

′

. If an interval is measured at the same point in that frame, so that

Δ

x

′ = 0

, then the transformations give this interval in

F

by

Δ

t

=

γ

Δ

t

′

. Either way, each observer measures the time interval between ticks of a moving clock to be longer by a factor

γ

than the time interval between ticks of his own clock.

**Length contraction**

Suppose there is a rod at rest in

F

aligned along the

x

axis, with length

Δ

x

. In

F

′

, the rod moves with velocity

−

v

, so its length must be measured by taking two simultaneous (

Δ

t

′ = 0

) measurements at opposite ends. Under these conditions, the inverse Lorentz transform shows that

Δ

x

=

γ

Δ

x

′

. In

F

the two measurements are no longer simultaneous, but this does not matter because the rod is at rest in

F

. So each observer measures the distance between the end points of a moving rod to be shorter by a factor

1/

γ

than the end points of an identical rod at rest in his own frame. Length contraction affects any geometric quantity related to lengths, so from the perspective of a moving observer, areas and volumes will also appear to shrink along the direction of motion.

### Vector transformations

The use of vectors allows positions and velocities to be expressed in arbitrary directions compactly. A single boost in any direction depends on the full relative velocity vector **v** with a magnitude |**v**| = *v* that cannot equal or exceed c, so that 0 ≤ *v* < *c*.

Only time and the coordinates parallel to the direction of relative motion change, while those coordinates perpendicular do not. With this in mind, split the spatial position vector **r** as measured in F, and **r**′ as measured in *F*′, each into components perpendicular (⊥) and parallel ( || ) to **v**, $\mathbf {r} =\mathbf {r} _{\perp }+\mathbf {r} _{\|}\,,\quad \mathbf {r} '=\mathbf {r} _{\perp }'+\mathbf {r} _{\|}'\,,$ then the transformations are ${\begin{aligned}t'&=\gamma \left(t-{\frac {\mathbf {r} _{\parallel }\cdot \mathbf {v} }{c^{2}}}\right)\\\mathbf {r} _{\|}'&=\gamma (\mathbf {r} _{\|}-\mathbf {v} t)\\\mathbf {r} _{\perp }'&=\mathbf {r} _{\perp }\end{aligned}}$ where · is the dot product. The Lorentz factor γ retains its definition for a boost in any direction, since it depends only on the magnitude of the relative velocity. The definition **β** = **v**/*c* with magnitude 0 ≤ *β* < 1 is also used by some authors.

Introducing a unit vector **n** = **v**/*v* = **β**/*β* in the direction of relative motion, the relative velocity is **v** = *v***n** with magnitude v and direction **n**, and vector projection and rejection give respectively $\mathbf {r} _{\parallel }=(\mathbf {r} \cdot \mathbf {n} )\mathbf {n} \,,\quad \mathbf {r} _{\perp }=\mathbf {r} -(\mathbf {r} \cdot \mathbf {n} )\mathbf {n}$

Accumulating the results gives the full transformations,

Lorentz boost

(

in direction

n

with magnitude

v

)

${\begin{aligned}t'&=\gamma \left(t-{\frac {v\mathbf {n} \cdot \mathbf {r} }{c^{2}}}\right)\,,\\\mathbf {r} '&=\mathbf {r} +(\gamma -1)(\mathbf {r} \cdot \mathbf {n} )\mathbf {n} -\gamma tv\mathbf {n} \,.\end{aligned}}$

The projection and rejection also applies to **r**′. For the inverse transformations, exchange **r** and **r**′ to switch observed coordinates, and negate the relative velocity **v** → −**v** (or simply the unit vector **n** → −**n** since the magnitude v is always positive) to obtain

Inverse Lorentz boost

(

in direction

n

with magnitude

v

)

${\begin{aligned}t&=\gamma \left(t'+{\frac {\mathbf {r} '\cdot v\mathbf {n} }{c^{2}}}\right)\,,\\\mathbf {r} &=\mathbf {r} '+(\gamma -1)(\mathbf {r} '\cdot \mathbf {n} )\mathbf {n} +\gamma t'v\mathbf {n} \,,\end{aligned}}$

The unit vector has the advantage of simplifying equations for a single boost, allows either **v** or **β** to be reinstated when convenient, and the rapidity parametrization is immediately obtained by replacing β and *βγ*. It is not convenient for multiple boosts.

The vectorial relation between relative velocity and rapidity is ${\boldsymbol {\beta }}=\beta \mathbf {n} =\mathbf {n} \tanh \zeta \,,$ and the "rapidity vector" can be defined as ${\boldsymbol {\zeta }}=\zeta \mathbf {n} =\mathbf {n} \tanh ^{-1}\beta \,,$ each of which serves as a useful abbreviation in some contexts. The magnitude of **ζ** is the absolute value of the rapidity scalar confined to 0 ≤ *ζ* < ∞, which agrees with the range 0 ≤ *β* < 1.

### Transformation of velocities

Defining the coordinate velocities and Lorentz factor by $\mathbf {u} ={\frac {d\mathbf {r} }{dt}}\,,\quad \mathbf {u} '={\frac {d\mathbf {r} '}{dt'}}\,,\quad \gamma _{\mathbf {v} }={\frac {1}{\sqrt {1-{\dfrac {\mathbf {v} \cdot \mathbf {v} }{c^{2}}}}}}$ taking the differentials in the coordinates and time of the vector transformations, then dividing equations, leads to $\mathbf {u} '={\frac {1}{1-{\frac {\mathbf {v} \cdot \mathbf {u} }{c^{2}}}}}\left[{\frac {\mathbf {u} }{\gamma _{\mathbf {v} }}}-\mathbf {v} +{\frac {1}{c^{2}}}{\frac {\gamma _{\mathbf {v} }}{\gamma _{\mathbf {v} }+1}}\left(\mathbf {u} \cdot \mathbf {v} \right)\mathbf {v} \right]$

The velocities **u** and **u**′ are the velocity of some massive object. They can also be for a third inertial frame (say F′′), in which case they must be *constant*. Denote either entity by X. Then X moves with velocity **u** relative to F, or equivalently with velocity **u**′ relative to F′, in turn F′ moves with velocity **v** relative to F. The inverse transformations can be obtained in a similar way, or as with position coordinates exchange **u** and **u**′, and change **v** to −**v**.

The transformation of velocity is useful in stellar aberration, the Fizeau experiment, and the relativistic Doppler effect.

The Lorentz transformations of acceleration can be similarly obtained by taking differentials in the velocity vectors, and dividing these by the time differential.

### Transformation of other quantities

In general, given four quantities A and **Z** = (*Z**x*, *Z**y*, *Z**z*) and their Lorentz-boosted counterparts A′ and **Z**′ = (*Z*′*x*, *Z*′*y*, *Z*′*z*), a relation of the form $A^{2}-\mathbf {Z} \cdot \mathbf {Z} ={A'}^{2}-\mathbf {Z} '\cdot \mathbf {Z} '$ implies the quantities transform under Lorentz transformations similar to the transformation of spacetime coordinates; ${\begin{aligned}A'&=\gamma \left(A-{\frac {v\mathbf {n} \cdot \mathbf {Z} }{c}}\right)\,,\\\mathbf {Z} '&=\mathbf {Z} +(\gamma -1)(\mathbf {Z} \cdot \mathbf {n} )\mathbf {n} -{\frac {\gamma Av\mathbf {n} }{c}}\,.\end{aligned}}$

The decomposition of **Z** (and **Z**′) into components perpendicular and parallel to **v** is exactly the same as for the position vector, as is the process of obtaining the inverse transformations (exchange (*A*, **Z**) and (*A*′, **Z**′) to switch observed quantities, and reverse the direction of relative motion by the substitution **n** ↦ −**n**).

The quantities (*A*, **Z**) collectively make up a *four-vector*, where A is the "timelike component", and **Z** the "spacelike component". Examples of A and **Z** are the following:

| Four-vector | A | **Z** |
|---|---|---|
| position four-vector | time (multiplied by c), *ct* | position vector, **r** |
| four-momentum | energy (divided by c), *E*/*c* | momentum, **p** |
| Four-wave vector | angular frequency (divided by c), *ω*/*c* | wave vector, **k** |
| four-spin | (No name), *s**t* | spin, **s** |
| four-current | charge density (multiplied by c), *ρc* | current density, **j** |
| electromagnetic four-potential | electric potential (divided by c), *φ*/*c* | magnetic vector potential, **A** |

For a given object (e.g., particle, fluid, field, material), if A or **Z** correspond to properties specific to the object like its charge density, mass density, spin, etc., its properties can be fixed in the rest frame of that object. Then the Lorentz transformations give the corresponding properties in a frame moving relative to the object with constant velocity. This breaks some notions taken for granted in non-relativistic physics. For example, the energy E of an object is a scalar in non-relativistic mechanics, but not in relativistic mechanics because energy changes under Lorentz transformations; its value is different for various inertial frames. In the rest frame of an object, it has a rest energy and zero momentum. In a boosted frame its energy is different and it appears to have a momentum. Similarly, in non-relativistic quantum mechanics the spin of a particle is a constant vector, but in relativistic quantum mechanics spin **s** depends on relative motion. In the rest frame of the particle, the spin pseudovector can be fixed to be its ordinary non-relativistic spin with a zero timelike quantity *s**t*, however a boosted observer will perceive a nonzero timelike component and an altered spin.

Not all quantities are invariant in the form as shown above, for example orbital angular momentum **L** does not have a timelike quantity, and neither does the electric field **E** nor the magnetic field **B**. The definition of angular momentum is **L** = **r** × **p**, and in a boosted frame the altered angular momentum is **L**′ = **r**′ × **p**′. Applying this definition using the transformations of coordinates and momentum leads to the transformation of angular momentum. It turns out **L** transforms with another vector quantity **N** = (*E*/*c*2)**r** − *t***p** related to boosts, see *Relativistic angular momentum* for details. For the case of the **E** and **B** fields, the transformations cannot be obtained as directly using vector algebra. The Lorentz force is the definition of these fields, and in F it is **F** = *q*(**E** + **v** × **B**) while in F′ it is **F**′ = *q*(**E**′ + **v**′ × **B**′). A method of deriving the EM field transformations in an efficient way which also illustrates the unit of the electromagnetic field uses tensor algebra, given below.
