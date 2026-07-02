---
title: "Structure factor"
source: https://en.wikipedia.org/wiki/Structure_factor
domain: x-ray-diffraction
license: CC-BY-SA-4.0
tags: x-ray diffraction, bragg law, powder diffraction, structure factor
fetched: 2026-07-02
---

# Structure factor

In condensed matter physics and crystallography, the **static structure factor** (or **structure factor** for short) is a mathematical description of how a material scatters incident radiation. The structure factor is a critical tool in the interpretation of scattering patterns (interference patterns) obtained in X-ray, electron and neutron diffraction experiments.

Confusingly, there are two different mathematical expressions in use, both called 'structure factor'. One is usually written $S(\mathbf {q} )$ ; it is more generally valid, and relates the observed diffracted intensity per atom to that produced by a single scattering unit. The other is usually written F or $F_{hk\ell }$ and is only valid for systems with long-range positional order — crystals. This expression relates the amplitude and phase of the beam diffracted by the $(hk\ell )$ planes of the crystal ( $(hk\ell )$ are the Miller indices of the planes) to that produced by a single scattering unit at the vertices of the primitive unit cell. $F_{hk\ell }$ is not a special case of $S(\mathbf {q} )$ ; $S(\mathbf {q} )$ gives the scattering intensity, but $F_{hk\ell }$ gives the amplitude. It is the modulus squared $|F_{hk\ell }|^{2}$ that gives the scattering intensity. $F_{hk\ell }$ is defined for a perfect crystal, and is used in crystallography, while $S(\mathbf {q} )$ is most useful for disordered systems. For partially ordered systems such as crystalline polymers there is obviously overlap, and experts will switch from one expression to the other as needed.

The static structure factor is measured without resolving the energy of scattered photons/electrons/neutrons. Energy-resolved measurements yield the dynamic structure factor.

## Derivation of *S*(*q*)

Consider the scattering of a beam of wavelength $\lambda$ by an assembly of N particles or atoms stationary at positions $\textstyle \mathbf {R} _{j},j=1,\,\ldots ,\,N$ . Assume that the scattering is weak, so that the amplitude of the incident beam is constant throughout the sample volume (Born approximation), and absorption, refraction and multiple scattering can be neglected (kinematic diffraction). The direction of any scattered wave is defined by its scattering vector $\mathbf {q}$ . This vector is $\mathbf {q} =\mathbf {k_{s}} -\mathbf {k_{o}}$ , where $\mathbf {k_{s}}$ and $\mathbf {k_{o}}$ ( $|\mathbf {k_{s}} |=|\mathbf {k_{0}} |=2\pi /\lambda$ ) are the scattered and incident beam wavevectors, and $\theta$ is the angle between them. For elastic scattering, $|\mathbf {k} _{s}|=|\mathbf {k_{o}} |$ and $q=|\mathbf {q} |={{\frac {4\pi }{\lambda }}\sin(\theta /2)}$ , limiting the possible range of $\mathbf {q}$ (see Ewald sphere). The amplitude and phase of this scattered wave will be the vector sum of the scattered waves from all the atoms $\Psi _{s}(\mathbf {q} )=\sum _{j=1}^{N}f_{j}\mathrm {e} ^{-i\mathbf {q} \cdot \mathbf {R} _{j}}$

For an assembly of atoms, $f_{j}$ is the atomic form factor of the j -th atom. The scattered intensity is obtained by multiplying this function by its complex conjugate

| $I(\mathbf {q} )=\Psi _{s}(\mathbf {q} )\times \Psi _{s}^{*}(\mathbf {q} )=\sum _{j=1}^{N}f_{j}\mathrm {e} ^{-i\mathbf {q} \cdot \mathbf {R} _{j}}\times \sum _{k=1}^{N}f_{k}\mathrm {e} ^{i\mathbf {q} \cdot \mathbf {R} _{k}}=\sum _{j=1}^{N}\sum _{k=1}^{N}f_{j}f_{k}\mathrm {e} ^{-i\mathbf {q} \cdot (\mathbf {R} _{j}-\mathbf {R} _{k})}$ |   | 1 |
|---|---|---|

The structure factor is defined as this intensity normalized by $1/\sum _{j=1}^{N}f_{j}^{2}$

| $S(\mathbf {q} )={\frac {1}{\sum _{j=1}^{N}f_{j}^{2}}}\sum _{j=1}^{N}\sum _{k=1}^{N}f_{j}f_{k}\mathrm {e} ^{-i\mathbf {q} \cdot (\mathbf {R} _{j}-\mathbf {R} _{k})}$ |   | 2 |
|---|---|---|

If all the atoms are identical, then Equation (**1**) becomes $I(\mathbf {q} )=f^{2}\sum _{j=1}^{N}\sum _{k=1}^{N}\mathrm {e} ^{-i\mathbf {q} \cdot (\mathbf {R} _{j}-\mathbf {R} _{k})}$ and $\sum _{j=1}^{N}f_{j}^{2}=Nf^{2}$ so

