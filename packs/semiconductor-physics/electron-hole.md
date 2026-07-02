---
title: "Electron hole"
source: https://en.wikipedia.org/wiki/Electron_hole
domain: semiconductor-physics
license: CC-BY-SA-4.0
tags: semiconductor physics, energy band gap, semiconductor doping, charge carrier
fetched: 2026-07-02
---

# Electron hole

In physics, chemistry, and electronic engineering, an **electron hole** (often simply called a **hole**) is a quasiparticle denoting the lack of an electron at a position where one could exist in an atom or atomic lattice. Since in a normal atom or crystal lattice the negative charge of the electrons is balanced by the positive charge of the atomic nuclei, the absence of an electron leaves a net positive charge at the hole's location.

Holes in a metal or semiconductor crystal lattice can move through the lattice as electrons can, and act similarly to positively-charged particles. They play an important role in the operation of semiconductor devices such as transistors, diodes (including light-emitting diodes) and integrated circuits. If an electron is excited into a higher state it leaves a hole in its old state. This meaning is used in Auger electron spectroscopy (and other x-ray techniques), in computational chemistry, and to explain the low electron-electron scattering-rate in crystals (metals and semiconductors). Although they act like elementary particles, holes are rather quasiparticles; they are different from the positron, which is the antiparticle of the electron. (See also Dirac sea.)

In crystals, electronic band structure calculations show that electrons have a negative effective mass at the top of a band. Although negative mass is unintuitive, a more familiar and intuitive picture emerges by considering a hole, which has a positive charge and a positive mass, instead.

## Definition

In semiconductors, an *electron hole* (usually referred to simply as a *hole*) is the absence of an electron from a full valence band. A hole is essentially a way to conceptualize the interactions of the electrons within a nearly full valence band of a crystal lattice, which is missing a small fraction of its electrons. In some ways, the behavior of a hole within a semiconductor crystal lattice is comparable to that of the bubble in a full bottle of water.

More generally, a hole is defined as the absence of an electron relative to the system's ground state. This concept applies not only to semiconductors but also to metals with partially filled bands and other electronic systems. A hole with wavevector *k* and spin $\uparrow$ is created by removing an electron with a wavevector *$-k$* and spin $\downarrow$ .

The hole concept was pioneered in 1929 by Rudolf Peierls, who analyzed the Hall effect using Bloch's theorem, and demonstrated that a nearly full and a nearly empty Brillouin zones give the opposite Hall voltages.

## Simplified analogy: Empty seat in an auditorium

Hole conduction in a valence band can be explained by the following analogy:

Imagine a row of people seated in an auditorium, where there are no spare chairs. Someone in the middle of the row wants to leave, so he jumps over the back of the seat into another row, and walks out. The empty row is analogous to the conduction band, and the person walking out is analogous to a conduction electron.

Now imagine someone else comes along and wants to sit down. The empty row has a poor view; so he does not want to sit there. Instead, a person in the crowded row moves into the empty seat the first person left behind. The empty seat moves one spot closer to the edge and the person waiting to sit down. The next person follows, and the next, et cetera. One could say that the empty seat moves towards the edge of the row. Once the empty seat reaches the edge, the new person can sit down.

In the process everyone in the row has moved along. If those people were negatively charged (like electrons), this movement would constitute conduction. If the seats themselves were positively charged, then only the vacant seat would be positive. This is a very simple model of how hole conduction works.

Instead of analyzing the movement of an empty state in the valence band as the movement of many separate electrons, a single equivalent imaginary particle called a "hole" is considered. In an applied electric field, the electrons move in one direction, corresponding to the hole moving in the other. If a hole associates itself with a neutral atom, that atom loses an electron and becomes positive. Therefore, the hole is taken to have positive charge of +*e*, precisely the opposite of the electron charge.

In reality, due to the uncertainty principle of quantum mechanics, combined with the energy levels available in the crystal, the hole is not localizable to a single position as described in the previous example. Rather, the positive charge which represents the hole spans an area in the crystal lattice covering many hundreds of unit cells. This is equivalent to being unable to tell which broken bond corresponds to the "missing" electron. Conduction band electrons are similarly delocalized.

## Detailed picture: A hole is the absence of a negative-mass electron

The analogy above is quite simplified, and cannot explain why holes in semiconductors create an opposite effect to electrons in the Hall effect and Seebeck effect. A more precise and detailed explanation follows.

*The dispersion relation determines how electrons respond to forces (via the concept of effective mass).*

A dispersion relation is the relationship between wavevector (k-vector) and energy in a band, part of the electronic band structure. In quantum mechanics, the electrons are waves, and energy is the wave frequency. A localized electron is a wavepacket, and the motion of an electron is given by the formula for the group velocity of a wave. An electric field affects an electron by gradually shifting all the wavevectors in the wavepacket, and the electron accelerates when its wave group velocity changes. Therefore, again, the way an electron responds to forces is entirely determined by its dispersion relation. An electron floating in space has the dispersion relation *E* = ℏ2*k*2/(2*m*), where *m* is the (real) electron mass and ℏ is reduced Planck constant. Near the bottom of the conduction band of a semiconductor, the dispersion relation is instead *E* = ℏ2*k*2/(2*m**) (*m** is the *effective mass*), so a conduction-band electron responds to forces *as if* it had the mass *m**.

