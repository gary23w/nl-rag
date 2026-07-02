---
title: "SD-WAN"
source: https://en.wikipedia.org/wiki/SD-WAN
domain: sase-architecture
license: CC-BY-SA-4.0
tags: secure access service edge, sase model, cloud-delivered security, converged networking security
fetched: 2026-07-02
---

# SD-WAN

A **Software-Defined Wide Area Network** (**SD-WAN**) is a wide area network that uses software-defined networking technology, such as communicating over the Internet using overlay tunnels which are encrypted when destined for internal organization locations.

If standard tunnel setup and configuration messages are supported by all of the network hardware vendors, SD-WAN simplifies the management and operation of a WAN by decoupling the networking hardware from its control mechanism. This concept is similar to how software-defined networking implements virtualization technology to improve data center management and operation. In practice, proprietary protocols are used to set up and manage an SD-WAN, meaning there is no decoupling of the hardware and its control mechanism.

A key application of SD-WAN is to allow companies to build higher-performance WANs using lower-cost and commercially available Internet access, enabling businesses to partially or wholly replace more expensive private WANs connection technologies such as MPLS.

When SD-WAN traffic is carried over the Internet, there are no end-to-end performance guarantees. Carrier MPLS VPN WAN services are not carried as Internet traffic, but rather over carefully controlled carrier capacity, and do come with an end-to-end performance guarantee.

## History

WANs were very important for the development of networking in general and for a long time one of the most important applications of networks both for military and enterprise applications. The ability to communicate data over long distances was one of the main driving factors for the development of data communications, as it made it possible to overcome the distance limitations, as well as shortening the time necessary to exchange messages with other parties.

Legacy WANs allowed communication over circuits connecting two or more endpoints. Earlier networking supported point-to-point communication over a slow speed circuit, usually between two fixed locations. As networking progressed, WAN circuits became faster and more flexible. Innovations like circuit and packet switching (in the form of X.25, ATM and later Internet Protocol or Multiprotocol Label Switching) allowed communication to become more dynamic, supporting ever-growing networks.

The need for strict control, security and quality of service (QOS) meant that multinational corporations were very conservative in leasing and operating their WANs. National regulations restricted the companies that could provide local service in each country, and complex arrangements were necessary to establish truly global networks. All that changed with the growth of the Internet, which permitted entities around the world to connect to each other. However, over the first years, the uncontrolled nature of the Internet was not considered adequate or safe for private corporate use.

Independent of safety concerns, connectivity to the Internet became a necessity to the point where every branch required Internet access. At first, due to safety concerns, private communications were still done via WAN, and communication with other entities (including customers and partners) moved to the Internet.

As the Internet grew in reach and maturity, companies started to evaluate how to leverage it for private corporate communications. During the early 2000s, application delivery over the WAN became an important topic of research and commercial innovation. Over the next decade, increasing computing power made it possible to create software-based appliances that were able to analyze traffic and make informed decisions without delays, making it possible to create large-scale overlay networks over the public Internet that could replicate all the functionality of legacy WANs, at a fraction of the cost.

SD-WAN combines several networking aspects to create full-fledged private networks, with the ability to dynamically share network bandwidth across the connection points. Additional enhancements include central controllers, zero-touch provisioning, integrated analytics and on-demand circuit provisioning, with some network intelligence based in the cloud, allowing centralized policy management and security.

Networking publications started using the term SD-WAN to describe this new networking trend as early as 2014. With the rapid shift to remote work as a result of lockdowns and stay at home orders during the COVID-19 pandemic, SD-WAN grew in popularity as a way of connecting remote workers.

## Overview

WANs allow companies to extend their computer networks over large distances, connecting remote branch offices to data centers and to each other, and delivering applications and services required to perform business functions. Due to the physical constraints imposed by the propagation time over large distances, and the need to integrate multiple service providers to cover global geographies (often crossing nation boundaries), WANs face important operational challenges, including network congestion, packet delay variation, packet loss, and even service outages. Modern applications such as VoIP calling, videoconferencing, streaming media, and virtualized applications and desktops require low latency. Bandwidth requirements are also increasing, especially for applications featuring high-definition video. It can be expensive and difficult to expand WAN capability, with corresponding difficulties related to network management and troubleshooting.

SD-WAN products are designed to address these network problems. By enhancing or even replacing traditional branch routers with virtualization appliances that can control application-level policies and offer a network overlay, less expensive consumer-grade Internet links can act more like a dedicated circuit. This simplifies the setup process for branch personnel.

SD-WAN products can be physical appliances or software based only.

### Components

The MEF Forum has defined an SD-WAN architecture consisting of an SD-WAN edge, SD-WAN gateway, SD-WAN controller and SD-WAN orchestrator.

#### SD-WAN edge

