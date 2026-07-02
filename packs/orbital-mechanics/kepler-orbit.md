---
title: "Kepler orbit"
source: https://en.wikipedia.org/wiki/Kepler_orbit
domain: orbital-mechanics
license: CC-BY-SA-4.0
tags: orbital mechanics, hohmann transfer orbit, orbital elements, rocket equation
fetched: 2026-07-02
---

# Kepler orbit

In celestial mechanics, a **Kepler orbit** (or **Keplerian orbit**, named after the German astronomer Johannes Kepler) is the motion of one body relative to another, in the form of an ellipse, parabola, or hyperbola, which forms a two-dimensional orbital plane in three-dimensional space. A Kepler orbit can also tend toward a straight line. It considers only the point-like gravitational attraction of two bodies, neglecting perturbations due to gravitational interactions with other objects, atmospheric drag, solar radiation pressure, a non-spherical central body, and so on. It is thus said to be a solution of a special case of the two-body problem, known as the Kepler problem. As a theory in classical mechanics, it also does not take into account the effects of general relativity. Keplerian orbits can be parameterized into six orbital elements in various ways.

In most applications, there is a large central body, the center of mass of which is assumed to be the center of mass of the entire system. The orbits of two objects of similar mass can be described as Kepler orbits around their common center of mass, their barycenter.

## Introduction

From ancient times until the 16th and 17th centuries, the motions of the planets were believed to follow perfectly circular geocentric paths as taught by the ancient Greek philosophers Aristotle and Ptolemy. Variations in the motions of the planets were explained by smaller circular paths overlaid on the larger path (see epicycle). As measurements of the planets became increasingly accurate, revisions to the theory were proposed. In 1543, Nicolaus Copernicus published a heliocentric model of the Solar System, although he still believed that the planets traveled in perfectly circular paths centered on the Sun.

## Development of the laws

In 1601, Johannes Kepler acquired the extensive, meticulous observations of the planets made by Tycho Brahe. Kepler would spend the next five years trying to fit the observations of the planet Mars to various curves. In 1609, Kepler published the first two of his three laws of planetary motion. The first law states:

> The orbit of every planet is an ellipse with the sun at a focus.

More generally, the path of an object undergoing Keplerian motion may also follow a parabola or a hyperbola, which, along with ellipses, belong to a group of curves known as conic sections. Mathematically, the distance between a central body and an orbiting body can be expressed as:

$r(\theta )={\frac {a(1-e^{2})}{1+e\cos(\theta )}}$

where:

- r is the distance
- a is the semi-major axis, which defines the size of the orbit
- e is the eccentricity, which defines the shape of the orbit
- $\theta$ is the true anomaly, which is the angle between the current position of the orbiting object and the location in the orbit at which it is closest to the central body (called the periapsis).

Alternately, the equation can be expressed as:

$r(\theta )={\frac {p}{1+e\cos(\theta )}}$

Where p is called the semi-latus rectum of the curve. This form of the equation is particularly useful when dealing with parabolic trajectories, for which the semi-major axis is infinite.

Despite developing these laws from observations, Kepler was never able to develop a theory to explain these motions. Isaac Newton produced the first such theory based around the concept of gravity. Albert Einstein's general relativity is the current description of gravitation in modern physics. The two-body problem in general relativity has no closed-form solutions.

### Isaac Newton

Between 1665 and 1666, Isaac Newton developed several concepts related to motion, gravitation and differential calculus. However, these concepts were not published until 1687 in the Principia, in which he outlined his laws of motion and his law of universal gravitation. His second of his three laws of motion states:

> The acceleration of a body is parallel and directly proportional to the net force acting on the body, is in the direction of the net force, and is inversely proportional to the mass of the body:
> 
> $\mathbf {F} =m\mathbf {a} =m{\frac {d^{2}\mathbf {r} }{dt^{2}}}$
> 
> Where:
> 
> - $\mathbf {F}$ is the force vector
> - m is the mass of the body on which the force is acting
> - $\mathbf {a}$ is the acceleration vector, the second time derivative of the position vector $\mathbf {r}$

Strictly speaking, this form of the equation only applies to an object of constant mass, which holds true based on the simplifying assumptions made below.

Newton's law of gravitation states:

> Every point mass attracts every other point mass by a force pointing along the line intersecting both points. The force is proportional to the product of the two masses and inversely proportional to the square of the distance between the point masses:
> 
> $F=G{\frac {m_{1}m_{2}}{r^{2}}}$
> 
> where:
> 
> - F is the magnitude of the gravitational force between the two point masses
> - G is the gravitational constant
> - $m_{1}$ is the mass of the first point mass
> - $m_{2}$ is the mass of the second point mass
> - r is the distance between the two point masses

From the laws of motion and the law of universal gravitation, Newton was able to derive Kepler's laws, which are specific to orbital motion in astronomy. Since Kepler's laws were well-supported by observation data, this consistency provided strong support of the validity of Newton's generalized theory, and unified celestial and ordinary mechanics. These laws of motion formed the basis of modern celestial mechanics until Albert Einstein introduced the concepts of special and general relativity in the early 20th century. For most applications, Keplerian motion approximates the motions of planets and satellites to relatively high degrees of accuracy and is used extensively in astronomy and astrodynamics.

### Simplified two body problem

To solve for the motion of an object in a two body system, two simplifying assumptions can be made:

1. The bodies are spherically symmetric and can be treated as point masses.
2. There are no external or internal forces acting upon the bodies other than their mutual gravitation.

The shapes of large celestial bodies are close to spheres. By symmetry, the net gravitational force attracting a mass point towards a homogeneous sphere must be directed towards its centre. The shell theorem (also proven by Isaac Newton) states that the magnitude of this force is the same as if all mass was concentrated in the middle of the sphere, even if the density of the sphere varies with depth (as it does for most celestial bodies). From this immediately follows that the attraction between two homogeneous spheres is as if both had its mass concentrated to its center.

