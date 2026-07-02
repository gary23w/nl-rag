---
title: "Circulator"
source: https://en.wikipedia.org/wiki/Circulator
domain: waveguides
license: CC-BY-SA-4.0
tags: rectangular waveguide, cutoff frequency, transverse mode, waveguide filter
fetched: 2026-07-02
---

# Circulator

In electrical engineering, a **circulator** is a passive, non-reciprocal three- or four-port device that only allows a microwave or radio-frequency (RF) signal to exit through the port directly after the one it entered. Optical circulators have similar behavior. Ports are where an external waveguide or transmission line, such as a microstrip line or a coaxial cable, connects to the device. For a three-port circulator, a signal applied to port 1 only comes out of port 2; a signal applied to port 2 only comes out of port 3; a signal applied to port 3 only comes out of port 1. An ideal three-port circulator thus has the following scattering matrix:

$S={\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}}$

## Theory of operation

Microwave circulators rely on the anisotropic and *non-reciprocal* properties of magnetized microwave ferrite material. Microwave electromagnetic waves propagating in magnetized ferrite interact with electron spins in the ferrite and are consequently influenced by the microwave magnetic permeability of the ferrite. This permeability is mathematically described by a linear vector operator, also known as a tensor. In the case of magnetized ferrite, the permeability tensor is the Polder tensor. The permeability is a function of the direction of microwave propagation relative to the direction of static magnetization of the ferrite material. Hence, microwave signals propagating in different directions in the ferrite experience different magnetic permeabilities.

In the CGS system, the Polder tensor is

$B={\begin{bmatrix}\mu &j\kappa &0\\-j\kappa &\mu &0\\0&0&1\end{bmatrix}}H$

where (neglecting damping)

$\mu =1+{\frac {\omega _{0}\omega _{m}}{\omega _{0}^{2}-\omega ^{2}}}$

$\kappa ={\frac {\omega \omega _{m}}{{\omega _{0}}^{2}-\omega ^{2}}}$

$\omega _{0}=\gamma H_{0}\$

$\omega _{m}=\gamma M\$

$\gamma =1.40\cdot g\,\,$ MHz / Oe is the effective gyromagnetic ratio and g , the so-called effective g-factor, is a ferrite material constant typically in the range of 1.5 - 2.6, depending on the particular ferrite material. $\omega$ is the frequency of the RF/microwave signal propagating through the ferrite, $H_{0}$ is the internal magnetic bias field, and M is the magnetization of the ferrite material.

In junction circulators and differential phase shift circulators, microwave signal propagation is usually orthogonal to the static magnetic bias field in the ferrite. This is the so-called *transverse field* case. The microwave propagation constants for this case, neglecting losses are

$\Gamma _{+}=j\omega {\sqrt {\mu _{0}\epsilon }}\,{\sqrt {\frac {\mu ^{2}-\kappa ^{2}}{\mu }}}$

$\Gamma _{-}=j\omega {\sqrt {\mu _{0}\epsilon }}$

where $\mu _{0}$ is the permeability of free space and $\epsilon$ is the absolute permittivity of the ferrite material. In a circulator, these propagation constants describe waves having elliptical polarization that would propagate in the direction of the static magnetic bias field, which is through the thickness of the ferrite. The plus and minus subscripts of the propagation constants indicate opposite wave polarizations.

## Types

Microwave circulators fall into two main classes: differential phase shift circulators and junction circulators, both of which are based on cancellation of waves propagating over two different paths in or near magnetized ferrite material. Waveguide circulators may be of either type, while more compact devices based on stripline are usually of the junction type. Two or more junction circulators can be combined in a single component to give four or more ports. Typically permanent magnets produce a static magnetic bias in the microwave ferrite material. Ferrimagnetic garnet crystal is used in optical circulators.

### Junction circulators

#### Stripline junction circulators

A stripline junction circulator contains a resonator, which is located at the central junction of the striplines. This resonator may have any shape that has three-fold Rotational symmetry, such as a disk, hexagon, or triangle. An RF/microwave signal entering a circulator port is connected via a stripline to the resonator, where energy is coupled into two counter-rotating circular modes formed by the elliptically polarized waves. These circular modes have different phase velocities which can cause them to combine constructively or destructively at a given port. This produces an anti-node at one port (port 2 if the signal is incident upon port 1) and a node or null at another port (port 3 if the microwave energy is coupled from port 1 to port 2 and not reflected back into port 2).

