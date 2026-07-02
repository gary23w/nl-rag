---
title: "Fusion power (part 1/2)"
source: https://en.wikipedia.org/wiki/Fusion_power
domain: plasma-physics
license: CC-BY-SA-4.0
tags: plasma physics, magnetohydrodynamics simulation, debye length, plasma oscillation
fetched: 2026-07-02
part: 1/2
---

# Fusion power

**Fusion power** is a potential method of electric power generation from heat released by nuclear fusion reactions. In fusion, two light atomic nuclei combine to form a heavier nucleus and release energy. Devices that use this process are known as **fusion reactors**.

Research on fusion reactors began in the 1940s. As of 2025, the National Ignition Facility (NIF) in the United States is the only laboratory to have demonstrated a fusion energy gain factor above one, but efficiencies orders of magnitude higher are required to reach engineering breakeven (a net electricity-producing plant) or economic breakeven (where the net electricity pays for the plant's whole-life cost).

Thermonuclear fusion reactions require fuel in a plasma state and a confined environment with high temperature, pressure, and sufficient confinement time. The relationship between these parameters is expressed by the Lawson criterion. In stars, gravity provides the conditions for fusing hydrogen isotopes. Experimental reactors use deuterium and tritium, heavier isotopes of hydrogen, in a process known as DT fusion. This reaction forms a helium nucleus and an energetic neutron.

Fusion fuel is extremely energy-dense, but tritium is scarce on Earth and decays with a half-life of about 12.3 years. Future reactors plan to use lithium breeding blankets that generate tritium when exposed to neutron radiation.

Fusion offers advantages compared with nuclear fission. It produces minimal high-level radioactive waste and involves lower inherent safety risks. However, the process generates intense neutron radiation that gradually damages the inner walls of a reactor. Achieving sustained energy gain beyond breakeven and converting it efficiently into electricity remain major technical challenges.

Research focuses mainly on two methods: magnetic confinement fusion (MCF) and inertial confinement fusion (ICF). MCF devices use magnetic fields to contain plasma. Early concepts included the z-pinch, stellarator, and magnetic mirror, with the tokamak design becoming dominant after Soviet experiments in the 1960s. ICF compresses and heats small fuel pellets using high-energy lasers, developed primarily since the 1970s. The largest active projects are ITER in France and the National Ignition Facility in the United States. Commercial and academic teams are also studying alternatives such as magnetized target fusion and modern stellarator designs.


## Terminology

The terms "fusion experiment" and "fusion device" refer to the collection of technologies used for scientific investigation of plasma, and technical advancement. Not all are capable of, or routinely used for, producing thermonuclear reactions i.e. fusion.

The term "fusion reactor" is used interchangeably to mean the above experiments, or to mean a hypothetical power-producing version, at the center of a commercial power plant, requiring additions such as a breeding blanket and heat engine.


## Background

### Mechanism

Fusion reactions occur when two or more atomic nuclei come close enough for long enough that the nuclear force pulling them together exceeds the electrostatic force pushing them apart, fusing them into heavier nuclei. For nuclei heavier than iron-56, the reaction is endothermic, requiring an input of energy. The heavy nuclei bigger than iron have many more protons resulting in a greater repulsive force. For nuclei lighter than iron-56, the reaction is exothermic, releasing energy when they fuse. Since hydrogen has a single proton in its nucleus, it requires the least effort to attain fusion, and yields the most net energy output. Also, since it has one electron, hydrogen is the easiest fuel to fully ionize.

The repulsive electrostatic interaction between nuclei operates across larger distances than the strong force, which has a range of roughly one femtometer—the diameter of a proton or neutron. The fuel atoms must be supplied enough kinetic energy to approach one another closely enough for the strong force to overcome the electrostatic repulsion in order to initiate fusion. The "Coulomb barrier" is the quantity of kinetic energy required to move the fuel atoms near enough. Atoms can be heated to extremely high temperatures or accelerated in a particle accelerator to produce this energy.

An atom loses its electrons once it is heated past its ionization energy. The resultant bare nucleus is a type of ion. The result of this ionization is plasma, which is a heated cloud of bare nuclei and free electrons that were formerly bound to them. Plasmas are electrically conducting and magnetically controlled because the charges are separated. This is used by several fusion devices to confine the hot particles.

### Cross section

A reaction's cross section, denoted σ, measures the probability that a fusion reaction will happen. This depends on the relative velocity of the two nuclei. Higher relative velocities generally increase the probability, but the probability begins to decrease again at very high energies.

In a plasma, particle velocity can be characterized using a probability distribution. If the plasma is thermalized, the distribution looks like a Gaussian curve, or Maxwell–Boltzmann distribution. In this case, it is useful to use the average particle cross section over the velocity distribution. This is entered into the volumetric fusion rate:

$P_{\text{fusion}}=n_{A}n_{B}\langle \sigma v_{A,B}\rangle E_{\text{fusion}}$

where:

- $P_{\text{fusion}}$ is the energy made by fusion, per time and volume
- *n* is the number density of species A or B, of the particles in the volume
- $\langle \sigma v_{A,B}\rangle$ is the cross section of that reaction, average over all the velocities of the two species *v*
- $E_{\text{fusion}}$ is the energy released by that fusion reaction.

### Lawson criterion

The Lawson criterion considers the energy balance between the energy produced in fusion reactions to the energy being lost to the environment. In order to generate usable energy, a system would have to produce more energy than it loses. Lawson assumed an energy balance, shown below.

$P_{\text{out}}=\eta _{\text{capture}}\left(P_{\text{fusion}}-P_{\text{conduction}}-P_{\text{radiation}}\right)$

where:

- $P_{\text{out}}$ is the net power from fusion
- $\eta _{\text{capture}}$ is the efficiency of capturing the output of the fusion
- $P_{\text{fusion}}$ is the rate of energy generated by the fusion reactions
- $P_{\text{conduction}}$ is the conduction losses as energetic mass leaves the plasma
- $P_{\text{radiation}}$ is the radiation losses as energy leaves as light and neutron flux.

The rate of fusion, and thus Pfusion, depends on the temperature and density of the plasma. The plasma loses energy through conduction and radiation. Conduction occurs when ions, electrons, or neutrals impact other substances, typically a surface of the device, and transfer a portion of their kinetic energy to the other atoms. The rate of conduction is also based on the temperature and density. Radiation is energy that leaves the cloud as light. Radiation also increases with temperature as well as the mass of the ions. Fusion power systems must operate in a region where the rate of fusion is higher than the losses.

### Triple product: density, temperature, time

The Lawson criterion argues that a machine holding a thermalized and quasi-neutral plasma has to generate enough energy to overcome its energy losses. The amount of energy released in a given volume is a function of the temperature, and thus the reaction rate on a per-particle basis, the density of particles within that volume, and finally the confinement time, the length of time that energy stays within the volume. This is known as the "triple product": the plasma density, temperature, and confinement time.

In magnetic confinement, the density is low, on the order of a "good vacuum". For instance, in the ITER device the fuel density is about 1.0 × 1019 m−3, which is about one-millionth atmospheric density. This means that the temperature and/or confinement time must increase. Fusion-relevant temperatures have been achieved using a variety of heating methods that were developed in the early 1970s. In modern machines, as of 2019, the major remaining issue was the confinement time. Plasmas in strong magnetic fields are subject to a number of inherent instabilities, which must be suppressed to reach useful durations. One way to do this is to simply make the reactor volume larger, which reduces the rate of leakage due to classical diffusion. This is why ITER is so large.

In contrast, inertial confinement systems approach useful triple product values via higher density, and have short confinement intervals. In NIF, the initial frozen hydrogen fuel load has a density less than water that is increased to about 100 times the density of lead. In these conditions, the rate of fusion is so high that the fuel fuses in the microseconds it takes for the heat generated by the reactions to blow the fuel apart. Although NIF is also large, this is a function of its "driver" design, not inherent to the fusion process.

### Energy capture

Multiple approaches have been proposed to capture the energy that fusion produces. The simplest is to heat a fluid. The commonly targeted D–T reaction releases much of its energy as fast-moving neutrons. Electrically neutral, the neutron is unaffected by the confinement scheme. In most designs, it is captured in a thick "blanket" of lithium surrounding the reactor core. When struck by a high-energy neutron, the blanket heats up. It is then actively cooled with a working fluid that drives a turbine to produce power.

Another design proposed to use the neutrons to breed fission fuel in a blanket of nuclear waste, a concept known as a fission-fusion hybrid. In these systems, the power output is enhanced by the fission events, and power is extracted using systems like those in conventional fission reactors.

Designs that use other fuels, notably the proton-boron aneutronic fusion reaction, release much more of their energy in the form of charged particles. In these cases, power extraction systems based on the movement of these charges are possible. Direct energy conversion was developed at Lawrence Livermore National Laboratory (LLNL) in the 1980s as a method to maintain a voltage directly using fusion reaction products. This has demonstrated energy capture efficiency of 48 percent.


## Plasma behavior

Plasma is an ionized gas that conducts electricity. In bulk, it is modeled using magnetohydrodynamics, which is a combination of the Navier–Stokes equations governing fluids and Maxwell's equations governing how magnetic and electric fields behave. Fusion exploits several plasma properties, including:

- Self-organizing plasma conducts electric and magnetic fields. Its motions generate fields that can in turn contain it.
- Diamagnetic plasma can generate its own internal magnetic field. This can reject an externally applied magnetic field, making it diamagnetic.
- Magnetic mirrors can reflect plasma when it moves from a low to high density field.:24


## Methods

### Magnetic confinement

- Tokamak: The most well-developed and well-funded approach. This method drives hot plasma around in a magnetically confined torus, with an internal electric current. When completed, ITER will become the world's largest tokamak. As of September 2018 an estimated 226 experimental tokamaks were either planned, decommissioned or operating (50) worldwide.
  - Spherical tokamak: Also known as spherical torus. A variation on the tokamak with a spherical shape.
- Stellarator: Twisted rings of hot plasma. The stellarator attempts to create a natural twisted plasma path, using external magnets. Stellarators were developed by Lyman Spitzer in 1950 and evolved into four designs: Torsatron, Heliotron, Heliac and Helias. One example is Wendelstein 7-X, a German device. It is the world's largest stellarator.
- Internal rings: Stellarators create a twisted plasma using external magnets, while tokamaks do so using a current induced in the plasma. Several classes of designs provide this twist using conductors inside the plasma. Early calculations showed that collisions between the plasma and the supports for the conductors would remove energy faster than fusion reactions could replace it. Modern variations, including the Levitated Dipole Experiment (LDX), use a solid superconducting torus that is magnetically levitated inside the reactor chamber.
- Magnetic mirror: Developed by Richard F. Post and teams at Lawrence Livermore National Laboratory (LLNL) in the 1960s. Magnetic mirrors reflect plasma back and forth in a line. Variations included the Tandem Mirror, magnetic bottle and the biconic cusp. A series of mirror machines were built by the US government in the 1970s and 1980s, principally at LLNL. However, calculations in the 1970s estimated it was unlikely these would ever be commercially useful.
- Bumpy torus: A number of magnetic mirrors are arranged end-to-end in a toroidal ring. Any fuel ions that leak out of one are confined in a neighboring mirror, permitting the plasma pressure to be raised arbitrarily high without loss. An experimental facility, the ELMO Bumpy Torus (EBT), was built and tested at Oak Ridge National Laboratory (ORNL) in the 1970s.
- Field-reversed configuration: This device traps plasma in a self-organized quasi-stable structure, where the particle motion makes an internal magnetic field which then traps itself.
- Spheromak: Similar to a field-reversed configuration, a semi-stable plasma structure made by using the plasmas' self-generated magnetic field. A spheromak has both toroidal and poloidal fields, while a field-reversed configuration has no toroidal field.
- Dynomak: A spheromak that is formed and sustained using continuous magnetic flux injection.
- Reversed field pinch: Here the plasma moves inside a ring. It has an internal magnetic field. Moving out from the center of this ring, the magnetic field reverses direction.

### Inertial confinement

- Indirect drive: Lasers heat a structure named a Hohlraum that becomes so hot it begins to radiate X-ray light. These X-rays heat a fuel pellet, causing it to collapse inward to compress the fuel. The largest system using this method is the National Ignition Facility, followed closely by Laser Mégajoule.
- Direct drive: Lasers directly heat the fuel pellet. Notable direct drive experiments have been conducted at the Laboratory for Laser Energetics (LLE) and the GEKKO XII facilities. Good implosions require fuel pellets with close to a perfect shape in order to generate a symmetrical inward shock wave that produces the high-density plasma.
- Fast ignition: Uses two laser blasts. The first blast compresses the fusion fuel, then the second ignites it. As of 2019, this method had lost favor for energy production.
- Magneto-inertial fusion or Magnetized Liner Inertial Fusion: This combines a laser pulse with a magnetic pinch. The pinch community refers to it as magnetized liner inertial fusion while the ICF community refers to it as magneto-inertial fusion.
- Ion beams: Ions replace light (lasers) in beams that implode and heat fuel pellets. The main difference is that the beam has significantly higher momentum due to the mass of the ions, compared to a laser of equal power. As of 2019 it appears unlikely that ion beams can be sufficiently focused spatially and in time.
- Z-machine: Sends an electric current through thin tungsten wires, heating them sufficiently to generate X-rays. Like the indirect drive approach, these X-rays then compress a fuel capsule.

### Magnetic or electric pinches

- *Z-pinch*: A current travels in the z-direction through the plasma. The current generates a magnetic field that compresses the plasma. Pinches were the first method for human-made controlled fusion. The z-pinch has inherent instabilities that limit its compression and heating to values too low for practical fusion. The largest such machine, the UK's ZETA, was the last major experiment of the sort. The problems in z-pinch led to the tokamak design. The dense plasma focus is a possibly superior variation.
- *Theta-pinch*: A current circles around the outside of a plasma column, in the theta direction. This induces a magnetic field running down the center of the plasma, as opposed to around it. The early theta-pinch device Scylla was the first to conclusively demonstrate fusion, but later work demonstrated it had inherent limits that made it uninteresting for power production.
- *Sheared flow stabilized z-pinch*: Research at the University of Washington under Uri Shumlak investigated the use of sheared-flow stabilizing to smooth out the usual instabilities of unstable z-pinches. This involves accelerating neutral gas along the axis of the pinch. Experimental machines included the FuZE and Zap Flow Z-Pinch experimental reactors. In 2017, British technology investor and entrepreneur Benj Conway, together with physicists Brian Nelson and Uri Shumlak, co-founded Zap Energy to attempt to commercialize the technology for power production.
- *Screw pinch*: Combines a theta- and z-pinch for higher stability.

### Inertial electrostatic confinement

- *Polywell*: Attempts to combine magnetic confinement with electrostatic fields, to avoid the conduction losses generated by the cage.

### Other thermonuclear

- *Magnetized target fusion*: Confines hot plasma using a magnetic field and squeezes it using inertia. Examples include LANL FRX-L machine, General Fusion (piston compression with liquid metal liner), HyperJet Fusion (plasma jet compression with plasma liner).
- *Uncontrolled*: Fusion has been initiated by man, using uncontrolled fission explosions to stimulate fusion. Early proposals for fusion power included using bombs to initiate reactions. See Project PACER.

### Other non-thermonuclear

- *Lattice confinement fusion (LCF)*: Deuteron-saturated metals are exposed to gamma radiation or ion beams, such as in an IEC fusor, avoiding the confined high-temperature plasmas used in most other reactor types.
- *Muon-catalyzed fusion*: In diatomic molecules of isotopes of hydrogen, electrons are replaced with muons: more massive particles with the same electric charge. Their greater mass shrinks the molecule and overcomes most of the electrostatic repulsion (Coulomb barrier) to fusion. As of 2007, producing muons needs more energy than can be obtained from muon-catalyzed fusion.
- *High-intensity laser illumination*: A multi-institution (Center for Intense Laser Application Technology, National University of Defense Technology, China Academy of Engineering Physics) Chinese theoretical analysis indicates that high-intensity laser illumination (> 1020 Watts/cm2) can lower substantially (~10 ×) the temperatures at which nuclei fuse, raising reaction rates greatly (103–109 ×). The mechanism is that longer wavelength, near-infrared lasers are more efficient, via multi-photon interactions raising nuclear quantum tunneling probability, than shorter-wavelength lasers, at overcoming the Coulomb barrier that usually prevents nuclei fusing. This might be used to assist most fusion reactions and devices.

### Negative power methods

When used alone, in isolation, these methods inherently consume more power than they can provide via fusion.

- *Fusor*: An electric field heats ions to fusion conditions. The machine typically uses two spherical cages, a cathode inside the anode, inside a vacuum. These machines are not considered a viable approach to net power because of their high conduction and radiation losses. They are simple enough to build that amateurs have fused atoms using them.
- *Colliding beam fusion*: A beam of high energy particles fired at another beam or target can initiate fusion. This was used in the 1970s and 1980s to study the cross sections of fusion reactions. However beam systems cannot be used for power because keeping a beam coherent takes more energy than comes from fusion.


## Common tools

Many approaches, equipment, and mechanisms are employed across multiple projects to address fusion heating, measurement, and power production.

### Machine learning

A deep reinforcement learning system has been used to control a tokamak-based reactor. The system was able to manipulate the magnetic coils to manage the plasma. The system was able to continuously adjust to maintain appropriate behavior (more complex than step-based systems). In 2014, Google began working with California-based fusion company TAE Technologies to control the Joint European Torus (JET) to predict plasma behavior. DeepMind has also developed a control scheme with TCV. Researchers at Princeton Plasma Physics Laboratory (PPPL) and Princeton University made significant advances using artificial intelligence to control plasma in a tokamak, achieving high confinement without harmful edge energy bursts (known edge-localized modes) on two tokamaks: DIII-D and KSTAR. An international collaboration involving some of the same researchers from Princeton University and PPPL, as well as researchers from Chung-Ang University, Columbia University and Seoul National University, also led to a new AI system known as Diag2Diag, that fills in missing sensor data for fusion systems, offering more detail than a real-world sensor could have provided. Data gathered from the Diag2Diag research also provided new support for a leading theory about controlling plasma disruptions.

### Heating

- Electrostatic heating: an electric field can do work on charged ions or electrons, heating them.
- Neutral beam injection: hydrogen is ionized and accelerated by an electric field to form a charged beam that is shone through a source of neutral hydrogen gas towards the plasma which itself is ionized and contained by a magnetic field. Some of the intermediate hydrogen gas is accelerated towards the plasma by collisions with the charged beam while remaining neutral: this neutral beam is thus unaffected by the magnetic field and so reaches the plasma. Once inside the plasma the neutral beam transmits energy to the plasma by collisions which ionize it and allow it to be contained by the magnetic field, thereby both heating and refueling the reactor in one operation. The remainder of the charged beam is diverted by magnetic fields onto cooled beam dumps. Neutral beam heating was used extensively in the PLT during 1975–1986. The peak ion temperatures achieved set a world record, reaching 75 million K, well beyond the minimum needed for a practical fusion device.
- Radio frequency heating: a radio wave causes the plasma to oscillate (i.e., microwave oven). This is also known as electron cyclotron resonance heating, using for example gyrotrons, or dielectric heating.
- Magnetic reconnection: when plasma gets dense, its electromagnetic properties can change, which can lead to magnetic reconnection. Reconnection helps fusion because it instantly dumps energy into a plasma, heating it quickly. Up to 45% of the magnetic field energy can heat the ions.
- Magnetic oscillations: varying electric currents can be supplied to magnetic coils that heat plasma confined within a magnetic wall.
- Antiproton annihilation: antiprotons injected into a mass of fusion fuel can induce thermonuclear reactions. This possibility as a method of spacecraft propulsion, known as antimatter-catalyzed nuclear pulse propulsion, was investigated at Pennsylvania State University in connection with the proposed AIMStar project.

### Measurement

The diagnostics of a fusion scientific reactor are extremely complex and varied. The diagnostics required for a fusion power reactor will be various but less complicated than those of a scientific reactor as by the time of commercialization, many real-time feedback and control diagnostics will have been perfected. However, the operating environment of a commercial fusion reactor will be harsher for diagnostic systems than in a scientific reactor because continuous operations may involve higher plasma temperatures and higher levels of neutron irradiation. In many proposed approaches, commercialization will require the additional ability to measure and separate diverter gases, for example helium and impurities, and to monitor fuel breeding, for instance the state of a tritium breeding liquid lithium liner. The following are some basic techniques.

- Flux loop: a loop of wire is inserted into the magnetic field. As the field passes through the loop, a current is made. The current measures the total magnetic flux through that loop. This has been used on the National Compact Stellarator Experiment, the polywell, and the LDX machines. A Langmuir probe, a metal object placed in a plasma, can be employed. A potential is applied to it, giving it a voltage against the surrounding plasma. The metal collects charged particles, drawing a current. As the voltage changes, the current changes. This makes an IV Curve. The IV-curve can be used to determine the local plasma density, potential and temperature.
- Thomson scattering: "Light scatters" from plasma can be used to reconstruct plasma behavior, including density and temperature. It is common in Inertial confinement fusion, Tokamaks, and fusors. In ICF systems, firing a second beam into a gold foil adjacent to the target makes x-rays that traverse the plasma. In tokamaks, this can be done using mirrors and detectors to reflect light.
- Neutron detectors: Several types of neutron detectors can record the rate at which neutrons are produced.
- X-ray detectors Visible, IR, UV, and X-rays are emitted anytime a particle changes velocity. If the reason is deflection by a magnetic field, the radiation is cyclotron radiation at low speeds and synchrotron radiation at high speeds. If the reason is deflection by another particle, plasma radiates X-rays, known as Bremsstrahlung radiation.

### Power production

Neutron blankets absorb neutrons, which heats the blanket. Power can be extracted from the blanket in various ways:

- Steam turbines can be driven by heat transferred into a working fluid that turns into steam, driving electric generators.
- Neutron blankets: These neutrons can regenerate spent fission fuel. Tritium can be produced using a breeder blanket of liquid lithium or a helium cooled pebble bed made of lithium-bearing ceramic pebbles.
- Direct energy conversion: The kinetic energy of a particle can be converted into voltage. It was first suggested by Richard F. Post in conjunction with magnetic mirrors, in the late 1960s. It has been proposed for field-reversed configuration and dense plasma focus devices. The process converts a large fraction of the random energy of the fusion products into directed motion. The particles are then collected on electrodes at various large electric potentials. This method has demonstrated an experimental efficiency of 48 percent.
- Traveling-wave tubes pass charged helium atoms at several megavolts and just coming off the fusion reaction through a tube with a coil of wire around the outside. This passing charge at high voltage pulls electricity through the wire.

### Confinement

Confinement refers to all the conditions necessary to keep a plasma dense and hot long enough to undergo fusion. General principles:

- Equilibrium: The forces acting on the plasma must be balanced. One exception is inertial confinement, where the fusion must occur faster than the dispersal time.
- Stability: The plasma must be constructed so that disturbances will not lead to the plasma dispersing.
- Transport or conduction: The loss of material must be sufficiently slow. The plasma carries energy off with it, so rapid loss of material will disrupt fusion. Material can be lost by transport into different regions or conduction through a solid or liquid.

To produce self-sustaining fusion, part of the energy released by the reaction must be used to heat new reactants and maintain the conditions for fusion.

#### Magnetic confinement

Magnetic confinement fusion uses magnetic fields to confine the plasma.

##### Magnetic mirror

In a magnetic mirror reactor, a configuration of electromagnets is used to create an area with an increasing density of magnetic field lines at either end of the confinement volume. Particles approaching the ends experience an increasing force that eventually causes them to reverse direction and return to the confinement area, like light reflected from a mirror. Several devices apply this effect. The most famous was the magnetic mirror machines, a series of devices built at LLNL from the 1960s to the 1980s. Other examples include magnetic bottles and the biconic cusp. Because the mirror machines were straight, they had some advantages over ring-shaped designs. The mirrors were easier to construct and maintain and direct conversion energy capture was easier to implement. Poor confinement has led this approach to be abandoned, except in the polywell design.

##### Magnetic loops

Magnetic loops bend the field lines back on themselves, either in circles or more commonly in nested toroidal surfaces. The most highly developed systems of this type are the tokamak, the stellarator, and the reversed field pinch. Compact toroids, especially the field-reversed configuration and the spheromak, attempt to combine the advantages of toroidal magnetic surfaces with those of a simply connected (non-toroidal) machine, resulting in a mechanically simpler and smaller confinement area.

#### Inertial confinement

Inertial confinement fusion is the use of rapid implosion to heat and confine plasma. A shell surrounding the fuel is imploded using a direct laser blast (direct drive), a secondary x-ray blast (indirect drive), or heavy beams. The fuel must be compressed to about 30 times solid density with energetic beams. Direct drive can in principle be efficient, but insufficient uniformity has prevented success.:19–20 Indirect drive uses beams to heat a shell, driving the shell to radiate x-rays, which then implode the pellet. The beams are commonly laser beams, but ion and electron beams have been investigated.:182–193

##### Electrostatic confinement

Electrostatic confinement fusion devices use electrostatic fields. The best known is the fusor. This device has a cathode inside an anode wire cage. Positive ions fly towards the negative inner cage, and are heated by the electric field in the process. If they miss the inner cage they can collide and fuse. Ions typically hit the cathode, however, creating prohibitory high conduction losses. Fusion rates in fusors are low because of competing physical effects, such as energy loss in the form of light radiation. Designs have been proposed to avoid the problems associated with the cage, by generating the field using a non-neutral cloud. These include a plasma oscillating device, a magnetically shielded-grid, a penning trap, the polywell, and the F1 cathode driver concept.

### Spin alignment

Spin polarization of deuterium and tritium is expected to have substantially advance fusion power towards becoming a practical technology given that aligned spins make fusion more probable. Benefits include:

- Fusion reactivity/cross-section increased as much as 50% for fully parallel D-T fuel. This is a direct quantum effect.
- Power increased by 80–90% or more) due to increased plasma temperature
- Electric power output as much as 2x the raw fusion increase
- Reduced tritium requirement, reducing reactor size and cost


