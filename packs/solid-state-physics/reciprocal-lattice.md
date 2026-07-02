---
title: "Reciprocal lattice"
source: https://en.wikipedia.org/wiki/Reciprocal_lattice
domain: solid-state-physics
license: CC-BY-SA-4.0
tags: solid-state physics, brillouin zone, density of states, reciprocal lattice
fetched: 2026-07-02
---

# Reciprocal lattice

**Reciprocal lattice** is a concept associated with solids with translational symmetry which plays a major role in many areas such as X-ray and electron diffraction as well as the energies of electrons in a solid. It emerges from the Fourier transform of the lattice associated with the arrangement of the atoms. The *direct lattice* or *real lattice* is a periodic function in physical space, such as a crystal system (usually a Bravais lattice). The reciprocal lattice exists in the mathematical space of spatial frequencies or wavenumbers *k*, known as **reciprocal space** or ***k* space**; it is the dual of physical space considered as a vector space. In other words, the reciprocal lattice is the sublattice which is dual to the direct lattice.

The reciprocal lattice is the set of all vectors $\mathbf {G} _{m}$ , that are wavevectors **k** of plane waves in the Fourier series of a spatial function whose periodicity is the same as that of a direct lattice $\mathbf {R} _{n}$ . Each plane wave in this Fourier series has the same phase or phases that are differed by multiples of $2\pi$ , at each direct lattice point (so essentially same phase at all the direct lattice points).

The reciprocal lattice of a reciprocal lattice is equivalent to the original direct lattice, because the defining equations are symmetrical with respect to the vectors in real and reciprocal space. Mathematically, direct and reciprocal lattice vectors represent covariant and contravariant vectors, respectively.

The Brillouin zone is a Wigner–Seitz cell of the reciprocal lattice.

## Wave-based description

### Reciprocal space

Reciprocal space (also called k-space) provides a way to visualize the results of the Fourier transform of a spatial function. It is similar in role to the frequency domain arising from the Fourier transform of a time dependent function; reciprocal space is a space over which the Fourier transform of a spatial function is represented at spatial frequencies or wavevectors of plane waves of the Fourier transform. The domain of the spatial function itself is often referred to as spatial domain or real space. In physical applications, such as crystallography, both real and reciprocal space will often each be two or three dimensional. Whereas the number of spatial dimensions of these two associated spaces will be the same, the spaces will differ in their quantity dimension, so that when the real space has the dimension length (**L**), its reciprocal space will have inverse length, so **L**−1 (the reciprocal of length).

Reciprocal space comes into play regarding waves, both classical and quantum mechanical. Because a sinusoidal plane wave with unit amplitude can be written as an oscillatory term $\cos(kx-\omega t+\varphi _{0})$ , with initial phase $\varphi _{0}$ , angular wavenumber k and angular frequency $\omega$ , it can be regarded as a function of both k and x (and the time-varying part as a function of both $\omega$ and t ). This complementary role of k and x leads to their visualization within complementary spaces (the real space and the reciprocal space). The spatial periodicity of this wave is defined by its wavelength $\lambda$ , where $k\lambda =2\pi$ ; hence the corresponding wavenumber in reciprocal space will be $k=2\pi /\lambda$ .

In three dimensions, the corresponding plane wave term becomes $\cos(\mathbf {k} \cdot \mathbf {r} -\omega t+\varphi _{0})$ , which simplifies to $\cos(\mathbf {k} \cdot \mathbf {r} +\varphi )$ at a fixed time t , where $\mathbf {r}$ is the position vector of a point in real space and now $\mathbf {k} =2\pi \mathbf {e} /\lambda$ is the wavevector in the three dimensional reciprocal space. (The magnitude of a wavevector is called wavenumber.) The constant $\varphi$ is the phase of the wavefront (a plane of a constant phase) through the origin $\mathbf {r} =0$ at time t , and $\mathbf {e}$ is a unit normal vector to this wavefront. The wavefronts with phases $\varphi +(2\pi )n$ , where n represents any integer, comprise a set of parallel planes, equally spaced by the wavelength $\lambda$ .

