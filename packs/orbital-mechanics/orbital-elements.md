---
title: "Orbital elements"
source: https://en.wikipedia.org/wiki/Orbital_elements
domain: orbital-mechanics
license: CC-BY-SA-4.0
tags: orbital mechanics, hohmann transfer orbit, orbital elements, rocket equation
fetched: 2026-07-02
---

# Orbital elements

**Orbital elements** are the parameters required to uniquely identify a specific orbit. In celestial mechanics these elements are considered in two-body systems using a Kepler orbit. There are many different ways to mathematically describe the same orbit, but certain schemes are commonly used in astronomy and orbital mechanics.

A real orbit and its elements change over time due to gravitational perturbations by other objects and the effects of general relativity. A Kepler orbit is an idealized, mathematical approximation of the orbit at a particular time.

When viewed from an inertial frame, two orbiting bodies trace out distinct trajectories. Each of these trajectories has its focus at the common center of mass. When viewed from a non-inertial frame centered on one of the bodies, only the trajectory of the opposite body is apparent; Keplerian elements describe these non-inertial trajectories. An orbit has two sets of Keplerian elements depending on which body is used as the point of reference. The reference body (usually the most massive) is called the *primary*, the other body is called the *secondary*. The primary does not necessarily possess more mass than the secondary, and even when the bodies are of equal mass, the orbital elements depend on the choice of the primary.

Orbital elements can be obtained from orbital state vectors (position and velocity vectors of the orbiting object) by manual transformations or with computer software through a process known as orbit determination.

Non-closed orbits exist, although these are typically referred to as trajectories and not orbits, as they are not periodic. The same elements used to describe closed orbits can also typically be used to represent open trajectories.

## Required parameters

A set of six orbital elements are needed to unambiguously define a Keplerian orbit. This is because the problem contains six degrees of freedom. These correspond to the six parameters defined in a set of orbital state vectors: three spatial dimensions which define position (*x*, *y*, *z* in a Cartesian coordinate system), and the velocity in each of these dimensions. The orbiting object's trajectory is completely defined by the orbital state vectors, but this is often an inconvenient and opaque way to represent the orbit, which is why orbital elements are commonly used instead.

Such a set of 6 elements, however, only describes the starting position of the orbiting object and the shape of its trajectory. If one wants to use a set of orbital elements to solve Kepler's problem, two additional parameters must be included. This is to say, in order to solve for the position and velocity of the orbiting object at an arbitrary future time, an extended set of eight orbital elements will be required.

When describing an orbit with orbital elements, typically two are needed to describe the size and shape of the trajectory, three are needed to describe the rotation of the orbit, and one is needed to describe the starting position along the orbit. These can then be extended to include an element describing the speed of motion, and an element describing the time that the starting position occurs if position as a function of time needs to be solved.

## Common orbital elements by type

### Size- and shape-describing parameters

Two parameters are required to describe the size and the shape of an orbit. Generally any two of these values can be used to calculate any other (as described below), so the choice of which to use is one of preference and the particular use case.

- Eccentricity ( e ) — shape of the ellipse, describing how much it deviates from a perfect a circle. An eccentricity of 0 (zero) describes a perfect circle, values less than 1 describe an ellipse; a value of exactly 1 describes a parabola; values greater than 1 describe a hyperbola.
- Semi-major axis ( a ) — half the distance between the apoapsis and periapsis (long axis of the ellipse). This value is positive for elliptical orbits, undefined for parabolic trajectories, and negative for hyperbolic trajectories, which can hinder its usability when working with different types of trajectories.
- Semi-minor axis ( b ) — half the short axis through the geometric center of the ellipse. This value shares the same limitations as with the semi-major axis: it is undefined for parabolic trajectories and negative for hyperbolic trajectories.
- Semi-parameter ( p ) — half the width of the orbit perpendicular to the periapsis direction, crossing the primary focus (the orbital radius r for a true anomaly of  ⁠±+*π*/2⁠ radians, or  ±90° ). This value is useful for its use in the general orbit equation, which can return the distance from the central body given p and the true anomaly for any type of orbit or trajectory. This value is also commonly referred to as the semi-latus rectum and given the alternate symbol ℓ Additionally, this value will always be defined and positive unlike the semi-major and semi-minor axes.
- Apoapsis ( ra ) — the farthest point in the orbit from the central body (at a true anomaly of π radians, or  180° ). This quantity is undefined (or infinity) for parabolic and hyperbolic trajectories, as they continue moving away from the central body forever. This value is sometimes given the symbol Q.
- Periapsis ( *r*p ) — the closest point in the orbit from the central body (at a true anomaly of 0). Unlike with apoapsis, this quantity is defined for all orbit types. This value is sometimes given the symbol q.

