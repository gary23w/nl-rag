---
title: "Master–slave (technology)"
source: https://en.wikipedia.org/wiki/Master/slave_(technology)
domain: modbus-protocol
license: CC-BY-SA-4.0
tags: modbus protocol, modbus rtu, modbus tcp, serial fieldbus
fetched: 2026-07-02
---

# Master–slave (technology)

(Redirected from

Master/slave (technology)

)

In engineering, **master–slave** is a relationship between two systems in which one controls the other. In some cases, one master controls just one slave system, but in others, there are multiple slave systems controlled by the same master. Sometimes the master is a different kind of system than the slave, but sometimes there are multiple similar systems and one of them is designated the master in order to centralize external (i.e., user) control of the collection.

Due to it being prone to being associated with slavery, the terminology is a subject of controversy and has been replaced with alternative terms in some cases.

## Examples

In photography, secondary, or slave, flash units are connected to a master unit to provide synchronized lighting.

Parallel audio duplication often entails multiple recording with devices (i.e., for cassette tape or compact disc) linked together so that operating the controls of a master device triggers the same commands on slave devices.

Railway locomotives operating in the same train (for example, to pull a load too heavy for a single locomotive) may be configured for master–slave operation with all but one of the locomotives controlled from the first. See Multiple-unit train control.

In a hydraulic system, a master cylinder is a control device that converts force into hydraulic pressure that drives movement in a slave cylinder at the other end of the hydraulic line. A common application is a vehicle brake system.

A master clock provides time signals used to synchronize one or more slave clocks as part of a clock network. A slave clock receives and displays the time from a master, though it may be able to keep time itself if the master is not working.

### Computing

Computer bus protocols often use a master-slave relationship. For instance, a USB host manages access to the USB bus shared by any number of USB devices. A serial peripheral interface (SPI) bus typically has a single master controlling multiple slaves. I2C and I3C may even have multiple masters on a bus. Modbus also uses a master device to initiate connection requests to slave devices.

An edge-triggered flip-flop can be created by arranging two gated latches in a master–slave configuration. It is so named because the master latch controls the slave latch's value and forces the slave latch to hold its value, as the slave latch always copies its new value from the master latch.

In database replication, the master database is the authoritative source. The slave or replica database is controlled by the master database, which repeats its update commands (for example by way of event log) to the slave. The slave therefore retains an exact copy of transaction processed by the source database (up to the most recently transmitted log) This scheme is not as strict as electronic devices sharing a clock, however the slave database only does what the master tells it, unless the slave is promoted due to failure of the master. Some databases implement so called *multi-master replication*, where a mix of writeable master nodes and readable nodes is used. These databases are used in scenarios where performance is an acceptable tradeoff for ACID properties, for example, non-mission-critical data, like suggesting similar purchases.

## Non-examples

The term *master* is used in some technology contexts that do not refer to a relationship of control. *Master* may be used to mean a copy that has more significance than other copies, in which case the term is an absolute concept, not a relationship. Sometimes the term *master–slave* is used in contexts that do not imply a controlling relationship.

In source code management *master* may refer to the trunk. In disk imaging, the gold master is the version that will be released to manufacturing for duplication.

A Parallel ATA (aka IDE) hard drive interface supports two hard drives on a cable, which are designated *master* and *slave*. The distinction is required by the interface even though neither drive has control or priority over the other.

## History

The *master–slave* terminology was first used in 1904.

The terminology was used in 1988 for RFC 1059 and in 1997 for RFC 2136, related to the domain name system. In 2020, Paul Vixie commented on his choice of words:

> I introduced the master/slave terminology in RFC 2136, because I needed names for the roles in an AXFR/IXFR transaction, and the zone transfer hierarchy could be more than one layer deep, such that a server might initiate some AXFR/IXFR's to the "primary master" but then respond to AXFR/IXFR's from other servers. In retrospect I should have chosen the terms, "transfer initiator" and "transfer responder". However, the hydraulic brake and clutch systems in my car had "master cylinders" and "slave cylinders", and so I did not think I was either inventing a new use for the words "master" and "slave", or that my use of them for this purpose would be controversial.

Said hydraulic brakes for the automotive industry were patented in 1917 by Malcolm Loughead. The term *slave cylinder* was used in other patent applications, including one by Robert Esnault-Pelterie, published in 1919.

## Controversy

Media analytics company Global Language Monitor placed *master/slave* first in their annual list of politically charged language for 2004. The Black Lives Matter movement in the United States sparked renewed discussion, and terminology changes occurred in 2020. Some argued, however, that terminology changes were superficial or performative activism.

Various alternate and generally context sensitive terms have been proposed including:

- *host–client*
- *primary–secondary*
- *main–replica*
- *main–subordinate*
- *initiator–target*
- *requester–responder*
- *controller–target*
- *controller–device*
- *host–worker*
- *host–proxy*
- *leader–follower*
- *director–performer*
- *boss–worker*
- *primary–replica*
- *principal–agent*
- *controller–worker*
- *primary–subordinate*
- *primary–worker*
- *orchestrator–worker*

### Notable events

In 2003, after receiving a discrimination complaint from a county employee, the County of Los Angeles in California asked that manufacturers, suppliers and contractors stop using *master* and *slave* terminology on products. Following complaints, the County of Los Angeles issued a statement saying that the decision was "nothing more than a request".

In 2018, after a heated debate, developers of Python replaced the term. Depending on context, Python switched to *main*, *parent*, or *server* (in place of *master*), and *worker*, *child*, or *helper* (in place of *slave*). The Linux kernel adopted a similar policy to use more specific terms in new code and documentation.

In July 2018, Google's developer style guide was updated to include avoiding the term *master* in software documentation, especially in combination with *slave.* Instead, the guide recommends terms – when in combination – such as *primary/secondary* and *original/replica*. Many individual variants of master and slave are given.

In 2020, GitHub renamed the default *master* git branch to *main*.