### Reciprocal lattice

In general, a geometric lattice is an infinite, regular array of vertices (points) in space, which can be modelled vectorially as a Bravais lattice. Some lattices may be skew, which means that their primary lines may not necessarily be at right angles. In reciprocal space, a reciprocal lattice is defined as the set of wavevectors $\mathbf {k}$ of plane waves in the Fourier series of any function $f(\mathbf {r} )$ whose periodicity is compatible with that of an initial direct lattice in real space. Equivalently, a wavevector is a vertex of the reciprocal lattice if it corresponds to a plane wave in real space whose phase at any given time is the same (actually differs by $(2\pi )n$ with an integer n ) at every direct lattice vertex.

One heuristic approach to constructing the reciprocal lattice in three dimensions is to write the position vector of a vertex of the direct lattice as $\mathbf {R} =n_{1}\mathbf {a} _{1}+n_{2}\mathbf {a} _{2}+n_{3}\mathbf {a} _{3}$ , where the $n_{i}$ are integers defining the vertex and the $\mathbf {a} _{i}$ are linearly independent primitive translation vectors (or shortly called primitive vectors) that are characteristic of the lattice. There is then a unique plane wave (up to a factor of negative one), whose wavefront through the origin $\mathbf {R} =0$ contains the direct lattice points at $\mathbf {a} _{2}$ and $\mathbf {a} _{3}$ , and with its adjacent wavefront (whose phase differs by $2\pi$ or $-2\pi$ from the former wavefront passing the origin) passing through $\mathbf {a} _{1}$ . Its angular wavevector takes the form $\mathbf {b} _{1}=2\pi \mathbf {e} _{1}/\lambda _{1}$ , where $\mathbf {e} _{1}$ is the unit vector perpendicular to these two adjacent wavefronts and the wavelength $\lambda _{1}$ must satisfy $\lambda _{1}=\mathbf {a} _{1}\cdot \mathbf {e} _{1}$ , means that $\lambda _{1}$ is equal to the distance between the two wavefronts. Hence by construction $\mathbf {a} _{1}\cdot \mathbf {b} _{1}=2\pi$ and $\mathbf {a} _{2}\cdot \mathbf {b} _{1}=\mathbf {a} _{3}\cdot \mathbf {b} _{1}=0$ .

Cycling through the indices in turn, the same method yields three wavevectors $\mathbf {b} _{j}$ with $\mathbf {a} _{i}\cdot \mathbf {b} _{j}=2\pi \,\delta _{ij}$ , where the Kronecker delta $\delta _{ij}$ equals one when $i=j$ and is zero otherwise. The $\mathbf {b} _{j}$ comprise a set of three primitive wavevectors or three primitive translation vectors for the reciprocal lattice, each of whose vertices takes the form $\mathbf {G} =m_{1}\mathbf {b} _{1}+m_{2}\mathbf {b} _{2}+m_{3}\mathbf {b} _{3}$ , where the $m_{j}$ are integers. The reciprocal lattice is also a Bravais lattice as it is formed by integer combinations of the primitive vectors, that are $\mathbf {b} _{1}$ , $\mathbf {b} _{2}$ , and $\mathbf {b} _{3}$ in this case. Simple algebra then shows that, for any plane wave with a wavevector $\mathbf {G}$ on the reciprocal lattice, the total phase shift $\mathbf {G} \cdot \mathbf {R}$ between the origin and any point $\mathbf {R}$ on the direct lattice is a multiple of $2\pi$ (that can be possibly zero if the multiplier is zero), so the phase of the plane wave with $\mathbf {G}$ will essentially be equal for every direct lattice vertex, in conformity with the reciprocal lattice definition above. (Although any wavevector $\mathbf {G}$ on the reciprocal lattice does always take this form, this derivation is motivational, rather than rigorous, because it has omitted the proof that no other possibilities exist.)

The Brillouin zone is a primitive cell (more specifically a Wigner–Seitz cell) of the reciprocal lattice, which plays an important role in solid state physics due to Bloch's theorem. In pure mathematics, the dual space of linear forms and the dual lattice provide more abstract generalizations of reciprocal space and the reciprocal lattice.

