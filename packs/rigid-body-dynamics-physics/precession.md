---
title: "Precession"
source: https://en.wikipedia.org/wiki/Precession
domain: rigid-body-dynamics-physics
license: CC-BY-SA-4.0
tags: rigid body dynamics, moment of inertia, gyroscopic precession, rotational motion
fetched: 2026-07-02
---

# Precession

**Precession** is a change in the orientation of the rotational axis of a rotating body. In an appropriate reference frame it can be defined as a change in the first Euler angle, whereas the third Euler angle defines the rotation itself. In other words, if the axis of rotation of a body is itself rotating about a second axis, that body is said to be precessing about the second axis. A motion in which the second Euler angle changes is called *nutation*. In physics, there are two types of precession: torque-free and torque-induced.

In astronomy, **precession** refers to any of several slow changes in an astronomical body's rotational or orbital parameters. An important example is the steady change in the orientation of the axis of rotation of the Earth, known as the precession of the equinoxes.

## Torque-free or torque neglected

Torque-free precession implies that no external moment (torque) is applied to the body. In torque-free precession, the angular momentum is a constant, but the angular velocity vector changes orientation with time. What makes this possible is a time-varying moment of inertia, or more precisely, a time-varying inertia matrix. The inertia matrix is composed of the moments of inertia of a body calculated with respect to separate coordinate axes (e.g. *x*, *y*, *z*). If an object is asymmetric about its principal axis of rotation, the moment of inertia with respect to each coordinate direction will change with time, while preserving angular momentum. The result is that the component of the angular velocities of the body about each axis will vary inversely with each axis' moment of inertia.

The torque-free precession rate of an object with an axis of symmetry, such as a disk, spinning about an axis not aligned with that axis of symmetry can be calculated as follows: ${\boldsymbol {\omega }}_{\mathrm {p} }={\frac {{\boldsymbol {I}}_{\mathrm {s} }{\boldsymbol {\omega }}_{\mathrm {s} }}{{\boldsymbol {I}}_{\mathrm {p} }\cos({\boldsymbol {\alpha }})}}$ where ***ω***p is the precession rate, ***ω***s is the spin rate about the axis of symmetry, ***I***s is the moment of inertia about the axis of symmetry, ***I***p is moment of inertia about either of the other two equal perpendicular principal axes, and **α** is the angle between the moment of inertia direction and the symmetry axis.

When an object is not perfectly rigid, inelastic dissipation will tend to damp torque-free precession, and the rotation axis will align itself with one of the inertia axes of the body.

For a generic solid object without any axis of symmetry, the evolution of the object's orientation, represented (for example) by a rotation matrix **R** that transforms internal to external coordinates, may be numerically simulated. Given the object's fixed internal moment of inertia tensor ***I***0 and fixed external angular momentum **L**, the instantaneous angular velocity is ${\boldsymbol {\omega }}\left({\boldsymbol {R}}\right)={\boldsymbol {R}}{\boldsymbol {I}}_{0}^{-1}{\boldsymbol {R}}^{T}{\boldsymbol {L}}$ Precession occurs by repeatedly recalculating **ω** and applying a small rotation vector ***ω** dt* for the short time *dt*; e.g.: ${\boldsymbol {R}}_{\text{new}}=\exp \left(\left[{\boldsymbol {\omega }}\left({\boldsymbol {R}}_{\text{old}}\right)\right]_{\times }dt\right){\boldsymbol {R}}_{\text{old}}$ for the skew-symmetric matrix [***ω***]×. The errors induced by finite time steps tend to increase the rotational kinetic energy: $E\left({\boldsymbol {R}}\right)={\boldsymbol {\omega }}\left({\boldsymbol {R}}\right)\cdot {\frac {\boldsymbol {L}}{2}}$ this unphysical tendency can be counteracted by repeatedly applying a small rotation vector **v** perpendicular to both **ω** and **L**, noting that $E\left(\exp \left(\left[{\boldsymbol {v}}\right]_{\times }\right){\boldsymbol {R}}\right)\approx E\left({\boldsymbol {R}}\right)+\left({\boldsymbol {\omega }}\left({\boldsymbol {R}}\right)\times {\boldsymbol {L}}\right)\cdot {\boldsymbol {v}}$

## Torque-induced