Smaller objects, like asteroids or spacecraft often have a shape strongly deviating from a sphere. But the gravitational forces produced by these irregularities are generally small compared to the gravity of the central body. The difference between an irregular shape and a perfect sphere also diminishes with distances, and most orbital distances are very large when compared with the diameter of a small orbiting body. Thus for some applications, shape irregularity can be neglected without significant impact on accuracy. This effect is quite noticeable for artificial Earth satellites, especially those in low orbits.

Planets rotate at varying rates and thus may take a slightly oblate shape because of the centrifugal force. With such an oblate shape, the gravitational attraction will deviate somewhat from that of a homogeneous sphere. At larger distances the effect of this oblateness becomes negligible. Planetary motions in the Solar System can be computed with sufficient precision if they are treated as point masses.

Two point mass objects with masses $m_{1}$ and $m_{2}$ and position vectors $\mathbf {r} _{1}$ and $\mathbf {r} _{2}$ relative to some inertial reference frame experience gravitational forces:

$m_{1}{\ddot {\mathbf {r} }}_{1}={\frac {-Gm_{1}m_{2}}{r^{2}}}\mathbf {\hat {r}}$ $m_{2}{\ddot {\mathbf {r} }}_{2}={\frac {Gm_{1}m_{2}}{r^{2}}}\mathbf {\hat {r}}$

where $\mathbf {r}$ is the relative position vector of mass 1 with respect to mass 2, expressed as:

$\mathbf {r} =\mathbf {r} _{1}-\mathbf {r} _{2}$

and $\mathbf {\hat {r}}$ is the unit vector in that direction and r is the length of that vector.

Dividing by their respective masses and subtracting the second equation from the first yields the equation of motion for the acceleration of the first object with respect to the second:

| ${\ddot {\mathbf {r} }}=-{\frac {\alpha }{r^{2}}}\mathbf {\hat {r}}$ |   | 1 |
|---|---|---|

where $\alpha$ is the gravitational parameter and is equal to

$\alpha =G(m_{1}+m_{2})$

In many applications, a third simplifying assumption can be made:

When compared to the central body, the mass of the orbiting body is insignificant. Mathematically,

m

1

>>

m

2

, so

α

=

G

(

m

1

+

m

2

) ≈

Gm

1

. Such

standard gravitational parameters

, often denoted as

$\mu =G\,M$

, are widely available for Sun, major planets and Moon, which have much larger masses

M

than their orbiting satellites.

This assumption is not necessary to solve the simplified two body problem, but it simplifies calculations, particularly with Earth-orbiting satellites and planets orbiting the Sun. Even Jupiter's mass is less than the Sun's by a factor of 1047, which would constitute an error of 0.096% in the value of α. Notable exceptions include the Earth-Moon system (mass ratio of 81.3), the Pluto-Charon system (mass ratio of 8.9) and binary star systems. Under these assumptions the differential equation for the two body case can be completely solved mathematically and the resulting orbit which follows Kepler's laws of planetary motion is called a "Kepler orbit". The orbits of all planets are to high accuracy Kepler orbits around the Sun. The small deviations are due to the much weaker gravitational attractions between the planets, and in the case of Mercury, due to general relativity. The orbits of the artificial satellites around the Earth are, with a fair approximation, Kepler orbits with small perturbations due to the gravitational attraction of the Sun, the Moon and the oblateness of the Earth. In high accuracy applications for which the equation of motion must be integrated numerically with all gravitational and non-gravitational forces (such as solar radiation pressure and atmospheric drag) being taken into account, the Kepler orbit concepts are of paramount importance and heavily used.

### Keplerian elements

Any Keplerian trajectory can be defined by six parameters. The motion of an object moving in three-dimensional space is characterized by a position vector and a velocity vector. Each vector has three components, so the total number of values needed to define a trajectory through space is six. An orbit is generally defined by six elements (known as *Keplerian elements*) that can be computed from position and velocity, three of which have already been discussed. These elements are convenient in that of the six, five are unchanging for an unperturbed orbit (a stark contrast to two constantly changing vectors). The future location of an object within its orbit can be predicted and its new position and velocity can be easily obtained from the orbital elements.

Two define the size and shape of the trajectory:

- Semimajor axis ( a )
- Eccentricity ( e )

Three define the orientation of the orbital plane:

- Inclination ( i ) defines the angle between the orbital plane and the reference plane.
- Longitude of the ascending node ( $\Omega$ ) defines the angle between the reference direction and the upward crossing of the orbit on the reference plane (the ascending node).
- Argument of periapsis ( $\omega$ ) defines the angle between the ascending node and the periapsis.

And finally:

- True anomaly ( $\nu$ ) defines the position of the orbiting body along the trajectory, measured from periapsis. Several alternate values can be used instead of true anomaly, the most common being M the mean anomaly and T , the time since periapsis.

Because i , $\Omega$ and $\omega$ are simply angular measurements defining the orientation of the trajectory in the reference frame, they are not strictly necessary when discussing the motion of the object within the orbital plane. They have been mentioned here for completeness, but are not required for the proofs below.

### Mathematical solution of the differential equation (**1**) above

For movement under any central force, i.e. a force parallel to **r**, the specific relative angular momentum $\mathbf {H} =\mathbf {r} \times {\dot {\mathbf {r} }}$ stays constant: ${\dot {\mathbf {H} }}={\frac {d}{dt}}\left(\mathbf {r} \times {\dot {\mathbf {r} }}\right)={\dot {\mathbf {r} }}\times {\dot {\mathbf {r} }}+\mathbf {r} \times {\ddot {\mathbf {r} }}=\mathbf {0} +\mathbf {0} =\mathbf {0}$

