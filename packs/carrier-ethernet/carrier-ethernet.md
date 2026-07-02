---
title: "Carrier Ethernet"
source: https://en.wikipedia.org/wiki/Carrier_Ethernet
domain: carrier-ethernet
license: CC-BY-SA-4.0
tags: carrier ethernet, provider backbone bridging, ethernet services, operator networks
fetched: 2026-07-02
---

# Carrier Ethernet

**Carrier Ethernet** is a marketing term for extensions to Ethernet for communications service providers that utilize Ethernet technology in their networks.

## Background

Ethernet has a long history. It has become dominant in enterprise networks. This dominance has led to high production-volume components, which in turn have allowed extremely low cost per bit. Likewise, Ethernet has a long history of re-inventing itself. From the original copper coaxial cable format ("thicknet") it has extended its scope to nearly all copper, optical fiber and wireless physical media. Bit rates have continued to increase, traditionally growing tenfold each time a new rate is defined. Gigabit Ethernet interfaces are widely deployed in PCs and servers, and 10 Gbit/s in local area network (LAN) backbones. Rates up to 100 Gigabit Ethernet were standardized in 2010 and 2011.

Ethernet's dominance is partly attributed to the simple advantages for the industry of adopting a single standard to drive up volumes and drive down prices. In part, it is also due to ease of deployment, using its ability to self-configure based on the key concepts of *learning bridge* (flooding, and associating learned destination addresses with bridge ports) and Spanning Tree Protocol (the protocol used for avoiding bridging loops).

Historically, competing protocols and cabling have been created in order to access higher speed devices than contemporary Ethernet-connected devices handled at an affordable price. Examples include FireWire and Light Peak. One motive to create competing standards has been to drive down the price of comparable-speed Ethernet devices. Once this purpose is achieved, competing standards tend to disappear or be confined to very specialized niches.

Ethernet is a fairly simple protocol which has scaled to hundreds of thousands of times faster speeds and consistently been able to adapt to meet the needs and demands of new markets. For example, time domain capabilities are being added to IEEE 802.3 Ethernet to support IEEE 802.1 Audio Video Bridging (AVB), and these capabilities will be applicable to time sensitive carrier applications likewise IEEE 1588.

Customer LAN networks are increasingly connected to wide-area telecommunications networks over Ethernet interfaces or to devices that bridge digital subscriber line (DSL) or wireless to these. Moreover, customers are familiar with the capabilities of Ethernet networks, and would like to extend these capabilities to multi-site networks. Meanwhile, the needs of such networks have expanded to include many services previously handled only on the LAN or by specialized connections, notably video and backup. It is not practical to expand most small networks beyond 1G or at most 2G (dual teaming gigabit) capacity per segment, since the bottleneck remains in the wide area links to other offices and online services.

### Carrier constraints

Thus wide area network (WAN) and metropolitan area network (MAN) providers find themselves with three needs:

1. To provide their customers with Ethernet services
2. To make use of the volume and cost advantages of Ethernet technologies in their networks
3. To replace non-Ethernet technologies with Ethernet competitors that have sufficient capacity for storage, backup and HD video and guarantee features (transfer certainty, low latency) needed to support these services

They are also constrained as services cannot be migrated from local to wide area services too fast lest they exceed the total provisioning available and result in unacceptable quality. Services that try to expand too fast lose money while those that wait too long lose customers. Accordingly, carriers must expand their services conservatively and pay close attention to quality of service (QoS).

#### The Beginning: Metro Ethernet

The MEF was formed in 2001 in order to develop ubiquitous business services for Enterprise users principally accessed over optical metropolitan networks in order to connect their Enterprise LANs. The principal concept was to bring the simplicity and cost model of Ethernet to the wide area network.

#### Expansion to Carrier Ethernet

The success of Metro Ethernet Services caught the imagination of the world when the concept expanded to include worldwide services traversing national and global networks:

- Access networks to provide availability to a much wider class of user over fiber, copper, cable, passive optical network (PON), and wireless
- Economy of scale from the resulting converged business, residential and wireless networks sharing the same infrastructure and services
- Scalability & rapid deployment of business applications
- Adoption of the certification program
- All while retaining the cost model and simplicity of Ethernet

