---
title: "Balun"
source: https://en.wikipedia.org/wiki/Balun
domain: smith-chart-matching
license: CC-BY-SA-4.0
tags: antenna tuner, quarter-wave transformer, impedance matching, matching stub
fetched: 2026-07-02
---

# Balun

A **balun** /ˈbælʌn/ (from "balanced to unbalanced", originally, but now derived from "**balancing unit**") is an electrical device that allows balanced and unbalanced lines to be interfaced without disturbing the impedance arrangement of either line. A balun can take many forms and may include devices that also transform impedances but need not do so. Sometimes, in the case of transformer baluns, they use magnetic coupling but need not do so. Common-mode chokes are also used as baluns and work by eliminating, rather than rejecting, common mode signals.

## Types of balun

### Classical transformer type

In classical transformers, there are two electrically separate windings of wire coils around the transformer's core. The advantage of transformer-type over other types of balun is that the electrically separate windings for input and output allow these baluns to connect circuits whose ground-level voltages are subject to ground loops or are otherwise electrically incompatible; for that reason they are often called isolation transformers.

This type is sometimes called a 'voltage balun'. The primary winding receives the input signal, and the secondary winding puts out the converted signal. The core that they are wound on may either be empty (air core) or, equivalently, a magnetically neutral material like a porcelain support, or it may be a material which is good magnetic conductor like ferrite in modern high-frequency (HF) baluns, or soft iron as in the early days of telegraphy.

The electrical signal in the primary coil is converted into a magnetic field in the transformer's core. When the electrical current through the primary reverses, it causes the established magnetic field to collapse. The collapsing magnetic field then induces an electric field in the secondary winding.

The ratio of loops in each winding and the efficiency of the coils' magnetic coupling determines the ratio of electrical potential (voltage) to electrical current and the total power of the output. For idealized transformers, although the ratio of voltage to current will change in exact proportion to the square of the winding ratio, the power (measured in watts) remains identical. In real transformers, some energy is lost inside to heating of the metallic core of the transformer, to the AC and DC resistances of the winding conductors, and lost outside to the surrounding environment because of imperfect magnetic coupling between the two coils.

### Autotransformer type

An ideal balun consists of two wires (primary and secondary) and a core: the current in the primary wire generates a magnetic field in the core, which in turn induces an electric field in the secondary wire. An autotransformer balun has only one coil, or is made of two or more coils that have an electrical connection, wound around a core. One can also make an autotransformer from an ordinary transformer by cross-wiring the primary and secondary windings. Baluns made with autotransformer windings are also called *voltage baluns*, since they produce balanced output voltage, but not necessarily balanced current.

In all autotransformers, the single winding must have at least one extra electrical connection – called a *tap* or *tap point* – between the two ends of the winding. The current sent into the balun through one pair of connections acts as if it were a primary coil, and magnetizes the entire core. When the electric current in the input segment of the coil changes, the induced magnetic field collapses and the collapse of the magnetic field in the core induces an electric current in the entire coil. Electrical connections to parts of the coil different from the input connections have higher or lower voltages depending on the length of the coil that the output is tapped from.

Unlike transformer-type baluns, an autotransformer balun provides a path for DC current to ground from every terminal. Since outdoor antennas are prone to build-up of static electric charge, the path for the static to drain to ground through an autotransformer balun can be a distinct advantage.

### Transmission-line transformer type

Transmission line or *choke* baluns can be considered as simple forms of transmission line transformers. This type is sometimes called a *current balun*, since it ensures equal current on both sides of its output, but not necessarily equal voltage. These are normally called ununs, because they go from unbalanced to unbalanced or un-un. Baluns are balanced to unbalanced or bal-un.

A more subtle type results when the transformer type (magnetic coupling) is combined with the transmission line type (electro-magnetic coupling). Most typically the same kind of transmission line wires are used for the windings as carry the signal from the radio to the antenna, although these baluns can be made using any type of wire. The resulting devices have very wideband operation. *Transmission line transformers* commonly use small ferrite cores in toroidal rings or two-hole, binocular, shapes.

The Guanella transmission line transformer (Guanella 1944) is often combined with a balun to act as an impedance matching transformer. Putting balancing aside a transformer of this type consists of a 75 Ω transmission line divided in parallel into two 150 Ω cables, which are then combined in series for 300 Ω. It is implemented as a specific wiring around the ferrite core of the balun.

Classic magnetic transformers are limited in maximum frequency due to the permeability of the magnetic material, which declines rapidly above MHz frequencies. This limits the operating frequency to around 1 GHz. Microwave systems require baluns in the 1-100 GHz range for applications including mixers, push-pull amplifiers, and interface to differential analog to digital and digital to analog converters.

Transmission line transformer baluns with a high frequency transmission line such as a wirewound pair are able to operate at significantly higher frequencies (to 8 GHz and above) by combining capacitive coupling with magnetic coupling typical of classic magnetic transformers.

### Planar and Marchand Baluns

