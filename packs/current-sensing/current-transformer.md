---
title: "Current transformer"
source: https://en.wikipedia.org/wiki/Current_transformer
domain: current-sensing
license: CC-BY-SA-4.0
tags: current sensor, current clamp, rogowski coil, current transformer
fetched: 2026-07-02
---

# Current transformer

A **current transformer** (**CT**) is a type of transformer that reduces or multiplies alternating current (AC), producing a current in its secondary which is proportional to the current in its primary.

Current transformers, along with voltage or potential transformers, are instrument transformers, which scale the large values of voltage or current to small, standardized values that are easy to handle for measuring instruments and protective relays. Instrument transformers isolate measurement or protection circuits from the high voltage of the primary system. A current transformer presents a negligible load to the primary circuit.

Current transformers are the current-sensing units of the power system and are used at generating stations, electrical substations, and in industrial and commercial electric power distribution.

## Function

A current transformer has a primary winding, a core, and a secondary winding, although some transformers use an air core. While the physical principles are the same, the details of a "current" transformer compared with a "voltage" transformer differ because of different requirements of the application. A current transformer is designed to maintain an accurate ratio between the currents in its primary and secondary circuits over a defined range.

The alternating current in the primary produces an alternating magnetic field in the core, which then induces an alternating current in the secondary. The primary circuit is largely unaffected by the insertion of the CT. Accurate current transformers need close coupling between the primary and secondary to ensure that the secondary current is proportional to the primary current over a wide current range. The current in the secondary is the current in the primary (assuming a single turn primary) divided by the number of turns of the secondary. In the illustration on the right, 'I' is the current in the primary, 'B' is the magnetic field, 'N' is the number of turns on the secondary, and 'A' is an AC ammeter.

Current transformers typically consist of a silicon steel ring core wound with many turns of copper wire, as shown in the illustration to the right. The conductor carrying the primary current is passed through the ring. The CT's primary, therefore, consists of a single 'turn'. The primary 'winding' may be a permanent part of the current transformer, i.e., a heavy copper bar to carry current through the core. Window-type (toroidal) current transformers are also common, which can have circuit cables run through the center of the core to provide a single-turn primary winding. To assist accuracy, the primary conductor should be centered in the aperture.

CTs are specified by their current ratio from primary to secondary. The rated secondary current is normally standardized at 1 or 5 amperes. For example, a 4000:5 CT secondary winding will supply an output current of 5 amperes when the primary winding current is 4000 amperes. This ratio can also be used to find the impedance or voltage on one side of the transformer, given the appropriate value at the other side. For the 4000:5 CT, the secondary impedance can be found as ZS = NZP = 800ZP, and the secondary voltage can be found as VS = NVP = 800VP. In some cases, the secondary impedance is *referred* to the primary side, and is found as ZS′ = N2ZP. Referring the impedance is done simply by multiplying initial secondary impedance value by the current ratio. The secondary winding of a CT can have taps to provide a range of ratios, five taps being common.

Current transformer shapes and sizes vary depending on the end-user or switch gear manufacturer. Low-voltage single ratio metering current transformers are either a ring type or plastic molded case.

Split-core current transformers either have a two-part core or a core with a removable section. This allows the transformer to be placed around a conductor without disconnecting it first. Split-core current transformers are typically used in low current measuring instruments, often portable, battery-operated, and hand-held (see illustration lower right).

## Use

Current transformers are used extensively for measuring current and monitoring the operation of the power grid. Along with voltage leads, revenue-grade CTs drive the electrical utility's watt-hour meter on many larger commercial and industrial supplies.

High-voltage current transformers are mounted on porcelain or polymer insulators to isolate them from ground. Some CT configurations slip around the bushing of a high-voltage transformer or circuit breaker, which automatically centers the conductor inside the CT window.

Current transformers can be mounted on the low voltage or high voltage leads of a power transformer. Sometimes a section of a bus bar can be removed to replace a current transformer.

Often, multiple CTs are installed as a "stack" for various uses. For example, protection devices and revenue metering may use separate CTs to provide isolation between metering and protection circuits and allows current transformers with different characteristics (accuracy, overload performance) to be used for the devices.

In the United States, the National Electrical Code (NEC) requires residual current devices in commercial and residential electrical systems to protect outlets installed in "wet" locations such as kitchens and bathrooms, as well as weatherproof outlets installed outdoors. Such devices, most commonly **ground fault circuit interrupters** (GFCIs), typically run both the 120-volt energized conductor and the neutral return conductor through a current transformer, with the secondary coil connected to a trip device.

