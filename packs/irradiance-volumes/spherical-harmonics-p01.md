---
title: "Spherical harmonics (part 1/2)"
source: https://en.wikipedia.org/wiki/Spherical_harmonics
domain: irradiance-volumes
license: CC-BY-SA-4.0
tags: irradiance volume, volumetric light grid, diffuse global illumination cache, light field probe
fetched: 2026-07-02
part: 1/2
---

# Spherical harmonics

In mathematics and physical science, **spherical harmonics** are special functions defined on the surface of a sphere. They are often employed in solving partial differential equations in many scientific fields. The table of spherical harmonics contains a list of common spherical harmonics.

Since the spherical harmonics form a complete set of orthogonal functions and thus an orthonormal basis, certain functions defined on the surface of a sphere can be written as a sum of these spherical harmonics. This is similar to periodic functions defined on a circle that can be expressed as a sum of circular functions (sines and cosines) via Fourier series. Like the sines and cosines in Fourier series, the spherical harmonics may be organized by (spatial) angular frequency, as seen in the rows of functions in the illustration on the right. Further, spherical harmonics are basis functions for irreducible representations of SO(3), the group of rotations in three dimensions, and thus play a central role in the group theoretic discussion of SO(3).

Spherical harmonics originate from solving Laplace's equation in the spherical domains. Functions that are solutions to Laplace's equation are called harmonics. Despite their name, spherical harmonics take their simplest form in Cartesian coordinates, where they can be defined as homogeneous polynomials of degree $\ell$ in $(x,y,z)$ that obey Laplace's equation. The connection with spherical coordinates arises immediately if one uses the homogeneity to extract a factor of radial dependence $r^{\ell }$ from the above-mentioned polynomial of degree $\ell$ ; the remaining factor can be regarded as a function of the spherical angular coordinates $\theta$ and $\varphi$ only, or equivalently of the orientational unit vector $\mathbf {r}$ specified by these angles. In this setting, they may be viewed as the angular portion of a set of solutions to Laplace's equation in three dimensions, and this viewpoint is often taken as an alternative definition. Notice, however, that spherical harmonics are *not* functions on the sphere which are harmonic with respect to the Laplace-Beltrami operator for the standard round metric on the sphere: the only harmonic functions in this sense on the sphere are the constants, since harmonic functions satisfy the Maximum principle. Spherical harmonics, as functions on the sphere, are eigenfunctions of the Laplace-Beltrami operator (see Higher dimensions).

A specific set of spherical harmonics, denoted $Y_{\ell }^{m}(\theta ,\varphi )$ or $Y_{\ell }^{m}({\mathbf {r} })$ , are known as Laplace's spherical harmonics, as they were first introduced by Pierre Simon de Laplace in 1782. These functions form an orthogonal system, and are thus basic to the expansion of a general function on the sphere as alluded to above.

Spherical harmonics are important in many theoretical and practical applications, including the representation of multipole electrostatic and electromagnetic fields, electron configurations, gravitational fields, geoids, the magnetic fields of planetary bodies and stars, and the cosmic microwave background radiation. In 3D computer graphics, spherical harmonics play a role in a wide variety of topics including indirect lighting (ambient occlusion, global illumination, precomputed radiance transfer, etc.) and modelling of 3D shapes.


## History

Spherical harmonics were first investigated in connection with the Newtonian potential of Newton's law of universal gravitation in three dimensions. In 1782, Pierre-Simon de Laplace had, in his *Mécanique Céleste*, determined that the gravitational potential $\mathbb {R} ^{3}\to \mathbb {R}$ at a point **x** associated with a set of point masses *m**i* located at points **x***i* was given by

$V(\mathbf {x} )=\sum _{i}{\frac {m_{i}}{|\mathbf {x} _{i}-\mathbf {x} |}}.$

Each term in the above summation is an individual Newtonian potential for a point mass. Just prior to that time, Adrien-Marie Legendre had investigated the expansion of the Newtonian potential in powers of *r* = |**x**| and *r*1 = |**x**1|. He discovered that if *r* ≤ *r*1 then

${\frac {1}{|\mathbf {x} _{1}-\mathbf {x} |}}=P_{0}(\cos \gamma ){\frac {1}{r_{1}}}+P_{1}(\cos \gamma ){\frac {r}{r_{1}^{2}}}+P_{2}(\cos \gamma ){\frac {r^{2}}{r_{1}^{3}}}+\cdots$

where *γ* is the angle between the vectors **x** and **x**1. The functions $P_{i}:[-1,1]\to \mathbb {R}$ are the Legendre polynomials, and they can be derived as a special case of spherical harmonics. Subsequently, in his 1782 memoir, Laplace investigated these coefficients using spherical coordinates to represent the angle *γ* between **x**1 and **x**. (See Legendre polynomials § Applications for more detail.)

In 1867, William Thomson (Lord Kelvin) and Peter Guthrie Tait introduced the solid spherical harmonics in their *Treatise on Natural Philosophy*, and also first introduced the name of "spherical harmonics" for these functions. The solid harmonics were homogeneous polynomial solutions $\mathbb {R} ^{3}\to \mathbb {R}$ of Laplace's equation ${\frac {\partial ^{2}u}{\partial x^{2}}}+{\frac {\partial ^{2}u}{\partial y^{2}}}+{\frac {\partial ^{2}u}{\partial z^{2}}}=0.$ By examining Laplace's equation in spherical coordinates, Thomson and Tait recovered Laplace's spherical harmonics. (See Harmonic polynomial representation.) The term "Laplace's coefficients" was employed by William Whewell to describe the particular system of solutions introduced along these lines, whereas others reserved this designation for the zonal spherical harmonics that had properly been introduced by Laplace and Legendre.

The 19th century development of Fourier series made possible the solution of a wide variety of physical problems in rectangular domains, such as the solution of the heat equation and wave equation. This could be achieved by expansion of functions in series of trigonometric functions. Whereas the trigonometric functions in a Fourier series represent the fundamental modes of vibration in a string, the spherical harmonics represent the fundamental modes of vibration of a sphere in much the same way. Many aspects of the theory of Fourier series could be generalized by taking expansions in spherical harmonics rather than trigonometric functions. Moreover, analogous to how trigonometric functions can equivalently be written as complex exponentials, spherical harmonics also possessed an equivalent form as complex-valued functions. This was a boon for problems possessing spherical symmetry, such as those of celestial mechanics originally studied by Laplace and Legendre.

