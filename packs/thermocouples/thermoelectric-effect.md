---
title: "Thermoelectric effect"
source: https://en.wikipedia.org/wiki/Thermoelectric_effect
domain: thermocouples
license: CC-BY-SA-4.0
tags: thermocouple sensor, thermoelectric effect, seebeck coefficient, thermopile array
fetched: 2026-07-02
---

# Thermoelectric effect

The **thermoelectric effect** is the direct conversion of temperature differences to electric voltage and vice versa via a thermocouple. A thermoelectric device creates a voltage when there is a different temperature on each side. Conversely, when a voltage is applied to it, heat is transferred from one side to the other, creating a temperature difference.

This effect can be used to generate electricity, measure temperature or change the temperature of objects. Because the direction of heating and cooling is affected by the applied voltage, thermoelectric devices can be used as temperature controllers.

The term "thermoelectric effect" encompasses three separately identified effects: the **Seebeck effect** (temperature differences cause electromotive forces), the **Peltier effect** (thermocouples create temperature differences), and the **Thomson effect** (the Seebeck coefficient varies with temperature). The Seebeck and Peltier effects are different manifestations of the same physical process; textbooks may refer to this process as the **Peltier–Seebeck effect** (the separation derives from the independent discoveries by Jean Charles Athanase Peltier and Thomas Johann Seebeck). The Thomson effect is an extension of the Peltier–Seebeck model and is credited to Lord Kelvin.

Joule heating, the heat that is generated whenever a current is passed through a conductive material, is not generally termed a thermoelectric effect. The Peltier–Seebeck and Thomson effects are thermodynamically reversible, whereas Joule heating is not.

## Origin

At the atomic scale, a temperature gradient causes charge carriers in the material to diffuse from the hot side to the cold side. This is due to charge carrier particles having higher mean velocities (and thus kinetic energy) at higher temperatures, leading them to migrate on average towards the colder side, in the process carrying heat across the material.

Depending on the material properties and nature of the charge carriers (whether they are positive holes in a bulk material or electrons of negative charge), heat can be carried in either direction with respect to voltage. Semiconductors of n-type and p-type are often combined in series as they have opposite directions for heat transport, as specified by the sign of their Seebeck coefficients.

## Seebeck effect

The **Seebeck effect** is the emergence of electromotive force (EMF) that develops across two points of an electrically conducting material when there is a temperature difference between them. The EMF is called the Seebeck EMF (or thermo/thermal/thermoelectric EMF). The ratio between the EMF and temperature difference is the Seebeck coefficient. A thermocouple measures the difference in potential across a hot and cold end for two dissimilar materials. This potential difference is proportional to the temperature difference between the hot and cold ends. First discovered in 1794 by Alessandro Volta, it is named after Thomas Johann Seebeck, who rediscovered it in 1821.

Seebeck observed what he called "thermomagnetic effect" wherein a magnetic compass needle would be deflected by a closed loop formed by two different metals joined in two places, with an applied temperature difference between the joints. Hans Christian Ørsted noted that the temperature difference was in fact driving an electric current, with the generation of magnetic field being an indirect consequence, and so coined the more accurate term "thermoelectricity".

The Seebeck effect is a classic example of an electromotive force (EMF) and leads to measurable currents or voltages in the same way as any other EMF. The local current density is given by

$\mathbf {J} =\sigma (-\nabla V+\mathbf {E} _{\text{EMF}}),$

where V is the local voltage, and $\sigma$ is the local conductivity. In general, the Seebeck effect is described locally by the creation of an electromotive field

$\mathbf {E} _{\text{EMF}}=-S\nabla T,$

where S is the Seebeck coefficient (also known as thermopower), a property of the local material, and $\nabla T$ is the temperature gradient.

The Seebeck coefficients generally vary as function of temperature and depend strongly on the composition of the conductor. For ordinary materials at room temperature, the Seebeck coefficient may range in value from −100 μV/K to +1,000 μV/K (see Seebeck coefficient article for more information).

### Applications

In practice, thermoelectric effects are essentially unobservable for a localized hot or cold spot in a single homogeneous conducting material, since the overall EMFs from the increasing and decreasing temperature gradients will perfectly cancel out. Attaching an electrode to the hotspot in an attempt to measure the locally shifted voltage will only partly succeed: It means another temperature gradient will appear inside of the electrode, so the overall EMF will depend on the difference in Seebeck coefficients between the electrode and the conductor it is attached to.

Thermocouples involve two wires, each of a different material, that are electrically joined in a region of unknown temperature. The loose ends are measured in an open-circuit state (without any current, $\mathbf {J} =0$ ). Although the materials' Seebeck coefficients S are nonlinearly temperature dependent and different for the two materials, the open-circuit condition means that $\nabla V=-S\nabla T$ everywhere. Therefore (see the thermocouple article for more details) the voltage measured at the loose ends of the wires is directly dependent on the unknown temperature, and yet totally independent of other details such as the exact geometry of the wires. This direct relationship allows the thermocouple arrangement to be used as a straightforward uncalibrated thermometer, provided knowledge of the difference in S -vs- T curves of the two materials, and of the reference temperature at the measured loose wire ends.

