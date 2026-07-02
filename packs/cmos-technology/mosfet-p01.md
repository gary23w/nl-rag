---
title: "MOSFET (part 1/2)"
source: https://en.wikipedia.org/wiki/MOSFET
domain: cmos-technology
license: CC-BY-SA-4.0
tags: cmos technology, mosfet transistor, finfet device, threshold voltage
fetched: 2026-07-02
part: 1/2
---

# MOSFET

In electronics, the **metal–oxide–semiconductor field-effect transistor** (**MOSFET**, **MOS-FET**, **MOS FET**, or **MOS transistor**) is a type of field-effect transistor (FET), most commonly fabricated by the controlled oxidation of silicon. It has an insulated gate, the voltage of which determines the conductivity of the device. This ability to change conductivity with the amount of applied voltage can be used for amplifying or switching electronic signals. The term *metal–insulator–semiconductor field-effect transistor* (*MISFET*) is almost synonymous with *MOSFET*. Another near-synonym is *insulated-gate field-effect transistor* (*IGFET*).

Physicist Julius Edgar Lilienfeld first proposed the concept of a field-effect transistor (FET) in 1925, but it was not possible to construct a working device at that time. The first working metal–oxide–semiconductor field-effect transistor (MOSFET) was invented in 1959 by engineers Mohamed Atalla and Dawon Kahng at Bell Labs. Their breakthrough—fabricating a practical field-effect transistor enabled by Atalla’s earlier work on silicon surface passivation and thermal oxidation—revolutionized electronics and paved the way for smaller and cheaper radios, calculators, computers, and other electronic devices.

The main advantage of a MOSFET is that it requires almost no input current to control the load current under steady-state or low-frequency conditions, especially compared to bipolar junction transistors (BJTs). However, at high frequencies or when switching rapidly, a MOSFET may require significant current to charge and discharge its gate capacitance. In an *enhancement mode* MOSFET, voltage applied to the gate terminal increases the conductivity of the device. In *depletion mode* transistors, voltage applied at the gate reduces the conductivity.

The "metal" in the name MOSFET is sometimes a misnomer, because the gate material can be a layer of polysilicon (polycrystalline silicon). Similarly, "oxide" in the name can also be a misnomer, as different dielectric materials are used with the aim of obtaining strong channels with smaller applied voltages.

The MOSFET is by far the most common transistor in digital circuits, as billions may be included in a memory chip or microprocessor. As MOSFETs can be made with either a p-type or n-type channel, complementary pairs of MOS transistors can be used to make switching circuits with very low power consumption, in the form of CMOS logic.


## History

The basic principle of the field-effect transistor was first filed as a patent by Julius Edgar Lilienfeld as a Canadian patent in 1925 and later as a U.S. patent in 1926. In 1934, inventor Oskar Heil independently patented a similar device in Europe.

In the 1940s, Bell Labs scientists William Shockley, John Bardeen and Walter Houser Brattain attempted to build a field-effect device which led to their discovery of the transistor effect. However, their structure failed to show the anticipated effects due to the problem of surface states: traps on the semiconductor surface that hold electrons immobile. With no surface passivation they were only able to build the BJT and thyristor transistors.

In 1955, Carl Frosch and Lincoln Derick accidentally grew a layer of silicon dioxide over the silicon wafer, for which they observed surface passivation effects. By 1957 Frosch and Derick, using masking and predeposition, were able to manufacture silicon dioxide field effect transistors; the first planar transistors, in which drain and source were adjacent at the same surface. They showed that silicon dioxide insulated, protected silicon wafers and prevented dopants from diffusing into the wafer. At Bell Labs, the importance of Frosch and Derick technique and transistors was immediately realized. Results of their work circulated around Bell Labs in the form of BTL memos before being published in 1957. At Shockley Semiconductor, Shockley had circulated the preprint of their article in December 1956 to all his senior staff, including Jean Hoerni, who would later invent the planar process in 1959 while at Fairchild Semiconductor.

After this, J.R. Ligenza and W.G. Spitzer studied the mechanism of thermally grown oxides, fabricated a high quality Si/SiO2 stack and published their results in 1960. Following this research, Mohamed Atalla and Dawon Kahng proposed a silicon MOS transistor in 1959 and successfully demonstrated a working MOS device with their Bell Labs team in 1960. Their team included E. E. LaBate and E. I. Povilonis who fabricated the device; M. O. Thurston, L. A. D'Asaro, and J. R. Ligenza who developed the diffusion processes, and H. K. Gummel and R. Lindner who characterized the device. This was a culmination of decades of field-effect research that began with Lilienfeld.

