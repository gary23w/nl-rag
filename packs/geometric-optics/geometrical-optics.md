---
title: "Geometrical optics"
source: https://en.wikipedia.org/wiki/Geometrical_optics
domain: geometric-optics
license: CC-BY-SA-4.0
tags: geometrical optics, focal length, optical aberration, total internal reflection
fetched: 2026-07-02
---

# Geometrical optics

**Geometrical optics**, or **ray optics**, is a model of optics that describes light propagation in terms of *rays*. The ray in geometrical optics is an abstraction useful for approximating the paths along which light propagates under certain circumstances.

The simplifying assumptions of geometrical optics include that light rays:

- propagate in straight-line paths as they travel in a homogeneous medium
- bend, and in particular circumstances may split in two, at the interface between two dissimilar media
- follow curved paths in a medium in which the refractive index changes
- may be absorbed or reflected.

Geometrical optics does not account for certain optical effects such as diffraction and interference, which are considered in physical optics. This simplification is useful in practice; it is an excellent approximation when the wavelength is small compared to the size of structures with which the light interacts. The techniques are particularly useful in describing geometrical aspects of imaging, including optical aberrations.

## Explanation

A light ray is a line or curve that is perpendicular to the light's wavefronts (and is therefore collinear with the wave vector). A slightly more rigorous definition of a light ray follows from Fermat's principle, which states that the path taken between two points by a ray of light is the path that can be traversed in the least time.

Geometrical optics is often simplified by making the paraxial approximation, or "small angle approximation". The mathematical behavior then becomes linear, allowing optical components and systems to be described by simple matrices. This leads to the techniques of Gaussian optics and *paraxial ray tracing*, which are used to find basic properties of optical systems, such as approximate image and object positions and magnifications.

## Reflection

Glossy surfaces such as mirrors reflect light in a simple, predictable way. This allows for production of reflected images that can be associated with an actual (real) or extrapolated (virtual) location in space.

With such surfaces, the direction of the reflected ray is determined by the angle the incident ray makes with the surface normal, a line perpendicular to the surface at the point where the ray hits. The incident and reflected rays lie in a single plane, and the angle between the reflected ray and the surface normal is the same as that between the incident ray and the normal. This is known as the Law of Reflection.

For flat mirrors, the law of reflection implies that images of objects are upright and the same distance behind the mirror as the objects are in front of the mirror. The image size is the same as the object size. (The magnification of a flat mirror is equal to one.) The law also implies that mirror images are parity inverted, which is perceived as a left-right inversion.

Mirrors with curved surfaces can be modeled by ray tracing and using the law of reflection at each point on the surface. For mirrors with parabolic surfaces, parallel rays incident on the mirror produce reflected rays that converge at a common focus. Other curved surfaces may also focus light, but with aberrations due to the diverging shape causing the focus to be smeared out in space. In particular, spherical mirrors exhibit spherical aberration. Curved mirrors can form images with magnification greater than or less than one, and the image can be upright or inverted. An upright image formed by reflection in a mirror is always virtual, while an inverted image is real and can be projected onto a screen.

## Refraction

Refraction occurs when light travels through an area of space that has a changing index of refraction. The simplest case of refraction occurs when there is an interface between a uniform medium with index of refraction $n_{1}$ and another medium with index of refraction $n_{2}$ . In such situations, Snell's Law describes the resulting deflection of the light ray: $n_{1}\sin \theta _{1}=n_{2}\sin \theta _{2}$ where $\theta _{1}$ and $\theta _{2}$ are the angles between the normal (to the interface) and the incident and refracted waves, respectively. This phenomenon is also associated with a changing speed of light as seen from the definition of index of refraction provided above which implies: $v_{1}\sin \theta _{2}\ =v_{2}\sin \theta _{1}$ where $v_{1}$ and $v_{2}$ are the wave velocities through the respective media.

Various consequences of Snell's Law include the fact that for light rays traveling from a material with a high index of refraction to a material with a low index of refraction, it is possible for the interaction with the interface to result in zero transmission. This phenomenon is called total internal reflection and allows for fiber optics technology. As light signals travel down a fiber optic cable, they undergo total internal reflection allowing for essentially no light lost over the length of the cable. It is also possible to produce polarized light rays using a combination of reflection and refraction: When a refracted ray and the reflected ray form a right angle, the reflected ray has the property of "plane polarization". The angle of incidence required for such a scenario is known as Brewster's angle.