## Fuels

The fuels considered for fusion power are mainly the heavier isotopes of hydrogen—deuterium and tritium. Deuterium is abundant on earth in the form of semiheavy water. Tritium, decaying with a half-life of 12 years, must be produced. Fusion reactor concepts assume as a component a proposed lithium "breeding blanket" technology surrounding the reactor. Helium-3 is a more speculative fuel, which must be mined extraterrestrially or produced by other nuclear reactions. The protium–boron-11 reaction is extremely speculative, but minimizes neutron radiation.

### Deuterium, tritium

The easiest nuclear reaction, at the lowest energy, is D+T:

2

1

D

+

3

1

T

→

4

2

He

(3.5 MeV) +

1

0

n

(14.1 MeV)

This reaction is common in research, industrial and military applications, usually as a neutron source. Deuterium is a naturally occurring isotope of hydrogen and is commonly available. The large mass ratio of the hydrogen isotopes makes their separation easy compared to the uranium enrichment process. Tritium is a natural isotope of hydrogen, but because it has a short half-life of 12.32 years, it is hard to find, store, produce, and is expensive. Consequently, the deuterium-tritium fuel cycle requires the breeding of tritium from lithium using one of the following reactions:

1

0

n

+

6

3

Li

→

3

1

T

+

4

2

