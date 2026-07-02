---
title: "High availability"
source: https://en.wikipedia.org/wiki/High_availability
domain: gcp-cloud-sql
license: CC-BY-SA-4.0
tags: gcp cloud sql, managed relational database gcp, mysql postgres gcp, database service google
fetched: 2026-07-02
---

# High availability

**High availability** (**HA**) is a characteristic of a system that aims to ensure an agreed level of operational performance, usually uptime, for a higher than normal period.

There is now more dependence on these systems as a result of modernization. For example, to carry out their regular daily tasks, hospitals and data centers need their systems to be highly available. Availability refers to the ability of the user to access a service or system, whether to submit new work, update or modify existing work, or retrieve the results of previous work. If a user cannot access the system, it is considered *unavailable from the user's perspective*. The term *downtime* is generally used to refer to describe periods when a system is unavailable.

## Resilience

High availability is a property of network **resilience**, the ability to "provide and maintain an acceptable level of service in the face of faults and challenges to normal operation." Threats and challenges for services can range from simple misconfiguration over large scale natural disasters to targeted attacks. As such, network resilience touches a very wide range of topics. In order to increase the resilience of a given communication network, the probable challenges and risks have to be identified and appropriate resilience metrics have to be defined for the service to be protected.

The importance of network resilience is continuously increasing, as communication networks are becoming a fundamental component in the operation of critical infrastructures. Consequently, recent efforts focus on interpreting and improving network and computing resilience with applications to critical infrastructures. As an example, one can consider as a resilience objective the provisioning of services over the network, instead of the services of the network itself. This may require coordinated response from both the network and from the services running on top of the network.

These services include:

- supporting distributed processing
- supporting network storage
- maintaining service of communication services such as
  - video conferencing
  - instant messaging
  - online collaboration
- access to applications and data as needed

Resilience and survivability are interchangeably used according to the specific context of a given study.

## Principles

There are three principles of systems design in reliability engineering that can help achieve high availability.

1. Elimination of single points of failure. This means adding or building redundancy into the system so that failure of a component does not mean failure of the entire system.
2. Reliable crossover. In redundant systems, the crossover point itself tends to become a single point of failure. Reliable systems must provide for reliable crossover.
3. Detection of failures as they occur. If the two principles above are observed, then a user may never see a failure – but the maintenance activity must.

## Scheduled and unscheduled downtime

A distinction can be made between scheduled and unscheduled downtime. Typically, scheduled downtime is a result of maintenance that is disruptive to system operation and usually cannot be avoided with a currently installed system design. Scheduled downtime events might include patches to system software that require a reboot or system configuration changes that only take effect upon a reboot. In general, scheduled downtime is usually the result of some logical, management-initiated event. Unscheduled downtime events typically arise from some physical event, such as a hardware or software failure or environmental anomaly. Examples of unscheduled downtime events include power outages, failed CPU or RAM components (or possibly other failed hardware components), an over-temperature related shutdown, logically or physically severed network connections, security breaches, or various application, middleware, and operating system failures.

If users can be warned away from scheduled downtimes, then the distinction is useful. But if the requirement is for true high availability, then downtime is downtime whether or not it is scheduled.

Many computing sites exclude scheduled downtime from availability calculations, assuming that it has little or no impact upon the computing user community. By doing this, they can claim to have phenomenally high availability, which might give the illusion of continuous availability. Systems that exhibit truly continuous availability are comparatively rare and higher priced, and most have carefully implemented specialty designs that eliminate any single point of failure and allow online hardware, network, operating system, middleware, and application upgrades, patches, and replacements. For certain systems, scheduled downtime does not matter, for example, system downtime at an office building after everybody has gone home for the night.

## Percentage calculation

Availability is usually expressed as a percentage of uptime in a given year. The following table shows the downtime that will be allowed for a particular percentage of availability, presuming that the system is required to operate continuously. Service level agreements often refer to monthly downtime or availability in order to calculate service credits to match monthly billing cycles. The following table shows the translation from a given availability percentage to the corresponding amount of time a system would be unavailable. Availability is often quoted in terms of "nines", with 90% availability being called "one nine", 99% "two nines", 99.9% "three nines" and so on. As the number of nines gets larger, the availability targets get exponentially more stringent.

Reliability levels of more than nine nines are rare, and typically only achieved by distributed networks of redundant systems, and even then largely only in theory since it is effectively impossible to measure such low levels of downtime in any reasonable period; even a single second of system-wide downtime in 30 years (say, through an unanticipated common-mode software error) would be sufficient to dethrone an 11-nines system to nine nines of availability.

