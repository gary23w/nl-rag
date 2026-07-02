---
title: "Network on a chip"
source: https://en.wikipedia.org/wiki/Network_on_a_chip
domain: network-on-chip
license: CC-BY-SA-4.0
tags: network on chip, on-chip interconnect, router topology, flow control hardware
fetched: 2026-07-02
---

# Network on a chip

A **network on a chip**, or **network on chip** (**NoC** /ˌɛnˌoʊˈsiː/ *en-oh-SEE* or /nɒk/ *knock*), is a network-based communications subsystem on an integrated circuit ("chip"), most typically between modules in a system on chip (SoC). The modules on the IC are typically semiconductor IP cores schematizing various functions of the computer system, and are designed to be modular in the sense of network science. The network on chip is a router-based packet switching network between SoC modules.

NoC technology applies the theory and methods of computer networking to on-chip communication and brings notable improvements over conventional bus and crossbar communication architectures. Networks on chip come in many network topologies, many of which are still experimental as of 2018.

In the 2000s, researchers had started to propose a type of on-chip interconnection in the form of packet switching networks in order to address the scalability issues of bus-based design. Preceding researches proposed the design that routes data packets instead of routing the wires. Then, the concept of "networks on chip" was proposed in 2002. NoCs improve the scalability of systems-on-chip and the power efficiency of complex SoCs compared to other communication subsystem designs. They are an emerging technology, with projections for large growth in the near future as multicore computer architectures become more common.

## Structure

NoCs can span synchronous and asynchronous clock domains, known as clock domain crossing, or use unclocked asynchronous logic. NoCs support globally asynchronous, locally synchronous electronics architectures, allowing each processor core or functional unit on a system on chip to have its own clock domain.

## Architectures

NoC architectures typically model sparse small-world networks (SWNs) and scale-free networks (SFNs) to limit the number, length, area and power consumption of interconnection wires and point-to-point connections.

## Topology

The topology determines the physical layout and connections between nodes and channels. The message traverses hops, and each hop's channel length depends on the topology. The topology significantly influences both latency and power consumption. Furthermore, since the topology determines the number of alternative paths between nodes, it affects the network traffic distribution, and hence the network bandwidth and performance achieved.

## Benefits

Traditionally, ICs have been designed with dedicated point-to-point connections, with one wire dedicated to each signal. This results in a dense network topology. For large designs, in particular, this has several limitations from a physical design viewpoint. It requires power quadratic in the number of interconnections. The wires occupy much of the area of the chip, and in nanometer CMOS technology, interconnects dominate both performance and dynamic power dissipation, as signal propagation in wires across the chip requires multiple clock cycles. This also allows more parasitic capacitance, resistance and inductance to accrue on the circuit. (See Rent's rule for a discussion of wiring requirements for point-to-point connections).

Sparsity and locality of interconnections in the communications subsystem yield several improvements over traditional bus-based and crossbar-based systems.

## Parallelism and scalability

The wires in the links of the network-on-chip are shared by many signals. A high level of parallelism is achieved, because all data links in the NoC can operate simultaneously on different data packets. Therefore, as the complexity of integrated systems keeps growing, a NoC provides enhanced performance (such as throughput) and scalability in comparison with previous communication architectures (e.g., dedicated point-to-point signal wires, shared buses, or segmented buses with bridges). The algorithms must be designed in such a way that they offer large parallelism and can hence utilize the potential of NoC.

## Current research

Some researchers think that NoCs need to support quality of service (QoS), namely achieve the various requirements in terms of throughput, end-to-end delays, fairness, and deadlines. Real-time computation, including audio and video playback, is one reason for providing QoS support. However, current system implementations like VxWorks, RTLinux or QNX are able to achieve sub-millisecond real-time computing without special hardware.

This may indicate that for many real-time applications the service quality of existing on-chip interconnect infrastructure is sufficient, and dedicated hardware logic would be necessary to achieve microsecond precision, a degree that is rarely needed in practice for end users (sound or video jitter need only tenth of milliseconds latency guarantee). Another motivation for NoC-level quality of service (QoS) is to support multiple concurrent users sharing resources of a single chip multiprocessor in a public cloud computing infrastructure. In such instances, hardware QoS logic enables the service provider to make contractual guarantees on the level of service that a user receives, a feature that may be deemed desirable by some corporate or government clients.

Many challenging research problems remain to be solved at all levels, from the physical link level through the network level, and all the way up to the system architecture and application software. The first dedicated research symposium on networks on chip was held at Princeton University, in May 2007. The second IEEE International Symposium on Networks-on-Chip was held in April 2008 at Newcastle University.

Research has been conducted on integrated optical waveguides and devices comprising an optical network on a chip (ONoC).

The possible way to increasing the performance of NoC is use wireless communication channels between chiplets — named wireless network on chip (WiNoC).

## Side benefits

In a multi-core system, connected by NoC, coherency messages and cache miss requests have to pass switches. Accordingly, switches can be augmented with simple tracking and forwarding elements to detect which cache blocks will be requested in the future by which cores. Then, the forwarding elements multicast any requested block to all the cores that may request the block in the future. This mechanism reduces cache miss rate.

## Benchmarks

NoC development and studies require comparing different proposals and options. NoC traffic patterns are under development to help such evaluations. Existing NoC benchmarks include NoCBench and MCSL NoC Traffic Patterns.

## Interconnect processing unit

An interconnect processing unit (IPU) is an on-chip communication network with hardware and software components which jointly implement key functions of different system-on-chip programming models through a set of communication and synchronization primitives and provide low-level platform services to enable advanced features in modern heterogeneous applications on a single die.
