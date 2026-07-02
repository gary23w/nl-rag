---
title: "Tokamak (part 2/2)"
source: https://en.wikipedia.org/wiki/Tokamak
domain: plasma-physics
license: CC-BY-SA-4.0
tags: plasma physics, magnetohydrodynamics simulation, debye length, plasma oscillation
fetched: 2026-07-02
part: 2/2
---

## Design

### Basic problem

Positively charged ions and negatively charged electrons in a fusion plasma are at very high temperatures, and have correspondingly large velocities. In order to maintain the fusion process, particles from the hot plasma must be confined in the central region, or the plasma will rapidly cool. Magnetic confinement fusion devices exploit the fact that charged particles in a magnetic field experience a Lorentz force and follow helical paths along the field lines.

The simplest magnetic confinement system is a solenoid. A plasma in a solenoid will spiral about the lines of field running down its center, preventing motion towards the sides. However, this does not prevent motion towards the ends. The obvious solution is to bend the solenoid around into a circle, forming a torus. However, it was demonstrated that such an arrangement is not uniform; for purely geometric reasons, the field on the outside edge of the torus is lower than on the inside edge. This asymmetry causes the electrons and ions to drift across the field, and eventually hit the walls of the torus.

The solution is to shape the lines so they do not simply run around the torus, but twist around like the stripes on a barber pole or candycane. In such a field any single particle will find itself at the outside edge where it will drift one way, then as it follows its magnetic line around the torus it will find itself on the inside edge, where it will drift the other way. This cancellation is not perfect, but calculations showed it was enough to allow the fuel to remain in the reactor for a useful time.

### Tokamak solution

The two first solutions to making a design with the required twist were the stellarator which did so through a mechanical arrangement, twisting the entire torus, and the z-pinch design which ran an electrical current through the plasma to create a second magnetic field to the same end. Both demonstrated improved confinement times compared to a simple torus, but both also demonstrated a variety of effects that caused the plasma to be lost from the reactors at rates that were not sustainable.

The tokamak is essentially identical to the z-pinch concept in its physical layout. Its key innovation was the realization that the instabilities that were causing the pinch to lose its plasma could be controlled. The issue was how "twisty" the fields were; fields that caused the particles to transit inside and out more than once per orbit around the long axis torus were much more stable than devices that had less twist. This ratio of twists to orbits became known as the *safety factor*, denoted *q*. Previous devices operated at *q* about 1⁄3, while the tokamak operates at *q* ≫ 1. This increases stability by orders of magnitude.

When the problem is considered even more closely, the need for a vertical (parallel to the axis of rotation) component of the magnetic field arises. The Lorentz force of the toroidal plasma current in the vertical field provides the inward force that holds the plasma torus in equilibrium.

### Other issues

Early tokamaks had an ion temperature limited by the empirical Artsimovich formula:

$T_{i}=5.9\times 10^{-7}(n_{e}IB_{t}R^{2}A^{-{\frac {3}{2}}})^{\frac {1}{3}}$

While the tokamak addresses the issue of plasma stability in a gross sense, plasmas are also subject to a number of dynamic instabilities. One of these, the kink instability, is strongly suppressed by the tokamak layout, a side-effect of the high safety factors of tokamaks. The lack of kinks allowed the tokamak to operate at much higher temperatures than previous machines, and this allowed a host of new phenomena to appear.

One of these, the banana orbits, is caused by the wide range of particle energies in a tokamak – much of the fuel is hot, but a certain percentage is much cooler. Due to the high twist of the fields in the tokamak, particles following their lines of force rapidly move towards the inner edge and then outer. As they move inward they are subject to increasing magnetic fields due to the smaller radius concentrating the field. The low-energy particles in the fuel will reflect off this increasing field and begin to travel backwards through the fuel, colliding with the higher energy nuclei and scattering them out of the plasma. This process causes fuel to be lost from the reactor, although this process is slow enough that a practical reactor is still well within reach.

Another instability is tearing instability. In 2024 researchers used reinforcement learning against a multimodal dynamic model to measure and forecast such instabilities based on signals from multiple diagnostics and actuators at 25 millisecond intervals. This forecast was used to reduce tearing instabilities in DIII-D6, in the US. The reward function balanced the conflicting objectives of maximum plasma pressure and instability risks. In particular, the plasma actively tracked the stable path while maintaining H-mode performance.

