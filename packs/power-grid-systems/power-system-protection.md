---
title: "Power system protection"
source: https://en.wikipedia.org/wiki/Power-system_protection
domain: power-grid-systems
license: CC-BY-SA-4.0
tags: electrical grid, power transmission, power distribution, power-system protection
fetched: 2026-07-02
---

# Power system protection

(Redirected from

Power-system protection

)

**Power system protection** is a set of techniques and power grid equipment used to limit the damage caused by an electrical fault and safeguard other components of the grid, like generators and transmission lines. The term is also used for a branch of electrical power engineering that deals with the protection. There is an overlap between the power system protection and power system operations, as the protection equipment, like other switchgear, can be used for operations.

The **protection devices** are used to protect the power systems from faults by detecting the faults and taking *action* ("**tripping**"). P. M. Anderson distinguishes the *reactionary devices*, like protective relays, that "clear" a fault by isolating it from the rest of system and *safeguard devices* that address the source of the hazard (for example, an emergency core cooling system of a nuclear reactor). As a discipline, power system protection mostly deals with the reactionary devices.

## Protection devices

Power system protection relies on few basic elements:

- a sensor performs a measurement (test) of a value (for example, of electric current in a transmission line);
- a comparator checks the test result against a *threshold* that the result is not supposed to cross during normal operation (for example, the maximum acceptable current value when testing for the overcurrent condition). Ability to identify an abnormal condition is called *sensitivity*;
- a timing element (*delay*) that checks for the persistence of the condition (for example, if a fault had been cleared by another protection device with a smaller delay setting, this device should not take any action);
- action element (typically circuit-opening).

Protective devices include, under a common label of "switchgear":

- fuses are the simplest protection devices combining overcurrent sensing, delay, and action in a single circuit-opening fusible part;
- protective relays sense the fault and initiate a trip, or disconnection, command;
- power circuit breakers use commands from relays and autoreclosers to open/close the electric circuit. The breakers for the protective system are safe to open under a fault current;
- reclosers and sectionalizers.

Connecting the protective devices to the grid usually involves additional hardware:

- instrument transformers, both current and voltage, are used to isolate the (mostly low-voltage) devices from the transmission levels;
- electric batteries (with chargers) ensure operation in case of power outage;
- data communications to obtain the current and voltage at remote terminals of a line and to allow remote tripping of equipment.

With the exception of the breaker, the components of the protective device are frequently deployed in a redundant fashion.

## Protective zones

The objective of a protection scheme is to keep the power system stable by isolating only the components that are under fault, whilst leaving as much of the network as possible in operation, thus minimizing the loss of load. This property of the protection system is called *selectivity*. To achieve selectivity, the power system is subdivided into *protective zones*, each containing a power system component (generator, bus, transformer, transmission or distribution line, motor) that should be protected. Each zone has its own protection device(s) and provides sensitivity to faults within its boundaries. If a fault were to occur in a given zone, necessary actions will be executed to isolate that zone from the entire system (all circuit breakers in a given zone with a fault will open in order to isolate the fault). The boundaries of zones overlap to leave no part of grid without protection, overlapped regions usually surround circuit breakers with two sets of instrument transformers and relays for each circuit breaker. The overlapping regions of sensitivity have a drawback of multiple relays possibly tripping when the fault is in the overlapped area. For example, unless special arrangements are made, a short circuit above the relay A, but still within the blue zone on the diagram, might cause overcurrent conditions in relays A, C, and D and cause them to trip, with the two latter trips being redundant. This can be avoided by using specialized relays (distance or directional ones) or by coordinating the relay actions using a communication channel ("pilot"). In any case, overlapped regions are designed to be as small as possible such that when a fault occurs in an overlap region and the two zones which encompass the fault are isolated, the sector of the power system.

### Backup

The power protection system needs to be resilient to its own malfunctions. Thus it includes backup protection devices. For example if the fault is in the top left red zone, but outside the blue zone, it is expected to be handled by the "primary" relay A. If the relay A malfunctions and cannot clear the fault, the *backup relays* C and D in the adjacent (blue) zone will trip. This can be arranged without coordination (for example, the delay setting of C and D can be higher so they do not act if A succeeds in clearing the fault) or through coordination via a pilot. The term *local backup* is used when the backup relays are within the same zone as the "primary" one being duplicated.

Local back-up protection, like the primary protective device, will isolate the elements of the plant affected by the fault to clear the latter. Adjacent-zone ("remote") back-up protection will generally isolate both the affected and unaffected items of plant to clear the fault.

## Fault types

The faults can be classified by their level of permanence that affects the possibility of autoreclosing:

- a *transient fault* clears quickly once the line is opened (for example, a flashover over an insulator on the transmission tower caused by lightning). A quick reclosing with not cause the fault to reappear. The transient faults represent the vast majority of faults on the overhead transmission lines;
- a *semipermanent fault*, like tree contact, are faults that might clear themselves if allowed to burn for a short time (a tree branch might burn away). Semipermanent faults occur more frequently in the subtransmission lines and electric distribution;
- a *permanent fault* must be repaired. Almost all the faults on the underground power cable are permanent.