## Mathematical description

Assuming a three-dimensional Bravais lattice and labelling each lattice vector (a vector indicating a lattice point) by the subscript $n=(n_{1},n_{2},n_{3})$ as 3-tuple of integers,

$\mathbf {R} _{n}=n_{1}\mathbf {a} _{1}+n_{2}\mathbf {a} _{2}+n_{3}\mathbf {a} _{3}$

where

$n_{1},n_{2},n_{3}\in \mathbb {Z}$

where $\mathbb {Z}$ is the set of integers and $\mathbf {a} _{i}$ is a primitive translation vector or shortly primitive vector. Taking a function $f(\mathbf {r} )$ where $\mathbf {r}$ is a position vector from the origin $\mathbf {R} _{n}=0$ to any position, if $f(\mathbf {r} )$ follows the periodicity of this lattice, e.g. the function describing the electronic density in an atomic crystal, it is useful to write $f(\mathbf {r} )$ as a multi-dimensional Fourier series

$\sum _{m}f_{m}e^{i\mathbf {G} _{m}\cdot \mathbf {r} }=f\left(\mathbf {r} \right)$

where now the subscript $m=(m_{1},m_{2},m_{3})$ , so this is a triple sum.

As $f(\mathbf {r} )$ follows the periodicity of the lattice, translating $\mathbf {r}$ by any lattice vector $\mathbf {R} _{n}$ we get the same value, hence

$f(\mathbf {r} +\mathbf {R} _{n})=f(\mathbf {r} ).$

Expressing the above instead in terms of their Fourier series we have $\sum _{m}f_{m}e^{i\mathbf {G} _{m}\cdot \mathbf {r} }=\sum _{m}f_{m}e^{i\mathbf {G} _{m}\cdot (\mathbf {r} +\mathbf {R} _{n})}=\sum _{m}f_{m}e^{i\mathbf {G} _{m}\cdot \mathbf {R} _{n}}\,e^{i\mathbf {G} _{m}\cdot \mathbf {r} }.$

Because equality of two Fourier series implies equality of their coefficients, $e^{i\mathbf {G} _{m}\cdot \mathbf {R} _{n}}=1$ , which only holds when

$\mathbf {G} _{m}\cdot \mathbf {R} _{n}=2\pi N$

where

$N\in \mathbb {Z} .$

Mathematically, the reciprocal lattice is the set of all vectors $\mathbf {G} _{m}$ , that are wavevectors of plane waves in the Fourier series of a spatial function whose periodicity is the same as that of a direct lattice as the set of all direct lattice point position vectors $\mathbf {R} _{n}$ , and $\mathbf {G} _{m}$ satisfy this equality for all $\mathbf {R} _{n}$ . Each plane wave in the Fourier series has the same phase (actually can be differed by a multiple of $2\pi$ ) at all the lattice point $\mathbf {R} _{n}$ .

$\mathbf {G} _{m}$ can be chosen in the form of $\mathbf {G} _{m}=m_{1}\mathbf {b} _{1}+m_{2}\mathbf {b} _{2}+m_{3}\mathbf {b} _{3}$ where $\mathbf {a} _{i}\cdot \mathbf {b} _{j}=2\pi \,\delta _{ij}$ . With this form, the reciprocal lattice as the set of all wavevectors $\mathbf {G} _{m}$ for the Fourier series of a spatial function which periodicity follows $\mathbf {R} _{n}$ , is itself a Bravais lattice as it is formed by integer combinations of its own primitive translation vectors $\left(\mathbf {b_{1}} ,\mathbf {b} _{2},\mathbf {b} _{3}\right)$ , and the reciprocal of the reciprocal lattice is the original lattice, which reveals the Pontryagin duality of their respective vector spaces. (There may be other form of $\mathbf {G} _{m}$ . Any valid form of $\mathbf {G} _{m}$ results in the same reciprocal lattice.)

### Two dimensions

For an infinite two-dimensional lattice, defined by its primitive vectors $\left(\mathbf {a} _{1},\mathbf {a} _{2}\right)$ , its reciprocal lattice can be determined by generating its two reciprocal primitive vectors, through the following formulae,

