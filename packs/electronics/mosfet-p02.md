---
title: "MOSFET (part 2/2)"
source: https://en.wikipedia.org/wiki/MOSFET
domain: electronics
license: CC-BY-SA-4.0
tags: electronics, circuit, resistor, capacitor, transistor, voltage, adc, logic gate
fetched: 2026-07-02
part: 2/2
---

## Scaling

Over the past decades, the MOSFET (as used for digital logic) has continually been scaled down in size; typical MOSFET channel lengths were once several micrometres, but modern integrated circuits are incorporating MOSFETs with channel lengths of tens of nanometers. Robert Dennard's work on scaling theory was pivotal in recognising that this ongoing reduction was possible. Intel began production of a process featuring a 32 nm feature size (with the channel being even shorter) in late 2009. The semiconductor industry maintains a "roadmap", the ITRS, which sets the pace for MOSFET development. Historically, the difficulties with decreasing the size of the MOSFET have been associated with the semiconductor device fabrication process, the need to use very low voltages, and with poorer electrical performance necessitating circuit redesign and innovation (small MOSFETs exhibit higher leakage currents and lower output resistance).

Smaller MOSFETs are desirable for several reasons. The main reason to make transistors smaller is to pack more and more devices in a given chip area. This results in a chip with the same functionality in a smaller area, or chips with more functionality in the same area. Since fabrication costs for a semiconductor wafer are relatively fixed, the cost per integrated circuits is mainly related to the number of chips that can be produced per wafer. Hence, smaller ICs allow more chips per wafer, reducing the price per chip. In fact, over the past 30 years the number of transistors per chip has been doubled every 2–3 years once a new technology node is introduced. For example, the number of MOSFETs in a microprocessor fabricated in a 45 nm technology can well be twice as many as in a 65 nm chip. This doubling of transistor density was first observed by Gordon Moore in 1965 and is commonly referred to as Moore's law. It is also expected that smaller transistors switch faster. For example, one approach to size reduction is a scaling of the MOSFET that requires all device dimensions to reduce proportionally. The main device dimensions are the channel length, channel width, and oxide thickness. When they are scaled down by equal factors, the transistor channel resistance does not change, while gate capacitance is cut by that factor. Hence, the RC delay of the transistor scales with a similar factor. While this has been traditionally the case for the older technologies, for the state-of-the-art MOSFETs reduction of the transistor dimensions does not necessarily translate to higher chip speed because the delay due to interconnections is more significant.

Producing MOSFETs with channel lengths much smaller than a micrometre is a challenge, and the difficulties of semiconductor device fabrication are always a limiting factor in advancing integrated circuit technology. Though processes such as ALD have improved fabrication for small components, the small size of the MOSFET (less than a few tens of nanometers) has created operational problems:

### Higher subthreshold conduction

As MOSFET geometries shrink, the voltage that can be applied to the gate must be reduced to maintain reliability. To maintain performance, the threshold voltage of the MOSFET has to be reduced as well. As threshold voltage is reduced, the transistor cannot be switched from complete turn-off to complete turn-on with the limited voltage swing available; the circuit design is a compromise between strong current in the *on* case and low current in the *off* case, and the application determines whether to favor one over the other. Subthreshold leakage (including subthreshold conduction, gate-oxide leakage and reverse-biased junction leakage), which was ignored in the past, now can consume upwards of half of the total power consumption of modern high-performance VLSI chips.

### Increased gate-oxide leakage

The gate oxide, which serves as insulator between the gate and channel, should be made as thin as possible to increase the channel conductivity and performance when the transistor is on and to reduce subthreshold leakage when the transistor is off. However, with current gate oxides with a thickness of around 1.2 nm (which in silicon is ~5 atoms thick) the quantum mechanical phenomenon of electron tunneling occurs between the gate and channel, leading to increased power consumption. Silicon dioxide has traditionally been used as the gate insulator. Silicon dioxide however has a modest dielectric constant. Increasing the dielectric constant of the gate dielectric allows a thicker layer while maintaining a high capacitance (capacitance is proportional to dielectric constant and inversely proportional to dielectric thickness). All else equal, a higher dielectric thickness reduces the quantum tunneling current through the dielectric between the gate and the channel.