For perfectly circular orbits, there is no distinct apoapsis or periapsis, as all points of the orbit have the same distance from the central body. Additionally, it is common to see the affix for "apoapsis" and "periapsis" changed depending on the central body (e.g. "apogee" and "perigee" for orbits of the Earth, and "aphelion" and "perihelion" for orbits of the Sun).

Other parameters can also be used to describe the size and shape of an orbit, such as the linear eccentricity, flattening, and focal parameter, but the use of these is limited.

#### Relations between elements

This section contains the common relations between these orbital elements, but more relations can be derived through manipulations of one or more of these equations. The variable names used here are consistent with the ones described above.

Eccentricity can be found using the semi-minor and semi-major axes as $e={\begin{cases}{\sqrt {\ 1-{\frac {\ b^{2}}{\ a^{2}}}~}}&~~{\mathsf {when}}~~a>0\quad {\mathsf {(ellipse)}}\ ,\\{\sqrt {\ 1+{\frac {\ b^{2}}{\ a^{2}}}~}}&~~{\mathsf {when}}~~a<0\quad {\mathsf {(hyperbola)}}~.\end{cases}}$

Eccentricity can also be found using the apoapsis and periapsis through the following relation: $e={\frac {r_{\mathsf {a}}-r_{\mathsf {p}}}{\ r_{\mathsf {a}}+r_{\mathsf {p}}\ }}~.$

The semi-major axis can be found using the fact that the lines that connects the apoapsis to the center of the conic and from the center to the periapsis both combined span the length of the conic, and thus the major axis. This is then divided by 2 to get the semi-major axis: $a={\frac {\ r_{\mathsf {p}}+r_{\mathsf {a}}\ }{2}}~.$

The semi-minor axis can be found using the semi-major axis and eccentricity through the following relations: $b~=~{\begin{cases}~a\;\!{\sqrt {\ 1-e^{2}~}}&~~{\mathsf {when}}~~e<1\quad {\mathsf {(ellipse)}}\ ,\\\\~a\;\!{\sqrt {\ e^{2}-1~}}&~~{\mathsf {when}}~~e>1\quad {\mathsf {(hyperbola)}}~.\end{cases}}$ Two formula are needed to avoid taking the square root of a negative number. Alternatively, use $~b=a\;\!{\sqrt {\;\!\left|1-e^{2}\right|~}}~.$

The semi-parameter can be found using the semi-major axis and eccentricity: $p=a\left(1-e^{2}\right)~.$

Apoapsis (for $\ e<1\$ ) can be found using the following equation using the semi-major axis and eccentricity: $r_{\mathsf {a}}=a\left(1+e\right)~.$

Periapsis can be found with the semi-major axis and eccentricity using the following equation: $r_{\mathsf {p}}=a\left(1-e\right)~.$

#### Element Animations

- Animations of orbits
- (Animation with constant semi-parameter ( p ) and changing eccentricity. Note how the semi-major and semi-minor axes approach infinity and then become negative as  e  exceeds 1.) Animation with constant semi-parameter ( p ) and changing eccentricity. Note how the semi-major and semi-minor axes approach infinity and then become negative as  e  exceeds 1.
- (Animation with constant periapsis ( rp ) and changing eccentricity.) Animation with constant periapsis ( rp ) and changing eccentricity.
- (Animation with constant semi-major axis ( a ) and changing eccentricity. The semi-major axis is made negative when  e  is greater than  1 . Note the discontinuity at   e = 1   . {\displaystyle \ e=1~.}) Animation with constant semi-major axis ( a ) and changing eccentricity. The semi-major axis is made negative when e is greater than 1. Note the discontinuity at $\ e=1~.$
- (Animation with constant semi-minor axis and changing eccentricity. The semi-minor axis is made negative when e) Animation with constant semi-minor axis and changing eccentricity. The semi-minor axis is made negative when e exceeds 1.