The SD-WAN edge is a physical or virtual network function that is placed at an organization's branch/regional/central office site, data center, and in public or private cloud platforms. MEF Forum has published the first SD-WAN service standard, MEF 70 which defines the fundamental characteristics of an SD-WAN service plus service requirements and attributes.

#### SD-WAN gateway

SD-WAN gateways provide access to the SD-WAN service in order to shorten the distance to cloud-based services or the user, and reduce service interruptions. A distributed network of gateways may be included in an SD-WAN service by the vendor or setup and maintained by the organization using the service. By sitting outside the headquarters in the cloud, the gateway also reduces headquarters traffic.

#### SD-WAN orchestrator

The SD-WAN orchestrator is a cloud hosted or on-premises web management tool that allows configuration, provisioning and other functions when operating an SD-WAN. It simplifies application traffic management by allowing central implementation of an organization's business policies.

#### SD-WAN controller

The SD-WAN controller functionality, which can be placed in the orchestrator or in an SD-WAN gateway, is used to make forwarding decisions for application flows. Application flows are IP packets that have been classified to determine their user application or grouping of applications to which they are associated. The grouping of application flows based on a common type, e.g., conferencing applications, is referred to as an Application Flow Group in MEF 70. Per MEF 70, the SD-WAN Edge classifies incoming IP packets at the SD-WAN UNI (SD-WAN user network interface), determines, via OSI Layer 2 through Layer 7 classification, which application flow the IP packets belong to, and then applies the policies to block the application flow or allow the application flows to be forwarded based on the availability of a route to the destination SD-WAN UNI on a remote SD-WAN Edge. This helps ensure that application performance meets service level agreements (SLAs).

## Required characteristics

The Gartner research firm has defined an SD-WAN as having four required characteristics:

- The ability to support multiple connection types, such as MPLS, last mile fiber optic network or through high speed cellular networks e.g. 4G LTE and 5G wireless technologies
- The ability to do dynamic path selection, for load sharing and resiliency purposes
- A simple interface that is easy to configure and manage
- The ability to support VPNs, and third party services such as WAN optimization controllers, firewalls and web gateways

## Features

Features of SD-WANs include resilience, quality of service (QoS), security, and performance, with flexible deployment options; simplified administration and troubleshooting; and online traffic engineering.

### Resilience

A resilient SD-WAN reduces network downtime. To be resilient, the technology must feature real-time detection of outages and automatic switch over (fail over) to working links. Many SD-WAN deployments use multiple network transports, including broadband, MPLS, and fixed wireless access, to maintain connectivity during outages or periods of degraded network performance.

### Quality of service

SD-WAN technology supports quality of service by having application level awareness, giving bandwidth priority to the most critical applications. This may include dynamic path selection, sending an application on a faster link, or even splitting an application between two paths to improve performance by delivering it faster.

### Security

SD-WAN communication is usually secured using IPsec, a staple of WAN security.

### Application optimization

SD-WANs can improve application delivery using caching, storing recently accessed information in memory to speed future access.

### Self-healing networks

SD-WANs can incorporate *artificial intelligence for IT operations* (AIOps) for continuous troubleshooting and fixes to network issues. Modern SD-WAN platforms may also use network analytics and real-time telemetry to improve traffic optimization, application visibility, and proactive issue detection across global enterprise environments.

### Deployment options

Most SD-WAN products are available as pre-configured appliances, placed at the network edge in data centers, branch offices and other remote locations. There are also virtual appliances that can work on existing network hardware, or the appliance can be deployed as a virtual appliance on the cloud in environments such as Amazon Web Services (AWS), Unified Communications as a service (UCaaS) or as Software as a Service (SaaS). This allows enterprises to benefit from SD-WAN services as they migrate application delivery from corporate servers to cloud based services such as Salesforce.com and Google apps.SD-WAN is commonly used to optimize connectivity between enterprise branch locations, cloud platforms, and software-as-a-service (SaaS) applications through centralized traffic management and intelligent routing.

### Administration and troubleshooting

As with network equipment in general, GUIs may be preferred to command line interface (CLI) methods of configuration and control. Other beneficial administrative features include automatic path selection, the ability to centrally configure each end appliance by pushing configuration changes out, and even a true software defined networking approach that lets all appliances and virtual appliances be configured centrally based on application needs rather than underlying hardware.

### Online traffic engineering

With a global view of network status, a controller that manages SD-WAN can perform careful and adaptive traffic engineering by assigning new transfer requests according to current usage of resources (links). For example, this can be achieved by performing central calculation of transmission rates at the controller and rate-limiting at the senders (end-points) according to such rates.

## Secure access service edge (SASE)

