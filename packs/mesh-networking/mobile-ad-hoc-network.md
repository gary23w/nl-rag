---
title: "Wireless ad hoc network"
source: https://en.wikipedia.org/wiki/Mobile_ad_hoc_network
domain: mesh-networking
license: CC-BY-SA-4.0
tags: mesh networking, wireless mesh network, self-healing topology, multi-hop routing
fetched: 2026-07-02
---

# Wireless ad hoc network

(Redirected from

Mobile ad hoc network

)

A **wireless ad hoc network** (**WANET**) or **mobile ad hoc network** (**MANET**) is a decentralized type of wireless network. The network is ad hoc because it does not rely on a pre-existing infrastructure, such as routers or wireless access points. Instead, each node participates in routing by forwarding data for other nodes. The determination of which nodes forward data is made dynamically on the basis of network connectivity and the routing algorithm in use.

Such wireless networks lack the complexities of infrastructure setup and administration, enabling devices to create and join networks "on the fly".

Each device in a MANET is free to move independently in any direction, and will therefore change its links to other devices frequently. Each must forward traffic unrelated to its own use, and therefore be a router. The primary challenge in building a MANET is equipping each device to continuously maintain the information required to properly route traffic. This becomes harder as the scale of the MANET increases due to (1) the desire to route packets to/through every other node, (2) the percentage of overhead traffic needed to maintain real-time routing status, (3) each node has its own goodput to route independent and unaware of others needs, and 4) all must share limited communication bandwidth, such as a slice of radio spectrum.

Such networks may operate by themselves or may be connected to the larger Internet. They may contain one or multiple and different transceivers between nodes. This results in a highly dynamic, autonomous topology. MANETs usually have a routable networking environment on top of a link layer ad hoc network.

## History

### Packet radio

The earliest wireless data network was called PRNET, the packet radio network, and was sponsored by Defense Advanced Research Projects Agency (DARPA) in the early 1970s. Bolt, Beranek and Newman Inc. (BBN) and SRI International designed, built, and experimented with these earliest systems. Experimenters included Robert Kahn, Jerry Burchfiel, and Ray Tomlinson. Similar experiments took place in the amateur radio community with the x25 protocol. These early packet radio systems predated the Internet, and indeed were part of the motivation of the original Internet Protocol suite. Later DARPA experiments included the Survivable Radio Network (SURAN) project, which took place in the 1980s. A successor to these systems was fielded in the mid-1990s for the US Army, and later other nations, as the Near-term digital radio.

Another third wave of academic and research activity started in the mid-1990s with the advent of inexpensive 802.11 radio cards for personal computers. Current wireless ad hoc networks are designed primarily for military utility. Problems with packet radios are: (1) bulky elements, (2) slow data rate, (3) unable to maintain links if mobility is high. The project did not proceed much further until the early 1990s when wireless ad hoc networks were born.

### Early work on MANET

The growth of laptops and 802.11/Wi-Fi wireless networking have made MANETs a popular research topic since the mid-1990s. Many academic papers evaluate protocols and their abilities, assuming varying degrees of mobility within a bounded space, usually with all nodes within a few hops of each other. Different protocols are then evaluated based on measures such as the packet drop rate, the overhead introduced by the routing protocol, end-to-end packet delays, network throughput, ability to scale, etc.

In the early 1990s, Charles Perkins from SUN Microsystems USA, and Chai Keong Toh from Cambridge University separately started to work on a different Internet, that of a wireless ad hoc network. Perkins was working on the dynamic addressing issues. Toh worked on a new routing protocol, which was known as ABR – associativity-based routing. Perkins eventually proposed DSDV – Destination Sequence Distance Vector routing, which was based on distributed distance vector routing. Toh's proposal was an on-demand based routing, i.e. routes are discovered on-the-fly in real-time as and when needed. ABR was submitted to IETF as RFCs. ABR was implemented successfully into Linux OS on Lucent WaveLAN 802.11a enabled laptops and a practical ad hoc mobile network was therefore proven to be possible in 1999. Another routing protocol known as AODV was subsequently introduced and later proven and implemented in 2005. In 2007, David Johnson and Dave Maltz proposed DSR – Dynamic Source Routing.

