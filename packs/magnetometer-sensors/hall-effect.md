---
title: "Hall effect"
source: https://en.wikipedia.org/wiki/Hall_effect
domain: magnetometer-sensors
license: CC-BY-SA-4.0
tags: magnetometer sensor, hall effect, magnetoresistance, fluxgate magnetometer
fetched: 2026-07-02
---

# Hall effect

The **Hall effect** is the production of a potential difference, across an electrical conductor, that is transverse to an electric current in the conductor and to an applied magnetic field perpendicular to the current. Such potential difference is known as the **Hall voltage**. It was discovered by Edwin Hall in 1879 through a study of the electromagnetic theory of James Clerk Maxwell, becoming a critical confirmation of that theory.

The **Hall coefficient** is defined as the ratio of the induced electric field to the product of the current density and the applied magnetic field. It is a characteristic of the material from which the conductor is made, since its value depends on the type, number, and properties of the charge carriers that constitute the current.

## Discovery

Wires carrying current in a magnetic field experience a mechanical force perpendicular to both the current and magnetic field.

In the 1820s, André-Marie Ampère observed this underlying mechanism that led to the discovery of the Hall effect. However it was not until a solid mathematical basis for electromagnetism was systematized by James Clerk Maxwell's "On Physical Lines of Force" (published in 1861–1862) that details of the interaction between magnets and electric current could be understood.

Edwin Hall then explored the question of whether magnetic fields interacted with the conductors *or* the electric current, and reasoned that if the force was specifically acting on the current, it should crowd current to one side of the wire, producing a small measurable voltage. In 1879, he discovered this *Hall effect* while he was working on his doctoral degree at Johns Hopkins University in Baltimore, Maryland. Eighteen years before the electron was discovered, his measurements of the tiny effect produced in the apparatus he used were an experimental tour de force, published under the name "On a New Action of the Magnet on Electric Currents".

## Theory

The Hall effect is due to the nature of the current in a conductor. Current consists of the movement of many small charge carriers, typically electrons, holes, ions (see Electromigration) or all three. When a magnetic field is present, these charges experience a force, called the Lorentz force. When such a magnetic field is absent, the charges follow approximately straight paths between collisions with impurities, phonons, etc. However, when a magnetic field with a perpendicular component is applied, their paths between collisions are curved; thus, moving charges accumulate on one face of the material. This leaves equal and opposite charges exposed on the other face, where there is a scarcity of mobile charges. The result is an asymmetric distribution of charge density across the Hall element, arising from a force that is perpendicular to both the straight path and the applied magnetic field. The separation of charge establishes an electric field that opposes the migration of further charge, so a steady electric potential is established for as long as the charge is flowing.

In classical electromagnetism, electrons move in the opposite direction of the current *I* (by convention "current" describes a theoretical "hole flow"). In some metals and semiconductors it *appears* "holes" are actually flowing because the direction of the voltage is opposite to the derivation below.

The Hall voltage *V*H can be derived for a conductor with only one type of charge carrier such as a simple metal with delocalised electrons. Charges that move in an electromagnetic field are affected by the Lorentz Force ${\vec {F}}_{L}$ . ${\vec {F}}_{L}=q\,({\vec {v}}\times {\vec {B}})$ With the velocity of the charge carriers ${\vec {v}}$ , the electric charge of said carriers q and the magnetic field ${\vec {B}}$ .

As charges accumulate towards one side of the carrier due to the Lorentz Force, a charge imbalance and hence an electric field ${\vec {E}}$ builds up, itself acting upon the charges $F_{E}=-q\cdot {\vec {E}}$ . In steady state, these forces cancel out: ${\vec {F}}=q\,({\vec {E}}+{\vec {v}}\times {\vec {B}})=0$

Consider the setup from the figure, with a cartesian coordinate system:

- A magnetic field in z -direction: $B_{z}$
- An Electric current in x -direction: $I_{x}$
  - Hence electrons moving in the negative x -direction: ${\vec {v}}=-v_{x}\cdot {\vec {e}}_{x}$

