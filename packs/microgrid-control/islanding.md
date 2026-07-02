---
title: "Islanding"
source: https://en.wikipedia.org/wiki/Islanding
domain: microgrid-control
license: CC-BY-SA-4.0
tags: microgrid, distributed generation, islanding, virtual power plant
fetched: 2026-07-02
---

# Islanding

**Islanding** is the intentional or unintentional division of an synchronous interconnected power grid into individual disconnected regions with their own power generation and distinct frequency.

Intentional islanding is often performed as a defence in depth to mitigate a cascading blackout. If one island collapses, it will not take neighboring islands with it. For example, nuclear power plants have safety-critical cooling systems that are typically powered from the general grid. The coolant loops typically lie on a separate circuit that can also operate off reactor power or emergency diesel generators if the grid collapses.

Grid designs that lend themselves to islanding near the customer level are commonly referred to as microgrids. In a power outage, the microgrid controller disconnects the local circuit from the grid on a dedicated switch and forces any online distributed generators to power the local load.

Unintentional islanding is a dangerous condition that may induce severe stress on the generator, as the generator must match any changes in electrical load alone. If not properly communicated to power line workers, an unintentional island can also present a risk of electrical shock. Unlike unpowered wires, islands require special techniques to reconnect to the larger grid, because the alternating current they carry is not in phase. For these reasons, solar inverters that are designed to supply power to the grid are generally required to have some sort of automatic anti-islanding circuitry, which shorts out the panels rather than continuing to power the unintentional island.

Methods that detect islands without a large number of false positives constitute the subject of considerable research. Each method has some threshold that needs to be crossed before a condition is considered to be a signal of grid interruption, which leads to a "**non-detection zone**" (NDZ), the range of conditions where a real grid failure will be filtered out. For this reason, before field deployment, grid-interactive inverters are typically tested by reproducing at their output terminals specific grid conditions and evaluating the effectiveness of the anti-islanding methods in detecting island conditions.

## Intentional islanding

Intentional islanding divides an electrical network into fragments with adequate power generation in each fragment to supply that fragment's loads. In practice, balancing generation and load in each fragment is difficult, and often the formation of islands requires temporarily shedding load. Synchronous generators may not deliver sufficient reactive power to prevent severe transients during fault-induced island formation, and any inverters must switch from constant-current to constant-voltage control. Intentional islanding can be used after a blackout and during the black start process to restore power to isolated parts of the grid.

Assuming P≠NP, no good cut set criterion exists to implement islanding. Polynomial-time approximations exist, but finding the exactly optimal divisions can be computationally infeasible.

However, islanding localizes any failures to the containing island, preventing failures from spreading. In general, blackout statistics follow a power law, such that fragmenting a network increases the probability of blackouts, but reduces the total amount of unsatisfied electricity demand.

Islanding reduces the economic efficiency of the wholesale power market, and is typically a last resort applied when the grid is known to be unstable but has not yet collapsed. In particular, islanding improves resilience to threats with known time but not location, such as terrorist attacks, military strikes on electrical infrastructure, or extreme weather events.

### Home islanding

Following the 2019 California power shutoffs, there was a rise in interest in the possibility of operating a house's electrical grid as an island. While typical distributed generation systems are too small to power all appliances in a home simultaneously, it is possible for them to manage critical household power needs through traditional load-frequency control. Modules installed in series between the generator and large loads, like air conditioners and electric ovens, measure the island power frequency and perform automatic load shedding as the inverter nears overload.

## Detection methods

Automatically detecting an island is the subject of considerable research. These can be performed passively, looking for transient events on the grid; or actively, by creating small instances of those transient events that will be negligible on a large grid but detectable on a small one. Active methods may be performed by local generators or "upstream" at the utility level.

Many passive methods rely on the inherent stress of operating an island. Each device in the island comprises a much larger proportion of the total load, such that the voltage and frequency changes as devices are added or removed are likely to be much larger than in normal grid conditions. However, the difference is not so large as to prevent identification errors, and voltage and frequency shifts are generally used along with other signals.

The active analogue of voltage and frequency shift detection attempts to measure the overall impedance fed by the inverter. When the circuit is grid-connected, there is almost no voltage response to slight variations in inverter current; but an island will observe a change in voltage. In principle, this technique has a vanishingly small NDZ, but in practice the grid is not always an infinitely-stiff voltage source, especially if multiple inverters attempt to measure impedance simultaneously.

Unlike the shifts, a random circuit is highly unlikely to have a characteristic frequency matching standard grid power. However, many devices, like televisions, deliberately synchronize to the grid frequency. Motors, in particular, may be able to stabilize circuit frequency close to the grid standard as they "wind down".