## Applications

The decentralized nature of wireless ad hoc networks makes them suitable for a variety of applications where central nodes can't be relied on and may improve the scalability of networks compared to wireless managed networks, though theoretical and practical limits to the overall capacity of such networks have been identified. Minimal configuration and quick deployment make ad hoc networks suitable for emergency situations like natural disasters or military conflicts. The presence of dynamic and adaptive routing protocols enables ad hoc networks to be formed quickly.

### Mobile ad hoc networks (MANETs)

A mobile ad hoc network (MANET) is a continuously self-configuring, self-organizing, infrastructure-less network of mobile devices connected without wires. It is sometimes known as "on-the-fly" networks or "spontaneous networks".

### Vehicular ad hoc networks (VANETs)

VANETs are used for communication between vehicles and roadside equipment. Intelligent vehicular ad hoc networks (InVANETs) are a kind of artificial intelligence that helps vehicles to behave in intelligent manners during vehicle-to-vehicle collisions, accidents. Vehicles are using radio waves to communicate with each other, creating communication networks instantly on-the-fly while vehicles move along roads. VANET needs to be secured with lightweight protocols.

### Smartphone ad hoc networks (SPANs)

A SPAN leverages existing hardware (primarily Wi-Fi and Bluetooth) and software (protocols) in commercially available smartphones to create peer-to-peer networks without relying on cellular carrier networks, wireless access points, or traditional network infrastructure. SPANs differ from traditional hub and spoke networks, such as Wi-Fi Direct, in that they support multi-hop relays and there is no notion of a group leader so peers can join and leave at will without destroying the network. Apple's iPhone with iOS version 7.0 and higher is capable of multi-peer ad hoc mesh networking.

### Wireless mesh networks

Mesh networks take their name from the topology of the resultant network. In a fully connected mesh, each node is connected to every other node, forming a "mesh". A partial mesh, by contrast, has a topology in which some nodes are not connected to others, although this term is seldom in use. Wireless ad hoc networks can take the form of a mesh networks or others. A wireless ad hoc network does not have fixed topology, and its connectivity among nodes is totally dependent on the behavior of the devices, their mobility patterns, distance with each other, etc. Hence, wireless mesh networks are a particular type of wireless ad hoc networks, with special emphasis on the resultant network topology. While some wireless mesh networks (particularly those within a home) have relatively infrequent mobility and thus infrequent link breaks, other more mobile mesh networks require frequent routing adjustments to account for lost links.

### Army tactical MANETs

Military or tactical MANETs are used by military units with emphasis on data rate, real-time requirement, fast re-routing during mobility, data security, radio range, and integration with existing systems. Common radio waveforms include the US Army's JTRS SRW and Silvus Technologies MN-MIMO Waveform (Mobile Networked MIMO),. Ad hoc mobile communications come in well to fulfill this need, especially its infrastructureless nature, fast deployment, and operation. Military MANETs are used by military units with an emphasis on rapid deployment, infrastructureless, all-wireless networks (no fixed radio towers), robustness (link breaks are no problem), security, range, and instant operation.

### Air Force UAV ad hoc networks

Flying ad hoc networks (FANETs) are composed of unmanned aerial vehicles, allowing great mobility and providing connectivity to remote areas.

Unmanned aerial vehicle, is an aircraft with no pilot on board. UAVs can be remotely controlled (i.e., flown by a pilot at a ground control station) or can fly autonomously based on pre-programmed flight plans. Civilian usage of UAV include modeling 3D terrains, package delivery (Logistics), etc.