Through the vector Product, we can find that ${\vec {F}}_{L}$ is zero in all directions but the y -direction. $F_{y}=q\,(E_{y}-v_{x}\cdot B_{z})=0$ Dividing by the charge: $0=E_{y}-v_{x}\cdot B_{z}$ The Current density ${\vec {j}}$ can be expressed as ${\vec {j}}=nq{\vec {v}}$ with the charge carrier density n . Inserting this into the equation yields: $E_{y}={\frac {j_{x}}{nq}}\cdot B_{z}$ A material and temperature dependent Hall Coefficient $R_{H}$ is defined $E_{y}=R_{H}j_{x}B_{z}$ .

To get the Voltage, one can use the same relation as in capacitors $E_{y}={\frac {V_{H}}{W}}$ with W the width of the conductor (refer to the figure above). Furthermore, the current density is the current divided by the cross-section. For our cubic conductor, this is $j_{x}={\frac {I_{x}}{dW}}$ with the thickness d . Rearranging the relation then gives: $V_{H}=R_{H}{\frac {I_{x}B_{z}}{d}}$ This relationship remains the same for more complicated conductors with different charge carriers, however the calculation of the Hall Constant is more complicated for those.

Notice through the diagram that no matter the sign of the charge carrier, it get's deflected in the same direction. The polarity of the Hall voltage however would be reversed as a positively charged field would build up in case of positive charge carriers.

This property of the Hall effect offered the first real proof that electric currents in most metals are carried by moving electrons, not by protons. It also showed that in some substances (especially p-type semiconductors), it is contrarily more appropriate to think of the current as positive "holes" moving rather than negative electrons. A common source of confusion with the Hall effect in such materials is that holes moving one way are really electrons moving the opposite way, so one expects the Hall voltage polarity to be the same as if electrons were the charge carriers as in most metals and n-type semiconductors. Yet we observe the opposite polarity of Hall voltage, indicating positive charge carriers. However, of course there are no actual positrons or other positive elementary particles carrying the charge in p-type semiconductors, hence the name "holes". In the same way as the oversimplistic picture of light in glass as photons being absorbed and re-emitted to explain refraction breaks down upon closer scrutiny, this apparent contradiction too can only be resolved by the modern quantum mechanical theory of quasiparticles wherein the collective quantized motion of multiple particles can, in a real physical sense, be considered to be a particle in its own right (albeit not an elementary one).

Unrelatedly, inhomogeneity in the conductive sample can result in a spurious sign of the Hall effect, even in ideal van der Pauw configuration of electrodes. For example, a Hall effect consistent with positive carriers was observed in evidently n-type semiconductors. Another source of artefact, in uniform materials, occurs when the sample's aspect ratio is not long enough: the full Hall voltage only develops far away from the current-introducing contacts, since at the contacts the transverse voltage is shorted out to zero.

### Hall effect in semiconductors

When a current-carrying semiconductor is kept in a magnetic field, the charge carriers of the semiconductor experience a force in a direction perpendicular to both the magnetic field and the current. At equilibrium, a voltage appears at the semiconductor edges.

The simple formula for the Hall coefficient given above is usually a good explanation when conduction is dominated by a single charge carrier. However, in semiconductors and many metals the theory is more complex, because in these materials conduction can involve significant, simultaneous contributions from both electrons and holes, which may be present in different concentrations and have different mobilities. For moderate magnetic fields the Hall coefficient is

$R_{\mathrm {H} }={\frac {p\mu _{\mathrm {h} }^{2}-n\mu _{\mathrm {e} }^{2}}{e(p\mu _{\mathrm {h} }+n\mu _{\mathrm {e} })^{2}}}$ or equivalently $R_{\mathrm {H} }={\frac {p-nb^{2}}{e(p+nb)^{2}}}$ with $b={\frac {\mu _{\mathrm {e} }}{\mu _{\mathrm {h} }}}.$ Here *n* is the electron concentration, *p* the hole concentration, *μ*e the electron mobility, *μ*h the hole mobility and *e* the elementary charge.

For large applied fields the simpler expression analogous to that for a single carrier type holds.

### Relationship with star formation

Although it is well known that magnetic fields play an important role in star formation, research models indicate that Hall diffusion critically influences the dynamics of gravitational collapse that forms protostars.

