---
title: "Total internal reflection (part 1/2)"
source: https://en.wikipedia.org/wiki/Total_internal_reflection
domain: geometric-optics
license: CC-BY-SA-4.0
tags: geometrical optics, focal length, optical aberration, total internal reflection
fetched: 2026-07-02
part: 1/2
---

# Total internal reflection

In physics, **total internal reflection** (**TIR**) is the phenomenon in which waves arriving at the interface (boundary) from one medium to another (e.g., from water to air) are not refracted into the second ("external") medium, but completely reflected back into the first ("internal") medium. It occurs when the second medium has a higher wave speed (i.e., lower refractive index) than the first, and the waves are incident at a sufficiently oblique angle on the interface. For example, the water-to-air surface in a typical fish tank, when viewed obliquely from below, reflects the underwater scene like a mirror with no loss of brightness (Fig. 1). A scenario opposite to TIR, referred to as total external reflection, occurs in the extreme ultraviolet and X-ray regimes.

TIR occurs not only with electromagnetic waves such as light and microwaves, but also with other types of waves, including sound and water waves. If the waves are capable of forming a narrow beam (Fig. 2), the reflection tends to be described in terms of "rays" rather than waves; in a medium whose properties are independent of direction, such as air, water or glass, the "rays" are perpendicular to associated wavefronts. The total internal reflection occurs when critical angle is exceeded.

Refraction is generally accompanied by *partial* reflection. When waves are refracted from a medium of lower propagation speed (higher refractive index) to a medium of higher propagation speed (lower refractive index)—e.g., from water to air—the *angle of refraction* (between the outgoing ray and the surface normal) is greater than the *angle of incidence* (between the incoming ray and the normal). As the angle of incidence approaches a certain threshold, called the *critical angle*, the angle of refraction approaches 90°, at which the refracted ray becomes parallel to the boundary surface. As the angle of incidence increases beyond the critical angle, the conditions of refraction can no longer be satisfied, so there is no refracted ray, and the partial reflection becomes total. For visible light, the critical angle is about 49° for incidence from water to air, and about 42° for incidence from common glass to air.

Details of the mechanism of TIR give rise to more subtle phenomena. While total reflection, by definition, involves no continuing flow of power *across* the interface between the two media, the external medium carries a so-called *evanescent wave*, which travels *along* the interface with an amplitude that falls off exponentially with distance from the interface. The "total" reflection is indeed total if the external medium is lossless (perfectly transparent), continuous, and of infinite extent, but can be conspicuously *less* than total if the evanescent wave is absorbed by a lossy external medium ("attenuated total reflectance"), or diverted by the outer boundary of the external medium or by objects embedded in that medium ("frustrated" TIR). Unlike *partial* reflection between transparent media, total internal reflection is accompanied by a non-trivial phase shift (not just zero or 180°) for each component of polarization (perpendicular or parallel to the plane of incidence), and the shifts vary with the angle of incidence. The explanation of this effect by Augustin-Jean Fresnel, in 1823, added to the evidence in favor of the wave theory of light.

The phase shifts are used by Fresnel's invention, the Fresnel rhomb, to modify polarization. The efficiency of the total internal reflection is exploited by optical fibers (used in telecommunications cables and in image-forming fiberscopes), and by reflective prisms, such as image-erecting Porro/roof prisms for monoculars and binoculars.


## Optical description

Although total internal reflection can occur with any kind of wave that can be said to have oblique incidence, including (e.g.) microwaves and sound waves,  it is most familiar in the case of light waves.

Total internal reflection of light can be demonstrated using a semicircular-cylindrical block of common glass or acrylic glass. In Fig. 3, a "ray box" projects a narrow beam of light (a "ray") radially inward. The semicircular cross-section of the glass allows the incoming ray to remain perpendicular to the curved portion of the air/glass surface, and then hence to continue in a straight line towards the flat part of the surface, although its angle with the flat part varies.

Where the ray meets the flat glass-to-air interface, the angle between the ray and the normal (perpendicular) to the interface is called the *angle of incidence*. If this angle is sufficiently small, the ray is *partly* reflected but mostly transmitted, and the transmitted portion is refracted away from the normal, so that the *angle of refraction* (between the refracted ray and the normal to the interface) is greater than the angle of incidence. For the moment, let us call the angle of incidence *θ*i and the angle of refraction *θ*t (where *t* is for *transmitted*, reserving *r* for *reflected*). As *θ*i increases and approaches a certain "critical angle", denoted by *θ*c (or sometimes *θ*cr), the angle of refraction approaches 90° (that is, the refracted ray approaches a tangent to the interface), and the refracted ray becomes fainter while the reflected ray becomes brighter. As *θ*i increases beyond *θ*c, the refracted ray disappears and only the reflected ray remains, so that all of the energy of the incident ray is reflected; this is total internal reflection (TIR). In brief:

- If  *θ*i < *θ*c‍,‍ the incident ray is split, being *partly* reflected and partly refracted;
- If  *θ*i > *θ*c‍,‍ the incident ray suffers total internal reflection (TIR); none of it is transmitted.