$\mathbf {G} _{m}=m_{1}\mathbf {b} _{1}+m_{2}\mathbf {b} _{2}$

where $m_{i}$ is an integer and

${\begin{aligned}\mathbf {b} _{1}&=2\pi {\frac {-\mathbf {Q} \,\mathbf {a} _{2}}{-\mathbf {a} _{1}\cdot \mathbf {Q} \,\mathbf {a} _{2}}}=2\pi {\frac {\mathbf {Q} \,\mathbf {a} _{2}}{\mathbf {a} _{1}\cdot \mathbf {Q} \,\mathbf {a} _{2}}}\\[8pt]\mathbf {b} _{2}&=2\pi {\frac {\mathbf {Q} \,\mathbf {a} _{1}}{\mathbf {a} _{2}\cdot \mathbf {Q} \,\mathbf {a} _{1}}}\end{aligned}}$

Here $\mathbf {Q}$ represents a 90 degree rotation matrix, i.e. a *q*uarter turn. The anti-clockwise rotation and the clockwise rotation can both be used to determine the reciprocal lattice: If $\mathbf {Q}$ is the anti-clockwise rotation and $\mathbf {Q'}$ is the clockwise rotation, $\mathbf {Q} \,\mathbf {v} =-\mathbf {Q'} \,\mathbf {v}$ for all vectors $\mathbf {v}$ . Thus, using the permutation

$\sigma ={\begin{pmatrix}1&2\\2&1\end{pmatrix}}$

we obtain

$\mathbf {b} _{n}=2\pi {\frac {\mathbf {Q} \,\mathbf {a} _{\sigma (n)}}{\mathbf {a} _{n}\cdot \mathbf {Q} \,\mathbf {a} _{\sigma (n)}}}=2\pi {\frac {\mathbf {Q} '\,\mathbf {a} _{\sigma (n)}}{\mathbf {a} _{n}\cdot \mathbf {Q} '\,\mathbf {a} _{\sigma (n)}}}.$

Notably, in a 3D space this 2D reciprocal lattice is an infinitely extended set of Bragg rods—described by Sung et al.

### Three dimensions

For an infinite three-dimensional lattice $\mathbf {R} _{n}=n_{1}\mathbf {a} _{1}+n_{2}\mathbf {a} _{2}+n_{3}\mathbf {a} _{3}$ , defined by its primitive vectors $\left(\mathbf {a_{1}} ,\mathbf {a} _{2},\mathbf {a} _{3}\right)$ and the subscript of integers $n=\left(n_{1},n_{2},n_{3}\right)$ , its reciprocal lattice $\mathbf {G} _{m}=m_{1}\mathbf {b} _{1}+m_{2}\mathbf {b} _{2}+m_{3}\mathbf {b} _{3}$ with the integer subscript $m=(m_{1},m_{2},m_{3})$ can be determined by generating its three reciprocal primitive vectors $\left(\mathbf {b_{1}} ,\mathbf {b} _{2},\mathbf {b} _{3}\right)$ ${\begin{aligned}\mathbf {b} _{1}&={\frac {2\pi }{V}}\ \mathbf {a} _{2}\times \mathbf {a} _{3}\\[8pt]\mathbf {b} _{2}&={\frac {2\pi }{V}}\ \mathbf {a} _{3}\times \mathbf {a} _{1}\\[8pt]\mathbf {b} _{3}&={\frac {2\pi }{V}}\ \mathbf {a} _{1}\times \mathbf {a} _{2}\end{aligned}}$ where $V=\mathbf {a} _{1}\cdot \left(\mathbf {a} _{2}\times \mathbf {a} _{3}\right)=\mathbf {a} _{2}\cdot \left(\mathbf {a} _{3}\times \mathbf {a} _{1}\right)=\mathbf {a} _{3}\cdot \left(\mathbf {a} _{1}\times \mathbf {a} _{2}\right)$ is the scalar triple product. The choice of these $\left(\mathbf {b_{1}} ,\mathbf {b} _{2},\mathbf {b} _{3}\right)$ is to satisfy $\mathbf {a} _{i}\cdot \mathbf {b} _{j}=2\pi \,\delta _{ij}$ as the known condition (There may be other condition.) of primitive translation vectors for the reciprocal lattice derived in the heuristic approach above and the section multi-dimensional Fourier series. This choice also satisfies the requirement of the reciprocal lattice $e^{i\mathbf {G} _{m}\cdot \mathbf {R} _{n}}=1$ mathematically derived above. Using column vector representation of (reciprocal) primitive vectors, the formulae above can be rewritten using matrix inversion:

$\left[\mathbf {b} _{1}\mathbf {b} _{2}\mathbf {b} _{3}\right]^{\mathsf {T}}=2\pi \left[\mathbf {a} _{1}\mathbf {a} _{2}\mathbf {a} _{3}\right]^{-1}.$

This method appeals to the definition, and allows generalization to arbitrary dimensions. The cross product formula dominates introductory materials on crystallography.

The above definition is called the "physics" definition, as the factor of $2\pi$ comes naturally from the study of periodic structures. An essentially equivalent definition, the "crystallographer's" definition, comes from defining the reciprocal lattice $\mathbf {K} _{m}=\mathbf {G} _{m}/2\pi$ . which changes the reciprocal primitive vectors to be

$\mathbf {b} _{1}={\frac {\mathbf {a} _{2}\times \mathbf {a} _{3}}{\mathbf {a} _{1}\cdot \left(\mathbf {a} _{2}\times \mathbf {a} _{3}\right)}}$

and so on for the other primitive vectors. The crystallographer's definition has the advantage that the definition of $\mathbf {b} _{1}$ is just the reciprocal magnitude of $\mathbf {a} _{1}$ in the direction of $\mathbf {a} _{2}\times \mathbf {a} _{3}$ , dropping the factor of $2\pi$ . This can simplify certain mathematical manipulations, and expresses reciprocal lattice dimensions in units of spatial frequency. It is a matter of taste which definition of the lattice is used, as long as the two are not mixed.

$m=(m_{1},m_{2},m_{3})$ is conventionally written as $(h,k,\ell )$ or $(hk\ell )$ , called Miller indices; $m_{1}$ is replaced with h , $m_{2}$ replaced with k , and $m_{3}$ replaced with $\ell$ . Each lattice point $(hk\ell )$ in the reciprocal lattice corresponds to a set of lattice planes $(hk\ell )$ in the real space lattice. (A lattice plane is a plane crossing lattice points.) The direction of the reciprocal lattice vector corresponds to the normal to the real space planes. The magnitude of the reciprocal lattice vector $\mathbf {K} _{m}$ is given in reciprocal length and is equal to the reciprocal of the interplanar spacing of the real space planes.

### Higher dimensions

The formula for n dimensions can be derived assuming an n -dimensional real vector space V with a basis $(\mathbf {a} _{1},\ldots ,\mathbf {a} _{n})$ and an inner product $g\colon V\times V\to \mathbf {R}$ . The reciprocal lattice vectors are uniquely determined by the formula $g(\mathbf {a} _{i},\mathbf {b} _{j})=2\pi \delta _{ij}$ . Using the permutation

$\sigma ={\begin{pmatrix}1&2&\cdots &n\\2&3&\cdots &1\end{pmatrix}},$

they can be determined with the following formula:

$\mathbf {b} _{i}=2\pi {\frac {\varepsilon _{\sigma ^{1}i\ldots \sigma ^{n}i}}{\omega (\mathbf {a} _{1},\ldots ,\mathbf {a} _{n})}}g^{-1}(\mathbf {a} _{\sigma ^{n-1}i}\,\lrcorner \ldots \mathbf {a} _{\sigma ^{1}i}\,\lrcorner \,\omega )\in V$

Here, $\omega \colon V^{n}\to \mathbf {R}$ is the volume form, $g^{-1}$ is the inverse of the vector space isomorphism ${\hat {g}}\colon V\to V^{*}$ defined by ${\hat {g}}(v)(w)=g(v,w)$ and $\lrcorner$ denotes the inner multiplication.