Snell's Law can be used to predict the deflection of light rays as they pass through "linear media" as long as the indexes of refraction and the geometry of the media are known. For example, the propagation of light through a prism results in the light ray being deflected depending on the shape and orientation of the prism. Additionally, since different frequencies of light have slightly different indexes of refraction in most materials, refraction can be used to produce dispersion spectra that appear as rainbows. The discovery of this phenomenon when passing light through a prism is famously attributed to Isaac Newton.

Some media have an index of refraction which varies gradually with position and, thus, light rays curve through the medium rather than travel in straight lines. This effect is what is responsible for mirages seen on hot days where the changing index of refraction of the air causes the light rays to bend creating the appearance of specular reflections in the distance (as if on the surface of a pool of water). Material that has a varying index of refraction is called a gradient-index (GRIN) material and has many useful properties used in modern optical scanning technologies including photocopiers and scanners. The phenomenon is studied in the field of gradient-index optics.

A device which produces converging or diverging light rays due to refraction is known as a lens. Thin lenses produce focal points on either side that can be modeled using the lensmaker's equation. In general, two types of lenses exist: convex lenses, which cause parallel light rays to converge, and concave lenses, which cause parallel light rays to diverge. The detailed prediction of how images are produced by these lenses can be made using ray-tracing similar to curved mirrors. Similarly to curved mirrors, thin lenses follow a simple equation that determines the location of the images given a particular focal length ( f ) and object distance ( $S_{1}$ ): ${\frac {1}{S_{1}}}+{\frac {1}{S_{2}}}={\frac {1}{f}}$ where $S_{2}$ is the distance associated with the image and is considered by convention to be negative if on the same side of the lens as the object and positive if on the opposite side of the lens. The focal length f is considered negative for concave lenses.

Incoming parallel rays are focused by a convex lens into an inverted real image one focal length from the lens, on the far side of the lens.

Rays from an object at finite distance are focused further from the lens than the focal distance; the closer the object is to the lens, the further the image is from the lens. With concave lenses, incoming parallel rays diverge after going through the lens, in such a way that they seem to have originated at an upright virtual image one focal length from the lens, on the same side of the lens that the parallel rays are approaching on.

Rays from an object at finite distance are associated with a virtual image that is closer to the lens than the focal length, and on the same side of the lens as the object. The closer the object is to the lens, the closer the virtual image is to the lens.

Likewise, the magnification of a lens is given by $M=-{\frac {S_{2}}{S_{1}}}={\frac {f}{f-S_{1}}}$ where the negative sign is given, by convention, to indicate an upright object for positive values and an inverted object for negative values. Similar to mirrors, upright images produced by single lenses are virtual while inverted images are real.

Lenses suffer from aberrations that distort images and focal points. These are due to both to geometrical imperfections and due to the changing index of refraction for different wavelengths of light (chromatic aberration).

## Underlying mathematics

As a mathematical study, geometrical optics emerges as a short-wavelength limit for solutions to hyperbolic partial differential equations (Sommerfeld–Runge method) or as a property of propagation of field discontinuities according to Maxwell's equations (Luneburg method). In this short-wavelength limit, it is possible to approximate the solution locally by $u(t,x)\approx a(t,x)e^{i(k\cdot x-\omega t)}$ where $k,\omega$ satisfy a dispersion relation, and the amplitude $a(t,x)$ varies slowly. More precisely, the leading order solution takes the form $a_{0}(t,x)e^{i\varphi (t,x)/\varepsilon }.$ The phase $\varphi (t,x)/\varepsilon$ can be linearized to recover large wavenumber $k:=\nabla _{x}\varphi$ , and frequency $\omega :=-\partial _{t}\varphi$ . The amplitude $a_{0}$ satisfies a transport equation. The small parameter $\varepsilon \,$ enters the scene due to highly oscillatory initial conditions. Thus, when initial conditions oscillate much faster than the coefficients of the differential equation, solutions will be highly oscillatory, and transported along rays. Assuming coefficients in the differential equation are smooth, the rays will be too. In other words, refraction does not take place. The motivation for this technique comes from studying the typical scenario of light propagation where short wavelength light travels along rays that minimize (more or less) its travel time. Its full application requires tools from microlocal analysis.

### Sommerfeld–Runge method