## Critical angle

The critical angle is the smallest angle of incidence that yields total reflection, or equivalently the largest angle for which a refracted ray exists. For light waves incident from an "internal" medium with a single refractive index *n*1, to an "external" medium with a single refractive index *n*2, the critical angle is given by $\theta _{\text{c}}=\arcsin(n_{2}/n_{1})$ and is defined if *n*2 ≤ *n*1. For some other types of waves, it is more convenient to think in terms of propagation velocities rather than refractive indices. The explanation of the critical angle in terms of velocities is more general and will therefore be discussed first.

When a wavefront is refracted from one medium to another, the incident (incoming) and refracted (outgoing) portions of the wavefront meet at a common line on the refracting surface (interface). Let this line, denoted by *L*, move at velocity u across the surface, where u is measured normal to *L* (Fig. 4). Let the incident and refracted wavefronts propagate with normal velocities $v_{1}$ and $v_{2}$ respectively, and let them make the dihedral angles *θ*1 and *θ*2 respectively with the interface. From the geometry, $v_{1}$ is the component of u in the direction normal to the incident wave, so that $v_{1}=u\sin \theta _{1}.$ Similarly, $v_{2}=u\sin \theta _{2}.$ Solving each equation for 1/*u* and equating the results, we obtain the general law of refraction for waves:

| ${\frac {\sin \theta _{1}}{v_{1}}}={\frac {\sin \theta _{2}}{v_{2}}}.$ |   | 1 |
|---|---|---|

But the dihedral angle between two planes is also the angle between their normals. So *θ*1 is the angle between the normal to the incident wavefront and the normal to the interface, while *θ*2 is the angle between the normal to the refracted wavefront and the normal to the interface; and Eq. (**1**) tells us that the sines of these angles are in the same ratio as the respective velocities.

This result has the form of "Snell's law", except that we have not yet said that the ratio of velocities is constant, nor identified *θ*1 and *θ*2 with the angles of incidence and refraction (called *θ*i and *θ*t above). However, if we now suppose that the properties of the media are *isotropic* (independent of direction), two further conclusions follow: first, the two velocities, and hence their ratio, are independent of their directions; and second, the wave-normal directions coincide with the *ray* directions, so that *θ*1 and *θ*2 coincide with the angles of incidence and refraction as defined above.

Obviously the angle of refraction cannot exceed 90°. In the limiting case, we put *θ*2 = 90° and *θ*1 = *θ*c in Eq. (**1**), and solve for the critical angle:

| $\theta _{\text{c}}=\arcsin(v_{1}/v_{2}).$ |   | 2 |
|---|---|---|

In deriving this result, we retain the assumption of isotropic media in order to identify *θ*1 and *θ*2 with the angles of incidence and refraction.

For electromagnetic waves, and especially for light, it is customary to express the above results in terms of *refractive indices*. The refractive index of a medium with normal velocity $v_{1}$ is defined as $n_{1}=c/v_{1},$ where *c* is the speed of light in vacuum. Hence $v_{1}=c/n_{1}.$ Similarly, $v_{2}=c/n_{2}.$ Making these substitutions in Eqs. (**1**) and (**2**), we obtain

| $n_{1}\sin \theta _{1}=n_{2}\sin \theta _{2}$ |   | 3 |
|---|---|---|

and

| $\theta _{\text{c}}=\arcsin(n_{2}/n_{1}).$ |   | 4 |
|---|---|---|

Eq. (**3**) is the law of refraction for general media, in terms of refractive indices, provided that *θ*1 and *θ*2 are taken as the dihedral angles; but if the media are *isotropic*, then *n*1 and *n*2 become independent of direction, while *θ*1 and *θ*2 may be taken as the angles of incidence and refraction for the rays, and Eq. (**4**) follows. So, for isotropic media, Eqs. (**3**) and (**4**) together describe the behavior in Fig. 5.

According to Eq. (**4**), for incidence from water (*n*1 ≈ 1.333) to air (*n*2 ≈ 1), we have *θ*c ≈ 48.6°, whereas for incidence from common or acrylic glass (*n*1 ≈ 1.50) to air (*n*2 ≈ 1), we have *θ*c ≈ 41.8°.

The arcsin function yielding *θ*c is defined only if *n*2 ≤ *n*1 $(v_{2}\geq v_{1}).$ Hence, for isotropic media, total internal reflection cannot occur if the second medium has a higher refractive index (lower normal velocity) than the first. For example, there cannot be TIR for incidence from air to water; rather, the critical angle for incidence from water to air is the angle of refraction at grazing incidence from air to water (Fig. 6).

The medium with the higher refractive index is commonly described as optically *denser*, and the one with the lower refractive index as optically *rarer*. Hence it is said that total internal reflection is possible for "dense-to-rare" incidence, but not for "rare-to-dense" incidence.


## Everyday examples

When standing beside an aquarium with one's eyes below the water level, one is likely to see fish or submerged objects reflected in the water-air surface (Fig. 1). The brightness of the reflected image – just as bright as the "direct" view – can be startling.

A similar effect can be observed by opening one's eyes while swimming just below the water's surface. If the water is calm, the surface outside the critical angle (measured from the vertical) appears mirror-like, reflecting objects below. The region above the water cannot be seen except overhead, where the hemispherical field of view is compressed into a conical field known as *Snell's window*, whose angular diameter is twice the critical angle (cf. Fig. 6).  The field of view above the water is theoretically 180° across, but seems less because as we look closer to the horizon, the vertical dimension is more strongly compressed by the refraction; e.g., by Eq. (**3**), for air-to-water incident angles of 90°, 80°, and 70°, the corresponding angles of refraction are 48.6° (*θcr* in Fig. 6), 47.6°, and 44.8°, indicating that the image of a point 20° above the horizon is 3.8° from the edge of Snell's window‍ while the image of a point 10° above the horizon is only 1° from the edge.

Fig. 7, for example, is a photograph taken near the bottom of the shallow end of a swimming pool. What looks like a broad horizontal stripe on the right-hand wall‍ consists of the lower edges of a row of orange tiles, and their reflections; this marks the water level, which can then be traced across the other wall. The swimmer has disturbed the surface above her, scrambling the lower half of her reflection, and distorting the reflection of the ladder (to the right). But most of the surface is still calm, giving a clear reflection of the tiled bottom of the pool. The space above the water is not visible except at the top of the frame, where the handles of the ladder are just discernible above the edge of Snell's window – within which the reflection of the bottom of the pool is only partial, but still noticeable in the photograph. One can even discern the color-fringing of the edge of Snell's window, due to variation of the refractive index, hence of the critical angle, with wavelength (see *Dispersion*).

The critical angle influences the angles at which gemstones are cut. The round "brilliant" cut, for example, is designed to refract light incident on the front facets, reflect it twice by TIR off the back facets, and transmit it out again through the front facets, so that the stone looks bright. Diamond (Fig. 8) is especially suitable for this treatment, because its high refractive index (about 2.42) and consequently small critical angle (about 24.5°) yield the desired behavior over a wide range of viewing angles. Cheaper materials that are similarly amenable to this treatment include cubic zirconia (index ≈ 2.15) and moissanite (non-isotropic, hence doubly refractive, with an index ranging from about 2.65 to 2.69, depending on direction and polarization); both of these are therefore popular as diamond simulants.


## Evanescent wave

Mathematically, waves are described in terms of time-varying fields, a "field" being a function of location in space. A propagating wave requires an "effort" field and a "flow" field, the latter being a vector (if we are working in two or three dimensions). The product of effort and flow is related to power (see *System equivalence*). For example, for sound waves in a non-viscous fluid, we might take the effort field as the pressure (a scalar), and the flow field as the fluid velocity (a vector). The product of these two is intensity (power per unit area). For electromagnetic waves, we shall take the effort field as the electric field  **E** , and the flow field as the magnetizing field  **H**. Both of these are vectors, and their vector product is again the intensity (see *Poynting vector*).

When a wave in (say) medium 1 is reflected off the interface between medium 1 and medium 2, the flow field in medium 1 is the vector sum of the flow fields due to the incident and reflected waves.  If the reflection is oblique, the incident and reflected fields are not in opposite directions and therefore cannot cancel out at the interface; even if the reflection is total, either the normal component or the tangential component of the combined field (as a function of location and time) must be non-zero adjacent to the interface. Furthermore, the physical laws governing the fields will generally imply that one of the two components is *continuous* across the interface (that is, it does not suddenly change as we cross the interface); for example, for electromagnetic waves, one of the interface conditions is that the tangential component of **H** is continuous if there is no surface current. Hence, even if the reflection is total, there must be some penetration of the flow field into medium 2; and this, in combination with the laws relating the effort and flow fields, implies that there will also be some penetration of the effort field. The same continuity condition implies that the variation ("waviness") of the field in medium 2 will be synchronized with that of the incident and reflected waves in medium 1.

But, if the reflection is total, the spatial penetration of the fields into medium 2 must be limited somehow, or else the total extent and hence the total energy of those fields would continue to increase, draining power from medium 1. Total reflection of a continuing wavetrain permits some energy to be stored in medium 2, but does not permit a *continuing* transfer of power from medium 1 to medium 2.

Thus, using mostly qualitative reasoning, we can conclude that total internal reflection must be accompanied by a wavelike field in the "external" medium, traveling along the interface in synchronism with the incident and reflected waves, but with some sort of limited spatial penetration into the "external" medium; such a field may be called an *evanescent wave*.

Fig. 9 shows the basic idea. The incident wave is assumed to be plane and sinusoidal. The reflected wave, for simplicity, is not shown. The evanescent wave travels to the right in lock-step with the incident and reflected waves, but its amplitude falls off with increasing distance from the interface.

(Two features of the evanescent wave in Fig. 9 are to be explained later: first, that the evanescent wave crests are perpendicular to the interface; and second, that the evanescent wave is slightly ahead of the incident wave.)

### Frustrated total internal reflection (FTIR)

If the internal reflection is to be total, there must be no diversion of the evanescent wave. Suppose, for example, that electromagnetic waves incident from glass (with a higher refractive index) to air (with a lower refractive index) at a certain angle of incidence are subject to TIR. And suppose that we have a third medium (often identical to the first) whose refractive index is sufficiently high that, if the third medium were to replace the second, we would get a standard transmitted wavetrain for the same angle of incidence. Then, if the third medium is brought within a distance of a few wavelengths from the surface of the first medium, where the evanescent wave has significant amplitude in the second medium, then the evanescent wave is effectively refracted into the third medium, giving non-zero transmission into the third medium, and therefore less than total reflection back into the first medium. As the amplitude of the evanescent wave decays across the air gap, the transmitted waves are attenuated, so that there is less transmission, and therefore more reflection, than there would be with no gap; but as long as there is *some* transmission, the reflection is less than total. This phenomenon is called *frustrated total internal reflection* (where "frustrated" negates "total"), abbreviated "frustrated TIR" or "FTIR".

Frustrated TIR can be observed by looking into the top of a glass of water held in one's hand (Fig. 10). If the glass is held loosely, contact may not be sufficiently close and widespread to produce a noticeable effect. But if it is held more tightly, the ridges of one's fingerprints interact strongly with the evanescent waves, allowing the ridges to be seen through the otherwise totally reflecting glass-air surface.

The same effect can be demonstrated with microwaves, using paraffin wax as the "internal" medium (where the incident and reflected waves exist). In this case the permitted gap width might be (e.g.) 1 cm or several cm, which is easily observable and adjustable.

The term *frustrated TIR* also applies to the case in which the evanescent wave is scattered by an object sufficiently close to the reflecting interface. This effect, together with the strong dependence of the amount of scattered light on the distance from the interface, is exploited in *total internal reflection microscopy*.

The mechanism of FTIR is called *evanescent-wave coupling*, and is a good analog to visualize quantum tunneling. Due to the wave nature of matter, an electron has a non-zero probability of "tunneling" through a barrier, even if classical mechanics would say that its energy is insufficient. Similarly, due to the wave nature of light, a photon has a non-zero probability of crossing a gap, even if ray optics would say that its approach is too oblique.

Another reason why internal reflection may be less than total, even beyond the critical angle, is that the external medium may be "lossy" (less than perfectly transparent), in which case the external medium will absorb energy from the evanescent wave, so that the maintenance of the evanescent wave will draw power from the incident wave. The consequent less-than-total reflection is called *attenuated total reflectance* (ATR). This effect, and especially the frequency-dependence of the absorption, can be used to study the composition of an unknown external medium.

### Derivation of evanescent wave

In a uniform plane sinusoidal electromagnetic wave, the electric field **E** has the form

| $\mathbf {E_{k}} e^{i(\mathbf {k\cdot r} -\omega t)},$ |   | 5 |
|---|---|---|

where **Ek** is the (constant) complex amplitude vector, *i* is the imaginary unit, **k** is the wave vector (whose magnitude *k* is the angular wavenumber), **r** is the position vector, *ω* is the angular frequency, *t* is time, and it is understood that the *real part* of the expression is the physical field. The magnetizing field **H** has the same form with the same **k** and *ω*. The value of the expression is unchanged if the position **r** varies in a direction normal to **k**; hence **k** *is normal to the wavefronts*.

If *ℓ* is the component of **r** in the direction of **k**, the field (**5**) can be written $\mathbf {E_{k}} e^{i(k\ell -\omega t)}.$ If the argument of $e^{i(\cdots )}$ is to be constant, *ℓ* must increase at the velocity $\omega /k,$ known as the *phase velocity*. This in turn is equal to $c/n,$ where *c* is the phase velocity in the reference medium (taken as vacuum), and *n* is the local refractive index w.r.t. the reference medium. Solving for *k* gives $k=n\omega /c,$ i.e.

| $k=nk_{0},$ |   | 6 |
|---|---|---|

where $k_{0}=\omega /c$ is the wavenumber in vacuum.

From (**5**), the electric field in the "external" medium has the form

| $\mathbf {E} _{\text{t}}=\mathbf {E} _{\mathbf {k} {\text{t}}}e^{i(\mathbf {k_{\text{t}}\cdot r} -\omega t)},$ |   | 7 |
|---|---|---|

where **k**t is the wave vector for the transmitted wave (we assume isotropic media, but the transmitted wave is not *yet* assumed to be evanescent).

In Cartesian coordinates (*x*, *y*, *z*), let the region *y* < 0 have refractive index *n*1, and let the region *y* > 0 have refractive index *n*2. Then the *xz* plane is the interface, and the *y* axis is normal to the interface (Fig. 11). Let **i** and **j** be the unit vectors in the *x* and *y* directions respectively. Let the plane of incidence (containing the incident wave-normal and the normal to the interface) be the *xy* plane (the plane of the page), with the angle of incidence *θ*i measured from **j** towards **i**. Let the angle of refraction, measured in the same sense, be *θ*t ("t" for *transmitted*, reserving "r" for *reflected*).

From (**6**), the transmitted wave vector **k**t has magnitude *n*2*k*0. Hence, from the geometry, $\mathbf {k} _{\text{t}}=n_{2}k_{0}(\mathbf {i} \sin \theta _{\text{t}}+\mathbf {j} \cos \theta _{\text{t}})=k_{0}(\mathbf {i} \,n_{1}\sin \theta _{\text{i}}+\mathbf {j} \,n_{2}\cos \theta _{\text{t}}),$ where the last step uses Snell's law. Taking the dot product with the position vector, we get $\mathbf {k} _{\text{t}}\cdot \mathbf {r} =k_{0}(n_{1}x\sin \theta _{\text{i}}+n_{2}y\cos \theta _{\text{t}}),$ so that Eq. (**7**) becomes

| $\mathbf {E} _{\text{t}}=\mathbf {E} _{\mathbf {k} {\text{t}}}\exp[i(n_{1}k_{0}x\sin \theta _{\text{i}}+n_{2}k_{0}y\cos \theta _{\text{t}}-\omega t)].$ |   | 8 |
|---|---|---|

In the case of TIR, the angle *θ*t does not exist in the usual sense. But we can still interpret (**8**) for the transmitted (evanescent) wave by allowing cos *θ*t to be *complex*. This becomes necessary when we write cos *θ*t in terms of sin *θ*t, and thence in terms of sin *θ*i using Snell's law: $\cos \theta _{\text{t}}={\sqrt {1-\sin ^{2}\theta _{\text{t}}}}={\sqrt {1-(n_{1}/n_{2})^{2}\sin ^{2}\theta _{\text{i}}}}.$ For *θ*i greater than the critical angle, the value under the square-root symbol is negative, so that

| $\cos \theta _{\text{t}}=\pm i\,{\sqrt {(n_{1}/n_{2})^{2}\sin ^{2}\theta _{\text{i}}-1}}.$ |   | 9 |
|---|---|---|

To determine which sign is applicable, we substitute (**9**) into (**8**), obtaining

| $\mathbf {E} _{\text{t}}=\mathbf {E} _{\mathbf {k} {\text{t}}}e^{\mp {\sqrt {n_{1}^{2}\sin ^{2}\theta _{\text{i}}-n_{2}^{2}}}\,k_{0}y}e^{i[(n_{1}k_{0}\sin \theta _{\text{i}})x-\omega t]},$ |   | 10 |
|---|---|---|

where the undetermined sign is the opposite of that in (**9**). For an *evanescent* transmitted wave – that is, one whose amplitude decays as *y* increases – the undetermined sign in (**10**) must be *minus*, so the undetermined sign in (**9**) must be *plus*.

With the correct sign, the result (**10**) can be abbreviated

| $\mathbf {E} _{\text{t}}\propto e^{-\kappa y}e^{i(k_{x}x-\omega t)},$ |   | 11 |
|---|---|---|

where

| ${\begin{aligned}\kappa &=k_{0}{\sqrt {n_{1}^{2}\sin ^{2}\theta _{\text{i}}-n_{2}^{2}}},\\k_{x}&=n_{1}k_{0}\sin \theta _{\text{i}},\end{aligned}}$ |   | 12 |
|---|---|---|

and *k*0 is the wavenumber in vacuum, i.e.  $\omega /c.$

So the evanescent wave is a plane sinewave traveling in the x direction, with an amplitude that decays exponentially in the y direction (Fig. 9). It is evident that the energy stored in this wave likewise travels in the x direction and does not cross the interface. Hence the Poynting vector generally has a component in the x direction, but its y component averages to zero (although its instantaneous y component is not *identically* zero).

Eq. (**11**) indicates that the amplitude of the evanescent wave falls off by a factor e as the coordinate y (measured from the interface) increases by the distance $d=1/\kappa ,$ commonly called the "penetration depth" of the evanescent wave. Taking reciprocals of the first equation of (**12**), we find that the penetration depth is $d={\frac {\lambda _{0}}{2\pi {\sqrt {n_{1}^{2}\sin ^{2}\theta _{\text{i}}-n_{2}^{2}}}}},$ where *λ*0 is the wavelength in vacuum, i.e. $2\pi /k_{0}.$ Dividing the numerator and denominator by *n*2 yields $d={\frac {\lambda _{2}}{2\pi {\sqrt {(n_{1}/n_{2})^{2}\sin ^{2}\theta _{\text{i}}-1}}}},$ where $\lambda _{2}=\lambda _{0}/n_{2}$ is the wavelength in the second (external) medium. Hence we can plot d in units of *λ*2 as a function of the angle of incidence for various values of $n_{1}/n_{2}$ (Fig. 12). As *θ*i decreases towards the critical angle, the denominator approaches zero, so that d increases without limit – as is to be expected, because as soon as *θ*i is *less* than critical, uniform plane waves are permitted in the external medium. As *θ*i approaches 90° (grazing incidence), d approaches a minimum $d_{\text{min}}={\frac {\lambda _{2}}{2\pi {\sqrt {(n_{1}/n_{2})^{2}-1}}}}.$ For incidence from water to air, or common glass to air, *d*min is not much different from *λ*2/(2*π*). But d is larger at smaller angles of incidence (Fig. 12), and the amplitude may still be significant at distances of several times d; for example, because e−4.6 is just greater than 0.01, the evanescent wave amplitude within a distance 4.6‍*d* of the interface is at least 1% of its value at the interface. Hence, speaking loosely, we tend to say that the evanescent wave amplitude is significant within "a few wavelengths" of the interface.


## Phase shifts

Between 1817 and 1823, Augustin-Jean Fresnel discovered that total internal reflection is accompanied by a non-trivial phase shift (that is, a phase shift that is not restricted to 0° or 180°), as the Fresnel reflection coefficient acquires a non-zero imaginary part. We shall now explain this effect for electromagnetic waves in the case of linear, homogeneous, isotropic, non-magnetic media. The phase shift turns out to be an *advance*, which grows as the incidence angle increases beyond the critical angle, but which depends on the polarization of the incident wave.

In equations (**5**), (**7**), (**8**), (**10**), and (**11**), we advance the phase by the angle *ϕ* if we replace *ωt* by *ωt* + *ϕ* (that is, if we replace −*ωt* by −*ωt* − *ϕ*), with the result that the (complex) field is multiplied by *e*−*iϕ*. So a phase *advance* is equivalent to multiplication by a complex constant with a *negative* argument. This becomes more obvious when (e.g.) the field (**5**) is factored as $\mathbf {E_{k}} e^{i\mathbf {k\cdot r} }e^{-i\omega t},$ where the last factor contains the time dependence.

To represent the polarization of the incident, reflected, or transmitted wave, the electric field adjacent to an interface can be resolved into two perpendicular components, known as the *s* and *p* components, which are parallel to the *surface* and the *plane* of incidence respectively; in other words, the *s* and *p* components are respectively *square* and *parallel* to the plane of incidence.

For each component of polarization, the incident, reflected, or transmitted electric field (**E** in Eq. (**5**)) has a certain direction and can be represented by its (complex) scalar component in that direction. The reflection or transmission coefficient can then be defined as a *ratio* of complex components at the same point, or at infinitesimally separated points on opposite sides of the interface. But, in order to fix the *signs* of the coefficients, we must choose positive senses for the "directions". For the *s* components, the obvious choice is to say that the positive directions of the incident, reflected, and transmitted fields are all the same (e.g., the z direction in Fig. 11). For the *p* components, this article adopts the convention that the positive directions of the incident, reflected, and transmitted fields are inclined towards the same medium (that is, towards the same side of the interface, e.g. like the red arrows in Fig. 11). But the reader should be warned that some books use a different convention for the *p* components, causing a different sign in the resulting formula for the reflection coefficient.

For the *s* polarization, let the reflection and transmission coefficients be rs and ts respectively. For the *p* polarization, let the corresponding coefficients be rp and tp . Then, for *linear, homogeneous, isotropic, non-magnetic* media, the coefficients are given by

| $r_{s}={\frac {n_{1}\cos \theta _{\text{i}}-n_{2}\cos \theta _{\text{t}}}{n_{1}\cos \theta _{\text{i}}+n_{2}\cos \theta _{\text{t}}}},$ |   | 13 |
|---|---|---|

| $t_{s}={\frac {2n_{1}\cos \theta _{\text{i}}}{n_{1}\cos \theta _{\text{i}}+n_{2}\cos \theta _{\text{t}}}},$ |   | 14 |
|---|---|---|

| $r_{p}={\frac {n_{2}\cos \theta _{\text{i}}-n_{1}\cos \theta _{\text{t}}}{n_{2}\cos \theta _{\text{i}}+n_{1}\cos \theta _{\text{t}}}},$ |   | 15 |
|---|---|---|

| $t_{p}={\frac {2n_{1}\cos \theta _{\text{i}}}{n_{2}\cos \theta _{\text{i}}+n_{1}\cos \theta _{\text{t}}}}.$ |   | 16 |
|---|---|---|

(For a derivation of the above, see Fresnel equations § Theory.)

Now we suppose that the transmitted wave is evanescent. With the correct sign (+), substituting (**9**) into (**13**) gives $r_{s}={\frac {n\cos \theta _{\text{i}}-i{\sqrt {n^{2}\sin ^{2}\theta _{\text{i}}-1}}}{n\cos \theta _{\text{i}}+i{\sqrt {n^{2}\sin ^{2}\theta _{\text{i}}-1}}}},$ where $n=n_{1}/n_{2};$ that is, n is the index of the "internal" medium relative to the "external" one, or the index of the internal medium if the external one is vacuum. So the magnitude of rs is 1, and the *argument* of rs is $-2\arctan {\frac {\sqrt {n^{2}\sin ^{2}\theta _{\text{i}}-1}}{n\cos \theta _{\text{i}}}},$ which gives a phase *advance* of

| $\delta _{s}=2\arctan {\frac {\sqrt {n^{2}\sin ^{2}\theta _{\text{i}}-1}}{n\cos \theta _{\text{i}}}}.$ |   | 17 |
|---|---|---|

Making the same substitution in (**14**), we find that ts has the same denominator as rs with a positive real numerator (instead of a complex conjugate numerator) and therefore has *half* the argument of *rs*, so that *the phase advance of the evanescent wave is half that of the reflected wave*.

With the same choice of sign, substituting (**9**) into (**15**) gives $r_{p}={\frac {\cos \theta _{\text{i}}-in{\sqrt {n^{2}\sin ^{2}\theta _{\text{i}}-1}}}{\cos \theta _{\text{i}}+in{\sqrt {n^{2}\sin ^{2}\theta _{\text{i}}-1}}}},$ whose magnitude is 1, and whose argument is $-2\arctan {\frac {n{\sqrt {n^{2}\sin ^{2}\theta _{\text{i}}-1}}}{\cos \theta _{\text{i}}}},$ which gives a phase *advance* of

| $\delta _{p}=2\arctan {\frac {n{\sqrt {n^{2}\sin ^{2}\theta _{\text{i}}-1}}}{\cos \theta _{\text{i}}}}.$ |   | 18 |
|---|---|---|

Making the same substitution in (**16**), we again find that the phase advance of the evanescent wave is *half* that of the reflected wave.

Equations (**17**) and (**18**) apply when *θ*c ≤ *θ*i < 90°, where *θ*i is the angle of incidence, and *θ*c is the critical angle arcsin (1/*n*). These equations show that

- each phase advance is zero at the critical angle (for which the numerator is zero);
- each phase advance approaches 180° as *θ*i → 90°; and
- *δp > δs* at intermediate values of *θ*i (because the factor *n* is in the numerator of (**18**) and the denominator of (**17**)).

For *θ*i ≤ *θ*c, the reflection coefficients are given by equations (**13**) and (**15**) and are *real*, so that the phase shift is either 0° (if the coefficient is positive) or 180° (if the coefficient is negative).

In (**13**), if we put $n_{2}=n_{1}\sin \theta _{\text{i}}/\sin \theta _{\text{t}}$ (Snell's law) and multiply the numerator and denominator by ⁠1/*n*1⁠ sin *θ*t, we obtain

| $r_{s}=-{\frac {\sin(\theta _{\text{i}}-\theta _{\text{t}})}{\sin(\theta _{\text{i}}+\theta _{\text{t}})}},$ |   | 19 |
|---|---|---|

which is positive for all angles of incidence with a transmitted ray (since *θ*t > *θ*i), giving a phase shift δs of zero.

If we do likewise with (**15**), the result is easily shown to be equivalent to

| $r_{p}={\frac {\tan(\theta _{\text{i}}-\theta _{\text{t}})}{\tan(\theta _{\text{i}}+\theta _{\text{t}})}},$ |   | 20 |
|---|---|---|

which is negative for small angles (that is, near normal incidence), but changes sign at *Brewster's angle*, where *θ*i and *θ*t are complementary. Thus the phase shift δp is 180° for small *θ*i but switches to 0° at Brewster's angle. Combining the complementarity with Snell's law yields *θ*i = arctan (1/*n*) as Brewster's angle for dense-to-rare incidence.

(Equations (**19**) and (**20**) are known as *Fresnel's sine law* and *Fresnel's tangent law*. Both reduce to 0/0 at normal incidence, but yield the correct results in the limit as *θ*i → 0. That they have opposite signs as we approach normal incidence is an obvious disadvantage of the sign convention used in this article; the corresponding advantage is that they have the same signs at grazing incidence.)

That completes the information needed to plot δs and δp for all angles of incidence. This is done in Fig. 13, with δp in red and δs in blue, for three refractive indices. On the angle-of-incidence scale (horizontal axis), Brewster's angle is where δp (red) falls from 180° to 0°, and the critical angle is where both δp and δs (red and blue) start to rise again. To the left of the critical angle is the region of *partial* reflection, where both reflection coefficients are real (phase 0° or 180°) with magnitudes less than 1. To the right of the critical angle is the region of *total* reflection, where both reflection coefficients are complex with magnitudes equal to 1. In that region, the black curves show the phase advance of the *p* component relative to the *s* component: $\delta =\delta _{p}-\delta _{s}.$ It can be seen that a refractive index of 1.45 is not enough to give a 45° phase difference, whereas a refractive index of 1.5 is enough (by a slim margin) to give a 45° phase difference at two angles of incidence: about 50.2° and 53.3°.

This 45° relative shift is employed in Fresnel's invention, now known as the Fresnel rhomb, in which the angles of incidence are chosen such that the two internal reflections cause a total relative phase shift of 90° between the two polarizations of an incident wave. This device performs the same function as a birefringent quarter-wave plate, but is more achromatic (that is, the phase shift of the rhomb is less sensitive to wavelength). Either device may be used, for instance, to transform linear polarization to circular polarization (which Fresnel also discovered) and conversely.

In Fig. 13, δ is computed by a final subtraction; but there are other ways of expressing it. Fresnel himself, in 1823, gave a formula for cos *δ*. Born and Wolf (1970, p. 50) derive an expression for tan (*δ*/2) and find its maximum analytically.

