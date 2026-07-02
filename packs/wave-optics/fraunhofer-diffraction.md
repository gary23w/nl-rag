---
title: "Fraunhofer diffraction"
source: https://en.wikipedia.org/wiki/Fraunhofer_diffraction
domain: wave-optics
license: CC-BY-SA-4.0
tags: wave interference, fresnel diffraction, fraunhofer diffraction, diffraction grating
fetched: 2026-07-02
---

# Fraunhofer diffraction

In optics, the **Fraunhofer diffraction** equation is used to model the diffraction of waves when plane waves are incident on a diffracting object, and the diffraction pattern is viewed at a sufficiently long distance (a distance satisfying the Fraunhofer condition) from the object (in the far-field region), and also when it is viewed at the focal plane of an imaging lens. In contrast, the diffraction pattern created near the diffracting object and (in the near field region) is given by the Fresnel diffraction equation.

The equation was named in honor of Joseph von Fraunhofer although he was not actually involved in the development of the theory.

This article explains where the Fraunhofer equation can be applied, and shows Fraunhofer diffraction patterns for various apertures. A detailed mathematical treatment of Fraunhofer diffraction is given in Fraunhofer diffraction equation.

## Equation

When a beam of light is partly blocked by an obstacle, some of the light is scattered around the object, light and dark bands are often seen at the edge of the shadow – this effect is a result of diffraction. These effects can be modelled using the Huygens–Fresnel principle; Huygens postulated that every point on a wavefront acts as a source of spherical secondary wavelets and the sum of these secondary wavelets determines the form of the proceeding wave at any subsequent time, while Fresnel developed an equation using the Huygens wavelets together with the principle of superposition of waves, which models these diffraction effects quite well.

It is generally not straightforward to calculate the wave amplitude given by the sum of the secondary wavelets (The wave sum is also a wave.), each of which has its own amplitude, phase, and oscillation direction (polarization), since this involves addition of many waves of varying amplitude, phase, and polarization. When two light waves as electromagnetic fields are added together (vector sum), the amplitude of the wave sum depends on the amplitudes, the phases, and even the polarizations of individual waves. On a certain direction where electromagnetic wave fields are projected (or considering a situation where two waves have the same polarization), two waves of equal (projected) amplitude which are in phase (same phase) give the amplitude of the resultant wave sum as double the individual wave amplitudes, while two waves of equal amplitude which are in opposite phases give the zero amplitude of the resultant wave as they cancel out each other. Generally, a two-dimensional integral over complex variables has to be solved and in many cases, an analytic solution is not available.

The Fraunhofer diffraction equation is a simplified version of Kirchhoff's diffraction formula and it can be used to model light diffraction when both a light source and a viewing plane (a plane of observation where the diffracted wave is observed) are effectively infinitely distant from a diffracting aperture. With a sufficiently distant light source from a diffracting aperture, the incident light to the aperture is effectively a plane wave so that the phase of the light at each point on the aperture is the same. At a sufficiently distant plane of observation from the aperture, the phase of the wave coming from each point on the aperture varies linearly with the point position on the aperture, making the calculation of the sum of the waves at an observation point on the plane of observation relatively straightforward in many cases. Even the amplitudes of the secondary waves coming from the aperture at the observation point can be treated as same or constant for a simple diffraction wave calculation in this case. Diffraction in such a geometrical requirement is called *Fraunhofer diffraction*, and the condition where Fraunhofer diffraction is valid is called *Fraunhofer condition*, as shown in the right box. A diffracted wave is often called *Far field* if it at least partially satisfies Fraunhofer condition such that the distance between the aperture and the observation plane L is $L\gg {\frac {W^{2}}{\lambda }}$ .

> **Fraunhofer diffraction** occurs when the Fresnel number ${\frac {W^{2}}{L\lambda }}\ll 1$ (Fraunhofer condition)
> 
> W – The largest size of a diffracting aperture or slit, $\lambda$ – Wavelength, L – The smaller of the two distances, one is between the diffracting aperture and the plane of observation and the other is between the diffracting plane and the point wave source.

