---
title: "Supercapacitor (part 1/4)"
source: https://en.wikipedia.org/wiki/Supercapacitor
domain: supercapacitors
license: CC-BY-SA-4.0
tags: supercapacitor cell, pseudocapacitance charge, equivalent series resistance, ragone plot
fetched: 2026-07-02
part: 1/4
---

# Supercapacitor

A **supercapacitor** (**SC**), also called an **ultracapacitor**, is a high-capacity capacitor, with a capacitance value much higher than solid-state capacitors but with lower voltage limits. It bridges the gap between electrolytic capacitors and rechargeable batteries. It typically stores 10 to 100 times more energy per unit mass or energy per unit volume than electrolytic capacitors, can accept and deliver charge much faster than batteries, and tolerates many more charge and discharge cycles than rechargeable batteries.

Unlike ordinary capacitors, supercapacitors do not use a conventional solid dielectric, but rather, they use electrostatic double-layer capacitance and electrochemical pseudocapacitance, both of which contribute to the total energy storage of the capacitor.

Supercapacitors are used in applications requiring many rapid charge/discharge cycles, rather than long-term compact energy storage: in automobiles, buses, trains, cranes, and elevators they are used for regenerative braking, short-term energy storage, or burst-mode power delivery. Smaller units are used as power backup for static random-access memory (SRAM).


## Background

The electrochemical charge storage mechanisms in solid media can be roughly (with some overlap) classified into 3 types:

- *Electrostatic double-layer capacitors* (*EDLCs*) use carbon electrodes or derivatives with much higher electrostatic double-layer capacitance than electrochemical pseudocapacitance, achieving separation of charge in a Helmholtz double layer at the interface between the surface of a conductive electrode and an electrolyte. The separation of charge is of the order of a few ångströms (0.3–0.8 nm), much smaller than in a conventional capacitor. The electric charge in EDLCs is stored in a two-dimensional interphase (surface) of an electronic conductor (e.g. carbon particle) and ionic conductor (electrolyte solution).
- *Batteries with solid electroactive materials* store charge in bulk solid phases by virtue of redox chemical reactions.
- *Electrochemical supercapacitors* (ECSCs) fall in between EDLCs and batteries. ECSCs use metal oxide or conducting polymer electrodes with a high amount of electrochemical pseudocapacitance additional to the double-layer capacitance. Pseudocapacitance is achieved by Faradaic electron charge-transfer with redox reactions, intercalation or electrosorption.

In solid-state capacitors, the mobile charges are electrons, and the gap between electrodes is a layer of a dielectric. In electrochemical double-layer capacitors, the mobile charges are solvated ions (cations and anions), and the effective thickness is determined on each of the two electrodes by their electrochemical double layer structure. In batteries the charge is stored in the bulk volume of solid phases, which have both electronic and ionic conductivities. In electrochemical supercapacitors, the charge storage mechanisms either combine the double-layer and battery mechanisms, or are based on mechanisms, which are intermediate between true double layer and true battery.


## History

In the early 1950s, General Electric engineers began experimenting with porous carbon electrodes in the design of capacitors, from the design of fuel cells and rechargeable batteries. Activated charcoal is an electrical conductor that is an extremely porous "spongy" form of carbon with a high specific surface area. In 1957 H. Becker developed a "Low voltage electrolytic capacitor with porous carbon electrodes". He believed that the energy was stored as a charge in the carbon pores as in the pores of the etched foils of electrolytic capacitors. Because the double layer mechanism was not known by him at the time, he wrote in the patent: "It is not known exactly what is taking place in the component if it is used for energy storage, but it leads to an extremely high capacity."

General Electric did not immediately pursue this work. In 1966 researchers at Standard Oil of Ohio (SOHIO) developed another version of the component as "electrical energy storage apparatus", while working on experimental fuel cell designs. The nature of electrochemical energy storage was not described in this patent. Even in 1970, the electrochemical capacitor patented by Donald L. Boos was registered as an electrolytic capacitor with activated carbon electrodes.

Early electrochemical capacitors used two aluminum foils covered with activated carbon (the electrodes) that were soaked in an electrolyte and separated by a thin porous insulator. This design gave a capacitor with a capacitance on the order of one farad, significantly higher than electrolytic capacitors of the same dimensions. This basic mechanical design remains the basis of most electrochemical capacitors.

