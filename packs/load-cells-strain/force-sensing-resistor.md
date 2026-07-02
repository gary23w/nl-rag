---
title: "Force-sensing resistor"
source: https://en.wikipedia.org/wiki/Force-sensing_resistor
domain: load-cells-strain
license: CC-BY-SA-4.0
tags: load cell, strain gauge, wheatstone bridge, force-sensing resistor
fetched: 2026-07-02
---

# Force-sensing resistor

A **force-sensing resistor** is a material whose resistance changes when a force, pressure or mechanical stress is applied. They are also known as **force-sensitive resistor** and are sometimes referred to by the initialism **FSR**.

## History

The technology of force-sensing resistors was invented and patented in 1977 by Franklin Eventoff. In 1985, Eventoff founded Interlink Electronics, a company based on his force-sensing-resistor (FSR). In 1987, Eventoff received the prestigious International IR 100 award for developing the FSR. In 2001, Eventoff founded a new company, Sensitronics, that he currently runs.

## Properties

Force-sensing resistors consist of a conductive polymer, which predictably changes resistance following applying force to its surface. They are normally supplied as a polymer sheet or ink that can be applied by screen printing. The sensing film consists of electrically conducting and non-conducting particles suspended in a matrix. The particles are sub-micrometre sizes formulated to reduce temperature dependence, improve mechanical properties and increase surface durability. Applying a force to the surface of the sensing film causes particles to touch the conducting electrodes, changing the film's resistance. As with all resistive-based sensors, force-sensing resistors require a relatively simple interface and can operate satisfactorily in moderately hostile environments. Compared to other force sensors, the advantages of FSRs are their size (thickness typically less than 0.5 mm), low cost, and good shock resistance. A disadvantage is their low precision: measurement results may differ by 10% and more. Force-sensing capacitors offer superior sensitivity and long-term stability, but require more complicated drive electronics.

## Operation principle of FSRs

There are two major operation principles in force-sensing resistors: percolation and quantum tunneling. Although both phenomena co-occur in the conductive polymer, one phenomenon dominates over the other depending on particle concentration. Particle concentration is also referred in the literature as the filler volume fraction $\phi$ . More recently, new mechanistic explanations have been established to explain the performance of force-sensing resistors; these are based on the property of contact resistance $R_{C}$ occurring between the sensor electrodes and the conductive polymer. Specifically the force induced transition from Sharvin contacts to conventional Holm contacts. The contact resistance, $R_{C}$ , plays an important role in the current conduction of force-sensing resistors in a twofold manner. First, for a given applied stress $\sigma$ , or force F , a plastic deformation occurs between the sensor electrodes and the polymer particles thus reducing the contact resistance. Second, the uneven polymer surface is flattened when subjected to incremental forces, and therefore, more contact paths are created; this causes an increment in the effective area for current conduction A . At a macroscopic scale, the polymer surface is smooth. However, under a scanning electron microscope, the conductive polymer is irregular due to agglomerations of the polymeric binder.

To date, no comprehensive model is capable of predicting all the non-linearities observed in force-sensing resistors. The multiple phenomena occurring in the conductive polymer turn out to be too complex such to embrace them all simultaneously; this condition is typical of systems encompassed within condensed matter physics. However, in most cases, the experimental behavior of force-sensing resistors can be grossly approximated to either the percolation theory or to the equations governing quantum tunneling through a rectangular potential barrier.

### Percolation in FSRs

The percolation phenomenon dominates in the conductive polymer when the particle concentration is above the percolation threshold $\phi _{c}$ . A force-sensing resistor operating based on percolation exhibits a positive coefficient of pressure, and therefore, an increment in the applied pressure causes an increment in the electrical resistance R , For a given applied stress $\sigma$ , the electrical resistivity $\rho$ of the conductive polymer can be computed from:

$\rho =\rho _{0}(\phi -\phi _{c})^{-x}$

where $\rho _{0}$ matches for a prefactor depending on the transport properties of the conductive polymer, and x is the critical conductivity exponent. Under percolation regime, the particles are separated from each other when mechanical stress is applied; this causes a net increment in the device's resistance.

### Quantum tunneling in FSRs

Quantum tunneling is the most common operation mode of force-sensing resistors. A conductive polymer operating on the basis of quantum tunneling exhibits a resistance decrement for incremental values of stress $\sigma$ . Commercial FSRs such as the FlexiForce, Interlink and Peratech sensors operate based on quantum tunneling. The Peratech sensors are also referred to in the literature as quantum tunnelling composite.