For example, if a 0.5 mm diameter circular hole is illuminated by a laser light with 0.6 μm wavelength, then Fraunhofer diffraction occurs if the viewing distance is greater than 1000 mm.

### Derivation of Fraunhofer condition

The derivation of Fraunhofer condition here is based on the geometry described in the right box. The diffracted wave path *r*2 can be expressed in terms of another diffracted wave path *r*1 and the distance *b* between two diffracting points by using the law of cosines;

${r_{2}}={\left(r_{1}^{2}+b^{2}-2b{r_{1}}\cos \left({\frac {\pi }{2}}-\theta \right)\right)}^{\frac {1}{2}}={r_{1}}{\left(1+{\frac {b^{2}}{r_{1}^{2}}}-2{\frac {b}{r_{1}}}\sin \theta \right)}^{\frac {1}{2}}.$

This can be expanded by calculating the expression's Taylor series to second order with respect to ${\frac {b}{r_{1}}}$ , ${r_{2}}={r_{1}}\left(1-{\frac {b}{r_{1}}}\sin \theta +{\frac {b^{2}}{2r_{1}^{2}}}\cos ^{2}\theta +\cdots \right)={r_{1}}-b\sin \theta +{\frac {b^{2}}{2r_{1}}}\cos ^{2}\theta +\cdots ~.$

The phase difference between waves propagating along the paths *r*2 and *r*1 are, with the wavenumber where λ is the light wavelength, $k{r_{2}}-k{r_{1}}=-kb\sin \theta +k{\frac {b^{2}}{2r_{1}}}\cos ^{2}\theta +\cdots .$

If $k{\frac {b^{2}}{2{r_{1}}}}\cos ^{2}\theta =\pi {\frac {b^{2}}{\lambda r_{1}}}\cos ^{2}\theta \ll \pi$ so ${\frac {b^{2}}{\lambda r_{1}}}\cos ^{2}\theta \ll 1$ , then the phase difference is $kr_{2}-kr_{1}\approx -kb\sin \theta$ . The geometrical implication from this expression is that the paths *r*2 and *r*1 are approximately parallel with each other. Since there can be a diffraction - observation plane, the diffracted wave path whose angle with respect to a straight line parallel to the optical axis is close to 0, this approximation condition can be further simplified as ${\frac {b^{2}}{\lambda }}\ll L$ where *L* is the distance between two planes along the optical axis. Due to the fact that an incident wave on a diffracting plane is effectively a plane wave if ${\frac {b^{2}}{\lambda }}\ll L$ where *L* is the distance between the diffracting plane and the point wave source is satisfied, Fraunhofer condition is ${\frac {b^{2}}{\lambda }}\ll L$ where *L* is the smaller of the two distances, one is between the diffracting plane and the plane of observation and the other is between the diffracting plane and the point wave source.

### Focal plane of a positive lens as the far field plane

In the far field, propagation paths for wavelets from every point on an aperture to a point of observation are approximately parallel, and a positive lens (focusing lens) focuses parallel rays toward the lens to a point on the focal plane (the focus point position on the focal plane depends on the angle of the parallel rays with respect to the optical axis). So, if a positive lens with a sufficiently long focal length (so that differences between electric field orientations for wavelets can be ignored at the focus) is placed after an aperture, then the lens practically makes the Fraunhofer diffraction pattern of the aperture on its focal plane as the parallel rays meet each other at the focus.

## Examples

In each of these examples, the aperture is illuminated by a monochromatic plane wave at normal incidence.

### Diffraction by a narrow rectangular slit

The width of the slit is W. The Fraunhofer diffraction pattern is shown in the image together with a plot of the intensity vs. angle θ. The pattern has maximum intensity at *θ* = 0, and a series of peaks of decreasing intensity. Most of the diffracted light falls between the first minima. The angle, α, subtended by these two minima is given by:

$\alpha \approx {\frac {2\lambda }{W}}$

Thus, the smaller the aperture, the larger the angle α subtended by the diffraction bands. The size of the central band at a distance *z* is given by

$d_{f}={\frac {2\lambda z}{W}}$

