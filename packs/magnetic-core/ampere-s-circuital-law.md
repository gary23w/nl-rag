---
title: "Ampère's circuital law"
source: https://en.wikipedia.org/wiki/Ampere's_circuital_law
domain: magnetic-core
license: CC-BY-SA-4.0
tags: magnetic core
fetched: 2026-07-03
---

# Ampère's circuital law

(Redirected from

Ampere's circuital law

)

In classical electromagnetism, **Ampère's circuital law**, often simply called **Ampère's law**, and sometimes **Oersted's law**, relates the circulation of a magnetic field around a closed loop to the electric current passing through that loop.

The law was inspired by Hans Christian Ørsted's 1820 discovery that an electric current generates a magnetic field. This finding prompted theoretical and experimental work by André-Marie Ampère and others, eventually leading to the formulation of the law in its modern form.

James Clerk Maxwell published the law in 1855. In 1865, he generalized the law to account for time-varying electric currents by introducing the displacement current term. The resulting equation, often called the **Ampère–Maxwell law**, is one of Maxwell's equations that form the foundation of classical electromagnetism.

## Background

Until the early 19th century, electricity and magnetism were thought to be completely separate phenomena. This view changed in 1820 when Danish physicist Hans Christian Ørsted discovered that an electric current produces a magnetic effect. He observed that a compass needle placed near a current-carrying wire deflected so that it aligned perpendicular to the wire. In a series of experiments, Ørsted demonstrated that the current could influence magnetic poles nearby, and that its effect extended outward from the wire. He also observed that this magnetic influence formed a vortex around the wire.

Ørsted's discovery sparked a great deal of research into the relation between electricity and magnetism. André-Marie Ampère investigated the magnetic force between two current-carrying wires, discovering Ampère's force law. In the 1850s, Scottish mathematical physicist James Clerk Maxwell generalized these results and others into a single mathematical law. The original form of Maxwell's circuital law, which he discussed in 1854 in correspondence with William Thomson (later ennobled as Lord Kelvin) and published in his 1855 paper "On Faraday's Lines of Force", was based on an analogy to hydrodynamics.

The original circuital law relates magnetic fields to electric currents that produce them and can be used to determine either the magnetic field associated with a given current, or the current associated with a given magnetic field. However, it applies only in magnetostatic situations, involving steady, continuous currents flowing in closed circuits. In systems where electric fields vary with time, the original law (as given in this section) must be modified by adding a term known as Maxwell's correction (see below).

### Equivalent forms

The original circuital law can be written in several different forms, which are all ultimately equivalent:

- An "integral form" and a "differential form". The forms are exactly equivalent, and related by the Kelvin–Stokes theorem (see the "proof" section below).
- Forms using SI units, and those using cgs units. Other units are possible, but rare. This section will use SI units, with cgs units discussed later.
- Forms using either **B** or **H** magnetic fields. These two forms use the total current density and free current density, respectively. The **B** and **H** fields are related by the constitutive equation: **B** = *μ*0**H** in non-magnetic materials where *μ*0 is the magnetic constant.

### Explanation

The integral form of the original circuital law is a line integral of the magnetic field around some closed curve C (arbitrary but must be closed). The curve C in turn bounds both a surface S which the electric current passes through (again arbitrary but not closed—since no three-dimensional volume is enclosed by S), and encloses the current. The mathematical statement of the law is a relation between the circulation of the magnetic field around some path (line integral) due to the current which passes through that enclosed path (surface integral).

In terms of total current, (which is the sum of both free current and bound current) the line integral of the magnetic **B**-field (in teslas, T) around closed curve C is proportional to the total current *I*enc passing through a surface S (enclosed by C). In terms of free current, the line integral of the magnetic **H**-field (in amperes per metre, A·m−1) around closed curve C equals the free current *I*f,enc through a surface S.

|   | Integral form | Differential form |
|---|---|---|
| Using **B**-field and total current | $\oint _{C}\mathbf {B} \cdot \mathrm {d} {\boldsymbol {l}}=\mu _{0}\iint _{S}\mathbf {J} \cdot \mathrm {d} \mathbf {S} =\mu _{0}I_{\mathrm {enc} }$ | $\nabla \times \mathbf {B} =\mu _{0}\mathbf {J}$ |
| Using **H**-field and free current | $\oint _{C}\mathbf {H} \cdot \mathrm {d} {\boldsymbol {l}}=\iint _{S}\mathbf {J} _{\mathrm {f} }\cdot \mathrm {d} \mathbf {S} =I_{\mathrm {f,enc} }$ | $\nabla \times \mathbf {H} =\mathbf {J} _{\mathrm {f} }$ |