Under normal conditions, the current in the two circuit wires will be equal and flow in opposite directions, resulting in zero net current through the CT and no current in the secondary coil. If the supply current is redirected downstream into the third (ground) circuit conductor (e.g., if the grounded metallic case of a power tool contacts a 120-volt conductor), or into earth ground (e.g., if a person contacts a 120-volt conductor), the neutral return current will be less than the supply current, resulting in a positive net current flow through the CT. This net current flow will induce current in the secondary coil, which will cause the trip device to operate and de-energize the circuit - typically within 0.2 seconds.

The burden (load) impedance should not exceed the specified maximum value to avoid the secondary voltage exceeding the limits for the current transformer. The primary current rating of a current transformer should not be exceeded, or the core may enter its non-linear region and ultimately saturate. This would occur near the end of the first half of each half (positive and negative) of the AC sine wave in the primary and compromise accuracy.

## Safety

Current transformers are often used to monitor high currents or currents at high voltages. Technical standards and design practices are used to ensure the safety of installations using current transformers.

The secondary of a current transformer should not be disconnected from its burden while current is in the primary, as the secondary will attempt to continue driving current into an effective infinite impedance potentially generating high voltages and thus compromising operator safety. For certain current transformers, this voltage may reach several kilovolts and may cause arcing. Exceeding the secondary voltage may also degrade the accuracy of the transformer or destroy it. Output voltage is limited by core saturation since the primary flux is not canceled by secondary flux when the core is saturated. Because of this, smaller current transformers may not actually incur dangerous voltages when operating nominally. Faster current transients from loads being switched on etc. can however still induce dangerous voltage levels due to high current slope.

## Accuracy

The accuracy of a CT is affected by a number of factors including:

- Burden
- Burden class/saturation class
- Rating factor
- Load
- External electromagnetic fields
- Temperature
- Physical configuration
- The selected tap, for multi-ratio CTs
- Phase change
- Capacitive coupling between primary and secondary
- Resistance of primary and secondary
- Core magnetizing current

Accuracy classes for various types of measurement and at standard loads in the secondary circuit (burdens) are defined in IEC 61869-1 as classes 0.1, 0.2s, 0.2, 0.5, 0.5s, 1 and 3. The class designation is an approximate measure of the CT's accuracy. The ratio (primary to secondary current) error of a Class 1 CT is 1% at rated current; the ratio error of a Class 0.5 CT is 0.5% or less. Errors in phase are also important, especially in power measuring circuits. Each class has an allowable maximum phase error for a specified load impedance.

Current transformers used for protective relaying also have accuracy requirements at overload currents in excess of the normal rating to ensure accurate performance of relays during system faults. A CT with a rating of 2.5L400 specifies with an output from its secondary winding of twenty times its rated secondary current (usually 5 A × 20 = 100 A) and 400 V (IZ drop) its output accuracy will be within 2.5 percent.

### Burden

The secondary load of a current transformer is termed the "burden" to distinguish it from the primary load.

The burden in a CT metering electrical network is largely resistive impedance presented to its secondary winding. Typical burden ratings for IEC CTs are 1.5 VA, 3 VA, 5 VA, 10 VA, 15 VA, 20 VA, 30 VA, 45 VA and 60 VA. ANSI/IEEE burden ratings are B-0.1, B-0.2, B-0.5, B-1.0, B-2.0 and B-4.0. This means a CT with a burden rating of B-0.2 will maintain its stated accuracy with up to 0.2 Ω on the secondary circuit. These specification diagrams show accuracy parallelograms on a grid incorporating magnitude and phase angle error scales at the CT's rated burden. Items that contribute to the burden of a current measurement circuit are switch-blocks, meters and intermediate conductors. The most common cause of excess burden impedance is the conductor between the meter and the CT. When substation meters are located far from the meter cabinets, the excessive length of cable creates a large resistance. This problem can be reduced by using thicker cables and CTs with lower secondary currents (1 A), both of which will produce less voltage drop between the CT and its metering devices.

### Knee-point core-saturation voltage