For example, when a slit of width 0.5 mm is illuminated by light of wavelength 0.6 μm, and viewed at a distance of 1000 mm, the width of the central band in the diffraction pattern is 2.4 mm.

The fringes extend to infinity in the *y* direction since the slit and illumination also extend to infinity.

If W < λ, the intensity of the diffracted light does not fall to zero, and if $D\ll \lambda$ , the diffracted wave is cylindrical.

#### Semi-quantitative analysis of single-slit diffraction

We can find the angle at which a first minimum is obtained in the diffracted light by the following reasoning. Consider the light diffracted at an angle θ where the distance *CD* is equal to the wavelength of the illuminating light. The width of the slit is the distance *AC*. The component of the wavelet emitted from the point A which is travelling in the θ direction is in anti-phase with the wave from the point *B* at middle of the slit, so that the net contribution at the angle θ from these two waves is zero. The same applies to the points just below *A* and *B*, and so on. Therefore, the amplitude of the total wave travelling in the direction θ is zero. We have:

$\theta _{\text{min}}\approx {\frac {CD}{AC}}={\frac {\lambda }{W}}.$

The angle subtended by the first minima on either side of the centre is then, as above:

$\alpha =2\theta _{\text{min}}={\frac {2\lambda }{W}}.$

There is no such simple argument to enable us to find the maxima of the diffraction pattern.

#### Single-slit diffraction using Huygens' principle

We can develop an expression for the far field of a continuous array of point sources of uniform amplitude and of the same phase. Let the array of length *a* be parallel to the y axis with its center at the origin as indicated in the figure to the right. Then the differential field is:

$dE={\frac {A}{r_{1}}}e^{i\omega [t-(r_{1}/c)]}dy={\frac {A}{r_{1}}}e^{i(\omega t-\beta r_{1})}dy$

where $\beta =\omega /c=2\pi /\lambda$ . However $r_{1}=r-y\sin \theta$ and integrating from $-a/2$ to $a/2$ ,

$E\simeq A'\int _{-a/2}^{a/2}e^{i\beta y\sin \theta }dy$ where $A'={\frac {Ae^{i(\omega t-\beta r)}}{r}}$ .