SOHIO did not commercialize their invention, licensing the technology to NEC, who finally marketed the results as "supercapacitors" in 1978, to provide backup power for computer memory.

Between 1975 and 1980 Brian Evans Conway conducted extensive fundamental and development work on ruthenium oxide electrochemical capacitors. In 1991 he described the difference between "supercapacitor" and "battery" behaviour in electrochemical energy storage. In 1999 he defined the term "supercapacitor" to make reference to the increase in observed capacitance by surface redox reactions with faradaic charge transfer between electrodes and ions. His "supercapacitor" stored electrical charge partially in the Helmholtz double-layer and partially as result of faradaic reactions with "pseudocapacitance" charge transfer of electrons and protons between electrode and electrolyte. The working mechanisms of pseudocapacitors are redox reactions, intercalation and electrosorption (adsorption onto a surface). With his research, Conway greatly expanded the knowledge of electrochemical capacitors.

The market expanded slowly. That changed around 1978 as Panasonic marketed its Goldcaps brand. This product became a successful energy source for memory backup applications. Competition started only years later. In 1987 ELNA "Dynacap"s entered the market. First generation EDLC's had relatively high internal resistance that limited the discharge current. They were used for low current applications such as powering SRAM chips or for data backup.

At the end of the 1980s, improved electrode materials increased capacitance values. At the same time, the development of electrolytes with better conductivity lowered the equivalent series resistance (ESR) increasing charge/discharge currents. The first supercapacitor with low internal resistance was developed in 1982 for military applications through the Pinnacle Research Institute (PRI), and were marketed under the brand name "PRI Ultracapacitor". In 1992, Maxwell Laboratories (later Maxwell Technologies) took over this development. Maxwell adopted the term Ultracapacitor from PRI and called them "Boost Caps" to underline their use for power applications.

Since capacitors' energy content increases with the square of the voltage, researchers were looking for a way to increase the electrolyte's breakdown voltage. In 1994 using the anode of a 200 V high-voltage tantalum electrolytic capacitor, David A. Evans developed an "Electrolytic-Hybrid Electrochemical Capacitor". These capacitors combine features of electrolytic and electrochemical capacitors. They combine the high dielectric strength of an anode from an electrolytic capacitor with the high capacitance of a pseudocapacitive metal oxide (ruthenium (IV) oxide) cathode from an electrochemical capacitor, yielding a hybrid electrochemical capacitor. Evans' capacitors, coined Capattery, had an energy content about a factor of 5 higher than a comparable tantalum electrolytic capacitor of the same size. Their high costs limited them to specific military applications.

Recent developments include lithium-ion capacitors. These hybrid capacitors were pioneered by Fujitsu's FDK in 2007. They combine an electrostatic carbon electrode with a pre-doped lithium-ion electrochemical electrode. This combination increases the capacitance value. Additionally, the pre-doping process lowers the anode potential and results in a high cell output voltage, further increasing specific energy.

Research departments active in many companies and universities are working to improve characteristics such as specific energy, specific power, and cycle stability and to reduce production costs.


## Design

### Basic design

Electrochemical capacitors (supercapacitors) consist of two electrodes separated by an ion-permeable membrane (separator), and an electrolyte ionically connecting both electrodes. When the electrodes are polarized by an applied voltage, ions in the electrolyte form electric double layers of opposite polarity to the electrode's polarity. For example, positively polarized electrodes will have a layer of negative ions at the electrode/electrolyte interface along with a charge-balancing layer of positive ions adsorbing onto the negative layer. The opposite is true for the negatively polarized electrode.

Additionally, depending on electrode material and surface shape, some ions may permeate the double layer becoming specifically adsorbed ions and contribute with pseudocapacitance to the total capacitance of the supercapacitor.

### Capacitance distribution

The two electrodes form a series circuit of two individual capacitors ⁠ $C_{1}$ ⁠ and ⁠ $C_{2}$ ⁠. The total capacitance ⁠ $C_{\mathrm {total} }$ ⁠ is given by the formula $C_{\mathrm {total} }={\frac {C_{1}\cdot C_{2}}{C_{1}+C_{2}}}.$

