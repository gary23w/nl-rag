---
title: "Redundancy (engineering)"
source: https://en.wikipedia.org/wiki/Redundancy_(engineering)
domain: lockstep-cores
license: CC-BY-SA-4.0
tags: lockstep cores, dual-core lockstep, triple modular redundancy, dual modular redundancy
fetched: 2026-07-02
---

# Redundancy (engineering)

In engineering and systems theory, **redundancy** is the intentional duplication of critical components or functions of a system with the goal of increasing reliability of the system, usually in the form of a backup or fail-safe, or to improve actual system performance, such as in the case of GNSS receivers, or multi-threaded computer processing.

In many safety-critical systems, such as fly-by-wire and hydraulic systems in aircraft, some parts of the control system may be triplicated, which is formally termed triple modular redundancy (TMR). An error in one component may then be out-voted by the other two. In a triply redundant system, the system has three sub components, all three of which must fail before the system fails. Since each one rarely fails, and the sub components are designed to preclude common failure modes (which can then be modelled as independent failure), the probability of all three failing is calculated to be extraordinarily small; it is often outweighed by other risk factors, such as human error. Electrical surges arising from lightning strikes are an example of a failure mode which is difficult to fully isolate, unless the components are powered from independent power busses and have no direct electrical pathway in their interconnect (communication by some means is required for voting). Redundancy may also be known by the terms "majority voting systems" or "voting logic".

Redundancy sometimes produces less, instead of greater reliability – it creates a more complex system which is prone to various issues, it may lead to human neglect of duty, and may lead to higher production demands which by overstressing the system may make it less safe.

Redundancy is one form of robustness as practiced in computer science.

**Geographic redundancy** has become important in the data center industry, to safeguard data against natural disasters and political instability (see below).

## Forms of redundancy

In computer science, there are four major forms of redundancy:

- Hardware redundancy, such as dual modular redundancy and triple modular redundancy
- Information redundancy, such as error detection and correction methods
- Time redundancy, performing the same operation multiple times such as multiple executions of a program or multiple copies of data transmitted
- Software redundancy such as N-version programming

A modified form of software redundancy, applied to hardware may be:

- Distinct functional redundancy, such as both mechanical and hydraulic braking in a car. Applied in the case of software, code written independently and distinctly different but producing the same results for the same inputs.

Structures are usually designed with redundant parts as well, ensuring that if one part fails, the entire structure will not collapse. A structure without redundancy is called fracture-critical, meaning that a single broken component can cause the collapse of the entire structure. Bridges that failed due to lack of redundancy include the Silver Bridge and the Interstate 5 bridge over the Skagit River.

Parallel and combined systems demonstrate different level of redundancy. The models are subject of studies in reliability and safety engineering.

### Dissimilar redundancy

Unlike traditional redundancy, which uses more than one of the same thing, dissimilar redundancy uses different things. The idea is that the different things are unlikely to contain identical flaws. The voting method may involve additional complexity if the two things take different amounts of time. Dissimilar redundancy is often used with software, because identical software contains identical flaws.

The chance of failure is reduced by using at least two different types of each of the following

- processors,
- operating systems,
- software,
- sensors,
- types of actuators (electric, hydraulic, pneumatic, manual mechanical, etc.)
- communications protocols,
- communications hardware,
- communications networks,
- communications paths

### Geographic redundancy

Geographic redundancy corrects the vulnerabilities of redundant devices deployed by geographically separating backup devices. Geographic redundancy reduces the likelihood of events such as power outages, floods, HVAC failures, lightning strikes, tornadoes, building fires, wildfires, and mass shootings disabling most of the system if not the entirety of it.

Geographic redundancy locations can be

- more than 621 miles (999 km) continental,
- more than 62 miles apart and less than 93 miles (150 km) apart,
- less than 62 miles apart, but not on the same campus, or
- different buildings that are more than 300 feet (91 m) apart on the same campus.

The following methods can reduce the risks of damage by a fire conflagration:

- large buildings at least 80 feet (24 m) to 110 feet (34 m) apart, but sometimes a minimum of 210 feet (64 m) apart.
- high-rise buildings at least 82 feet (25 m) apart
- open spaces clear of flammable vegetation within 200 feet (61 m) on each side of objects
- different wings on the same building, in rooms that are separated by more than 300 feet (91 m)
- different floors on the same wing of a building in rooms that are horizontally offset by a minimum of 70 feet (21 m) with fire walls between the rooms that are on different floors
- two rooms separated by another room, leaving at least a 70-foot gap between the two rooms
- there should be a minimum of two separated fire walls and on opposite sides of a corridor

Geographic redundancy is used by Amazon Web Services (AWS), Google Cloud Platform (GCP), Microsoft Azure, Netflix, Dropbox, Salesforce, LinkedIn, PayPal, Twitter, Facebook, Apple iCloud, Cisco Meraki, and many others to provide geographic redundancy, high availability, fault tolerance and to ensure availability and reliability for their cloud services.

