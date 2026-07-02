---
title: "Magnetic dipole"
source: https://en.wikipedia.org/wiki/Magnetic_dipole
domain: magnetostatics
license: CC-BY-SA-4.0
tags: magnetostatic field, biot-savart law, magnetic dipole, magnetic vector potential
fetched: 2026-07-02
---

# Magnetic dipole

In electromagnetism, a **magnetic dipole** is a theoretical description of a sufficiently small magnet such as that of an atom or electron. All magnets can be described as being a magnetic dipole for sufficiently large distances from the magnet. The strength of a magnetic dipole is determined by a single property its magnetic dipole moment. The magnetic dipole model accurately predicts many properties of small magnets such as the magnetic field it produces, how it interacts with other magnetic dipoles, and how an external magnetic field will apply a torque or create a net force on the dipole.

Two different models can be used to describe a magnetic dipole. The simplest to understand, but least correct, is to imagine the magnet as 2 equal but opposite poles that act similar to electric charges. The 'ideal' magnetic dipole then is modeled by shrinking the distance between the poles while increasing the magnetic pole strength such that product of the two (the magnetic dipole moment) remains at the given value for that dipole. This can often give correct results in an easy to understand way, but suffers from being incorrect (magnetic poles do not exist as separate entities) and giving incorrect results in certain cases (for example inside of a magnet).

The more correct description of a magnetic dipole is that of a closed loop of electric current that encloses a flat area **a**. The magnetic moment of this dipole then is the product of its area and it current. This amperian loop model has the advantage of being physically correct, at least for the part of the magnetic field of an atom due to the motion of the electrons around the nucleus of atoms.

Because magnetic monopoles do not exist, the magnetic field at a large distance from any static magnetic source looks like the field of a dipole with the same dipole moment. For higher-order sources (e.g. quadrupoles) with no dipole moment, their field decays towards zero with distance faster than a dipole field does.

## Models

The preferred classical explanation of a magnetic dipole has changed over time. Before the 1930s, textbooks explained the magnetic dipole using hypothetical magnetic point charges. Since then, most have defined it in terms of Ampèrian currents. In magnetic materials, the cause of the magnetic moment are the spin and orbital angular momentum states of the electrons.

### Magnetic pole model

The sources of magnetic moments in materials can be represented by poles in analogy to electrostatics. This is sometimes known as the Gilbert model. In this model, a small magnet is modeled by a pair of *fictitious* magnetic monopoles of equal magnitude but opposite polarity. Each pole is the source of magnetic force which weakens with distance. Since magnetic poles always come in pairs, their forces partially cancel each other because while one pole pulls, the other repels. This cancellation is greatest when the poles are close to each other i.e. when the bar magnet is short. The magnetic force produced by a bar magnet, at a given point in space, therefore depends on two factors: the strength p of its poles (*magnetic pole strength*), and the vector $\mathrm {\boldsymbol {\ell }}$ separating them. The magnetic dipole moment **m** is related to the fictitious poles as $\mathbf {m} =p\,\mathrm {\boldsymbol {\ell }} \,.$

It points in the direction from the South to the North pole. The analogy with electric dipoles should not be taken too far because magnetic dipoles are associated with angular momentum (see Relation to angular momentum). Nevertheless, magnetic poles are very useful for magnetostatic calculations, particularly in applications to ferromagnets. Practitioners using the magnetic pole approach generally represent the magnetic field by the irrotational field **H**, in analogy to the electric field **E**.

### Ampèrian loop model

After Hans Christian Ørsted discovered that electric currents produce a magnetic field and André-Marie Ampère discovered that electric currents attract and repel each other similar to magnets, it was natural to hypothesize that all magnetic fields are due to electric current loops. In this model developed by Ampère, the elementary magnetic dipole that makes up all magnets is a sufficiently small amperian loop of current *I*. The dipole moment of this loop is $\mathbf {m} =I{\boldsymbol {S}},$ where S is the area of the loop. The direction of the magnetic moment is in a direction normal to the area enclosed by the current consistent with the direction of the current using the right hand rule.