The prevalence of spherical harmonics already in physics set the stage for their later importance in the 20th century birth of quantum mechanics. The (complex-valued) spherical harmonics $S^{2}\to \mathbb {C}$ are eigenfunctions of the square of the orbital angular momentum operator $-i\hbar \mathbf {r} \times \nabla ,$ and therefore they represent the different quantized configurations of atomic orbitals.


## Laplace's spherical harmonics

Laplace's equation imposes that the Laplacian of a scalar field *f* is zero. (Here the scalar field is understood to be complex, i.e. to correspond to a (smooth) function $f:\mathbb {R} ^{3}\to \mathbb {C}$ .) In spherical coordinates this is:

$\nabla ^{2}f={\frac {1}{r^{2}}}{\frac {\partial }{\partial r}}\left(r^{2}{\frac {\partial f}{\partial r}}\right)+{\frac {1}{r^{2}\sin \theta }}{\frac {\partial }{\partial \theta }}\left(\sin \theta {\frac {\partial f}{\partial \theta }}\right)+{\frac {1}{r^{2}\sin ^{2}\theta }}{\frac {\partial ^{2}f}{\partial \varphi ^{2}}}=0.$

Consider the problem of finding solutions of the form *f*(*r*, *θ*, *φ*) = *R*(*r*) *Y*(*θ*, *φ*). By separation of variables, two differential equations result by imposing Laplace's equation: ${\frac {1}{R}}{\frac {d}{dr}}\left(r^{2}{\frac {dR}{dr}}\right)=\lambda ,\qquad {\frac {1}{Y}}{\frac {1}{\sin \theta }}{\frac {\partial }{\partial \theta }}\left(\sin \theta {\frac {\partial Y}{\partial \theta }}\right)+{\frac {1}{Y}}{\frac {1}{\sin ^{2}\theta }}{\frac {\partial ^{2}Y}{\partial \varphi ^{2}}}=-\lambda .$ The second equation can be simplified under the assumption that *Y* has the form *Y*(*θ*, *φ*) = Θ(*θ*) Φ(*φ*). Applying separation of variables again to the second equation gives way to the pair of differential equations

${\frac {1}{\Phi }}{\frac {d^{2}\Phi }{d\varphi ^{2}}}=-m^{2}$ $\lambda \sin ^{2}\theta +{\frac {\sin \theta }{\Theta }}{\frac {d}{d\theta }}\left(\sin \theta {\frac {d\Theta }{d\theta }}\right)=m^{2}$

for some number *m*. A priori, *m* is a complex constant, but because Φ must be a periodic function whose period evenly divides 2*π*, *m* is necessarily an integer and Φ is a linear combination of the complex exponentials *e*± *imφ*. The solution function *Y*(*θ*, *φ*) is regular at the poles of the sphere, where *θ* = 0, *π*. Imposing this regularity in the solution Θ of the second equation at the boundary points of the domain is a Sturm–Liouville problem that forces the parameter *λ* to be of the form *λ* = *ℓ* (*ℓ* + 1) for some non-negative integer with *ℓ* ≥ |*m*|; this is also explained below in terms of the orbital angular momentum. Furthermore, a change of variables *t* = cos *θ* transforms this equation into the Legendre equation, whose solution is a multiple of the associated Legendre polynomial *Pm ℓ*(cos *θ*) . Finally, the equation for *R* has solutions of the form *R*(*r*) = *A rℓ* + *B r*−*ℓ* − 1; requiring the solution to be regular throughout **R**3 forces *B* = 0.

Here the solution was assumed to have the special form *Y*(*θ*, *φ*) = Θ(*θ*) Φ(*φ*). For a given value of *ℓ*, there are 2*ℓ* + 1 independent solutions of this form, one for each integer *m* with −*ℓ* ≤ *m* ≤ *ℓ*. These angular solutions $Y_{\ell }^{m}:S^{2}\to \mathbb {C}$ are a product of trigonometric functions, here represented as a complex exponential, and associated Legendre polynomials:

$Y_{\ell }^{m}(\theta ,\varphi )=Ne^{im\varphi }P_{\ell }^{m}(\cos {\theta })$

which fulfill $r^{2}\nabla ^{2}Y_{\ell }^{m}(\theta ,\varphi )=-\ell (\ell +1)Y_{\ell }^{m}(\theta ,\varphi ).$

Here $Y_{\ell }^{m}:S^{2}\to \mathbb {C}$ is called a **spherical harmonic function of degree *ℓ* and order *m***, $P_{\ell }^{m}:[-1,1]\to \mathbb {R}$ is an associated Legendre polynomial, *N* is a normalization constant, and *θ* and *φ* represent colatitude and longitude, respectively. In particular, the colatitude *θ*, or polar angle, ranges from *0* at the North Pole, to *π*/2 at the Equator, to *π* at the South Pole, and the longitude *φ*, or azimuth, may assume all values with 0 ≤ *φ* < 2*π*. For a fixed integer *ℓ*, every solution *Y*(*θ*, *φ*), $Y:S^{2}\to \mathbb {C}$ , of the eigenvalue problem $r^{2}\nabla ^{2}Y=-\ell (\ell +1)Y$ is a linear combination of $Y_{\ell }^{m}:S^{2}\to \mathbb {C}$ . In fact, for any such solution, *rℓ Y*(*θ*, *φ*) is the expression in spherical coordinates of a homogeneous polynomial $\mathbb {R} ^{3}\to \mathbb {C}$ that is harmonic (see below), and so counting dimensions shows that there are 2*ℓ* + 1 linearly independent such polynomials.

The general solution $f:\mathbb {R} ^{3}\to \mathbb {C}$ to Laplace's equation $\Delta f=0$ in a ball centered at the origin is a linear combination of the spherical harmonic functions multiplied by the appropriate scale factor *rℓ*,

$f(r,\theta ,\varphi )=\sum _{\ell =0}^{\infty }\sum _{m=-\ell }^{\ell }f_{\ell }^{m}r^{\ell }Y_{\ell }^{m}(\theta ,\varphi ),$

where the $f_{\ell }^{m}\in \mathbb {C}$ are constants and the factors *rℓ Yℓm* are known as (*regular*) solid harmonics $\mathbb {R} ^{3}\to \mathbb {C}$ . Such an expansion is valid in the ball

$r<R={\frac {1}{\limsup _{\ell \to \infty }|f_{\ell }^{m}|^{{1}/{\ell }}}}.$

For $r>R$ , the solid harmonics with negative powers of r (the *irregular* solid harmonics $\mathbb {R} ^{3}\setminus \{\mathbf {0} \}\to \mathbb {C}$ ) are chosen instead. In that case, one needs to expand the solution of known regions in Laurent series (about $r=\infty$ ), instead of the Taylor series (about $r=0$ ) used above, to match the terms and find series expansion coefficients $f_{\ell }^{m}\in \mathbb {C}$ .