At the utility level, protective relays designed to isolate a portion of the grid can also switch in high impedance components, such that an islanded distributed generator will necessarily overload and shut down. This practice, however, relies on the expensive widespread provision of high-impedance devices.

Alternatively, anti-islanding circuitry can rely on out-of-band signals. For example, utilities can send a shut-down signal through power line carrier communications or a telephony hookup.

### Inverter-specific techniques

Certain passive methods are uniquely viable with direct current generators (inverter-based resources), such as solar panels.

For example, inverters typically generate a phase shift when islanding. Inverters generally match the grid signal with a phase locked loop (PLL) that tracks zero-crossings. Between those events, the inverter produces a sinusoidal output, varying the current to produce the proper voltage waveform given the previous cycle's load. When the main grid disconnects, the power factor on the island suddenly decreases, and inverter's current no longer produces the proper waveform. By the time the waveform is completed and returns to zero, the signal will be out of phase. However, many common events, like motors starting, also cause phase jumps as new impedances are added to the circuit.

A more effective technique inverts the islanding phase shift: the inverter is designed to produce output slightly mis-aligned with the grid, with the expectation that the grid will overwhelm the signal. The phase-locked loop then becomes unstable when the grid signal is missing; the system drifts away from the design frequency; and the inverter shuts down.

A very secure islanding detection method searches for distinctive 2nd and 3rd harmonics generated by nonlinear interactions inside the inverter transformers. There are generally no other total harmonic distortion (THD) sources that match an inverter. Even noisy sources, like motors, do not effect measurable distortion on a grid-connected circuit, as the latter has essentially infinite filtration capacity. Switched-mode inverters generally have large distortions — as much as 5%. When the grid disconnects, the local circuit then exhibits inverter-induced distortion. Modern inverters attempt to minimize harmonic distortion, in some cases to unmeasurable limits, but in principle it is straightforward to design one which introduces a controlled amount of distortion to actively search for island formation.

## Distributed generation controversy

Utilities have refused to allow installation of home solar or other distributed generation systems, on the grounds that they may create uncontrolled grid islands. In Ontario, a 2009 modification to the feed-in tariff induced many rural customers to establish small (10 kW) systems under the "capacity exempt" microFIT. However, Hydro One then refused to connect the systems to the grid after construction.

The issue can be hotly political, in part because distributed generation proponents believe the islanding concern is largely pretextual. A 1999 test in the Netherlands was unable to find distributed-generation islands 60 seconds after grid collapse. Moreover, moments when distributed generation only matched distributed loads occurred at a rate comparable to 10−6 yr−1, and that the chance that the grid would disconnect at that point in time was even less, so that the "probability of encountering an islanding [*sic*] is virtually zero".

Unintentional islanding risk is primarily the case of synchronous generators, as in microhydro. A 2004 Canadian report concluded that "Anti-islanding technology for inverter based DG systems is much better developed, and published risk assessments suggest that the current technology and standards provide adequate protection."

Utilities generally argue that the distributed generators might effect the following problems:

**Safety concerns**

If an island forms, repair crews may be faced with unexpected live wires.

**End-user damage**

Distributed generators may not be able to maintain grid

frequencies

or

voltages

close to standard, and nonstandard currents can damage customer equipment. Depending on the circuit configuration, the utility may be liable for the damage.

**Controlled grid reconnection**

Reclosing distribution circuits onto an active island may damage equipment or be inhibited by

out-of-phase protection relays

. Procedures to prevent these outcomes may delay restoration of electric service to dropped customers.

The first two claims are disputed within the power industry. For example, normal linework constantly risks exposure to live wires, and standard procedures require explicit checks to ensure that a wire is dead before worker contact. Supervisory Control and Data Acquisition (SCADA) systems can be set to alarm if there is unexpected voltage on a purportedly-isolated line. A UK-based study concluded that "The risk of electric shock associated with islanding of PV systems under worst-case PV penetration scenarios to both network operators and customers is typically <10−9 per year." Likewise, damage to end-user devices is largely inhibited by modern island-detection systems.

It is, generally, the last problem that most concerns utilities. Reclosers are commonly used to divide up the grid into smaller sections that will automatically, and quickly, re-energize the branch as soon as the fault condition (a tree branch on lines for instance) clears. There is some concern that the reclosers may not re-energize in the case of an island or that an intervening loss of synchrony might damage distributed generators on the island. However, it is neither clear that reclosers are still useful in modern utility practice nor that breaker-reclosers must act on all phases.