Supercapacitors may have either symmetric or asymmetric electrodes. Symmetry implies that both electrodes have the same capacitance value, yielding a total capacitance of half the value of each single electrode (if ⁠ $C_{1}=C_{2}$ ⁠, then ⁠ $\textstyle C_{\mathrm {total} }={1 \over 2}C_{1}$ ⁠). For asymmetric capacitors, the total capacitance can be taken as that of the electrode with the smaller capacitance (if ⁠ $C_{1}\gg C_{2}$ ⁠, then ⁠ $C_{\mathrm {total} }\approx C_{2}$ ⁠).

### Storage principles

Electrochemical capacitors use the double-layer effect to store electric energy; however, this double-layer has no conventional solid dielectric to separate the charges. There are two storage principles in the electric double-layer of the electrodes that contribute to the total capacitance of an electrochemical capacitor:

- Double-layer capacitance, electrostatic storage of the electrical energy achieved by separation of charge in a Helmholtz double layer.
- Pseudocapacitance, electrochemical storage of the electrical energy. The original type uses faradaic redox reactions with charge-transfer.

Both capacitances are only separable by measurement techniques. The amount of charge stored per unit voltage in an electrochemical capacitor is primarily a function of the electrode size, although the amount of capacitance of each storage principle can vary extremely.

#### Electrical double-layer capacitance

Every electrochemical capacitor has two electrodes, mechanically separated by a separator, which are ionically connected to each other via the electrolyte. The electrolyte is a mixture of positive and negative ions dissolved in a solvent such as water. At each of the two electrode surfaces originates an area in which the liquid electrolyte contacts the conductive metallic surface of the electrode. This interface forms a common boundary among two different phases of matter, such as an insoluble solid electrode surface and an adjacent liquid electrolyte. In this interface occurs a very special phenomenon of the double layer effect.

Applying a voltage to an electrochemical capacitor causes both electrodes in the capacitor to generate electrical double-layers. These double-layers consist of two layers of charges: one electronic layer is in the surface lattice structure of the electrode, and the other, with opposite polarity, emerges from dissolved and solvated ions in the electrolyte. The two layers are separated by a monolayer of solvent molecules, e.g., for water as solvent by water molecules, called inner Helmholtz plane (IHP). Solvent molecules adhere by physical adsorption on the surface of the electrode and separate the oppositely polarized ions from each other, and can be idealised as a molecular dielectric. In the process, there is no transfer of charge between electrode and electrolyte, so the forces that cause the adhesion are not chemical bonds, but physical forces, e.g., electrostatic forces. The adsorbed molecules are polarized, but, due to the lack of transfer of charge between electrolyte and electrode, suffered no chemical changes.

The amount of charge in the electrode is matched by the magnitude of counter-charges in outer Helmholtz plane (OHP). This double-layer phenomena stores electrical charges as in a conventional capacitor. The double-layer charge forms a static electric field in the molecular layer of the solvent molecules in the IHP that corresponds to the strength of the applied voltage.

The double-layer serves approximately as the dielectric layer in a conventional capacitor, albeit with the thickness of a single molecule. Thus, the standard formula for conventional plate capacitors can be used to calculate their capacitance: $C=\varepsilon {\frac {A}{d}}.$

Accordingly, capacitance ⁠ C ⁠ is greatest in capacitors made from materials with a high permittivity ⁠ $\varepsilon$ ⁠, large electrode plate surface areas ⁠ A ⁠ and small distance between plates ⁠ d ⁠. As a result, double-layer capacitors have much higher capacitance values than conventional capacitors, arising from the extremely large surface area of activated carbon electrodes and the extremely thin double-layer distance on the order of a few ångströms (0.3–0.8 nm), of order of the Debye length.

Assuming that the minimum distance between the electrode and the charge accumulating region cannot be less than the typical distance between negative and positive charges in atoms of ~0.05 nm a general capacitance upper limit of ~18 μF/cm2 has been predicted for non-faradaic capacitors.