| $S(\mathbf {q} )={\frac {1}{N}}\sum _{j=1}^{N}\sum _{k=1}^{N}\mathrm {e} ^{-i\mathbf {q} \cdot (\mathbf {R} _{j}-\mathbf {R} _{k})}$ |   | 3 |
|---|---|---|

Another useful simplification is if the material is isotropic, like a powder or a simple liquid. In that case, the intensity depends on $q=|\mathbf {q} |$ and $r_{jk}=|\mathbf {r} _{j}-\mathbf {r} _{k}|$ . In three dimensions, Equation (**2**) then simplifies to the Debye scattering equation:

| $S(q)={\frac {1}{\sum _{j=1}^{N}f_{j}^{2}}}\sum _{j=1}^{N}\sum _{k=1}^{N}f_{j}f_{k}{\frac {\sin(qr_{jk})}{qr_{jk}}}$ |   | 4 |
|---|---|---|

An alternative derivation gives good insight, but uses Fourier transforms and convolution. To be general, consider a scalar (real) quantity $\phi (\mathbf {r} )$ defined in a volume V ; this may correspond, for instance, to a mass or charge distribution or to the refractive index of an inhomogeneous medium. If the scalar function is integrable, we can write its Fourier transform as $\textstyle \psi (\mathbf {q} )=\int _{V}\phi (\mathbf {r} )\exp(-i\mathbf {q} \cdot \mathbf {r} )\,\mathrm {d} \mathbf {r}$ . In the Born approximation the amplitude of the scattered wave corresponding to the scattering vector $\mathbf {q}$ is proportional to the Fourier transform $\textstyle \psi (\mathbf {q} )$ . When the system under study is composed of a number N of identical constituents (atoms, molecules, colloidal particles, etc.) each of which has a distribution of mass or charge $f(\mathbf {r} )$ then the total distribution can be considered the convolution of this function with a set of delta functions.

| $\phi (\mathbf {r} )=\sum _{j=1}^{N}f(\mathbf {r} -\mathbf {R} _{j})=f(\mathbf {r} )\ast \sum _{j=1}^{N}\delta (\mathbf {r} -\mathbf {R} _{j}),$ |   | 5 |
|---|---|---|

with $\textstyle \mathbf {R} _{j},j=1,\,\ldots ,\,N$ the particle positions as before. Using the property that the Fourier transform of a convolution product is simply the product of the Fourier transforms of the two factors, we have $\textstyle \psi (\mathbf {q} )=f(\mathbf {q} )\times \sum _{j=1}^{N}\exp(-i\mathbf {q} \cdot \mathbf {R} _{j})$ , so that:

| $I(\mathbf {q} )=\left\|f(\mathbf {q} )\right\|^{2}\times \left(\sum _{j=1}^{N}\mathrm {e} ^{-i\mathbf {q} \cdot \mathbf {R} _{j}}\right)\times \left(\sum _{k=1}^{N}\mathrm {e} ^{i\mathbf {q} \cdot \mathbf {R} _{k}}\right)=\left\|f(\mathbf {q} )\right\|^{2}\sum _{j=1}^{N}\sum _{k=1}^{N}\mathrm {e} ^{-i\mathbf {q} \cdot (\mathbf {R} _{j}-\mathbf {R} _{k})}.$ |   | 6 |
|---|---|---|

This is clearly the same as Equation (**1**) with all particles identical, except that here f is shown explicitly as a function of $\mathbf {q}$ .

In general, the particle positions are not fixed and the measurement takes place over a finite exposure time and with a macroscopic sample (much larger than the interparticle distance). The experimentally accessible intensity is thus an averaged one $\textstyle \langle I(\mathbf {q} )\rangle$ ; we need not specify whether $\langle \cdot \rangle$ denotes a time or ensemble average. To take this into account we can rewrite Equation (**3**) as:

| $S(\mathbf {q} )={\frac {1}{N}}\left\langle \sum _{j=1}^{N}\sum _{k=1}^{N}\mathrm {e} ^{-i\mathbf {q} \cdot (\mathbf {R} _{j}-\mathbf {R} _{k})}\right\rangle .$ |   | 7 |
|---|---|---|

## Perfect crystals

In a crystal, the constitutive particles are arranged periodically, with translational symmetry forming a lattice. The crystal structure can be described as a Bravais lattice with a group of atoms, called the basis, placed at every lattice point; that is, [crystal structure] = [lattice] $\ast$ [basis]. If the lattice is infinite and completely regular, the system is a perfect crystal. For such a system, only a set of specific values for $\mathbf {q}$ can give scattering, and the scattering amplitude for all other values is zero. This set of values forms a lattice, called the reciprocal lattice, which is the Fourier transform of the real-space crystal lattice.

In principle the scattering factor $S(\mathbf {q} )$ can be used to determine the scattering from a perfect crystal; in the simple case when the basis is a single atom at the origin (and again neglecting all thermal motion, so that there is no need for averaging) all the atoms have identical environments. Equation (**1**) can be written as

$I(\mathbf {q} )=f^{2}\left|\sum _{j=1}^{N}\mathrm {e} ^{-i\mathbf {q} \cdot \mathbf {R} _{j}}\right|^{2}$