- **J** is the total current density (in amperes per square metre, A·m−2),
- **J**f is the free current density only,
- ∮*C* is the closed line integral around the closed curve C,
- ∬*S* denotes a surface integral over the surface S bounded by the curve C,
- · is the vector dot product,
- d***l*** is an infinitesimal element (a differential) of the curve C (i.e. a vector with magnitude equal to the length of the infinitesimal line element, and direction given by the tangent to the curve C)
- d**S** is the vector area of an infinitesimal element of surface S (that is, a vector with magnitude equal to the area of the infinitesimal surface element, and direction normal to surface S. The direction of the normal must correspond with the orientation of C by the right hand rule), see below for further explanation of the curve C and surface S.
- ∇ × is the curl operator.

### Ambiguities and sign conventions

There are a number of ambiguities in the above definitions that require clarification and a choice of convention.

1. First, three of these terms are associated with sign ambiguities: the line integral ∮*C* could go around the loop in either direction (clockwise or counterclockwise); the vector area d**S** could point in either of the two directions normal to the surface; and *I*enc is the net current passing through the surface S, meaning the current passing through in one direction, minus the current in the other direction—but either direction could be chosen as positive. These ambiguities are resolved by the right-hand rule: With the palm of the right-hand toward the area of integration, and the index-finger pointing along the direction of line-integration, the outstretched thumb points in the direction that must be chosen for the vector area d**S**. Also the current passing in the same direction as d**S** must be counted as positive. The right hand grip rule can also be used to determine the signs.
2. Second, there are infinitely many possible surfaces S that have the curve C as their border. (Imagine a soap film on a wire loop, which can be deformed by blowing on the film). Which of those surfaces is to be chosen? If the loop does not lie in a single plane, for example, there is no one obvious choice. The answer is that it does not matter: in the magnetostatic case, the current density is solenoidal (see next section), so the divergence theorem and continuity equation imply that the flux through any surface with boundary C, with the same sign convention, is the same. In practice, one usually chooses the most convenient surface (with the given boundary) to integrate over.

## Free current versus bound current

The electric current that arises in the simplest textbook situations would be classified as "free current"—for example, the current that passes through a wire or battery. In contrast, "bound current" arises in the context of bulk materials that can be magnetized and/or polarized. (All materials can to some extent.)

When a material is magnetized (for example, by placing it in an external magnetic field), the electrons remain bound to their respective atoms, but behave as if they were orbiting the nucleus in a particular direction, creating a microscopic current. When the currents from all these atoms are put together, they create the same effect as a macroscopic current, circulating perpetually around the magnetized object. This magnetization current **J**M is one contribution to "bound current".

The other source of bound current is bound charge. When an electric field is applied, the positive and negative bound charges can separate over atomic distances in polarizable materials, and when the bound charges move, the polarization changes, creating another contribution to the "bound current", the polarization current **J**P.

The total current density **J** due to free and bound charges is then:

$\mathbf {J} =\mathbf {J} _{\mathrm {f} }+\mathbf {J} _{\mathrm {M} }+\mathbf {J} _{\mathrm {P} }\,,$

with **J**f the "free" or "conduction" current density.

All current is fundamentally the same, microscopically. Nevertheless, there are often practical reasons for wanting to treat bound current differently from free current. For example, the bound current usually originates over atomic dimensions, and one may wish to take advantage of a simpler theory intended for larger dimensions. The result is that the more microscopic Ampère's circuital law, expressed in terms of **B** and the microscopic current (which includes free, magnetization and polarization currents), is sometimes put into the equivalent form below in terms of **H** and the free current only. For a detailed definition of free current and bound current, and the proof that the two formulations are equivalent, see the "proof" section below.

## Shortcomings of the original formulation of the circuital law

There are two important issues regarding the circuital law that require closer scrutiny. First, there is an issue regarding the continuity equation for electrical charge. In vector calculus, the identity for the divergence of a curl states that the divergence of the curl of a vector field must always be zero. Hence $\nabla \cdot (\nabla \times \mathbf {B} )=0\,,$ and so the original Ampère's circuital law implies that $\nabla \cdot \mathbf {J} =0\,,$ i.e. that the current density is solenoidal.

But in general, reality follows the continuity equation for electric charge: $\nabla \cdot \mathbf {J} =-{\frac {\partial \rho }{\partial t}}\,,$ which is nonzero for a time-varying charge density. An example occurs in a capacitor circuit where time-varying charge densities exist on the plates.