One can verify that this formula is equivalent to the known formulas for the two- and three-dimensional case by using the following facts: In three dimensions, $\omega (u,v,w)=g(u\times v,w)$ and in two dimensions, $\omega (v,w)=g(Rv,w)$ , where $R\in {\text{SO}}(2)\subset L(V,V)$ is the rotation by 90 degrees (just like the volume form, the angle assigned to a rotation depends on the choice of orientation).

## Reciprocal lattices of various crystals

Reciprocal lattices for the cubic crystal system are as follows.

### Simple cubic lattice

The simple cubic Bravais lattice, with cubic primitive cell of side a , has for its reciprocal a simple cubic lattice with a cubic primitive cell of side ${\textstyle {\frac {2\pi }{a}}}$ (or ${\textstyle {\frac {1}{a}}}$ in the crystallographer's definition). The cubic lattice is therefore said to be self-dual, having the same symmetry in reciprocal space as in real space.

### Face-centered cubic (FCC) lattice

The reciprocal lattice to an FCC lattice is the body-centered cubic (BCC) lattice, with a cube side of ${\textstyle {\frac {4\pi }{a}}}$ .

Consider an FCC compound unit cell. Locate a primitive unit cell of the FCC; i.e., a unit cell with one lattice point. Now take one of the vertices of the primitive unit cell as the origin. Give the basis vectors of the real lattice. Then from the known formulae, you can calculate the basis vectors of the reciprocal lattice. These reciprocal lattice vectors of the FCC represent the basis vectors of a BCC real lattice. The basis vectors of a real BCC lattice and the reciprocal lattice of an FCC resemble each other in direction but not in magnitude.

### Body-centered cubic (BCC) lattice

The reciprocal lattice to a BCC lattice is the FCC lattice, with a cube side of ${\textstyle 4\pi /a}$ .

It can be proven that only the Bravais lattices which have 90 degrees between $\left(\mathbf {a} _{1},\mathbf {a} _{2},\mathbf {a} _{3}\right)$ (cubic, tetragonal, orthorhombic) have primitive translation vectors for the reciprocal lattice, $\left(\mathbf {b} _{1},\mathbf {b} _{2},\mathbf {b} _{3}\right)$ , parallel to their real-space vectors.

### Simple hexagonal lattice

The reciprocal to a simple hexagonal Bravais lattice with lattice constants ${\textstyle a}$ and ${\textstyle c}$ is another simple hexagonal lattice with lattice constants ${\textstyle 2\pi /c}$ and ${\textstyle 4\pi /(a{\sqrt {3}})}$ rotated through 90° about the *c* axis with respect to the direct lattice. The simple hexagonal lattice is therefore said to be self-dual, having the same symmetry in reciprocal space as in real space. Primitive translation vectors for this simple hexagonal Bravais lattice vectors are ${\begin{aligned}a_{1}&={\frac {\sqrt {3}}{2}}a{\hat {x}}+{\frac {1}{2}}a{\hat {y}},\\[8pt]a_{2}&=-{\frac {\sqrt {3}}{2}}a{\hat {x}}+{\frac {1}{2}}a{\hat {y}},\\[8pt]a_{3}&=c{\hat {z}}.\end{aligned}}$

## Arbitrary collection of atoms

One path to the reciprocal lattice of an arbitrary collection of atoms comes from the idea of scattered waves in the Fraunhofer (long-distance or lens back-focal-plane) limit as a Huygens-style sum of amplitudes from all points of scattering (in this case from each individual atom). This sum is denoted by the complex amplitude F in the equation below, because it is also the Fourier transform (as a function of spatial frequency or reciprocal distance) of an effective scattering potential in direct space:

$F[{\vec {g}}]=\sum _{j=1}^{N}f_{j}\!\left[{\vec {g}}\right]e^{2\pi i{\vec {g}}\cdot {\vec {r}}_{j}}.$

Here **g** = **q**/(2π) is the scattering vector **q** in crystallographer units, *N* is the number of atoms, *f**j*[**g**] is the atomic scattering factor for atom *j* and scattering vector **g**, while **r***j* is the vector position of atom *j*. The Fourier phase depends on one's choice of coordinate origin.

For the special case of an infinite periodic crystal, the scattered amplitude *F* = *M* *Fh,k,ℓ* from *M* unit cells (as in the cases above) turns out to be non-zero only for integer values of $(h,k,\ell )$ , where

$F_{h,k,\ell }=\sum _{j=1}^{m}f_{j}\left[g_{h,k,\ell }\right]e^{2\pi i\left(hu_{j}+kv_{j}+\ell w_{j}\right)}$

when there are *j* = 1,*m* atoms inside the unit cell whose fractional lattice indices are respectively {*u**j*, *v**j*, *w**j*}. To consider effects due to finite crystal size, of course, a shape convolution for each point or the equation above for a finite lattice must be used instead.

Whether the array of atoms is finite or infinite, one can also imagine an "intensity reciprocal lattice" I[**g**], which relates to the amplitude lattice F via the usual relation *I* = *F***F* where *F** is the complex conjugate of F. Since Fourier transformation is reversible, of course, this act of conversion to intensity tosses out "all except 2nd moment" (i.e. the phase) information. For the case of an arbitrary collection of atoms, the intensity reciprocal lattice is therefore:

$I[{\vec {g}}]=\sum _{j=1}^{N}\sum _{k=1}^{N}f_{j}\left[{\vec {g}}\right]f_{k}\left[{\vec {g}}\right]e^{2\pi i{\vec {g}}\cdot {\vec {r}}_{\!\!\;jk}}.$

Here **r***jk* is the vector separation between atom *j* and atom *k*. One can also use this to predict the effect of nano-crystallite shape, and subtle changes in beam orientation, on detected diffraction peaks even if in some directions the cluster is only one atom thick. On the down side, scattering calculations using the reciprocal lattice basically consider an incident plane wave. Thus after a first look at reciprocal lattice (kinematic scattering) effects, beam broadening and multiple scattering (i.e. dynamical) effects may be important to consider as well.

## Generalization of a dual lattice

There are actually two versions in mathematics of the abstract dual lattice concept, for a given lattice *L* in a real vector space *V*, of finite dimension.

The first, which generalises directly the reciprocal lattice construction, uses Fourier analysis. It may be stated simply in terms of Pontryagin duality. The dual group *V*^ to *V* is again a real vector space, and its closed subgroup *L*^ dual to *L* turns out to be a lattice in *V*^. Therefore, *L*^ is the natural candidate for *dual lattice*, in a different vector space (of the same dimension).

The other aspect is seen in the presence of a quadratic form *Q* on *V*; if it is non-degenerate it allows an identification of the dual space *V** of *V* with *V*. The relation of *V** to *V* is not intrinsic; it depends on a choice of Haar measure (volume element) on *V*. But given an identification of the two, which is in any case well-defined up to a scalar, the presence of *Q* allows one to speak to the dual lattice to *L* while staying within *V*.

In mathematics, the dual lattice of a given lattice *L* in an abelian locally compact topological group *G* is the subgroup *L*∗ of the dual group of *G* consisting of all continuous characters that are equal to one at each point of *L*.

In discrete mathematics, a lattice is a locally discrete set of points described by all integral linear combinations of dim = *n* linearly independent vectors in **R***n*. The dual lattice is then defined by all points in the linear span of the original lattice (typically all of **R***n*) with the property that an integer results from the inner product with all elements of the original lattice. It follows that the dual of the dual lattice is the original lattice.

Furthermore, if we allow the matrix *B* to have columns as the linearly independent vectors that describe the lattice, then the matrix $A=B\left(B^{\mathsf {T}}B\right)^{-1}$ has columns of vectors that describe the dual lattice.

## In quantum physics

In quantum physics, reciprocal space is closely related to *momentum space* according to the proportionality $\mathbf {p} =\hbar \mathbf {k}$ , where $\mathbf {p}$ is the momentum vector and $\hbar$ is the reduced Planck constant.
