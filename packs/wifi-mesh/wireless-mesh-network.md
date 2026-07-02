---
title: "Wireless mesh network"
source: https://en.wikipedia.org/wiki/Wireless_mesh_network
domain: wifi-mesh
license: CC-BY-SA-4.0
tags: wi-fi mesh, wireless mesh network, self-healing wireless, multi-hop wireless
fetched: 2026-07-02
---

# Wireless mesh network

A **wireless mesh network** (**WMN**) is a communications network made up of radio nodes organized in a mesh topology. It can also be a form of wireless ad hoc network.

A **mesh** refers to rich interconnection among devices or nodes. Wireless mesh networks often consist of mesh clients, mesh routers and gateways. Mobility of nodes is less frequent. If nodes constantly or frequently move, the mesh spends more time updating routes than delivering data. In a wireless mesh network, topology tends to be more static, so that routes computation can converge and delivery of data to their destinations can occur. Hence, this is a low-mobility centralized form of wireless ad hoc network. Also, because it sometimes relies on static nodes to act as gateways, it is not a truly all-wireless ad hoc network.

Mesh clients are often laptops, cell phones, and other wireless devices. Mesh routers forward traffic to and from the gateways, which may or may not be connected to the Internet. The coverage area of all radio nodes working as a single network is sometimes called a mesh cloud. Access to this mesh cloud depends on the radio nodes working together to create a radio network. A mesh network is reliable and offers redundancy. When one node can no longer operate, the rest of the nodes can still communicate with each other, directly or through one or more intermediate nodes. Wireless mesh networks can self form and self heal. Wireless mesh networks work with different wireless technologies including 802.11, 802.15, 802.16, cellular technologies and need not be restricted to any one technology or protocol.

## History

Wireless mesh radio networks were originally developed for military applications, such that every node could dynamically serve as a router for every other node. In that way, even in the event of a failure of some nodes, the remaining nodes could continue to communicate with each other, and, if necessary, serve as uplinks for the other nodes.

Early wireless mesh network nodes had a single half-duplex radio that, at any one instant, could either transmit or receive, but not both at the same time. This was accompanied by the development of shared mesh networks. This was subsequently superseded by more complex radio hardware that could receive packets from an upstream node and transmit packets to a downstream node simultaneously (on a different frequency or a different CDMA channel). This allowed the development of switched mesh networks. As the size, cost, and power requirements of radios declined further, nodes could be cost-effectively equipped with multiple radios. This, in turn, permitted each radio to handle a different function, for instance, one radio for client access, and another for backhaul services.

Work in this field has been aided by the use of game theory methods to analyze strategies for the allocation of resources and routing of packets.

## Features

### Architecture

Wireless mesh architecture is a first step towards providing cost effective and low mobility over a specific coverage area. Wireless mesh infrastructure is, in effect, a network of routers minus the cabling between nodes. It is built of peer radio devices that do not have to be cabled to a wired port like traditional WLAN access points (AP) do. Mesh infrastructure carries data over large distances by splitting the distance into a series of short hops. Intermediate nodes not only boost the signal, but cooperatively pass data from point A to point B by making forwarding decisions based on their knowledge of the network, i.e. perform routing by first deriving the topology of the network.

Wireless mesh networks is a relatively "stable-topology" network except for the occasional failure of nodes or addition of new nodes. The path of traffic, being aggregated from a large number of end users, changes infrequently. Practically all the traffic in an infrastructure mesh network is either forwarded to or from a gateway, while in wireless ad hoc networks or client mesh networks the traffic flows between arbitrary pairs of nodes.

If rate of mobility among nodes are high, i.e., link breaks happen frequently, wireless mesh networks start to break down and have low communication performance.

### Management