## Carrier Ethernet services

To create a market in Ethernet services, it is necessary to clarify and standardise the services to be provided. Recognising this, the industry created the MEF. This played a key role in defining:

- **Ethernet Virtual Private Line** or **E-Line**: a service connecting two customer Ethernet ports over a WAN.
- **Ethernet Virtual Private LAN** or **E-LAN**: a multipoint service connecting a set of customer endpoints, giving the appearance to the customer of a bridged Ethernet network connecting the sites.
- **Ethernet Virtual Private Tree** or **E-Tree**: a multipoint service connecting one or more roots and a set of leaves, but preventing inter-leaf communication.

All these services provide standard definitions of such characteristics as bandwidth, resilience and service multiplexing, allowing customers to compare service offerings and facilitating service level agreements (SLAs). *Analogous definitions for wireless networks are defined in IEEE 802.21 and IEEE 802.11u, though these are intended for much shorter time commitments and services appropriate for mobile users only.*

### Ethernet Virtual Private Tree

**Ethernet Virtual Private Tree** or **E-Tree** is a point-to-multipoint Ethernet Virtual Connection defined by the MEF — an Ethernet VLAN configuration suitable for multicast services.

### Ethernet private line

**Ethernet private line** (**EPL**) and **Ethernet virtual private line** (**EVPL**) are data services defined by the MEF. EPL provides a point-to-point Ethernet virtual connection (EVC) between a pair of dedicated user–network interfaces (UNIs), with a high degree of transparency. EVPL provides a point-to-point or point-to-multipoint connection between a pair of UNIs.

The services are categorized as an E-line service type, with an expectation of low frame delay, frame delay variation and frame loss ratio. EPL is implemented using a point-to-point EVC with no service multiplexing at each UNI (physical interface), i.e., all service frames at the UNI are mapped to a single EVC (a.k.a. all-to-one bundling).

Due to a high degree of transparency, EPL is often used to provide point-to-point transparent LAN service (TLS), where the service frame's header and payload are identical at both the source and destination UNI. Some implementations tunnel most Ethernet Layer 2 control protocols (L2CPs) except for some link-layer L2CPs such as IEEE 802.3x pause frames.

Unlike EPL, EVPL allows for service multiplexing, i.e., multiple EVCs or Ethernet services per UNI. The other difference between the EVPL and EPL is the degree of transparency: while EPL is highly transparent, filtering only the pause frames, EVPL is required to either peer or drop most of the Layer 2 control protocols.

### Ethernet Virtual Private LAN

**Ethernet Virtual Private LAN** (EVP-LAN) is a multipoint-to-multipoint Ethernet Virtual Connection defined by the MEF — a Carrier Ethernet equivalent of Virtual Private LAN Service (VPLS) or Transparent LAN Services. EVP-LAN enables any-to-any communication between all customer locations associated with the customer's Ethernet Virtual Connections (EVC). It is categorized as an E-LAN service type, with an expectation of low Frame Delay, Frame Delay Variation and Frame Loss Ratio. Service multiplexing is allowed at the UNI and EVPL and EVP-LAN service types may share the same port. CE-VLAN IDs are maintained across the network.

## Transport of Ethernet services