If losses are neglected for simplification, the counter-rotating modes must differ in phase by an integer multiple of $2\pi$ for signal propagation from port 1 to port 2 (or from port 2 to port 3, or from port 3 to port 1):

$2\Gamma _{-}l-\Gamma _{+}l=2m\pi$

and similarly, for the remaining port (port 3 if signal propagation is from port 1 to port 2) to be nulled,

$-\Gamma _{-}l+2\Gamma _{+}l=(2n-1)\pi$

where l is the path length between adjacent ports and m and n are integers. Solving the two preceding equations simultaneously, for proper circulation the necessary conditions are

$\Gamma _{-}l={\frac {4m+2n-1}{3}}\pi$

and

$\Gamma _{+}l={\frac {2m+4n-2}{3}}\pi$

Each of the two counter-rotating modes has its own resonant frequency. The two resonant frequencies are known as the split frequencies. The circulator operating frequency is set between the two split frequencies.

These circulator types operate based on faraday rotation. Wave cancellation occurs when waves propagate with and against the circulator's direction of circulation. An incident wave arriving at any port is split equally into two waves. They propagate in each direction around the circulator with different phase velocities. When they arrive at the output port they have different phase relationships and thus combine accordingly. This combination of waves propagating at different phase velocities is how junction circulators fundamentally operate.

The geometry of a stripline junction circulator comprises two ferrite disks or triangles separated by a stripline center conductor and sandwiched between two parallel ground planes. A stripline circulator is essentially a stripline center conductor sandwich on ferrite, between ground planes. That is, there is one ferrite disk above the stripline circuit and one ferrite disk below the stripline circuit. Stripline circulators do not have to be constructed with disk- or triangle-shaped ferrites; the ferrites can have almost any shape that has three-way symmetry. This is also true of the resonator (the center junction portion of the center conductor)- it can be any shape that has three-way symmetry, although there are electrical considerations.

The ferrites are magnetized through their thicknesses, i.e., the static magnetic bias field is perpendicular to the plane of the device and the direction of signal propagation is transverse to the direction of the static magnetic field. Both ferrites are in the same static ad RF magnetic fields. The two ferrites can be thought of as one continuous ferrite with an embedded stripline center conductor. For practical manufacturing reasons, the center conductor is not generally embedded in ferrite, so two discrete ferrites are used. The static magnetic bias field is typically provided by permanent magnets that are located external to the circulator ground planes. Magnetic shielding incorporated into the circulator design prevents detuning or partial demagnetization of the circulator in the presence of external magnetic fields or ferrous materials, and protects nearby devices from the effects of the circulator's static magnetic field.

- Internal Construction of Stripline Junction Circulators
- (Internal construction of a stripline junction circulator having triangular ferrites and an irregular triangle-shaped resonator.)Internal construction of a stripline junction circulator having triangular ferrites and an irregular triangle-shaped resonator.
- (Internal construction of stripline junction circulator having disk ferrites and a disk-shaped resonator.)Internal construction of stripline junction circulator having disk ferrites and a disk-shaped resonator.
- (Internal construction of a stripline junction circulator having disk ferrites and a triangle-shaped resonator.)Internal construction of a stripline junction circulator having disk ferrites and a triangle-shaped resonator.

#### Waveguide junction circulators

A waveguide junction circulator contains a magnetized ferrite resonator, which is located at the junction of three waveguides. In contrast with a stripline junction circulator, the ferrite itself is the resonator, rather than the metal central portion of a stripline center conductor. The ferrite resonator may have any shape that has three-fold rotational symmetry, such as a cylinder or triangular prism. The resonator is often just one ferrite, but it is sometimes composed of two or more ferrites, which may be coupled to each other, in various geometrical configurations. The geometry of the resonator is influenced by electrical and thermal performance considerations. Waveguide junction circulators function in much the same way as stripline junction circulators, and their basic theory of operation is the same.

The internal geometry of a waveguide junction circulator comprises a junction of three waveguides, the ferrite resonator, and impedance matching structures. Many of these circulators contain pedestals located in the central junction, on which the ferrite resonator is located. These pedestals effectively reduce the height of the waveguide, reducing its characteristic impedance in the resonator region to optimize electrical performance. The reduced-height waveguide sections leading from the resonator to the full-height waveguides serve as impedance transformers.

