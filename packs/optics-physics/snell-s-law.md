---
title: "Snell's law"
source: https://en.wikipedia.org/wiki/Snell's_law
domain: optics-physics
license: CC-BY-SA-4.0
tags: physical optics, optical refraction, wave polarization, light diffraction
fetched: 2026-07-02
---

# Snell's law

**Snell's law** (also known as the **Snell–Descartes law**, and the **law of refraction**) is a formula used to describe the relationship between the angles of incidence and refraction, when referring to light or other waves passing through a boundary between two different isotropic media, such as water, glass, or air. In optics, the law is used in ray tracing to compute the angles of transmission or refraction, and in experimental optics to find the refractive index of a material. The law is also satisfied in meta-materials, which allow light to be bent "backward" at a negative angle of refraction with a negative refractive index.

The law states that, for a given pair of media, the ratio of the sines of angle of incidence $\left(\theta _{1}\right)$ and angle of refraction $\left(\theta _{2}\right)$ is equal to the refractive index of the second medium with regard to the first ( $n_{2,1}$ ) which is equal to the ratio of the refractive indices $\left({\tfrac {n_{2}}{n_{1}}}\right)$ of the two media, or equivalently, to the ratio of the phase velocities $\left({\tfrac {v_{1}}{v_{2}}}\right)$ in the two media.

${\frac {\sin \theta _{1}}{\sin \theta _{2}}}=n_{2,1}={\frac {n_{2}}{n_{1}}}={\frac {v_{1}}{v_{2}}}$

The law follows from Fermat's principle of least time, which in turn follows from the propagation of light as waves.

## History

Ptolemy, in Alexandria, Egypt, had found a relationship regarding refraction angles, but it was inaccurate for angles that were not small. Ptolemy was confident he had found an accurate empirical law, partially as a result of slightly altering his data to fit theory (see: confirmation bias).

The law was eventually named after Snell, although it was first discovered by the Persian scientist Ibn Sahl, at Baghdad court in 984. In the manuscript *On Burning Mirrors and Lenses*, Sahl used the law to derive lens shapes that focus light with no geometric aberration.

Ibn al-Haytham, in his *Book of Optics* (1021), came close to rediscovering the law of refraction, but he did not take this step.

The law was rediscovered by Thomas Harriot in 1602, who however did not publish his results although he had corresponded with Kepler on this very subject. In 1621, the Dutch astronomer Willebrord Snellius (1580–1626)—Snell—derived a mathematically equivalent form, that remained unpublished during his lifetime. René Descartes independently derived the law using heuristic momentum conservation arguments in terms of sines in his 1637 essay *La Dioptrique*, and used it to solve a range of optical problems. Rejecting Descartes' solution, Pierre de Fermat arrived at the same solution based solely on his principle of least time. Descartes assumed the speed of light was infinite, yet in his derivation of Snell's law he also assumed the denser the medium, the greater the speed of light. Fermat supported the opposing assumptions, i.e., the speed of light is finite, and his derivation depended upon the speed of light being slower in a denser medium. Fermat's derivation also utilized his invention of adequality, a mathematical procedure equivalent to differential calculus, for finding maxima, minima, and tangents.

In his influential mathematics book *Geometry*, Descartes solves a problem that was worked on by Apollonius of Perga and Pappus of Alexandria. Given n lines L and a point P(L) on each line, find the locus of points Q such that the lengths of the line segments QP(L) satisfy certain conditions. For example, when n = 4, given the lines a, b, c, and d and a point A on a, B on b, and so on, find the locus of points Q such that the product QA*QB equals the product QC*QD. When the lines are not all parallel, Pappus showed that the loci are conics, but when Descartes considered larger n, he obtained cubic and higher degree curves. To show that the cubic curves were interesting, he showed that they arose naturally in optics from Snell's law.

According to Dijksterhuis, "In *De natura lucis et proprietate* (1662) Isaac Vossius said that Descartes had seen Snell's paper and concocted his own proof. We now know this charge to be undeserved but it has been adopted many times since." Both Fermat and Huygens repeated this accusation that Descartes had copied Snell. In French, Snell's Law is sometimes called "la loi de Descartes" or more frequently "*loi de Snell-Descartes*".