*Electrons near the top of the valence band behave as if they have negative mass.*

The dispersion relation near the top of the valence band is *E* = ℏ2*k*2/(2*m**) with *negative* effective mass. So electrons near the top of the valence band behave like they have negative mass. When a force pulls the electrons to the right, these electrons actually move left. This is solely due to the shape of the valence band and is unrelated to whether the band is full or empty. If you could somehow empty out the valence band and just put one electron near the valence band maximum (an unstable situation), this electron would move the "wrong way" in response to forces.

*Positively-charged holes as a shortcut for calculating the total current of an almost-full band.*

A perfectly full band always has zero current. One way to think about this fact is that the electron states near the top of the band have negative effective mass, and those near the bottom of that band have positive effective mass, so the net motion is exactly zero. If an otherwise-almost-full valence band has a state *without* an electron in it, we say that this state is occupied by a hole. There is a mathematical shortcut for calculating the current due to every electron in the whole valence band: Start with zero current (the total if the band were full), and *subtract* the current due to the electrons that *would* be in each hole state if it wasn't a hole. Since *subtracting* the current caused by a *negative* charge in motion is the same as *adding* the current caused by a *positive* charge moving on the same path, the mathematical shortcut is to pretend that each hole state is carrying a positive charge, while ignoring every other electron state in the valence band.

*A hole near the top of the valence band moves the same way as an electron near the top of the valence band **would** move* (which is in the opposite direction compared to conduction-band electrons experiencing the same force.)

This fact follows from the discussion and definition above. This is an example where the auditorium analogy above is misleading. When a person moves left in a full auditorium, an empty seat moves right. But in this section we are imagining how electrons move through k-space, not real space, and the effect of a force is to move all the electrons through k-space in the same direction at the same time. In this context, a better analogy is a bubble underwater in a river: The bubble moves the same direction as the water, not the opposite.

Since force = mass × acceleration, a negative-effective-mass electron near the top of the valence band would move the opposite direction as a positive-effective-mass electron near the bottom of the conduction band, in response to a given electric or magnetic force. Therefore, a hole moves this way as well.

*Conclusion: Hole is a positive-charge, positive-mass quasiparticle*.

From the above, a hole (1) carries a positive charge, and (2) responds to electric and magnetic fields as if it had a positive charge and positive mass. (The latter is because a particle with positive charge and positive mass respond to electric and magnetic fields in the same way as a particle with a negative charge and negative mass.) That explains why holes can be treated in all situations as ordinary positively charged quasiparticles.

## Role in semiconductor technology

In some semiconductors, such as silicon, the hole's effective mass is dependent on a direction (anisotropic), however a value averaged over all directions can be used for some macroscopic calculations.

In most semiconductors, the effective mass of a hole is much larger than that of an electron. This results in lower mobility for holes under the influence of an electric field and this may slow down the speed of the electronic device made of that semiconductor. This is one major reason for adopting electrons as the primary charge carriers, whenever possible in semiconductor devices, rather than holes. This is also why NMOS logic is faster than PMOS logic. OLED screens have been modified to reduce imbalance resulting in non radiative recombination by adding extra layers and/or decreasing electron density on one plastic layer so electrons and holes precisely balance within the emission zone. However, in many semiconductor devices, both electrons *and* holes play an essential role. Examples include p–n diodes, bipolar transistors, and CMOS logic.

## Comparison to positron

A hole in semiconductor physics, defined as the absence of an electron in a nearly full valence band, has a formal analogy to the positron in Paul Dirac's relativistic theory of the electron (See Dirac equation). In both cases, the system is described as a filled sea of negative-energy or valence states, and the removal of an electron leads to a positively charged entity that can carry current. The analogy extends to their electromagnetic behavior: both holes and positrons have a charge that is equal and opposite to that of an electron. When an electron and positron collide, they annihilate each other and the energy is emitted as photons or other radiation. An analogous process, recombination, happens in semiconductors, and can be described as an electron falling to the empty hole state and filling it, emitting radiation.

However, there are also limitations to this analogy. Due to the symmetries of Dirac's theory, positron and electron have exactly the same mass, while holes and electrons in crystals generally have different masses. The positron is a real particle with positive inertial mass and rest energy, while the hole is a quasiparticle whose inertial mass is negative. For this reason the responses differ in non-inertial frames: in an accelerating crystal lattice, a positron lags behind, whereas a hole moves forward with the lattice. These differences also appear in composite systems; for example, excitons (electron–hole pairs) move rigidly with the lattice and carry no net momentum, unlike positronium atoms (electron–positron pairs), which gain momentum and energy relative to an accelerating frame.

The concept of an electron hole in solid-state physics predates the concept of a hole in Dirac equation, but there is no evidence that it would have influenced Dirac's thinking.