| Nines | Availability % | Downtime per year | Downtime per month | Downtime per week | Downtime per day |
|---|---|---|---|---|---|
| 1 | 90% | 37 days | 73 hours | 17 hours | 2.4 hours |
| 2 | 99% | 3.7 days | 7.3 hours | 1.7 hours | 14 minutes |
| 3 | 99.9% | 9 hours | 44 minutes | 10 minutes | 1.4 minutes |
| 4 | 99.99% | 53 minutes | 4.4 minutes | 1 minute | 8.6 s |
| 5 | 99.999% | 5.3 minutes | 26 s | 6 s | 860 ms |
| 6 | 99.9999% | 32 s | 2.6 s | 600 ms | 86 ms |
| 7 | 99.99999% | 3.2 s | 260 ms | 60 ms | 8.6 ms |
| 8 | 99.999999% | 320 ms | 26 ms | 6 ms | 860 μs |
| 9 | 99.9999999% | 32 ms | 2.6 ms | 600 μs | 86 μs |
| 10 | 99.99999999% | 3.2 ms | 260 μs | 60 μs | 8.6 μs |

The terms uptime and availability are often used interchangeably but do not always refer to the same thing. For example, a system can be "up" with its services not "available" in the case of a network outage. Or a system undergoing software maintenance can be "available" to be worked on by a system administrator, but its services do not appear "up" to the end user or customer. The subject of the terms is thus important here: whether the focus of a discussion is the server hardware, server OS, functional service, software service/process, or similar, it is only if there is a single, consistent subject of the discussion that the words uptime and availability can be used synonymously.

### Five-by-five mnemonic

A simple mnemonic rule states that *5 nines* allows approximately 5 minutes of downtime per year. Variants can be derived by multiplying or dividing by 10: 4 nines is 50 minutes and 3 nines is 500 minutes. In the opposite direction, 6 nines is 0.5 minutes (30 sec) and 7 nines is 3 seconds.

### "Powers of 10" trick

Another memory trick to calculate the allowed downtime duration for an " n -nines" availability percentage is to use the formula $8.64\times 10^{4-n}$ seconds per day.

For example, 90% ("one nine") yields the exponent $4-1=3$ , and therefore the allowed downtime is $8.64\times 10^{3}$ seconds per day.

Also, 99.999% ("five nines") gives the exponent $4-5=-1$ , and therefore the allowed downtime is $8.64\times 10^{-1}$ seconds per day.

### "Nines"

Percentages of a particular order of magnitude are sometimes referred to by the number of nines or "class of nines" in the digits. For example, electricity that is delivered without interruptions (blackouts, brownouts or surges) 99.999% of the time would have 5 nines reliability, or class five. In particular, the term is used in connection with mainframes or enterprise computing, often as part of a service-level agreement.

Similarly, percentages ending in a 5 have conventional names, traditionally the number of nines, then "five", so 99.95% is "three nines five", abbreviated 3N5. This is casually referred to as "three and a half nines", but this is incorrect: a 5 is only a factor of 2, while a 9 is a factor of 10, so a 5 is 0.3 nines (per below formula: $\log _{10}2\approx 0.3$ ): 99.95% availability is 3.3 nines, not 3.5 nines. More simply, going from 99.9% availability to 99.95% availability is a factor of 2 (0.1% to 0.05% unavailability), but going from 99.95% to 99.99% availability is a factor of 5 (0.05% to 0.01% unavailability), over twice as much.

A formulation of the *class of 9s* c based on a system's unavailability x would be

$c:=\lfloor -\log _{10}x\rfloor$

(cf. Floor and ceiling functions).

A similar measurement is sometimes used to describe the purity of substances.

In general, the number of nines is not often used by a network engineer when modeling and measuring availability because it is hard to apply in formula. More often, the unavailability expressed as a probability (like 0.00001), or a downtime per year is quoted. Availability specified as a number of nines is often seen in marketing documents. The use of the "nines" has been called into question, since it does not appropriately reflect that the impact of unavailability varies with its time of occurrence. For large amounts of 9s, the "unavailability" index (measure of downtime rather than uptime) is easier to handle. For example, this is why an "unavailability" rather than availability metric is used in hard disk or data link bit error rates.

Sometimes the humorous term "nine fives" (55.5555555%) is used to contrast with "five nines" (99.999%), though this is not an actual goal, but rather a sarcastic reference to something totally failing to meet any reasonable target.

## Measurement and interpretation

Availability measurement is subject to some degree of interpretation. A system that has been up for 365 days in a non-leap year might have been eclipsed by a network failure that lasted for 9 hours during a peak usage period; the user community will see the system as unavailable, whereas the system administrator will claim 100% uptime. However, given the true definition of availability, the system will be approximately 99.9% available, or three nines (8751 hours of available time out of 8760 hours per non-leap year). Also, systems experiencing performance problems are often deemed partially or entirely unavailable by users, even when the systems are continuing to function. Similarly, unavailability of select application functions might go unnoticed by administrators yet be devastating to users – a true availability measure is holistic.

Availability must be measured to be determined, ideally with comprehensive monitoring tools ("instrumentation") that are themselves highly available. If there is a lack of instrumentation, systems supporting high volume transaction processing throughout the day and night, such as credit card processing systems or telephone switches, are often inherently better monitored, at least by the users themselves, than systems which experience periodic lulls in demand.