He

1

0

n

+

7

3

Li

→

3

1

T

+

4

2

He

+

1

0

n

The reactant neutron is supplied by the D–T fusion reaction shown above, and the one that has the greatest energy yield. The reaction with 6Li is exothermic, providing a small energy gain for the reactor. The reaction with 7Li is endothermic, but does not consume the neutron. Neutron multiplication reactions are required to replace the neutrons lost to absorption by other elements. Leading candidate neutron multiplication materials are beryllium and lead, but the 7Li reaction helps to keep the neutron population high. Natural lithium is mainly 7Li, which has a low tritium production cross section compared to 6Li so most reactor designs use breeding blankets with enriched 6Li.

Drawbacks commonly attributed to D–T fusion power include:

- The supply of neutrons results in neutron activation of the reactor materials.:242
- 80% of the resultant energy is carried off by neutrons, which limits the use of direct energy conversion.
- It requires the radioisotope tritium. Tritium may leak from reactors. Some estimates suggest that this would represent a substantial environmental radioactivity release.

The neutron flux expected in a commercial D–T fusion reactor is about 100 times that of fission power reactors, posing problems for material design. After a series of D–T tests at JET, the vacuum vessel was sufficiently radioactive that it required remote handling for the year following the tests.

In a production setting, the neutrons would react with lithium in the breeding blanket composed of lithium ceramic pebbles or liquid lithium, yielding tritium. The energy of the neutrons ends up in the lithium, which would then be transferred to drive electrical production. The lithium blanket protects the outer portions of the reactor from the neutron flux. Newer designs, the advanced tokamak in particular, use lithium inside the reactor core as a design element. The plasma interacts directly with the lithium, preventing a problem known as "recycling". The advantage of this design was demonstrated in the Lithium Tokamak Experiment.