#### Localized current distributions

The magnetic dipole moment can be calculated for a localized (does not extend to infinity) current distribution assuming that we know all of the currents involved. Conventionally, the derivation starts from a multipole expansion of the vector potential. This leads to the definition of the magnetic dipole moment as: $\mathbf {m} ={\tfrac {1}{2}}\iiint _{V}\mathbf {r} \times \mathbf {j} (\mathbf {r} )\,\mathrm {d} V,$ where × is the vector cross product, **r** is the position vector, and **j** is the electric current density and the integral is a volume integral. When the current density in the integral is replaced by a loop of current I in a plane enclosing an area S then the volume integral becomes a line integral and the resulting dipole moment becomes $\mathbf {m} =I\mathbf {S} ,$ which is how the magnetic dipole moment for an Amperian loop is derived.

Practitioners using the current loop model generally represent the magnetic field by the solenoidal field **B**, analogous to the electrostatic field **D**.

#### Magnetic moment of a solenoid

A generalization of the above current loop is a coil, or solenoid. Its moment is the vector sum of the moments of individual turns. If the solenoid has N identical turns (single-layer winding) and vector area **S**, $\mathbf {m} =NI\mathbf {S} .$

### Quantum mechanical model

When calculating the magnetic moments of materials or molecules on the microscopic level it is often convenient to use a third model for the magnetic moment that exploits the linear relationship between the angular momentum and the magnetic moment of a particle. While this relation is straightforward to develop for macroscopic currents using the amperian loop model (see below), neither the magnetic pole model nor the amperian loop model truly represents what is occurring at the atomic and molecular levels. At that level quantum mechanics must be used. Fortunately, the linear relationship between the magnetic dipole moment of a particle and its angular momentum still holds, although it is different for each particle. Further, care must be used to distinguish between the intrinsic angular momentum (or spin) of the particle and the particle's orbital angular momentum.

## External magnetic field produced by a magnetic dipole moment

In classical physics, the magnetic field of a dipole is calculated as the limit of either a current loop or a pair of charges as the source shrinks to a point while keeping the magnetic moment **m** constant. For the current loop, this limit is most easily derived from the vector potential:

${\mathbf {A} }({\mathbf {r} })={\frac {\mu _{0}}{4\pi }}{\frac {{\mathbf {m} }\times {\mathbf {r} }}{r^{3}}},$

where *μ*0 is the vacuum permeability constant and 4*π r*2 is the surface of a sphere of radius *r*. The magnetic flux density (strength of the B-field) is then

$\mathbf {B} ({\mathbf {r} })=\nabla \times {\mathbf {A} }={\frac {\mu _{0}}{4\pi }}\left[{\frac {3\mathbf {r} (\mathbf {m} \cdot \mathbf {r} )}{r^{5}}}-{\frac {\mathbf {m} }{r^{3}}}\right].$

Alternatively one can obtain the scalar potential first from the magnetic pole limit,

$\psi ({\mathbf {r} })={\frac {{\mathbf {m} }\cdot {\mathbf {r} }}{4\pi r^{3}}},$

and hence the magnetic field strength (or strength of the H-field) is

${\mathbf {H} }({\mathbf {r} })=-\nabla \psi ={\frac {1}{4\pi }}\left[{\frac {3\mathbf {\hat {r}} (\mathbf {m} \cdot \mathbf {\hat {r}} )-\mathbf {m} }{r^{3}}}\right]={\frac {\mathbf {B} ({\mathbf {r} })}{\mu _{0}}}.$

The magnetic field strength is symmetric under rotations about the axis of the magnetic moment. In spherical coordinates, with $\mathbf {\hat {z}} =\mathbf {\hat {r}} \cos \theta -{\boldsymbol {\hat {\theta }}}\sin \theta$ , and with the magnetic moment aligned with the z-axis, then the field strength can more simply be expressed as