For TIR of a beam with finite width, the variation in the phase shift with the angle of incidence gives rise to the *Goos–Hänchen effect*, which is a lateral shift of the reflected beam within the plane of incidence. This effect applies to linear polarization in the *s* or *p* direction. The *Imbert–Fedorov effect* is an analogous effect for circular or elliptical polarization and produces a shift perpendicular to the plane of incidence.


## Applications

**Optical fibers** exploit total internal reflection to carry signals over long distances with little attenuation. They are used in telecommunication cables, and in image-forming fiberscopes such as colonoscopes.

In the **catadioptric Fresnel lens**, invented by Augustin-Jean Fresnel for use in lighthouses, the outer prisms use TIR to deflect light from the lamp through a greater angle than would be possible with purely refractive prisms, but with less absorption of light (and less risk of tarnishing) than with conventional mirrors.

Other **reflecting prisms** that use TIR include the following (with some overlap between the categories):

- **Image-erecting prisms** for binoculars and spotting scopes include paired 45°-90°-45° Porro prisms (Fig. 14), the Porro–Abbe prism, the inline Koenig and Abbe–Koenig prisms, and the compact inline Schmidt–Pechan prism. (The last consists of two components, of which one is a kind of Bauernfeind prism, which requires a reflective coating on one of its two reflecting faces, due to a sub-critical angle of incidence.) These prisms have the additional function of folding the optical path from the objective lens to the prime focus, reducing the overall length for a given primary focal length.
- A **prismatic star diagonal** for an astronomical telescope may consist of a single Porro prism (configured for a single reflection, giving a mirror-reversed image) or an Amici roof prism (which gives a non-reversed image).
- **Roof prisms** use TIR at two faces meeting at a sharp 90° angle. This category includes the Koenig, Abbe–Koenig, Schmidt–Pechan, and Amici types (already mentioned), and the roof pentaprism used in SLR cameras; the last of these requires a reflective coating on one non-TIR face.
- A **prismatic corner reflector** uses three total internal reflections to reverse the direction of incoming light.
- The **Dove prism** gives an inline view with mirror-reversal.