### Deuterium

Fusing two deuterium nuclei is the second easiest fusion reaction. The reaction has two branches that occur with nearly equal probability:

2

1

D

+

2

1

D

→

3

1

T

+

1

1

H

2

1

D

+

2

1

D

→

3

2

He

+

1

0

n

This reaction is also common in research. The optimum energy to initiate this reaction is 15 keV, only slightly higher than that for the D–T reaction. The first branch produces tritium, so that a D–D reactor is not tritium-free, even though it does not require an input of tritium or lithium. Unless the tritons are quickly removed, most of the tritium produced is burned in the reactor, which reduces the handling of tritium, with the disadvantage of producing more, and higher-energy, neutrons. The neutron from the second branch of the D–D reaction has an energy of only 2.45 MeV (0.393 pJ), while the neutron from the D–T reaction has an energy of 14.1 MeV (2.26 pJ), resulting in greater isotope production and material damage. When the tritons are removed quickly while allowing the 3He to react, the fuel cycle is called "tritium suppressed fusion". The removed tritium decays to 3He with a 12.32-year half-life. By recycling the 3He decay product into the reactor, the fusion reactor does not require materials resistant to fast neutrons.

Assuming complete removal of tritium and 3He recycling, only 6% of the fusion energy is carried by neutrons. The tritium-suppressed D–D fusion requires an energy confinement that is 10 times longer compared to D–T and double the plasma temperature.