UAVs have also been used by US Air Force for data collection and situation sensing, without risking the pilot in a foreign unfriendly environment. With wireless ad hoc network technology embedded into the UAVs, multiple UAVs can communicate with each other and work as a team, collaboratively to complete a task and mission. If a UAV is destroyed by an enemy, its data can be quickly offloaded wirelessly to other neighboring UAVs. The UAV ad hoc communication network is also sometimes referred to UAV instant sky network. More generally, aerial MANET in UAVs are now (as of 2021) successfully implemented and operational as mini tactical reconnaissance ISR UAVs like the BRAMOR C4EYE from Slovenia.

### Navy ad hoc networks

Navy ships traditionally use satellite communications and other maritime radios to communicate with each other or with ground station back on land. However, such communications are restricted by delays and limited bandwidth. Wireless ad hoc networks enable ship-area-networks to be formed while at sea, enabling high-speed wireless communications among ships, enhancing their sharing of imaging and multimedia data, and better co-ordination in battlefield operations. Some defense companies (such as Rockwell Collins, Silvus Technologies and Rohde & Schwartz) have produced products that enhance ship-to-ship and ship-to-shore communications.

### Sensor networks

Sensors are useful devices that collect information related to a specific parameter, such as noise, temperature, humidity, pressure, etc. Sensors are increasingly connected via wireless to allow large-scale collection of sensor data. With a large sample of sensor data, analytics processing can be used to make sense out of these data. The connectivity of wireless sensor networks rely on the principles behind wireless ad hoc networks, since sensors can now be deploy without any fixed radio towers, and they can now form networks on-the-fly. "Smart Dust" was one of the early projects done at U C Berkeley, where tiny radios were used to interconnect smart dust. More recently, mobile wireless sensor networks (MWSNs) have also become an area of academic interest.

### Robotics

Efforts have been made to co-ordinate and control a group of robots to undertake collaborative work to complete a task. Centralized control is often based on a "star" approach, where robots take turns to talk to the controller station. However, with wireless ad hoc networks, robots can form a communication network on-the-fly, i.e., robots can now "talk" to each other and collaborate in a distributed fashion. With a network of robots, the robots can communicate among themselves, share local information, and distributively decide how to resolve a task in the most effective and efficient way.

### Disaster response

Another civilian use of wireless ad hoc network is for public safety. At times of disasters (floods, storms, earthquakes, fires, etc.), a quick and instant wireless communication network is necessary. Especially at times of earthquakes when radio towers had collapsed or were destroyed, wireless ad hoc networks can be formed independently. Firefighters and rescue workers can use ad hoc networks to communicate and rescue those injured. Commercial radios with such capability are available on the market.

### Hospital ad hoc network

Wireless ad hoc networks allow sensors, videos, instruments, and other devices to be deployed and interconnected wirelessly for clinic and hospital patient monitoring, doctor and nurses alert notification, and also making senses of such data quickly at fusion points, so that lives can be saved.

### Data monitoring and mining

MANETS can be used for facilitating the collection of sensor data for data mining for a variety of applications such as air pollution monitoring and different types of architectures can be used for such applications. A key characteristic of such applications is that nearby sensor nodes monitoring an environmental feature typically register similar values. This kind of data redundancy due to the spatial correlation between sensor observations inspires the techniques for in-network data aggregation and mining. By measuring the spatial correlation between data sampled by different sensors, a wide class of specialized algorithms can be developed to develop more efficient spatial data mining algorithms as well as more efficient routing strategies. Also, researchers have developed performance models for MANET to apply queueing theory.

## Challenges

Several books and works have revealed the technical and research challenges facing wireless ad hoc networks or MANETs. The advantages for users, the technical difficulties in implementation, and the side effect on radio spectrum pollution can be briefly summarized below:

### Advantages for users

The obvious appeal of MANETs is that the network is decentralised and nodes/devices are mobile, that is to say there is no fixed infrastructure which provides the possibility for numerous applications in different areas such as environmental monitoring, disaster relief and military communications. Since the early 2000s, interest in MANETs has greatly increased which, in part, is due to the fact mobility can improve network capacity, shown by Grossglauser and Tse along with the introduction of new technologies.