The main drawback of carbon electrodes of double-layer supercapacitors is small values of quantum capacitance which act in series with capacitance of ionic space charge. Therefore, further increase of density of capacitance in SCs can be connected with increasing of quantum capacitance of carbon electrode nanostructures.

The amount of charge stored per unit voltage in an electrochemical capacitor is primarily a function of the electrode size. The electrostatic storage of energy in the double-layers is linear with respect to the stored charge, and correspond to the concentration of the adsorbed ions. Also, while charge in conventional capacitors is transferred via electrons, capacitance in double-layer capacitors is related to the limited moving speed of ions in the electrolyte and the resistive porous structure of the electrodes. Since no chemical changes take place within the electrode or electrolyte, charging and discharging electric double-layers in principle is unlimited. Real supercapacitors lifetimes are only limited by electrolyte evaporation effects.

#### Electrochemical pseudocapacitance

Applying a voltage at the electrochemical capacitor terminals moves electrolyte ions to the opposite polarized electrode and forms a double-layer in which a single layer of solvent molecules acts as separator. Pseudocapacitance can originate when specifically adsorbed ions out of the electrolyte pervade the double-layer. This pseudocapacitance stores electrical energy by means of reversible faradaic redox reactions on the surface of suitable electrodes in an electrochemical capacitor with an electric double-layer. Pseudocapacitance is accompanied with an electron charge-transfer between electrolyte and electrode coming from a de-solvated and adsorbed ion whereby only one electron per charge unit is participating. This faradaic charge transfer originates by a very fast sequence of reversible redox, intercalation or electrosorption processes. The adsorbed ion has no chemical reaction with the atoms of the electrode (no chemical bonds arise) since only a charge-transfer take place.

The electrons involved in the faradaic processes are transferred to or from valence electron states (orbitals) of the redox electrode reagent. They enter the negative electrode and flow through the external circuit to the positive electrode where a second double-layer with an equal number of anions has formed. The electrons reaching the positive electrode are not transferred to the anions forming the double-layer, instead they remain in the strongly ionized and "electron hungry" transition-metal ions of the electrode's surface. As such, the storage capacity of faradaic pseudocapacitance is limited by the finite quantity of reagent in the available surface.

A faradaic pseudocapacitance only occurs together with a static double-layer capacitance, and its magnitude may exceed the value of double-layer capacitance for the same surface area by factor of 100, depending on the nature and the structure of the electrode, because all the pseudocapacitance reactions take place only with de-solvated ions, which are much smaller than solvated ion with their solvating shell. The amount of pseudocapacitance has a linear function within narrow limits determined by the potential-dependent degree of surface coverage of the adsorbed anions.

The ability of electrodes to accomplish pseudocapacitance effects by redox reactions, intercalation or electrosorption strongly depends on the chemical affinity of electrode materials to the ions adsorbed on the electrode surface as well as on the structure and dimension of the electrode pores. Materials exhibiting redox behavior for use as electrodes in pseudocapacitors are transition-metal oxides like RuO2, IrO2, or MnO2 inserted by doping in the conductive electrode material such as active carbon, as well as conducting polymers such as polyaniline or derivatives of polythiophene covering the electrode material.

The amount of electric charge stored in a pseudocapacitance is linearly proportional to the applied voltage. The unit of pseudocapacitance is farad, same as that of capacitance.

Although conventional battery-type electrode materials also use chemical reactions to store charge, they show very different electrical profiles, as the rate of discharge is limited by the speed of diffusion. Grinding those materials down to nanoscale frees them of the diffusion limit and give them a more pseudocapacitative behavior, making them *extrinsic pseudocapacitors*. Chodankar shows the representative voltage-capacity curves for bulk LiCoO2, nano LiCoO2, a redox pseudocapacitor (RuO2), and an intercalation pseudocapacitor (T−Nb2O5).

#### Asymmetric capacitors

Supercapacitors can also be made with different materials and principles at the electrodes. If both of those materials use a fast, supercapacitor-type reaction (capacitance or pseudocapacitance), the result is called an asymmetric capacitor. The two electrodes have different electric potentials; when combined with proper balancing, the result is improved energy density with no loss of lifespan or current capacity.

#### Hybrid capacitors