and

$S(\mathbf {q} )={\frac {1}{N}}\left|\sum _{j=1}^{N}\mathrm {e} ^{-i\mathbf {q} \cdot \mathbf {R} _{j}}\right|^{2}$

.

The structure factor is then simply the squared modulus of the Fourier transform of the lattice, and shows the directions in which scattering can have non-zero intensity. At these values of $\mathbf {q}$ the wave from every lattice point is in phase. The value of the structure factor is the same for all these reciprocal lattice points, and the intensity varies only due to changes in f with $\mathbf {q}$ .

### Units

The units of the structure-factor amplitude depend on the incident radiation. For X-ray crystallography they are multiples of the unit of scattering by a single electron (2.82 $\times 10^{-15}$ m); for neutron scattering by atomic nuclei the unit of scattering length of $10^{-14}$ m is commonly used.

The above discussion uses the wave vectors $|\mathbf {k} |=2\pi /\lambda$ and $|\mathbf {q} |=4\pi \sin \theta /\lambda$ . However, crystallography often uses wave vectors $|\mathbf {s} |=1/\lambda$ and $|\mathbf {g} |=2\sin \theta /\lambda$ . Therefore, when comparing equations from different sources, the factor $2\pi$ may appear and disappear, and care to maintain consistent quantities is required to get correct numerical results.

### Definition of *F**hkl*

In crystallography, the basis and lattice are treated separately. For a perfect crystal the lattice gives the reciprocal lattice, which determines the positions (angles) of diffracted beams, and the basis gives the structure factor $F_{hkl}$ which determines the amplitude and phase of the diffracted beams:

| $F_{hk\ell }=\sum _{j=1}^{N}f_{j}\mathrm {e} ^{[-2\pi i(hx_{j}+ky_{j}+\ell z_{j})]},$ |   | 8 |
|---|---|---|