One main advantage to a decentralised network is that they are typically more robust than centralised networks due to the multi-hop fashion in which information is relayed. For example, in the cellular network setting, a drop in coverage occurs if a base station stops working, however the chance of a single point of failure in a MANET is reduced significantly since the data can take multiple paths. Since the MANET architecture evolves with time it has the potential to resolve issues such as isolation/disconnection from the network. Further advantages of MANETS over networks with a fixed topology include flexibility (an ad hoc network can be created anywhere with mobile devices), scalability (adding nodes to the network is easy) and lower administration costs (no need to build an infrastructure first).

### Implementation difficulties

With a time evolving network it is clear we should expect variations in network performance due to no fixed architecture (no fixed connections). Furthermore, since network topology determines interference and thus connectivity, the mobility pattern of devices within the network will impact on network performance, possibly resulting in data having to be resent a lot of times (increased delay) and finally allocation of network resources such as power remains unclear. Finally, finding a model that accurately represents human mobility whilst remaining mathematically tractable remains an open problem due to the large range of factors that influence it. Some typical models used include the random walk, random waypoint and levy flight models.

### Side effects

- Use of unlicensed frequency spectrum, contributing to radio spectrum pollution.

## Radios and modulation

Wireless ad hoc networks can operate over different types of radios. All radios use modulation to move information over a certain bandwidth of radio frequencies. Given the need to move large amounts of information quickly over long distances, a MANET radio channel ideally has large bandwidth (e.g. amount of radio spectrum), lower frequencies, and higher power. Given the desire to communicate with many other nodes ideally simultaneously, many channels are needed. Given radio spectrum is shared and regulated, there is less bandwidth available at lower frequencies. Processing many radio channels requires many resources. Given the need for mobility, small size and lower power consumption are very important. Picking a MANET radio and modulation has many trade-offs; many start with the specific frequency and bandwidth they are allowed to use.

Radios can be UHF (300 – 3000 MHz), SHF (3 – 30 GHz), and EHF (30 – 300 GHz). Wi-Fi ad hoc uses the unlicensed ISM 2.4 GHz radios. They can also be used on 5.8 GHz radios.

The higher the frequency, such as those of 300 GHz, absorption of the signal will be more predominant. Army tactical radios usually employ a variety of UHF and SHF radios, including those of VHF to provide a variety of communication modes. At the 800, 900, 1200, 1800 MHz range, cellular radios are predominant. Some cellular radios use ad hoc communications to extend cellular range to areas and devices not reachable by the cellular base station.

Next generation Wi-Fi known as 802.11ax provides low delay, high capacity (up to 10 Gbit/s) and low packet loss rate, offering 12 streams – 8 streams at 5 GHz and 4 streams at 2.4 GHz. IEEE 802.11ax uses 8x8 MU-MIMO, OFDMA, and 80 MHz channels. Hence, 802.11ax has the ability to form high capacity Wi-Fi ad hoc networks.

At 60 GHz, there is another form of Wi-Fi known as WiGi – wireless gigabit. This has the ability to offer up to 7 Gbit/s throughput. Currently, WiGi is targeted to work with 5G cellular networks.

Circa 2020, the general consensus finds the 'best' modulation for moving information over higher frequency waves to be orthogonal frequency-division multiplexing, as used in 4G LTE, 5G, and Wi-Fi.

## Protocol stack

The challenges affecting MANETs span from various layers of the OSI protocol stack. The media access layer (MAC) has to be improved to resolve collisions and hidden terminal problems. The network layer routing protocol has to be improved to resolve dynamically changing network topologies and broken routes. The transport layer protocol has to be improved to handle lost or broken connections. The session layer protocol has to deal with discovery of servers and services.