The first MOS transistor at Bell Labs was about 100 times slower than contemporary bipolar transistors and was initially seen as inferior. Nevertheless, Kahng pointed out several advantages of the device, notably ease of fabrication and its application in integrated circuits.


## Composition

Silicon remains the primary semiconductor in CMOS devices, but to enhance carrier mobility, manufacturers—most notably IBM and Intel—induce strain in the silicon channel by incorporating silicon-germanium (SiGe) in nearby regions or applying stress engineering techniques, thereby improving transistor performance without using SiGe alloys as the channel material itself.

Many semiconductors with better electrical properties than silicon, such as gallium arsenide, do not form good semiconductor-to-insulator interfaces, and thus are not suitable for MOSFETs. Research continues on creating insulators with acceptable electrical characteristics on other semiconductor materials.

To overcome the increase in power consumption due to gate current leakage, a high-κ dielectric is used instead of silicon dioxide for the gate insulator, while polysilicon is replaced by metal gates (e.g. Intel, 2009).

The gate is separated from the channel by a thin insulating layer, traditionally of silicon dioxide and later of silicon oxynitride. Some companies use a high-κ dielectric and metal gate combination in the 45 nanometer node.

When a voltage is applied between the gate and the source, the electric field generated penetrates through the oxide and creates an *inversion layer* or *channel* at the semiconductor-insulator interface. The inversion layer provides a channel through which current can pass between source and drain terminals. Varying the voltage between the gate and body modulates the conductivity of this layer and thereby controls the current flow between drain and source. This is known as enhancement mode.


## Operation

### Metal–oxide–semiconductor structure

The traditional metal–oxide–semiconductor (MOS) structure is obtained by growing a layer of silicon dioxide (SiO 2) on top of a silicon substrate, commonly by thermal oxidation and depositing a layer of metal or polycrystalline silicon (the latter is commonly used). As silicon dioxide is a dielectric material, its structure is equivalent to a planar capacitor, with one of the electrodes replaced by a semiconductor.

When a voltage is applied across a MOS structure, it modifies the distribution of charges in the semiconductor. If we consider a p-type semiconductor (with *N*A the density of acceptors, *p* the density of holes; *p = N*A in neutral bulk), a positive voltage, *V*G, from gate to body (see figure) creates a depletion layer by forcing the positively charged holes away from the gate-insulator/semiconductor interface, leaving exposed a carrier-free region of immobile, negatively charged acceptor ions (see doping). If *V*G is high enough, a high concentration of negative charge carriers forms in an *inversion layer* located in a thin layer next to the interface between the semiconductor and the insulator.

Conventionally, the gate voltage at which the volume density of electrons in the inversion layer is the same as the volume density of holes in the body is called the threshold voltage. When the voltage between transistor gate and source (*V*G) exceeds the threshold voltage (*V*th), the difference is known as overdrive voltage.

This structure with p-type body is the basis of the n-type MOSFET, which requires the addition of n-type source and drain regions.

### MOS capacitors and band diagrams

The MOS capacitor structure is the heart of the MOSFET. Consider a MOS capacitor where the silicon base is of p-type. If a positive voltage is applied at the gate, holes which are at the surface of the p-type substrate will be repelled by the electric field generated by the voltage applied. At first, the holes will simply be repelled and what will remain on the surface will be immobile (negative) atoms of the acceptor type, which creates a depletion region on the surface. A hole is created by an acceptor atom, e.g., boron, which has one less electron than a silicon atom. Holes are not actually repelled, being non-entities; electrons are attracted by the positive field, and fill these holes. This creates a depletion region where no charge carriers exist because the electron is now fixed onto the atom and immobile.

As the voltage at the gate increases, there will be a point at which the surface above the depletion region will be converted from p-type into n-type, as electrons from the bulk area will start to get attracted by the larger electric field. This is known as *inversion*. The threshold voltage at which this conversion happens is one of the most important parameters in a MOSFET.

In the case of a p-type MOSFET, bulk inversion happens when the intrinsic energy level at the surface becomes smaller than the Fermi level at the surface. This can be seen on a band diagram. The Fermi level defines the type of semiconductor in discussion. If the Fermi level is equal to the Intrinsic level, the semiconductor is of intrinsic, or pure type. If the Fermi level lies closer to the conduction band (valence band) then the semiconductor type will be of n-type (p-type).

When the gate voltage is increased in a positive sense (for the given example), this will shift the intrinsic energy level band so that it will curve downwards towards the valence band. If the Fermi level lies closer to the valence band (for p-type), there will be a point when the Intrinsic level will start to cross the Fermi level and when the voltage reaches the threshold voltage, the intrinsic level does cross the Fermi level, and that is what is known as inversion. At that point, the surface of the semiconductor is inverted from p-type into n-type.