### Orbital angular momentum

In quantum mechanics, Laplace's spherical harmonics are understood in terms of the orbital angular momentum $\mathbf {L} =-i\hbar (\mathbf {x} \times \mathbf {\nabla } )=L_{x}\mathbf {i} +L_{y}\mathbf {j} +L_{z}\mathbf {k} .$ The *ħ* is conventional in quantum mechanics; it is convenient to work in units in which *ħ* = 1. The spherical harmonics are eigenfunctions of the square of the orbital angular momentum ${\begin{aligned}\mathbf {L} ^{2}&=-r^{2}\nabla ^{2}+\left(r{\frac {\partial }{\partial r}}+1\right)r{\frac {\partial }{\partial r}}\\&=-{\frac {1}{\sin \theta }}{\frac {\partial }{\partial \theta }}\sin \theta {\frac {\partial }{\partial \theta }}-{\frac {1}{\sin ^{2}\theta }}{\frac {\partial ^{2}}{\partial \varphi ^{2}}}.\end{aligned}}$ Laplace's spherical harmonics are the joint eigenfunctions of the square of the orbital angular momentum and the generator of rotations about the azimuthal axis: ${\begin{aligned}L_{z}&=-i\left(x{\frac {\partial }{\partial y}}-y{\frac {\partial }{\partial x}}\right)\\&=-i{\frac {\partial }{\partial \varphi }}.\end{aligned}}$

These operators commute, and are densely defined self-adjoint operators on the weighted Hilbert space of functions *f* square-integrable with respect to the normal distribution as the weight function on **R**3: ${\frac {1}{(2\pi )^{3/2}}}\int _{\mathbb {R} ^{3}}|f(x)|^{2}e^{-|x|^{2}/2}\,dx<\infty .$ Furthermore, **L**2 is a positive operator.

If *Y* is a joint eigenfunction of **L**2 and *L**z*, then by definition ${\begin{aligned}\mathbf {L} ^{2}Y&=\lambda Y\\L_{z}Y&=mY\end{aligned}}$ for some real numbers *m* and *λ*. Here *m* must in fact be an integer, for *Y* must be periodic in the coordinate *φ* with period a number that evenly divides 2*π*. Furthermore, since $\mathbf {L} ^{2}=L_{x}^{2}+L_{y}^{2}+L_{z}^{2}$ and each of *L**x*, *L**y*, *L**z* are self-adjoint, it follows that *λ* ≥ *m*2.

Denote this joint eigenspace by *E**λ*,*m*, and define the raising and lowering operators by ${\begin{aligned}L_{+}&=L_{x}+iL_{y}\\L_{-}&=L_{x}-iL_{y}\end{aligned}}$ Then *L*+ and *L*− commute with **L**2, and the Lie algebra generated by *L*+, *L*−, *L**z* is the special linear Lie algebra of order 2, ${\mathfrak {sl}}_{2}(\mathbb {C} )$ , with commutation relations $[L_{z},L_{+}]=L_{+},\quad [L_{z},L_{-}]=-L_{-},\quad [L_{+},L_{-}]=2L_{z}.$ Thus *L*+ : *E**λ*,*m* → *E**λ*,*m*+1 (it is a "raising operator") and *L*− : *E**λ*,*m* → *E**λ*,*m*−1 (it is a "lowering operator"). In particular, *L**k* + : *E**λ*,*m* → *E**λ*,*m*+*k* must be zero for *k* sufficiently large, because the inequality *λ* ≥ *m*2 must hold in each of the nontrivial joint eigenspaces. Let *Y* ∈ *E**λ*,*m* be a nonzero joint eigenfunction, and let k be the least integer such that $L_{+}^{k}Y=0.$ Then, since $L_{-}L_{+}=\mathbf {L} ^{2}-L_{z}^{2}-L_{z}$ it follows that $0=L_{-}L_{+}^{k}Y=(\lambda -(m+k)^{2}-(m+k))Y.$ Thus *λ* = *ℓ*(*ℓ* + 1) for the positive integer *ℓ* = *m* + *k*.

The foregoing has been all worked out in the spherical coordinate representation, $\langle \theta ,\varphi |lm\rangle =Y_{l}^{m}(\theta ,\varphi )$ but may be expressed more abstractly in the complete, orthonormal spherical ket basis.


## Harmonic polynomial representation

The spherical harmonics can be expressed as the restriction to the unit sphere of certain polynomial functions $\mathbb {R} ^{3}\to \mathbb {C}$ . Specifically, we say that a (complex-valued) polynomial function $p:\mathbb {R} ^{3}\to \mathbb {C}$ is *homogeneous* of degree $\ell$ if $p(\lambda \mathbf {x} )=\lambda ^{\ell }p(\mathbf {x} )$ for all real numbers $\lambda \in \mathbb {R}$ and all $\mathbf {x} \in \mathbb {R} ^{3}$ . We say that p is *harmonic* if $\Delta p=0,$ where $\Delta$ is the Laplacian. Then for each $\ell$ , we define $\mathbf {A} _{\ell }=\left\{{\text{harmonic polynomials }}\mathbb {R} ^{3}\to \mathbb {C} {\text{ that are homogeneous of degree }}\ell \right\}.$

For example, when $\ell =1$ , $\mathbf {A} _{1}$ is just the 3-dimensional space of all linear functions $\mathbb {R} ^{3}\to \mathbb {C}$ , since any such function is automatically harmonic. Meanwhile, when $\ell =2$ , we have a 5-dimensional space: $\mathbf {A} _{2}=\operatorname {span} _{\mathbb {C} }(x_{1}x_{2},\,x_{1}x_{3},\,x_{2}x_{3},\,x_{1}^{2}-x_{2}^{2},\,2x_{3}^{2}-x_{1}^{2}-x_{2}^{2}).$

For any $\ell$ , the space $\mathbf {H} _{\ell }$ of spherical harmonics of degree $\ell$ is just the space of restrictions to the sphere $S^{2}$ of the elements of $\mathbf {A} _{\ell }$ . As suggested in the introduction, this perspective is presumably the origin of the term "spherical harmonic" (i.e., the restriction to the sphere of a harmonic function).