A major limitation with mobile nodes is that they have high mobility, causing links to be frequently broken and reestablished. Moreover, the bandwidth of a wireless channel is also limited, and nodes operate on limited battery power, which will eventually be exhausted. These factors make the design of a mobile ad hoc network challenging.

The cross-layer design deviates from the traditional network design approach in which each layer of the stack would be made to operate independently. The modified transmission power will help that node to dynamically vary its propagation range at the physical layer. This is because the propagation distance is always directly proportional to transmission power. This information is passed from the physical layer to the network layer so that it can take optimal decisions in routing protocols. A major advantage of this protocol is that it allows access of information between physical layer and top layers (MAC and network layer).

Some elements of the software stack were developed to allow code updates *in situ*, i.e., with the nodes embedded in their physical environment and without needing to bring the nodes back into the lab facility. Such software updating relied on epidemic mode of dissemination of information and had to be done both efficiently (few network transmissions) and fast.

## Routing

Routing in wireless ad hoc networks or MANETs generally falls into three categories, namely: proactive routing, reactive routing, and hybrid routing.

### Proactive routing

This type of protocols maintains fresh lists of destinations and their routes by periodically distributing routing tables throughout the network. The main disadvantages of such algorithms are:

- Respective amount of data for maintenance.
- Slow reaction on restructuring and failures.

Example: Optimized Link State Routing Protocol (OLSR)

#### Distance vector routing

As in a fix net nodes maintain routing tables. Distance-vector protocols are based on calculating the direction and distance to any link in a network. "Direction" usually means the next hop address and the exit interface. "Distance" is a measure of the cost to reach a certain node. The least cost route between any two nodes is the route with minimum distance. Each node maintains a vector (table) of minimum distance to every node. The cost of reaching a destination is calculated using various route metrics. RIP uses the hop count of the destination whereas IGRP takes into account other information such as node delay and available bandwidth.

### Reactive routing

This type of protocol finds a route based on user and traffic demand by flooding the network with Route Request or Discovery packets. The main disadvantages of such algorithms are:

- High latency time in route finding.
- Excessive flooding can lead to network clogging.

However, clustering can be used to limit flooding. The latency incurred during route discovery is not significant compared to periodic route update exchanges by all nodes in the network.

Example: Ad hoc On-Demand Distance Vector Routing (AODV)

#### Flooding

Is a simple routing algorithm in which every incoming packet is sent through every outgoing link except the one it arrived on. Flooding is used in bridging and in systems such as Usenet and peer-to-peer file sharing and as part of some routing protocols, including OSPF, DVMRP, and those used in wireless ad hoc networks.

### Hybrid routing

This type of protocol combines the advantages of *proactive* and *reactive routing*. The routing is initially established with some proactively prospected routes and then serves the demand from additionally activated nodes through reactive flooding. The choice of one or the other method requires predetermination for typical cases. The main disadvantages of such algorithms are:

1. Advantage depends on number of other nodes activated.
2. Reaction to traffic demand depends on gradient of traffic volume.

Example: Zone Routing Protocol (ZRP)

### Position-based routing

Position-based routing methods use information on the exact locations of the nodes. This information is obtained for example via a GPS receiver. Based on the exact location the best path between source and destination nodes can be determined.

Example: "Location-Aided Routing in mobile ad hoc networks" (LAR)

## Technical requirements for implementation

An ad hoc network is made up of multiple "nodes" connected by "links."

Links are influenced by the node's resources (e.g., transmitter power, computing power and memory) and behavioral properties (e.g., reliability), as well as link properties (e.g. length-of-link and signal loss, interference and noise). Since links can be connected or disconnected at any time, a functioning network must be able to cope with this dynamic restructuring, preferably in a way that is timely, efficient, reliable, robust, and scalable.

The network must allow any two nodes to communicate by relaying the information via other nodes. A "path" is a series of links that connects two nodes. Various routing methods use one or two paths between any two nodes; flooding methods use all or most of the available paths.

