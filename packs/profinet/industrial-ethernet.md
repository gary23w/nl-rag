---
title: "Industrial Ethernet"
source: https://en.wikipedia.org/wiki/Industrial_Ethernet
domain: profinet
license: CC-BY-SA-4.0
tags: profinet, industrial ethernet, real-time fieldbus, profinet io
fetched: 2026-07-02
---

# Industrial Ethernet

**Industrial Ethernet** (**IE**) is the use of Ethernet in an industrial environment with protocols that provide determinism and real-time control. Protocols for industrial Ethernet include EtherCAT, EtherNet/IP, PROFINET, POWERLINK, SERCOS III, CC-Link IE, and Modbus TCP. Many industrial Ethernet protocols use a modified media access control (MAC) layer to provide low latency and determinism. Some microprocessors provide industrial Ethernet support.

Industrial Ethernet can also refer to the use of standard Ethernet protocols with rugged connectors and extended temperature switches in an industrial environment, for automation or process control. Components used in plant process areas must be designed to work in harsh environments of temperature extremes, humidity, and vibration that exceed the ranges for information technology equipment intended for installation in controlled environments. The use of fiber-optic Ethernet variants reduces the problems of electrical noise and provides electrical isolation.

Some industrial networks emphasized deterministic delivery of transmitted data, whereas Ethernet used collision detection which made transport time for individual data packets difficult to estimate with increasing network traffic. Typically, industrial uses of Ethernet employ full-duplex standards and other methods so that collisions do not unacceptably influence transmission times.

## Application environment

Industrial use requires consideration of the environment in which the equipment must operate. Factory equipment must tolerate a wider range of temperature, vibration, physical contamination and electrical noise than equipment installed in dedicated information-technology wiring closets. Since critical process control may rely on an Ethernet link, the economic cost of interruptions may be high and high availability is therefore an essential criterion. Industrial Ethernet networks must interoperate with both current and legacy systems, and must provide predictable performance and maintainability. In addition to physical compatibility and low-level transport protocols, a practical industrial Ethernet system must also provide interoperability of higher levels of the OSI model. An industrial network must provide security both from intrusions from outside the plant, and inadvertent or unauthorized use within the plant.

When an industrial network must connect to an office network or external networks, a firewall system can be inserted to control exchange of data between the networks. This network separation preserves the performance and reliability of the industrial network.

Industrial environments are often much harsher, often subject to oil sprays, water sprays, and physical vibrations, so often industrial Ethernet requires a more rugged and watertight connector on one or both ends of the Cat 5 or Cat 6 cable, such as M12 connectors or M8 connectors, rather than the 8P8C connectors commonly used in homes and businesses.

## Advantages and difficulties

Programmable logic controllers (PLCs) communicate using one of several possible open or proprietary protocols, such as EtherNet/IP, EtherCAT, Modbus, Sinec H1, Profibus, CANopen, DeviceNet or FOUNDATION Fieldbus. The idea to use standard Ethernet makes these systems more interoperable.

Some of the advantages over other types of industrial network include:

- Increased speed, up from 9.6 kbit/s with RS-232 to 1 Gbit/s with Gigabit Ethernet
- Ability to use ubiquitous Cat5e/Cat6 cables
- Option to use optical fiber for increased distance
- Ability to use standard networking hardware for wired and wireless communication
- Ability to have more than two nodes on link, which was possible with RS-485 but not with RS-232
- Potential to use peer-to-peer architectures as opposed to client–server ones
- Better interoperability

Difficulties of using industrial Ethernet include:

- Migrating existing systems to a new protocol
- Real-time performance may suffer for protocols using TCP
- Additional complexity associated with network technology
- The minimum Ethernet frame size is 64 bytes, while typical industrial communication data sizes can be closer to 1–8 bytes. This protocol overhead affects data transmission efficiency.