Since the cross product of the position vector and its velocity stays constant, they must lie in the same plane, orthogonal to $\mathbf {H}$ . This implies the vector function is a plane curve.

Because the equation has symmetry around its origin, it is easier to solve in polar coordinates. However, equation (**1**) refers to linear acceleration $\left({\ddot {\mathbf {r} }}\right),$ as opposed to angular $\left({\ddot {\theta }}\right)$ or radial $\left({\ddot {r}}\right)$ acceleration. Therefore, one must be cautious when transforming the equation. Introducing a cartesian coordinate system $({\hat {\mathbf {x} }},{\hat {\mathbf {y} }})$ and polar unit vectors $({\hat {\mathbf {r} }},{\hat {\mathbf {q} }})$ in the plane orthogonal to $\mathbf {H}$ :

${\begin{aligned}{\hat {\mathbf {r} }}&=\cos {\theta }{\hat {\mathbf {x} }}+\sin {\theta }{\hat {\mathbf {y} }}\\{\hat {\mathbf {q} }}&=-\sin {\theta }{\hat {\mathbf {x} }}+\cos {\theta }{\hat {\mathbf {y} }}\end{aligned}}$

The vector function $\mathbf {r}$ and its derivatives can now be rewritten as:

${\begin{aligned}\mathbf {r} &=r\left(\cos \theta {\hat {\mathbf {x} }}+\sin \theta {\hat {\mathbf {y} }}\right)=r{\hat {\mathbf {r} }}\\{\dot {\mathbf {r} }}&={\dot {r}}{\hat {\mathbf {r} }}+r{\dot {\theta }}{\hat {\mathbf {q} }}\\{\ddot {\mathbf {r} }}&=\left({\ddot {r}}-r{\dot {\theta }}^{2}\right){\hat {\mathbf {r} }}+\left(r{\ddot {\theta }}+2{\dot {r}}{\dot {\theta }}\right){\hat {\mathbf {q} }}\end{aligned}}$

(see "Vector calculus"). Substituting these into (**1**) yields: $\left({\ddot {r}}-r{\dot {\theta }}^{2}\right){\hat {\mathbf {r} }}+\left(r{\ddot {\theta }}+2{\dot {r}}{\dot {\theta }}\right){\hat {\mathbf {q} }}=\left(-{\frac {\alpha }{r^{2}}}\right){\hat {\mathbf {r} }}+(0){\hat {\mathbf {q} }}$

This gives the ordinary differential equation in the two variables r and $\theta$ :

| ${\ddot {r}}-r{\dot {\theta }}^{2}=-{\frac {\alpha }{r^{2}}}$ |   | 2 |
|---|---|---|

In order to solve this equation, all time derivatives must be eliminated. This brings: $H=|\mathbf {r} \times {\dot {\mathbf {r} }}|=\left|{\begin{pmatrix}r\cos(\theta )\\r\sin(\theta )\\0\end{pmatrix}}\times {\begin{pmatrix}{\dot {r}}\cos(\theta )-r\sin(\theta ){\dot {\theta }}\\{\dot {r}}\sin(\theta )+r\cos(\theta ){\dot {\theta }}\\0\end{pmatrix}}\right|=\left|{\begin{pmatrix}0\\0\\r^{2}{\dot {\theta }}\end{pmatrix}}\right|=r^{2}{\dot {\theta }}$

| ${\dot {\theta }}={\frac {H}{r^{2}}}$ |   | 3 |
|---|---|---|

Taking the time derivative of (**3**) gets

| ${\ddot {\theta }}=-{\frac {2\cdot H\cdot {\dot {r}}}{r^{3}}}$ |   | 4 |
|---|---|---|

Equations (**3**) and (**4**) can be used to eliminate the time derivatives of $\theta$ . In order to eliminate the time derivatives of r , the chain rule is used to find appropriate substitutions:

| ${\dot {r}}={\frac {dr}{d\theta }}\cdot {\dot {\theta }}$ |   | 5 |
|---|---|---|

| ${\ddot {r}}={\frac {d^{2}r}{d\theta ^{2}}}\cdot {\dot {\theta }}^{2}+{\frac {dr}{d\theta }}\cdot {\ddot {\theta }}$ |   | 6 |
|---|---|---|

Using these four substitutions, all time derivatives in (**2**) can be eliminated, yielding an ordinary differential equation for r as function of $\theta .$ ${\ddot {r}}-r{\dot {\theta }}^{2}=-{\frac {\alpha }{r^{2}}}$ ${\frac {d^{2}r}{d\theta ^{2}}}\cdot {\dot {\theta }}^{2}+{\frac {dr}{d\theta }}\cdot {\ddot {\theta }}-r{\dot {\theta }}^{2}=-{\frac {\alpha }{r^{2}}}$ ${\frac {d^{2}r}{d\theta ^{2}}}\cdot \left({\frac {H}{r^{2}}}\right)^{2}+{\frac {dr}{d\theta }}\cdot \left(-{\frac {2\cdot H\cdot {\dot {r}}}{r^{3}}}\right)-r\left({\frac {H}{r^{2}}}\right)^{2}=-{\frac {\alpha }{r^{2}}}$

| ${\frac {H^{2}}{r^{4}}}\cdot \left({\frac {d^{2}r}{d\theta ^{2}}}-2\cdot {\frac {\left({\frac {dr}{d\theta }}\right)^{2}}{r}}-r\right)=-{\frac {\alpha }{r^{2}}}$ |   | 7 |
|---|---|---|

The differential equation (**7**) can be solved analytically by the variable substitution

| $r={\frac {1}{s}}$ |   | 8 |
|---|---|---|

Using the chain rule for differentiation gets:

