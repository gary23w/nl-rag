---
title: "Ohmic contact"
source: https://en.wikipedia.org/wiki/Ohmic_contact
domain: esd-protection
license: CC-BY-SA-4.0
tags: electrostatic discharge, human body model, ohmic contact, clamp diode
fetched: 2026-07-02
---

# Ohmic contact

An **ohmic contact** is a non-rectifying electrical junction: a junction between two conductors that has a linear current–voltage (I–V) curve as with Ohm's law. Low-resistance ohmic contacts are used to allow charge to flow easily in both directions between the two conductors, without blocking due to rectification or excess power dissipation due to voltage thresholds.

By contrast, a junction or contact that does not demonstrate a linear I–V curve is called non-ohmic. Non-ohmic contacts come in a number of forms, such as p–n junction, Schottky barrier, rectifying heterojunction, or breakdown junction.

Generally the term "ohmic contact" implicitly refers to an ohmic contact of a metal to a semiconductor, where achieving ohmic contact resistance is possible but requires careful technique. Metal–metal ohmic contacts are relatively simpler to make, by ensuring direct contact between the metals without intervening layers of insulating contamination, excessive roughness or oxidation; various techniques are used to create ohmic metal–metal junctions (soldering, welding, crimping, deposition, electroplating, etc.).

Stable contacts at semiconductor interfaces, with low contact resistance and linear I–V behavior, are critical for the performance and reliability of semiconductor devices, and their preparation and characterization are major efforts in circuit fabrication. Poorly prepared junctions to semiconductors can easily show rectifying behaviour by causing depletion of the semiconductor near the junction, rendering the device useless by blocking the flow of charge between those devices and the external circuitry. Ohmic contacts to semiconductors are typically constructed by depositing thin metal films of a carefully chosen composition, possibly followed by annealing to alter the semiconductor–metal bond.

## Physics of formation of metal–semiconductor ohmic contacts

Both ohmic contacts and Schottky barriers are dependent on the Schottky barrier height, which sets the threshold for the excess energy an electron requires to pass from the semiconductor to the metal. For the junction to admit electrons easily in both directions (ohmic contact), the barrier height must be small in at least some parts of the junction surface. To form an excellent ohmic contact (low resistance), the barrier height should be small everywhere and furthermore the interface should not reflect electrons.

The Schottky barrier height between a metal and semiconductor is naively predicted by the Schottky–Mott rule to be proportional to the difference of the metal-vacuum work function and the semiconductor-vacuum electron affinity. In practice, most metal–semiconductor interfaces do not follow this rule to the predicted degree. Instead, the chemical termination of the semiconductor crystal against a metal creates electron states within its band gap. The nature of these metal-induced gap states and their occupation by electrons tends to pin the center of the band gap to the Fermi level, an effect known as Fermi level pinning. Thus, the heights of the Schottky barriers in metal–semiconductor contacts often show little dependence on the value of the semiconductor or metal work functions, in stark contrast to the Schottky–Mott rule. Different semiconductors exhibit this Fermi level pinning to different degrees, but a technological consequence is that high quality (low resistance) ohmic contacts are usually difficult to form in important semiconductors such as silicon and gallium arsenide.

The Schottky–Mott rule is not entirely incorrect since, in practice, metals with high work functions form the best contacts to p-type semiconductors, while those with low work functions form the best contacts to n-type semiconductors. Unfortunately experiments have shown that the predictive power of the model doesn't extend much beyond this statement. Under realistic conditions, contact metals may react with semiconductor surfaces to form a compound with new electronic properties. A contamination layer at the interface may effectively widen the barrier. The surface of the semiconductor may reconstruct leading to a new electronic state. The dependence of contact resistance on the details of the interfacial chemistry is what makes the reproducible fabrication of ohmic contacts such a manufacturing challenge.

## Preparation and characterization of ohmic contacts

The fabrication of the ohmic contacts is a much-studied part of materials engineering that nonetheless remains something of an art. The reproducible, reliable fabrication of contacts relies on extreme cleanliness of the semiconductor surface. Since a *native oxide* rapidly forms on the surface of silicon, for example, the performance of a contact can depend sensitively on the details of preparation. Often the contact region is heavily doped to ensure the type of contact wanted. As a rule, ohmic contacts on semiconductors form more easily when the semiconductor is highly doped near the junction; a high doping narrows the depletion region at the interface and allow electrons to flow in both directions easily at any bias by tunneling through the barrier.

