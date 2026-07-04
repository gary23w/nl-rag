---
title: "Acoustoelastic effect"
source: https://en.wikipedia.org/wiki/Acoustoelastic_effect
domain: exhaust-system
license: CC-BY-SA-4.0
tags: exhaust system
fetched: 2026-07-04
---

# Acoustoelastic effect

The **acoustoelastic effect** is how the sound velocities (both longitudinal and shear wave velocities) of an elastic material change if subjected to an initial static stress field. This is a non-linear effect of the constitutive relation between mechanical stress and finite strain in a material of continuous mass. In classical linear elasticity theory small deformations of most elastic materials can be described by a linear relation between the applied stress and the resulting strain. This relationship is commonly known as the generalised Hooke's law. The linear elastic theory involves second order elastic constants (e.g. $\lambda$ and $\mu$ ) and yields constant longitudinal and shear sound velocities in an elastic material, not affected by an applied stress. The acoustoelastic effect on the other hand include higher order expansion of the constitutive relation (non-linear elasticity theory) between the applied stress and resulting strain, which yields longitudinal and shear sound velocities dependent of the stress state of the material. In the limit of an unstressed material the sound velocities of the linear elastic theory are reproduced.

The acoustoelastic effect was investigated as early as 1925 by Brillouin. He found that the propagation velocity of acoustic waves would decrease proportional to an applied hydrostatic pressure. However, a consequence of his theory was that sound waves would stop propagating at a sufficiently large pressure. This paradoxical effect was later shown to be caused by the incorrect assumptions that the elastic parameters were not affected by the pressure.

In 1937 Francis Dominic Murnaghan presented a mathematical theory extending the linear elastic theory to also include finite deformation in elastic isotropic materials. This theory included three third-order elastic constants l , m , and n . In 1953 Huges and Kelly used the theory of Murnaghan in their experimental work to establish numerical values for higher order elastic constants for several elastic materials including Polystyrene, Armco iron, and Pyrex, subjected to hydrostatic pressure and uniaxial compression.

## Non-linear elastic theory for hyperelastic materials

The acoustoelastic effect is an effect of finite deformation of non-linear elastic materials. A modern comprehensive account of this can be found in. This book treats the application of the non-linear elasticity theory and the analysis of the mechanical properties of solid materials capable of large elastic deformations. The special case of the acoustoelastic theory for a compressible isotropic hyperelastic material, like polycrystalline steel, is reproduced and shown in this text from the non-linear elasticity theory as presented by Ogden.

Note

that the setting in this text as well as in

is

isothermal

, and no reference is made to

thermodynamics

.

### Constitutive relation – hyperelastic materials (Stress-strain relation)

A hyperelastic material is a special case of a Cauchy elastic material in which the stress at any point is objective and determined only by the current state of deformation with respect to an arbitrary reference configuration (for more details on deformation see also the pages Deformation (mechanics) and Finite strain). However, the work done by the stresses may depend on the path the deformation takes. Therefore, a Cauchy elastic material has a non-conservative structure, and the stress cannot be derived from a scalar elastic potential function. The special case of Cauchy elastic materials where the work done by the stresses is independent of the path of deformation is referred to as a Green elastic or hyperelastic material. Such materials are conservative and the stresses in the material can be derived by a scalar elastic potential, more commonly known as the Strain energy density function.

The constitutive relation between the stress and strain can be expressed in different forms based on the chosen stress and strain forms. Selecting the 1st Piola-Kirchhoff stress tensor ${\boldsymbol {P}}$ (which is the transpose of the nominal stress tensor ${\boldsymbol {P}}^{T}={\boldsymbol {N}}$ ), the constitutive equation for a compressible hyper elastic material can be expressed in terms of the Lagrangian Green strain ( ${\boldsymbol {E}}$ ) as: ${\boldsymbol {P}}={\boldsymbol {F}}\cdot {\frac {\partial W}{\partial {\boldsymbol {E}}}}\qquad {\text{or}}\qquad P_{ij}=F_{ik}~{\frac {\partial W}{\partial E_{kj}}},\qquad i,j=1,2,3~,$ where ${\boldsymbol {F}}$ is the deformation gradient tensor, and where the second expression uses the Einstein summation convention for index notation of tensors. W is the strain energy density function for a hyperelastic material and have been defined per unit volume rather than per unit mass since this avoids the need of multiplying the right hand side with the mass density $\rho _{0}$ of the reference configuration.

