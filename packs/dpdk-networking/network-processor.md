---
title: "Network processor"
source: https://en.wikipedia.org/wiki/Network_processor
domain: dpdk-networking
license: CC-BY-SA-4.0
tags: data plane development kit, kernel bypass, packet processing, network processor
fetched: 2026-07-02
---

# Network processor

A **network processor** is an integrated circuit which has a feature set specifically targeted at the networking application domain.

Network processors are typically software programmable devices and would have generic characteristics similar to general purpose central processing units that are commonly used in many different types of equipment and products.

## History of development

In modern telecommunications networks, information (voice, video, data) is transferred as packet data (termed packet switching) which is in contrast to older telecommunications networks that carried information as analog signals such as in the public switched telephone network (PSTN) or analog TV/Radio networks. The processing of these packets has resulted in the creation of integrated circuits (IC) that are optimised to deal with this form of packet data. Network processors have specific features or architectures that are provided to enhance and optimise packet processing within these networks.

Network processors have evolved into ICs with specific functions. This evolution has resulted in more complex and more flexible ICs being created. The newer circuits are programmable and thus allow a single hardware IC design to undertake a number of different functions, where the appropriate software is installed.

Network processors are used in the manufacture of many different types of network equipment such as:

- Routers, software routers and switches (Inter-network processors)
- Firewalls
- Session border controllers
- Intrusion detection devices
- Intrusion prevention devices
- Network monitoring systems
- Network security (secure cryptoprocessors)

### Reconfigurable Match-Tables

Reconfigurable Match-Tables were introduced in 2013 to allow switches to operate at high speeds while maintaining flexibility with respect to which network protocols are enabled on the device and/or how those protocols are processed. P4 is used to program the chips. The company Barefoot Networks was based around these processors and was later purchased by Intel in 2019.

An RMT pipeline relies on three main stages; the programmable parser, the Match-Action tables and the programmable deparser. The parser reads the packet in chunks and processes these chunks to find out which protocols are used in the packet (Ethernet, VLAN, IPv4...) and extracts certain fields from the packet into the Packet Header Vector (PHV). Certain fields in the PHV may be reserved for special uses such as present headers or total packet length. The protocols are typically programmable, and so are the fields to extract. The Match-Action tables are a series of units that read an input PHV and match certain fields in it using a crossbar and CAM memory. The result is a wide instruction that operates on one or more fields of the PHV and data to support this instruction. The output PHV is then sent to the next MA stage or to the deparser. The deparser takes in the PHV as well as the original packet and its metadata (to fill in missing bits that weren't extracted into the PHV) and then outputs the modified packet as chunks. The deparser, like the parser, is typically programmable and the two may share some configuration files.

FlexNIC attempts to apply this model to Network Interface Controllers allowing servers to send and receive packets at high speeds while maintaining protocol flexibility and without increasing the CPU overhead.

## Generic functions

In the generic role as a packet processor, a number of optimised features or functions are typically present in a network processor, which include:

- Pattern matching – the ability to find specific patterns of bits or bytes within packets in a packet stream.
- Key lookup – the ability to quickly undertake a database lookup using a key (typically an address in a packet) to find a result, typically routing information.
- Computation
- Data bitfield manipulation – the ability to change certain data fields contained in the packet as it is being processed.
- Queue management – as packets are received, processed and scheduled to be sent onwards, they are stored in queues.
- Control processing – the micro operations of processing a packet are controlled at a macro level which involves communication and orchestration with other nodes in a system.
- Quick allocation and re-circulation of packet buffers.

## Architectural paradigms

In order to deal with high data-rates, several architectural paradigms are commonly used:

- Pipeline of processors - each stage of the pipeline consisting of a processor performing one of the functions listed above.
- Parallel processing with multiple processors, often including multithreading.
- Specialized microcoded engines to more efficiently accomplish the tasks at hand.
- With the advent of multicore architectures, network processors can be used for higher layer (L4-L7) processing.

Additionally, traffic management, which is a critical element in L2-L3 network processing and used to be executed by a variety of co-processors, has become an integral part of the network processor architecture, and a substantial part of its silicon area ("real estate") is devoted to the integrated traffic manager. Modern network processors are also equipped with low-latency high-throughput on-chip interconnection networks optimized for the exchange of small messages among cores (few data words). Such networks can be used as an alternative facility for the efficient inter-core communication aside of the standard use of shared memory.

## Applications

Using the generic function of the network processor, a software program implements an application that the network processor executes, resulting in the piece of physical equipment performing a task or providing a service. Some of the applications types typically implemented as software running on network processors are:

- Packet or frame discrimination and forwarding, that is, the basic operation of a router or switch.
- Quality of service (QoS) enforcement – identifying different types or classes of packets and providing preferential treatment for some types or classes of packet at the expense of other types or classes of packet.
- Access Control functions – determining whether a specific packet or stream of packets should be allowed to traverse the piece of network equipment.
- Encryption of data streams – built in hardware-based encryption engines allow individual data flows to be encrypted by the processor.
- TCP offload processing