For example, for any $c\in \mathbb {C}$ the formula $p(x_{1},x_{2},x_{3})=c(x_{1}+ix_{2})^{\ell }$ defines a homogeneous polynomial of degree $\ell$ with domain and codomain $\mathbb {R} ^{3}\to \mathbb {C}$ , which happens to be independent of $x_{3}$ . This polynomial is easily seen to be harmonic. If we write p in spherical coordinates $(r,\theta ,\varphi )$ and then restrict to $r=1$ , we obtain $p(\theta ,\varphi )=c\sin(\theta )^{\ell }(\cos(\varphi )+i\sin(\varphi ))^{\ell },$ which can be rewritten as $p(\theta ,\varphi )=c\left({\sqrt {1-\cos ^{2}(\theta )}}\right)^{\ell }e^{i\ell \varphi }.$ After using the formula for the associated Legendre polynomial $P_{\ell }^{\ell }$ , we may recognize this as the formula for the spherical harmonic $Y_{\ell }^{\ell }(\theta ,\varphi ).$ (See Special cases.)


## Conventions

### Condon–Shortley phase

One source of confusion with the definition of the spherical harmonic functions concerns a phase factor of $(-1)^{m}$ , commonly referred to as the Condon–Shortley phase in the quantum mechanical literature. This phase factor may be included either in the definition of the associated Legendre polynomials or in the definition of the spherical harmonic functions, but it should not be counted twice.

In this section, unless otherwise stated, $P_{\ell }^{m}$ denotes the associated Legendre function with the Condon–Shortley phase included, so that for $m>0$ $P_{\ell }^{m}(x)=(-1)^{m}(1-x^{2})^{m/2}{\frac {d^{m}}{dx^{m}}}P_{\ell }(x),$ and $P_{\ell }^{-m}=(-1)^{m}{\frac {(\ell -m)!}{(\ell +m)!}}P_{\ell }^{m}.$ This is the convention used, for example, by the NIST Digital Library of Mathematical Functions and in many mathematical references.

Some authors instead define associated Legendre functions without this phase factor. If these are denoted here by ${\widetilde {P}}_{\ell }^{m}$ , then ${\widetilde {P}}_{\ell }^{m}(x)=(1-x^{2})^{m/2}{\frac {d^{m}}{dx^{m}}}P_{\ell }(x),\qquad P_{\ell }^{m}(x)=(-1)^{m}{\widetilde {P}}_{\ell }^{m}(x).$ With this notation, a formula with an external factor $(-1)^{m}$ multiplying ${\widetilde {P}}_{\ell }^{m}$ gives the same spherical harmonic as a formula using $P_{\ell }^{m}$ without an external phase factor.

There is no requirement to use the Condon–Shortley phase in the definition of the spherical harmonic functions, but including it can simplify some quantum mechanical operations, especially the application of raising and lowering operators. The geodesy and magnetics communities commonly use conventions in which the Condon–Shortley phase factor is not included in the associated Legendre functions or in the spherical harmonics.

### Orthogonality and normalization

Several different normalizations are in common use for the Laplace spherical harmonic functions $S^{2}\to \mathbb {C}$ . These normalization choices are independent of the placement of the Condon–Shortley phase.

With the Condon–Shortley phase included in $P_{\ell }^{m}$ , the orthonormal complex spherical harmonics are $Y_{\ell }^{m}(\theta ,\varphi )={\sqrt {{\frac {(2\ell +1)}{4\pi }}{\frac {(\ell -m)!}{(\ell +m)!}}}}\,P_{\ell }^{m}(\cos {\theta })\,e^{im\varphi }.$ This is the convention used in this article, and is common in acoustics.

The same orthonormal functions are often written in quantum mechanics as $Y_{\ell }^{m}(\theta ,\varphi )=(-1)^{m}{\sqrt {{\frac {(2\ell +1)}{4\pi }}{\frac {(\ell -m)!}{(\ell +m)!}}}}\,{\widetilde {P}}_{\ell }^{m}(\cos {\theta })\,e^{im\varphi },$ where ${\widetilde {P}}_{\ell }^{m}$ denotes the associated Legendre function without the Condon–Shortley phase. This avoids counting the phase twice.

With either placement of the Condon–Shortley phase, the orthonormal spherical harmonics satisfy $\int _{\theta =0}^{\pi }\int _{\varphi =0}^{2\pi }Y_{\ell }^{m}\,Y_{\ell '}^{m'}{}^{*}\,d\Omega =\delta _{\ell \ell '}\,\delta _{mm'},$ where *δ**ij* is the Kronecker delta and *d*Ω = sin(*θ*) *dφ* *dθ*. This normalization is used in quantum mechanics because it ensures that probability is normalized, i.e., $\int {|Y_{\ell }^{m}|^{2}d\Omega }=1.$

The disciplines of geodesy and spectral analysis often use the corresponding $4\pi$ -normalized harmonics. Written with the same phase convention as above, these are $Y_{\ell }^{m}(\theta ,\varphi )={\sqrt {{(2\ell +1)}{\frac {(\ell -m)!}{(\ell +m)!}}}}\,P_{\ell }^{m}(\cos {\theta })\,e^{im\varphi },$ which possess unit power ${\frac {1}{4\pi }}\int _{\theta =0}^{\pi }\int _{\varphi =0}^{2\pi }Y_{\ell }^{m}\,Y_{\ell '}^{m'}{}^{*}d\Omega =\delta _{\ell \ell '}\,\delta _{mm'}.$ In geodetic applications this normalization is commonly combined with omission of the Condon–Shortley phase.

The magnetics community, in contrast, often uses Schmidt semi-normalized harmonics. Written with the same phase convention as above, these are $Y_{\ell }^{m}(\theta ,\varphi )={\sqrt {\frac {(\ell -m)!}{(\ell +m)!}}}\,P_{\ell }^{m}(\cos {\theta })\,e^{im\varphi },$ which have the normalization $\int _{\theta =0}^{\pi }\int _{\varphi =0}^{2\pi }Y_{\ell }^{m}\,Y_{\ell '}^{m'}{}^{*}d\Omega ={\frac {4\pi }{(2\ell +1)}}\delta _{\ell \ell '}\,\delta _{mm'}.$ In quantum mechanics this normalization is sometimes used as well, and is named Racah's normalization after Giulio Racah.

For the phase convention used in this article, the complex spherical harmonics satisfy $Y_{\ell }^{m}{}^{*}(\theta ,\varphi )=(-1)^{m}Y_{\ell }^{-m}(\theta ,\varphi ),$ where the superscript * denotes complex conjugation. Equivalently, since $(-1)^{m}=(-1)^{-m}$ for integer m , this may also be written with $(-1)^{-m}$ . This equation also follows from the relation of the spherical harmonic functions with the Wigner D-matrix.

### Real form