| ${\frac {dr}{d\theta }}=-{\frac {1}{s^{2}}}\cdot {\frac {ds}{d\theta }}$ |   | 9 |
|---|---|---|

| ${\frac {d^{2}r}{d\theta ^{2}}}={\frac {2}{s^{3}}}\cdot \left({\frac {ds}{d\theta }}\right)^{2}-{\frac {1}{s^{2}}}\cdot {\frac {d^{2}s}{d\theta ^{2}}}$ |   | 10 |
|---|---|---|

Using the expressions (**10**) and (**9**) for ${\frac {d^{2}r}{d\theta ^{2}}}$ and ${\frac {dr}{d\theta }}$ gets

| $H^{2}\cdot \left({\frac {d^{2}s}{d\theta ^{2}}}+s\right)=\alpha$ |   | 11 |
|---|---|---|

with the general solution

| $s={\frac {\alpha }{H^{2}}}\cdot \left(1+e\cdot \cos(\theta -\theta _{0})\right)$ |   | 12 |
|---|---|---|

where *e* and $\theta _{0}$ are constants of integration depending on the initial values for *s* and ${\tfrac {ds}{d\theta }}.$

Instead of using the constant of integration $\theta _{0}$ explicitly one introduces the convention that the unit vectors ${\hat {x}},{\hat {y}}$ defining the coordinate system in the orbital plane are selected such that $\theta _{0}$ takes the value zero and *e* is positive. This then means that $\theta$ is zero at the point where s is maximal and therefore $r={\tfrac {1}{s}}$ is minimal. Defining the parameter *p* as ${\tfrac {H^{2}}{\alpha }}$ one has that

$r={\frac {1}{s}}={\frac {p}{1+e\cdot \cos \theta }}$

#### Alternate derivation

Another way to solve this equation without the use of polar differential equations is as follows:

Define a unit vector $\mathbf {u}$ , $\mathbf {u} ={\frac {\mathbf {r} }{r}}$ , such that $\mathbf {r} =r\mathbf {u}$ and ${\ddot {\mathbf {r} }}=-{\tfrac {\alpha }{r^{2}}}\mathbf {u}$ . It follows that $\mathbf {H} =\mathbf {r} \times {\dot {\mathbf {r} }}=r\mathbf {u} \times {\frac {d}{dt}}(r\mathbf {u} )=r\mathbf {u} \times (r{\dot {\mathbf {u} }}+{\dot {r}}\mathbf {u} )=r^{2}(\mathbf {u} \times {\dot {\mathbf {u} }})+r{\dot {r}}(\mathbf {u} \times \mathbf {u} )=r^{2}\mathbf {u} \times {\dot {\mathbf {u} }}$

Now consider ${\ddot {\mathbf {r} }}\times \mathbf {H} =-{\frac {\alpha }{r^{2}}}\mathbf {u} \times (r^{2}\mathbf {u} \times {\dot {\mathbf {u} }})=-\alpha \mathbf {u} \times (\mathbf {u} \times {\dot {\mathbf {u} }})=-\alpha [(\mathbf {u} \cdot {\dot {\mathbf {u} }})\mathbf {u} -(\mathbf {u} \cdot \mathbf {u} ){\dot {\mathbf {u} }}]$

(see Vector triple product). Notice that $\mathbf {u} \cdot \mathbf {u} =|\mathbf {u} |^{2}=1$ $\mathbf {u} \cdot {\dot {\mathbf {u} }}={\frac {1}{2}}(\mathbf {u} \cdot {\dot {\mathbf {u} }}+{\dot {\mathbf {u} }}\cdot \mathbf {u} )={\frac {1}{2}}{\frac {d}{dt}}(\mathbf {u} \cdot \mathbf {u} )=0$

Substituting these values into the previous equation gives: ${\ddot {\mathbf {r} }}\times \mathbf {H} =\alpha {\dot {\mathbf {u} }}$

Integrating both sides: ${\dot {\mathbf {r} }}\times \mathbf {H} =\alpha \mathbf {u} +\mathbf {c}$

where **c** is a constant vector. Dotting this with **r** yields an interesting result: $\mathbf {r} \cdot ({\dot {\mathbf {r} }}\times \mathbf {H} )=\mathbf {r} \cdot (\alpha \mathbf {u} +\mathbf {c} )=\alpha \mathbf {r} \cdot \mathbf {u} +\mathbf {r} \cdot \mathbf {c} =\alpha r(\mathbf {u} \cdot \mathbf {u} )+rc\cos(\theta )=r(\alpha +c\cos(\theta ))$ where $\theta$ is the angle between $\mathbf {r}$ and $\mathbf {c}$ . Solving for *r* : $r={\frac {\mathbf {r} \cdot ({\dot {\mathbf {r} }}\times \mathbf {H} )}{\alpha +c\cos(\theta )}}={\frac {(\mathbf {r} \times {\dot {\mathbf {r} }})\cdot \mathbf {H} }{\alpha +c\cos(\theta )}}={\frac {|\mathbf {H} |^{2}}{\alpha +c\cos(\theta )}}={\frac {|\mathbf {H} |^{2}/\alpha }{1+(c/\alpha )\cos(\theta )}}.$

Notice that $(r,\theta )$ are effectively the polar coordinates of the vector function. Making the substitutions $p={\tfrac {|\mathbf {H} |^{2}}{\alpha }}$ and $e={\tfrac {c}{\alpha }}$ , again results in the equation

| $r={\frac {p}{1+e\cdot \cos \theta }}$ |   | 13 |
|---|---|---|

This is the equation in polar coordinates for a conic section with origin in a focal point. The argument $\theta$ is called "true anomaly".

#### Eccentricity Vector

