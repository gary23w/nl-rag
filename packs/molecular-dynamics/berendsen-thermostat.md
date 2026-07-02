---
title: "Berendsen thermostat"
source: https://en.wikipedia.org/wiki/Berendsen_thermostat
domain: molecular-dynamics
license: CC-BY-SA-4.0
tags: molecular dynamics, force field chemistry, lennard-jones potential, periodic boundary conditions
fetched: 2026-07-02
---

# Berendsen thermostat

The **Berendsen thermostat** is an algorithm to re-scale the velocities of particles in molecular dynamics simulations to control the simulation temperature. It is named after Herman Berendsen.

## Description

In this scheme, the system is weakly coupled to a heat bath with some temperature. The thermostat suppresses fluctuations of the kinetic energy of the system and therefore cannot produce trajectories consistent with the canonical ensemble. The temperature of the system is corrected such that the deviation exponentially decays with some time constant $\tau$ .

${\frac {dT}{dt}}={\frac {T_{0}-T}{\tau }}$

Though the thermostat does not generate a correct canonical ensemble (especially for small systems), for large systems on the order of hundreds or thousands of atoms/molecules, the approximation yields roughly correct results for most calculated properties. The scheme is widely used due to the efficiency with which it relaxes a system to some target (bath) temperature. In many instances, systems are initially equilibrated using the Berendsen scheme, while properties are calculated using the widely known Nosé–Hoover thermostat, which correctly generates trajectories consistent with a canonical ensemble. However, the Berendsen thermostat can result in the flying ice cube effect, an artifact which can be eliminated by using the more rigorous Bussi–Donadio–Parrinello thermostat; for this reason, it has been recommended that usage of the Berendsen thermostat be discontinued in almost all cases except for replication of prior studies.