This type of infrastructure can be decentralized (with no central server) or centrally managed (with a central server). Both are relatively inexpensive, and can be very reliable and resilient, as each node needs only transmit as far as the next node. Nodes act as routers to transmit data from nearby nodes to peers that are too far away to reach in a single hop, resulting in a network that can span larger distances. The topology of a mesh network must be relatively stable, i.e., not too much mobility. If one node drops out of the network, due to hardware failure or any other reason, its neighbors can quickly find another route using a routing protocol.

### Applications

Mesh networks may involve either fixed or mobile devices. The solutions are as diverse as communication needs, for example in difficult environments such as emergency situations, tunnels, oil rigs, battlefield surveillance, high-speed mobile-video applications on board public transport, real-time racing-car telemetry, or self-organizing Internet access for communities. An important possible application for wireless mesh networks is VoIP. By using a quality of service scheme, the wireless mesh may support routing local telephone calls through the mesh. Most applications in wireless mesh networks are similar to those in wireless ad hoc networks.

Some current applications:

- U.S. military forces are now using wireless mesh networking to connect their computers, mainly ruggedized laptops, in field operations. They specifically use forms of mobile ad hoc network (MANET) using a range of military protocols. See mobile ad hoc network § Army tactical MANETs.
- Electric smart meters now being deployed on residences, transfer their readings from one to another and eventually to the central office for billing, without the need for human meter readers or the need to connect the meters with cables.
- The laptops in the One Laptop per Child program use wireless mesh networking to enable students to exchange files and get on the Internet even though they lack wired or cell phone or other physical connections in their area.
- Smart home devices such as Google Wi-Fi, Google Nest Wi-Fi, and Google OnHub support Wi-Fi mesh (i.e., Wi-Fi ad hoc) networking. Several manufacturers of Wi-Fi routers began offering mesh routers for home use in the mid-2010s.
- Wireless mesh networks can be used to overcome gaps in cellular coverage for a vehicle tracking system. In applications such as fleet management, vehicles often travel through remote areas where a consistent GSM/cellular signal is not available, preventing telemetry data from being transmitted in real-time. A mesh network allows vehicles to act as mobile nodes. If one vehicle is out of cellular range, its GPS tracking unit can transmit its vehicle location data to a nearby vehicle that is in range. That second vehicle then acts as a relay, forwarding the data to the central server. This ensures that a continuous track and trace record is maintained, even in areas with poor connectivity.
- Some communications satellite constellations operate as a mesh network, with wireless links between adjacent satellites. Calls between two satellite phones are routed through the mesh, from one satellite to another across the constellation, without having to go through an earth station. This makes for a shorter travel distance for the signal, reducing latency, and also allows for the constellation to operate with far fewer earth stations than would be required for an equal number of traditional communications satellites. The Iridium satellite constellation, consists of 66 active satellites in a polar orbit and operates as a mesh network providing global coverage.

### Operation

The principle is similar to the way packets travel around the wired Internet – data hops from one device to another until it eventually reaches its destination. Dynamic routing algorithms implemented in each device allow this to happen. To implement such dynamic routing protocols, each device needs to communicate routing information to other devices in the network. Each device then determines what to do with the data it receives – either pass it on to the next device or keep it, depending on the protocol. The routing algorithm used should attempt to always ensure that the data takes the most appropriate (fastest) route to its destination.

### Multi-radio mesh

Multi-radio mesh refers to having different radios operating at different frequencies to interconnect nodes in a mesh. This means there is a unique frequency used for each wireless hop and thus a dedicated CSMA collision domain. With more radio bands, communication throughput is likely to increase as a result of more available communication channels. This is similar to providing dual or multiple radio paths to transmit and receive data.

### Research topics

One of the more often cited papers on wireless mesh networks identified the following areas as open research problems in 2005:

**New modulation schemes**

To achieve higher transmission rate requires new wideband transmission schemes other than

OFDM

and

UWB

.

**Advanced antenna processing**

Advanced antenna processing including

directional

,

smart

and

multiple antenna

technologies is further investigated, since their complexity and cost are still too high for wide commercialization.

**Flexible spectrum management**