Second, there is an issue regarding the propagation of electromagnetic waves. For example, in free space, where $\mathbf {J} =\mathbf {0} \,,$ the circuital law implies that $\nabla \times \mathbf {B} =\mathbf {0} \,,$ i.e. that the magnetic field is irrotational, but to maintain consistency with the continuity equation for electric charge, we must have $\nabla \times \mathbf {B} ={\frac {1}{c^{2}}}{\frac {\partial \mathbf {E} }{\partial t}}\,.$

To 'resolve' these situations (w/ eqn. above), the contribution of displacement current must be added to the current term in the circuital law.

James Clerk Maxwell conceived of displacement current as a polarization current in the dielectric vortex sea, which he used to model the magnetic field hydrodynamically and mechanically. He added this displacement current to Ampère's circuital law at equation 112 in his 1861 paper "On Physical Lines of Force".

### Displacement current

In free space, the displacement current is related to the time rate of change of electric field.

In a dielectric the above contribution to displacement current is present too, but a major contribution to the displacement current is related to the polarization of the individual molecules of the dielectric material. Even though charges cannot flow freely in a dielectric, the charges in molecules can move a little under the influence of an electric field. The positive and negative charges in molecules separate under the applied field, causing an increase in the state of polarization, expressed as the polarization density **P**. A changing state of polarization is equivalent to a current.

Both contributions to the displacement current are combined by defining the displacement current as: $\mathbf {J} _{\mathrm {D} }={\frac {\partial }{\partial t}}\mathbf {D} (\mathbf {r} ,\,t)\,,$ where the electric displacement field is defined as: $\mathbf {D} =\varepsilon _{0}\mathbf {E} +\mathbf {P} =\varepsilon _{0}\varepsilon _{\mathrm {r} }\mathbf {E} \,,$ where *ε*0 is the electric constant, *ε*r the relative static permittivity, and **P** is the polarization density. Substituting this form for **D** in the expression for displacement current, it has two components: $\mathbf {J} _{\mathrm {D} }=\varepsilon _{0}{\frac {\partial \mathbf {E} }{\partial t}}+{\frac {\partial \mathbf {P} }{\partial t}}\,.$

The first term on the right hand side is present everywhere, even in a vacuum. It doesn't involve any actual movement of charge, but it nevertheless has an associated magnetic field, as if it were an actual current. Some authors apply the name *displacement current* to only this contribution.

The second term on the right hand side is the displacement current as originally conceived by Maxwell, associated with the polarization of the individual molecules of the dielectric material.

Maxwell's original explanation for displacement current focused upon the situation that occurs in dielectric media. In the modern post-aether era, the concept has been extended to apply to situations with no material media present, for example, to the vacuum between the plates of a charging vacuum capacitor. The displacement current is justified today because it serves several requirements of an electromagnetic theory: correct prediction of magnetic fields in regions where no free current flows; prediction of wave propagation of electromagnetic fields; and conservation of electric charge in cases where charge density is time-varying. For greater discussion see Displacement current.

## Extending the original law: the Ampère–Maxwell equation

Next, the circuital equation is extended by including the polarization current, thereby remedying the limited applicability of the original circuital law.

Treating free charges separately from bound charges, the equation including Maxwell's correction in terms of the **H**-field is (the **H**-field is used because it includes the magnetization currents, so **J**M does not appear explicitly, see **H**-field and also Note): $\oint _{C}\mathbf {H} \cdot \mathrm {d} {\boldsymbol {l}}=\iint _{S}\left(\mathbf {J} _{\mathrm {f} }+{\frac {\partial \mathbf {D} }{\partial t}}\right)\cdot \mathrm {d} \mathbf {S}$ (integral form), where **H** is the magnetic **H** field (also called "auxiliary magnetic field", "magnetic field intensity", or just "magnetic field"), **D** is the electric displacement field, and **J**f is the enclosed conduction current or free current density. In differential form, $\nabla \times \mathbf {H} =\mathbf {J} _{\mathrm {f} }+{\frac {\partial \mathbf {D} }{\partial t}}\,.$

On the other hand, treating all charges on the same footing (disregarding whether they are bound or free charges), the generalized Ampère's equation, also called the Maxwell–Ampère equation, is in integral form (see the "proof" section below):

$\oint _{C}\mathbf {B} \cdot \mathrm {d} {\boldsymbol {l}}=\iint _{S}\left(\mu _{0}\mathbf {J} +\mu _{0}\varepsilon _{0}{\frac {\partial \mathbf {E} }{\partial t}}\right)\cdot \mathrm {d} \mathbf {S}$

In differential form,

$\nabla \times \mathbf {B} =\mu _{0}\mathbf {J} +\mu _{0}\varepsilon _{0}{\frac {\partial \mathbf {E} }{\partial t}}$

