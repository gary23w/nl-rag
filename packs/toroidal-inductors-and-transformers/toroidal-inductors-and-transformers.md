---
title: "Toroidal inductors and transformers"
source: https://en.wikipedia.org/wiki/Toroidal_inductors_and_transformers
domain: toroidal-inductors-and-transformers
license: CC-BY-SA-4.0
tags: toroidal inductors and transformers
fetched: 2026-07-03
---

# Toroidal inductors and transformers

**Toroidal inductors and transformers** are inductors and transformers which use magnetic cores with a toroidal (ring or donut) shape. They are passive electronic components, consisting of a circular ring or donut shaped magnetic core of ferromagnetic material such as laminated iron, iron powder, or ferrite, around which wire is wound.

Although closed-core inductors and transformers often use cores with a rectangular shape, the use of toroidal-shaped cores sometimes provides superior electrical performance. The advantage of the toroidal shape is that, due to its symmetry, the amount of magnetic flux that escapes outside the core (leakage flux) can be made low, potentially making it more efficient and making it emit less electromagnetic interference (EMI).

Toroidal inductors and transformers are used in a wide range of electronic circuits: power supplies, inverters, and amplifiers, which in turn are used in the vast majority of electrical equipment: TVs, radios, computers, and audio power amplifiers.

## Advantages

In general, toroidal inductors and transformers are more compact than other shaped cores, resulting in up to a 50% lighter weight design. This is especially the case for power devices.

Because the toroid is a closed-loop core, it has a higher inductance and Q factor than an inductor of the same mass with a straight core (solenoid coils). This is because most of the magnetic field is contained within the core. By comparison, with an inductor with a straight core, the magnetic field emerging from one end of the core has a long path through air to enter the other end.

Because the windings are relatively short and the magnetic field is closed, a toroidal transformer has higher efficiency, electrical performance, and reduces effects such as distortion and fringing.

Due to the symmetry of a toroid, little magnetic flux escapes from the core (leakage flux). Thus, a toroidal inductor/transformer, couples less electromagnetic interference (EMI) to adjacent circuits and is often chosen for highly concentrated environments. Manufacturers have adopted toroidal coils in recent years to comply with standards limiting the amount of electromagnetic field consumer electronics can produce.

## Total B field confinement

In some circumstances, the current in the winding of a toroidal inductor contributes only to the **B** field inside the windings. It does not contribute to the magnetic **B** field outside the windings. This is a consequence of symmetry and Ampère's circuital law.

### Sufficient conditions

|   |   |
|---|---|

The absence of circumferential current (the path of circumferential current is indicated by the red arrow in figure 3 of this section) and the axially symmetric layout of the conductors and magnetic materials are sufficient conditions for total internal confinement of the **B** field. (Some authors prefer to use the **H** field). Because of the symmetry, the lines of B flux must form circles of constant intensity centered on the axis of symmetry. The only lines of B flux that encircle any current are those that are inside the toroidal winding. Therefore, from Ampere's circuital law, the intensity of the B field must be zero outside the windings.

Figure 3 of this section shows the most common toroidal winding. It fails both requirements for total B field confinement. Looking out from the axis, sometimes the winding is on the inside of the core and sometimes on the outside of the core. It is not axially symmetric in the near region. However, at points a distance of several times the winding spacing, the toroid does look symmetric. There is still the problem of the circumferential current. No matter how many times the winding encircles the core and no matter how thin the wire, this toroidal inductor will still include a one coil loop in the plane of the toroid. This winding will also produce and be susceptible to an **E** field in the plane of the inductor.

Figures 4-6 show different ways to neutralize the circumferential current. Figure 4 is the simplest and has the advantage that the return wire can be added after the inductor is bought or built.

|   |   |   |
|---|---|---|

### External electric field

|   |   |
|---|---|

There will be a distribution of potential along the winding. This can lead to an **E**-Field in the plane of the toroid and also a susceptibility to an **E** field in the plane of the toroid, as shown in figure 7. This can be mitigated by using a return winding, as shown in Figure 8. With this winding, each place the winding crosses itself, the two parts will be at equal and opposite polarity, which substantially reduces the E field generated in the plane.

### Magnetic vector potential

See Feynman chapter 14 and 15 for a general discussion of magnetic vector potential. See Feynman page 15-11 for a diagram of the magnetic vector potential around a long thin solenoid which also exhibits total internal confinement of the **B** field, at least in the infinite limit.

The **A** field is accurate when using the assumption $bf{A}=0$ . This would be true under the following assumptions:

- 1. the Coulomb gauge is used
- 2. the Lorenz gauge is used and there is no distribution of charge, $\rho =0\,$
- 3. the Lorenz gauge is used and zero frequency is assumed
- 4. the Lorenz gauge is used and a non-zero frequency that is low enough to neglect ${\frac {1}{c^{2}}}{\frac {\partial \phi }{\partial t}}$ is assumed.