Tremendous efforts on research of frequency-agile techniques are being performed for increased efficiency.

**Cross-layer optimization**

Cross-layer research is a popular current research topic where information is shared between different communications layers to increase the knowledge and current state of the network. This could facilitate development of new and more efficient protocols. A joint protocol that addresses various design problems—routing, scheduling, channel assignment etc.—can achieve higher performance since these problems are strongly co-related.

Note that careless cross-layer design can lead to code that is difficult to maintain and extend.

**Software-defined wireless networking**

Centralized, distributed, or hybrid? - In

a new SDN architecture for WMNs is explored that eliminates the need for multi-hop flooding of route information and therefore enables WMNs to easily expand. The key idea is to split network control and data forwarding by using two separate frequency bands. The forwarding nodes and the SDN controller exchange link-state information and other network control signaling in one of the bands, while actual data forwarding takes place in the other band.

**Security**

A WMN can be seen as a group of nodes (clients or routers) that cooperate to provide connectivity. Such an

open architecture

, where clients serve as routers to forward data packets, is exposed to many types of attacks that can interrupt the whole network and cause denial of service (DoS) or Distributed Denial of Service (DDoS).

## Examples

A number of wireless community networks have been started as grassroots projects across the world at various points in time.

Other projects, often proprietary or tied to a single institution, are:

- ALOHAnet was first used in Hawaii in 1971 to connect the islands.
- Amateur radio operators began experimenting with VHF and later UHF digital communications networks in Canada in 1978 and the US in 1980. By 1984, the volunteer-operated Amateur Packet Radio Network (AMPRNet) of 'digipeaters' spanned most of North America. The emerging network allowed a licensed operator using merely an early laptop computer such as TRS-80 Model 100 and compatible handheld FM transceiver operating in the 1.25-meter band or 2-meter band to accomplish wireless transcontinental digital communications. With the development of the Internet, portals into and out of other IP networks facilitated 'tunnels' to reach packet networks in other parts of the world.
- In 1998–1999, a field implementation of a campus-wide wireless network using 802.11 WaveLAN 2.4 GHz wireless interface on several laptops was successfully completed. Several real applications, mobility and data transmissions were made.
- Mesh networks were useful for the military market because of the radio capability, and because not all military missions have frequently moving nodes. The Pentagon launched the DoD JTRS program in 1997, with an ambition to use software to control radio functions - such as frequency, bandwidth, modulation and security previously baked into the hardware. This approach would allow the DoD to build a family of radios with a common software core, capable of handling functions that were previously split among separate hardware-based radios: VHF voice radios for infantry units; UHF voice radios for air-to-air and ground-to-air communications; long-range HF radios for ships and ground troops; and a wideband radio capable of transmitting data at megabit speeds across a battlefield. However, JTRS program was shut down in 2012 by the US Army because the radios made by Boeing had a 75% failure rate.
- Amazon eero is a Wi-Fi mesh networking system designed for use in homes and small businesses.
- Google Home and Google Nest Wifi support Wi-Fi mesh networking.
- In rural Catalonia, Guifi.net was developed in 2004 as a response to the lack of broadband Internet, where commercial Internet providers weren't providing a connection or a very poor one. Nowadays with more than 30,000 nodes it is only halfway a fully connected network, but following a peer to peer agreement it remained an open, free and neutral network with extensive redundancy.
- In 2004, TRW Inc. engineers from Carson, California, successfully tested a multi-node mesh wireless network using 802.11a/b/g radios on several high speed laptops running Linux, with new features such as route precedence and preemption capability, adding different priorities to traffic service class during packet scheduling and routing, and quality of service. Their work concluded that data rate can be greatly enhanced using MIMO technology at the radio front end to provide multiple spatial paths.
- Zigbee digital radios are incorporated into some consumer appliances, including battery-powered appliances. Zigbee radios spontaneously organize a mesh network, using specific routing algorithms; transmission and reception are synchronized. This means the radios can be off much of the time, and thus conserve power. Zigbee is for low power low bandwidth application scenarios.
- Thread is a consumer wireless networking protocol built on open standards and IPv6/6LoWPAN protocols. Thread's features include a secure and reliable mesh network with no single point of failure, simple connectivity and low power. Thread networks are easy to set up and secure to use with banking-class encryption to close security holes that exist in other wireless protocols. In 2014 Google Inc's Nest Labs announced a working group with the companies Samsung, ARM Holdings, Freescale, Silicon Labs, Big Ass Fans and the lock company Yale to promote Thread.
- In early 2007, the US-based firm Meraki launched a mini wireless mesh router. The 802.11 radio within the Meraki Mini has been optimized for long-distance communication, providing coverage over 250 metres. In contrast to multi-radio long-range mesh networks with tree-based topologies and their advantages in O(n) routing, the Maraki had only one radio, which it used for both client access and backhaul traffic. In 2012, Meraki was acquired by Cisco.
- The Naval Postgraduate School, Monterey CA, demonstrated such wireless mesh networks for border security. In a pilot system, aerial cameras kept aloft by balloons relayed real time high resolution video to ground personnel via a mesh network.
- SPAWAR, a division of the US Navy, is prototyping and testing a scalable, secure Disruption Tolerant Mesh Network to protect strategic military assets, both stationary and mobile. Machine control applications, running on the mesh nodes, "take over", when Internet connectivity is lost. Use cases include Internet of Things e.g. smart drone swarms.
- An MIT Media Lab project has developed the XO-1 laptop or "OLPC" (One Laptop per Child) which is intended for disadvantaged schools in developing nations and uses mesh networking (based on the IEEE 802.11s standard) to create a robust and inexpensive infrastructure. The instantaneous connections made by the laptops are claimed by the project to reduce the need for an external infrastructure such as the Internet to reach all areas, because a connected node could share the connection with nodes nearby. A similar concept has also been implemented by Greenpacket with its application called SONbuddy.
- In Cambridge, UK, on 3 June 2006, mesh networking was used at the “Strawberry Fair” to run mobile live television, radio and Internet services to an estimated 80,000 people.
- Broadband-Hamnet, a mesh networking project used in amateur radio, is "a high-speed, self-discovering, self-configuring, fault-tolerant, wireless computer network" with very low power consumption and a focus on emergency communication.
- The Champaign-Urbana Community Wireless Network (CUWiN) project is developing mesh networking software based on open source implementations of the Hazy-Sighted Link State Routing Protocol and Expected Transmission Count metric. Additionally, the Wireless Networking Group in the University of Illinois at Urbana-Champaign are developing a multichannel, multi-radio wireless mesh testbed, called Net-X as a proof of concept implementation of some of the multichannel protocols being developed in that group. The implementations are based on an architecture that allows some of the radios to switch channels to maintain network connectivity, and includes protocols for channel allocation and routing.
- FabFi is an open-source, city-scale, wireless mesh networking system originally developed in 2009 in Jalalabad, Afghanistan to provide high-speed Internet to parts of the city and designed for high performance across multiple hops. It is an inexpensive framework for sharing wireless Internet from a central provider across a town or city. A second larger implementation followed a year later near Nairobi, Kenya with a freemium pay model to support network growth. Both projects were undertaken by the Fablab users of the respective cities.
- SMesh is an 802.11 multi-hop wireless mesh network developed by the Distributed System and Networks Lab at Johns Hopkins University. A fast handoff scheme allows mobile clients to roam in the network without interruption in connectivity, a feature suitable for real-time applications, such as VoIP.
- Many mesh networks operate across multiple radio bands. For example, Firetide and Wave Relay mesh networks have the option to communicate node to node on 5.2 GHz or 5.8 GHz, but communicate node to client on 2.4 GHz (802.11). This is accomplished using software-defined radio (SDR).
- The SolarMESH project examined the potential of powering 802.11-based mesh networks using solar power and rechargeable batteries. Legacy 802.11 access points were found to be inadequate due to the requirement that they be continuously powered. The IEEE 802.11s standardization efforts are considering power save options, but solar-powered applications might involve single radio nodes where relay-link power saving will be inapplicable.
- The WING project (sponsored by the Italian Ministry of university and Research and led by CREATE-NET and Technion) developed a set of novel algorithms and protocols for enabling wireless mesh networks as the standard access architecture for next generation Internet. Particular focus has been given to interference and traffic-aware channel assignment, multi-radio/multi-interface support, and opportunistic scheduling and traffic aggregation in highly volatile environments.
- WiBACK Wireless Backhaul Technology has been developed by the Fraunhofer Institute for Open Communication Systems (FOKUS) in Berlin. Powered by solar cells and designed to support all existing wireless technologies, networks are due to be rolled out to several countries in sub-Saharan Africa in summer 2012.
- Recent standards for wired communications have also incorporated concepts from Mesh Networking. An example is ITU-T G.hn, a standard that specifies a high-speed (up to 1 Gbit/s) local area network using existing home wiring (power lines, phone lines and coaxial cables). In noisy environments such as power lines (where signals can be heavily attenuated and corrupted by noise), it is common that mutual visibility between devices in a network is not complete. In those situations, one of the nodes has to act as a relay and forward messages between those nodes that cannot communicate directly, effectively creating a "relaying" network. In G.hn, relaying is performed at the data link layer.
- Meshtastic and MeshCore using LoRa in ISM bands.