Insulators that have a larger dielectric constant than silicon dioxide (referred to as high-κ dielectrics), such as group IVb metal silicates e.g. hafnium and zirconium silicates and oxides are being used to reduce the gate leakage from the 45 nanometer technology node onwards. On the other hand, the barrier height of the new gate insulator is an important consideration; the difference in conduction band energy between the semiconductor and the dielectric (and the corresponding difference in valence band energy) also affects leakage current level. For the traditional gate oxide, silicon dioxide, the former barrier is approximately 8 eV. For many alternative dielectrics the value is significantly lower, tending to increase the tunneling current, somewhat negating the advantage of higher dielectric constant. The maximum gate-source voltage is determined by the strength of the electric field able to be sustained by the gate dielectric before significant leakage occurs. As the insulating dielectric is made thinner, the electric field strength within it goes up for a fixed voltage. This necessitates using lower voltages with the thinner dielectric.

### Increased junction leakage

To make devices smaller, junction design has become more complex, leading to higher doping levels, shallower junctions, "halo" doping and so forth, all to decrease drain-induced barrier lowering (see the section on junction design). To keep these complex junctions in place, the annealing steps formerly used to remove damage and electrically active defects must be curtailed increasing junction leakage. Heavier doping is also associated with thinner depletion layers and more recombination centers that result in increased leakage current, even without lattice damage.

### Drain-induced barrier lowering and *V*T roll off

Drain-induced barrier lowering (DIBL) and *V*T roll off: Because of the short-channel effect, channel formation is not entirely done by the gate, but now the drain and source also affect the channel formation. As the channel length decreases, the depletion regions of the source and drain come closer together and make the threshold voltage (*V*T) a function of the length of the channel. This is called *V*T roll-off. *V*T also becomes function of drain to source voltage *V*DS. As we increase the *V*DS, the depletion regions increase in size, and a considerable amount of charge is depleted by the *V*DS. The gate voltage required to form the channel is then lowered, and thus, the *V*T decreases with an increase in *V*DS. This effect is called drain induced barrier lowering (DIBL).

### Lower output resistance

For analog operation, good gain requires a high MOSFET output impedance, which is to say, the MOSFET current should vary only slightly with the applied drain-to-source voltage. As devices are made smaller, the influence of the drain competes more successfully with that of the gate due to the growing proximity of these two electrodes, increasing the sensitivity of the MOSFET current to the drain voltage. To counteract the resulting decrease in output resistance, circuits are made more complex, either by requiring more devices, for example the cascode and cascade amplifiers, or by feedback circuitry using operational amplifiers, for example a circuit like that in the adjacent figure.

### Lower transconductance

The transconductance of the MOSFET decides its gain and is proportional to hole or electron mobility (depending on device type), at least for low drain voltages. As MOSFET size is reduced, the fields in the channel increase and the dopant impurity levels increase. Both changes reduce the carrier mobility, and hence the transconductance. As channel lengths are reduced without proportional reduction in drain voltage, raising the electric field in the channel, the result is velocity saturation of the carriers, limiting the current and the transconductance.

### Interconnect capacitance

Traditionally, switching time was roughly proportional to the gate capacitance of gates. However, with transistors becoming smaller and more transistors being placed on the chip, interconnect capacitance (the capacitance of the metal-layer connections between different parts of the chip) is becoming a large percentage of capacitance. Signals have to travel through the interconnect, which leads to increased delay and lower performance.

### Heat production