Assuming the complex spherical harmonics are normalized and phased so that $Y_{\ell }^{m}{}^{*}=(-1)^{m}Y_{\ell }^{-m},$ a real basis of spherical harmonics $Y_{\ell m}:S^{2}\to \mathbb {R}$ can be defined in terms of their complex analogues $Y_{\ell }^{m}:S^{2}\to \mathbb {C}$ by setting ${\begin{aligned}Y_{\ell m}&={\begin{cases}{\dfrac {i}{\sqrt {2}}}\left(Y_{\ell }^{m}-(-1)^{m}\,Y_{\ell }^{-m}\right)&{\text{if}}\ m<0\\Y_{\ell }^{0}&{\text{if}}\ m=0\\{\dfrac {1}{\sqrt {2}}}\left(Y_{\ell }^{-m}+(-1)^{m}\,Y_{\ell }^{m}\right)&{\text{if}}\ m>0.\end{cases}}\\&={\begin{cases}{\dfrac {i}{\sqrt {2}}}\left(Y_{\ell }^{-|m|}-(-1)^{m}\,Y_{\ell }^{|m|}\right)&{\text{if}}\ m<0\\Y_{\ell }^{0}&{\text{if}}\ m=0\\{\dfrac {1}{\sqrt {2}}}\left(Y_{\ell }^{-|m|}+(-1)^{m}\,Y_{\ell }^{|m|}\right)&{\text{if}}\ m>0.\end{cases}}\\&={\begin{cases}{\sqrt {2}}\,(-1)^{m}\,\Im [{Y_{\ell }^{|m|}}]&{\text{if}}\ m<0\\Y_{\ell }^{0}&{\text{if}}\ m=0\\{\sqrt {2}}\,(-1)^{m}\,\Re [{Y_{\ell }^{m}}]&{\text{if}}\ m>0.\end{cases}}\end{aligned}}$ The Condon–Shortley phase convention is used here for consistency. The corresponding inverse equations defining the complex spherical harmonics $Y_{\ell }^{m}:S^{2}\to \mathbb {C}$ in terms of the real spherical harmonics $Y_{\ell m}:S^{2}\to \mathbb {R}$ are $Y_{\ell }^{m}={\begin{cases}{\dfrac {1}{\sqrt {2}}}\left(Y_{\ell |m|}-iY_{\ell ,-|m|}\right)&{\text{if}}\ m<0\\[4pt]Y_{\ell 0}&{\text{if}}\ m=0\\[4pt]{\dfrac {(-1)^{m}}{\sqrt {2}}}\left(Y_{\ell |m|}+iY_{\ell ,-|m|}\right)&{\text{if}}\ m>0.\end{cases}}$

The real spherical harmonics $Y_{\ell m}:S^{2}\to \mathbb {R}$ are sometimes known as *tesseral spherical harmonics*. These functions have the same orthonormality properties as the complex ones $Y_{\ell }^{m}:S^{2}\to \mathbb {C}$ above. The real spherical harmonics $Y_{\ell m}$ with *m* > 0 are said to be of cosine type, and those with *m* < 0 of sine type. The reason for this can be seen by writing the functions in terms of the Legendre polynomials as $Y_{\ell m}={\begin{cases}\left(-1\right)^{m}{\sqrt {2}}{\sqrt {{\dfrac {2\ell +1}{4\pi }}{\dfrac {(\ell -|m|)!}{(\ell +|m|)!}}}}\;P_{\ell }^{|m|}(\cos \theta )\ \sin(|m|\varphi )&{\text{if }}m<0\\[4pt]{\sqrt {\dfrac {2\ell +1}{4\pi }}}\ P_{\ell }^{0}(\cos \theta )&{\text{if }}m=0\\[4pt]\left(-1\right)^{m}{\sqrt {2}}{\sqrt {{\dfrac {2\ell +1}{4\pi }}{\dfrac {(\ell -m)!}{(\ell +m)!}}}}\;P_{\ell }^{m}(\cos \theta )\ \cos(m\varphi )&{\text{if }}m>0\,.\end{cases}}$ Here $P_{\ell }^{m}$ again denotes the associated Legendre function with the Condon–Shortley phase included. With a different placement of that phase, the displayed signs must be changed consistently.

The same sine and cosine factors can be also seen in the following subsection that deals with the Cartesian representation.

See here for a list of real spherical harmonics up to and including $\ell =4$ , which can be seen to be consistent with the output of the equations above.

#### Use in quantum chemistry

From the analytic solutions for the hydrogen atom, the eigenfunctions of the angular part of the wave function are spherical harmonics. However, the solutions of the non-relativistic Schrödinger equation without magnetic terms can be made real. This is why the real forms are extensively used in basis functions for quantum chemistry, as the programs do not then need to use complex algebra. Here, the real functions span the same space as the complex ones would.

For example, as can be seen from the table of spherical harmonics, the usual *p* functions ( $\ell =1$ ) are complex and mix axis directions, but the real versions are essentially just *x*, *y*, and *z*.


## Spherical harmonics in Cartesian form

The complex spherical harmonics $Y_{\ell }^{m}$ give rise to the solid harmonics by extending from $S^{2}$ to all of $\mathbb {R} ^{3}$ as a homogeneous function of degree $\ell$ , i.e. setting $R_{\ell }^{m}(v):=\|v\|^{\ell }Y_{\ell }^{m}\left({\frac {v}{\|v\|}}\right)$ It turns out that $R_{\ell }^{m}$ is basis of the space of harmonic and homogeneous polynomials of degree $\ell$ . More specifically, it is the (unique up to normalization) Gelfand-Tsetlin-basis of this representation of the rotational group $SO(3)$ and an explicit formula for $R_{\ell }^{m}$ in cartesian coordinates can be derived from that fact.

### The Herglotz generating function

If the quantum mechanical convention is adopted for the $Y_{\ell }^{m}:S^{2}\to \mathbb {C}$ , then $e^{v{\mathbf {a} }\cdot {\mathbf {r} }}=\sum _{\ell =0}^{\infty }\sum _{m=-\ell }^{\ell }{\sqrt {\frac {4\pi }{2\ell +1}}}{\frac {r^{\ell }v^{\ell }{\lambda ^{m}}}{\sqrt {(\ell +m)!(\ell -m)!}}}Y_{\ell }^{m}(\mathbf {r} /r).$ Here, $\mathbf {r}$ is the vector with components $(x,y,z)\in \mathbb {R} ^{3}$ , $r=|\mathbf {r} |$ , and ${\mathbf {a} }={\mathbf {\hat {z}} }-{\frac {\lambda }{2}}\left({\mathbf {\hat {x}} }+i{\mathbf {\hat {y}} }\right)+{\frac {1}{2\lambda }}\left({\mathbf {\hat {x}} }-i{\mathbf {\hat {y}} }\right).$ $\mathbf {a}$ is a vector with complex coordinates:

$\mathbf {a} =[{\frac {1}{2}}({\frac {1}{\lambda }}-\lambda ),-{\frac {i}{2}}({\frac {1}{\lambda }}+\lambda ),1].$

The essential property of $\mathbf {a}$ is that it is null: $\mathbf {a} \cdot \mathbf {a} =0.$

It suffices to take v and $\lambda$ as real parameters. In naming this generating function after Herglotz, we follow Courant & Hilbert 1962, §VII.7, who credit unpublished notes by him for its discovery.

Essentially all the properties of the spherical harmonics can be derived from this generating function. An immediate benefit of this definition is that if the vector $\mathbf {r}$ is replaced by the quantum mechanical spin vector operator $\mathbf {J}$ , such that ${\mathcal {Y}}_{\ell }^{m}({\mathbf {J} })$ is the operator analogue of the solid harmonic $r^{\ell }Y_{\ell }^{m}(\mathbf {r} /r)$ , one obtains a generating function for a standardized set of spherical tensor operators, ${\mathcal {Y}}_{\ell }^{m}({\mathbf {J} })$ :

$e^{v{\mathbf {a} }\cdot {\mathbf {J} }}=\sum _{\ell =0}^{\infty }\sum _{m=-\ell }^{\ell }{\sqrt {\frac {4\pi }{2\ell +1}}}{\frac {v^{\ell }{\lambda ^{m}}}{\sqrt {(\ell +m)!(\ell -m)!}}}{\mathcal {Y}}_{\ell }^{m}({\mathbf {J} }).$

The parallelism of the two definitions ensures that the ${\mathcal {Y}}_{\ell }^{m}$ 's transform under rotations (see below) in the same way as the $Y_{\ell }^{m}$ 's, which in turn guarantees that they are spherical tensor operators, $T_{q}^{(k)}$ , with $k={\ell }$ and $q=m$ , obeying all the properties of such operators, such as the Clebsch-Gordan composition theorem, and the Wigner-Eckart theorem. They are, moreover, a standardized set with a fixed scale or normalization.

### Separated Cartesian form

The Herglotzian definition yields polynomials which may, if one wishes, be further factorized into a polynomial of z and another of x and y , as follows (Condon–Shortley phase): $r^{\ell }\,{\begin{pmatrix}Y_{\ell }^{m}\\Y_{\ell }^{-m}\end{pmatrix}}=\left[{\frac {2\ell +1}{4\pi }}\right]^{1/2}{\bar {\Pi }}_{\ell }^{m}(z){\begin{pmatrix}\left(-1\right)^{m}(A_{m}+iB_{m})\\(A_{m}-iB_{m})\end{pmatrix}},\qquad m>0.$ and for *m* = 0: $r^{\ell }\,Y_{\ell }^{0}\equiv {\sqrt {\frac {2\ell +1}{4\pi }}}{\bar {\Pi }}_{\ell }^{0}.$ Here $A_{m}(x,y)=\sum _{p=0}^{m}{\binom {m}{p}}x^{p}y^{m-p}\cos \left((m-p){\frac {\pi }{2}}\right),$ $B_{m}(x,y)=\sum _{p=0}^{m}{\binom {m}{p}}x^{p}y^{m-p}\sin \left((m-p){\frac {\pi }{2}}\right),$ and ${\bar {\Pi }}_{\ell }^{m}(z)=\left[{\frac {(\ell -m)!}{(\ell +m)!}}\right]^{1/2}\sum _{k=0}^{\left\lfloor (\ell -m)/2\right\rfloor }(-1)^{k}2^{-\ell }{\binom {\ell }{k}}{\binom {2\ell -2k}{\ell }}{\frac {(\ell -2k)!}{(\ell -2k-m)!}}\;r^{2k}\;z^{\ell -2k-m}.$ For $m=0$ this reduces to ${\bar {\Pi }}_{\ell }^{0}(z)=\sum _{k=0}^{\left\lfloor \ell /2\right\rfloor }(-1)^{k}2^{-\ell }{\binom {\ell }{k}}{\binom {2\ell -2k}{\ell }}\;r^{2k}\;z^{\ell -2k}.$

The factor ${\bar {\Pi }}_{\ell }^{m}(z)$ is essentially the associated Legendre polynomial $P_{\ell }^{m}(\cos \theta )$ , and the factors $(A_{m}\pm iB_{m})$ are essentially $e^{\pm im\varphi }$ .

#### Examples

Using the expressions for ${\bar {\Pi }}_{\ell }^{m}(z)$ , $A_{m}(x,y)$ , and $B_{m}(x,y)$ listed explicitly above we obtain: $Y_{3}^{1}=-{\frac {1}{r^{3}}}\left[{\tfrac {7}{4\pi }}\cdot {\tfrac {3}{16}}\right]^{1/2}\left(5z^{2}-r^{2}\right)\left(x+iy\right)=-\left[{\tfrac {7}{4\pi }}\cdot {\tfrac {3}{16}}\right]^{1/2}\left(5\cos ^{2}\theta -1\right)\left(\sin \theta e^{i\varphi }\right)$

$Y_{4}^{-2}={\frac {1}{r^{4}}}\left[{\tfrac {9}{4\pi }}\cdot {\tfrac {5}{32}}\right]^{1/2}\left(7z^{2}-r^{2}\right)\left(x-iy\right)^{2}=\left[{\tfrac {9}{4\pi }}\cdot {\tfrac {5}{32}}\right]^{1/2}\left(7\cos ^{2}\theta -1\right)\left(\sin ^{2}\theta e^{-2i\varphi }\right)$ It may be verified that this agrees with the function listed here and here.

#### Real forms

Using the equations above to form the real spherical harmonics, it is seen that for $m>0$ only the $A_{m}$ terms (cosines) are included, and for $m<0$ only the $B_{m}$ terms (sines) are included:

$r^{\ell }\,{\begin{pmatrix}Y_{\ell m}\\Y_{\ell -m}\end{pmatrix}}={\sqrt {\frac {2\ell +1}{2\pi }}}{\bar {\Pi }}_{\ell }^{m}(z){\begin{pmatrix}A_{m}\\B_{m}\end{pmatrix}},\qquad m>0.$ and for *m* = 0: $r^{\ell }\,Y_{\ell 0}\equiv {\sqrt {\frac {2\ell +1}{4\pi }}}{\bar {\Pi }}_{\ell }^{0}.$


## Special cases and values