where the sum is over all atoms in the unit cell, $x_{j},y_{j},z_{j}$ are the positional coordinates of the j -th atom, and $f_{j}$ is the scattering factor of the j -th atom. The coordinates $x_{j},y_{j},z_{j}$ have the directions and dimensions of the lattice vectors $\mathbf {a} ,\mathbf {b} ,\mathbf {c}$ . That is, (0,0,0) is at the lattice point, the origin of position in the unit cell; (1,0,0) is at the next lattice point along $\mathbf {a}$ and (1/2, 1/2, 1/2) is at the body center of the unit cell. $(hkl)$ defines a reciprocal lattice point at $(h\mathbf {a^{*}} ,k\mathbf {b^{*}} ,l\mathbf {c^{*}} )$ which corresponds to the real-space plane defined by the Miller indices $(hkl)$ (see Bragg's law).

$F_{hk\ell }$ is the vector sum of waves from all atoms within the unit cell. An atom at any lattice point has the reference phase angle zero for all $hk\ell$ since then $(hx_{j}+ky_{j}+\ell z_{j})$ is always an integer. A wave scattered from an atom at (1/2, 0, 0) will be in phase if h is even, out of phase if h is odd.

Again an alternative view using convolution can be helpful. Since [crystal structure] = [lattice] $\ast$ [basis], ${\mathcal {F}}$ [crystal structure] = ${\mathcal {F}}$ [lattice] $\times {\mathcal {F}}$ [basis]; that is, scattering $\propto$ [reciprocal lattice] $\times$ [structure factor].

### Examples of *F**hkl* in 3-D

#### Body-centered cubic (BCC)

For the body-centered cubic Bravais lattice (*cI*), we use the points $(0,0,0)$ and $({\tfrac {1}{2}},{\tfrac {1}{2}},{\tfrac {1}{2}})$ which leads us to

$F_{hk\ell }=\sum _{j}f_{j}e^{-2\pi i(hx_{j}+ky_{j}+\ell z_{j})}=f\left[1+\left(e^{-i\pi }\right)^{h+k+\ell }\right]=f\left[1+(-1)^{h+k+\ell }\right]$

and hence

$F_{hk\ell }={\begin{cases}2f,&h+k+\ell ={\text{even}}\\0,&h+k+\ell ={\text{odd}}\end{cases}}$

#### Face-centered cubic (FCC)

The FCC lattice is a Bravais lattice, and its Fourier transform is a body-centered cubic lattice. However to obtain $F_{hk\ell }$ without this shortcut, consider an FCC crystal with one atom at each lattice point as a primitive or simple cubic with a basis of 4 atoms, at the origin $x_{j},y_{j},z_{j}=(0,0,0)$ and at the three adjacent face centers, $x_{j},y_{j},z_{j}=\left({\frac {1}{2}},{\frac {1}{2}},0\right)$ , $\left(0,{\frac {1}{2}},{\frac {1}{2}}\right)$ and $\left({\frac {1}{2}},0,{\frac {1}{2}}\right)$ . Equation (**8**) becomes

$F_{hk\ell }=f\sum _{j=1}^{4}\mathrm {e} ^{[-2\pi i(hx_{j}+ky_{j}+\ell z_{j})]}=f\left[1+\mathrm {e} ^{[-i\pi (h+k)]}+\mathrm {e} ^{[-i\pi (k+\ell )]}+\mathrm {e} ^{[-i\pi (h+\ell )]}\right]=f\left[1+(-1)^{h+k}+(-1)^{k+\ell }+(-1)^{h+\ell }\right]$

with the result

$F_{hk\ell }={\begin{cases}4f,&h,k,\ell \ \ {\mbox{all even or all odd}}\\0,&h,k,\ell \ \ {\mbox{mixed parity}}\end{cases}}$

The most intense diffraction peak from a material that crystallizes in the FCC structure is typically the (111). Films of FCC materials like gold tend to grow in a (111) orientation with a triangular surface symmetry. A zero diffracted intensity for a group of diffracted beams (here, $h,k,\ell$ of mixed parity) is called a systematic absence.

#### Diamond crystal structure

The diamond cubic crystal structure occurs for example in diamond (carbon), tin, and most semiconductors. There are 8 atoms in the cubic unit cell. We can consider the structure as a simple cubic with a basis of 8 atoms, at positions

${\begin{aligned}x_{j},y_{j},z_{j}=&(0,\ 0,\ 0)&\left({\frac {1}{2}},\ {\frac {1}{2}},\ 0\right)\ &\left(0,\ {\frac {1}{2}},\ {\frac {1}{2}}\right)&\left({\frac {1}{2}},\ 0,\ {\frac {1}{2}}\right)\\&\left({\frac {1}{4}},\ {\frac {1}{4}},\ {\frac {1}{4}}\right)&\left({\frac {3}{4}},\ {\frac {3}{4}},\ {\frac {1}{4}}\right)\ &\left({\frac {1}{4}},\ {\frac {3}{4}},\ {\frac {3}{4}}\right)&\left({\frac {3}{4}},\ {\frac {1}{4}},\ {\frac {3}{4}}\right)\\\end{aligned}}$

But comparing this to the FCC above, we see that it is simpler to describe the structure as FCC with a basis of two atoms at (0, 0, 0) and (1/4, 1/4, 1/4). For this basis, Equation (**8**) becomes:

$F_{hk\ell }({\rm {{basis})=f\sum _{j=1}^{2}\mathrm {e} ^{[-2\pi i(hx_{j}+ky_{j}+\ell z_{j})]}=f\left[1+\mathrm {e} ^{[-i\pi /2(h+k+\ell )]}\right]=f\left[1+(-i)^{h+k+\ell }\right]}}$

And then the structure factor for the diamond cubic structure is the product of this and the structure factor for FCC above, (only including the atomic form factor once)

$F_{hk\ell }=f\left[1+(-1)^{h+k}+(-1)^{k+\ell }+(-1)^{h+\ell }\right]\times \left[1+(-i)^{h+k+\ell }\right]$

with the result

- If h, k, ℓ are of mixed parity (odd and even values combined) the first (FCC) term is zero, so $|F_{hk\ell }|^{2}=0$
- If h, k, ℓ are all even or all odd then the first (FCC) term is 4
  - if h+k+ℓ is odd then $F_{hk\ell }=4f(1\pm i),|F_{hk\ell }|^{2}=32f^{2}$
  - if h+k+ℓ is even and exactly divisible by 4 ( $h+k+\ell =4n$ ) then $F_{hk\ell }=4f\times 2,|F_{hk\ell }|^{2}=64f^{2}$
  - if h+k+ℓ is even but not exactly divisible by 4 ( $h+k+\ell \neq 4n$ ) the second term is zero and $|F_{hk\ell }|^{2}=0$

These points are encapsulated by the following equations:

$F_{hk\ell }={\begin{cases}8f,&h+k+\ell =4N\\4(1\pm i)f,&h+k+\ell =2N+1\\0,&h+k+\ell =4N+2\\\end{cases}}$

$\Rightarrow |F_{hk\ell }|^{2}={\begin{cases}64f^{2},&h+k+\ell =4N\\32f^{2},&h+k+\ell =2N+1\\0,&h+k+\ell =4N+2\\\end{cases}}$

where N is an integer.

#### Zincblende crystal structure

The zincblende structure is similar to the diamond structure except that it is a compound of two distinct interpenetrating fcc lattices, rather than all the same element. Denoting the two elements in the compound by A and B , the resulting structure factor is

$F_{hk\ell }={\begin{cases}4(f_{A}+f_{B}),&h+k+\ell =4N\\4(f_{A}\pm if_{B}),&h+k+\ell =2N+1\\4(f_{A}-f_{B}),&h+k+\ell =4N+2\\\end{cases}}$

#### Cesium chloride

Cesium chloride is a simple cubic crystal lattice with a basis of Cs at (0,0,0) and Cl at (1/2, 1/2, 1/2) (or the other way around, it makes no difference). Equation (**8**) becomes

$F_{hk\ell }=\sum _{j=1}^{2}f_{j}\mathrm {e} ^{[-2\pi i(hx_{j}+ky_{j}+\ell z_{j})]}=\left[f_{Cs}+f_{Cl}\mathrm {e} ^{[-i\pi (h+k+\ell )]}\right]=\left[f_{Cs}+f_{Cl}(-1)^{h+k+\ell }\right]$

We then arrive at the following result for the structure factor for scattering from a plane $(hk\ell )$ :

$F_{hk\ell }={\begin{cases}(f_{Cs}+f_{Cl}),&h+k+\ell &{\text{even}}\\(f_{Cs}-f_{Cl}),&h+k+\ell &{\text{odd}}\end{cases}}$

and for scattered intensity, $|F_{hk\ell }|^{2}={\begin{cases}(f_{Cs}+f_{Cl})^{2},&h+k+\ell &{\text{even}}\\(f_{Cs}-f_{Cl})^{2},&h+k+\ell &{\text{odd}}\end{cases}}$

#### Hexagonal close-packed (HCP)

In an HCP crystal such as graphite, the two coordinates include the origin $\left(0,0,0\right)$ and the next plane up the *c* axis located at *c*/2, and hence $\left(1/3,2/3,1/2\right)$ , which gives us

$F_{hk\ell }=f\left[1+e^{2\pi i\left({\tfrac {h}{3}}+{\tfrac {2k}{3}}+{\tfrac {\ell }{2}}\right)}\right]$

From this it is convenient to define dummy variable $X\equiv h/3+2k/3+\ell /2$ , and from there consider the modulus squared so hence

$|F|^{2}=f^{2}\left(1+e^{2\pi iX}\right)\left(1+e^{-2\pi iX}\right)=f^{2}\left(2+e^{2\pi iX}+e^{-2\pi iX}\right)=f^{2}\left(2+2\cos[2\pi X]\right)=f^{2}\left(4\cos ^{2}\left[\pi X\right]\right)$

This leads us to the following conditions for the structure factor:

$|F_{hk\ell }|^{2}={\begin{cases}0,&h+2k=3N{\text{ and }}\ell {\text{ is odd,}}\\4f^{2},&h+2k=3N{\text{ and }}\ell {\text{ is even,}}\\3f^{2},&h+2k=3N\pm 1{\text{ and }}\ell {\text{ is odd,}}\\f^{2},&h+2k=3N\pm 1{\text{ and }}\ell {\text{ is even}}\\\end{cases}}$

### Perfect crystals in one and two dimensions

The reciprocal lattice is easily constructed in one dimension: for particles on a line with a period a , the reciprocal lattice is an infinite array of points with spacing $2\pi /a$ . In two dimensions, there are only five Bravais lattices. The corresponding reciprocal lattices have the same symmetry as the direct lattice. 2-D lattices are excellent for demonstrating simple diffraction geometry on a flat screen, as below. Equations (1)–(7) for structure factor $S(\mathbf {q} )$ apply with a scattering vector of limited dimensionality and a crystallographic structure factor can be defined in 2-D as $F_{hk}=\sum _{j=1}^{N}f_{j}\mathrm {e} ^{[-2\pi i(hx_{j}+ky_{j})]}$ .

However, recall that real 2-D crystals such as graphene exist in 3-D. The reciprocal lattice of a 2-D hexagonal sheet that exists in 3-D space in the $xy$ plane is a hexagonal array of lines parallel to the z or $z^{*}$ axis that extend to $\pm \infty$ and intersect any plane of constant z in a hexagonal array of points.

The Figure shows the construction of one vector of a 2-D reciprocal lattice and its relation to a scattering experiment.

A parallel beam, with wave vector $\mathbf {k} _{i}$ is incident on a square lattice of parameter a . The scattered wave is detected at a certain angle, which defines the wave vector of the outgoing beam, $\mathbf {k} _{o}$ (under the assumption of elastic scattering, $|\mathbf {k} _{o}|=|\mathbf {k} _{i}|$ ). One can equally define the scattering vector $\mathbf {q} =\mathbf {k} _{o}-\mathbf {k} _{i}$ and construct the harmonic pattern $\exp(i\mathbf {q} \mathbf {r} )$ . In the depicted example, the spacing of this pattern coincides to the distance between particle rows: $q=2\pi /a$ , so that contributions to the scattering from all particles are in phase (constructive interference). Thus, the total signal in direction $\mathbf {k} _{o}$ is strong, and $\mathbf {q}$ belongs to the reciprocal lattice. It is easily shown that this configuration fulfills Bragg's law.

## Imperfect crystals

Technically a perfect crystal must be infinite, so a finite size is an imperfection. Real crystals always exhibit imperfections of their order besides their finite size, and these imperfections can have profound effects on the properties of the material. André Guinier proposed a widely employed distinction between imperfections that preserve the long-range order of the crystal that he called *disorder of the first kind* and those that destroy it called *disorder of the second kind*. An example of the first is thermal vibration; an example of the second is some density of dislocations.

The generally applicable structure factor $S(\mathbf {q} )$ can be used to include the effect of any imperfection. In crystallography, these effects are treated as separate from the structure factor $F_{hkl}$ , so separate factors for size or thermal effects are introduced into the expressions for scattered intensity, leaving the perfect crystal structure factor unchanged. Therefore, a detailed description of these factors in crystallographic structure modeling and structure determination by diffraction is not appropriate in this article.

### Finite-size effects

For $S(q)$ a finite crystal means that the sums in equations 1-7 are now over a finite N . The effect is most easily demonstrated with a 1-D lattice of points. The sum of the phase factors is a geometric series and the structure factor becomes:

$S(q)={\frac {1}{N}}\left|{\frac {1-\mathrm {e} ^{-iNqa}}{1-\mathrm {e} ^{-iqa}}}\right|^{2}={\frac {1}{N}}\left[{\frac {\sin(Nqa/2)}{\sin(qa/2)}}\right]^{2}.$

This function is shown in the Figure for different values of N . When the scattering from every particle is in phase, which is when the scattering is at a reciprocal lattice point $q=2k\pi /a$ , the sum of the amplitudes must be $\propto N$ and so the maxima in intensity are $\propto N^{2}$ . Taking the above expression for $S(q)$ and estimating the limit $S(q\to 0)$ using, for instance, L'Hôpital's rule) shows that $S(q=2k\pi /a)=N$ as seen in the Figure. At the midpoint $S(q=(2k+1)\pi /a)=1/N$ (by direct evaluation) and the peak width decreases like $1/N$ . In the large N limit, the peaks become infinitely sharp Dirac delta functions, the reciprocal lattice of the perfect 1-D lattice.