If the Fermi level lies above the intrinsic level, the semiconductor is of n-type, therefore at inversion, when the intrinsic level reaches and crosses the Fermi level (which lies closer to the valence band), the semiconductor type changes at the surface as dictated by the relative positions of the Fermi and intrinsic energy levels.

### Structure and channel formation

A MOSFET is based on the modulation of charge concentration by a MOS capacitance between a *body* electrode and a *gate* electrode located above the body and insulated from all other device regions by a gate dielectric layer. If dielectrics other than an oxide are employed, the device may be referred to as a metal-insulator-semiconductor FET (MISFET). Compared to the MOS capacitor, the MOSFET includes two additional terminals (*source* and *drain*), each connected to individual highly doped regions that are separated by the body region. These regions can be either p or n type, but they must both be of the same type, and of opposite type to the body region. The source and drain (unlike the body) are highly doped as signified by a "+" sign after the type of doping.

If the MOSFET is an n-channel or nMOS FET, then the source and drain are *n+* regions and the body is a *p* region. If the MOSFET is a p-channel or pMOS FET, then the source and drain are *p+* regions and the body is a *n* region. The source is so named because it is the source of the charge carriers (electrons for n-channel, holes for p-channel) that flow through the channel; similarly, the drain is where the charge carriers leave the channel.

The occupancy of the energy bands in a semiconductor is set by the position of the Fermi level relative to the semiconductor energy-band edges.

With sufficient gate voltage, the valence band edge is driven far from the Fermi level, and holes from the body are driven away from the gate.

At larger gate bias still, near the semiconductor surface the conduction band edge is brought close to the Fermi level, populating the surface with electrons in an *inversion layer* or *n-channel* at the interface between the p region and the oxide. This conducting channel extends between the source and the drain, and current is conducted through it when a voltage is applied between the two electrodes. Increasing the voltage on the gate leads to a higher electron density in the inversion layer and therefore increases the current flow between the source and drain. For gate voltages below the threshold value, the channel is lightly populated, and only a very small subthreshold leakage current can flow between the source and the drain.

When a negative gate-source voltage (positive source-gate) is applied, it creates a *p-channel* at the surface of the n region, analogous to the n-channel case, but with opposite polarities of charges and voltages. When a voltage less negative than the threshold value (a negative voltage for the p-channel) is applied between gate and source, the channel disappears and only a very small subthreshold current can flow between the source and the drain. The device may comprise a silicon on insulator device in which a buried oxide is formed below a thin semiconductor layer. If the channel region between the gate dielectric and the buried oxide region is very thin, the channel is referred to as an ultrathin channel region with the source and drain regions formed on either side in or above the thin semiconductor layer. Other semiconductor materials may be employed. When the source and drain regions are formed above the channel in whole or in part, they are referred to as raised source/drain regions.

| Parameter | nMOS FET | pMOS FET |   |
|---|---|---|---|
| Source/drain type | n-type | p-type |   |
| Channel type(MOS capacitor) | n-type | p-type |   |
| Gatetype | Polysilicon | n+ | p+ |
| Metal | φm ~ Si conduction band | φm ~ Si valence band |   |
| Well type | p-type | n-type |   |
| Threshold voltage, *V*th | Positive (enhancement)Negative (depletion) | Negative (enhancement)Positive (depletion) |   |
| Band-bending | Downwards | Upwards |   |
| Inversion layer carriers | Electrons | Holes |   |
| Substrate type | p-type | n-type |   |

### Modes of operation

The operation of a MOSFET can be separated into three different modes, depending on the device's threshold voltage ( $V_{\text{th}}$ ), gate-to-source voltage ( $V_{\text{GS}}$ ), and drain-to-source voltage ( $V_{\text{DS}}$ ). In the following discussion, a simplified algebraic model is used. Modern MOSFET characteristics are more complex than the algebraic model presented here.

For an *enhancement-mode, n-channel MOSFET*, the three operational modes are:

#### Cutoff, subthreshold, and weak-inversion mode

Criterion: $V_{\text{GS}}<V_{\text{th}}.$

According to the basic threshold model, the transistor is turned off, and there is no conduction between drain and source. A more accurate model considers the effect of thermal energy on the Fermi–Dirac distribution of electron energies which allow some of the more energetic electrons at the source to enter the channel and flow to the drain. This results in a subthreshold current that is an exponential function of gate-source voltage. While the current between drain and source should ideally be zero when the transistor is being used as a turned-off switch, there is a weak-inversion current, sometimes called subthreshold leakage.

In weak inversion where the source is tied to bulk, the current varies exponentially with $V_{\text{GS}}$ as given approximately by:

$I_{\text{D}}\approx I_{\text{D0}}e^{\frac {V_{\text{GS}}-V_{\text{th}}}{nV_{\text{T}}}},$