The ferrite resonator is magnetized through its height, i.e., the static magnetic bias field is perpendicular to the plane of the device and the direction of signal propagation is transverse to the direction of the static magnetic field. The static magnetic bias field is typically provided by permanent magnets that are external to the waveguide junction.

E-Field Plots Showing Electromagnetic Wave Propagation in Waveguide Junction Circulators

|   |   |
|---|---|

#### Microstrip junction circulators

The microstrip junction circulator is another widely used form of circulator that utilizes the microstrip transmission line topology. A microstrip circulator consists primarily of a circuit pattern on a ferrite substrate. The circuit is typically formed using thick-film or thin-film metallization processes, often including photolithography. The ferrite substrate is sometimes bonded to a ferrous metal carrier, which serves to improve the efficiency of the magnetic circuit, increase the mechanical strength of the circulator, and protect the ferrite from thermal expansion mismatches between it and the surface to which the circulator is mounted. A permanent magnet that is bonded to the circuit face of the ferrite substrate provides the static magnetic bias to the ferrite. Microstrip circulators function in the same way as stripline junction circulators, and their basic theory of operation is the same. In comparison with stripline circulators, electrical performance of microstrip circulators is somewhat reduced because of radiation and dispersion effects.

The performance disadvantages of microstrip circulators are offset by their relative ease of integration with other planar circuitry. The electrical connections of these circulators to adjacent circuitry are typically made using wire bonds or ribbon bonds. Another advantage of microstrip circulators is their smaller size and correspondingly lower mass than stripline circulators. Despite this advantage, microstrip circulators are often the largest components in microwave modules.

#### Self-biased junction circulators

Self-biased junction circulators are unique in that they do not utilize permanent magnets that are separate from the microwave ferrite. The elimination of external magnets significantly reduces the size and weight of the circulator compared to electrically-equivalent microstrip junction circulators for similar applications.

Monolithic ferrites that are used for self-biased circulators are M-type uniaxial (single magnetic axis) hexagonal ferrites that have been optimized to have low microwave losses. In contrast with the magnetically soft (low-coercivity) ferrites used in other circulators, the hexagonal ferrites used for self-biased circulators are magnetically hard (high-coercivity) materials. These ferrites are essentially ceramic permanent magnets. In addition to their high magnetic remanence, these ferrites have very large magnetic anisotropy fields, enabling circulator operation up to high microwave frequencies.

Because of their thin, planar shape, self-biased circulators can be conveniently integrated with other planar circuitry. Integration of self-biased circulators with semiconductor wafers has been demonstrated at KA-band and V-band frequencies.

### Lumped-element circulators

Lumped-element circulators are small-size devices that are typically used at frequencies in the HF through UHF bands. In a junction circulator, the size of the ferrite(s) is proportional to signal wavelength, but in a lumped-element circulator, the ferrite can be smaller because there is no such wavelength proportionality.

In a lumped-element circulator, conductors are wrapped around the ferrite, forming what is typically a woven mesh. The conductor strips are insulated from each other by thin dielectric layers. In some circulators, the mesh is in the form of traces on a printed wiring board with metallized vias to make connections between layers. The conductive strips can be thought of as non-reciprocally coupled inductors. Impedance matching circuitry and broad-banding circuitry in lumped-element circulators are often constructed using discrete ceramic capacitors and air-core inductors.

This class of circulator offers a considerable size reduction compared with the junction circulators. On the other hand, lumped-element circulators generally have lower RF power handling capacity than equivalent junction devices and are more complex from a mechanical perspective. The discrete lumped-element inductors and capacitors can be less stable when exposed to vibration or mechanical shocks than the simple distributed impedance transformers in a stripline junction circulator.

### Switching circulators

Switching circulators are similar to other junction circulators, and their microwave theory of operation is the same, except that their direction of circulation can be electronically controlled.

Junction circulators use permanent magnets to provide the static magnetic bias for the ferrite(s). However, switching circulators typically rely on the remanent magnetization of the ferrite itself. The ferrites that are used in switching circulators have square magnetic hysteresis loops and often sub-Oersted coercivities. Such a ferrite material requires a relatively small magnetic field and low energy level to flip its magnetic polarity. This is distinctly advantageous for a switching circulator, but the absence of permanent magnets would be a disadvantage of a non-switching junction circulator that must retain its magnetic bias despite exposures to the potentially demagnetizing effects of stray magnetic fields, nearby ferrous materials, and temperature variations.