Many pieces of the grid equipment can develop internal problems. For these devices, the faults can be classified into *internal* and *external*. As an example of the internal fault, a transformer might develop overpressure inside its containment vessel with the root cause (for example, local overheating) not triggering any other alarms. For the same transformer, an overload condition would represent an external fault.

## Relay types

The relays can be classified by their sensitivity to the location of a fault:

- a *nondirectional* relay does not provide an information on which side of it the fault is located, this is the simplest form of the overcurrent relay. For example, in a radial system of electrical power distribution, the current always flows to the load spokes, so there is no need to sense its direction, as an overcurrent condition always indicates a short circuit on the load side;
- a directional relay compares the current phase with the reference and performs action only if the direction to the fault matches the selected one;
- a differential relay compares the values of electrical measurements on the input and output of a protected device. For example, in an electrical transformer, input and output voltage and current values are related through the transformer ratio, and large deviations from this constant indicate a fault;
- a distance relay determines the distance of the fault by calculating the line electrical impedance as seen by the relay based on observe current, voltage, and the phase difference between them. The knowledge of distance can be used to prevent tripping when the fault is in the wrong zone;
- a **pilot protection** relay senses the conditions on the other end of the line through a communication channel (wire pilot, carrier pilot, microwave pilot, and fiber-optic pilot).

In the 21st century a lot of testing for abnormal conditions is performed by multifunctional numerical relays that use computers for calculations. Individual measurements use cryptic identifiers from the ANSI device numbers list, like "50" for the "Instantaneous Overcurrent Relay" or "87L" for the "Segregated Line Current Differential".

Historically, the power industry went through multiple generations of sensors and comparators, retaining the terminology and some of the devices:

- *electromechanical relays* are the simplest devices used for protection since the early days of electrical power industry. For example, an *induction disk overcurrent relay* is an overcurrent relay that uses an induction disk as a sensor and timing element;
- *electronic relays*, with comparators and level detectors were introduced slowly over a long period of time starting in the 1930s. The process accelerated with the arrival of transistor in 1950s.
- *digital relays* were proposed in 1969, but became widespread only with the introduction of microprocessor in the early 1970s.

## Types of protection

### Transmission protection

High-voltage transmission lines typically form a mesh-like grid, so the current might be flowing into the fault from either direction, making the non-directional relays mostly unsuitable for protection, so the distance and pilot relays are typically used. The use of directional relays is not always possible.

#### Ground fault

In a grounded neutral transmission line, the phase relays might detect and clear a ground fault. However, since almost all faults on high-voltage lines are of the one-phase-to-ground variety, specialized ground relays are used for quick reaction. These relay utilize the zero-sequence current for detection. During the normal operation, the zero-sequence current is very small, so a high current value that depends on the network configuration, not on the (varying) load, is a convenient and reliable indicator of a ground fault.

### Generators

Generators are expensive and complex pieces of the grid equipment, thus the larger machines use tens of types of protection devices. Practically every generator has the stator protection, usually using differential relays. The internal failures of generators are unusual, so the protective relays trips are very rare.

### Transformers

Not only the transformers are expensive, but it might take a long time to replace a failed large transformer. Electrical protection of a transformer mostly uses the differential relays. This protection can be combined with the one of the busbar or generator.

### Low-voltage networks

The low-voltage network generally relies upon fuses or low-voltage circuit breakers to remove both overload and earth faults.

## Disturbance-monitoring equipment

Disturbance-monitoring equipment (DME) monitors and records system data pertaining to a fault. DME accomplish three main purposes:

- model validation,
- disturbance investigation, and
- assessment of system protection performance.

DME devices include:

- Sequence of event recorders, which record equipment response to the event
- Fault recorders, which record actual waveform data of the system primary voltages and currents
- Dynamic disturbance recorders (DDRs), which record incidents that portray power system behavior during dynamic events such as low frequency (0.1 Hz – 3 Hz) oscillations and abnormal frequency or voltage excursions

## Performance measures

Protection engineers define dependability as the tendency of the protection system to operate correctly for in-zone faults. They define security as the tendency not to operate for out-of-zone faults. Both dependability and security are reliability issues. Fault tree analysis is one tool with which a protection engineer can compare the relative reliability of proposed protection schemes. Quantifying protection reliability is important for making the best decisions on improving a protection system, managing dependability versus security tradeoffs, and getting the best results for the least money. A quantitative understanding is essential in the competitive utility industry.

- Reliability: Devices must function consistently when fault conditions occur, regardless of possibly being idle for months or years. Without this reliability, systems may cause costly damages.
- Selectivity: Devices must avoid unwarranted, false trips.
- Speed: Devices must function quickly to reduce equipment damage and fault duration, with only very precise intentional time delays.
- Sensitivity: Devices must detect even the smallest value of faults and respond.
- Economy: Devices must provide maximum protection at minimum cost.
- Simplicity: Devices must minimize protection circuitry and equipment.

**Reliability: Dependability vs Security**

There are two aspects of reliable operation of protection systems: dependability and security. Dependability is the ability of the protection system to operate when called upon to remove a faulted element from the power system. Security is the ability of the protection system to restrain itself from operating during an external fault. Choosing the appropriate balance between security and dependability in designing the protection system requires engineering judgement and varies on a case-by-case basis.