The ever-increasing density of MOSFETs on an integrated circuit creates problems of substantial localized heat generation that can impair circuit operation. Circuits operate more slowly at high temperatures, and have reduced reliability and shorter lifetimes. Heat sinks and other cooling devices and methods are now required for many integrated circuits including microprocessors. Power MOSFETs are at risk of thermal runaway. As their on-state resistance rises with temperature, if the load is approximately a constant-current load then the power loss rises correspondingly, generating further heat. When the heatsink is not able to keep the temperature low enough, the junction temperature may rise quickly and uncontrollably, resulting in destruction of the device.

### Process variations

With MOSFETs becoming smaller, the number of atoms in the silicon that produce many of the transistor's properties is becoming fewer, with the result that control of dopant numbers and placement is more erratic. During chip manufacturing, random process variations affect all transistor dimensions: length, width, junction depths, oxide thickness *etc.*, and become a greater percentage of overall transistor size as the transistor shrinks. The transistor characteristics become less certain, more statistical. The random nature of manufacture means we do not know which particular example MOSFETs actually will end up in a particular instance of the circuit. This uncertainty forces a less optimal design because the design must work for a great variety of possible component MOSFETs. See process variation, design for manufacturability, reliability engineering, and statistical process control.

### Modeling challenges

Modern ICs are computer-simulated with the goal of obtaining working circuits from the first manufactured lot. As devices are miniaturized, the complexity of the processing makes it difficult to predict exactly what the final devices look like, and modeling of physical processes becomes more challenging as well. In addition, microscopic variations in structure due simply to the probabilistic nature of atomic processes require statistical (not just deterministic) predictions. These factors combine to make adequate simulation and "right the first time" manufacture difficult.


## Other types

### Dual-gate

The dual-gate MOSFET has a tetrode configuration, where both gates control the current in the device. It is commonly used for small-signal devices in radio frequency applications where biasing the drain-side gate at constant potential reduces the gain loss caused by Miller effect, replacing two separate transistors in cascode configuration. Other common uses in RF circuits include gain control and mixing (frequency conversion). The *tetrode* description, though accurate, does not replicate the vacuum-tube tetrode. Vacuum-tube tetrodes, using a screen grid, exhibit much lower grid-plate capacitance and much higher output impedance and voltage gains than triode vacuum tubes. These improvements are commonly an order of magnitude (10 times) or considerably more. Tetrode transistors (whether bipolar junction or field-effect) do not exhibit improvements of such a great degree.

The FinFET is a double-gate silicon-on-insulator device, one of a number of geometries being introduced to mitigate the effects of short channels and reduce drain-induced barrier lowering. The *fin* refers to the narrow channel between source and drain. A thin insulating oxide layer on either side of the fin separates it from the gate. SOI FinFETs with a thick oxide on top of the fin are called *double-gate* and those with a thin oxide on top as well as on the sides are called *triple-gate* FinFETs.

### Depletion-mode

There are *depletion-mode* MOSFET devices, which are less commonly used than the standard *enhancement-mode* devices already described. These are MOSFET devices that are doped so that a channel exists even with zero voltage from gate to source. To control the channel, a negative voltage is applied to the gate (for an n-channel device), depleting the channel, which reduces the current flow through the device. In essence, the depletion-mode device is equivalent to a normally closed (on) switch, while the enhancement-mode device is equivalent to a normally open (off) switch.

Due to their low noise figure in the RF region, and better gain, these devices are often preferred to bipolars in RF front-ends such as in TV sets.

Depletion-mode MOSFET families include the BF960 by Siemens and Telefunken, and the BF980 in the 1980s by Philips (later to become NXP Semiconductors), whose derivatives are still used in AGC and RF mixer front-ends.

### Metal–insulator–semiconductor field-effect transistor (MISFET)

Metal–insulator–semiconductor field-effect-transistor, or *MISFET*, is a more general term than *MOSFET* and a synonym to *insulated-gate field-effect transistor* (IGFET). All MOSFETs are MISFETs, but not all MISFETs are MOSFETs.