## Medium-access control

In most wireless ad hoc networks, the nodes compete for access to shared wireless medium, often resulting in collisions (interference). Collisions can be handled using centralized scheduling or distributed contention access protocols. Using cooperative wireless communications improves immunity to interference by having the destination node combine self-interference and other-node interference to improve decoding of the desired signals.

## Simulation

One key problem in wireless ad hoc networks is foreseeing the variety of possible situations that can occur. As a result, modeling and simulation (M&S) using extensive parameter sweeping and what-if analysis becomes an extremely important paradigm for use in ad hoc networks. One solution is the use of simulation tools like OPNET, NetSim or ns2. A comparative study of various simulators for VANETs reveal that factors such as constrained road topology, multi-path fading and roadside obstacles, traffic flow models, trip models, varying vehicular speed and mobility, traffic lights, traffic congestion, drivers' behavior, etc., have to be taken into consideration in the simulation process to reflect realistic conditions.

### Emulation testbed

In 2009, the U.S. Army Research Laboratory (ARL) and Naval Research Laboratory (NRL) developed a Mobile Ad-Hoc Network emulation testbed, where algorithms and applications were subjected to representative wireless network conditions. The testbed was based on a version of the "MANE" (Mobile Ad hoc Network Emulator) software originally developed by NRL.

### Mathematical models

The traditional model is the random geometric graph. Early work included simulating ad hoc mobile networks on sparse and densely connected topologies. Nodes are firstly scattered in a constrained physical space randomly. Each node then has a predefined fixed cell size (radio range). A node is said to be connected to another node if this neighbor is within its radio range. Nodes are then moved (migrated away) based on a random model, using random walk or brownian motion. Different mobility and number of nodes present yield different route length and hence different number of multi-hops.

These are graphs consisting of a set of nodes placed according to a point process in some usually bounded subset of the n-dimensional plane, mutually coupled according to a Boolean probability mass function of their spatial separation (see e.g. unit disk graphs). The connections between nodes may have different weights to model the difference in channel attenuations. One can then study network observables (such as connectivity, centrality or the degree distribution) from a graph-theoretic perspective. One can further study network protocols and algorithms to improve network throughput and fairness.

## Security

Most wireless ad hoc networks do not implement any network access control, leaving these networks vulnerable to resource consumption attacks where a malicious node injects packets into the network with the goal of depleting the resources of the nodes relaying the packets.

To thwart or prevent such attacks, it was necessary to employ authentication mechanisms that ensure that only authorized nodes can inject traffic into the network. Even with authentication, these networks are vulnerable to packet dropping or delaying attacks, whereby an intermediate node drops the packet or delays it, rather than promptly sending it to the next hop.

In a multicast and dynamic environment, establishing temporary 1:1 secure 'sessions' using PKI with every other node is not feasible (like is done with HTTPS, most VPNs, etc. at the transport layer). Instead, a common solution is to use pre-shared keys for symmetric, authenticated encryption at the link layer, for example MACsec using AES-256-GCM. With this method, every properly formatted packet received is authenticated then passed along for decryption or dropped. It also means the key(s) in each node must be changed more often and simultaneously (e.g. to avoid reusing an IV).

### Trust management

Trust establishment and management in MANETs face challenges due to resource constraints and the complex interdependency of networks. Managing trust in a MANET needs to consider the interactions between the composite cognitive, social, information and communication networks, and take into account the resource constraints (e.g., computing power, energy, bandwidth, time), and dynamics (e.g., topology changes, node mobility, node failure, propagation channel conditions).

Researchers of trust management in MANET suggested that such complex interactions require a composite trust metric that captures aspects of communications and social networks, and corresponding trust measurement, trust distribution, and trust management schemes.

Continuous monitoring of every node within a MANET is necessary for trust and reliability but difficult because it by definition is dis-continuous, 2) it requires input from the node itself and 3) from its 'nearby' peers.