### Deuterium, helium-3

A second-generation approach to controlled fusion power involves combining helium-3 (3He) and deuterium (2H):

2

1

D

+

3

2

He

→

4

2

He

+

1

1

H

This reaction produces 4He and a high-energy proton. As with the p-11B aneutronic fusion fuel cycle, most of the reaction energy is released as charged particles, reducing activation of the reactor housing and potentially allowing more efficient energy harvesting (via any of several pathways). In practice, D–D side reactions produce a significant number of neutrons, leaving p-11B as the preferred cycle for aneutronic fusion.

### Proton, boron-11

Both material science problems and non-proliferation concerns are greatly diminished by aneutronic fusion. Theoretically, the most reactive aneutronic fuel is 3He. However, obtaining reasonable quantities of 3He implies large scale extraterrestrial mining on the Moon or in the atmosphere of Uranus or Saturn. Therefore, the most promising candidate fuel for such fusion is fusing the readily available protium (i.e. a proton) and boron. Their fusion releases no neutrons, but produces energetic charged alpha (helium) particles whose energy can directly be converted to electrical power:

1

1

H

+

11

5

B

→ 3

4

2

He

Side reactions are likely to yield neutrons that carry only about 0.1% of the power,:177–182 which means that neutron scattering is not used for energy transfer and material activation is reduced several thousand-fold. The optimum temperature for this reaction of 123 keV is nearly ten times higher than that for pure hydrogen reactions, and energy confinement must be 500 times better than that required for the D–T reaction. In addition, the power density is 2500 times lower than for D–T, although per unit mass of fuel, this is still considerably higher compared to fission reactors.