**Polarizing prisms**: Although the Fresnel rhomb, which converts between linear and elliptical polarization, is not birefringent (doubly refractive), there are other kinds of prisms that combine birefringence with TIR in such a way that light of a particular polarization is totally reflected while light of the orthogonal polarization is at least partly transmitted. Examples include the Nicol prism, Glan–Thompson prism, Glan–Foucault prism (or "Foucault prism"), and Glan–Taylor prism.

**Refractometers**, which measure refractive indices, often use the critical angle.

**Rain sensors** for automatic windscreen/windshield wipers have been implemented using the principle that total internal reflection will guide an infrared beam from a source to a detector if the outer surface of the windshield is dry, but any water drops on the surface will divert some of the light.

**Edge-lit LED panels**, used (e.g.) for backlighting of LCD computer monitors, exploit TIR to confine the LED light to the acrylic glass pane, except that some of the light is scattered by etchings on one side of the pane, giving an approximately uniform luminous emittance.

**Total internal reflection microscopy** (TIRM) uses the evanescent wave to illuminate small objects close to the reflecting interface. The consequent scattering of the evanescent wave (a form of frustrated TIR), makes the objects appear bright when viewed from the "external" side. In the *total internal reflection fluorescence microscope* (TIRFM), instead of relying on simple scattering, we choose an evanescent wavelength short enough to cause fluorescence (Fig. 15). The high sensitivity of the illumination to the distance from the interface allows measurement of extremely small displacements and forces.