1. When $m=0$ , the spherical harmonics $Y_{\ell }^{m}:S^{2}\to \mathbb {C}$ reduce to the ordinary Legendre polynomials: $Y_{\ell }^{0}(\theta ,\varphi )={\sqrt {\frac {2\ell +1}{4\pi }}}P_{\ell }(\cos \theta ).$
2. When $m=\pm \ell$ , $Y_{\ell }^{\pm \ell }(\theta ,\varphi )={\frac {(\mp 1)^{\ell }}{2^{\ell }\ell !}}{\sqrt {\frac {(2\ell +1)!}{4\pi }}}\sin ^{\ell }\theta \,e^{\pm i\ell \varphi },$ or more simply in Cartesian coordinates, $r^{\ell }Y_{\ell }^{\pm \ell }({\mathbf {r} })={\frac {(\mp 1)^{\ell }}{2^{\ell }\ell !}}{\sqrt {\frac {(2\ell +1)!}{4\pi }}}(x\pm iy)^{\ell }.$
3. At the north pole, where $\theta =0$ , and $\varphi$ is undefined, all spherical harmonics except those with $m=0$ vanish: $Y_{\ell }^{m}(0,\varphi )=Y_{\ell }^{m}({\mathbf {z} })={\sqrt {\frac {2\ell +1}{4\pi }}}\delta _{m0}.$


## Symmetry properties

The spherical harmonics have deep and consequential properties under the operations of spatial inversion (parity) and rotation.

### Parity

The spherical harmonics have definite parity. That is, they are either even or odd with respect to inversion about the origin. Inversion is represented by the operator $P\Psi (\mathbf {r} )=\Psi (-\mathbf {r} )$ . Then, as can be seen in many ways (perhaps most simply from the Herglotz generating function), with $\mathbf {r}$ being a unit vector, $Y_{\ell }^{m}(-\mathbf {r} )=(-1)^{\ell }Y_{\ell }^{m}(\mathbf {r} ).$

In terms of the spherical angles, parity transforms a point with coordinates $\{\theta ,\varphi \}$ to $\{\pi -\theta ,\pi +\varphi \}$ . The statement of the parity of spherical harmonics is then $Y_{\ell }^{m}(\theta ,\varphi )\to Y_{\ell }^{m}(\pi -\theta ,\pi +\varphi )=(-1)^{\ell }Y_{\ell }^{m}(\theta ,\varphi )$ (This can be seen as follows: The associated Legendre polynomials gives (−1)*ℓ*+*m* and from the exponential function we have (−1)*m*, giving together for the spherical harmonics a parity of (−1)*ℓ*.)

Parity continues to hold for real spherical harmonics, and for spherical harmonics in higher dimensions: applying a point reflection to a spherical harmonic of degree ℓ changes the sign by a factor of (−1)*ℓ*.

### Rotations

Consider a rotation ${\mathcal {R}}$ about the origin that sends the unit vector $\mathbf {r}$ to $\mathbf {r} '$ . Under this operation, a spherical harmonic of degree $\ell$ and order m transforms into a linear combination of spherical harmonics of the same degree. That is, $Y_{\ell }^{m}({\mathbf {r} }')=\sum _{m'=-\ell }^{\ell }A_{mm'}Y_{\ell }^{m'}({\mathbf {r} }),$ where $A_{mm'}$ is a matrix of order $(2\ell +1)$ that depends on the rotation ${\mathcal {R}}$ . However, this is not the standard way of expressing this property. In the standard way one writes,