The magnetization polarity of the ferrite, and hence the direction of circulation of a switching circulator, is controlled using a magnetizing coil that loops through the ferrite. The coil is connected to electronic driver circuitry that sends current pulses of the correct polarity through the magnetizing coil to magnetize the ferrite in the polarity to provide the desired direction of circulation.

### Differential phase shift circulators

Differential phase shift circulators are mainly used in high power microwave applications. They are usually built from rectangular waveguide components. These circulators are 4-port devices having circulation in the sequence 1 - 2 - 3 - 4 - 1, with ports numbered as shown in the schematic. There are various feasible circulator architectures, the most common of which utilizes a magic tee hybrid coupler, a quadrature hybrid coupler, and two oppositely magnetized differential phase shifters.

A differential phase shifter provides *non-reciprocal* transmission phase shift. That is, the forward phase shift is different from the phase shift in the reverse transmission direction. It is this difference in phase shifts that enables the non-reciprocal behavior of the circulator. A differential phase shifter consists of one or more ferrite slabs, usually positioned on the broad wall(s) of the waveguide. Permanent magnets located outside the waveguide provide static magnetic bias field to the ferrite(s). The ferrite-loaded waveguide is another example of a *transverse-field* device as described in Circulator § Theory of operation. Different microwave propagation constants corresponding to different directions of signal propagation give rise to different phase velocities and hence, different transmission phase shifts.

Depending on which circulator port an incident signal enters, phase shift relationships in the hybrid couplers and the differential phase shifts cause signals to combine at one other port and cancel at each of the remaining two ports. Differential phase shift circulators are often used as 3-port circulators by connecting one circulator port to a reflectionless termination, or they can be used as isolators by terminating two circulator ports.

## Non-ferrite circulators

Though ferrite circulators can provide good "forward" signal circulation while suppressing greatly the "reverse" circulation, their major shortcomings, especially at low frequencies, are the bulky sizes and the narrow bandwidths.

Early work on non-ferrite circulators includes active circulators using transistors that are non-reciprocal in nature. In contrast to ferrite circulators which are passive devices, active circulators require power. Major issues associated with transistor-based active circulators are the power limitation and the signal-to-noise degradation, which are critical when it is used as a duplexer for sustaining the strong transmit power and clean reception of the signal from the antenna.

Varactors offer one solution. One study employed a structure similar to a time-varying transmission line with the effective nonreciprocity triggered by a one-direction propagating carrier pump. This is like an AC-powered active circulator. The research claimed to be able to achieve positive gain and low noise for receiving path and broadband nonreciprocity. Another study used resonance with nonreciprocity triggered by angular-momentum biasing, which more closely mimics the way that signals passively circulate in a ferrite circulator.

In 1964, Mohr presented and experimentally demonstrated a circulator based on transmission lines and switches. In April, 2016 a research team significantly extended this concept, presenting an integrated circuit circulator based on N-path filter concepts. It offers the potential for full-duplex communication (transmitting and receiving at the same time with a single shared antenna over a single frequency). The device uses capacitors and a clock and is much smaller than conventional devices.

## Applications

### Isolator

When one port of a three-port circulator is terminated in a matched load, it can be used as an *isolator*, since a signal can travel in only one direction between the remaining ports. An isolator is used to shield equipment on its input side from the effects of conditions on its output side; for example, to prevent a microwave source being detuned by a mismatched load.

### Duplexer

In radar, circulators are used as a type of duplexer, to route signals from the transmitter to the antenna and from the antenna to the receiver, without allowing signals to pass directly from transmitter to receiver. The alternative type of duplexer is a *transmit-receive switch* (*TR switch*) that alternates between connecting the antenna to the transmitter and to the receiver. The use of chirped pulses and a high dynamic range may lead to temporal overlap of the sent and received pulses, however, requiring a circulator for this function.

### Reflection amplifier

A reflection amplifier is a type of microwave amplifier circuit utilizing negative differential resistance diodes such as tunnel diodes and Gunn diodes. Negative differential resistance diodes can amplify signals, and often perform better at microwave frequencies than two-port devices. However, since the diode is a one-port (two terminal) device, a nonreciprocal component is needed to separate the outgoing amplified signal from the incoming input signal. By using a 3-port circulator with the signal input connected to one port, the biased diode connected to a second, and the output load connected to the third, the output and input can be uncoupled.