Because the confinement properties of the tokamak and laser pellet fusion are marginal, most proposals for aneutronic fusion are based on radically different confinement concepts, such as the Polywell and the dense plasma focus. In 2013, a research team led by Christine Labaune at École Polytechnique, reported a new fusion rate record for proton-boron fusion, with an estimated 80 million fusion reactions during a 1.5 nanosecond laser fire, 100 times greater than reported in previous experiments.


## Material selection

Structural material stability is a critical issue. Materials that can survive the high temperatures and neutron bombardment experienced in a fusion reactor are considered key to success. The principal issues are the conditions generated by the plasma, neutron degradation of wall surfaces, and the related issue of plasma-wall surface conditions. Reducing hydrogen permeability is seen as crucial to hydrogen recycling and control of the tritium inventory. Materials with the lowest bulk hydrogen solubility and diffusivity provide the optimal candidates for stable barriers. A few pure metals, including tungsten and beryllium, and compounds such as carbides, dense oxides, and nitrides have been investigated. Research has highlighted that coating techniques for preparing well-adhered and perfect barriers are of equivalent importance. The most attractive techniques are those in which an ad-layer is formed by oxidation alone. Alternative methods utilize specific gas environments with strong magnetic and electric fields. Assessment of barrier performance represents an additional challenge. Classical coated membranes gas permeation continues to be the most reliable method to determine hydrogen permeation barrier (HPB) efficiency. In 2021, in response to increasing numbers of designs for fusion power reactors for 2040, the United Kingdom Atomic Energy Authority published the UK Fusion Materials Roadmap 2021–2040, focusing on five priority areas, with a focus on tokamak family reactors:

- Novel materials to minimize the amount of activation in the structure of the fusion power plant;
- Compounds that can be used within the power plant to optimise breeding of tritium fuel to sustain the fusion process;
- Magnets and insulators that are resistant to irradiation from fusion reactions—especially under cryogenic conditions;
- Structural materials able to retain their strength under neutron bombardment at high operating temperatures (over 550 degrees C);
- Engineering assurance for fusion materials—providing irradiated sample data and modelled predictions such that plant designers, operators and regulators have confidence that materials are suitable for use in future commercial power stations.

### Superconducting materials

In a plasma that is embedded in a magnetic field (known as a magnetized plasma) the fusion rate scales as the magnetic field strength to the 4th power. For this reason, many fusion companies that rely on magnetic fields to control their plasma are trying to develop high temperature superconducting devices. In 2021, SuperOx, a Russian and Japanese company, developed a new manufacturing process for making superconducting YBCO wire for fusion reactors. This new wire was shown to conduct between 700 and 2000 Amps per square millimeter. The company was able to produce 186 miles of wire in nine months.

### Containment considerations

Even on smaller production scales, the containment apparatus is blasted with matter and energy. Designs for plasma containment must consider:

- A heating and cooling cycle, up to a 10 MW/m2 thermal load.
- Neutron radiation, which over time leads to neutron activation and embrittlement.
- High energy ions leaving at tens to hundreds of electronvolts.
- Alpha particles leaving at millions of electronvolts.
- Electrons leaving at high energy.
- Light radiation (IR, visible, UV, X-ray).