Torque-induced precession (**gyroscopic precession**) is the phenomenon in which the axis of a spinning object (e.g., a gyroscope) describes a cone in space when an external torque is applied to it. The phenomenon is commonly seen in a spinning toy top, but all rotating objects can undergo precession. If the speed of the rotation and the magnitude of the external torque are constant, the spin axis will move at right angles to the direction that would intuitively result from the external torque. In the case of a toy top, its weight is acting downwards from its center of mass and the normal force (reaction) of the ground is pushing up on it at the point of contact with the support. These two opposite forces produce a torque which causes the top to precess.

The device depicted on the right is gimbal-mounted. From inside to outside there are three axes of rotation: the hub of the wheel, the gimbal axis, and the vertical pivot.

To distinguish between the two horizontal axes, rotation around the wheel hub will be called *spinning*, and rotation around the gimbal axis will be called *pitching*. Rotation around the vertical pivot axis is called *rotation*.

First, imagine that the entire device is rotating around the (vertical) pivot axis. Then, spinning of the wheel (around the wheelhub) is added. Imagine the gimbal axis to be locked, so that the wheel cannot pitch. The gimbal axis has sensors, that measure whether there is a torque around the gimbal axis.

In the picture, a section of the wheel has been named *dm*1. At the depicted moment in time, section *dm*1 is at the perimeter of the rotating motion around the (vertical) pivot axis. Section *dm*1, therefore, has a lot of angular rotating velocity with respect to the rotation around the pivot axis, and as *dm*1 is forced closer to the pivot axis of the rotation (by the wheel spinning further), because of the Coriolis effect, with respect to the vertical pivot axis, *dm*1 tends to move in the direction of the top-left arrow in the diagram (shown at 45°) in the direction of rotation around the pivot axis. Section *dm*2 of the wheel is moving away from the pivot axis, and so a force (again, a Coriolis force) acts in the same direction as in the case of *dm*1. Note that both arrows point in the same direction.

The same reasoning applies for the bottom half of the wheel, but there the arrows point in the opposite direction to that of the top arrows. Combined over the entire wheel, there is a torque around the gimbal axis when some spinning is added to rotation around a vertical axis.

The torque around the gimbal axis arises without any delay; the response is instantaneous.

In the discussion above, the setup was kept unchanging by preventing pitching around the gimbal axis. In the case of a spinning toy top, when the spinning top starts tilting, gravity exerts a torque. However, instead of rolling over, the spinning top just pitches a little. This pitching motion reorients the spinning top with respect to the torque that is being exerted. The result is that the torque exerted by gravity – via the pitching motion – elicits gyroscopic precession (which in turn yields a counter torque against the gravity torque) rather than causing the spinning top to fall to its side.

Precession or gyroscopic considerations have an effect on bicycle performance at high speed. Precession is also the mechanism behind gyrocompasses.

### Classical (Newtonian)

Precession is the change of angular velocity and angular momentum produced by a torque. The general equation that relates the torque to the rate of change of angular momentum is: ${\boldsymbol {\tau }}={\frac {\mathrm {d} \mathbf {L} }{\mathrm {d} t}}$ where ${\boldsymbol {\tau }}$ and $\mathbf {L}$ are the torque and angular momentum vectors respectively.

Due to the way the torque vectors are defined, it is a vector that is perpendicular to the plane of the forces that create it. Thus it may be seen that the angular momentum vector will change perpendicular to those forces. Depending on how the forces are created, they will often rotate with the angular momentum vector, and then circular precession is created.

Under these circumstances the angular velocity of precession is given by:

${\boldsymbol {\omega }}_{\mathrm {p} }={\frac {\ mgr}{I_{\mathrm {s} }{\boldsymbol {\omega }}_{\mathrm {s} }}}={\frac {\tau }{I_{\mathrm {s} }{\boldsymbol {\omega }}_{\mathrm {s} }\sin(\theta )}}$