where:

- $I_{\text{D0}}$ is the current when $V_{\text{GS}}{=}V_{\text{th}}$ ,
- $V_{\text{T}}{=}kT/q$ is the thermal voltage, and
- n is the slope factor given by:

$n=1+{\frac {C_{\text{dep}}}{C_{\text{ox}}}},$

where $C_{\text{dep}}$ is the capacitance of the depletion layer and $C_{\text{ox}}$ is the capacitance of the oxide layer. This equation is generally used, but is only an adequate approximation for the source tied to the bulk. For the source not tied to the bulk, the subthreshold equation for drain current in saturation is

$I_{\text{D}}\approx I_{\text{D0}}e^{\frac {V_{\text{G}}-V_{\text{th}}}{nV_{\text{T}}}}e^{-{\frac {V_{\text{S}}}{V_{\text{T}}}}}.$

In a long-channel device, there is no drain voltage dependence of the current once $V_{\text{DS}}\gg V_{\text{T}}$ , but as channel length is reduced drain-induced barrier lowering introduces drain voltage dependence that depends in a complex way upon the device geometry (for example, the channel doping, the junction doping and so on). Frequently, threshold voltage *V*th for this mode is defined as the gate voltage at which a selected value of current *I*D0 occurs, for example, *I*D0 = 1 μA, which may not be the same *V*th-value used in the equations for the following modes.

Some micropower analog circuits are designed to take advantage of subthreshold conduction. By working in the weak-inversion region, the MOSFETs in these circuits deliver the highest possible transconductance-to-current ratio, namely: $g_{m}/I_{\text{D}}=1/\left(nV_{\text{T}}\right)$ , almost that of a bipolar transistor.

The subthreshold *I–V curve* depends exponentially upon threshold voltage, introducing a strong dependence on any manufacturing variation that affects threshold voltage; for example: variations in oxide thickness, junction depth, or body doping that change the degree of drain-induced barrier lowering. The resulting sensitivity to fabricational variations complicates optimization for leakage and performance.

#### Triode mode or linear region (also known as the ohmic mode)

Criteria: $V_{\text{GS}}>V_{\text{th}}$ and $V_{\text{DS}}<(V_{\text{GS}}-V_{\text{th}}).$

The transistor is turned on, and a channel has been created which allows current between the drain and the source. The MOSFET operates like a resistor, controlled by the gate voltage relative to both the source and drain voltages. The current from drain to source is modeled as:

$I_{\text{D}}=\mu _{n}C_{\text{ox}}{\frac {W}{L}}\left(\left(V_{\text{GS}}-V_{\rm {th}}\right)V_{\text{DS}}-{\frac {{V_{\text{DS}}}^{2}}{2}}\right),$

where $\mu _{n}$ is the charge-carrier effective mobility, W is the gate width, L is the gate length and $C_{\text{ox}}$ is the gate oxide capacitance per unit area. The transition from the exponential subthreshold region to the triode region is not as sharp as the equations suggest.

#### Saturation or active mode

Criteria: $V_{\text{GS}}>V_{\text{th}}$ and $V_{\text{DS}}\geq (V_{\text{GS}}-V_{\text{th}}).$

The switch is turned on, and a channel has been created, which allows current between the drain and source. Since the drain voltage is higher than the source voltage, the electrons spread out, and conduction is not through a narrow channel but through a broader, two- or three-dimensional current distribution extending away from the interface and deeper in the substrate. The onset of this region is also known as pinch-off to indicate the lack of channel region near the drain. Although the channel does not extend the full length of the device, the electric field between the drain and the channel is very high, and conduction continues. The drain current is now weakly dependent upon drain voltage and controlled primarily by the gate-source voltage, and modeled approximately as:

$I_{\text{D}}={\frac {\mu _{n}C_{\text{ox}}}{2}}{\frac {W}{L}}\left[V_{\text{GS}}-V_{\text{th}}\right]^{2}\left[1+\lambda V_{\text{DS}}\right].$

The additional factor involving λ, the channel-length modulation parameter, models current dependence on drain voltage due to the Early effect, or channel length modulation. According to this equation, a key design parameter, the MOSFET transconductance is:

$g_{m}={\frac {\partial I_{D}}{\partial V_{\text{GS}}}}={\frac {2I_{\text{D}}}{V_{\text{GS}}-V_{\text{th}}}}={\frac {2I_{\text{D}}}{V_{\text{ov}}}},$

where the combination *V*ov = *V*GS − *V*th is called the overdrive voltage, and where *V*DSsat = *V*GS − *V*th accounts for a small discontinuity in $I_{\text{D}}$ which would otherwise appear at the transition between the triode and saturation regions.