Assuming that the scalar strain energy density function $W({\boldsymbol {E}})$ can be approximated by a Taylor series expansion in the current strain ${\boldsymbol {E}}$ , it can be expressed (in index notation) as: $W\approx C_{0}+C_{ij}E_{ij}+{\frac {1}{2!}}C_{ijkl}E_{ij}E_{kl}+{\frac {1}{3!}}C_{ijklmn}E_{ij}E_{kl}E_{mn}+\cdots$ Imposing the restrictions that the strain energy function should be zero and have a minimum when the material is in the un-deformed state (i.e. $W(E_{ij}=0)=0$ ) it is clear that there are no constant or linear term in the strain energy function, and thus: $W\approx {\frac {1}{2!}}C_{ijkl}E_{ij}E_{kl}+{\frac {1}{3!}}C_{ijklmn}E_{ij}E_{kl}E_{mn}+\cdots ,$ where $C_{ijkl}$ is a fourth-order tensor of second-order elastic moduli, while $C_{ijklmn}$ is a sixth-order tensor of third-order elastic moduli. The symmetry of $E_{ij}=E_{ji}$ together with the scalar strain energy density function W implies that the second order moduli $C_{ijkl}$ have the following symmetry: $C_{ijkl}=C_{jikl}=C_{ijlk},$ which reduce the number of independent elastic constants from 81 to 36. In addition the power expansion implies that the second order moduli also have the major symmetry $C_{ijkl}=C_{klij},$ which further reduce the number of independent elastic constants to 21. The same arguments can be used for the third order elastic moduli $C_{ijklmn}$ . These symmetries also allows the elastic moduli to be expressed by the Voigt notation (i.e. $C_{ijkl}=C_{IJ}$ and $C_{ijklmn}=C_{IJK}$ ).

The deformation gradient tensor can be expressed in component form as $F_{ij}={\frac {\partial u_{i}}{\partial X_{j}}}+\delta _{ij},$ where $u_{i}$ is the displacement of a material point P from coordinate $X_{i}$ in the reference configuration to coordinate $x_{i}$ in the deformed configuration (see Figure 2 in the finite strain theory page). Including the power expansion of strain energy function in the constitutive relation and replacing the Lagrangian strain tensor $E_{kl}$ with the expansion given on the finite strain tensor page yields (note that lower case u have been used in this section compared to the upper case on the finite strain page) the **constitutive equation** $P_{ij}=C_{ijkl}{\frac {\partial u_{k}}{\partial X_{l}}}+{\frac {1}{2}}M_{ijklmn}{\frac {\partial u_{k}}{\partial X_{l}}}{\frac {\partial u_{m}}{\partial X_{n}}}+{\frac {1}{3}}M_{ijklmnpq}{\frac {\partial u_{k}}{\partial X_{l}}}{\frac {\partial u_{m}}{\partial X_{n}}}{\frac {\partial u_{p}}{\partial X_{q}}}+\cdots ,$ where $M_{ijklmn}=C_{ijklmn}+C_{ijln}\delta _{km}+C_{jnkl}\delta _{im}+C_{jlmn}\delta _{ik},$ and higher order terms have been neglected (see for detailed derivations). For referenceM by neglecting higher order terms in $\partial u_{k}/\partial X_{l}$ this expression reduce to $P_{ij}=C_{ijkl}{\frac {\partial u_{k}}{\partial X_{l}}},$ which is a version of the generalised Hooke's law where $P_{ij}$ is a measure of stress while $\partial u_{k}/\partial X_{l}$ is a measure of strain, and $C_{ijkl}$ is the linear relation between them.

### Sound velocity