### Breakeven, *Q*, and ignition

One of the first goals for any controlled fusion device is to reach *breakeven*, the point where the energy being released by the fusion reactions is equal to the amount of energy being used to maintain the reaction. The ratio of output to input energy is denoted *Q*, and breakeven corresponds to a *Q* of 1. A *Q* of more than one is needed for the reactor to generate net energy, but for practical reasons, it is desirable for it to be much higher.

Once breakeven is reached, further improvements in confinement generally lead to a rapidly increasing *Q*. That is because some of the energy being given off by the fusion reactions of the most common fusion fuel, a 50-50 mix of deuterium and tritium, is in the form of alpha particles. These can collide with the fuel nuclei in the plasma and heat it, reducing the amount of external heat needed. At some point, known as *ignition*, this internal self-heating is enough to keep the reaction going without any external heating, corresponding to an infinite *Q*.

In the case of the tokamak, this self-heating process is maximized if the alpha particles remain in the fuel long enough to guarantee they will collide with the fuel. As the alphas are electrically charged, they are subject to the same fields that are confining the fuel plasma. The amount of time they spend in the fuel can be maximized by ensuring their orbit in the field remains within the plasma. It can be demonstrated that this occurs when the electrical current in the plasma is about 3 MA.

### Advanced tokamaks

In the early 1970s, studies at Princeton into the use of high-power superconducting magnets in future tokamak designs examined the layout of the magnets. They noticed that the arrangement of the main toroidal coils meant that there was significantly more tension between the magnets on the inside of the curvature where they were closer together. Considering this, they noted that the tensional forces within the magnets would be evened out if they were shaped like a D, rather than an O. This became known as the "Princeton D-coil".

This was not the first time this sort of arrangement had been considered, although for entirely different reasons. The safety factor varies across the axis of the machine; for purely geometrical reasons, it is always smaller at the inside edge of the plasma closest to the machine's center because the long axis is shorter there. That means that a machine with an average *q* = 2 might still be less than 1 in certain areas. In the 1970s, it was suggested that one way to counteract this and produce a design with a higher average *q* would be to shape the magnetic fields so that the plasma only filled the outer half of the torus, shaped like a D or C when viewed end-on, instead of the normal circular cross section.

One of the first machines to incorporate a D-shaped plasma was the JET, which began its design work in 1973. This decision was made both for theoretical reasons as well as practical; because the force is larger on the inside edge of the torus, there is a large net force pressing inward on the entire reactor. The D-shape also had the advantage of reducing the net force, as well as making the supported inside edge flatter so it was easier to support. Code exploring the general layout noticed that a non-circular shape would slowly drift vertically, which led to the addition of an active feedback system to hold it in the center. Once JET had selected this layout, the General Atomics Doublet III team redesigned that machine into the D-IIID with a D-shaped cross-section, and it was selected for the Japanese JT-60 design as well. This layout has been largely universal since then.

One problem seen in all fusion reactors is that the presence of heavier elements causes energy to be lost at an increased rate, cooling the plasma. During the very earliest development of fusion power, a solution to this problem was found, the *divertor*, essentially a large mass spectrometer that would cause the heavier elements to be flung out of the reactor. This was initially part of the stellarator designs, where it is easy to integrate into the magnetic windings. However, designing a divertor for a tokamak proved to be a very difficult design problem.

Another problem seen in all fusion designs is the heat load that the plasma places on the wall of the confinement vessel. There are materials that can handle this load, but they are generally undesirable and expensive heavy metals. When such materials are sputtered in collisions with hot ions, their atoms mix with the fuel and rapidly cool it. A solution used on most tokamak designs is the *limiter*, a small ring of light metal that projected into the chamber so that the plasma would hit it before hitting the walls. This eroded the limiter and caused its atoms to mix with the fuel, but these lighter materials cause less disruption than the wall materials.