### Rotation-describing elements

Three parameters are required to describe the orientation of the plane of the orbit and the orientation of the orbit within that plane.

- Inclination ( i ) — vertical tilt of the orbital plane with respect to the reference plane, typically the equator of the central body, measured at the ascending node (where the orbit crosses the reference plane, represented by the green angle i in the diagram). Inclinations near zero indicate equatorial orbits, and inclinations near 90° indicate polar orbits. Inclinations from 90 to 180° are typically used to denote retrograde orbits.
- Longitude of the ascending node ( Ω ) — describes the angle from the ascending node of the orbit (☊ in the diagram) to the reference frame's reference direction (♈︎ in the diagram). This is measured in the reference plane, and is shown as the green angle Ω in the diagram. This quantity is undefined for perfectly equatorial (coplanar) orbits, but is often set to zero instead by convention. This quantity is also sometimes referred to as the right ascension of the ascending node (RAAN).
- Argument of periapsis ( ω ) — defines the orientation in the orbital plane, as an angle measured from the ascending node to the periapsis (the closest point the satellite body comes to the primary body around which it orbits), the purple angle ω in the diagram. This quantity is undefined for circular orbits, but is often set to zero instead by convention.

These three elements together can be described as Euler angles defining the orientation of the orbit relative to the reference coordinate system. Although these three are the most common, other elements do exist and are useful to describe other properties of the orbit.

- Longitude of periapsis ( ϖ ) — describes the angle between the vernal point and the periapsis, measured in the reference plane. This can be described as the sum of the longitude of the ascending node and the argument of periapsis: $\varpi =\Omega +\omega$ . Unlike the longitude of the ascending node, this value is defined for orbits where the inclination is zero.

### Elements describing motion over time

One parameter is required to describe the speed of motion of the orbiting object around the central body. However, this can be omitted if only a description of the shape of the orbit is required. Various quantities that do not directly describe a speed can be used to satisfy this condition, and it is possible to convert from one to any other (formula below).

- Mean motion ( n ) — quantity that describes the average angular speed of the orbiting body, measured as an angle per unit time. For non-circular orbits, the actual angular speed is not constant, so the mean motion will not describe a physical angle. Instead this corresponds to a change in the mean anomaly, which indeed increases linearly with time.
- Orbital period ( P ) — the time it takes for the orbiting body to complete one full revolution around the central body. This quantity is undefined for parabolic and hyperbolic trajectories, as they are non-periodic.
- Mass of the 2-body system ( M ) — the total mass of the central body and orbiting body ( ${\textstyle m_{1}+m_{2}}$ ). If the mass of the orbiting object is insignificant compared to the mass of the primary (e.g. for artificial satellites in orbit of a massive planet), then the mass of the central body only can be used.
- Standard gravitational parameter ( μ ) — quantity equal to the mass of the 2-body system ( M ) (or of only the central body if the mass of the orbiting object is insignificant) times the gravitational constant G. This quantity is often used instead of mass, as it can be easier to measure with precision than either mass or G. This is also often not included as part of orbital element lists, as in some cases it can assumed to be known based on the central body.

#### Relations between elements

This section contains the common relations between the set of orbital elements described above, but more relations can be derived through manipulations of one or more of these equations. The variable names used here are consistent with the ones described above.

Mean motion can be calculated using the standard gravitational parameter and the semi-major axis of the orbit. $n~={\sqrt {\;\!{\frac {\mu }{\ |a|^{3}}}~}}~.$ This equation returns the mean motion in radians and will need to be converted if n is desired to be in a different unit.