### Quantum Hall effect

For a two-dimensional electron system which can be produced in a MOSFET, in the presence of large magnetic field strength and low temperature, one can observe the quantum Hall effect, in which the Hall conductance σ undergoes quantum Hall transitions to take on quantized values.

### Spin Hall effect

The spin Hall effect consists in the spin accumulation on the lateral boundaries of a current-carrying sample. No magnetic field is needed. It was predicted by Mikhail Dyakonov and V. I. Perel in 1971 and observed experimentally more than 30 years later, both in semiconductors and in metals, at cryogenic as well as at room temperatures.

The quantity describing the strength of the Spin Hall effect is known as Spin Hall angle, and it is defined as:

$\theta _{SH}={\frac {2e}{\hbar }}{\frac {|j_{s}|}{|j_{e}|}}$

Where $j_{s}$ is the spin current generated by the applied current density $j_{e}$ .

### Quantum spin Hall effect

For mercury telluride two dimensional quantum wells with strong spin-orbit coupling, in zero magnetic field, at low temperature, the quantum spin Hall effect has been observed in 2007.

### Anomalous Hall effect

In ferromagnetic materials (and paramagnetic materials in a magnetic field), the Hall resistivity includes an additional contribution, known as the **anomalous Hall effect** (or the **extraordinary Hall effect**), which depends directly on the magnetization of the material, and is often much larger than the ordinary Hall effect. (Note that this effect is *not* due to the contribution of the magnetization to the total magnetic field.) For example, in nickel, the anomalous Hall coefficient is about 100 times larger than the ordinary Hall coefficient near the Curie temperature, but the two are similar at very low temperatures. Although a well-recognized phenomenon, there is still debate about its origins in the various materials. The anomalous Hall effect can be either an *extrinsic* (disorder-related) effect due to spin-dependent scattering of the charge carriers, or an *intrinsic* effect which can be described in terms of the Berry phase effect in the crystal momentum space (*k*-space).

### Hall effect in ionized gases

The Hall effect in an ionized gas (plasma) is significantly different from the Hall effect in solids (where the **Hall parameter** is always much less than unity). In a plasma, the Hall parameter can take any value. The Hall parameter, *β*, in a plasma is the ratio between the electron gyrofrequency, *Ω*e, and the electron-heavy particle collision frequency, ν: $\beta ={\frac {\Omega _{\mathrm {e} }}{\nu }}={\frac {eB}{m_{\mathrm {e} }\nu }}$ where

- *e* is the elementary charge (approximately 1.6×10−19 C)
- *B* is the magnetic field (in teslas)
- *m*e is the electron mass (approximately 9.1×10−31 kg).

The Hall parameter value increases with the magnetic field strength.

Physically, the trajectories of electrons are curved by the Lorentz force. Nevertheless, when the Hall parameter is low, their motion between two encounters with heavy particles (neutral or ion) is almost linear. But if the Hall parameter is high, the electron movements are highly curved. The current density vector, **J**, is no longer collinear with the electric field vector, **E**. The two vectors **J** and **E** make the **Hall angle**, θ, which also gives the Hall parameter: $\beta =\tan(\theta ).$

### Other Hall effects

The Hall Effects family has expanded to encompass other quasi-particles in semiconductor nanostructures. Specifically, a set of Hall Effects has emerged based on excitons and exciton-polaritons in 2D materials and quantum wells.

## Applications

Hall sensors amplify and use the Hall effect for a variety of sensing applications. Hall-effect thrusters use the Hall effect to limit electrons' axial motion and use them to accelerate a propellant.

## Corbino effect

The Corbino effect, named after its discoverer Orso Mario Corbino, is a phenomenon involving the Hall effect, but a disc-shaped metal sample is used in place of a rectangular one. Because of its shape the Corbino disc allows the observation of Hall effect–based magnetoresistance without the associated Hall voltage.

A radial current through a circular disc, subjected to a magnetic field perpendicular to the plane of the disc, produces a "circular" current through the disc. The absence of the free transverse boundaries renders the interpretation of the Corbino effect simpler than that of the Hall effect.