In crystallography when $F_{hkl}$ is used, N is large, and the formal size effect on diffraction is taken as $\left[{\frac {\sin(Nqa/2)}{(qa/2)}}\right]^{2}$ , which is the same as the expression for $S(q)$ above near to the reciprocal lattice points, $q\approx 2k\pi /a$ . Using convolution, we can describe the finite real crystal structure as [lattice] $\ast$ [basis] $\times$ rectangular function, where the rectangular function has a value 1 inside the crystal and 0 outside it. Then ${\mathcal {F}}$ [crystal structure] = ${\mathcal {F}}$ [lattice] $\times {\mathcal {F}}$ [basis] $\ast {F}$ [rectangular function]; that is, scattering $\propto$ [reciprocal lattice] $\times$ [structure factor] $\ast$ [ sinc function]. Thus the intensity, which is a delta function of position for the perfect crystal, becomes a ${\textstyle \operatorname {sinc} ^{2}}$ function around every point with a maximum $\propto N^{2}$ , a width $\propto 1/N$ , area $\propto N$ .

### Disorder of the first kind

This model for disorder in a crystal starts with the structure factor of a perfect crystal. In one-dimension for simplicity and with *N* planes, we then start with the expression above for a perfect finite lattice, and then this disorder only changes $S(q)$ by a multiplicative factor, to give