where *I*s is the moment of inertia, ***ω***s is the angular velocity of spin about the spin axis, m is the mass, *g* is the acceleration due to gravity, θ is the angle between the spin axis and the axis of precession and *r* is the distance between the center of mass and the pivot. The torque vector originates at the center of mass. Using ***ω*** = ⁠2π/*T*⁠, we find that the period of precession is given by: $T_{\mathrm {p} }={\frac {4\pi ^{2}I_{\mathrm {s} }}{\ mgrT_{\mathrm {s} }}}={\frac {4\pi ^{2}I_{\mathrm {s} }\sin(\theta )}{\ \tau T_{\mathrm {s} }}}$

Where *I*s is the moment of inertia, *T*s is the period of spin about the spin axis, and **τ** is the torque. In general, the problem is more complicated than this, however.

### Relativistic (Einsteinian)

The special and general theories of relativity give three types of corrections to the Newtonian precession, of a gyroscope near a large mass such as Earth, described above. They are:

- Thomas precession, a special-relativistic correction accounting for an object (such as a gyroscope) being accelerated along a curved path.
- de Sitter precession, a general-relativistic correction accounting for the Schwarzschild metric of curved space near a large non-rotating mass.
- Lense–Thirring precession, a general-relativistic correction accounting for the frame dragging by the Kerr metric of curved space near a large rotating mass.

The Schwarzschild geodesics (sometimes Schwarzschild precession) are used in the prediction of the anomalous perihelion precession of the planets, most notably for the accurate prediction of the apsidal precession of Mercury.

## Astronomy

In astronomy, precession refers to any of several gravity-induced, slow and continuous changes in an astronomical body's rotational axis or orbital path. Precession of the equinoxes, perihelion precession, changes in the tilt of Earth's axis to its orbit, and the eccentricity of its orbit over tens of thousands of years are all important parts of the astronomical theory of ice ages.

### Axial precession (precession of the equinoxes)

Axial precession is the movement of the rotational axis of an astronomical body, whereby the axis slowly traces out a cone. In the case of Earth, this type of precession is also known as the *precession of the equinoxes*, *lunisolar precession*, or *precession of the equator*. Earth goes through one such complete precessional cycle in a period of approximately 26,000 years or 1° every 72 years, during which the positions of stars will slowly change in both equatorial coordinates and ecliptic longitude. Over this cycle, Earth's north axial pole moves from where it is now, within 1° of Polaris, in a circle around the ecliptic pole, with an angular radius of about 23.5°.

The ancient Greek astronomer Hipparchus (c. 190–120 BC) is generally accepted to be the earliest known astronomer to recognize and assess the precession of the equinoxes at about 1° per century (which is not far from the actual value for antiquity, 1.38°), although there is some minor dispute about whether he was. In ancient China, the Jin dynasty scholar-official Yu Xi (fl. 307–345 AD) made a similar discovery centuries later, noting that the position of the Sun during the winter solstice had drifted roughly one degree over the course of fifty years relative to the position of the stars. The precession of Earth's axis was later explained by Newtonian physics. Being an oblate spheroid, Earth has a non-spherical shape, bulging outward at the equator. The gravitational tidal forces of the Moon and Sun apply torque to the equator, attempting to pull the equatorial bulge into the plane of the ecliptic, but instead causing it to precess. The torque exerted by the planets, particularly Jupiter, also plays a role.

Precessional movement of the axis (left), precession of the equinox in relation to the distant stars (middle), and the path of the north celestial pole among the stars due to the precession. Vega is the bright star near the bottom (right).

### Apsidal precession

The orbits of planets around the Sun do not really follow an identical ellipse each time, but actually trace out a flower-petal shape because the major axis of each planet's elliptical orbit also precesses within its orbital plane, partly in response to perturbations in the form of the changing gravitational forces exerted by other planets. This is called perihelion precession or apsidal precession.

In the adjunct image, Earth's apsidal precession is illustrated. As the Earth travels around the Sun, its elliptical orbit rotates gradually over time. The eccentricity of its ellipse and the precession rate of its orbit are exaggerated for visualization. Most orbits in the Solar System have a much smaller eccentricity and precess at a much slower rate, making them nearly circular and nearly stationary.

Discrepancies between the observed perihelion precession rate of the planet Mercury and that predicted by classical mechanics were prominent among the forms of experimental evidence leading to the acceptance of Einstein's Theory of Relativity (in particular, his General Theory of Relativity), which accurately predicted the anomalies. Deviating from Newton's law, Einstein's theory of gravitation predicts an extra term of ⁠*A*/*r*4⁠, which accurately gives the observed excess turning rate of 43 arcseconds per century.

### Nodal precession

Orbital nodes also precess over time.