A **beam-splitter cube** uses frustrated TIR to divide the power of the incoming beam between the transmitted and reflected beams. The width of the air gap (or low-refractive-index gap) between the two prisms can be made adjustable, giving higher transmission and lower reflection for a narrower gap, or higher reflection and lower transmission for a wider gap.

**Optical modulation** can be accomplished by means of frustrated TIR with a rapidly variable gap. As the transmission coefficient is highly sensitive to the gap width (the function being approximately exponential until the gap is almost closed), this technique can achieve a large dynamic range.

**Optical fingerprinting** devices have used frustrated TIR to record images of persons' fingerprints without the use of ink (cf. Fig. 11).

**Gait analysis** can be performed by using frustrated TIR with a high-speed camera, to capture and analyze footprints.

A **gonioscope**, used in optometry and ophthalmology for the diagnosis of glaucoma, *suppresses* TIR in order to look into the angle between the iris and the cornea. This view is usually blocked by TIR at the cornea-air interface. The gonioscope replaces the air with a higher-index medium, allowing transmission at oblique incidence, typically followed by reflection in a "mirror", which itself may be implemented using TIR.

Some **multi-touch** interactive tables and whiteboards utilise FTIR to detect fingers touching the screen. An infrared camera is placed behind the screen surface, which is edge-lit by infrared LEDs; when touching the surface FTIR causes some of the infrared light to escape the screen plane, and the camera sees this as bright areas. Computer vision software is then used to translate this into a series of coordinates and gestures.