Because the semi-major axis is related to the mean motion and standard gravitational parameter, it can be calculated without being specified. This is especially useful if μ is assumed to be known, as then n can be used to calculate a, and likewise for specifying a. This can allow one less element to specified.

Orbital period can be found from n given the fact that the mean motion can be described as a frequency (number of orbits per unit time), which is the reciprocal of period: $P={\begin{cases}~~{\dfrac {\;\!2\pi \;\!}{n}}&{\mathsf {if}}~~n~~{\mathsf {is\ in\ radians}}\ ;\\\\{\dfrac {\ 360^{\circ }\;\!}{n}}&{\mathsf {if}}~~n~~{\mathsf {is\ in\ degrees}}~.\end{cases}}$

The standard gravitational parameter can be found given the mean motion and the semi-major axis through the following relation (assuming that n is in radians): $\mu =n^{2}a^{3}~.$

The mass of the 2-body system (or of the central body) ( M ) can be found given the standard gravitational parameter using a rearrangement of its definition as the product of the mass and the gravitational constant, $M={\frac {\ \mu \ }{G}}~.$

### Epoch-describing elements

Two elements are needed to describe the position of the body around its orbit and the time at which this occurs. If this time is defined to be at a point where the specific position variable is a designated constant (usually zero), then it does not need to be specified.

- Epoch ( *t*0 ) — time at which one of the below elements is defined. Alternatively this is the point in time where the orbital elements were measured. Sometimes the epoch time is considered as part of the reference frame and is not listed as a distinct element.
- Time of periapsis passage ( *T*0 ) — time at which the orbiting body is at periapsis. This is also when the mean anomaly and true anomaly (and others) are zero, so they do not need to be defined. This value is not defined for circular orbits, as they do not have a uniquely defined point of periapsis.
- Mean anomaly at epoch ( *M*0 ) — mean anomaly at the epoch time. Mean anomaly is a mathematically convenient angle that increases linearly with time as if the orbit were perfectly circular. Zero is defined as being at periapsis, and one period spans 2π radians. The rate at which the mean anomaly increases is equal to the mean motion n. Because this angle is relative to periapsis, it is not defined for circular orbits.
- Mean longitude at epoch ( *L*0 ) — mean longitude at the epoch time. Mean longitude is similar to mean anomaly, in that it increases linearly with time and does not represent the real angular displacement. Unlike with mean anomaly, mean longitude is defined relative to the vernal point, which means it is defined for circular orbits.
- Eccentric anomaly at epoch ( *E*0 ) — the eccentric anomaly at the epoch time. Eccentric anomaly is defined at the angular displacement along the auxiliary circle of the ellipse (circle tangent to the ellipse both at apses). This value takes into account the varying speed of objects in elliptical orbits, but does not account for the elliptical shape of the orbit. As such, it still does not correspond to the real angular displacement of the orbiting body. Like with mean anomaly and true anomaly, the eccentric anomaly is measured relative to periapsis and is not defined for circular orbits. The eccentric anomaly is also not defined for parabolic and hyperbolic trajectories, and instead the parabolic anomaly or hyperbolic anomaly are used.
- True anomaly at epoch ( *t*0 ) — angle that represents the real angular displacement of the orbiting body at the epoch time, taking into account the varying speed and elliptical shape of an orbit. Like with mean anomaly, true anomaly is measured relative to periapsis and thus it has the same limitations with circular orbits.
- True longitude at epoch ( *l*0 ) — the angular displacement of the orbiting body at the epoch time. Unlike with the true anomaly, the true longitude is measured relative to the vernal point, so it can be defined for circular orbits.
- Mean argument of latitude ( *u*M0 ) at epoch — the angular displacement of the orbiting body at the epoch time. Mean argument of latitude is similar to the mean anomaly and mean longitude, but instead it is measured relative to the ascending node. This means while it is well defined for circular orbits, it is not for equatorial orbits.
- Argument of latitude at epoch ( *u*0 ) — the angular displacement of the orbiting body at the epoch time. This angle is measured relative to the ascending node, so while it is defined for circular orbits, it is not defined for equatorial orbits.