The gate dielectric insulator in a MISFET is a substrate oxide (hence typically silicon dioxide) in a MOSFET, but other materials can also be employed. The gate dielectric lies directly below the gate electrode and above the channel of the MISFET. The term *metal* is historically used for the gate material, even though now it is usually highly doped polysilicon or some other non-metal.

Insulator types may be:

- Silicon dioxide, in silicon MOSFETs
- Organic insulators (e.g., undoped trans-polyacetylene; cyanoethyl pullulan, CEP), for organic-based FETs.

### NMOS logic

For devices of equal current driving capability, n-channel MOSFETs can be made smaller than p-channel MOSFETs, due to p-channel charge carriers (holes) having lower mobility than do n-channel charge carriers (electrons), and producing only one type of MOSFET on a silicon substrate is cheaper and technically simpler. These were the driving principles in the design of nMOS logic which uses n-channel MOSFETs exclusively. However, neglecting leakage current, unlike CMOS logic, nMOS logic consumes power even when no switching is taking place. With advances in technology, CMOS logic displaced nMOS logic in the mid-1980s to become the preferred process for digital chips.

### Power MOSFET

Power MOSFETs have a different structure. As with most power devices, the structure is vertical and not planar. Using a vertical structure, it is possible for the transistor to sustain both high blocking voltage and high current. The voltage rating of the transistor is a function of the doping and thickness of the N-epitaxial layer (see cross section), while the current rating is a function of the channel width (the wider the channel, the higher the current). In a planar structure, the current and breakdown voltage ratings are both a function of the channel dimensions (respectively width and length of the channel), resulting in inefficient use of the "silicon estate". With the vertical structure, the component area is roughly proportional to the current it can sustain, and the component thickness (actually the N-epitaxial layer thickness) is proportional to the breakdown voltage.

Power MOSFETs with lateral structure are mainly used in high-end audio amplifiers and high-power PA systems. Their advantage is a better behaviour in the saturated region (corresponding to the linear region of a bipolar transistor) than the vertical MOSFETs. Vertical MOSFETs are designed for switching applications.

### Double-diffused metal–oxide–semiconductor (DMOS)

There are *LDMOS* (lateral double-diffused metal oxide semiconductor) and *VDMOS* (vertical double-diffused metal oxide semiconductor). Most power MOSFETs are made using this technology.

### Radiation-hardened-by-design (RHBD)

Semiconductor sub-micrometer and nanometer electronic circuits are the primary concern for operating within the normal tolerance in harsh radiation environments like outer space. One of the design approaches for making a radiation-hardened-by-design (RHBD) device is enclosed-layout-transistor (ELT). Normally, the gate of the MOSFET surrounds the drain, which is placed in the center of the ELT. The source of the MOSFET surrounds the gate. Another RHBD MOSFET is called H-Gate. Both of these transistors have very low leakage currents with respect to radiation. However, they are large in size and take up more space on silicon than a standard MOSFET. In older STI (shallow trench isolation) designs, radiation strikes near the silicon oxide region cause the channel inversion at the corners of the standard MOSFET due to accumulation of radiation induced trapped charges. If the charges are large enough, the accumulated charges affect STI surface edges along the channel near the channel interface (gate) of the standard MOSFET. This causes a device channel inversion to occur along the channel edges, creating an off-state leakage path. Subsequently, the device turns on; this process severely degrades the reliability of circuits. The ELT offers many advantages, including an improvement of reliability by reducing unwanted surface inversion at the gate edges which occurs in the standard MOSFET. Since the gate edges are enclosed in ELT, there is no gate oxide edge (STI at gate interface), and thus the transistor off-state leakage is reduced very much. Low-power microelectronic circuits including computers, communication devices, and monitoring systems in space shuttles and satellites are very different from what is used on earth. They are radiation (high-speed atomic particles like proton and neutron, solar flare magnetic energy dissipation in Earth's space, energetic cosmic rays like X-ray, gamma ray etc.) tolerant circuits. These special electronics are designed by applying different techniques using RHBD MOSFETs to ensure safe space journeys and safe space-walks of astronauts.