Another key design parameter is the MOSFET output resistance *rout* given by:

$r_{\text{out}}={\frac {1}{\lambda I_{\text{D}}}}\,.$

Note: *r*out is the inverse of *g*DS, where $g_{\text{DS}}={\frac {\partial I_{\text{DS}}}{\partial V_{\text{DS}}}}$ . *I*D is the expression in the saturation region.

If λ is taken as zero, an infinite output resistance of the device results that leads to unrealistic circuit predictions, particularly in analog circuits.

As the channel length becomes very short, these equations become quite inaccurate. New physical effects arise. For example, carrier transport in the active mode may become limited by velocity saturation. When velocity saturation dominates, the saturation drain current is more nearly linear than quadratic in *V*GS. At even shorter lengths, carriers transport with near zero scattering, known as quasi-ballistic transport. In the ballistic regime, the carriers travel at an injection velocity that may exceed the saturation velocity and approaches the Fermi velocity at high inversion charge density. In addition, drain-induced barrier lowering increases off-state (cutoff) current and requires an increase in threshold voltage to compensate, which in turn reduces the saturation current.

### Body effect

The occupancy of the energy bands in a semiconductor is set by the position of the Fermi level relative to the semiconductor energy-band edges. Application of a source-to-substrate reverse bias of the source-body pn-junction introduces a split between the Fermi levels for electrons and holes, moving the Fermi level for the channel further from the band edge, lowering the occupancy of the channel. The effect is to increase the gate voltage necessary to establish the channel, as seen in the figure. This change in channel strength by application of reverse bias is called the "body effect".

Using an nMOS example, the gate-to-body bias *V*GB positions the conduction-band energy levels, while the source-to-body bias VSB positions the electron Fermi level near the interface, deciding occupancy of these levels near the interface, and hence the strength of the inversion layer or channel.

The body effect upon the channel can be described using a modification of the threshold voltage, approximated by the following equation:

$V_{\text{TB}}=V_{T0}+\gamma \left({\sqrt {V_{\text{SB}}+2\varphi _{B}}}-{\sqrt {2\varphi _{B}}}\right),$

where *V*TB is the threshold voltage with substrate bias present, and *V*T0 is the zero-*V*SB value of threshold voltage, $\gamma$ is the body effect parameter, and 2*φ*B is the approximate potential drop between surface and bulk across the depletion layer when *V*SB = 0 and gate bias is sufficient to ensure that a channel is present. As this equation shows, a reverse bias *V*SB > 0 causes an increase in threshold voltage *V*TB and therefore demands a larger gate voltage before the channel populates.

The body can be operated as a second gate, and is sometimes referred to as the "back gate"; the body effect is sometimes called the "back-gate effect".


## Circuit symbols

A variety of symbols are used for the MOSFET. The basic design is generally a line for the channel with the source and drain leaving it at right angles and then bending back at right angles into the same direction as the channel. Sometimes three line segments are used for enhancement mode and a solid line for depletion mode (see depletion and enhancement modes). Another line is drawn parallel to the channel for the gate.

The *bulk* or *body* connection, if shown, is shown connected to the back of the channel with an arrow indicating pMOS or nMOS. This arrow always points from P to N, so an nMOS (N-channel in P-well or P-substrate) has the arrow pointing from the bulk to the channel. Typically the bulk is internally connected to the source (as is generally the case with discrete devices), in which case the bulk end of the arrow will have a line drawn between it and the source to explicitly show this connection. Some symbols will also explicitly show the MOSFET's *intrinsic body diode* along an outer (and sometimes dotted, as may be done for parasitic elements) path between drain and source. Note that tying the bulk to the source is by no means the only important configuration. In general, the MOSFET is a four-terminal device. In integrated circuits, many of the MOSFETs share a body connection, not necessarily connected to the source terminals of all the transistors.

If the bulk is not shown (as is often the case in IC design as they are generally common bulk) an inversion symbol is sometimes used to indicate pMOS. Alternatively, as is done with bipolar transistors, an arrow on the MOSFET's source may indicate the direction of conventional current: pointing out for nMOS, in for pMOS.

In the following symbols for JFETs, enhancement-mode MOSFETs, and depletion-mode MOSFETs, the orientation of the symbols (most significantly the position of source relative to drain) is such that more positive voltages appear higher on the page than less positive voltages, implying conventional current flowing "down" the page:

|   | JFET | Enhancement-mode MOSFET | Depletion-mode MOSFET |   |   |   |
|---|---|---|---|---|---|---|
| Bulk explicitly tied to source | Exposed bulk terminal | Bulk connection not shown | Bulk explicitly tied to source |   |   |   |
| P-channel |   |   |   |   |   |   |
| N-channel |   |   |   |   |   |   |