$\mathbf {H} ({\mathbf {r} })={\frac {|\mathbf {m} |}{4\pi r^{3}}}\left(2\cos \theta \,\mathbf {\hat {r}} +\sin \theta \,{\boldsymbol {\hat {\theta }}}\right).$

## Internal magnetic field of a dipole

The two models for a dipole (current loop and magnetic poles), give the same predictions for the magnetic field far from the source. However, inside the source region they give different predictions. The magnetic field between poles is in the opposite direction to the magnetic moment (which points from the negative charge to the positive charge), while inside a current loop it is in the same direction (see the figure to the right (above for mobile users)). Clearly, the limits of these fields must also be different as the sources shrink to zero size. This distinction only matters if the dipole limit is used to calculate fields inside a magnetic material.

If a magnetic dipole is formed by making a current loop smaller and smaller, but keeping the product of current and area constant, the limiting field is

$\mathbf {B} (\mathbf {r} )={\frac {\mu _{0}}{4\pi }}\left[{\frac {3\mathbf {\hat {r}} (\mathbf {\hat {r}} \cdot \mathbf {m} )-\mathbf {m} }{|\mathbf {r} |^{3}}}+{\frac {8\pi }{3}}\mathbf {m} \delta (\mathbf {r} )\right],$

where *δ*(**r**) is the Dirac delta function in three dimensions. Unlike the expressions in the previous section, this limit is correct for the internal field of the dipole.

If a magnetic dipole is formed by taking a "north pole" and a "south pole", bringing them closer and closer together but keeping the product of magnetic pole-charge and distance constant, the limiting field is

$\mathbf {H} (\mathbf {r} )={\frac {1}{4\pi }}\left[{\frac {3\mathbf {\hat {r}} (\mathbf {\hat {r}} \cdot \mathbf {m} )-\mathbf {m} }{|\mathbf {r} |^{3}}}-{\frac {4\pi }{3}}\mathbf {m} \delta (\mathbf {r} )\right].$

These fields are related by **B** = *μ*0(**H** + **M**), where

$\mathbf {M} (\mathbf {r} )=\mathbf {m} \delta (\mathbf {r} )$

is the magnetization.

## Forces between two magnetic dipoles

The force **F** exerted by one dipole moment **m**1 on another **m**2 separated in space by a vector **r** can be calculated using:

$\mathbf {F} =\nabla \left(\mathbf {m} _{2}\cdot \mathbf {B} _{1}\right),$

or

$\mathbf {F} (\mathbf {r} ,\mathbf {m} _{1},\mathbf {m} _{2})={\dfrac {3\mu _{0}}{4\pi r^{5}}}\left[(\mathbf {m} _{1}\cdot \mathbf {r} )\mathbf {m} _{2}+(\mathbf {m} _{2}\cdot \mathbf {r} )\mathbf {m} _{1}+(\mathbf {m} _{1}\cdot \mathbf {m} _{2})\mathbf {r} -{\dfrac {5(\mathbf {m} _{1}\cdot \mathbf {r} )(\mathbf {m} _{2}\cdot \mathbf {r} )}{r^{2}}}\mathbf {r} \right],$

where r is the distance between dipoles. The force acting on **m**1 is in the opposite direction.

The torque can be obtained from the formula

${\boldsymbol {\tau }}=\mathbf {m} _{2}\times \mathbf {B} _{1}.$

## Dipolar fields from finite sources

The magnetic scalar potential *ψ* produced by a finite source, but external to it, can be represented by a multipole expansion. Each term in the expansion is associated with a characteristic moment and a potential having a characteristic rate of decrease with distance *r* from the source. Monopole moments have a 1/*r* rate of decrease, dipole moments have a 1/*r*2 rate, quadrupole moments have a 1/*r*3 rate, and so on. The higher the order, the faster the potential drops off. Since the lowest-order term observed in magnetic sources is the dipole term, it dominates at large distances. Therefore, at large distances any magnetic source looks like a dipole of the same magnetic moment.