The MEF does not specify how Ethernet services are to be provided in a carrier network. Despite the advantages described above, Ethernet has traditionally had a number of limitations in the WAN application. The "bridge" and "spanning tree" concepts described above do not scale to large international networks. Moreover, Ethernet has lacked some of the dependability features necessary in this application (in particular, mechanisms to isolate one customer's traffic from another, to measure performance of a customer service instance, and to rapidly detect and repair failures in large networks). Because of these limitations, and because of the need to make use of pre-existing equipment, Ethernet services have been carried across wide area networks using other technologies. Two types of technology have been widely used, while a third (Carrier-Ethernet transport) is rapidly emerging as a viable and logical option for Carrier-Ethernet services.

### Ethernet over SDH/SONET

Point-to-point Ethernet links are carried over SDH/SONET networks, making use of virtual concatenation (ITU-T G.707) and LCAS (Link Capacity Adjustment Scheme - ITU-T G.7042) to create an appropriate size carrier bundle, of the Generic Framing Procedure of SDH equipment, and takes advantage of the management and recovery features of SDH to provide high availability and resilience to failures.

### Ethernet over MPLS

Ethernet services are carried over IP/MPLS networks making use of a wide range of IP-related protocols. Ethernet links are transported as "pseudowires" using MPLS label-switched paths (LSPs) inside an outer MPLS "tunnel". This strategy can support both point-to-point (Virtual Private Wire Service - VPWS) and multipoint (Virtual Private LAN service - VPLS) services, and has recently achieved significant deployment in routed networks. It makes use of a number of basic transport protocols, including SDH and (increasingly) Ethernet.

### Ethernet over Carrier-Ethernet Transport (CET)

Proponents of Carrier-Class Ethernet argue Ethernet is the best for Metro Area Networks because all data traffic originates as Ethernet. Ethernet's ubiquitous presence in the LANs worldwide drives down the cost of Ethernet as a technology. Thus, the use of Ethernet in a metro network allows service providers to take advantage of volumes that a much larger enterprise segment commands. Carrier-Ethernet Transport (CET) usually involves an evolution of conventional Ethernet and comprises multiple technology components. Provider Backbone Bridges (PBB) provides the scalability and a secure demarcation, while Provider Backbone Bridge Traffic Engineering (PBB-TE, commonly called PBT) provides for traffic-engineering and an effective transport for protected Ethernet services. Connectivity-Fault Management (CFM-OAM) provides the much-required OAM that makes Ethernet carrier grade.

## Carrier Ethernet demarcation

Carrier Ethernet demarcation is a key element in Carrier Ethernet services and transport networks for business, wholesale and mobile backhaul applications, as it enables service providers to extend their control over the entire service path, starting from the hand off points. This is achieved by connecting customer premises equipment (CPE) to the network with provider-owned demarcation devices that are deployed at customer locations, thereby enabling a clear separation between the user and provider networks.

Carrier Ethernet demarcation devices (EDD) are required to support services, such as Ethernet Private Line (EPL), Ethernet Virtual Private Line (EVPL or E-LAN), and Ethernet Virtual Private Tree (E-Tree), as specified by the MEF. Such support needs to include service level agreement (SLA) management capabilities, with consistent performance over fiber, DSL, bonded PDH, and SDH/SONET access lines. As a result, must-have Carrier Ethernet demarcation features include sophisticated traffic management and hierarchical quality of service (QoS) mechanisms, standard end-to-end operations, administration and maintenance (OAM) and performance monitoring, extensive fault management and diagnostics, and SDH/SONET-like resiliency to reduce service provider operating costs and capital expenses.

## Carrier Ethernet technologies

The industry has made a concerted effort to resolve the limitations of Ethernet in the WAN described above, so as to allow the use of "native" Ethernet technologies by network providers. The key roles have been played by the Institute of Electrical and Electronics Engineers (IEEE) 802.1 and 802.3 standards committees. IEEE 802.1 has addressed the scalability and management issues in the standards for Provider Bridges (802.1ad) and Provider Backbone Bridges (802.1ah). These standards allow for Ethernet networks of planetary scale. Associated standards (IEEE 802.1ag, and related ITU-T standard Y.1731) provide Operations and Maintenance (OAM) capabilities allowing connectivity verification, rapid recovery, and performance measurement. Current work on PBB-TE (802.1Qay: Provider Backbone Bridging-Traffic Engineering) is allowing such an Ethernet to be controlled by an external control or management application (for example, a network management application or a transport control plane such as GMPLS (IETF RFC 3945)), so as to allow the full range of traffic engineering policies and strategies to a network provider.

The IEEE 802.3 Working Group in close cooperation with the ITU have been working to simplify the transport of 40G and 100G technologies being developed by both bodies: 802.3 for LAN and ITU for the OTN. The OIF and the Ethernet Alliance have also been working cooperatively with their members to enable future enhancements to Ethernet for the WAN while looking to the future speed of Ethernet technologies and services.