$S(q)={\frac {1}{N}}\left[{\frac {\sin(Nqa/2)}{\sin(qa/2)}}\right]^{2}\exp \left(-q^{2}\langle \delta x^{2}\rangle \right)$

where the disorder is measured by the mean-square displacement of the positions $x_{j}$ from their positions in a perfect one-dimensional lattice: $a(j-(N-1)/2)$ , i.e., $x_{j}=a(j-(N-1)/2)+\delta x$ , where $\delta x$ is a small (much less than a ) random displacement. For disorder of the first kind, each random displacement $\delta x$ is independent of the others, and with respect to a perfect lattice. Thus the displacements $\delta x$ do not destroy the translational order of the crystal. This has the consequence that for infinite crystals ( $N\to \infty$ ) the structure factor still has delta-function Bragg peaks – the peak width still goes to zero as $N\to \infty$ , with this kind of disorder. However, it does reduce the amplitude of the peaks, and due to the factor of $q^{2}$ in the exponential factor, it reduces peaks at large q much more than peaks at small q .

The structure is simply reduced by a q and disorder dependent term because all disorder of the first-kind does is smear out the scattering planes, effectively reducing the form factor.

In three dimensions the effect is the same, the structure is again reduced by a multiplicative factor, and this factor is often called the Debye–Waller factor. Note that the Debye–Waller factor is often ascribed to thermal motion, i.e., the $\delta x$ are due to thermal motion, but any random displacements about a perfect lattice, not just thermal ones, will contribute to the Debye–Waller factor.

### Disorder of the second kind

However, fluctuations that cause the correlations between pairs of atoms to decrease as their separation increases, causes the Bragg peaks in the structure factor of a crystal to broaden. To see how this works, we consider a one-dimensional toy model: a stack of plates with mean spacing a . The derivation follows that in chapter 9 of Guinier's textbook. This model has been pioneered by and applied to a number of materials by Hosemann and collaborators over a number of years. Guinier and they termed this disorder of the second kind, and Hosemann in particular referred to this imperfect crystalline ordering as paracrystalline ordering. Disorder of the first kind is the source of the Debye–Waller factor.

To derive the model we start with the definition (in one dimension) of the

$S(q)={\frac {1}{N}}\sum _{j,k=1}^{N}\mathrm {e} ^{-iq(x_{j}-x_{k})}$

To start with we will consider, for simplicity an infinite crystal, i.e., $N\to \infty$ . We will consider a finite crystal with disorder of the second-type below.