## Protocols

### Routing protocols

There are more than 70 competing schemes for routing packets across mesh networks. Some of these include:

- Associativity-Based Routing (ABR)
- AODV (Ad hoc On-Demand Distance Vector)
- B.A.T.M.A.N. (Better Approach To Mobile Ad hoc Networking)
- Babel (protocol) (a distance-vector routing protocol for IPv6 and IPv4 with fast convergence properties)
- Dynamic NIx-Vector Routing|DNVR
- DSDV (Destination-Sequenced Distance-Vector Routing)
- DSR (Dynamic Source Routing)
- HSLS (Hazy-Sighted Link State)
- HWMP (Hybrid Wireless Mesh Protocol, the default mandatory routing protocol of IEEE 802.11s)
- *Infrastructure Wireless Mesh Protocol* (IWMP) for Infrastructure Mesh Networks by GRECO UFPB-Brazil
- ODMRP (On-Demand Multicast Routing Protocol)
- OLSR (Optimized Link State Routing protocol)
- OORP (OrderOne Routing Protocol) (OrderOne Networks Routing Protocol)
- OSPF (Open Shortest Path First Routing)
- Routing Protocol for Low-Power and Lossy Networks (IETF ROLL RPL protocol, RFC 6550)
- PWRP (Predictive Wireless Routing Protocol)
- TORA (Temporally-Ordered Routing Algorithm)
- ZRP (Zone Routing Protocol)

The IEEE has developed a set of standards under the title 802.11s.

A less thorough list can be found at list of ad hoc routing protocols.

### Autoconfiguration protocols

Standard autoconfiguration protocols, such as DHCP or IPv6 stateless autoconfiguration may be used over mesh networks.

Mesh network specific autoconfiguration protocols include:

- Ad Hoc Configuration Protocol (AHCP)
- Proactive Autoconfiguration (Proactive Autoconfiguration Protocol)
- Dynamic WMN Configuration Protocol (DWCP)

## Communities and providers

- Anyfi
- AWMN (Athens [Greece] Wireless Metropolitan Network)
- CUWiN
- Freifunk (DE) / FunkFeuer (AT) / OpenWireless (CH)
- Firechat
- Firetide
- Guifi.net
- Netsukuku
- Ninux (IT)
- NYC Mesh
- Red Hook Wi-Fi