The method of obtaining equations of geometrical optics by taking the limit of zero wavelength was first described by Arnold Sommerfeld and J. Runge in 1911. Their derivation was based on an oral remark by Peter Debye. Consider a monochromatic scalar field $\psi (\mathbf {r} ,t)=\phi (\mathbf {r} )e^{i\omega t}$ , where $\psi$ could be any of the components of electric or magnetic field and hence the function $\phi$ satisfy the wave equation $\nabla ^{2}\phi +k_{o}^{2}n(\mathbf {r} )^{2}\phi =0$ where $k_{o}=\omega /c=2\pi /\lambda _{o}$ with c being the speed of light in vacuum. Here, $n(\mathbf {r} )$ is the refractive index of the medium. Without loss of generality, let us introduce $\phi =A(k_{o},\mathbf {r} )e^{ik_{o}S(\mathbf {r} )}$ to convert the equation to $-k_{o}^{2}A[(\nabla S)^{2}-n^{2}]+2ik_{o}(\nabla S\cdot \nabla A)+ik_{o}A\nabla ^{2}S+\nabla ^{2}A=0.$

Since the underlying principle of geometrical optics lies in the limit $\lambda _{o}\sim k_{o}^{-1}\rightarrow 0$ , the following asymptotic series is assumed, $A(k_{o},\mathbf {r} )=\sum _{m=0}^{\infty }{\frac {A_{m}(\mathbf {r} )}{(ik_{o})^{m}}}$

For large but finite value of $k_{o}$ , the series diverges, and one has to be careful in keeping only appropriate first few terms. For each value of $k_{o}$ , one can find an optimum number of terms to be kept and adding more terms than the optimum number might result in a poorer approximation. Substituting the series into the equation and collecting terms of different orders, one finds ${\begin{aligned}O(k_{o}^{2}):&\quad (\nabla S)^{2}=n^{2},\\[1ex]O(k_{o}):&\quad 2\nabla S\cdot \nabla A_{0}+A_{0}\nabla ^{2}S=0,\\[1ex]O(1):&\quad 2\nabla S\cdot \nabla A_{1}+A_{1}\nabla ^{2}S=-\nabla ^{2}A_{0},\end{aligned}}$ in general, $O(k_{o}^{1-m}):\quad 2\nabla S\cdot \nabla A_{m}+A_{m}\nabla ^{2}S=-\nabla ^{2}A_{m-1}.$

The first equation is known as the **eikonal equation**, which determines the **eikonal** $S(\mathbf {r} )$ is a Hamilton–Jacobi equation, written for example in Cartesian coordinates becomes $\left({\frac {\partial S}{\partial x}}\right)^{2}+\left({\frac {\partial S}{\partial y}}\right)^{2}+\left({\frac {\partial S}{\partial z}}\right)^{2}=n^{2}.$

The remaining equations determine the functions $A_{m}(\mathbf {r} )$ .

### Luneburg method

The method of obtaining equations of geometrical optics by analysing surfaces of discontinuities of solutions to Maxwell's equations was first described by Rudolf Karl Luneburg in 1944. It does not restrict the electromagnetic field to have a special form required by the Sommerfeld-Runge method which assumes the amplitude $A(k_{o},\mathbf {r} )$ and phase $S(\mathbf {r} )$ satisfy the equation ${\textstyle \lim _{k_{0}\to \infty }{\frac {1}{k_{0}}}\left({\frac {1}{A}}\,\nabla S\cdot \nabla A+{\frac {1}{2}}\nabla ^{2}S\right)=0}$ . This condition is satisfied by e.g. plane waves but is not additive.

The main conclusion of Luneburg's approach is the following:

**Theorem.** Suppose the fields $\mathbf {E} (x,y,z,t)$ and $\mathbf {H} (x,y,z,t)$ (in a linear isotropic medium described by dielectric constants $\varepsilon (x,y,z)$ and $\mu (x,y,z)$ ) have finite discontinuities along a (moving) surface in $\mathbf {R} ^{3}$ described by the equation $\psi (x,y,z)-ct=0$ . Then Maxwell's equations in the integral form imply that $\psi$ satisfies the eikonal equation: $\psi _{x}^{2}+\psi _{y}^{2}+\psi _{z}^{2}=\varepsilon \mu =n^{2},$ where $n(x,y,z)$ is the index of refraction of the medium (Gaussian units).

An example of such surface of discontinuity is the initial wave front emanating from a source that starts radiating at a certain instant of time.

The surfaces of field discontinuity thus become geometrical optics wave fronts with the corresponding geometrical optics fields defined as: ${\begin{aligned}\mathbf {E} ^{*}(x,y,z)&=\mathbf {E} (x,y,z,\psi (x,y,z)/c)\\[1ex]\mathbf {H} ^{*}(x,y,z)&=\mathbf {H} (x,y,z,\psi (x,y,z)/c)\end{aligned}}$