Notice also that, since $\theta$ is the angle between the position vector $\mathbf {r}$ and the integration constant $\mathbf {c}$ , the vector $\mathbf {c}$ must be pointing in the direction of the **periapsis** of the orbit. Then, the **eccentricity vector** associated with the orbit can be defined as: $\mathbf {e} \triangleq {\frac {\mathbf {c} }{\alpha }}={\frac {{\dot {\mathbf {r} }}\times \mathbf {H} }{\alpha }}-\mathbf {u} ={\frac {\mathbf {v} \times \mathbf {H} }{\alpha }}-{\frac {\mathbf {r} }{r}}={\frac {\mathbf {v} \times (\mathbf {r} \times \mathbf {v} )}{\alpha }}-{\frac {\mathbf {r} }{r}}$

where $\mathbf {H} =\mathbf {r} \times {\dot {\mathbf {r} }}=\mathbf {r} \times \mathbf {v}$ is the constant angular momentum vector of the orbit, and $\mathbf {v}$ is the velocity vector associated with the position vector $\mathbf {r}$ .

Obviously, the **eccentricity vector**, having the same direction as the integration constant $\mathbf {c}$ , also points to the direction of the **periapsis** of the orbit, and it has the magnitude of orbital eccentricity. This makes it very useful in orbit determination (OD) for the orbital elements of an orbit when a **state vector** [ $\mathbf {r} ,\mathbf {\dot {r}}$ ] or [ $\mathbf {r} ,\mathbf {v}$ ] is known.

### Properties of trajectory equation

For $e=0$ this is a circle with radius *p*.

For $0<e<1,$ this is an ellipse with

| $a={\frac {p}{1-e^{2}}}$ |   | 14 |
|---|---|---|

| $b={\frac {p}{\sqrt {1-e^{2}}}}=a\cdot {\sqrt {1-e^{2}}}$ |   | 15 |
|---|---|---|

For $e=1$ this is a parabola with focal length ${\tfrac {p}{2}}$

For $e>1$ this is a hyperbola with

| $a={\frac {p}{e^{2}-1}}$ |   | 16 |
|---|---|---|

| $b={\frac {p}{\sqrt {e^{2}-1}}}=a\cdot {\sqrt {e^{2}-1}}$ |   | 17 |
|---|---|---|

The following image illustrates a circle (grey), an ellipse (red), a parabola (green) and a hyperbola (blue)

The point on the horizontal line going out to the right from the focal point is the point with $\theta =0$ for which the distance to the focus takes the minimal value ${\tfrac {p}{1+e}},$ the pericentre. For the ellipse there is also an apocentre for which the distance to the focus takes the maximal value ${\tfrac {p}{1-e}}.$ For the hyperbola the range for $\theta$ is $-\cos ^{-1}\left(-{\frac {1}{e}}\right)<\theta <\cos ^{-1}\left(-{\frac {1}{e}}\right)$ and for a parabola the range is $-\pi <\theta <\pi$

Using the chain rule for differentiation (**5**), the equation (**2**) and the definition of *p* as ${\frac {H^{2}}{\alpha }}$ one gets that the radial velocity component is

| $V_{r}={\dot {r}}={\frac {H}{p}}e\sin \theta ={\sqrt {\frac {\alpha }{p}}}e\sin \theta$ |   | 18 |
|---|---|---|

and that the tangential component (velocity component perpendicular to $V_{r}$ ) is

| $V_{t}=r\cdot {\dot {\theta }}={\frac {H}{r}}={\sqrt {\frac {\alpha }{p}}}\cdot (1+e\cdot \cos \theta )$ |   | 19 |
|---|---|---|

The connection between the polar argument $\theta$ and time *t* is slightly different for elliptic and hyperbolic orbits.

For an elliptic orbit one switches to the "eccentric anomaly" *E* for which

| $x=a\cdot (\cos E-e)$ |   | 20 |
|---|---|---|

| $y=b\cdot \sin E$ |   | 21 |
|---|---|---|

and consequently

| ${\dot {x}}=-a\cdot \sin E\cdot {\dot {E}}$ |   | 22 |
|---|---|---|

| ${\dot {y}}=b\cdot \cos E\cdot {\dot {E}}$ |   | 23 |
|---|---|---|

and the angular momentum *H* is

| $H=x\cdot {\dot {y}}-y\cdot {\dot {x}}=a\cdot b\cdot (1-e\cdot \cos E)\cdot {\dot {E}}$ |   | 24 |
|---|---|---|

Integrating with respect to time *t* gives

| $H\cdot t=a\cdot b\cdot (E-e\cdot \sin E)$ |   | 25 |
|---|---|---|

under the assumption that time $t=0$ is selected such that the integration constant is zero.

As by definition of *p* one has

| $H={\sqrt {\alpha \cdot p}}$ |   | 26 |
|---|---|---|

this can be written

| $t=a\cdot {\sqrt {\frac {a}{\alpha }}}(E-e\cdot \sin E)$ |   | 27 |
|---|---|---|

For a hyperbolic orbit one uses the hyperbolic functions for the parameterisation

| $x=a\cdot (e-\cosh E)$ |   | 28 |
|---|---|---|

| $y=b\cdot \sinh E$ |   | 29 |
|---|---|---|

for which one has

| ${\dot {x}}=-a\cdot \sinh E\cdot {\dot {E}}$ |   | 30 |
|---|---|---|

| ${\dot {y}}=b\cdot \cosh E\cdot {\dot {E}}$ |   | 31 |
|---|---|---|

and the angular momentum *H* is

| $H=x\cdot {\dot {y}}-y\cdot {\dot {x}}=a\cdot b\cdot (e\cdot \cosh E-1)\cdot {\dot {E}}$ |   | 32 |
|---|---|---|

Integrating with respect to time *t* gets

| $H\cdot t=a\cdot b\cdot (e\cdot \sinh E-E)$ |   | 33 |
|---|---|---|