A number of newer supercapacitors are "hybrid": only one electrode uses a fast reaction (capacitance or pseudocapacitance), the other using a more "battery-like" (slower but higher-capacity) material. Hybrid capacitors combine the rapid charge/discharge kinetics of electric double-layer capacitors (EDLCs) with the high energy density of pseudocapacitive or battery-type electrodes. These systems bridge the gap between conventional capacitors and batteries, making them critical for applications requiring both power and energy density. For example, an EDLC anode can be combined with an activated carbon–Ni(OH)2 cathode, the latter being a slow faradaic material. The CV and GCD profiles of a hybrid capacitor have a shape between that of a battery and a supercapacitor, more similar to that of an SC. Hybrid capacitors have much higher energy density, but have inferior cycle life and current capacity owing to the slower electrode.

### Potential distribution

Conventional capacitors (also known as electrostatic capacitors), such as ceramic capacitors and film capacitors, consist of two electrodes separated by a dielectric material. When charged, the energy is stored in a static electric field that permeates the dielectric between the electrodes. The total energy increases with the amount of stored charge, which in turn correlates linearly with the potential (voltage) between the plates. The maximum potential difference between the plates (the maximal voltage) is limited by the dielectric's breakdown field strength. The same static storage also applies for electrolytic capacitors in which most of the potential decreases over the anode's thin oxide layer. The somewhat resistive liquid electrolyte (cathode) accounts for a small decrease of potential for "wet" electrolytic capacitors, while electrolytic capacitors with solid conductive polymer electrolyte this voltage drop is negligible.

In contrast, electrochemical capacitors (supercapacitors) consists of two electrodes separated by an ion-permeable membrane (separator) and electrically connected via an electrolyte. Energy storage occurs within the double-layers of both electrodes as a mixture of a double-layer capacitance and pseudocapacitance. When both electrodes have approximately the same resistance (internal resistance), the potential of the capacitor decreases symmetrically over both double-layers, whereby a voltage drop across the equivalent series resistance (ESR) of the electrolyte is achieved. For asymmetrical supercapacitors like hybrid capacitors the voltage drop between the electrodes could be asymmetrical. The maximum potential across the capacitor (the maximal voltage) is limited by the electrolyte decomposition voltage.

Both electrostatic and electrochemical energy storage in supercapacitors are linear with respect to the stored charge, just as in conventional capacitors. The voltage between the capacitor terminals is linear with respect to the amount of stored energy. Such linear voltage gradient differs from rechargeable electrochemical batteries, in which the voltage between the terminals remains independent of the amount of stored energy, providing a relatively constant voltage.

### Comparison with other storage technologies

Supercapacitors compete with electrolytic capacitors and rechargeable batteries, especially lithium-ion batteries. The following table compares the major parameters of the three main supercapacitor families with electrolytic capacitors and batteries.

Performance parameters of supercapacitors compared with electrolytic capacitors and lithium-ion batteries

Capacitor

Is

SC

?

Temp.

range,

(

°C

Tooltip degrees Celsius

)

Max.

voltage

(V)

Min.

voltage

(V)

Recharge cycles,

(×1,000)

Capacitance

,

(

F

Tooltip farad

)

Specific energy

,

(

Wh

Tooltip watt-hours

/kg)

Specific power

,

(

W

Tooltip watt

/g)

Self-discharge

time at room

temp.

Efficiency (%)

Working life at room

temp.

(

y

)

Aluminum

electrolytic

capacitors

No

−40 – +125

4 – 630

0

∞

≤ 2.7

0.01 – 0.3

> 100

short

(days)

99%

> 20

Double-layer

capacitors

(memory backup)

Yes

−40 – +70

1.2 – 3.3

0

100 –

1000

0.1 – 470

1.5 – 3.9

2 – 10

medium

(weeks)

95%

5 – 10

Pseudocapacitors

−20 – +70

2.2 – 3.3

100 –

1000

100 –

12

000

4 – 9

3 – 10

medium

(weeks)

95%

5 – 10

Hybrid (Li-ion)

−20 – +65

3.8 – 4.0

2.5

10 – 500

3 –

3300

37

3 – 14

long

(month)

90%

5 – 10

NTGS

EDLC

(experimental)

~4.0

> 20

206