Those fields obey transport equations consistent with the transport equations of the Sommerfeld-Runge approach. Light rays in Luneburg's theory are defined as trajectories orthogonal to the discontinuity surfaces and can be shown to obey Fermat's principle of least time thus establishing the identity of those rays with light rays of standard optics.

The above developments can be generalised to anisotropic media.

The proof of Luneburg's theorem is based on investigating how Maxwell's equations govern the propagation of discontinuities of solutions. The basic technical lemma is as follows:

**A technical lemma.** Let $\varphi (x,y,z,t)=0$ be a hypersurface (a 3-dimensional manifold) in spacetime $\mathbf {R} ^{4}$ on which one or more of: $\mathbf {E} (x,y,z,t)$ , $\mathbf {H} (x,y,z,t)$ , $\varepsilon (x,y,z)$ , $\mu (x,y,z)$ , have a finite discontinuity. Then at each point of the hypersurface the following formulas hold: ${\begin{aligned}\nabla \varphi \cdot [\varepsilon \mathbf {E} ]&=0\\[1ex]\nabla \varphi \cdot [\mu \mathbf {H} ]&=0\\[1ex]\nabla \varphi \times [\mathbf {E} ]+{\frac {1}{c}}\,\varphi _{t}\,[\mu \mathbf {H} ]&=0\\[1ex]\nabla \varphi \times [\mathbf {H} ]-{\frac {1}{c}}\,\varphi _{t}\,[\varepsilon \mathbf {E} ]&=0\end{aligned}}$ where the $\nabla$ operator acts in the $xyz$ -space (for every fixed t ) and the square brackets denote the difference in values on both sides of the discontinuity surface (set up according to an arbitrary but fixed convention, e.g. the gradient $\nabla \varphi$ pointing in the direction of the quantities being subtracted *from*).

**Sketch of proof.** Start with Maxwell's equations away from the sources (Gaussian units): ${\begin{aligned}\nabla \cdot \varepsilon \mathbf {E} =0\\[1ex]\nabla \cdot \mu \mathbf {H} =0\\[1ex]\nabla \times \mathbf {E} +{\tfrac {\mu }{c}}\,\mathbf {H} _{t}=0\\[1ex]\nabla \times \mathbf {H} -{\tfrac {\varepsilon }{c}}\,\mathbf {E} _{t}=0\end{aligned}}$

Using Stokes' theorem in $\mathbf {R} ^{4}$ one can conclude from the first of the above equations that for any domain D in $\mathbf {R} ^{4}$ with a piecewise smooth (3-dimensional) boundary $\Gamma$ the following is true: $\oint _{\Gamma }(\mathbf {M} \cdot \varepsilon \mathbf {E} )\,dS=0$ where $\mathbf {M} =(x_{N},y_{N},z_{N})$ is the projection of the outward unit normal $(x_{N},y_{N},z_{N},t_{N})$ of $\Gamma$ onto the 3D slice $t={\rm {const}}$ , and $dS$ is the volume 3-form on $\Gamma$ . Similarly, one establishes the following from the remaining Maxwell's equations: ${\begin{aligned}\oint _{\Gamma }\left(\mathbf {M} \cdot \mu \mathbf {H} \right)dS&=0\\[1.55ex]\oint _{\Gamma }\left(\mathbf {M} \times \mathbf {E} +{\frac {\mu }{c}}\,t_{N}\,\mathbf {H} \right)dS&=0\\[1.55ex]\oint _{\Gamma }\left(\mathbf {M} \times \mathbf {H} -{\frac {\varepsilon }{c}}\,t_{N}\,\mathbf {E} \right)dS&=0\end{aligned}}$

Now by considering arbitrary small sub-surfaces $\Gamma _{0}$ of $\Gamma$ and setting up small neighbourhoods surrounding $\Gamma _{0}$ in $\mathbf {R} ^{4}$ , and subtracting the above integrals accordingly, one obtains: ${\begin{aligned}\int _{\Gamma _{0}}(\nabla \varphi \cdot [\varepsilon \mathbf {E} ])\,{dS \over \|\nabla ^{4D}\varphi \|}&=0\\[1ex]\int _{\Gamma _{0}}(\nabla \varphi \cdot [\mu \mathbf {H} ])\,{dS \over \|\nabla ^{4D}\varphi \|}&=0\\[1ex]\int _{\Gamma _{0}}\left(\nabla \varphi \times [\mathbf {E} ]+{1 \over c}\,\varphi _{t}\,[\mu \mathbf {H} ]\right)\,{\frac {dS}{\|\nabla ^{4D}\varphi \|}}&=0\\[1ex]\int _{\Gamma _{0}}\left(\nabla \varphi \times [\mathbf {H} ]-{1 \over c}\,\varphi _{t}\,[\varepsilon \mathbf {E} ]\right)\,{\frac {dS}{\|\nabla ^{4D}\varphi \|}}&=0\end{aligned}}$ where $\nabla ^{4D}$ denotes the gradient in the 4D $xyzt$ -space. And since $\Gamma _{0}$ is arbitrary, the integrands must be equal to 0 which proves the lemma.