Thermoelectric sorting functions similarly to a thermocouple but involves an unknown material instead of an unknown temperature: a metallic probe of known composition is kept at a constant known temperature and held in contact with the unknown sample that is locally heated to the probe temperature, thereby providing an approximate measurement of the unknown Seebeck coefficient S . This can help distinguish between different metals and alloys.

Thermopiles are formed from many thermocouples in series, zig-zagging back and forth between hot and cold. This multiplies the voltage output.

Thermoelectric generators are like a thermocouple/thermopile but instead draw some current from the generated voltage in order to extract power from heat differentials. They are optimized differently from thermocouples, using high quality thermoelectric materials in a thermopile arrangement, to maximize the extracted power. Though not particularly efficient, these generators have the advantage of not having any moving parts.

## Peltier effect

When an electric current is passed through a circuit of a thermocouple, heat is generated (dumped, pumped) at one junction and absorbed at the other junction. This is known as the **Peltier effect**: the presence of heating or cooling at an electrified junction of two different conductors. The effect is named after French physicist Jean Charles Athanase Peltier, who discovered it in 1834. When a current is made to flow through a junction between two conductors, A and B, heat may be generated or removed at the junction. The Peltier heat generated at the junction per unit time is

${\dot {Q}}=(\Pi _{\text{A}}-\Pi _{\text{B}})I,$

where $\Pi _{\text{A}}$ and $\Pi _{\text{B}}$ are the Peltier coefficients of conductors A and B, and I is the electric current (from A to B). The total heat generated is not determined by the Peltier effect alone, as it may also be influenced by Joule heating and thermal-gradient effects (see below).

The Peltier coefficients represent how much heat is carried per unit charge. Since charge current must be continuous across a junction, the associated heat flow will develop a discontinuity if $\Pi _{\text{A}}$ and $\Pi _{\text{B}}$ differ. The Peltier effect can be considered as the back-action counterpart to the Seebeck effect (analogous to the back-EMF in magnetic induction): if a simple thermoelectric circuit is closed, then the Seebeck effect will drive a current, which in turn (by the Peltier effect) will always transfer heat from the hot to the cold junction. The close relationship between Peltier and Seebeck effects can be seen in the direct connection between their coefficients: $\Pi =TS$ (see below).

A typical Peltier heat-pump involves multiple junctions in series, through which a current is driven. Some of the junctions lose heat due to the Peltier effect, while others gain heat. Thermoelectric heat pumps exploit this phenomenon, as do thermoelectric-cooling devices found in refrigerators.

A **Peltier cell** operates on the basis of the Peltier effect.

### Applications

The Peltier effect can be used to create a heat pump. Notably, the Peltier thermoelectric cooler is a refrigerator that is compact and has no circulating fluid or moving parts. Such refrigerators are useful in applications where their advantages outweigh the disadvantage of their very low efficiency.

Other heat-pump applications such as dehumidifiers may also use Peltier heat-pumps.

Thermoelectric coolers are trivially reversible, in that they can be used as heaters by simply reversing the current. Unlike ordinary resistive electrical heating (Joule heating) that varies with the square of current, the thermoelectric heating effect is linear in current (at least for small currents) but requires a cold sink to replenish with heat energy. This rapid reversing heating and cooling effect is used by many modern thermal cyclers, laboratory devices used to amplify DNA by the polymerase chain reaction (PCR). PCR requires the cyclic heating and cooling of samples to specified temperatures. The inclusion of many thermocouples in a small space enables many samples to be amplified in parallel.

## Thomson effect

For certain materials, the Seebeck coefficient is not constant in temperature, and so a spatial gradient in temperature can result in a gradient in the Seebeck coefficient. If a current is driven through this gradient, then a continuous version of the Peltier effect will occur. This **Thomson effect** was predicted and later observed in 1851 by Lord Kelvin (William Thomson). It describes the heating or cooling of a current-carrying conductor with a temperature gradient. If a current density $\mathbf {J}$ is passed through a homogeneous conductor, the Thomson effect predicts a heat production rate per unit volume.

${\dot {q}}=-{\mathcal {K}}\mathbf {J} \cdot \nabla T,$

where $\nabla T$ is the temperature gradient, and ${\mathcal {K}}$ is the Thomson coefficient. The Thomson effect is a manifestation of the direction of flow of electrical carriers with respect to a temperature gradient within a conductor. These absorb energy (heat) flowing in a direction opposite to a thermal gradient, increasing their potential energy, and, when flowing in the same direction as a thermal gradient, they liberate heat, decreasing their potential energy. The Thomson coefficient is related to the Seebeck coefficient as ${\mathcal {K}}=T{\tfrac {dS}{dT}}$ (see below). This equation, however, neglects Joule heating and ordinary thermal conductivity (see full equations below).

## Full thermoelectric equations