To operate at even higher frequencies, magnetic loading becomes ineffective. Nathan Marchand proposed a 'conversion transformer' that was capable of operation over a 1:3 bandwidth ratio in 1944. This basic circuit has been widely adapted and modified for use in planar structures (such as MMICs and RFICs) at frequencies up to at least 100 GHz.

These types of planar baluns work exciting a mode in a ground plane or shield, which is then 'floated' away from the main ground. This allows extraction of the negative signal in addition to the main transmission line, creating positive and negative signal pairs. By connecting the positive and negative signal paths in various configurations dozens of balun configurations have been proposed and published in the electronics literature.

## Self-resonance

Although baluns are designed as magnetic devices – each winding in a balun is an inductor – all transformers made of real materials also have a small capacitance between the primary and secondary windings, as well as between individual loops in any single winding, forming unwanted *self-capacitance*.

The electrical connection of capacitance and inductance leads to a frequency where the electrical reactance of the self-inductance and self-capacitance in the balun are equal in magnitude but opposite in sign: that is, to resonance. A balun of any design operates poorly at or above its self-resonant frequency, and some of the design considerations for baluns are for the purpose of making the resonant frequency as far above the operating frequency as possible.

## Balun alternatives

An RF choke can be used in place of a balun. If a coil is made using coaxial cable near to the feed point of a balanced antenna, then the RF current that flows on the outer surface of the coaxial cable can be attenuated. One way of doing this would be to pass the cable through a ferrite toroid. The end result is exactly the same as a 1:1 current balun (or Guanella-type balun). (Straw 2005, 25-26)

## Applications

A balun's function is generally to achieve compatibility between systems, and as such, finds extensive application in modern communications, particularly in realising frequency conversion mixers to make cellular phone and data transmission networks possible. They are also used to send an E1 carrier signal from coaxial cable (BNC connector, 1.0/2.3 connector, 1.6/5.6 connector, Type 43 connectors) to UTP CAT-5 cable or IDC connector.

### Radio and television

In television, amateur radio, and other antenna installations and connections, baluns convert between impedances and symmetry of feedlines and antennas.

For example, transformation of 300-Ω twin-lead or 450-Ω ladder line (balanced) to 75-Ω coaxial cable (unbalanced), or to directly connect a balanced antenna to unbalanced coaxial cable. To avoid feed line radiation, baluns are typically used as a form of common mode choke attached at the antenna feed point to prevent the coaxial cable from acting as an antenna and radiating power. This typically is needed when a balanced antenna (for instance, a dipole) is fed with coax; without a balun, the shield of the coax could couple with one side of the dipole, inducing common mode current, and becoming part of the antenna and unintentionally radiating.

In measuring the impedance or radiation pattern of a balanced antenna using a coaxial cable, it is important to place a balun between the cable and the antenna feed. Unbalanced currents that may otherwise flow on the cable will make the measured antenna impedance sensitive to the configuration of the feed cable, and the radiation pattern of small antennas may be distorted by radiation from the cable.

Baluns are present in radars, transmitters, satellites, in every telephone network, and probably in most wireless network modem/routers used in homes. It can be combined with transimpedance amplifiers to compose high-voltage amplifiers out of low-voltage components.

### Video

Baseband video uses frequencies up to several megahertz. A balun can be used to couple video signals to twisted-pair cables instead of using coaxial cable. Many security cameras now have both a balanced unshielded twisted pair (UTP) output and an unbalanced coaxial one via an internal balun. A balun is also used on the video recorder end to convert back from the 100 Ω balanced to 75 Ω unbalanced. A balun of this type has a BNC connector with two screw terminals. VGA/DVI baluns are baluns with electronic circuitry used to connect VGA/DVI sources (laptop, DVD, etc.) to VGA/DVI display devices over long runs of CAT-5/CAT-6 cable. Runs over 130 m (400 ft) may lose quality because of attenuation and variations in the arrival time of each signal. A skew control and special low skew or skew free cable is used for runs over 130 m (400 ft).

### Audio

In audio applications, baluns serve multiple purposes: they can convert between high-impedance unbalanced and low impedance balanced lines. Another application is decoupling of devices (avoidance of earth loops).

A third application of baluns in audio systems is in the provision of balanced mains power to the equipment. The common-mode rejection of interference characteristic of balanced mains power, eliminates a wide range of noise coming from the wall plug, e.g. mains-borne interference from air conditioner/furnace/refrigerator motors, switching noise produced by fluorescent lighting and dimmer switches, digital noise from personal computers, and radio frequency signals picked up by the power lines/cords acting as antennae. This noise infiltrates the audio/video system through the power supplies and raises the noise floor of the entire system.

Except for the connections, the three devices in the image are electrically identical, but only the leftmost two can be used as baluns. The device on the left would normally be used to connect a high impedance source, such as a guitar, into a balanced microphone input, serving as a passive DI unit. The one in the center is for connecting a low impedance balanced source, such as a microphone, into a guitar amplifier. The one at the right is not a balun, as it provides only impedance matching.

### Other applications

- In power line communications, baluns are used in coupling signals onto a power line.
- In electronic communications, baluns convert Twinax cables to Cat 5 cables, and back.