When reactors moved to the D-shaped plasmas it was quickly noted that the escaping particle flux of the plasma could be shaped as well. Over time, this led to the idea of using the fields to create an internal divertor that flings the heavier elements out of the fuel, typically towards the bottom of the reactor. There, a pool of liquid lithium metal is used as a sort of limiter; the particles hit it and are rapidly cooled, remaining in the lithium. This internal pool is much easier to cool, due to its location, and although some lithium atoms are released into the plasma, its very low mass makes it a much smaller problem than even the lightest metals used previously.

As machines began to explore this newly shaped plasma, they noticed that certain arrangements of the fields and plasma parameters would sometimes enter what is now known as the high-confinement mode, or H-mode, which operated stably at higher temperatures and pressures. Operating in the H-mode, which can also be seen in stellarators, is now a major design goal of the tokamak design.

Finally, it was noted that when the plasma had a non-uniform density it would give rise to internal electrical currents. This is known as the *bootstrap current*. This allows a properly designed reactor to generate some of the internal current needed to twist the magnetic field lines without having to supply it from an external source. This has a number of advantages, and modern designs all attempt to generate as much of their total current through the bootstrap process as possible.

By the early 1990s, the combination of these features and others collectively gave rise to the "advanced tokamak" concept. This forms the basis of modern research, including ITER.

### Plasma disruptions

Tokamaks are subject to events known as "disruptions" that cause confinement to be lost in milliseconds. The two primary mechanisms are the "vertical displacement event" (VDE), in which the entire plasma moves vertically until it touches the upper or lower section of the vacuum chamber. By contrast, in the "major disruption", long wavelength, non-axisymmetric magnetohydrodynamical instabilities cause the plasma to be forced into non-symmetrical shapes, often squeezed into the top and bottom of the chamber.

When the plasma touches the vessel walls it undergoes rapid cooling, or "thermal quenching". In the major disruption case, this is normally accompanied by a brief increase in plasma current as the plasma concentrates. Quenching ultimately breaks up the plasma confinement. In the case of the major disruption the current drops again, the "current quench". The initial increase in current is not seen in the VDE, and the thermal and current quench occurs at the same time. In both cases, the thermal and electrical load of the plasma is rapidly deposited on the reactor vessel, which has to be able to handle these loads. ITER is designed to handle 2600 of these events over its lifetime.

For high-energy devices such as ITER, which achieves plasma currents on the order of 15 megaamperes, it is possible the brief increase in current during a major disruption will cross a critical threshold. This occurs when the current produces a force on the electrons that is higher than the frictional forces of the collisions between particles in the plasma. In this event, electrons can be accelerated to relativistic velocities, creating so-called "runaway electrons" in the relativistic runaway electron avalanche. These retain their energy even during the current quench.

When confinement breaks down, these runaway electrons impact the side of the reactor. These can reach 12 megaamps of current deposited in a small area, well beyond the capabilities of any mechanical solution. In one famous case, the Tokamak de Fontenay aux Roses had a major disruption where the runaway electrons burned a hole through the vacuum chamber.

Major disruptions in tokamaks occur frequently, on the order of a few percent of shots. The damage is often large but rarely dramatic. In ITER it is expected that major disruptions would damage the chamber with no possibility to restore the device. The development of systems to counter the effects of runaway electrons is considered a must-have technology for ITER.

A large amplitude of the central current density can also result in internal disruptions, or sawteeth, which do not generally terminate the discharge.

Densities over the Greenwald limit, a bound depending on the plasma current and the minor radius, typically leads to disruptions. While it has been exceeded up to factors of 10, it remains an important concept describing the phenomenology of the transition of the plasma flow, which still needs to be understood.


## Plasma heating

In an operating fusion reactor, part of the energy generated will serve to maintain the plasma temperature as fresh deuterium and tritium are introduced. However, in the startup of a reactor, either initially or after a temporary shutdown, the plasma will have to be heated to its operating temperature of greater than 10 keV (over 100 million degrees Celsius). In current tokamak (and other) magnetic fusion experiments, insufficient fusion energy is produced to maintain the plasma temperature, and constant external heating must be supplied. Chinese researchers set up the Experimental Advanced Superconducting Tokamak (EAST) in 2006, which can supposedly sustain a plasma temperature of 100 million degree Celsius for initiating fusion between hydrogen atoms, according to a November 2018 test.