i.e.

| $t=a\cdot {\sqrt {\frac {a}{\alpha }}}(e\cdot \sinh E-E)$ |   | 34 |
|---|---|---|

To find what time, t, corresponds to a certain true anomaly $\theta$ it is necessary to compute the corresponding parameter *E* connected to time with relation (**27**) for an elliptic and with relation (**34**) for a hyperbolic orbit.

Note that the relations (**27**) and (**34**) define a mapping between the ranges $\left[-\infty <t<\infty \right]\longleftrightarrow \left[-\infty <E<\infty \right]$

### Some additional formulae

#### Elliptic orbit

For an *elliptic orbit,* from (**20**) and (**21**) that

| $r=a\cdot (1-e\cos E)$ |   | 35 |
|---|---|---|

and therefore that

| $\cos \theta ={\frac {x}{r}}={\frac {\cos E-e}{1-e\cos E}}$ |   | 36 |
|---|---|---|

From (**36**) then follows that $\tan ^{2}{\frac {\theta }{2}}={\frac {1-\cos \theta }{1+\cos \theta }}={\frac {1-{\frac {\cos E-e}{1-e\cos E}}}{1+{\frac {\cos E-e}{1-e\cos E}}}}={\frac {1-e\cos E-\cos E+e}{1-e\cos E+\cos E-e}}={\frac {1+e}{1-e}}\cdot {\frac {1-\cos E}{1+\cos E}}={\frac {1+e}{1-e}}\cdot \tan ^{2}{\frac {E}{2}}$

From the geometrical construction defining the eccentric anomaly it is clear that the vectors $(\cos E,\sin E)$ and $(\cos \theta ,\sin \theta )$ are on the same side of the *x*-axis. From this then follows that the vectors $\left(\cos {\tfrac {E}{2}},\sin {\tfrac {E}{2}}\right)$ and $\left(\cos {\tfrac {\theta }{2}},\sin {\tfrac {\theta }{2}}\right)$ are in the same quadrant. One therefore has that

| $\tan {\frac {\theta }{2}}={\sqrt {\frac {1+e}{1-e}}}\cdot \tan {\frac {E}{2}}$ |   | 37 |
|---|---|---|

and that

| $\theta =2\cdot \arg \left({\sqrt {1-e}}\cdot \cos {\frac {E}{2}},{\sqrt {1+e}}\cdot \sin {\frac {E}{2}}\right)+n\cdot 2\pi$ |   | 38 |
|---|---|---|

| $E=2\cdot \arg \left({\sqrt {1+e}}\cdot \cos {\frac {\theta }{2}},{\sqrt {1-e}}\cdot \sin {\frac {\theta }{2}}\right)+n\cdot 2\pi$ |   | 39 |
|---|---|---|

where " $\arg(x,y)$ " is the polar argument of the vector $(x,y)$ and *n* is selected such that $|E-\theta |<\pi$

For the numerical computation of $\arg(x,y)$ the standard function ATAN2(y,x) (or in double precision DATAN2(y,x)) available in for example the programming language FORTRAN can be used.

Note that this is a mapping between the ranges $\left[-\infty <\theta <\infty \right]\longleftrightarrow \left[-\infty <E<\infty \right]$

#### Hyperbolic orbit

For a *hyperbolic orbit*, from (**28**) and (**29**), it follows that

| $r=a\cdot (e\cdot \cosh E-1)$ |   | 40 |
|---|---|---|

and therefore that

| $\cos \theta ={\frac {x}{r}}={\frac {e-\cosh E}{e\cdot \cosh E-1}}$ |   | 41 |
|---|---|---|

As $\tan ^{2}{\frac {\theta }{2}}={\frac {1-\cos \theta }{1+\cos \theta }}={\frac {1-{\frac {e-\cosh E}{e\cdot \cosh E-1}}}{1+{\frac {e-\cosh E}{e\cdot \cosh E-1}}}}={\frac {e\cdot \cosh E-e+\cosh E}{e\cdot \cosh E+e-\cosh E}}={\frac {e+1}{e-1}}\cdot {\frac {\cosh E-1}{\cosh E+1}}={\frac {e+1}{e-1}}\cdot \tanh ^{2}{\frac {E}{2}}$ and as $\tan {\frac {\theta }{2}}$ and $\tanh {\frac {E}{2}}$ have the same sign it follows that

| $\tan {\frac {\theta }{2}}={\sqrt {\frac {e+1}{e-1}}}\cdot \tanh {\frac {E}{2}}$ |   | 42 |
|---|---|---|

This relation is convenient for passing between "true anomaly" and the parameter *E*, the latter being connected to time through relation (**34**). Note that this is a mapping between the ranges $\left[-\cos ^{-1}\left(-{\frac {1}{e}}\right)<\theta <\cos ^{-1}\left(-{\frac {1}{e}}\right)\right]\longleftrightarrow \left[-\infty <E<\infty \right]$ and that ${\tfrac {E}{2}}$ can be computed using the relation $\tanh ^{-1}x={\frac {1}{2}}\ln \left({\frac {1+x}{1-x}}\right)$

From relation (**27**) follows that the orbital period *P* for an elliptic orbit is

| $P=2\pi a\cdot {\sqrt {\frac {a}{\alpha }}}$ |   | 43 |
|---|---|---|

As the potential energy corresponding to the force field of relation (**1**) is $-{\frac {\alpha }{r}}$ it follows from (**13**), (**14**), (**18**) and (**19**) that the sum of the kinetic and the potential energy ${\frac {{V_{r}}^{2}+{V_{t}}^{2}}{2}}-{\frac {\alpha }{r}}$ for an elliptic orbit is

| $-{\frac {\alpha }{2a}}$ |   | 44 |
|---|---|---|