The **knee-point voltage** of a current transformer is the magnitude of the secondary voltage above which the output current ceases to linearly follow the input current within declared accuracy. In testing, if a voltage is applied across the secondary terminals the magnetizing current will increase in proportion to the applied voltage, until the knee point is reached. The knee point is defined as the voltage at which a 10% increase in applied voltage increases the magnetizing current by 50%. For voltages greater than the knee point, the magnetizing current increases considerably even for small increments in voltage across the secondary terminals. The knee-point voltage is less applicable for metering current transformers as their accuracy is generally much higher but constrained within a very small range of the current transformer rating, typically 1.2 to 1.5 times rated current. However, the concept of knee point voltage is very pertinent to protection current transformers, since they are necessarily exposed to fault currents of 20 to 30 times rated current.

### Phase shift

Ideally, the primary and secondary currents of a current transformer should be in phase. In practice, this is impossible, but, at normal power frequencies, phase shifts of a few tenths of a degree are achievable, while simpler CTs may have larger phase shifts. For current measurement, phase shift is immaterial as ammeters only display the magnitude of the current. However, in wattmeters, energy meters, and power factor, phase shift produces errors. For power and energy measurement, the errors are considered to be negligible at unity power factor but become more significant as the power factor approaches zero. The introduction of electronic power and energy meters has allowed current phase error to be calibrated out.

## Construction

Bar-type current transformers have terminals for source and load connections of the primary circuit, and the body of the current transformer provides insulation between the primary circuit and ground. By use of oil insulation and porcelain bushings, such transformers can be applied at the highest transmission voltages.

Ring-type current transformers are installed over a bus bar or an insulated cable and have only a low level of insulation on the secondary coil. To obtain non-standard ratios or for other special purposes, more than one turn of the primary cable may be passed through the ring. Where a metal shield is present in the cable jacket, it must be terminated so no net sheath current passes through the ring, to ensure accuracy. Current transformers used to sense ground fault (zero sequence) currents, such as in a three-phase installation, may have three primary conductors passed through the ring. Only the net unbalanced current produces a secondary current - this can be used to detect a fault from an energized conductor to ground. Ring-type transformers usually use dry insulation systems, with a hard rubber or plastic case over the secondary windings.

For temporary connections, a split ring-type current transformer can be slipped over a cable without disconnecting it. This type has a laminated iron core, with a hinged section that allows it to be installed over the cable; the core links the magnetic flux produced by the single turn primary winding to a wound secondary with many turns. Because the gaps in the hinged segment introduce inaccuracy, such devices are not normally used for revenue metering.

Current transformers, especially those intended for high voltage substation service, may have multiple taps on their secondary windings, providing several ratios in the same device. This can be done to allow for reduced inventory of spare units, or to allow for load growth in an installation. A high-voltage current transformer may have several secondary windings with the same primary, to allow for separate metering and protection circuits, or for connection to different types of protective devices. For example, one secondary may be used for branch overcurrent protection, while a second winding may be used in a bus differential protective scheme, and a third winding used for power and current measurement.

## Special types

Specially constructed *wideband current transformers* are also used (usually with an oscilloscope) to measure waveforms of high frequency or pulsed currents within pulsed power systems. Unlike CTs used for power circuitry, wideband CTs are rated in output volts per ampere of primary current.

If the burden resistance is much less than inductive impedance of the secondary winding at the measurement frequency then the current in the secondary tracks the primary current and the transformer provides a current output that is proportional to the measured current. On the other hand, if that condition is not true, then the transformer is inductive and gives a differential output. The Rogowski coil uses this effect and requires an external integrator in order to provide a voltage output that is proportional to the measured current.

## Standards

Ultimately, depending on client requirements, there are two main standards to which current transformers are designed. IEC 61869-1 (in the past IEC 60044-1) & IEEE C57.13 (ANSI), although the Canadian and Australian standards are also recognised.

## High voltage types

Current transformers are used for protection, measurement and control in high-voltage electrical substations and the electrical grid. Current transformers may be installed inside switchgear or in apparatus bushings, but very often free-standing outdoor current transformers are used. In a switchyard, *live tank* current transformers have a substantial part of their enclosure energized at the line voltage and must be mounted on insulators. *Dead tank* current transformers isolate the measured circuit from the enclosure. Live tank CTs are useful because the primary conductor is short, which gives better stability and a higher short-circuit current rating. The primary of the winding can be evenly distributed around the magnetic core, which gives better performance for overloads and transients. Since the major insulation of a live-tank current transformer is not exposed to the heat of the primary conductors, insulation life and thermal stability is improved.

A high-voltage current transformer may contain several cores, each with a secondary winding, for different purposes (such as metering circuits, control, or protection). A neutral current transformer is used as earth fault protection to measure any fault current flowing through the neutral line from the wye neutral point of a transformer.