For our infinite crystal, we want to consider pairs of lattice sites. For large each plane of an infinite crystal, there are two neighbours m planes away, so the above double sum becomes a single sum over pairs of neighbours either side of an atom, at positions $-m$ and m lattice spacings away, times N . So, then

$S(q)=1+2\sum _{m=1}^{\infty }\int _{-\infty }^{\infty }{\rm {d}}(\Delta x)p_{m}(\Delta x)\cos \left(q\Delta x\right)$

where $p_{m}(\Delta x)$ is the probability density function for the separation $\Delta x$ of a pair of planes, m lattice spacings apart. For the separation of neighbouring planes we assume for simplicity that the fluctuations around the mean neighbour spacing of *a* are Gaussian, i.e., that

$p_{1}(\Delta x)={\frac {1}{\left(2\pi \sigma _{2}^{2}\right)^{1/2}}}\exp \left[-\left(\Delta x-a\right)^{2}/(2\sigma _{2}^{2})\right]$

and we also assume that the fluctuations between a plane and its neighbour, and between this neighbour and the next plane, are independent. Then $p_{2}(\Delta x)$ is just the convolution of two $p_{1}(\Delta x)$ s, etc. As the convolution of two Gaussians is just another Gaussian, we have that

$p_{m}(\Delta x)={\frac {1}{\left(2\pi m\sigma _{2}^{2}\right)^{1/2}}}\exp \left[-\left(\Delta x-ma\right)^{2}/(2m\sigma _{2}^{2})\right]$

The sum in $S(q)$ is then just a sum of Fourier transforms of Gaussians, and so

$S(q)=1+2\sum _{m=1}^{\infty }r^{m}\cos \left(mqa\right)$

for $r=\exp[-q^{2}\sigma _{2}^{2}/2]$ . The sum is just the real part of the sum $\sum _{m=1}^{\infty }[r\exp(iqa)]^{m}$ and so the structure factor of the infinite but disordered crystal is

$S(q)={\frac {1-r^{2}}{1+r^{2}-2r\cos(qa)}}$

This has peaks at maxima $q_{p}=2n\pi /a$ , where $\cos(q_{P}a)=1$ . These peaks have heights

$S(q_{P})={\frac {1+r}{1-r}}\approx {\frac {4}{q_{P}^{2}\sigma _{2}^{2}}}={\frac {a^{2}}{n^{2}\pi ^{2}\sigma _{2}^{2}}}$

i.e., the height of successive peaks drop off as the order of the peak (and so q ) squared. Unlike finite-size effects that broaden peaks but do not decrease their height, disorder lowers peak heights. Note that here we assuming that the disorder is relatively weak, so that we still have relatively well defined peaks. This is the limit $q\sigma _{2}\ll 1$ , where $r\simeq 1-q^{2}\sigma _{2}^{2}/2$ . In this limit, near a peak we can approximate $\cos(qa)\simeq 1-(\Delta q)^{2}a^{2}/2$ , with $\Delta q=q-q_{P}$ and obtain

$S(q)\approx {\frac {S(q_{P})}{1+{\frac {r}{(1-r)^{2}}}{\frac {\Delta q^{2}a^{2}}{2}}}}\approx {\frac {S(q_{P})}{1+{\frac {\Delta q^{2}}{[q_{P}^{2}\sigma _{2}^{2}/a]^{2}/2}}}}$

which is a Lorentzian or Cauchy function, of FWHM $q_{P}^{2}\sigma _{2}^{2}/a=4\pi ^{2}n^{2}(\sigma _{2}/a)^{2}/a$ , i.e., the FWHM increases as the square of the order of peak, and so as the square of the wave vector q at the peak.

Finally, the product of the peak height and the FWHM is constant and equals $4/a$ , in the $q\sigma _{2}\ll 1$ limit. For the first few peaks where n is not large, this is just the $\sigma _{2}/a\ll 1$ limit.

#### Finite crystals with disorder of the second kind

For a one-dimensional crystal of size N

$S(q)=1+2\sum _{m=1}^{N}\left(1-{\frac {m}{N}}\right)r^{m}\cos \left(mqa\right)$

where the factor in parentheses comes from the fact the sum is over nearest-neighbour pairs ( $m=1$ ), next nearest-neighbours ( $m=2$ ), ... and for a crystal of N planes, there are $N-1$ pairs of nearest neighbours, $N-2$ pairs of next-nearest neighbours, etc.

## Liquids

In contrast with crystals, liquids have no long-range order (in particular, there is no regular lattice), so the structure factor does not exhibit sharp peaks. They do however show a certain degree of short-range order, depending on their density and on the strength of the interaction between particles. Liquids are isotropic, so that, after the averaging operation in Equation (**4**), the structure factor only depends on the absolute magnitude of the scattering vector $q=\left|\mathbf {q} \right|$ . For further evaluation, it is convenient to separate the diagonal terms $j=k$ in the double sum, whose phase is identically zero, and therefore each contribute a unit constant:

| $S(q)=1+{\frac {1}{N}}\left\langle \sum _{j\neq k}\mathrm {e} ^{-i\mathbf {q} (\mathbf {R} _{j}-\mathbf {R} _{k})}\right\rangle$ . |   | 9 |
|---|---|---|

One can obtain an alternative expression for $S(q)$ in terms of the radial distribution function $g(r)$ :

| $S(q)=1+\rho \int _{V}\mathrm {d} \mathbf {r} \,[g(r)-1]\mathrm {e} ^{-i\mathbf {q} \mathbf {r} }$ . |   | 10 |
|---|---|---|

### Ideal gas

In the limiting case of no interaction, the system is an ideal gas and the structure factor is completely featureless: $S(q)=1$ , because there is no correlation between the positions $\mathbf {R} _{j}$ and $\mathbf {R} _{k}$ of different particles (they are independent random variables), so the off-diagonal terms in Equation (**9**) average to zero: $\langle \exp[-i\mathbf {q} (\mathbf {R} _{j}-\mathbf {R} _{k})]\rangle =\langle \exp(-i\mathbf {q} \mathbf {R} _{j})\rangle \langle \exp(i\mathbf {q} \mathbf {R} _{k})\rangle =0$ .

### High-*q* limit

Even for interacting particles, at high scattering vector the structure factor goes to 1. This result follows from Equation (**10**), since $S(q)-1$ is the Fourier transform of the "regular" function $g(r)$ and thus goes to zero for high values of the argument q . This reasoning does not hold for a perfect crystal, where the distribution function exhibits infinitely sharp peaks.

### Low-*q* limit

In the low- q limit, as the system is probed over large length scales, the structure factor contains thermodynamic information, being related to the isothermal compressibility $\chi _{T}$ of the liquid by the compressibility equation:

$\lim _{q\rightarrow 0}S(q)=\rho \,k_{\mathrm {B} }T\,\chi _{T}=k_{\mathrm {B} }T\left({\frac {\partial \rho }{\partial p}}\right)$

.

### Hard-sphere liquids

In the hard sphere model, the particles are described as impenetrable spheres with radius R ; thus, their center-to-center distance $r\geq 2R$ and they experience no interaction beyond this distance. Their interaction potential can be written as:

$V(r)={\begin{cases}\infty &{\text{for }}r<2R,\\0&{\text{for }}r\geq 2R.\end{cases}}$

This model has an analytical solution in the Percus–Yevick approximation. Although highly simplified, it provides a good description for systems ranging from liquid metals to colloidal suspensions. In an illustration, the structure factor for a hard-sphere fluid is shown in the Figure, for volume fractions $\Phi$ from 1% to 40%.

## Polymers

In polymer systems, the general definition (**4**) holds; the elementary constituents are now the monomers making up the chains. However, the structure factor being a measure of the correlation between particle positions, one can reasonably expect that this correlation will be different for monomers belonging to the same chain or to different chains.

Let us assume that the volume V contains $N_{c}$ identical molecules, each composed of $N_{p}$ monomers, such that $N_{c}N_{p}=N$ ( $N_{p}$ is also known as the degree of polymerization). We can rewrite (**4**) as:

| $S(\mathbf {q} )={\frac {1}{N_{c}N_{p}}}\left\langle \sum _{\alpha \beta =1}^{N_{c}}\sum _{jk=1}^{N_{p}}\mathrm {e} ^{-i\mathbf {q} (\mathbf {R} _{\alpha j}-\mathbf {R} _{\beta k})}\right\rangle ={\frac {1}{N_{c}N_{p}}}\left\langle \sum _{\alpha =1}^{N_{c}}\sum _{jk=1}^{N_{p}}\mathrm {e} ^{-i\mathbf {q} (\mathbf {R} _{\alpha j}-\mathbf {R} _{\alpha k})}\right\rangle +{\frac {1}{N_{c}N_{p}}}\left\langle \sum _{\alpha \neq \beta =1}^{N_{c}}\sum _{jk=1}^{N_{p}}\mathrm {e} ^{-i\mathbf {q} (\mathbf {R} _{\alpha j}-\mathbf {R} _{\beta k})}\right\rangle$ , |   | 11 |
|---|---|---|

where indices $\alpha ,\beta$ label the different molecules and $j,k$ the different monomers along each molecule. On the right-hand side we separated *intramolecular* ( $\alpha =\beta$ ) and *intermolecular* ( $\alpha \neq \beta$ ) terms. Using the equivalence of the chains, (**11**) can be simplified:

| $S(\mathbf {q} )=\underbrace {{\frac {1}{N_{p}}}\left\langle \sum _{jk=1}^{N_{p}}\mathrm {e} ^{-i\mathbf {q} (\mathbf {R} _{j}-\mathbf {R} _{k})}\right\rangle } _{S_{1}(q)}+{\frac {N_{c}-1}{N_{p}}}\left\langle \sum _{jk=1}^{N_{p}}\mathrm {e} ^{-i\mathbf {q} (\mathbf {R} _{1j}-\mathbf {R} _{2k})}\right\rangle$ , |   | 12 |
|---|---|---|

where $S_{1}(q)$ is the single-chain structure factor.
