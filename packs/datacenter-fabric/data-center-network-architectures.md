---
title: "Data center network architectures"
source: https://en.wikipedia.org/wiki/Data_center_network_architectures
domain: datacenter-fabric
license: CC-BY-SA-4.0
tags: data center fabric, network fabric, fat tree topology, network architecture
fetched: 2026-07-02
---

# Data center network architectures

A **data center** is a pool of resources (computational, storage, network) interconnected using a communication network. A data center network (DCN) holds a pivotal role in a data center, as it interconnects all of the data center resources together. DCNs need to be scalable and efficient to connect tens or even hundreds of thousands of servers to handle the growing demands of cloud computing. Today's data centers are constrained by the interconnection network.

The adoption of hybrid cloud computing has influenced the design of modern data center networks. By integrating on-premises infrastructure with private and public cloud environments, organizations can distribute applications and workloads across multiple locations. As a result, data center resources no longer need to be physically co-located and can communicate through interconnected network architectures.

## Types of data center network topologies

Data center networks can be divided into multiple separate categories.

- **Fixed topology**
  - Tree-based
    - Basic tree
    - Clos network
      - VL2
      - Fat-tree
        - Al-Fares et al.
        - Portland
        - Hedera
  - Recursive
    - DCell
    - BCube
    - MDCube
    - FiConn
  - Flat
    - RNG
- **Flexible topology**
  - Fully optical
    - OSA (Optical switching architecture)
  - Hybrid
    - c-Through
    - Helios

## Types of data center network architectures

### Three-tier

The legacy three-tier DCN architecture follows a multi-rooted tree based network topology composed of three layers of network switches, namely access, aggregate, and core layers. The servers in the lowest layers are connected directly to one of the edge layer switches. The aggregate layer switches interconnect together multiple access layer switches. All of the aggregate layer switches are connected to each other by core layer switches. Core layer switches are also responsible for connecting the data center to the Internet. The three-tier is the common network architecture used in data centers. However, three-tier architecture is unable to handle the growing demand of cloud computing. The higher layers of the three-tier DCN are highly oversubscribed. Moreover, scalability is another major issue in three-tier DCN. Major problems faced by the three-tier architecture include, scalability, fault tolerance, energy efficiency, and cross-sectional bandwidth. The three-tier architecture uses enterprise-level network devices at the higher layers of topology that are very expensive and power hungry.

### Fat tree

The fat tree DCN architecture reduces the oversubscription and cross section bandwidth problem faced by the legacy three-tier DCN architecture. Fat tree DCN employs commodity network switches based architecture using Clos topology. The network elements in fat tree topology also follows hierarchical organization of network switches in access, aggregate, and core layers. However, the number of network switches is much larger than the three-tier DCN. The architecture is composed of *k* pods, where each pod contains, (k/2)2 servers, k/2 access layer switches, and k/2 aggregate layer switches in the topology. The core layers contain (k/2)2 core switches where each of the core switches is connected to one aggregate layer switch in each of the pods. The fat tree topology can offer up to 1:1 oversubscription ratio and full bisection bandwidth, depending on each rack's total bandwidth versus the bandwidth available at the tree's highest levels. Higher tree branches are typically oversubscribed to their lower branches by a ratio of 1:5, with the problem compounding at the highest tree levels, including up to 1:80 or 1:240, at the highest levels. The fat tree architecture uses a customized addressing scheme and routing algorithm. The scalability is one of the major issues in fat tree DCN architecture and maximum number of pods is equal to the number of ports in each switch.

### DCell

DCell is a server-centric hybrid DCN architecture where one server is directly connected to one server. A server in the DCell architecture is equipped with multiple network interface cards (NICs). The DCell follows a recursively built hierarchy of cells. A cell0 is the basic unit and building block of DCell topology arranged in multiple levels, where a higher level cell contains multiple lower layer cells. The cell0 is building block of DCell topology, which contains *n* servers and one commodity network switch. The network switch is only used to connect the server within a cell0. A cell1 contains *k=n+1* cell0 cells, and similarly a cell2 contains k * n + 1 dcell1. The DCell is a highly scalable architecture where a four level DCell with only six servers in cell0 can accommodate around 3.26 million servers. Besides very high scalability, the DCell architecture depicts very high structural robustness. However, cross section bandwidth and network latency is a major issue in DCell DCN architecture.

### Others

Some of the other well-known DCNs include BCube, Camcube, FiConn, Jelly fish, and Scafida. A qualitative discussion of different DCNs along with benefits and drawbacks associated with each one has been made available.

## Challenges

Scalability is one of the foremost challenges to the DCNs. With the advent of cloud paradigm, data centers are required to scale up to hundreds of thousands of nodes. Besides offering immense scalability, the DCNs are also required to deliver high cross-section bandwidth. Current DCN architectures, such as three-tier DCN offer poor cross-section bandwidth and possess very high over-subscription ratio near the root. Fat tree DCN architecture delivers 1:1 oversubscription ratio and high cross section bandwidth, but it suffers from low scalability limited to *k*=total number of ports in a switch. DCell offers immense scalability, but it delivers very poor performance under heavy network load and one-to-many traffic patterns.

## Performance Analysis of DCNs

A quantitative analysis of the three-tier, fat tree, and DCell architectures for performance comparison (based on throughput and latency) is performed for different network traffic pattern. The fat tree DCN delivers high throughput and low latency as compared to three-tier and DCell. DCell suffers from very low throughput under high network load and one to many traffic patterns. One of the major reasons for DCell's low throughput is very high over subscription ratio on the links that interconnect the highest level cells.

## Structural robustness and Connectivity of DCNs

The DCell exhibits very high robustness against random and targeted attacks and retains most of its node in the giant cluster after even 10% of targeted failure. multiple failures whether targeted or random, as compared to the fat tree and three-tier DCNs. One of the major reasons for high robustness and connectivity of the DCell is its multiple connectivity to other nodes that is not found in fat tree or three-tier architectures.

## Energy efficiency of DCNs

The concerns about the energy needs and environmental impacts of data centers are intensifying. Energy efficiency is one of the major challenges of today's information and communications technology (ICT) sector. The networking portion of a data center is accounted to consume around 15% of overall cyber energy usage. Around 15.6 billion kWh of energy was utilized solely by the communication infrastructure within the data centers worldwide in 2010. The energy consumption by the network infrastructure within a data center is expected to increase to around 50% in data centers. IEEE 802.3az standard has been standardized in 2011 that make use of adaptive link rate technique for energy efficiency. Moreover, fat tree and DCell architectures use commodity network equipment that is inherently energy efficient. Workload consolidation is also used for energy efficiency by consolidating the workload on few devices to power-off or sleep the idle devices.