32

Lithium-ion

batteries

No

−20 – +60

4.2

2.5

0.5 – 10

—

100 – 265

0.3 – 1.5

long

(month)

90%

3 – 5

Electrolytic capacitors feature nearly unlimited charge/discharge cycles, high dielectric strength (up to 550 V) and good frequency response as alternating current (AC) reactance in the lower frequency range. Supercapacitors can store 10 to 100 times more energy than electrolytic capacitors, but they do not support AC applications.

With regards to rechargeable batteries, supercapacitors feature higher peak currents, low cost per cycle, no danger of overcharging, good reversibility, non-corrosive electrolyte and low material toxicity. Batteries offer lower purchase cost and stable voltage under discharge, but require complex electronic control and switching equipment, with consequent energy loss and spark hazard given a short.


## Styles

Supercapacitors are made in different styles, such as flat with a single pair of electrodes, wound in a cylindrical case, or stacked in a rectangular case. Because they cover a broad range of capacitance values, the size of the cases can vary.

Supercapacitors are constructed with two metal foils (current collectors), each coated with an electrode material such as activated carbon, which serve as the power connection between the electrode material and the external terminals of the capacitor. Specifically to the electrode material is a very large surface area. In this example the activated carbon is electrochemically etched, so that the surface area of the material is about 100,000 times greater than the smooth surface. The electrodes are kept apart by an ion-permeable membrane (separator) used as an insulator to protect the electrodes against short circuits. This construction is subsequently rolled or folded into a cylindrical or rectangular shape and can be stacked in an aluminum can or an adaptable rectangular housing. The cell is then impregnated with a liquid or viscous electrolyte of organic or aqueous type. The electrolyte, an ionic conductor, enters the pores of the electrodes and serves as the conductive connection between the electrodes across the separator. Finally, the housing is hermetically sealed to ensure stable behavior over the specified lifetime.


## Types

Electrical energy is stored in supercapacitors via two storage principles, static double-layer capacitance and electrochemical pseudocapacitance; and the distribution of the two types of capacitance depends on the material and structure of the electrodes. There are three types of supercapacitors based on storage principle:

- *Double-layer capacitors* (*EDLCs*): with activated carbon electrodes or derivatives with much higher electrostatic double-layer capacitance than electrochemical pseudocapacitance
- *Pseudocapacitors*: with transition metal oxide or conducting polymer electrodes with a high electrochemical pseudocapacitance
- *Hybrid capacitors*: with asymmetric electrodes, one of which exhibits mostly electrostatic and the other mostly electrochemical capacitance, such as lithium-ion capacitors

Because double-layer capacitance and pseudocapacitance both contribute inseparably to the total capacitance value of an electrochemical capacitor, a correct description of these capacitors only can be given under the generic term. The concepts of supercapattery and supercabattery have been recently proposed to better represent those hybrid devices that behave more like the supercapacitor and the rechargeable battery, respectively.

The capacitance value of a supercapacitor is determined by two storage principles:

- Double-layer capacitance – electrostatic storage of the electrical energy achieved by separation of charge in a Helmholtz double layer at the interface between the surface of a conductor electrode and an electrolytic solution electrolyte. The separation of charge distance in a double-layer is on the order of a few ångströms (0.3–0.8 nm) and is static in origin.
- Pseudocapacitance – Electrochemical storage of the electrical energy, achieved by redox reactions, electrosorption or intercalation on the surface of the electrode by specifically adsorbed ions, that results in a reversible faradaic charge-transfer on the electrode.

Double-layer capacitance and pseudocapacitance both contribute inseparably to the total capacitance value of a supercapacitor. However, the ratio of the two can vary greatly, depending on the design of the electrodes and the composition of the electrolyte. Pseudocapacitance can increase the capacitance value by as much as a factor of ten over that of the double-layer by itself.

Electric double-layer capacitors (EDLC) are electrochemical capacitors in which energy storage predominantly is achieved by double-layer capacitance. In the past, all electrochemical capacitors were called "double-layer capacitors". Contemporary usage sees double-layer capacitors, together with pseudocapacitors, as part of a larger family of electrochemical capacitors called supercapacitors. They are also known as ultracapacitors.