### Ohmic heating ~ inductive mode

Since the plasma is an electrical conductor, it is possible to heat the plasma by inducing a current through it; the induced current that provides most of the poloidal field is also a major source of initial heating.

The heating caused by the induced current is called ohmic (or resistive) heating; it is the same kind of heating that occurs in an electric light bulb or in an electric heater. The heat generated depends on the resistance of the plasma and the amount of electric current running through it. But as the temperature of heated plasma rises, the resistance decreases and ohmic heating becomes less effective. It appears that the maximum plasma temperature attainable by ohmic heating in a tokamak is 20–30 million degrees Celsius. To obtain still higher temperatures, additional heating methods must be used.

The current is induced by continually increasing the current through an electromagnetic winding linked with the plasma torus: the plasma can be viewed as the secondary winding of a transformer. This is inherently a pulsed process because there is a limit to the current through the primary (there are also other limitations on long pulses). Tokamaks must therefore either operate for short periods or rely on other means of heating and current drive.

### Magnetic compression

A gas can be heated by sudden compression. In the same way, the temperature of a plasma is increased if it is compressed rapidly by increasing the confining magnetic field. In a tokamak, this compression is achieved simply by moving the plasma into a region of higher magnetic field (i.e., radially inward). Since plasma compression brings the ions closer together, the process has the additional benefit of facilitating attainment of the required density for a fusion reactor.

Magnetic compression was an area of research in the early "tokamak stampede", and was the purpose of one major design, the ATC. The concept has not been widely used since then, although a somewhat similar concept is part of the General Fusion design.

### Neutral-beam injection

Neutral-beam injection involves the introduction of high energy (rapidly moving) atoms or molecules into an ohmically heated, magnetically confined plasma within the tokamak.

The high energy atoms originate as ions in an arc chamber before being extracted through a high voltage grid set. The term "ion source" is used to generally mean the assembly consisting of a set of electron emitting filaments, an arc chamber volume, and a set of extraction grids. A second device, similar in concept, is used to separately accelerate electrons to the same energy. The much lighter mass of the electrons makes this device much smaller than its ion counterpart. The two beams then intersect, where the ions and electrons recombine into neutral atoms, allowing them to travel through the magnetic fields.

Once the neutral beam enters the tokamak, interactions with the main plasma ions occur. This has two effects. One is that the injected atoms re-ionize and become charged, thereby becoming trapped inside the reactor and adding to the fuel mass. The other is that the process of being ionized occurs through impacts with the rest of the fuel, and these impacts deposit energy in that fuel, heating it.

This form of heating has no inherent energy (temperature) limitation, in contrast to the ohmic method, but its rate is limited to the current in the injectors. Ion source extraction voltages are typically on the order of 50–100 kV, and high voltage, negative ion sources (-1 MV) are being developed for ITER. The ITER Neutral Beam Test Facility in Padova will be the first ITER facility to start operation.

While neutral beam injection is used primarily for plasma heating, it can also be used as a diagnostic tool and in feedback control by making a pulsed beam consisting of a string of brief 2–10 ms beam blips. Deuterium is a primary fuel for neutral beam heating systems and hydrogen and helium are sometimes used for selected experiments.

### Radio-frequency heating

High-frequency electromagnetic waves are generated by oscillators (often by gyrotrons or klystrons) outside the torus. If the waves have the correct frequency (or wavelength) and polarization, their energy can be transferred to the charged particles in the plasma, which in turn collide with other plasma particles, thus increasing the temperature of the bulk plasma. Various techniques exist including electron cyclotron resonance heating (ECRH) and ion cyclotron resonance heating. This energy is usually transferred by microwaves.


## Particle inventory

Plasma discharges within the tokamak's vacuum chamber consist of energized ions and atoms. The energy from these particles eventually reaches the inner wall of the chamber through radiation, collisions, or lack of confinement. The heat from the particles is removed via conduction through the chamber's inner wall to a water-cooling system, where the heated water proceeds to an external cooling system through convection.