An alternative metric is mean time between failures (MTBF).

Recovery time (or estimated time of repair (ETR), also known as recovery time objective (RTO) is closely related to availability, that is the total time required for a planned outage or the time required to fully recover from an unplanned outage. Another metric is mean time to recovery (MTTR). Recovery time could be infinite with certain system designs and failures, i.e. full recovery is impossible. One such example is a fire or flood that destroys a data center and its systems when there is no secondary disaster recovery data center.

Another related concept is data availability, that is the degree to which databases and other information storage systems faithfully record and report system transactions. Information management often focuses separately on data availability, or Recovery Point Objective, in order to determine acceptable (or actual) data loss with various failure events. Some users can tolerate application service interruptions but cannot tolerate data loss.

A service level agreement ("SLA") formalizes an organization's availability objectives and requirements.

## Military control systems

High availability is one of the primary requirements of the control systems in unmanned vehicles and autonomous maritime vessels. If the controlling system becomes unavailable, the Ground Combat Vehicle (GCV) or ASW Continuous Trail Unmanned Vessel (ACTUV) would be lost.

## System design

On one hand, adding more components to an overall system design can undermine efforts to achieve high availability because complex systems inherently have more potential failure points and are more difficult to implement correctly. While some analysts would put forth the theory that the most highly available systems adhere to a simple architecture (a single, high-quality, multi-purpose physical system with comprehensive internal hardware redundancy), this architecture suffers from the requirement that the entire system must be brought down for patching and operating system upgrades. More advanced system designs allow for systems to be patched and upgraded without compromising service availability (see load balancing and failover). High availability requires less human intervention to restore operation in complex systems; the reason for this being that the most common cause for outages is human error.

### High availability through redundancy

On the other hand, redundancy is used to create systems with high levels of availability (e.g. popular ecommerce websites). In this case it is required to have high levels of failure detectability and avoidance of common cause failures.

If redundant parts are used in parallel and have independent failure (e.g. by not being within the same data center), they can exponentially increase the availability and make the overall system highly available. If you have N parallel components each having X availability, then you can use following formula:

Availability of parallel components = 1 - (1 - X)^ N

So for example if each of your components has only 50% availability, by using 10 of components in parallel, you can achieve 99.9023% availability.

Two kinds of redundancy are passive redundancy and active redundancy.

Passive redundancy is used to achieve high availability by including enough excess capacity in the design to accommodate a performance decline. The simplest example is a boat with two separate engines driving two separate propellers. The boat continues toward its destination despite failure of a single engine or propeller. A more complex example is multiple redundant power generation facilities within a large system involving electric power transmission. Malfunction of single components is not considered to be a failure unless the resulting performance decline exceeds the specification limits for the entire system.

Active redundancy is used in complex systems to achieve high availability with no performance decline. Multiple items of the same kind are incorporated into a design that includes a method to detect failure and automatically reconfigure the system to bypass failed items using a voting scheme. This is used with complex computing systems that are linked. Internet routing is derived from early work by Birman and Joseph in this area. Active redundancy may introduce more complex failure modes into a system, such as continuous system reconfiguration due to faulty voting logic.

**Zero downtime** system design means that modeling and simulation indicates mean time between failures significantly exceeds the period of time between planned maintenance, upgrade events, or system lifetime. Zero downtime involves massive redundancy, which is needed for some types of aircraft and for most kinds of communications satellites. Global Positioning System is an example of a zero downtime system.

Fault instrumentation can be used in systems with limited redundancy to achieve high availability. Maintenance actions occur during brief periods of downtime only after a fault indicator activates. Failure is only significant if this occurs during a mission critical period.

Modeling and simulation is used to evaluate the theoretical reliability for large systems. The outcome of this kind of model is used to evaluate different design options. A model of the entire system is created, and the model is stressed by removing components. Redundancy simulation involves the N-x criteria. N represents the total number of components in the system. x is the number of components used to stress the system. N-1 means the model is stressed by evaluating performance with all possible combinations where one component is faulted. N-2 means the model is stressed by evaluating performance with all possible combinations where two component are faulted simultaneously.

## Reasons for unavailability

A survey among academic availability experts in 2010 ranked reasons for unavailability of enterprise IT systems. All reasons refer to **not following best practice** in each of the following areas (in order of importance):

1. Monitoring of the relevant components
2. Requirements and procurement
3. Operations
4. Avoidance of network failures
5. Avoidance of internal application failures
6. Avoidance of external services that fail
7. Physical environment
8. Network redundancy
9. Technical solution of backup
10. Process solution of backup
11. Physical location
12. Infrastructure redundancy
13. Storage architecture redundancy

A book on the factors themselves was published in 2003.

## Costs of unavailability

In a 1998 report from IBM Global Services, unavailable systems were estimated to have cost American businesses $4.54 billion in 1996, due to lost productivity and revenues.