Often, more than one of the above effects is involved in the operation of a real thermoelectric device. The Seebeck effect, Peltier effect, and Thomson effect can be gathered together in a consistent and rigorous way, described here; this also includes the effects of Joule heating and ordinary heat conduction. As stated above, the Seebeck effect generates an electromotive force, leading to the current equation

$\mathbf {J} =\sigma (-{\boldsymbol {\nabla }}V-S\nabla T).$

To describe the Peltier and Thomson effects, we must consider the flow of energy. If temperature and charge change with time, the full thermoelectric equation for the energy accumulation, ${\dot {e}}$ , is

${\dot {e}}=\nabla \cdot (\kappa \nabla T)-\nabla \cdot (V+\Pi )\mathbf {J} +{\dot {q}}_{\text{ext}},$

where $\kappa$ is the thermal conductivity. The first term is the Fourier's heat conduction law, and the second term shows the energy carried by currents. The third term, ${\dot {q}}_{\text{ext}}$ , is the heat added from an external source (if applicable).

If the material has reached a steady state, the charge and temperature distributions are stable, so ${\dot {e}}=0$ and $\nabla \cdot \mathbf {J} =0$ . Using these facts and the second Thomson relation (see below), the heat equation can be simplified to

$-{\dot {q}}_{\text{ext}}=\nabla \cdot (\kappa \nabla T)+\mathbf {J} \cdot \left(\sigma ^{-1}\mathbf {J} \right)-T\mathbf {J} \cdot \nabla S.$

The middle term is the Joule heating, and the last term includes both Peltier ( $\nabla S$ at junction) and Thomson ( $\nabla S$ in thermal gradient) effects. Combined with the Seebeck equation for $\mathbf {J}$ , this can be used to solve for the steady-state voltage and temperature profiles in a complicated system.

If the material is not in a steady state, a complete description needs to include dynamic effects such as relating to electrical capacitance, inductance and heat capacity.

The thermoelectric effects lie beyond the scope of equilibrium thermodynamics. They necessarily involve continuing flows of energy. At least, they involve three bodies or thermodynamic subsystems, arranged in a particular way, along with a special arrangement of the surroundings. The three bodies are the two different metals and their junction region. The junction region is an inhomogeneous body, assumed to be stable, not suffering amalgamation by diffusion of matter. The surroundings are arranged to maintain two temperature reservoirs and two electric reservoirs.

For an imagined, but not actually possible, thermodynamic equilibrium, heat transfer from the hot reservoir to the cold reservoir would need to be prevented by a specifically matching voltage difference maintained by the electric reservoirs, and the electric current would need to be zero. For a steady state, there must be at least some heat transfer or some non-zero electric current. The two modes of energy transfer, as heat and by electric current, can be distinguished when there are three distinct bodies and a distinct arrangement of surroundings.

But in the case of continuous variation in the media, heat transfer and thermodynamic work cannot be uniquely distinguished. This is more complicated than the often considered thermodynamic processes, in which just two respectively homogeneous subsystems are connected.

## Thomson relations

In 1854, Lord Kelvin found relationships between the three coefficients, implying that the Thomson, Peltier, and Seebeck effects are different manifestations of one effect (uniquely characterized by the Seebeck coefficient).

The first Thomson relation is

${\mathcal {K}}\equiv {\frac {d\Pi }{dT}}-S,$

where T is the absolute temperature, ${\mathcal {K}}$ is the Thomson coefficient, $\Pi$ is the Peltier coefficient, and S is the Seebeck coefficient. This relationship is easily shown given that the Thomson effect is a continuous version of the Peltier effect.

The second Thomson relation is

$\Pi =TS.$

This relation expresses a subtle and fundamental connection between the Peltier and Seebeck effects. It was not satisfactorily proven until the advent of the Onsager relations, and it is worth noting that this second Thomson relation is only guaranteed for a time-reversal symmetric material; if the material is placed in a magnetic field or is itself magnetically ordered (ferromagnetic, antiferromagnetic, etc.), then the second Thomson relation does not take the simple form shown here.

Now, using the second relation, the first Thomson relation becomes

${\mathcal {K}}=T{\tfrac {dS}{dT}}$

The Thomson coefficient is unique among the three main thermoelectric coefficients because it is the only one directly measurable for individual materials. The Peltier and Seebeck coefficients can only be easily determined for pairs of materials; hence, it is difficult to find values of absolute Seebeck or Peltier coefficients for an individual material.

If the Thomson coefficient of a material is measured over a wide temperature range, it can be integrated using the Thomson relations to determine the absolute values for the Peltier and Seebeck coefficients. This needs to be done only for one material, since the other values can be determined by measuring pairwise Seebeck coefficients in thermocouples containing the reference material and then adding back the absolute Seebeck coefficient of the reference material. For more details on absolute Seebeck coefficient determination, see Seebeck coefficient.

### Efficiency

The efficiency of such devices varies on several conditions, including its environment and the device in question. However, they roughly operate at efficiencies as low as 5% or sometimes as high as 12%.