$Y_{\ell }^{m}({\mathbf {r} }')=\sum _{m'=-\ell }^{\ell }[D_{mm'}^{(\ell )}({\mathcal {R}})]^{*}Y_{\ell }^{m'}({\mathbf {r} }),$ where $D_{mm'}^{(\ell )}({\mathcal {R}})^{*}$ is the complex conjugate of an element of the Wigner D-matrix. In particular when $\mathbf {r} '$ is a $\phi _{0}$ rotation of the azimuth we get the identity,

$Y_{\ell }^{m}({\mathbf {r} }')=Y_{\ell }^{m}({\mathbf {r} })e^{im\phi _{0}}.$

The rotational behavior of the spherical harmonics is perhaps their quintessential feature from the viewpoint of group theory. The $Y_{\ell }^{m}$ 's of degree $\ell$ provide a basis set of functions for the irreducible representation of the group SO(3) of dimension $(2\ell +1)$ . Many facts about spherical harmonics (such as the addition theorem) that are proved laboriously using the methods of analysis acquire simpler proofs and deeper significance using the methods of symmetry.


## Spherical harmonics expansion

The Laplace spherical harmonics $Y_{\ell }^{m}:S^{2}\to \mathbb {C}$ form a complete set of orthonormal functions and thus form an orthonormal basis of the Hilbert space of square-integrable functions $L_{\mathbb {C} }^{2}(S^{2})$ . On the unit sphere $S^{2}$ , any square-integrable function $f:S^{2}\to \mathbb {C}$ can thus be expanded as a linear combination of these:

$f(\theta ,\varphi )=\sum _{\ell =0}^{\infty }\sum _{m=-\ell }^{\ell }f_{\ell }^{m}\,Y_{\ell }^{m}(\theta ,\varphi ).$

This expansion holds in the sense of mean-square convergence — convergence in L2 of the sphere — which is to say that

$\lim _{N\to \infty }\int _{0}^{2\pi }\int _{0}^{\pi }\left|f(\theta ,\varphi )-\sum _{\ell =0}^{N}\sum _{m=-\ell }^{\ell }f_{\ell }^{m}Y_{\ell }^{m}(\theta ,\varphi )\right|^{2}\sin \theta \,d\theta \,d\varphi =0.$

The expansion coefficients are the analogs of Fourier coefficients, and can be obtained by multiplying the above equation by the complex conjugate of a spherical harmonic, integrating over the solid angle Ω, and utilizing the above orthogonality relationships. This is justified rigorously by basic Hilbert space theory. For the case of orthonormalized harmonics, this gives:

$f_{\ell }^{m}=\int _{\Omega }f(\theta ,\varphi )\,Y_{\ell }^{m*}(\theta ,\varphi )\,d\Omega =\int _{0}^{2\pi }d\varphi \int _{0}^{\pi }\,d\theta \,\sin \theta f(\theta ,\varphi )Y_{\ell }^{m*}(\theta ,\varphi ).$

If the coefficients decay in *ℓ* sufficiently rapidly — for instance, exponentially — then the series also converges uniformly to *f*.

A square-integrable function $f:S^{2}\to \mathbb {R}$ can also be expanded in terms of the real harmonics $Y_{\ell m}:S^{2}\to \mathbb {R}$ above as a sum

$f(\theta ,\varphi )=\sum _{\ell =0}^{\infty }\sum _{m=-\ell }^{\ell }f_{\ell m}\,Y_{\ell m}(\theta ,\varphi ).$

The convergence of the series holds again in the same sense, namely the real spherical harmonics $Y_{\ell m}:S^{2}\to \mathbb {R}$ form a complete set of orthonormal functions and thus form an orthonormal basis of the Hilbert space of square-integrable functions $L_{\mathbb {R} }^{2}(S^{2})$ . The benefit of the expansion in terms of the real harmonic functions $Y_{\ell m}$ is that for real functions $f:S^{2}\to \mathbb {R}$ the expansion coefficients $f_{\ell m}$ are guaranteed to be real, whereas their coefficients $f_{\ell }^{m}$ in their expansion in terms of the $Y_{\ell }^{m}$ (considering them as functions $f:S^{2}\to \mathbb {C} \supset \mathbb {R}$ ) do not have that property.

### Completeness Relation

The completeness relation is a distributional equality between a sum over all indices and the Dirac delta function. For the spherical harmonics, the Dirac delta is the tensor product of two Dirac delta functions, one for the azimuthal angle on the sphere, and one for the polar angle. The relation reads,

$\sum _{l=0}^{\infty }\sum _{m=-l}^{l}Y_{lm}^{*}(\theta \,',\,\phi \,')Y_{lm}(\theta ,\,\phi )=\delta (\phi -\phi \,')\,\delta (\cos \theta -\cos \theta \,').$


## Spectrum analysis

### Power spectrum in signal processing

The total power of a function *f* is defined in the signal processing literature as the integral of the function squared, divided by the area of its domain. Using the orthonormality properties of the real unit-power spherical harmonic functions, it is straightforward to verify that the total power of a function defined on the unit sphere is related to its spectral coefficients by a generalization of Parseval's theorem (here, the theorem is stated for Schmidt semi-normalized harmonics, the relationship is slightly different for orthonormal harmonics):

${\frac {1}{4\,\pi }}\int _{\Omega }|f(\Omega )|^{2}\,d\Omega =\sum _{\ell =0}^{\infty }S_{f\!f}(\ell ),$ where $S_{f\!f}(\ell )={\frac {1}{2\ell +1}}\sum _{m=-\ell }^{\ell }|f_{\ell m}|^{2}$

is defined as the angular power spectrum (for Schmidt semi-normalized harmonics). In a similar manner, one can define the cross-power of two functions as ${\frac {1}{4\,\pi }}\int _{\Omega }f(\Omega )\,g^{\ast }(\Omega )\,d\Omega =\sum _{\ell =0}^{\infty }S_{fg}(\ell ),$ where $S_{fg}(\ell )={\frac {1}{2\ell +1}}\sum _{m=-\ell }^{\ell }f_{\ell m}g_{\ell m}^{\ast }$

is defined as the cross-power spectrum. If the functions *f* and *g* have a zero mean (i.e., the spectral coefficients *f*00 and *g*00 are zero), then *S**ff*(*ℓ*) and *S**fg*(*ℓ*) represent the contributions to the function's variance and covariance for degree ℓ, respectively. It is common that the (cross-)power spectrum is well approximated by a power law of the form

$S_{f\!f}(\ell )=C\,\ell ^{\beta }.$

When *β* = 0, the spectrum is "white" as each degree possesses equal power. When *β* < 0, the spectrum is termed "red" as there is more power at the low degrees with long wavelengths than higher degrees. Finally, when *β* > 0, the spectrum is termed "blue". The condition on the order of growth of *S**ff*(*ℓ*) is related to the order of differentiability of *f* in the next section.


## Approximation and smoothness

Spherical harmonics are used to approximate functions on the sphere, and the order of decay of the power governs smoothness. Let $\Pi _{n}(S^{2})$ denote the space spanned by spherical harmonics of degree at most n . For a function f on the sphere, the error of best approximation by spherical polynomials of degree at most n is

$E_{n}(f)_{p}=\inf _{P\in \Pi _{n}(S^{2})}\|f-P\|_{p},$

with the norm taken in $L^{p}(S^{2})$ , or in the uniform norm when $p=\infty$ . The asymptotic behavior of $E_{n}(f)_{p}$ as $n\to \infty$ gives a quantitative measure of how well f can be approximated by low-degree spherical harmonics. This is analogous to approximation by trigonometric polynomials in ordinary Fourier analysis.

On the circle, smoothness can be measured by the decay of Fourier coefficients. On the sphere, smoother functions admit faster approximation by spherical polynomials, while conversely, sufficiently rapid decay of the approximation error implies smoothness. More precisely, Sobolev-type smoothness can also be described spectrally, since spherical harmonics of degree $\ell$ are eigenfunctions of the Laplace–Beltrami operator with eigenvalue $-\ell (\ell +1)$ .

For $p=2$ this relation can be stated especially explicitly. If

$f=\sum _{\ell =0}^{\infty }\sum _{m=-\ell }^{\ell }f_{\ell m}Y_{\ell m}$

is the spherical harmonic expansion of f , then the Sobolev norm of order s is equivalent, up to the normalization convention for the harmonics, to

$\|f\|_{H^{s}(S^{2})}^{2}=\sum _{\ell =0}^{\infty }(1+\ell (\ell +1))^{s}S_{ff}(\ell ).$

Thus $f\in H^{s}(S^{2})$ precisely when this weighted sum is finite. Since $\ell (\ell +1)$ grows like $\ell ^{2}$ , higher Sobolev smoothness requires faster decay of the power in high degrees.

In $L^{2}$ , the best approximation by spherical harmonics of degree at most n is obtained by truncating the spherical harmonic expansion, so that

$E_{n}(f)_{2}^{2}=\sum _{\ell >n}S_{ff}(\ell ).$

Consequently, if $f\in H^{s}(S^{2})$ , then

$E_{n}(f)_{2}\leq C_{s}n^{-s}\|f\|_{H^{s}(S^{2})},$

which bounds the approximation error by the Sobolev norm.

With the above power normalization, a decay estimate of the form $S_{ff}(\ell )=O(\ell ^{-\alpha })$ implies membership in $H^{s}(S^{2})$ whenever $\alpha >2s+1$ . By the Sobolev embedding theorem, $H^{s}(S^{2})$ embeds into $C^{k}(S^{2})$ when $s>k+1$ . Thus sufficiently fast polynomial decay of the power spectrum implies differentiability, and decay faster than every power implies smoothness of all orders.