Turbomolecular or diffusion pumps allow for particles to be evacuated from the bulk volume and cryogenic pumps, consisting of a liquid helium-cooled surface, serve to effectively control the density throughout the discharge by providing an energy sink for condensation to occur. When done correctly, the fusion reactions produce large amounts of high energy neutrons. Being electrically neutral and relatively tiny, the neutrons are not affected by the magnetic fields nor are they stopped much by the surrounding vacuum chamber.

The neutron flux is reduced significantly at a purpose-built neutron shield boundary that surrounds the tokamak in all directions. Shield materials vary but are generally materials made of atoms which are close to the size of neutrons because these work best to absorb the neutron and its energy. Good candidate materials include those with much hydrogen, such as water and plastics. Boron atoms are also good absorbers of neutrons. Thus, concrete and polyethylene doped with boron make inexpensive neutron shielding materials.

Once freed, the neutron has a relatively short half-life of about 10 minutes before it decays into a proton and electron with the emission of energy. When the time comes to actually try to make electricity from a tokamak-based reactor, some of the neutrons produced in the fusion process would be absorbed by a liquid metal blanket and their kinetic energy would be used in heat transfer processes to ultimately turn a generator.


## Experimental tokamaks

### Currently in operation

(in chronological order of start of operations)

- 1960s: TM1-MH (since 1977 as Castor; since 2007 as Golem) in Prague, Czech Republic. In operation in Kurchatov Institute since the early 1960s but renamed to Castor in 1977 and moved to IPP CAS, Prague. In 2007 moved to FNSPE, Czech Technical University in Prague and renamed to Golem.
- 1975: T-10, in Kurchatov Institute, Moscow, Russia (formerly Soviet Union); 2 MW
- 1986: DIII-D, in San Diego, United States; operated by General Atomics since the late 1980s
- 1987: STOR-M, University of Saskatchewan, Canada; its predecessor, STOR1-M built in 1983, was used for the first demonstration of alternating current in a tokamak.
- 1988: Tore Supra, but renamed to WEST in 2016, at the CEA, Cadarache, France
- 1989: Aditya, at Institute for Plasma Research (IPR) in Gujarat, India
- 1989: COMPASS, in Prague, Czech Republic; in operation since 2008, previously operated from 1989 to 1999 in Culham, United Kingdom
- 1990: FTU, in Frascati, Italy
- 1991: ISTTOK, at the Instituto de Plasmas e Fusão Nuclear, Lisbon, Portugal

- 1991: ASDEX Upgrade, in Garching, Germany
- 1992: H-1NF (H-1 National Plasma Fusion Research Facility) based on the H-1 Heliac device built by Australia National University's plasma physics group and in operation since 1992
- 1992: Tokamak à configuration variable (TCV), at the Swiss Plasma Center, EPFL, Switzerland
- 1993: HBT-EP Tokamak, at Columbia University in New York City
- 1994: TCABR, at the University of São Paulo, São Paulo, Brazil; this tokamak was transferred from CRPP (now Swiss Plasma Center) in Switzerland
- 1996: Pegasus Toroidal Experiment at the University of Wisconsin–Madison; in operation since the late 1990s
- 1999: NSTX in Princeton, New Jersey
- 1999: Globus-M in Ioffe Institute, Saint Petersburg, Russia
- 2000: ETE at the National Institute for Space Research, São Paulo, Brazil
- 2002: HL-2A, in Chengdu, China
- 2006: EAST (HT-7U), in Hefei, at The Hefei Institutes of Physical Science, China (ITER member)
- 2007: QUEST, in Fukuoka, JAPAN https://www.triam.kyushu-u.ac.jp/QUEST_HP/suben/history.html
- 2008: KSTAR, in Daejon, South Korea (ITER member)
- 2012: Medusa CR, in Cartago, at the Costa Rica Institute of Technology, Costa Rica
- 2012: SST-1, in Gandhinagar, at the Institute for Plasma Research, India (ITER member)
- 2012: IR-T1, Islamic Azad University, Science and Research Branch, Tehran, Iran
- 2015: ST25-HTS at Tokamak Energy Ltd in Culham, United Kingdom
- 2017: KTM – this is an experimental thermonuclear facility for research and testing of materials under energy load conditions close to ITER and future energy fusion reactors, Kazakhstan.
- 2018: ST40 at Tokamak Energy Ltd in Oxford, United Kingdom
- 2020: HL-2M China National Nuclear Corporation and the Southwestern Institute of Physics, China
- 2020: MAST Upgrade, in Culham, Oxfordshire, United Kingdom; the world's largest spherical tokamak.
- 2023: JT-60SA, in Naka, Japan (ITER member); upgraded from the JT-60.
- 2024: HH70, China; The reactor is the first tokamak to feature ReBCO high-temperature superconductors.

