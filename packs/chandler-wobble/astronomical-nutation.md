---
title: "Astronomical nutation"
source: https://en.wikipedia.org/wiki/Astronomical_nutation
domain: chandler-wobble
license: CC-BY-SA-4.0
tags: chandler wobble
fetched: 2026-07-03
---

# Astronomical nutation

**Astronomical nutation** is a phenomenon which causes the orientation of the axis of rotation of a spinning astronomical object to vary over time. It is caused by the gravitational forces of other nearby bodies acting upon the spinning object. Although they are caused by the same effect operating over different timescales, astronomers usually make a distinction between *precession*, which is a steady long-term change in the axis of rotation, and *nutation*, which is the combined effect of similar shorter-term variations.

An example of precession and nutation is the variation over time of the orientation of the axis of rotation of the Earth. This is important because the most commonly used frame of reference for measurement of the positions of astronomical objects is the Earth's equator — the so-called equatorial coordinate system. The effect of precession and nutation causes this frame of reference itself to change over time, relative to an arbitrary fixed frame.

Nutation is one of the corrections which must be applied to obtain the apparent place of an astronomical object. When calculating the position of an object, it is initially expressed relative to the *mean equinox and equator* — defined by the orientation of the Earth's axis at a specified date, taking into account the long-term effect of precession, but *not* the shorter-term effects of nutation. It is then necessary to apply a further correction to take into account the effect of nutation, after which the position relative to the *true equinox and equator* is obtained.

Because the dynamic motions of the planets are so well known, their nutations can be calculated to within arcseconds over periods of many decades. There is another disturbance of the Earth's rotation called polar motion that can be estimated for only a few months into the future because it is influenced by rapidly and unpredictably varying things such as ocean currents, wind systems, and hypothesised motions in the liquid nickel-iron outer core of the Earth.

## Earth's nutation

Precession and nutation are caused principally by the gravitational forces of the Moon and Sun acting upon the non-spherical figure of the Earth. Precession is the effect of these forces averaged over a very long period of time, and a time-varying moment of inertia (If an object is asymmetric about its principal axis of rotation, the moment of inertia with respect to each coordinate direction will change with time, while preserving angular momentum), and has a timescale of about 26,000 years. Nutation occurs because the forces are not constant, and vary as the Earth revolves around the Sun, and the Moon revolves around the Earth. Basically, there are also torques from other planets that cause planetary precession which contributes to about 2% of the total precession. Because of periodic variations in the torques from the sun and the moon, the wobbling (nutation) comes into place. You can think of precession as the average and nutation as the instantaneous.

The largest contributor to nutation is the inclination of the orbit of the Moon around the Earth, at slightly over 5° to the plane of the ecliptic. The orientation of this orbital plane varies over a period of about 18.6 years (this period is referred to as the saros). Because the Earth's equator is itself inclined at an angle of about 23.4° to the ecliptic (the obliquity of the ecliptic, $\epsilon$ ), these effects combine to vary the inclination of the Moon's orbit to the equator by between 18.4° and 28.6° over the 18.6 year period. This causes the orientation of the Earth's axis to vary over the same period, with the true position of the celestial poles describing a small ellipse around their mean position. The maximum radius of this ellipse is the *constant of nutation*, approximately 9.2 arcseconds.

Smaller effects also contribute to nutation. These are caused by the monthly motion of the Moon around the Earth and its orbital eccentricity, and similar terms caused by the annual motion of the Earth around the Sun.

### Effect on position of astronomical objects

Because nutation causes a change to the frame of reference, rather than a change in position of an observed object itself, it applies equally to all objects. Its magnitude at any point in time is usually expressed in terms of ecliptic coordinates, as *nutation in longitude* ( $\Delta \psi$ ) in seconds of arc and *nutation in obliquity* ( $\Delta \epsilon$ ) in seconds of arc. The largest term in nutation is expressed numerically (in arcseconds) as follows:

${\begin{aligned}\Delta \psi &=-17.2\sin \Omega \\\Delta \epsilon &=9.2\cos \Omega \end{aligned}}$

where $\Omega$ is the ecliptic longitude of the ascending node of the Moon's orbit. By way of reference, the sum of the absolute value of all the remaining terms is 1.4 arcseconds for longitude and 0.9 arcseconds for obliquity.

Spherical trigonometry can then be used on any given object to convert these quantities into an adjustment in the object's right ascension ( $\alpha$ ) and declination ( $\delta$ ) For objects that are not close to a celestial pole, nutation in right ascension ( $\Delta \alpha$ ) and declination ( $\Delta \delta$ ) can be calculated approximately as follows:

${\begin{aligned}\Delta \alpha &=(\cos \epsilon +\sin \epsilon \sin \alpha \tan \delta )\Delta \psi -\cos \alpha \tan \delta \Delta \epsilon \\\Delta \delta &=\cos \alpha \sin \epsilon \Delta \psi +\sin \alpha \Delta \epsilon \end{aligned}}$

### Free nutation

Earth also has an additional 0.10 to 0.15 seconds of arc nutations with a period 6 and half years called Chandler wobble and its due to free nutation caused by irregular distribution of mass around Earth axis.

## History

Nutation was discovered by James Bradley from a series of observations of stars conducted between 1727 and 1747. These observations were originally intended to demonstrate conclusively the existence of the annual aberration of light, a phenomenon that Bradley had unexpectedly discovered in 1725–6. However, there were some residual discrepancies in the stars' positions that were not explained by aberration, and Bradley suspected that they were caused by nutation taking place over the 18.6 year period of the revolution of the nodes of the Moon's orbit. This was confirmed by his 20-year series of observations, in which he discovered that the celestial pole moved in a slightly flattened ellipse of 18 by 16 arcseconds about its mean position.

Although Bradley's observations proved the existence of nutation and he intuitively understood that it was caused by the action of the Moon on the rotating Earth, it was left to later mathematicians, Jean le Rond d'Alembert and Leonhard Euler, to develop a more detailed theoretical explanation of the phenomenon.