In schematics where G, S, D are not labeled, the detailed features of the symbol indicate which terminal is source and which is drain. For enhancement-mode and depletion-mode MOSFET symbols (in columns two and five), the source terminal is the one connected to the triangle. Additionally, in this diagram, the gate is shown as an "L" shape, whose input leg is closer to S than D, also indicating which is which. However, these symbols are often drawn with a T-shaped gate (as elsewhere on this page), so it is the triangle which must be relied upon to indicate the source terminal.


## Applications

Digital integrated circuits such as microprocessors and memory devices contain thousands to billions of integrated MOSFETs on each device, providing the basic switching functions required to implement logic gates and data storage. Discrete devices are widely used in applications such as switch mode power supplies, variable-frequency drives and other power electronics applications where each device may be switching thousands of watts. Radio-frequency amplifiers up to the UHF spectrum use MOSFET transistors as analog signal and power amplifiers. Radio systems also use MOSFETs as oscillators, or mixers to convert frequencies. MOSFET devices are also applied in audio-frequency power amplifiers for public address systems, sound reinforcement and home and automobile sound systems

### MOS integrated circuits

Following the development of clean rooms to reduce contamination to levels never before thought necessary, and of photolithography and the planar process to allow circuits to be made in very few steps, the Si–SiO2 system possessed the technical attractions of low cost of production (on a per circuit basis) and ease of integration. Largely because of these two factors, the MOSFET has become the most widely used type of transistor in the Institution of Engineering and Technology (IET).

General Micro-electronics introduced the first commercial MOS integrated circuit in 1964. Additionally, the method of coupling two complementary MOSFETs (P-channel and N-channel) into one high/low switch, known as CMOS, means that digital circuits dissipate very little power except when actually switched.

The earliest microprocessors starting in 1970 were all MOS microprocessors, fabricated entirely from PMOS logic or fabricated entirely from nMOS logic. In the 1970s, MOS microprocessors were often contrasted with CMOS microprocessors and bipolar bit-slice processors.

### CMOS circuits

The MOSFET is used in digital complementary metal–oxide–semiconductor (CMOS) logic, which uses p- and n-channel MOSFETs as building blocks. Overheating is a major concern in integrated circuits since ever more transistors are packed into ever smaller chips. CMOS logic reduces power consumption because no current flows (ideally), and thus no power is consumed, except when the inputs to logic gates are being switched. CMOS accomplishes this current reduction by complementing every nMOS FET with a pMOS FET and connecting both gates and both drains together. A high voltage on the gates will cause the nMOS FET to conduct and the pMOS FET not to conduct and a low voltage on the gates causes the reverse. During the switching time as the voltage goes from one state to another, both MOSFETs will conduct briefly. This arrangement greatly reduces power consumption and heat generation.

#### Digital

The growth of digital technologies like the microprocessor has provided the motivation to advance MOSFET technology faster than any other type of silicon-based transistor. A big advantage of MOSFETs for digital switching is that the oxide layer between the gate and the channel prevents DC current from flowing through the gate, further reducing power consumption and giving a very large input impedance. The insulating oxide between the gate and channel effectively isolates a MOSFET in one logic stage from earlier and later stages, which allows a single MOSFET output to drive a considerable number of MOSFET inputs. Bipolar transistor-based logic (such as TTL) does not have such a high fanout capacity. This isolation also makes it easier for the designers to ignore to some extent loading effects between logic stages independently. That extent is defined by the operating frequency: as frequencies increase, the input impedance of the MOSFETs decreases.

#### Analog

The MOSFET's advantages in digital circuits do not translate into supremacy in all analog circuits. The two types of circuit draw upon different features of transistor behavior. Digital circuits switch, spending most of their time either fully on or fully off. The transition from one to the other is only of concern with regards to speed and charge required. Analog circuits depend on operation in the transition region where small changes to *V*gs can modulate the output (drain) current. The JFET and bipolar junction transistor (BJT) are preferred for accurate matching (of adjacent devices in integrated circuits), higher transconductance and certain temperature characteristics which simplify keeping performance predictable as circuit temperature varies.

Nevertheless, MOSFETs are widely used in many types of analog circuits because of their own advantages (zero gate current, high and adjustable output impedance and improved robustness vs. BJTs which can be permanently degraded by even lightly breaking down the emitter-base). The characteristics and performance of many analog circuits can be scaled up or down by changing the sizes (length and width) of the MOSFETs used. By comparison, bipolar transistors follow a different scaling law. MOSFETs' ideal characteristics regarding gate current (zero) and drain-source offset voltage (zero) also make them nearly ideal switch elements, and also make switched capacitor analog circuits practical. In their linear region, MOSFETs can be used as precision resistors, which can have a much higher controlled resistance than BJTs. In high power circuits, MOSFETs sometimes have the advantage of not suffering from thermal runaway as BJTs do. This means that complete analog circuits can be made on a silicon chip in a much smaller space and with simpler fabrication techniques. MOSFETS are ideally suited to switch inductive loads because of tolerance to inductive kickback.