Assuming that a small dynamic (acoustic) deformation disturb an already statically stressed material the acoustoelastic effect can be regarded as the effect on a small deformation superposed on a larger finite deformation (also called the small-on-large theory). Let us define three states of a given material point. In the reference (un-stressed) state the point is defined by the coordinate vector ${\boldsymbol {X}}$ while the same point has the coordinate vector ${\boldsymbol {x}}$ in the static initially stressed state (i.e. under the influence of an applied pre-stress). Finally, assume that the material point under a small dynamic disturbance (acoustic stress field) have the coordinate vector ${\boldsymbol {x'}}$ . The total displacement of the material points (under influence of both a static pre-stress and a dynamic acoustic disturbance) can then be described by the displacement vectors ${\boldsymbol {u}}={\boldsymbol {u}}^{(0)}+{\boldsymbol {u}}^{(1)}={\boldsymbol {x'}}-{\boldsymbol {X}},$ where ${\boldsymbol {u}}^{(0)}={\boldsymbol {x}}-{\boldsymbol {X}},\qquad {\boldsymbol {u}}^{(1)}={\boldsymbol {x'}}-{\boldsymbol {x}}$ describes the static (Lagrangian) initial displacement due to the applied pre-stress, and the (Eulerian) displacement due to the acoustic disturbance, respectively. Cauchy's first law of motion (or balance of linear momentum) for the additional Eulerian disturbance ${\boldsymbol {u}}^{(1)}$ can then be derived in terms of the intermediate Lagrangian deformation ${\boldsymbol {u}}^{(0)}$ assuming that the small-on-large assumption $|{\boldsymbol {u}}^{(1)}|\ll |{\boldsymbol {u}}^{(0)}|$ holds. Using the Lagrangian form of Cauchy's first law of motion, where the effect of a constant body force (i.e. gravity) has been neglected, yields $\operatorname {Div} {\boldsymbol {P}}=\rho _{0}{\ddot {{\boldsymbol {x}}'}}.$

Note

that the subscript/superscript "0" is used in this text to denote the un-stressed reference state, and a dotted variable is as usual the

time (

t

) derivative

of the variable, and

$\operatorname {Div}$

is the

divergence

operator with respect to the Lagrangian coordinate system

${\boldsymbol {X}}$

.