### Previously operated

- 1960s: T-3 and T-4, in Kurchatov Institute, Moscow, Russia (formerly Soviet Union); T-4 in operation in 1968.
- 1963: LT-1, Australia National University's plasma physics group built a device to explore toroidal configurations, independently discovering the tokamak layout
- 1970: Stellarator C reopens as the Symmetric Tokamak in May at PPPL
- 1971–1980: Texas Turbulent Tokamak, University of Texas at Austin, US
- 1972: The Adiabatic Toroidal Compressor (ATC) begins operation at PPPL
- 1973–1976: Tokamak de Fontenay aux Roses (TFR), near Paris, France
- 1973–1979: Alcator A, MIT, US
- 1975: Princeton Large Torus begins operation at PPPL
- 1978–1987: Alcator C, MIT, US
- 1978–2013: TEXTOR, in Jülich, Germany
- 1979-1982 PDX operated at PPPL
- 1979–1998: MT-1 Tokamak, Budapest, Hungary (Built at the Kurchatov Institute, Russia, transported to Hungary in 1979, rebuilt as MT-1M in 1991)
- 1980–1990: Tokoloshe Tokamak, Atomic Energy Board, South Africa
- 1980–2004: TEXT/TEXT-U, University of Texas at Austin, US
- 1982–1997: TFTR, Princeton University, US
- 1983–2023: Joint European Torus (JET), in Culham, United Kingdom
- 1983–2000: Novillo Tokamak, at the Instituto Nacional de Investigaciones Nucleares, in Mexico City, Mexico
- 1984–1992: HL-1 Tokamak, in Chengdu, China
- 1985–2010: JT-60, in Naka, Ibaraki Prefecture, Japan; (Being upgraded 2015–2018 to Super, Advanced model)
- 1987–1999: Tokamak de Varennes; Varennes, Canada; operated by Hydro-Québec and used by researchers from *Institut de recherche en électricité du Québec* (IREQ) and the *Institut national de la recherche scientifique* (INRS)
- 1988–2005: T-15, in Kurchatov Institute, Moscow, Russia (formerly Soviet Union); 10 MW
- 1991–1998: START, in Culham, United Kingdom
- 1990s–2001: COMPASS, in Culham, United Kingdom
- 1994–2001: HL-1M Tokamak, in Chengdu, China
- 1999–2006: UCLA Electric Tokamak, in Los Angeles, US
- 1999–2014: MAST, in Culham, United Kingdom
- 1992–2016: Alcator C-Mod, MIT, Cambridge, US
- 1995–2013: HT-7, at the Institute of Plasma Physics, Hefei, China

### Planned

- ITER, international project in Cadarache, France; 500 MW; construction began in 2010, first plasma expected in 2034. Expected fully operational by 2039.
- DEMO; 2000 MW, continuous operation, connected to power grid. Planned successor to ITER; construction to begin in 2040 according to EUROfusion 2018 timetable.
- CFETR, also known as "China Fusion Engineering Test Reactor"; 200 MW; Next generation Chinese fusion reactor, is a new tokamak device.
- K-DEMO in South Korea; 2200–3000 MW, a net electric generation on the order of 500 MW is planned; construction is targeted by 2037.
- Spherical Tokamak for Energy Production (STEP), a UK project planning to produce a burning plasma by 2035.
- SPARC a development of Commonwealth Fusion Systems (CFS) in collaboration with the Massachusetts Institute of Technology (MIT) Plasma Science and Fusion Center (PSFC) in Devens, Massachusetts. Expected to achieve energy gain in 2026 with a fraction of ITERs size by utilizing high magnetic fields.