In his 1678 *Traité de la Lumière*, Christiaan Huygens showed how Snell's law of sines could be explained by, or derived from, the wave nature of light, using what we have come to call the Huygens–Fresnel principle.

With the development of modern optical and electromagnetic theory, Snell's law was redefined. In 1962, Nicolaas Bloembergen showed that at the boundary of nonlinear medium, Snell's law could be written in a general form. In 2008 and 2011, plasmonic metasurfaces were also demonstrated to change the reflection and refraction directions of light beam.

## Explanation

Snell's law is used to determine the direction of light rays through refractive media with varying indices of refraction. The indices of refraction of the media, labeled $n_{1}$ , $n_{2}$ and so on, are used to represent the factor by which a light ray's speed decreases when traveling through a refractive medium, such as glass or water, as opposed to its velocity in a vacuum.

As light passes the border between media, depending upon the relative refractive indices of the two media, the light will either be refracted to a lesser angle, or a greater one. These angles are measured with respect to the *normal line*, represented perpendicular to the boundary. In the case of light traveling from air into water, light would be refracted towards the normal line, because the light is slowed down in water; light traveling from water to air would refract away from the normal line.

Refraction between two surfaces is also referred to as *reversible* because if all conditions were identical, the angles would be the same for light propagating in the opposite direction.

Snell's law is generally true only for isotropic or specular media (such as glass). In anisotropic media such as some crystals, birefringence may split the refracted ray into two rays, the *ordinary* or *o*-ray which follows Snell's law, and the other *extraordinary* or *e*-ray which may not be co-planar with the incident ray.

When the light or other wave involved is monochromatic, that is, of a single frequency, Snell's law can also be expressed in terms of a ratio of wavelengths in the two media, $\lambda _{1}$ and $\lambda _{2}$ :

${\frac {\sin \theta _{1}}{\sin \theta _{2}}}={\frac {v_{1}}{v_{2}}}={\frac {\lambda _{1}}{\lambda _{2}}}$

## Derivations and formula

Snell's law can be derived in various ways.

### Derivation from Fermat's principle