The **right hand side** (the time dependent part) of the law of motion can be expressed as ${\begin{aligned}\rho _{0}{\ddot {{\boldsymbol {x}}'}}&=\rho _{0}{\frac {\partial ^{2}}{\partial t^{2}}}({\boldsymbol {u}}^{(0)}+{\boldsymbol {u}}^{(1)}+{\boldsymbol {X}})\\&=\rho _{0}{\frac {\partial ^{2}{\boldsymbol {u}}^{(1)}}{\partial t^{2}}}\end{aligned}}$ under the assumption that both the unstressed state and the initial deformation state are static and thus ${\textstyle \partial ^{2}{\boldsymbol {u}}^{(0)}/\partial t^{2}=\partial ^{2}{\boldsymbol {X}}/\partial t^{2}=0}$ .

For the **left hand side** (the space dependent part) the spatial Lagrangian partial derivatives with respect to $X_{j}$ can be expanded in the Eulerian $x_{j}$ by using the chain rule and changing the variables through the relation between the displacement vectors as ${\frac {\partial }{\partial X_{j}}}={\frac {\partial }{\partial x_{j}}}+u_{k,j}^{(0)}{\frac {\partial }{\partial x_{k}}}+\cdots$ where the short form $u_{k,j}^{(0)}\equiv \partial u_{k}^{(0)}/\partial x_{j}$ has been used. Thus ${\frac {\partial P_{ij}}{\partial X_{j}}}\approx {\frac {\partial P_{ij}}{\partial x_{j}}}+u_{p.j}^{(0)}{\frac {\partial P_{ij}}{\partial x_{p}}}$ Assuming further that the static initial deformation ${\boldsymbol {u}}^{(0)}$ (the pre-stressed state) is in equilibrium means that $\operatorname {Div} {\boldsymbol {P}}^{(0)}={\boldsymbol {0}}$ , and the law of motion can in combination with the constitutive equation given above be reduced to a linear relation (i.e. where higher order terms in $u_{m,n}^{(0)}$ ) between the static initial deformation ${\boldsymbol {u}}^{(0)}$ and the additional dynamic disturbance ${\boldsymbol {u}}^{(1)}({\boldsymbol {x}},t)$ as (see for detailed derivations) $B_{ijkl}{\frac {\partial ^{2}u_{k}^{(1)}}{\partial x_{j}\partial x_{l}}}=\rho _{0}{\frac {\partial ^{2}u_{i}^{(1)}}{\partial t^{2}}},$ where $B_{ijkl}=C_{ijkl}+\delta _{ik}C_{jlqr}u_{q,r}^{(0)}+C_{rjkl}u_{i,r}^{(0)}+C_{irkl}u_{j,r}^{(0)}+C_{ijrl}u_{k,r}^{(0)}+C_{ijkr}u_{l,r}^{(0)}+C_{ijklmn}u_{m,n}^{(0)}.$ This expression is recognised as the linear wave equation. Considering a plane wave of the form ${\boldsymbol {u}}^{(1)}({\boldsymbol {x}},t)={\boldsymbol {m}}\,f({\boldsymbol {N}}\cdot {\boldsymbol {x}}-ct),$ where ${\boldsymbol {N}}$ is a Lagrangian unit vector in the direction of propagation (i.e., parallel to the wave number ${\boldsymbol {k}}=k{\boldsymbol {N}}$ normal to the wave front), ${\boldsymbol {m}}$ is a unit vector referred to as the polarization vector (describing the direction of particle motion), c is the phase wave speed, and f is a twice continuously differentiable function (e.g. a sinusoidal function). Inserting this plane wave in to the linear wave equation derived above yields ${\boldsymbol {Q}}({\boldsymbol {N}}){\boldsymbol {m}}=\rho _{0}c^{2}{\boldsymbol {m}}$ where ${\boldsymbol {Q}}({\boldsymbol {N}})$ is introduced as the acoustic tensor, and depends on ${\boldsymbol {N}}$ as $[{\boldsymbol {Q}}({\boldsymbol {N}})]_{ik}=B_{ijkl}N_{j}N_{l}.$ This expression is called the propagation condition and determines for a given propagation direction ${\boldsymbol {n}}$ the velocity and polarization of possible waves corresponding to plane waves. The wave velocities can be determined by the characteristic equation $\det({\boldsymbol {Q}}({\boldsymbol {N}})-\rho _{0}c^{2}{\boldsymbol {I}})=0,$ where $\det$ is the determinant and ${\boldsymbol {I}}$ is the identity matrix.

For a hyperelastic material ${\boldsymbol {Q}}({\boldsymbol {N}})$ is symmetric (but not in general), and the eigenvalues ( $\rho _{0}c^{2}$ ) are thus real. For the wave velocities to also be real the eigenvalues need to be positive. If this is the case, three mutually orthogonal real plane waves exist for the given propagation direction ${\boldsymbol {N}}$ . From the two expressions of the acoustic tensor it is clear that $\rho _{0}c^{2}={\boldsymbol {Q}}({\boldsymbol {N}}){\boldsymbol {m}}\cdot {\boldsymbol {m}}=B_{ijkl}N_{j}N_{l}m_{i}m_{k},$ and the inequality $B_{ijkl}N_{j}N_{l}m_{i}m_{k}>0$ (also called the strong ellipticity condition) for all non-zero vectors ${\boldsymbol {N}}$ and ${\boldsymbol {m}}$ guarantee that the velocity of homogeneous plane waves are real. The polarization ${\boldsymbol {m}}={\boldsymbol {N}}$ corresponds to a longitudinal wave where the particle motion is parallel to the propagation direction (also referred to as a compressional wave). The two polarizations where ${\boldsymbol {m}}\cdot {\boldsymbol {N}}=0$ corresponds to transverse waves where the particle motion is orthogonal to the propagation direction (also referred to as shear waves).

## Isotropic materials

### Elastic moduli for isotropic materials

For a second order isotropic tensor (i.e. a tensor having the same components in any coordinate system) like the Lagrangian strain tensor ${\boldsymbol {E}}$ have the invariants $\operatorname {tr} {\boldsymbol {E}}^{q}$ where $\operatorname {tr}$ is the trace operator, and $q\in \left\{1,2,3,\dots \right\}$ . The strain energy function of an isotropic material can thus be expressed by $W({\boldsymbol {E}})=W(\operatorname {tr} {\boldsymbol {E}}^{q}),\,k\in \left\{1,2,3,\ldots \right\}$ , or a superposition there of, which can be rewritten as $W={\frac {\lambda }{2}}(\operatorname {tr} {\boldsymbol {E}})^{2}+\mu \operatorname {tr} {\boldsymbol {E}}^{2}+{\frac {C}{3}}(\operatorname {tr} {\boldsymbol {E}})^{3}+B(\operatorname {tr} {\boldsymbol {E}})\operatorname {tr} {\boldsymbol {E}}^{2}+{\frac {A}{3}}\operatorname {tr} {\boldsymbol {E}}^{3}+\cdots ,$ where $\lambda ,\mu ,A,B,C$ are constants. The constants $\lambda$ and $\mu$ are the second order elastic moduli better known as the Lamé parameters, while $A,B,$ and C are the third order elastic moduli introduced by, which are alternative but equivalent to $l,m,$ and n introduced by Murnaghan. Combining this with the general expression for the strain energy function it is clear that ${\begin{aligned}C_{ijkl}&=\lambda \delta _{ij}\delta _{kl}+2\mu \delta I_{ijkl},\\C_{ijklmn}&=2C\delta _{ij}\delta _{kl}\delta _{mn}+2B(\delta _{ij}I_{klmn}+\delta _{kl}I_{mnij}+\delta _{mn}I_{ijkl})+{\frac {1}{2}}A(\delta _{ik}I_{jlmn}+\delta _{il}I_{jkmn}+\delta _{jk}I_{ilmn}+\delta _{jl}I_{ikmn}),\end{aligned}}\!\,$ where $I_{ijkl}={\frac {1}{2}}(\delta _{ik}\delta _{jl}+\delta _{il}\delta _{jk})$ . Historically different selection of these third order elastic constants have been used, and some of the variations is shown in Table 1.

| Landau & Lifshitz (1986) | Toupin & Bernstein (1961) | Murnaghan (1951) | Bland (1969) | Eringen & Suhubi (1974) | Standard $C_{IJK}$ |   |
|---|---|---|---|---|---|---|
| A | $\nu _{1}=2C$ | $l=B+C$ | $\alpha ={\frac {1}{3}}C$ | $l_{E}={\frac {1}{3}}A+B+{\frac {1}{3}}C$ | $C_{123}=2C$ | $C_{111}=2A+6B+2C$ |
| B | $\nu _{2}=B$ | $m={\frac {1}{2}}A+B$ | $\beta =B$ | $m_{E}=-A-2B$ | $C_{144}=B$ | $C_{112}=2B+2C$ |
| C | $\nu _{3}={\frac {1}{4}}A$ | $n=A$ | $\gamma ={\frac {1}{3}}A$ | $n_{E}=A$ | $C_{456}={\frac {1}{4}}A$ | $C_{166}={\frac {1}{2}}A+B$ |

#### Example values for steel

Table 2 and 3 present the second and third order elastic constants for some steel types presented in literature

|   | Lamé constants | Toupin & Bernstein constants |   |   |   |
|---|---|---|---|---|---|
| Material | $\lambda$ | $\mu$ | $\nu _{1}$ | $\nu _{2}$ | $\nu _{3}$ |
| Hecla 37 (0.4%C) | 111±1 | 82.1±0.5 | −385±70 | −282±30 | −177±8 |
| Hecla 37 (0.6%C) | 110.5±1 | 82.0±0.5 | −134±20 | −261±20 | −167±6 |
| Hecla 138A | 109±1 | 81.9±0.5 | −323±50 | −265±30 | −177±10 |
| Rex 535 Ni steel | 109±1 | 81.8±0.5 | −175±50 | −240±50 | −169±15 |
| Hecla ATV austenitic | 87±2 | 71.6±3 | 34±20 | −552±80 | −100±10 |

|   | Lamé constants | Murnaghan constants |   |   |   |
|---|---|---|---|---|---|
| Material | $\lambda$ | $\mu$ | l | m | n |
| Nickel-steel S/NVT | 109.0±1 | 81.7±0.2 | −56±20 | −671±6 | −785±7 |
| Rail steel sample 1 | 115.8±2.3% | 79.9±2.3% | −248±2.8% | −623±4.1% | −714±2.7% |
| Rail steel sample 4 | 110.7±2.3% | 82.4±2.3% | −302±2.8% | −616±4.1% | −724±2.7% |

## Acoustoelasticity for uniaxial tension of isotropic hyperelastic materials

A cuboidal sample of a compressible solid in an unstressed reference configuration can be expressed by the Cartesian coordinates $X_{i}\in [0,L_{i}],\,i=1,2,3$ , where the geometry is aligned with the Lagrangian coordinate system, and $L_{i}$ is the length of the sides of the cuboid in the reference configuration. Subjecting the cuboid to a uniaxial tension in the $x_{1}$ -direction so that it deforms with a pure homogeneous strain such that the coordinates of the material points in the deformed configuration can be expressed by $x_{1}=\lambda _{1}X_{1},x_{2}=\lambda _{2}X_{2},x_{3}=\lambda _{3}X_{3}$ , which gives the elongations $e_{i}\equiv l_{i}/L_{i}-1=\lambda _{i}-1$ in the $x_{i}$ -direction. Here $l_{i}$ signifies the current (deformed) length of the cuboid side i and where the ratio between the length of the sides in the current and reference configuration are denoted by $\lambda _{i}\equiv l_{i}/L_{i}$ called the principal stretches. For an isotropic material this corresponds to a deformation without any rotation (See polar decomposition of the deformation gradient tensor where ${\boldsymbol {F}}={\boldsymbol {RU}}={\boldsymbol {VR}}$ and the rotation ${\boldsymbol {R}}={\boldsymbol {I}}$ ). This can be described through spectral representation by the principal stretches $\lambda _{i}$ as eigenvalues, or equivalently by the elongations $e_{i}$ .

For a uniaxial tension in the $x_{1}$ -direction ( $P_{11}>0$ we assume that the $e_{1}$ increase by some amount. If the lateral faces are free of traction (i.e., $P_{22}=P_{33}=0$ ) the lateral elongations $e_{2}$ and $e_{3}$ are limited to the range $e_{2},e_{3}\in (-1,0]$ . For isotropic symmetry the lateral elongations (or contractions) must also be equal (i.e. $e_{2}=e_{3}$ ). The range corresponds to the range from total lateral contraction ( $e_{2}=e_{3}=-1$ , which is non-physical), and to no change in the lateral dimensions ( $e_{2}=e_{3}=0$ ). It is noted that theoretically the range could be expanded to values large than 0 corresponding to an increase in lateral dimensions as a result of increase in axial dimension. However, very few materials (called auxetic materials) exhibit this property.

### Expansion of sound velocities

If the strong ellipticity condition ( $B_{ijkl}N_{j}N_{l}m_{i}m_{k}>0$ ) holds, three orthogonally polarization directions ( ${\boldsymbol {m}}$ will give a non-zero and real sound velocity for a given propagation direction ${\boldsymbol {N}}$ . The following will derive the sound velocities for óne selection of applied uniaxial tension, propagation direction, and an orthonormal set of polarization vectors. For a uniaxial tension applied in the $x_{1}$ -direction, and deriving the sound velocities for waves propagating orthogonally to the applied tension (e.g. in the $x_{3}$ -direction with propagation vector ${\boldsymbol {N}}=[0,0,1]$ ), one selection of orthonormal polarizations may be $\{{\boldsymbol {m}}\}={\begin{cases}\mathbf {m} _{1}=\mathbf {\hat {x}} _{1}=[1,0,0]&\|\,{\text{to applied tension}}\\\mathbf {m} _{2}=\mathbf {\hat {x}} _{2}=[0,1,0]&\perp {\text{to applied tension}}\\\mathbf {m} _{3}=\mathbf {\hat {x}} _{3}=[0,0,1]&\|\,{\textrm {to}}\,\mathbf {N} \end{cases}}$ which gives the three sound velocities $\rho _{0}c_{33}^{2}=B_{3333},\qquad \rho _{0}c_{31}^{2}=B_{1313},\qquad \rho _{0}c_{32}^{2}=B_{2323},$ where the first index i of the sound velocities $c_{ij}$ indicate the propagation direction (here the $x_{3}$ -direction, while the second index j indicate the selected polarization direction ( $j=i$ corresponds to particle motion in the propagation direction i – i.e. longitudinal wave, and $j\neq i$ corresponds to particle motion perpendicular to the propagation direction – i.e. shear wave).

Expanding the relevant coefficients of the acoustic tensor, and substituting the second- and third-order elastic moduli $C_{ijkl}$ and $C_{ijklmn}$ with their isotropic equivalents, $\lambda ,\mu$ and $A,B,C$ respectively, leads to the sound velocities expressed as $\rho _{0}c_{33}^{2}=\lambda +2\mu +a_{33}e_{1},\qquad \rho _{0}c_{3k}^{2}=\mu +a_{3k}e_{1},\quad k=1,2$ where $a_{33}=-{\frac {2\lambda (\lambda +2\mu )+\lambda A+2(\lambda -\mu )B-2\mu C}{\lambda +\mu }}$ $a_{31}={\frac {(\lambda +2\mu )(4\mu +A)+4\mu B}{4(\lambda +\mu )}}$ $a_{32}=-{\frac {\lambda (4\mu +A)-2\mu B}{2(\lambda +\mu )}}$ are the acoustoelastic coefficients related to effects from third order elastic constants.

## Measurement methods

To be able to measure the sound velocity, and more specifically the change in sound velocity, in a material subjected to some stress state, one can measure the velocity of an acoustic signal propagating through the material in question. There are several methods to do this but all of them use one of two physical relations of the sound velocity. The first relation is related to the time it takes a signal to propagate from one point to another (typically the distance between two acoustic transducers or two times the distance from one transducer to a reflective surface). This is often referred to as "Time-of-flight" (TOF) measurements, and use the relation $c={\frac {d}{t}}$ where d is the distance the signal travels and t is the time it takes to travel this distance. The second relation is related to the inverse of the time, the frequency, of the signal. The relation here is $c=f\lambda$ where f is the frequency of the signal and $\lambda$ is the wave length. The measurements using the frequency as measurand use the phenomenon of acoustic resonance where n number of wave lengths match the length over which the signal resonate. Both these methods are dependent on the distance over which it measure, either directly as in the Time-of-flight, or indirectly through the matching number of wavelengths over the physical extent of the specimen which resonate.

### Example of ultrasonic testing techniques

In general there are two ways to set up a transducer system to measure the sound velocity in a solid. One is a setup with two or more transducers where one is acting as a transmitter, while the other(s) is acting as a receiver. The sound velocity measurement can then be done by measuring the time between a signal is generated at the transmitter and when it is recorded at the receiver while assuming to know (or measure) the distance the acoustic signal have traveled between the transducers, or conversely to measure the resonance frequency knowing the thickness over which the wave resonate. The other type of setup is often called a *pulse-echo* system. Here one transducer is placed in the vicinity of the specimen acting both as transmitter and receiver. This requires a reflective interface where the generated signal can be reflected back toward the transducer which then act as a receiver recording the reflected signal. See ultrasonic testing for some measurement systems.

### Longitudinal and polarized shear waves

As explained above, a set of three orthonormal polarizations ( ${\boldsymbol {m}}$ ) of the particle motion exist for a given propagation direction ${\boldsymbol {N}}$ in a solid. For measurement setups where the transducers can be fixated directly to the sample under investigation it is possible to create these three polarizations (one longitudinal, and two orthogonal transverse waves) by applying different types of transducers exciting the desired polarization (e.g. piezoelectric transducers with the needed oscillation mode). Thus it is possible to measure the sound velocity of waves with all three polarizations through either time dependent or frequency dependent measurement setups depending on the selection of transducer types. However, if the transducer can not be fixated to the test specimen a coupling medium is needed to transmit the acoustic energy from the transducer to the specimen. Water or gels are often used as this coupling medium. For measurement of the longitudinal sound velocity this is sufficient, however fluids do not carry shear waves, and thus to be able to generate and measure the velocity of shear waves in the test specimen the incident longitudinal wave must interact at an oblique angle at the fluid/solid surface to generate shear waves through mode conversion. Such shear waves are then converted back to longitudinal waves at the solid/fluid surface propagating back through the fluid to the recording transducer enabling the measurement of shear wave velocities as well through a coupling medium.

## Applications

### Engineering material – stress estimation

As the industry strives to reduce maintenance and repair costs, non-destructive testing of structures becomes increasingly valued both in production control and as a means to measure the utilization and condition of key infrastructure. There are several measurement techniques to measure stress in a material. However, techniques using optical measurements, magnetic measurements, X-ray diffraction, and neutron diffraction are all limited to measuring surface or near surface stress or strains. Acoustic waves propagate with ease through materials and provide thus a means to probe the interior of structures, where the stress and strain level is important for the overall structural integrity. Since the sound velocity of such non-linear elastic materials (including common construction materials like aluminium and steel) have a stress dependency, one application of the acoustoelastic effect may be measurement of the stress state in the interior of a loaded material utilizing different acoustic probes (e.g. ultrasonic testing) to measure the change in sound velocities.

### Granular and porous materials – geophysics

seismology study the propagation of elastic waves through the Earth and is used in e.g. earthquake studies and in mapping the Earth's interior. The interior of the Earth is subjected to different pressures, and thus the acoustic signals may pass through media in different stress states. The acoustoelastic theory may thus be of practical interest where nonlinear wave behaviour may be used to estimate geophysical properties.

### Soft tissue – medical ultrasonics

Other applications may be in medical sonography and elastography measuring the stress or pressure level in relevant elastic tissue types (e.g., ), enhancing non-invasive diagnostics.