These elements are also used to describe the position of an object in its orbit in a more general context and are not limited to describing the state at an epoch time.

#### Relations between elements

This section contains the common relations between the set of orbital elements described above, but more relations can be derived through manipulations of one or more of these equations. The variable names used here are consistent with the ones described above. These formulae also hold true for conversions between these elements in general. (Note break in notation:  M  is redefined to now represent the mean anomaly, instead of the mass of the central body, as above.)

Epoch can be found given the time of periapsis passage, the mean anomaly at epoch, and mean motion: $t_{0}\ =\ T_{0}+{\frac {\ M_{0}}{n}}~.$

Time of periapsis passage can be found from the epoch, mean anomaly at epoch, and mean motion by re-arranging the previous equation: $T_{0}\ =\ t_{0}-{\frac {\ M_{0}}{n}}~.$

Mean anomaly can be found from the eccentric anomaly and eccentricity using Kepler's equation: $M\ =\ E-e\sin E~.$

Mean longitude can be found using the mean anomaly at epoch and the longitude of periapsis: $L\ =\ M+\varpi \ ,\qquad {\mathsf {or}}\qquad L\ =\ M+\omega +\Omega ~.$

Eccentric anomaly can be found with the mean anomaly and eccentricity using Kepler's equation $E\ =\ M+e\sin E$ through various means, such as iterative calculations or numerical solutions (for some values of e). It can be solved through a root-finding algorithm, usually Newton's method: $E_{k+1}~=~E_{k}\ +\ {\frac {\ M-E_{k}+e\sin(E_{k})\ }{1-e\cos(E_{k})}}~.$

Typically a starting guess of either $\ M\ ,$ $\ M-e\ ,$ $\ M+e\ ,$ or $\ M+e\sin M\$ are used. This iteration can be repeated until a desired level of tolerance is reached.

True anomaly can be found from the eccentric anomaly using the following relations: ${\begin{aligned}\sin \nu \ &=\ {\frac {\ {\sqrt {1-e^{2}\ }}\sin E\ }{1-e\cos E}}\ ,\\\\\cos \nu \ &=\ {\frac {\cos E-e}{\ 1-e\cos E\ }}~.\end{aligned}}$ The quadrant of the solution can be resolved using an atan2(*y*, *x*) function.

True longitude can be found using the true anomaly and longitude of periapsis: $l\ =\ \nu +\varpi \ ,\qquad {\mathsf {or}}\qquad l\ =\ \nu +\omega +\Omega ~.$

Mean argument of latitude can be calculated using the mean anomaly and argument of periapsis: $u_{M}\ =\ \Omega +M~.$

Argument of latitude can be found using the true anomaly and argument of periapsis: $u\ =\ \nu +\Omega ~.$

## Common sets of elements

### Classical Keplerian elements

While in theory, any set of elements that meets the requirements above can be used to describe an orbit, in practice, certain sets are much more common than others.

The most common elements used to describe the size and shape of the orbit are the semi-major axis (a) and the eccentricity (e). Sometimes the semi-parameter (p) is used instead of the semi-major axis, as the semi-major axis experiences a singularity for parabolic trajectories, and thus cannot be used for this case.

It is common to specify the period (P) or mean motion (n) instead of the semi-major axis in Keplerian element sets, as each can be computed from the other provided the standard gravitational parameter ( $\mu$ ) is known for the central body though the relations above.

For the epoch, the epoch time (t) along with the mean anomaly (*M*0), mean longitude (*L*0), true anomaly ( $\nu _{0}$ ) or (more rarely) the eccentric anomaly (*E*0) are often used. The time of periapsis passage (*T*0) is also sometimes used for this purpose, since using it eliminates the need to specify position at the epoch.

It is also quite common to see either the mean anomaly or the mean longitude expressed directly, without either *M*0 or *L*0 as intermediary steps, as a linear function of time: $M(t)=M_{0}+n(t-t_{0}).$ This method of expression consolidates the mean motion as the slope of this linear equation.

### Elements by body type