SD-WAN is a core component of secure access service edge solutions (SASE) which incorporate network and security capabilities to more efficiently and securely connect distributed work environments (branch office, headquarters, home office, remote) to distributed applications located in data centers, cloud infrastructure, or delivered by SaaS services. With SASE, SD-WAN is combined with other network and security technologies including cloud access security broker (CASB), Secure Web Gateway, Data Loss Prevention (DLP), Zero Trust Network Access (ZTNA), Firewall, and other capabilities to connect and protect users and applications. SD-WAN and SASE architectures are increasingly used by multinational organizations to improve application performance, simplify global connectivity, and support hybrid work environments across distributed enterprise locations. In December 2021, Gartner research firm estimated that by 2025, 50% of SD-WAN purchases will be part of a single vendor SASE offering.

## Complementary technology

### SD-WAN versus WAN optimization

There are some similarities between SD-WAN and WAN optimization, the name given to the collection of techniques used to increase data-transfer efficiencies across WANs. The goal of each is to accelerate application delivery between branch offices and data centers, but SD-WAN technology focuses additionally on cost savings and efficiency, specifically by allowing lower cost network links to perform the work of more expensive leased lines, whereas WAN Optimization focuses squarely on improving packet delivery. An SD-WAN utilizing virtualization techniques assisted with WAN Optimization traffic control allows network bandwidth to dynamically grow or shrink as needed. SD-WAN technology and WAN optimization can be used separately or together, and some SD-WAN vendors are adding WAN optimization features to their products.

### WAN edge routers

A WAN edge router is a device that routes data packets between different WAN locations, giving enterprise access to a carrier network. Also called a boundary router, it is unlike a core router, which only sends packets within a single network. SD-WANs can work as an overlay to simplify the management of existing WAN edge routers, by lowering dependence on routing protocols. SD-WAN can also potentially be an alternative to WAN Edge routers.

### SD-WAN versus hybrid WAN

SD-WANs are similar to hybrid WANs, and sometimes the terms are used interchangeably, but they are not identical. A hybrid WAN consists of different connection types, and may have a software defined network (SDN) component, but doesn't have to.

### SD-WAN versus MPLS

Cloud-based SD-WAN offers advanced features, such as enhanced security, seamless cloud, and support for mobile users, that result naturally from the use of cloud infrastructure. As a result, cloud-based SD-WAN can replace MPLS, enabling organizations to release resources once tied to WAN investments and create new capabilities. Many organizations adopt hybrid WAN strategies that combine MPLS, broadband internet, and wireless connectivity to balance performance, resilience, and cost efficiency during network modernization initiatives.

An overview discussing three typical reasons to compare MPLS with SD-WAN. Specifically where IT teams need to retain MPLS due to contract commitments and where the Enterprise migrates from MPLS to an Internet-based SD-WAN.

## Testing and validation

As there is no standard algorithm for SD-WAN controllers, device manufacturers each use their own proprietary algorithm in the transmission of data. These algorithms determine which traffic to direct over which link and when to switch traffic from one link to another. Given the breadth of options available in relation to both software and hardware SD-WAN control solutions, it's imperative they be tested and validated under real-world conditions within a lab setting prior to deployment.

There are multiple solutions available for testing purposes, ranging from purpose-built network emulation appliances which can apply specified network impairments to the network being tested in order to reliably validate performance, to software-based solutions.

## Marketplace

Network World IT website divides the SD-WAN vendor market into three groups: established networking vendors who are adding SD-WAN products to their offerings, WAN specialists who are starting to integrate SD-WAN functionality into their products, and startups focused specifically on the SD-WAN market. The global SD-WAN market stood at $3.25 billion in 2021 and the market is expected to grow 30% in 2022. According to SD-WAN market Report Datavagyanik, North America accounted for more than 77% of the market.

Alternatively, a market overview by Nemertes Research groups SD-WAN vendors into categories based on their original technology space, and which are "Pure-play SD-WAN providers", "WAN optimization vendors", "Link-aggregation vendors", and "General network vendors". While Network World's second category (startups focused specifically on the SD-WAN market), is generally equivalent to Nemertes' "Pure-play SD-WAN providers" category, Nemertes offers a more detailed view of the preexisting WAN and overall networking providers.

Additionally, Nemertes Research also describes the in-net side of the SD-WAN market, describing the go-to-market strategy of connectivity providers entering the SD-WAN market. These providers include "Network-as-a-service vendors", "Carriers or telcos", "Content delivery networks" and "Secure WAN providers".

### Open source

MEF 70 standardizes SD-WAN service attributes and uses standard IPv4 and IPv6 routing protocols. SD-WAN services also use standard IPsec encryption protocols. Additional standardization for other SD-WAN functions and related security functionality not covered in MEF 70 are under development at the MEF Forum. There are several opensource SD-WAN solutions and opensource SD-WAN implementations available. For example, the Linux Foundation has three projects that intersect with and help the SD-WAN market: ONAP, OpenDaylight Project, and the Tungsten Fabric (formerly Juniper Networks' OpenContrail).