Some ICs combine analog and digital MOSFET circuitry on a single mixed-signal integrated circuit, making the needed board space even smaller. This creates a need to isolate the analog circuits from the digital circuits on a chip level, leading to the use of isolation rings and silicon on insulator (SOI). Since MOSFETs require more space to handle a given amount of power than a BJT, fabrication processes can incorporate BJTs and MOSFETs into a single device. Mixed-transistor devices are called bi-FETs (bipolar FETs) if they contain just one BJT-FET and BiCMOS (bipolar-CMOS) if they contain complementary BJT-FETs. Such devices have the advantages of both insulated gates and higher current density.

### Analog switches

Bidirectional analog switches pass analog signals when on or block them (by presenting a high impedance) when off. The MOSFETs used are typically symmetrical, such that their drain and source exchange places depending on the relative voltages of their electrodes; at any moment, the source would be the more negative side for an nMOS or the more positive side for a pMOS. All of these switches are limited on what signals they can pass or stop by their gate-source, gate-drain and source–drain voltages; exceeding the voltage, current, or power limits will potentially damage the switch. See Power MOSFET subsection down below.

#### Single-type

This analog switch uses a four-terminal symmetrical MOSFET of either P or N type.

In the case of an n-type switch, the body is connected to the most negative supply (usually GND) and the gate is used as the switch control. Whenever the gate voltage exceeds the source voltage by at least a threshold voltage, the MOSFET conducts. The higher the voltage, the more the MOSFET can conduct. An nMOS switch passes all voltages less than Vgate − *V*threshold_nMOS, but passes lower voltages better than higher ones. When the switch is conducting, it typically operates in the linear (or ohmic) mode of operation, since the source and drain voltages will typically be nearly equal.

In the case of a pMOS, the body is connected to the most positive voltage, and the gate is brought to a lower potential to turn the switch on. The pMOS switch passes all voltages higher than Vgate − *V*threshold_pMOS (note: enhancement-mode pMOS FETs have a negative threshold voltage), but passes higher voltages better than lower ones.

#### Dual-type (CMOS)

This "complementary" or CMOS type of switch uses one pMOS and one nMOS FET connected in parallel to counteract the limitations of the single-type switch. When used in digital logic it is called a transmission gate. The FETs have their drains and sources connected in parallel, the body of the pMOS is connected to the high potential (Vpos in diagram) and the body of the nMOS is connected to the low potential (Vneg). To turn the switch on, the gate of the pMOS is driven to the low potential and the gate of the nMOS is driven to the high potential. For voltages between Vpos − *V*threshold_nMOS and Vneg − *V*threshold_pMOS, both FETs conduct the signal, though with the nMOS passing lower voltages better while the pMOS passes higher voltages better. For voltages less than Vneg − *V*threshold_pMOS, the nMOS conducts alone. For voltages greater than Vpos − *V*threshold_nMOS, the pMOS conducts alone.

The voltage limits for this switch are the gate-source, gate-drain and source-drain voltage limits for both FETs. Also, the pMOS is typically two to three times wider than the nMOS, so the switch will be balanced for speed in the two directions.

Tri-state circuitry sometimes incorporates a CMOS MOSFET switch on its output to provide for a low-ohmic, full-range output when on, and a high-ohmic, mid-level signal when off.


## Construction

### Gate material

The primary criterion for the gate material is that it is a good conductor. Highly doped polycrystalline silicon is an acceptable but certainly not ideal conductor, and also suffers from some more technical deficiencies in its role as the standard gate material. Nevertheless, there are several reasons favoring use of polysilicon:

1. The threshold voltage (and consequently the drain to source on-current) is modified by the work function difference between the gate material and channel material. Because polysilicon is a semiconductor, its work function can be modulated by adjusting the type and level of doping. Furthermore, because polysilicon has the same bandgap as the underlying silicon channel, it is quite straightforward to tune the work function to achieve low threshold voltages for both nMOS and pMOS devices. By contrast, the work functions of metals are not easily modulated, so tuning the work function to obtain low threshold voltages (LVT) becomes a significant challenge. Additionally, obtaining low-threshold devices on both pMOS and nMOS devices sometimes requires the use of different metals for each device type.
2. The silicon-SiO2 interface has been well studied and is known to have relatively few defects. By contrast many metal-insulator interfaces contain significant levels of defects which can lead to Fermi level pinning, charging, or other phenomena that ultimately degrade device performance.
3. In the MOSFET IC fabrication process, it is preferable to deposit the gate material prior to certain high-temperature steps in order to make better-performing transistors. Such high temperature steps would melt some metals, limiting the types of metal that can be used in a metal-gate-based process.