The quantum tunneling operation implies that the average inter-particle separation s is reduced when the conductive polymer is subjected to mechanical stress; such a reduction in s causes a probability increment for particle transmission according to the equations for a rectangular potential barrier. Similarly, the contact resistance $R_{C}$ is reduced amid larger applied forces. To operate based on quantum tunneling, particle concentration in the conductive polymer must be held below the percolation threshold $\phi _{c}$ .

Several authors have developed theoretical models for the quantum tunneling conduction of FSRs, some of the models rely upon the equations for particle transmission across a rectangular potential barrier. However, the practical usage of such equations is limited because they are stated in terms of electron energy, E , that follows a Fermi Dirac probability distribution, i.e., electron energy is not a priori determined or can not be set by the final user. The analytical derivation of the equations for a rectangular potential barrier including the Fermi Dirac distribution was found in the 60's by Simmons. Such equations relate the current density J with the external applied voltage across the sensor U . However, J is not straightforward measurable in practice, so the transformation $I=JA$ is usually applied in literature when dealing with FSRs.

Just as in the equations for a rectangular potential barrier, the Simmons' equations are piecewise regarding the magnitude of U , i.e., different expressions are stated depending on U and the height of the rectangular potential barrier $V_{a}$ . The simplest Simmons' equation relates I with U , s when $U\approx 0$ as next:

$I(U,s)={\frac {3A{\sqrt {2mV_{a}}}}{2s}}({\frac {e}{h}})^{2}U\exp(-{\frac {4{\pi }s}{h}}{\sqrt {2mV_{a}}})$

where $V_{a}$ is in units of electron volt, m , e are the electron's mass and charge respectively, and h is the Planck constant. The low voltage equation of the Simmons' model is fundamental for modeling the current conduction of FSRs. The most widely accepted model for tunneling conduction has been proposed by Zhang et al. based on such equation. By re-arranging the equation above, it is possible to obtain an expression for the conductive polymer resistance $R_{Pol}$ , where $R_{Pol}$ is given by the quotient $U/I$ according to the Ohm's law:

$R_{\it {Pol}}={\frac {s}{A{\sqrt {2mV_{a}}}}}({\frac {h}{e}})^{2}\exp({\frac {4{\pi }s}{h}}{\sqrt {2mV_{a}}})$

When the conductive polymer is fully unloaded, the following relationship can be stated between the inter-particle separation at rest state $s_{0}$ ,the filler volume fraction $\phi$ and particle diameter D :

$s_{0}=D{\Big [}{\Big (}{\frac {\pi }{6\phi }}{\Big )}^{\frac {1}{3}}-1{\Big ]}$

Similarly, the following relationship can be stated between the inter-particle separation s and stress $\sigma$

$s=s_{0}(1-{\frac {\sigma }{M}})$

where M is the Young's modulus of the conductive polymer. Finally, by combining all the equations above, the Zhang's model is obtained as next:

$R_{\it {Pol}}={\frac {D{\Big [}{\Big (}{\frac {\pi }{6\phi }}{\Big )}^{\frac {1}{3}}-1{\Big ]}(1-{\frac {\sigma }{M}})}{A{\sqrt {2mV_{a}}}}}{\big (}{\frac {h}{e}}{\big )}^{2}\exp {\Big (}{\frac {4{\pi }D}{h}}{\Big [}{\Big (}{\frac {\pi }{6\phi }}{\Big )}^{\frac {1}{3}}-1{\Big ]}(1-{\frac {\sigma }{M}}){\sqrt {2mV_{a}}}{\Big )}$

Although the model from Zhang et al. has been widely accepted by many authors, it has been unable to predict some experimental observations reported in force-sensing resistors. Probably, the most challenging phenomenon to predict is sensitivity degradation. When subjected to dynamic loading, some force-sensing resistors exhibit degradation in sensitivity. Up to date, a physical explanation for such a phenomenon has not been provided, but experimental observations and more complex modeling from some authors have demonstrated that sensitivity degradation is a voltage-related phenomenon that can be avoided by choosing an appropriate driving voltage in the experimental set-up.

The model proposed by Paredes-Madrid et al. uses the entire set of Simmons' equations and embraces the contact resistance within the model; this implies that the externally applied voltage to the sensor $V_{FSR}$ is split between the tunneling voltage $V_{bulk}$ and the voltage drop across the contact resistance $V_{Rc}$ as next:

$V_{FSR}=2V_{RC}+V_{bulk}$

By replacing sensor current I in the above expression, $V_{bulk}$ can be stated as a function of the contact resistance $Rc$ and I as next:

$V_{bulk}=V_{FSR}-2RcI$

and the contact resistance $R_{C}$ is given by:

$R_{C}=R_{\it {par}}+{\frac {R_{C}^{0}}{\sigma ^{k}}}$

where $R_{par}$ is the resistance of the conductive nano-particles and $R_{C}^{0}$ , k are experimentally determined factors that depend on the interface material between the conductive polymer and the electrode. Finally the expressions relating sensor current I with $V_{FSR}$ are piecewise functions just as the Simmons equations are:

When $V_{bulk}\approx 0$

$R_{\it {bulk}}={\frac {s_{0}(1-{\frac {\sigma }{M}})}{(A_{0}+A_{1}\sigma ^{A_{2}}){\sqrt {2mV_{a}}}}}({\frac {h}{e}})^{2}\exp({\frac {4{\pi }s_{0}(1-{\frac {\sigma }{M}})}{h}}{\sqrt {2mV_{a}}})$

When $V_{bulk}<V_{a}/e$

$I={\frac {(A_{0}+A_{1}\sigma ^{A_{2}})e}{2{\pi }hs_{0}^{2}(1-{\frac {\sigma }{M}})^{2}}}{\Bigg \{}(V_{a}-{\frac {V_{bulk}}{2}})\exp {\Bigg [}-{\frac {4{\pi }}{h}}s_{0}(1-{\frac {\sigma }{M}}){\sqrt {2m(V_{a}-{\frac {eV_{bulk}}{2}})}}{\Bigg ]}-(V_{a}+{\frac {V_{bulk}}{2}})\exp {\Bigg [}-{\frac {4{\pi }}{h}}s_{0}(1-{\frac {\sigma }{M}}){\sqrt {2m(V_{a}+{\frac {eV_{bulk}}{2}})}}{\Bigg ]}{\Bigg \}}$

When $V_{bulk}>V_{a}/e$

$I={\frac {2.2e^{3}V_{bulk}^{2}(A_{0}+A_{1}\sigma ^{A_{2}})}{8{\pi }hV_{a}s_{0}^{2}(1-{\frac {\sigma }{M}})^{2}}}{\Bigg \{}\exp {\Bigg [}-{\frac {8{\pi }s_{0}(1-{\frac {\sigma }{M}})}{2.96heV_{bulk}^{2}}}{\sqrt {2mV_{a}^{3}}}{\Bigg ]}-(1+{\frac {2eV_{bulk}}{V_{a}}})\exp {\Bigg [}-{\frac {8{\pi }s_{0}(1-{\frac {\sigma }{M}})}{2.96heV_{bulk}}}{\sqrt {2mV_{a}^{3}(1+{\frac {2eV_{bulk}}{V_{a}}})}}{\Bigg ]}{\Bigg \}}$

In the equations above, the effective area for tunneling conduction A is stated as an increasing function dependent on the applied stress $\sigma$ , and on coefficients $A_{0}$ , $A_{1}$ , $A_{2}$ to be experimentally determined. This formulation accounts for the increment in the number of conduction paths with stress:

$A=A_{0}+A_{1}\sigma ^{A_{2}}$

### Current research trends in FSRs

Although the above model is unable to describe the undesired phenomenon of sensitivity degradation, the inclusion of rheological models has predicted that drift can be reduced by choosing an appropriate sourcing voltage; experimental observations have supported this statement. Another approach to reduce drift is to employ non-aligned electrodes to minimize the effects of polymer creep. There is currently a great effort placed on improving the performance of FSRs with multiple different approaches: in-depth modeling of such devices in order to choose the most adequate driving circuit, changing the electrode configuration to minimize drift and/or hysteresis, investigating on new materials type such as carbon nanotubes, or solutions combining the aforesaid methods.

## Uses

Force-sensing resistors are commonly used to create pressure-sensing "buttons" and have applications in many fields, including musical instruments (such as the Sensel Morph), car occupancy sensors, artificial limbs, foot pronation systems, and portable electronics. They are also used in mixed or augmented reality systems as well as to enhance mobile interaction.