As another example, to minimize risk of damage from severe windstorms or water damage, buildings can be located at least 2 miles (3.2 km) away from the shore, with an elevation of at least 5 feet (1.5 m) above sea level. For additional protection, they can be located at least 100 feet (30 m) away from flood plain areas.

## Functions of redundancy

The two functions of redundancy are passive redundancy and active redundancy. Both functions prevent performance decline from exceeding specification limits without human intervention using extra capacity.

Passive redundancy uses excess capacity to reduce the impact of component failures. One common form of passive redundancy is the extra strength of cabling and struts used in bridges. This extra strength allows some structural components to fail without bridge collapse. The extra strength used in the design is called the margin of safety.

Eyes and ears provide working examples of passive redundancy. Vision loss in one eye does not cause blindness but depth perception is impaired. Hearing loss in one ear does not cause deafness but directionality is lost. Performance decline is commonly associated with passive redundancy when a limited number of failures occur.

Active redundancy eliminates performance declines by monitoring the performance of individual devices, and this monitoring is used in voting logic. The voting logic is linked to switching that automatically reconfigures the components. Error detection and correction and the Global Positioning System (GPS) are two examples of active redundancy.

Electrical power distribution provides an example of active redundancy. Several power lines connect each generation facility with customers. Each power line includes monitors that detect overload. Each power line also includes circuit breakers. The combination of power lines provides excess capacity. Circuit breakers disconnect a power line when monitors detect an overload. Power is redistributed across the remaining lines. At the Toronto Airport, there are 4 redundant electrical lines. Each of the 4 lines supply enough power for the entire airport. A spot network substation uses reverse current relays to open breakers to lines that fail, but lets power continue to flow the airport.

Electrical power systems use power scheduling to reconfigure active redundancy. Computing systems adjust the production output of each generating facility when other generating facilities are suddenly lost. This prevents blackout conditions during major events such as an earthquake.

## Disadvantages

Charles Perrow, author of *Normal Accidents*, has said that sometimes redundancies backfire and produce less, not more reliability. This may happen in three ways: First, redundant safety devices result in a more complex system, more prone to errors and accidents. Second, redundancy may lead to shirking of responsibility among workers. Third, redundancy may lead to increased production pressures, resulting in a system that operates at higher speeds, but less safely.

## Voting logic

Voting logic uses performance monitoring to determine how to reconfigure individual components so that operation continues without violating specification limitations of the overall system. Voting logic often involves computers, but systems composed of items other than computers may be reconfigured using voting logic. Circuit breakers are an example of a form of non-computer voting logic.

The simplest voting logic in computing systems involves two components: primary and alternate. They both run similar software, but the output from the alternate remains inactive during normal operation. The primary monitors itself and periodically sends an activity message to the alternate as long as everything is OK. All outputs from the primary stop, including the activity message, when the primary detects a fault. The alternate activates its output and takes over from the primary after a brief delay when the activity message ceases. Errors in voting logic can cause both outputs to be active or inactive at the same time, or cause outputs to flutter on and off.

A more reliable form of voting logic involves an odd number of three devices or more. All perform identical functions and the outputs are compared by the voting logic. The voting logic establishes a majority when there is a disagreement, and the majority will act to deactivate the output from other device(s) that disagree. A single fault will not interrupt normal operation. This technique is used with avionics systems, such as those responsible for operation of the Space Shuttle.

## Calculating the probability of system failure

Each duplicate component added to the system decreases the probability of system failure according to the formula:-

${p}=\prod _{i=1}^{n}p_{i}$

where:

- n – number of components
- $p_{i}$ – probability of component i failing
- p – the probability of all components failing (system failure)

This formula assumes independence of failure events. That means that the probability of a component B failing given that a component A has already failed is the same as that of B failing when A has not failed. There are situations where this is unreasonable, such as using two power supplies connected to the same socket in such a way that if one power supply failed, the other would too.

It also assumes that only one component is needed to keep the system running.

## Redundancy and high availability

You can achieve higher availability through redundancy. Let's say you have three redundant components: A, B and C. You can use following formula to calculate availability of the overall system:

Availability of redundant components = 1 - (1 - availability of component A) X (1 - availability of component B) X (1 - availability of component C)

In corollary, if you have N parallel components each having X availability, then:

Availability of parallel components = 1 - (1 - X)^ N

Using redundant components can exponentially increase the availability of overall system. For example if each of your hosts has only 50% availability, by using 10 of hosts in parallel, you can achieve 99.9023% availability.

Note that redundancy doesn't always lead to higher availability. In fact, redundancy increases complexity which in turn reduces availability. According to Marc Brooker, to take advantage of redundancy, ensure that:

1. You achieve a net-positive improvement in the overall availability of your system
2. Your redundant components fail independently
3. Your system can reliably detect healthy redundant components
4. Your system can reliably scale out and scale-in redundant components.