In both forms **J** includes magnetization current density as well as conduction and polarization current densities. That is, the current density on the right side of the Ampère–Maxwell equation is: $\mathbf {J} _{\mathrm {f} }+\mathbf {J} _{\mathrm {D} }+\mathbf {J} _{\mathrm {M} }=\mathbf {J} _{\mathrm {f} }+\mathbf {J} _{\mathrm {P} }+\mathbf {J} _{\mathrm {M} }+\varepsilon _{0}{\frac {\partial \mathbf {E} }{\partial t}}=\mathbf {J} +\varepsilon _{0}{\frac {\partial \mathbf {E} }{\partial t}}\,,$ where current density **J**D is the *displacement current*, and **J** is the current density contribution actually due to movement of charges, both free and bound. Because ∇ ⋅ **D** = *ρ*, the charge continuity issue with Ampère's original formulation is no longer a problem. Because of the term in *ε*0⁠∂**E**/∂*t*⁠, wave propagation in free space now is possible.

With the addition of the displacement current, Maxwell was able to hypothesize (correctly) that light was a form of electromagnetic wave. See electromagnetic wave equation for a discussion of this important discovery.

### Proof of equivalence

**Proof that the formulations of the circuital law in terms of free current are equivalent to the formulations involving total current**

In this proof, we will show that the equation $\nabla \times \mathbf {H} =\mathbf {J} _{\mathrm {f} }+{\frac {\partial \mathbf {D} }{\partial t}}$ is equivalent to the equation ${\frac {1}{\mu _{0}}}(\nabla \times \mathbf {B} )=\mathbf {J} +\varepsilon _{0}{\frac {\partial \mathbf {E} }{\partial t}}\,.$ Note that we are only dealing with the differential forms, not the integral forms, but that is sufficient since the differential and integral forms are equivalent in each case, by the Kelvin–Stokes theorem.

We introduce the polarization density **P**, which has the following relation to **E** and **D**: $\mathbf {D} =\varepsilon _{0}\mathbf {E} +\mathbf {P} \,.$

Next, we introduce the magnetization density **M**, which has the following relation to **B** and **H**: ${\frac {1}{\mu _{0}}}\mathbf {B} =\mathbf {H} +\mathbf {M}$ and the following relation to the bound current: ${\begin{aligned}\mathbf {J} _{\mathrm {bound} }&=\nabla \times \mathbf {M} +{\frac {\partial \mathbf {P} }{\partial t}}\\&=\mathbf {J} _{\mathrm {M} }+\mathbf {J} _{\mathrm {P} },\end{aligned}}$ where $\mathbf {J} _{\mathrm {M} }=\nabla \times \mathbf {M} ,$ is called the magnetization current density, and $\mathbf {J} _{\mathrm {P} }={\frac {\partial \mathbf {P} }{\partial t}},$ is the polarization current density. Taking the equation for **B**: ${\begin{aligned}{\frac {1}{\mu _{0}}}\nabla \times \mathbf {B} &=\nabla \times \left(\mathbf {H} +\mathbf {M} \right)\\&=\nabla \times \mathbf {H} +\mathbf {J} _{\mathrm {M} }\\&=\mathbf {J} _{\mathrm {f} }+\mathbf {J} _{\mathrm {P} }+\varepsilon _{0}{\frac {\partial \mathbf {E} }{\partial t}}+\mathbf {J} _{\mathrm {M} }.\end{aligned}}$

Consequently, referring to the definition of the bound current: ${\begin{aligned}{\frac {1}{\mu _{0}}}(\nabla \times \mathbf {B} )&=\mathbf {J} _{\mathrm {f} }+\mathbf {J} _{\mathrm {bound} }+\varepsilon _{0}{\frac {\partial \mathbf {E} }{\partial t}}\\&=\mathbf {J} +\varepsilon _{0}{\frac {\partial \mathbf {E} }{\partial t}},\end{aligned}}$ as was to be shown.

## Ampère's circuital law in cgs units

In cgs units, the integral form of the equation, including Maxwell's correction, reads $\oint _{C}\mathbf {B} \cdot \mathrm {d} {\boldsymbol {l}}={\frac {1}{c}}\iint _{S}\left(4\pi \mathbf {J} +{\frac {\partial \mathbf {E} }{\partial t}}\right)\cdot \mathrm {d} \mathbf {S} ,$ where c is the speed of light.

The differential form of the equation (again, including Maxwell's correction) is $\nabla \times \mathbf {B} ={\frac {1}{c}}\left(4\pi \mathbf {J} +{\frac {\partial \mathbf {E} }{\partial t}}\right).$