The choice of elements can differ depending on the type of astronomical body. The eccentricity (*e*) and either the semi-major axis (*a*) or the distance of periapsis (*q*) are used to specify the shape and size of an orbit. The longitude of the ascending node (Ω) the inclination (*i*) and the argument of periapsis (*ω*) or the longitude of periapsis (*ϖ*) specify the orientation of the orbit in its plane. Either the Mean longitude at epoch (*L*0) the mean anomaly at epoch (*M*0) or the time of periapsis passage (*T*0) are used to specify a known point in the orbit. The choices made depend whether the vernal equinox or the node are used as the primary reference.

| Object | Elements used |
|---|---|
| Major planet | *e*, *a*, *i*, Ω, *ϖ*, *L*0 |
| Comet | *e*, *q*, *i*, Ω, *ω*, *T*0 |
| Asteroid | *e*, *a*, *i*, Ω, *ω*, *M*0 |

### Two-line elements

Orbital elements can be encoded as text in a number of formats. The most common of them is the NASA / NORAD **"two-line elements"** (TLE) format, originally designed for use with 80-column punched cards, but still in use because it is the most common format, and 80-character ASCII records can be handled efficiently by modern databases.

The two-line element format lists the eccentricity (e), inclination (i), longitude of the ascending node (Ω), argument of periapsis (ω), mean motion (n), epoch (*t*0), and mean anomaly at epoch (*M*0). Since the format is primarily meant for orbits of the Earth, the standard gravitational parameter (μ), can be assumed and used to calculate the semi-major axis with the mean motion via the relations above.

Depending on the application and object orbit, the data derived from TLEs older than 30 days can become unreliable. Orbital positions can be calculated from TLEs through simplified perturbations models (SGP4 / SDP4 / SGP8 / SDP8).

Example of a two-line element for the SORCE satellite:

```
1 27651U 03004A   07269.09107561  .00000015  00000-0  17636-4 0  4191
2 27651 039.9956 188.8112 0026975 282.9289 076.8483 14.81973121252789
```

### Delaunay variables

The Delaunay orbital elements were introduced by Charles-Eugène Delaunay during his study of the motion of the Moon. Commonly called *Delaunay variables*, they are a set of canonical variables, which are action-angle coordinates. The angles are simple sums of some of the Keplerian angles and are often referred to with different symbols than in other applications:

- the mean anomaly: $\ell =M$ ,
- the argument of periapsis: $g=\omega$ ,
- the longitude of the ascending node: $h=\Omega$ ,

along with their respective conjugate momenta L, G, and H. The momenta L, G, and H are the *action* variables and are more elaborate combinations of the Keplerian elements a, e, and i.

Delaunay variables are used to simplify perturbative calculations in celestial mechanics, for example, while investigating the Kozai–Lidov oscillations in hierarchical triple systems. The advantage of the Delaunay variables is that they remain well defined and non-singular (except for h, which can be tolerated) even for circular and equatorial orbits.

## Perturbations and elemental variance

Unperturbed, two-body, Newtonian orbits are always conic sections, so the Keplerian elements define an unchanging ellipse, parabola, or hyperbola. Real orbits have perturbations, so a given set of Keplerian elements accurately describes an orbit only at the epoch. Evolution of the orbital elements takes place due to the gravitational pull of bodies other than the primary, the non-sphericity of the primary, atmospheric drag, relativistic effects, radiation pressure, electromagnetic forces, and so on.

Keplerian elements can be used to produce useful predictions of a location of a moving body on its orbit. Perturbed trajectories can be modeled as a sequence of Keplerian orbits. Usually, these instantaneous orbits are chosen to be osculating. This means that they osculate ("kiss" or touch) the real trajectory. The evolution of the orbital elements defining instantaneous orbits is described by the so-called planetary equations, differential equations which come in different forms developed by Lagrange, Gauss, Delaunay, Poincaré, or Hill.

Be mindful that in some situations planetary equations in at least two standard types of orbital elements (Lagrange-type or Delaunay-type), when perturbed, produce elements that turn out to be non-osculating.