and from (**13**), (**16**), (**18**) and (**19**) that the sum of the kinetic and the potential energy for a hyperbolic orbit is

| ${\frac {\alpha }{2a}}$ |   | 45 |
|---|---|---|

Relative the inertial coordinate system ${\hat {x}},{\hat {y}}$ in the orbital plane with ${\hat {x}}$ towards pericentre one gets from (**18**) and (**19**) that the velocity components are

| $V_{x}=V_{r}\cos \theta -V_{t}\sin \theta =-{\sqrt {\frac {\alpha }{p}}}\cdot \sin \theta$ |   | 46 |
|---|---|---|

| $V_{y}=V_{r}\sin \theta +V_{t}\cos \theta ={\sqrt {\frac {\alpha }{p}}}\cdot (e+\cos \theta )$ |   | 47 |
|---|---|---|

The equation of the center relates mean anomaly to true anomaly for elliptical orbits, for small numerical eccentricity.

#### Parabolic orbit

For a *parabolic* orbit, let $e=1$ and $p=2f$ in (**13**) so that the orbit in polar coordinates is

$r={\frac {2\,f}{1+\cos \theta }}$

This gives the orbit in cartesian coordinates as

$y^{2}=-4\,f\,(x-f)$

This is a parabola with focal length f and focus at the origin. The parabola extends to minus infinity in x . In terms of the true anomaly $\theta$ and the periapsis distance $q=f$ , the equations for the x and y coordinates are

${\begin{aligned}x&=q\,{\Big (}1-\tan ^{2}{\Big (}{\frac {\theta }{2}}{\Big )}{\Big )}\\y&=2\,q\,\tan {\Big (}{\frac {\theta }{2}}{\Big )}\end{aligned}}$

As required

${\begin{aligned}{\frac {y}{x}}&=\tan \theta \\r&={\sqrt {x^{2}+y^{2}}}=q\,\sec ^{2}{\Big (}{\frac {\theta }{2}}{\Big )}={\frac {2\,q}{1+\cos \theta }}\end{aligned}}$

The area $S(\theta )$ swept out from the periapsis by the radius vector is

${\begin{aligned}S(\theta )=\int \limits _{0}^{\theta }{\frac {1}{2}}r^{2}\,d\theta \,&=\int \limits _{0}^{\theta }{\frac {1}{2}}\,q^{2}\,\sec ^{4}{\Big (}{\frac {\theta }{2}}{\Big )}\,d\,\theta =\int \limits _{0}^{\theta }q^{2}\,{\Big (}1+\tan ^{2}{\Big (}{\frac {\theta }{2}}{\Big )}{\Big )}\;d\,\tan {\Big (}{\frac {\theta }{2}}{\Big )}\\&=\,q^{2}{\Big (}\tan {\Big (}{\frac {\theta }{2}}{\Big )}+{\frac {1}{3}}\,\tan ^{3}{\Big (}{\frac {\theta }{2}}{\Big )}{\Big )}\end{aligned}}$

By Kepler's Second Law of equal areas in equal times this must be proportional to the time t since the periapsis. Let $q^{2}K$ be the constant of proportionality so that

$S(\theta )=q^{2}\,K\,t$ {\displaystyle } ({\displaystyle })

Differentiation with respect to t gives

${\frac {d\,\theta }{d\,t}}=2\,K\,\cos ^{4}{\Big (}{\frac {\theta }{2}}{\Big )}$

By conservation of energy, the sum of the kinetic energy $KE$ and potential energy $PE$ must not depend upon $\theta$ . These are given by

${\begin{aligned}KE&={\frac {1}{2}}({\dot {x}}^{2}+{\dot {y}}^{2})={\frac {q^{2}}{2}}\,\sec ^{6}{\Big (}{\frac {\theta }{2}}{\Big )}\,{\Big (}{\frac {d\,\theta }{d\,t}}{\Big )}^{2}=2\,q^{2}\,K^{2}\,\cos ^{2}{\Big (}{\frac {\theta }{2}}{\Big )}\\PE&={\frac {-G\,M}{r}}={\frac {-G\,M}{q}}\,\cos ^{2}{\Big (}{\frac {\theta }{2}}{\Big )}\end{aligned}}$

For $KE+PE$ to be independent of $\theta$ , it must be that

$K={\sqrt {\frac {G\,M}{2\,q^{3}}}}$

This makes the total energy be zero, as expected. Then

$\tan {\Big (}{\frac {\theta }{2}}{\Big )}+{\frac {1}{3}}\,\tan ^{3}{\Big (}{\frac {\theta }{2}}{\Big )}={\sqrt {\frac {G\,M}{2\,q^{3}}}}\,t$

This is Barker's equation and can be solved exactly for $\theta (t)$ . Solve this cubic equation by letting

$\tan {\Big (}{\frac {\theta }{2}}{\Big )}=B-{\frac {1}{B}}$

to obtain

$B^{3}-{\frac {1}{B^{3}}}\,=2\,A\;{\text{for}}\;A={\frac {3}{2}}\,{\sqrt {\frac {G\,M}{2\,q^{3}}}}\,t$

This is a quadratic equation in $B^{3}$ which has the solution

$B={\sqrt[{3}]{A+{\sqrt {A^{2}+1}}}}$

### Determination of the Kepler orbit that corresponds to a given initial state

This is the "initial value problem" for the differential equation (**1**) which is a first order equation for the 6-dimensional "state vector" $(\mathbf {r} ,\mathbf {v} )$ when written as

| ${\dot {\mathbf {v} }}=-\alpha \cdot {\frac {\hat {\mathbf {r} }}{r^{2}}}$ |   | 48 |
|---|---|---|

| ${\dot {\mathbf {r} }}=\mathbf {v}$ |   | 49 |
|---|---|---|