Integrating we then get $E={\frac {2A'}{\beta \sin \theta }}\sin \left({\frac {\beta a}{2}}\sin \theta \right)$

Letting $\psi ^{'}=\beta a\sin \theta =\alpha _{r}\sin \theta$ where the array length in radians is $a_{r}=\beta a=2\pi a/\lambda$ , then, $E=A'a{\frac {\sin(\psi ^{'}/2)}{\psi ^{'}/2}}$

### Diffraction by a rectangular aperture

The form of the diffraction pattern given by a rectangular aperture is shown in the figure on the right (or above, in tablet format). There is a central semi-rectangular peak, with a series of horizontal and vertical fringes. The dimensions of the central band are related to the dimensions of the slit by the same relationship as for a single slit so that the larger dimension in the diffracted image corresponds to the smaller dimension in the slit. The spacing of the fringes is also inversely proportional to the slit dimension.

If the illuminating beam does not illuminate the whole vertical length of the slit, the spacing of the vertical fringes is determined by the dimensions of the illuminating beam. Close examination of the double-slit diffraction pattern below shows that there are very fine horizontal diffraction fringes above and below the main spot, as well as the more obvious horizontal fringes.

### Diffraction by a circular aperture

The diffraction pattern given by a circular aperture is shown in the figure on the right. This is known as the Airy diffraction pattern. It can be seen that most of the light is in the central disk. The angle subtended by this disk, known as the Airy disk, is

$\alpha \approx {\frac {1.22\lambda }{W}}$ where *W* is the diameter of the aperture.

The Airy disk can be an important parameter in limiting the ability of an imaging system to resolve closely located objects.

### Diffraction by an aperture with a Gaussian profile

The diffraction pattern obtained given by an aperture with a Gaussian profile, for example, a photographic slide whose transmissivity has a Gaussian variation is also a Gaussian function. The form of the function is plotted on the right (above, for a tablet), and it can be seen that, unlike the diffraction patterns produced by rectangular or circular apertures, it has no secondary rings. This technique can be used in a process called apodization—the aperture is covered by a Gaussian filter, giving a diffraction pattern with no secondary rings.

The output profile of a single mode laser beam may have a Gaussian intensity profile and the diffraction equation can be used to show that it maintains that profile however far away it propagates from the source.

### Diffraction by a double slit

In the double-slit experiment, the two slits are illuminated by a single light beam. If the width of the slits is small enough (less than the wavelength of the light), the slits diffract the light into cylindrical waves. These two cylindrical wavefronts are superimposed, and the amplitude, and therefore the intensity, at any point in the combined wavefronts depends on both the magnitude and the phase of the two wavefronts. These fringes are often known as Young's fringes.

The angular spacing of the fringes is given by $\theta _{\text{f}}=\lambda /d.$

The spacing of the fringes at a distance z from the slits is given by $w_{\text{f}}=z\theta _{f}=z\lambda /d,$ where d is the separation of the slits.

The fringes in the picture were obtained using the yellow light from a sodium light (wavelength = 589 nm), with slits separated by 0.25 mm, and projected directly onto the image plane of a digital camera.

Double-slit interference fringes can be observed by cutting two slits in a piece of card, illuminating with a laser pointer, and observing the diffracted light at a distance of 1 m. If the slit separation is 0.5 mm, and the wavelength of the laser is 600 nm, then the spacing of the fringes viewed at a distance of 1 m would be 1.2 mm.

#### Semi-quantitative explanation of double-slit fringes

The difference in phase between the two waves is determined by the difference in the distance travelled by the two waves.

If the viewing distance is large compared with the separation of the slits (the far field), the phase difference can be found using the geometry shown in the figure. The path difference between two waves travelling at an angle θ is given by $d\sin \theta \approx d\theta .$

When the two waves are in phase, i.e. the path difference is equal to an integral number of wavelengths, the summed amplitude, and therefore the summed intensity is maximal, and when they are in anti-phase, i.e. the path difference is equal to half a wavelength, one and a half wavelengths, etc., then the two waves cancel, and the summed intensity is zero. This effect is known as interference.

The interference fringe maxima occur at angles $d\theta _{n}=n\lambda ,\quad n=0,\pm 1,\pm 2,\ldots$ where λ is the wavelength of the light. The angular spacing of the fringes is given by $\theta _{\text{f}}\approx \lambda /d.$

When the distance between the slits and the viewing plane is *z*, the spacing of the fringes is equal to *zθ* and is the same as above: $w=z\lambda /d.$

### Diffraction by a grating

A grating is defined in Born and Wolf as "any arrangement which imposes on an incident wave a periodic variation of amplitude or phase, or both".

A grating whose elements are separated by *S* diffracts a normally incident beam of light into a set of beams, at angles *θ**n* given by:

$~\sin \theta _{n}={\frac {n\lambda }{S}},\quad n=0,\pm 1,\pm 2,\ldots$

This is known as the grating equation. The finer the grating spacing, the greater the angular separation of the diffracted beams.

If the light is incident at an angle θ0, the grating equation is: $\sin \theta _{n}={\frac {n\lambda }{S}}+\sin \theta _{0},\quad n=0,\pm 1,\pm 2,\ldots$

The detailed structure of the repeating pattern determines the form of the individual diffracted beams, as well as their relative intensity while the grating spacing always determines the angles of the diffracted beams.

The image on the right shows a laser beam diffracted by a grating into *n* = 0, and ±1 beams. The angles of the first order beams are about 20°; if we assume the wavelength of the laser beam is 600 nm, we can infer that the grating spacing is about 1.8 μm.

#### Semi-quantitative explanation

A simple grating consists of a series of slits in a screen. If the light travelling at an angle θ from each slit has a path difference of one wavelength with respect to the adjacent slit, all these waves will add together, so that the maximum intensity of the diffracted light is obtained when:

$W\sin \theta =n\lambda ,\quad n=0,\pm 1,\pm 2,\ldots$

This is the same relationship that is given above.