Snell's law can be derived from Fermat's principle, which states that the light travels the path which takes the least time. By taking the derivative of the optical path length, the stationary point is found giving the path taken by the light. (There are situations of light violating Fermat's principle by not taking the least time path, as in reflection in a (spherical) mirror.) In a classic analogy, the area of lower refractive index is replaced by a beach, the area of higher refractive index by the sea, and the fastest way for a rescuer on the beach to get to a drowning person in the sea is to run along a path that follows Snell's law.

As shown in the figure to the right, assume the refractive index of medium 1 and medium 2 are $n_{1}$ and $n_{2}$ respectively. Light enters medium 2 from medium 1 via point O.

$\theta _{1}$ is the angle of incidence, $\theta _{2}$ is the angle of refraction with respect to the normal.

The phase velocities of light in medium 1 and medium 2 are $v_{1}=c/n_{1}$ and $v_{2}=c/n_{2}$ respectively, where c is the speed of light in vacuum.

Let *T* be the time required for the light to travel from point Q through point O to point P. ${\begin{aligned}T&={\frac {\sqrt {x^{2}+a^{2}}}{v_{1}}}+{\frac {\sqrt {b^{2}+(\ell -x)^{2}}}{v_{2}}}\\&={\frac {\sqrt {x^{2}+a^{2}}}{v_{1}}}+{\frac {\sqrt {b^{2}+\ell ^{2}-2\ell x+x^{2}}}{v_{2}}}\end{aligned}}$ where *a*, *b*, *ℓ*, and *x* are as denoted in the right-hand figure, *x* being the varying parameter.

To minimize it, one can differentiate: ${\frac {dT}{dx}}={\frac {x}{v_{1}{\sqrt {x^{2}+a^{2}}}}}+{\frac {-(\ell -x)}{v_{2}{\sqrt {(\ell -x)^{2}+b^{2}}}}}$ and set it to 0 to find the stationary points.

Note that ${\frac {x}{\sqrt {x^{2}+a^{2}}}}=\sin \theta _{1}$

and ${\frac {\ell -x}{\sqrt {(\ell -x)^{2}+b^{2}}}}=\sin \theta _{2}$

Therefore,

${\frac {dT}{dx}}={\frac {\sin \theta _{1}}{v_{1}}}-{\frac {\sin \theta _{2}}{v_{2}}}=0$ ${\begin{aligned}{\frac {\sin \theta _{1}}{v_{1}}}&={\frac {\sin \theta _{2}}{v_{2}}}\\{\frac {n_{1}\sin \theta _{1}}{c}}&={\frac {n_{2}\sin \theta _{2}}{c}}\\n_{1}\sin \theta _{1}&=n_{2}\sin \theta _{2}\end{aligned}}$

### Derivation from Huygens's principle

Alternatively, Snell's law can be derived using interference of all possible paths of light wave from source to observer—it results in destructive interference.

### Derivation from Maxwell's equations

Another way to derive Snell's Law involves an application of the general boundary conditions of Maxwell equations for electromagnetic radiation and induction.

### Derivation from conservation of energy and momentum

Yet another way to derive Snell's law is based on translation symmetry considerations. For example, a homogeneous surface perpendicular to the z direction cannot change the transverse momentum. Since the propagation vector $\mathbf {k}$ is proportional to the photon's momentum, the transverse propagation direction $(k_{x},k_{y},0)$ must remain the same in both regions. Assume without loss of generality a plane of incidence in the $z,x$ plane $k_{x{\text{Region}}_{1}}=k_{x{\text{Region}}_{2}}$ . Using the well known dependence of the wavenumber on the refractive index of the medium, we derive Snell's law immediately.

${\begin{aligned}k_{x{\text{Region}}_{1}}&=k_{x{\text{Region}}_{2}}\\n_{1}k_{0}\sin \theta _{1}&=n_{2}k_{0}\sin \theta _{2}\\n_{1}\sin \theta _{1}&=n_{2}\sin \theta _{2}\end{aligned}}$

where $k_{0}={\frac {2\pi }{\lambda _{0}}}={\frac {\omega }{c}}$ is the wavenumber in vacuum. Although no surface is truly homogeneous at the atomic scale, full translational symmetry is an excellent approximation whenever the region is homogeneous on the scale of the light wavelength.

### Vector form

Given a normalized light vector ${\boldsymbol {\ell }}$ (pointing from the light source toward the surface) and a normalized plane normal vector $\mathbf {n}$ , one can work out the normalized reflected and refracted rays, via the cosines of the angle of incidence $\theta _{1}$ and angle of refraction $\theta _{2}$ , without explicitly using the sine values or any trigonometric functions or angles:

$\cos \theta _{1}=-\mathbf {n} \cdot {\boldsymbol {\ell }}$

Note: $\cos \theta _{1}$ must be positive, which it will be if $\mathbf {n}$ is the normal vector that points from the surface toward the side where the light is coming from, the region with index $n_{1}$ . If $\cos \theta _{1}$ is negative, then $\mathbf {n}$ points to the side without the light, so start over with $\mathbf {n}$ replaced by its negative.

$\mathbf {v} _{\mathrm {reflect} }={\boldsymbol {\ell }}+2\cos \theta _{1}\mathbf {n}$ This reflected direction vector points back toward the side of the surface where the light came from.

Now apply Snell's law to the ratio of sines to derive the formula for the refracted ray's direction vector: $\sin \theta _{2}={\frac {n_{1}}{n_{2}}}\sin \theta _{1}={\frac {n_{1}}{n_{2}}}{\sqrt {1-\left(\cos \theta _{1}\right)^{2}}}$ $\cos \theta _{2}={\sqrt {1-(\sin \theta _{2})^{2}}}={\sqrt {1-\left({\frac {n_{1}}{n_{2}}}\right)^{2}\left(1-\left(\cos \theta _{1}\right)^{2}\right)}}$ $\mathbf {v} _{\mathrm {refract} }=\left({\frac {n_{1}}{n_{2}}}\right){\boldsymbol {\ell }}+\left({\frac {n_{1}}{n_{2}}}\cos \theta _{1}-\cos \theta _{2}\right)\mathbf {n}$

The formula may appear simpler in terms of renamed simple values $r=n_{1}/n_{2}$ and $c=-\mathbf {n} \cdot {\boldsymbol {\ell }}$ , avoiding any appearance of trig function names or angle names: $\mathbf {v} _{\mathrm {refract} }=r{\boldsymbol {\ell }}+\left(rc-{\sqrt {1-r^{2}\left(1-c^{2}\right)}}\right)\mathbf {n}$

Example: ${\boldsymbol {\ell }}=\{0.707107,-0.707107\},~\mathbf {n} =\{0,1\},~r={\frac {n_{1}}{n_{2}}}=0.9$ $c=\cos \theta _{1}=0.707107,~{\sqrt {1-r^{2}\left(1-c^{2}\right)}}=\cos \theta _{2}=0.771362$ $\mathbf {v} _{\mathrm {reflect} }=\{0.707107,0.707107\},~\mathbf {v} _{\mathrm {refract} }=\{0.636396,-0.771362\}$

The cosine values may be saved and used in the Fresnel equations for working out the intensity of the resulting rays.

Total internal reflection is indicated by a negative radicand in the equation for $\cos \theta _{2}$ , which can only happen for rays crossing into a less-dense medium ( $n_{2}<n_{1}$ ). In applied optics, these vector calculations are sequentially utilized to model complex multi-layer optical stacks, such as anti-reflective coatings or display panels. In these systems, the lateral beam displacement and total internal reflection conditions must be verified at each dielectric interface to ensure precision alignment.

## Total internal reflection and critical angle

When light travels from a medium with a higher refractive index to one with a lower refractive index, Snell's law seems to require in some cases (whenever the angle of incidence is large enough) that the sine of the angle of refraction be greater than one. This of course is impossible, and the light in such cases is completely reflected by the boundary, a phenomenon known as total internal reflection. The largest possible angle of incidence which still results in a refracted ray is called the **critical angle**; in this case the refracted ray travels along the boundary between the two media.

For example, consider a ray of light moving from water to air with an angle of incidence of 50°. The refractive indices of water and air are approximately 1.333 and 1, respectively, so Snell's law gives us the relation

$\sin \theta _{2}={\frac {n_{1}}{n_{2}}}\sin \theta _{1}={\frac {1.333}{1}}\cdot \sin \left(50^{\circ }\right)=1.333\cdot 0.766=1.021,$

which is impossible to satisfy. The critical angle *θ*crit is the value of *θ*1 for which *θ*2 equals 90°:

$\theta _{\text{crit}}=\arcsin \left({\frac {n_{2}}{n_{1}}}\sin \theta _{2}\right)=\arcsin {\frac {n_{2}}{n_{1}}}=48.6^{\circ }.$

## Dispersion

In many wave-propagation media, wave velocity changes with frequency or wavelength of the waves; this is true of light propagation in most transparent substances other than a vacuum. These media are called dispersive. The result is that the angles determined by Snell's law also depend on frequency or wavelength, so that a ray of mixed wavelengths, such as white light, will spread or disperse. Such dispersion of light in glass or water underlies the origin of rainbows and other optical phenomena, in which different wavelengths appear as different colors.

In optical instruments, dispersion leads to chromatic aberration; a color-dependent blurring that sometimes is the resolution-limiting effect. This was especially true in refracting telescopes, before the invention of achromatic objective lenses.

## Lossy, absorbing, or conducting media

In a conducting medium, permittivity and index of refraction are complex-valued. Consequently, so are the angle of refraction and the wave-vector. This implies that, while the surfaces of constant real phase are planes whose normals make an angle equal to the angle of refraction with the interface normal, the surfaces of constant amplitude, in contrast, are planes parallel to the interface itself. Since these two planes do not in general coincide with each other, the wave is said to be inhomogeneous. The refracted wave is exponentially attenuated, with exponent proportional to the imaginary component of the index of refraction.