It's now easy to show that as they propagate through a continuous medium, the discontinuity surfaces obey the eikonal equation. Specifically, if $\varepsilon$ and $\mu$ are continuous, then the discontinuities of $\mathbf {E}$ and $\mathbf {H}$ satisfy: $[\varepsilon \mathbf {E} ]=\varepsilon [\mathbf {E} ]$ and $[\mu \mathbf {H} ]=\mu [\mathbf {H} ]$ . In this case the last two equations of the lemma can be written as:

${\begin{aligned}\nabla \varphi \times [\mathbf {E} ]+{\mu \over c}\,\varphi _{t}\,[\mathbf {H} ]&=0\\[1ex]\nabla \varphi \times [\mathbf {H} ]-{\varepsilon \over c}\,\varphi _{t}\,[\mathbf {E} ]&=0\end{aligned}}$

Taking the cross product of the second equation with $\nabla \varphi$ and substituting the first yields: $\nabla \varphi \times (\nabla \varphi \times [\mathbf {H} ])-{\varepsilon \over c}\,\varphi _{t}\,(\nabla \varphi \times [\mathbf {E} ])=(\nabla \varphi \cdot [\mathbf {H} ])\,\nabla \varphi -\|\nabla \varphi \|^{2}\,[\mathbf {H} ]+{\varepsilon \mu \over c^{2}}\varphi _{t}^{2}\,[\mathbf {H} ]=0$

The continuity of $\mu$ and the second equation of the lemma imply: $\nabla \varphi \cdot [\mathbf {H} ]=0$ , hence, for points lying on the surface $\varphi =0$ *only*: $\|\nabla \varphi \|^{2}={\varepsilon \mu \over c^{2}}\varphi _{t}^{2}$

(Notice the presence of the discontinuity is essential in this step as we'd be dividing by zero otherwise.)

Because of the physical considerations one can assume without loss of generality that $\varphi$ is of the following form: $\varphi (x,y,z,t)=\psi (x,y,z)-ct$ , i.e. a 2D surface moving through space, modelled as level surfaces of $\psi$ . (Mathematically $\psi$ exists if $\varphi _{t}\neq 0$ by the implicit function theorem.) The above equation written in terms of $\psi$ becomes: $\|\nabla \psi \|^{2}={\varepsilon \mu \over c^{2}}\,(-c)^{2}=\varepsilon \mu =n^{2}$ i.e., $\psi _{x}^{2}+\psi _{y}^{2}+\psi _{z}^{2}=n^{2}$ which is the eikonal equation and it holds for all x , y , z , since the variable t is absent. Other laws of optics like Snell's law and Fresnel formulae can be similarly obtained by considering discontinuities in $\varepsilon$ and $\mu$ .

### General equation using four-vector notation

In four-vector notation used in special relativity, the wave equation can be written as ${\frac {\partial ^{2}\psi }{\partial x_{i}\partial x^{i}}}=0$

and the substitution $\psi =Ae^{iS/\varepsilon }$ leads to $-{\frac {A}{\varepsilon ^{2}}}{\frac {\partial S}{\partial x_{i}}}{\frac {\partial S}{\partial x^{i}}}+{\frac {2i}{\varepsilon }}{\frac {\partial A}{\partial x_{i}}}{\frac {\partial S}{\partial x^{i}}}+{\frac {iA}{\varepsilon }}{\frac {\partial ^{2}S}{\partial x_{i}\partial x^{i}}}+{\frac {\partial ^{2}A}{\partial x_{i}\partial x^{i}}}=0.$

Therefore, the eikonal equation is given by ${\frac {\partial S}{\partial x_{i}}}{\frac {\partial S}{\partial x^{i}}}=0.$

Once eikonal is found by solving the above equation, the wave four-vector can be found from $k_{i}=-{\frac {\partial S}{\partial x^{i}}}.$