Depending on the approach, these effects may be higher or lower than fission reactors. Depending on the approach, other considerations such as electrical conductivity, magnetic permeability, and mechanical strength matter. Materials must also not end up as long-lived radioactive waste.

### Plasma-wall surface conditions

For long term use, each atom in the wall is expected to be hit by a neutron and displaced about 100 times before the material is replaced. These high-energy neutron collisions with the atoms in the wall result in the absorption of the neutrons, forming unstable isotopes of the atoms. When the isotope decays, it may emit alpha particles, protons, or gamma rays. Alpha particles, once stabilized by capturing electrons, form helium atoms which accumulate at grain boundaries and may result in swelling, blistering, or embrittlement of the material.

### Selection of materials

Tungsten is widely regarded as the optimal material for plasma-facing components in next-generation fusion devices due to its unique properties and potential for enhancements. Its low sputtering rates and high melting point make it particularly suitable for the high-stress environments of fusion reactors, allowing it to withstand intense conditions without rapid degradation. Additionally, tungsten's low tritium retention through co-deposition and implantation is essential in fusion contexts, as it helps to minimize the accumulation of this radioactive isotope.

Liquid metals (lithium, gallium, tin) have been proposed, e.g., by injection of 1–5 mm thick streams flowing at 10 m/s on solid substrates.

Graphite features a gross erosion rate due to physical and chemical sputtering amounting to many meters per year, requiring redeposition of the sputtered material. The redeposition site generally does not exactly match the sputter site, allowing net erosion that may be prohibitive. An even larger problem is that tritium is redeposited with the redeposited graphite. The tritium inventory in the wall and dust could build up to many kilograms, representing a waste of resources and a radiological hazard in case of an accident. Graphite found favor as material for short-lived experiments, but appears unlikely to become the primary plasma-facing material (PFM) in a commercial reactor.

Ceramic materials such as silicon carbide (SiC) have similar issues like graphite. Tritium retention in silicon carbide plasma-facing components is approximately 1.5–2 times higher than in graphite, resulting in reduced fuel efficiency and heightened safety risks in fusion reactors. SiC tends to trap more tritium, limiting its availability for fusion and increasing the risk of hazardous accumulation, complicating tritium management. Furthermore, the chemical and physical sputtering of SiC remains significant, contributing to tritium buildup through co-deposition over time and with increasing particle fluence. As a result, carbon-based materials have been excluded from ITER, DEMO, and similar devices.

Tungsten's sputtering rate is orders of magnitude smaller than carbon's, and tritium is much less incorporated into redeposited tungsten. However, tungsten plasma impurities are much more damaging than carbon impurities, and self-sputtering can be high, requiring the plasma in contact with the tungsten not be too hot (a few tens of eV rather than hundreds of eV). Tungsten also has issues around eddy currents and melting in off-normal events, as well as some radiological issues.

Recent advances in materials for containment apparatus materials have found that certain ceramics can actually improve the longevity of the material of the containment apparatus. Studies on MAX phases, such as titanium silicon carbide, show that under the high operating temperatures of nuclear fusion, the material undergoes a phase transformation from a hexagonal structure to a face-centered-cubic (FCC) structure, driven by helium bubble growth. Helium atoms preferentially accumulate in the Si layer of the hexagonal structure, as the Si atoms are more mobile than the Ti–C slabs. As more atoms are trapped, the Ti–C slab is peeled off, causing the Si atoms to become highly mobile interstitial atoms in the new FCC structure. Lattice strain induced by the He bubbles cause Si atoms to diffuse out of compressive areas, typically towards the surface of the material, forming a protective silicon dioxide layer.

Doping vessel materials with iron silicate has emerged as a promising approach to enhance containment materials in fusion reactors, as well. This method targets helium embrittlement at grain boundaries, a common issue that arises as helium atoms accumulate and form bubbles. Over time, these bubbles coalesce at grain boundaries, causing them to expand and degrade the material's structural integrity. By contrast, introducing iron silicate creates nucleation sites within the metal matrix that are more thermodynamically favorable for helium aggregation. This localized congregation around iron silicate nanoparticles induces matrix strain rather than weakening grain boundaries, preserving the material's strength and longevity.