For any values for the initial "state vector" $(\mathbf {r} _{0},\mathbf {v} _{0})$ the Kepler orbit corresponding to the solution of this initial value problem can be found with the following algorithm:

Define the orthogonal unit vectors $({\hat {\mathbf {r} }},{\hat {\mathbf {t} }})$ through

| $\mathbf {r} _{0}=r{\hat {\mathbf {r} }}$ |   | 50 |
|---|---|---|

| $\mathbf {v} _{0}=V_{r}{\hat {\mathbf {r} }}+V_{t}{\hat {\mathbf {t} }}$ |   | 51 |
|---|---|---|

with $r>0$ and $V_{t}>0$

From (**13**), (**18**) and (**19**) follows that by setting

| $p={\frac {{(r\cdot V_{t})}^{2}}{\alpha }}$ |   | 52 |
|---|---|---|

and by defining $e\geq 0$ and $\theta$ such that

| $e\cos \theta ={\frac {V_{t}}{V_{0}}}-1$ |   | 53 |
|---|---|---|

| $e\sin \theta ={\frac {V_{r}}{V_{0}}}$ |   | 54 |
|---|---|---|

where

| $V_{0}={\sqrt {\frac {\alpha }{p}}}$ |   | 55 |
|---|---|---|

one gets a Kepler orbit that for true anomaly $\theta$ has the same r, $V_{r}$ and $V_{t}$ values as those defined by (**50**) and (**51**).

If this Kepler orbit then also has the same $({\hat {\mathbf {r} }},{\hat {\mathbf {t} }})$ vectors for this true anomaly $\theta$ as the ones defined by (**50**) and (**51**) the state vector $(\mathbf {r} ,\mathbf {v} )$ of the Kepler orbit takes the desired values $(\mathbf {r} _{0},\mathbf {v} _{0})$ for true anomaly $\theta$ .

The standard inertially fixed coordinate system $({\hat {\mathbf {x} }},{\hat {\mathbf {y} }})$ in the orbital plane (with ${\hat {\mathbf {x} }}$ directed from the centre of the homogeneous sphere to the pericentre) defining the orientation of the conical section (ellipse, parabola or hyperbola) can then be determined with the relation

| ${\hat {\mathbf {x} }}=\cos \theta {\hat {\mathbf {r} }}-\sin \theta {\hat {\mathbf {t} }}$ |   | 56 |
|---|---|---|

| ${\hat {\mathbf {y} }}=\sin \theta {\hat {\mathbf {r} }}+\cos \theta {\hat {\mathbf {t} }}$ |   | 57 |
|---|---|---|

Note that the relations (**53**) and (**54**) has a singularity when $V_{r}=0$ and $V_{t}=V_{0}={\sqrt {\frac {\alpha }{p}}}={\sqrt {\frac {\alpha }{\frac {{(r\cdot V_{t})}^{2}}{\alpha }}}}$ i.e.

| $V_{t}={\sqrt {\frac {\alpha }{r}}}$ |   | 58 |
|---|---|---|

which is the case that it is a circular orbit that is fitting the initial state $(\mathbf {r} _{0},\mathbf {v} _{0})$

### The osculating Kepler orbit

For any state vector $(\mathbf {r} ,\mathbf {v} )$ the Kepler orbit corresponding to this state can be computed with the algorithm defined above. First the parameters $p,e,\theta$ are determined from $r,V_{r},V_{t}$ and then the orthogonal unit vectors in the orbital plane ${\hat {x}},{\hat {y}}$ using the relations (**56**) and (**57**).

If now the equation of motion is

| ${\ddot {\mathbf {r} }}=\mathbf {F} (\mathbf {r} ,{\dot {\mathbf {r} }},t)$ |   | 59 |
|---|---|---|

where $\mathbf {F} (\mathbf {r} ,{\dot {\mathbf {r} }},t)$ is a function other than $-\alpha {\frac {\mathbf {r} }{r^{2}}}$ the resulting parameters p , e , $\theta$ , ${\hat {\mathbf {x} }}$ , ${\hat {\mathbf {y} }}$ defined by $\mathbf {r} ,{\dot {\mathbf {r} }}$ will all vary with time as opposed to the case of a Kepler orbit for which only the parameter $\theta$ will vary.

The Kepler orbit computed in this way having the same "state vector" as the solution to the "equation of motion" (**59**) at time t is said to be "osculating" at this time.

This concept is for example useful in case $\mathbf {F} (\mathbf {r} ,{\dot {\mathbf {r} }},t)=-\alpha {\frac {\hat {\mathbf {r} }}{r^{2}}}+\mathbf {f} (\mathbf {r} ,{\dot {\mathbf {r} }},t)$ where $\mathbf {f} (\mathbf {r} ,{\dot {\mathbf {r} }},t)$

is a small "perturbing force" due to for example a faint gravitational pull from other celestial bodies. The parameters of the osculating Kepler orbit will then only slowly change and the osculating Kepler orbit is a good approximation to the real orbit for a considerable time period before and after the time of osculation.

This concept can also be useful for a rocket during powered flight as it then tells which Kepler orbit the rocket would continue in case the thrust is switched off.

For a "close to circular" orbit the concept "eccentricity vector" defined as $\mathbf {e} =e{\hat {\mathbf {x} }}$ is useful. From (**53**), (**54**) and (**56**) follows that

| $\mathbf {e} ={\frac {(V_{t}-V_{0}){\hat {\mathbf {r} }}-V_{r}{\hat {\mathbf {t} }}}{V_{0}}}$ |   | 60 |
|---|---|---|

i.e. $\mathbf {e}$ is a smooth differentiable function of the state vector $(\mathbf {r} ,\mathbf {v} )$ also if this state corresponds to a circular orbit.