Number 4 will be presumed for the rest of this section and may be referred to the "quasi-static condition".

Although the axially symmetric toroidal inductor with no circumferential current totally confines the **B** field within the windings, the **A** field (magnetic vector potential) is not confined. Arrow #1 in the picture depicts the vector potential on the axis of symmetry. Radial current sections a and b are equal distances from the axis but pointed in opposite directions, so they cancel. Likewise, segments c and d cancel. All the radial current segments cancel. The situation for axial currents is different. The axial current on the outside of the toroid is pointed down and the axial current on the inside of the toroid is pointed up. Each axial current segment on the outside of the toroid can be matched with an equal but oppositely directed segment on the inside of the toroid. The segments on the inside are closer than the segments on the outside to the axis, therefore there is a net upward component of the **A** field along the axis of symmetry.

Since the equations $\nabla \times \mathbf {A} =\mathbf {B} \$ , and $\nabla \times \mathbf {B} =\mu _{0}\mathbf {j} \$ (assuming quasi-static conditions, i.e. ${\frac {\partial E}{\partial t}}\rightarrow 0$ ) have the same form, then the lines and contours of **A** relate to **B** like the lines and contours of **B** relate to **j**. Thus, a depiction of the **A** field around a loop of **B** flux (as would be produced in a toroidal inductor) is qualitatively the same as the **B** field around a loop of current. The figure to the left is an artist's depiction of the **A** field around a toroidal inductor. The thicker lines indicate paths of higher average intensity (shorter paths have higher intensity so that the path integral is the same). The lines are just drawn to look good and impart general look of the **A** field.

### Transformer action

The **E** and **B** fields can be computed from the **A** and $\phi \,$ (scalar electric potential) fields

$\mathbf {B} =\nabla \times \mathbf {A} .$

and

:

$\mathbf {E} =-\nabla \phi -{\frac {\partial \mathbf {A} }{\partial t}}$

and so even if the region outside the windings is devoid of

B

field, it is filled with non-zero

E

field.

The quantity

${\frac {\partial \mathbf {A} }{\partial t}}$

is responsible for the desirable magnetic field coupling between primary and secondary while the quantity

$\nabla \phi \,$

is responsible for the undesirable electric field coupling between primary and secondary. Transformer designers attempt to minimize the electric field coupling. For the rest of this section,

$\nabla \phi \,$

will assumed to be zero unless otherwise specified.

Stokes theorem applies, so that the path integral of **A** is equal to the enclosed **B** flux, just as the path integral **B** is equal to a constant times the enclosed current

The path integral of **E** along the secondary winding gives the secondary's induced EMF (Electro-Motive Force).

$\mathbf {EMF} =\oint _{path}\mathbf {E} \cdot {\rm {d}}l=-\oint _{path}{\frac {\partial \mathbf {A} }{\partial t}}\cdot {\rm {d}}l=-{\frac {\partial }{\partial t}}\oint _{path}\mathbf {A} \cdot {\rm {d}}l=-{\frac {\partial }{\partial t}}\int _{surface}\mathbf {B} \cdot {\rm {d}}s$

which says the EMF is equal to the time rate of change of the B flux enclosed by the winding, which is the usual result.

### Poynting vector coupling

This figure shows the half section of a toroidal transformer. Quasi-static conditions are assumed, so the phase of each field is the same everywhere. The transformer, its windings and all things are distributed symmetrically about the axis of symmetry. The windings are such that there is no circumferential current. The requirements are met for full internal confinement of the **B** field due to the primary current. The core and primary winding are represented by the gray-brown torus. The primary winding is not shown, but the current in the winding at the cross-section surface is shown as gold (or orange) ellipses. The **B** field caused by the primary current is confined to the region enclosed by the primary winding (i.e. the core). Blue dots on the left-hand cross-section indicate that lines of **B** flux in the core come out of the left-hand cross-section. On the other cross-section, blue plus signs indicate that the **B** flux enters there. The **E** field sourced from the primary currents is shown as green ellipses. The secondary winding is shown as a brown line coming directly down the axis of symmetry. In standard practice, the two ends of the secondary are connected with a long wire that stays well away from the torus, but to maintain the absolute axial symmetry, the entire apparatus is envisioned as being inside a perfectly conductive sphere with the secondary wire "grounded" to the inside of the sphere at each end. The secondary is made of resistance wire, so there is no separate load. The **E** field along the secondary causes current in the secondary (yellow arrows), which causes a **B** field around the secondary (shown as blue ellipses). This **B** field fills space, including inside the transformer core, so in the end, there is a continuous non-zero **B** field from the primary to the secondary, if the secondary is not open-circuited. The cross product of the **E** field (sourced from primary currents) and the **B** field (sourced from the secondary currents) forms the Poynting vector, which points from the primary toward the secondary.