While polysilicon gates have been the de facto standard for the last twenty years, they do have some disadvantages which have led to their likely future replacement by metal gates. These disadvantages include:

- Polysilicon is not a great conductor (approximately 1000 times more resistive than metals) which reduces the signal propagation speed through the material. The resistivity can be lowered by increasing the level of doping, but even highly doped polysilicon is not as conductive as most metals. To improve conductivity further, sometimes a high-temperature metal such as tungsten, titanium, cobalt, and more recently nickel is alloyed with the top layers of the polysilicon. Such a blended material is called silicide. The silicide-polysilicon combination has better electrical properties than polysilicon alone and still does not melt in subsequent processing. Also the threshold voltage is not significantly higher than with polysilicon alone, because the silicide material is not near the channel. The process in which silicide is formed on both the gate electrode and the source and drain regions is sometimes called salicide, self-aligned silicide.
- When the transistors are extremely scaled down, it is necessary to make the gate dielectric layer very thin, around 1 nm in state-of-the-art technologies. A phenomenon observed here is the so-called poly depletion, where a depletion layer is formed in the gate polysilicon layer next to the gate dielectric when the transistor is in the inversion. To avoid this problem, a metal gate is desired. A variety of metal gates such as tantalum, tungsten, tantalum nitride, and titanium nitride are used, usually in conjunction with high-κ dielectrics. An alternative is to use fully silicided polysilicon gates, a process known as FUSI.

Present high performance CPUs use metal gate technology, together with high-κ dielectrics, a combination known as *high-κ, metal gate* (HKMG). The disadvantages of metal gates are overcome by a few techniques:

1. The threshold voltage is tuned by including a thin "work function metal" layer between the high-κ dielectric and the main metal. This layer is thin enough that the total work function of the gate is influenced by both the main metal and thin metal work functions (either due to alloying during annealing, or simply due to the incomplete screening by the thin metal). The threshold voltage thus can be tuned by the thickness of the thin metal layer.
2. High-κ dielectrics are now well studied, and their defects are understood.
3. HKMG processes exist that do not require the metals to experience high temperature anneals; other processes select metals that can survive the annealing step.

### Insulator

As devices are made smaller, insulating layers are made thinner, often through steps of thermal oxidation or localised oxidation of silicon (LOCOS). For nano-scaled devices, at some point tunneling of carriers through the insulator from the channel to the gate electrode takes place. To reduce the resulting leakage current, the insulator can be made thinner by choosing a material with a higher dielectric constant. To see how thickness and dielectric constant are related, note that Gauss's law connects field to charge as:

$Q=\kappa \epsilon _{0}E,$

with *Q* = charge density, κ = dielectric constant, ε0 = permittivity of empty space and *E* = electric field. From this law it appears the same charge can be maintained in the channel at a lower field provided κ is increased. The voltage on the gate is given by:

$V_{\text{G}}=V_{\text{ch}}+E\,t_{\text{ins}}=V_{\text{ch}}+{\frac {Qt_{\text{ins}}}{\kappa \epsilon _{0}}},$

with *V*G = gate voltage, *V*ch = voltage at channel side of insulator, and *t*ins = insulator thickness. This equation shows the gate voltage will not increase when the insulator thickness increases, provided κ increases to keep *t*ins / κ = constant (see the article on high-κ dielectrics for more detail, and the section in this article on gate-oxide leakage).

The insulator in a MOSFET is a dielectric which can in any event be silicon oxide, formed by LOCOS but many other dielectric materials are employed. The generic term for the dielectric is gate dielectric since the dielectric lies directly below the gate electrode and above the channel of the MOSFET.

### Junction design

The source-to-body and drain-to-body junctions are the object of much attention because of three major factors: their design affects the current–voltage (*I–V*) characteristics of the device, lowering output resistance, and also the speed of the device through the loading effect of the junction capacitances, and finally, the component of stand-by power dissipation due to junction leakage.

The drain induced barrier lowering of the threshold voltage and channel length modulation effects upon *I-V* curves are reduced by using shallow junction extensions. In addition, *halo* doping can be used, that is, the addition of very thin heavily doped regions of the same doping type as the body tight against the junction walls to limit the extent of depletion regions.

The capacitive effects are limited by using raised source and drain geometries that make most of the contact area border thick dielectric instead of silicon.

These various features of junction design are shown (with artistic license) in the figure.