The fundamental steps in contact fabrication are semiconductor surface cleaning, contact metal deposition, patterning and annealing. Surface cleaning may be performed by sputter-etching, chemical etching, reactive gas etching or ion milling. For example, the native oxide of silicon may be removed with a hydrofluoric acid dip, while GaAs is more typically cleaned by a bromine-methanol dip. After cleaning, metals are deposited via sputter deposition, evaporation or chemical vapor deposition (CVD). Sputtering is a faster and more convenient method of metal deposition than evaporation but the ion bombardment from the plasma may induce surface states or even invert the charge carrier type at the surface. For this reason the gentler but still rapid CVD may be used. Post-deposition annealing of contacts is useful for relieving stress as well as for inducing any desirable reactions between the metal and the semiconductor.

Because deposited metals can themselves react in ambient conditions, to the detriment of the contacts' electrical properties, it is common to form ohmic contacts with layered structures, with the bottom layer, in contact with the semiconductor, chosen for its ability to induce ohmic behaviour. A diffusion barrier-layer may be used to prevent the layers from mixing during any annealing process.

The measurement of contact resistance is most simply performed using a four-point probe although for more accurate determination, use of the transmission line method is typical.

## Technologically important kinds of contacts

Aluminum was originally the most important contact metal for silicon which was used with either the n-type or p-type semiconductor. As with other reactive metals, Al contributes to contact formation by consuming oxygen from native silicon-dioxide residue. Pure aluminum did react with the silicon, so it was replaced by silicon-doped aluminum and eventually by silicides less prone to diffuse during subsequent high-temperature processing.

Modern ohmic contacts to silicon such as titanium-tungsten disilicide are usually silicides made by CVD. Contacts are often made by depositing the transition metal and forming the silicide by annealing with the result that the silicide may be non-stoichiometric. Silicide contacts can also be deposited by direct sputtering of the compound or by ion implantation of the transition metal followed by annealing.

Formation of contacts to compound semiconductors is considerably more difficult than with silicon. For example, GaAs surfaces tend to lose arsenic and the trend towards As loss can be considerably exacerbated by the deposition of metal. In addition, the volatility of As limits the amount of post-deposition annealing that GaAs devices will tolerate. One solution for GaAs and other compound semiconductors is to deposit a low-bandgap alloy contact layer as opposed to a heavily doped layer. For example, GaAs itself has a smaller bandgap than AlGaAs and so a layer of GaAs near its surface can promote ohmic behavior. In general the technology of ohmic contacts for III-V and II-VI semiconductors is much less developed than for Si.

| Material | Contact materials |
|---|---|
| Si | Al, Al-Si, TiSi2, TiN, W, MoSi2, PtSi, CoSi2, WSi2 |
| Ge | In, AuGa, AuSb |
| GaAs | AuGe, PdGe, PdSi, Ti/Pt/Au |
| GaN | Ti/Al/Ni/Au, Pd/Au |
| InSb | In |
| ZnO | InSnO2, Al |
| CuIn1−xGaxSe2 | Mo, InSnO2 |
| HgCdTe | In |
| C (diamond) | Ti/Au,Mo/Au |

Transparent or semi-transparent contacts are necessary for active matrix LCDs, optoelectronic devices such as laser diodes and photovoltaics. The most popular choice is indium tin oxide, a metal that is formed by reactive sputtering of an In-Sn target in an oxide atmosphere.

## Significance

The RC time constant associated with contact resistance can limit the frequency response of devices. The charging and discharging of the leads resistance is a major cause of power dissipation in high-clock-rate digital electronics. Contact resistance causes power dissipation by Joule heating in low-frequency and analog circuits (for example, solar cells) made from less common semiconductors. The establishment of a contact fabrication methodology is a critical part of the technological development of any new semiconductor. Electromigration and delamination at contacts are also a limitation on the lifetime of electronic devices.
