---
title: "Wireless sensor network"
source: https://en.wikipedia.org/wiki/Wireless_sensor_network
domain: lorawan-deep
license: CC-BY-SA-4.0
tags: lorawan protocol, lora wide-area network, lpwan networking, chirp spread spectrum radio
fetched: 2026-07-02
---

# Wireless sensor network

**Wireless sensor networks** (**WSNs**) refer to networks of spatially dispersed and dedicated sensors that monitor and record the physical conditions of the environment and forward the collected data to a central location. WSNs can measure environmental conditions such as temperature, sound, pollution levels, humidity and wind.

These are similar to wireless ad hoc networks in the sense that they rely on wireless connectivity and spontaneous formation of networks so that sensor data can be transported wirelessly. WSNs monitor physical conditions, such as temperature, sound, and pressure. Modern networks are bi-directional, both collecting data and enabling control of sensor activity.  The development of these networks was motivated by military applications such as battlefield surveillance. Such networks are used in industrial and consumer applications, such as industrial process monitoring and control and machine health monitoring and agriculture.

A WSN is built of "nodes" – from a few to hundreds or thousands, where each node is connected to other sensors. Each such node typically has several parts: a radio transceiver with an internal antenna or connection to an external antenna, a microcontroller, an electronic circuit for interfacing with the sensors and an energy source, usually a battery or an embedded form of energy harvesting. A sensor node might vary in size from a shoebox to (theoretically) a grain of dust, although microscopic dimensions have yet to be realized. Sensor node cost is similarly variable, ranging from a few to hundreds of dollars, depending on node sophistication. Size and cost constraints constrain resources such as energy, memory, computational speed and communications bandwidth. The topology of a WSN can vary from a simple star network to an advanced multi-hop wireless mesh network. Propagation can employ routing or flooding.

In computer science and telecommunications, wireless sensor networks are an active research area supporting many workshops and conferences, including the International Workshop on Embedded Networked Sensors (EmNetS), International Conference on Information Processing in Sensor Networks (IPSN), SenSys, MobiCom and European Conference on Wireless Sensor Networks (EWSN). As of 2010, wireless sensor networks had deployed approximately 120 million remote units worldwide.

## Application

### Area monitoring

Area monitoring is a common application of WSNs. In area monitoring, the WSN is deployed over a region where some phenomenon is to be monitored. A military example is the use of sensors to detect enemy intrusion; a civilian example is the geo-fencing of gas or oil pipelines.

### Health care monitoring

There are several types of sensor networks for medical applications: implanted, wearable, and environment-embedded. Implantable medical devices are those that are inserted inside the human body. Wearable devices are used on the body surface of a human or just at close proximity of the user. Environment-embedded systems employ sensors contained in the environment. Possible applications include body position measurement, location of persons, overall monitoring of ill patients in hospitals and at home. Devices embedded in the environment track the physical state of a person for continuous health diagnosis, using as input the data from a network of depth cameras, a sensing floor, or other similar devices. Body-area networks can collect information about an individual's health, fitness, and energy expenditure. In health care applications the privacy and authenticity of user data has prime importance. Especially due to the integration of sensor networks, with IoT, the user authentication becomes more challenging; however, a solution is presented in recent work.

### Habitat monitoring

Wireless sensor networks have been used to monitor various species and habitats, beginning with the Great Duck Island Deployment, including marmots, cane toads in Australia and zebras in Kenya.

### Environmental/Earth sensing

There are many applications in monitoring environmental parameters, examples of which are given below. They share the extra challenges of harsh environments and reduced power supply.

#### Air quality monitoring

Experiments have shown that personal exposure to air pollution in cities can vary a lot. Therefore, it is of interest to have higher temporal and spatial resolution of pollutants and particulates. For research purposes, wireless sensor networks have been deployed to monitor the concentration of dangerous gases for citizens (e.g., in London). However, sensors for gases and particulate matter suffer from high unit-to-unit variability, cross-sensitivities, and (concept) drift. Moreover, the quality of data is currently insufficient for trustworthy decision-making, as field calibration leads to unreliable measurement results, and frequent recalibration might be required. A possible solution could be blind calibration or the usage of mobile references.

#### Forest fire detection

A network of Sensor Nodes can be installed in a forest to detect when a fire has started. The nodes can be equipped with sensors to measure temperature, humidity and gases which are produced by fire in the trees or vegetation. The early detection is crucial for a successful action of the firefighters; thanks to Wireless Sensor Networks, the fire brigade will be able to know when a fire is started and how it is spreading.

#### Landslide detection

A landslide detection system makes use of a wireless sensor network to detect the slight movements of soil and changes in various parameters that may occur before or during a landslide. Through the data gathered it may be possible to know the impending occurrence of landslides long before it actually happens.

#### Water quality monitoring

Water quality monitoring involves analyzing water properties in dams, rivers, lakes and oceans, as well as underground water reserves. The use of many wireless distributed sensors enables the creation of a more accurate map of the water status, and allows the permanent deployment of monitoring stations in locations of difficult access, without the need of manual data retrieval.

#### Natural disaster prevention

Wireless sensor networks can be effective in preventing adverse consequences of natural disasters, like floods. Wireless nodes have been deployed successfully in rivers, where changes in water levels must be monitored in real time.

### Industrial monitoring

#### Machine health monitoring

Wireless sensor networks have been developed for machinery condition-based maintenance (CBM) as they offer significant cost savings and enable new functionality.

Wireless sensors can be placed in locations difficult or impossible to reach with a wired system, such as rotating machinery and untethered vehicles.

#### Data logging

Wireless sensor networks also are used for the collection of data for monitoring of environmental information. This can be as simple as monitoring the temperature in a fridge or the level of water in overflow tanks in nuclear power plants. The statistical information can then be used to show how systems have been working. The advantage of WSNs over conventional loggers is the "live" data feed that is possible.

#### Water/waste water monitoring

Monitoring the quality and level of water includes many activities such as checking the quality of underground or surface water and ensuring a country's water infrastructure for the benefit of both human and animal. It may be used to protect the wastage of water.

#### Structural health monitoring

WSN can be used to monitor the condition of civil infrastructure and related geo-physical processes close to real time, and over long periods through data logging, using appropriately interfaced sensors.

#### Wine production

Wireless sensor networks are used to monitor wine production, both in the field and the cellar.

### Threat detection

The Wide Area Tracking System (WATS) is a prototype network for detecting a ground-based nuclear device such as a nuclear "briefcase bomb". WATS is being developed at the Lawrence Livermore National Laboratory (LLNL). WATS would be made up of wireless gamma and neutron sensors connected through a communications network. Data picked up by the sensors undergoes "data fusion", which converts the information into easily interpreted forms; this data fusion is the most important aspect of the system.

The data fusion process occurs *within* the sensor network rather than at a centralized computer and is performed by a specially developed algorithm based on Bayesian statistics. WATS would not use a centralized computer for analysis because researchers found that factors such as latency and available bandwidth tended to create significant bottlenecks. Data processed in the field by the network itself (by transferring small amounts of data between neighboring sensors) is faster and makes the network more scalable.

An important factor in WATS development is *ease of deployment*, since more sensors both improves the detection rate and reduces false alarms. WATS sensors could be deployed in permanent positions or mounted in vehicles for mobile protection of specific locations. One barrier to the implementation of WATS is the size, weight, energy requirements and cost of currently available wireless sensors. The development of improved sensors is a major component of current research at the Nonproliferation, Arms Control, and International Security (NAI) Directorate at LLNL.

WATS was profiled to the U.S. House of Representatives' Military Research and Development Subcommittee on October 1, 1997, during a hearing on nuclear terrorism and countermeasures. On August 4, 1998, in a subsequent meeting of that subcommittee, Chairman Curt Weldon stated that research funding for WATS had been cut by the Clinton administration to a subsistence level and that the program had been poorly re-organized.

#### Incident monitoring

Studies show that using sensors for incident monitoring improve the response of firefighters and police to an unexpected situation. For an early detection of incidents we can use acoustic sensors to detect a spike in the noise of the city because of a possible accident, or use termic sensors to detect a possible fire.

### Supply chains

Using low-power electronics, WSN:s can be cost-efficiently applied also in supply chains in various industries.

## Characteristics

The main characteristics of a WSN include

- Power consumption constraints for nodes using batteries or energy harvesting. Examples of suppliers are ReVibe Energy and Perpetuum
- Ability to cope with node failures (resilience)
- Some mobility of nodes (for highly mobile nodes see MWSNs)
- Heterogeneity of nodes
- Homogeneity of nodes
- Scalability to large scale of deployment
- Ability to withstand harsh environmental conditions
- Ease of use
- Cross-layer optimization

Cross-layer is becoming an important studying area for wireless communications. In addition, the traditional layered approach presents three main problems:

1. Traditional layered approach cannot share different information among different layers, which leads to each layer not having complete information. The traditional layered approach cannot guarantee the optimization of the entire network.
2. The traditional layered approach does not have the ability to adapt to the environmental change.
3. Because of the interference between the different users, access conflicts, fading, and the change of environment in the wireless sensor networks, traditional layered approach for wired networks is not applicable to wireless networks.

So the cross-layer can be used to make the optimal modulation to improve the transmission performance, such as data rate, energy efficiency, quality of service (QoS), etc. Sensor nodes can be imagined as small computers which are extremely basic in terms of their interfaces and their components. They usually consist of a *processing unit* with limited computational power and limited memory, *sensors* or MEMS (including specific conditioning circuitry), a *communication device* (usually radio transceivers or alternatively optical), and a power source usually in the form of a battery. Other possible inclusions are energy harvesting modules, secondary ASICs, and possibly secondary communication interface (e.g. RS-232 or USB).

The base stations are one or more components of the WSN with much more computational, energy and communication resources. They act as a gateway between sensor nodes and the end user as they typically forward data from the WSN on to a server. Other special components in routing based networks are routers, designed to compute, calculate and distribute the routing tables.

## Platforms

### Hardware

One major challenge in a WSN is to produce *low cost* and *tiny* sensor nodes. There are an increasing number of small companies producing WSN hardware and the commercial situation can be compared to home computing in the 1970s. Many of the nodes are still in the research and development stage, particularly their software. Also inherent to sensor network adoption is the use of very low power methods for radio communication and data acquisition.

In many applications, a WSN communicates with a local area network or wide area network through a gateway. The Gateway acts as a bridge between the WSN and the other network. This enables data to be stored and processed by devices with more resources, for example, in a remotely located server. A wireless wide area network used primarily for low-power devices is known as a Low-Power Wide-Area Network (LPWAN).

### Wireless

There are several wireless standards and solutions for sensor node connectivity. Thread and Zigbee can connect sensors operating at 2.4 GHz with a data rate of 250 kbit/s. Many use a lower frequency to increase radio range (typically 1 km), for example Z-wave operates at 915 MHz (in North America) and in the EU 868 MHz has been widely used but these have a lower data rate (typically 50 kbit/s). The IEEE 802.15.4 working group provides a standard for low power device connectivity and commonly sensors and smart meters use one of these standards for connectivity. With the emergence of Internet of Things, many other proposals have been made to provide sensor connectivity. LoRa is a form of LPWAN which provides long range low power wireless connectivity for devices, which has been used in smart meters and other long range sensor applications. Wi-SUN connects devices at home. NarrowBand IOT and LTE-M can connect up to millions of sensors and devices using cellular technology.

### Software

Energy is the scarcest resource of WSN nodes, and it determines the lifetime of WSNs. WSNs may be deployed in large numbers in various environments, including remote and hostile regions, where ad hoc communications are a key component. For this reason, algorithms and protocols need to address the following issues:

- Increased lifespan
- Robustness and fault tolerance
- Self-configuration

Lifetime maximization: Energy/Power Consumption of the sensing device should be minimized and sensor nodes should be energy efficient since their limited energy resource determines their lifetime. To conserve power, wireless sensor nodes normally power off both the radio transmitter and the radio receiver when not in use.

#### Routing protocols

Wireless sensor networks are composed of low-energy, small-size, and low-range unattended sensor nodes. Recently, it has been observed that by periodically turning on and off the sensing and communication capabilities of sensor nodes, we can significantly reduce the active time and thus prolong network lifetime. However, this duty cycling may result in high network latency, routing overhead, and neighbor discovery delays due to asynchronous sleep and wake-up scheduling. These limitations call for a countermeasure for duty-cycled wireless sensor networks which should minimize routing information, routing traffic load, and energy consumption. Researchers from Sungkyunkwan University have proposed a lightweight non-increasing delivery-latency interval routing referred as LNDIR. This scheme can discover minimum latency routes at each non-increasing delivery-latency interval instead of each time slot. Simulation experiments demonstrated the validity of this novel approach in minimizing routing information stored at each sensor. Furthermore, this novel routing can also guarantee the minimum delivery latency from each source to the sink. Performance improvements of up to 12-fold and 11-fold are observed in terms of routing traffic load reduction and energy efficiency, respectively, as compared to existing schemes.

#### Operating systems

Operating systems for wireless sensor network nodes are typically less complex than general-purpose operating systems. They more strongly resemble embedded systems, for two reasons. First, wireless sensor networks are typically deployed with a particular application in mind, rather than as a general platform. Second, a need for low costs and low power leads most wireless sensor nodes to have low-power microcontrollers ensuring that mechanisms such as virtual memory are either unnecessary or too expensive to implement.

It is therefore possible to use embedded operating systems such as eCos or uC/OS for sensor networks. However, such operating systems are often designed with real-time properties.

TinyOS, developed by David Culler, is perhaps the first operating system specifically designed for wireless sensor networks. TinyOS is based on an event-driven programming model instead of multithreading. TinyOS programs are composed of *event handlers* and *tasks* with run-to-completion semantics. When an external event occurs, such as an incoming data packet or a sensor reading, TinyOS signals the appropriate event handler to handle the event. Event handlers can post tasks that are scheduled by the TinyOS kernel some time later.

LiteOS is a newly developed OS for wireless sensor networks, which provides UNIX-like abstraction and support for the C programming language.

Contiki, developed by Adam Dunkels, is an OS which uses a simpler programming style in C while providing advances such as 6LoWPAN and Protothreads.

RIOT (operating system) is a more recent real-time OS including similar functionality to Contiki.

PreonVM is an OS for wireless sensor networks, which provides 6LoWPAN based on Contiki and support for the Java programming language.

### Online collaborative sensor data management platforms

Online collaborative sensor data management platforms are on-line database services that allow sensor owners to register and connect their devices to feed data into an online database for storage and also allow developers to connect to the database and build their own applications based on that data. Examples include Xively and the Wikisensing platform Archived 2021-06-09 at the Wayback Machine. Such platforms simplify online collaboration between users over diverse data sets ranging from energy and environment data to that collected from transport services. Other services include allowing developers to embed real-time graphs & widgets in websites; analyse and process historical data pulled from the data feeds; send real-time alerts from any datastream to control scripts, devices and environments.

The architecture of the Wikisensing system describes the key components of such systems to include APIs and interfaces for online collaborators, a middleware containing the business logic needed for the sensor data management and processing and a storage model suitable for the efficient storage and retrieval of large volumes of data.

## Simulation

At present, agent-based modeling and simulation is the only paradigm which allows the simulation of complex behavior in the environments of wireless sensors (such as flocking). Agent-based simulation of wireless sensor and ad hoc networks is a relatively new paradigm. Agent-based modelling was originally based on social simulation.

Network simulators like Opnet, Tetcos NetSim and NS can be used to simulate a wireless sensor network.

## Other concepts

### Localization

Network localization refers to the problem of estimating the location of wireless sensor nodes during deployments and in dynamic settings. For ultra-low power sensors, size, cost and environment precludes the use of Global Positioning System receivers on sensors. In 2000, Nirupama Bulusu, John Heidemann and Deborah Estrin first motivated and proposed a radio connectivity based system for localization of wireless sensor networks. Subsequently, such localization systems have been referred to as range free localization systems, and many localization systems for wireless sensor networks have been subsequently proposed including AHLoS, APS, and Stardust.

### Sensor data calibration and fault tolerance

Sensors and devices used in wireless sensor networks are state-of-the-art technology with the lowest possible price. The sensor measurements we get from these devices are therefore often noisy, incomplete and inaccurate. Researchers studying wireless sensor networks hypothesize that much more information can be extracted from hundreds of unreliable measurements spread across a field of interest than from a smaller number of high-quality, high-reliability instruments with the same total cost.

### Macroprogramming

Macro-programming is a term coined by Matt Welsh. It refers to programming the entire sensor network as an ensemble, rather than individual sensor nodes. Another way to macro-program a network is to view the sensor network as a database, which was popularized by the TinyDB system developed by Sam Madden.

### Reprogramming

Reprogramming is the process of updating the code on the sensor nodes. The most feasible form of reprogramming is remote reprogramming whereby the code is disseminated wirelessly while the nodes are deployed. Different reprogramming protocols exist that provide different levels of speed of operation, reliability, energy expenditure, requirement of code resident on the nodes, suitability to different wireless environments, resistance to DoS, etc. Popular reprogramming protocols are Deluge (2004), Trickle (2004), MNP (2005), Synapse (2008), and Zephyr (2009).

### Security

Infrastructure-less architecture (i.e. no gateways are included, etc.) and inherent requirements (i.e. unattended working environment, etc.) of WSNs might pose several weak points that attract adversaries. Therefore, security is a big concern when WSNs are deployed for special applications such as military and healthcare. Owing to their unique characteristics, traditional security methods of computer networks would be useless (or less effective) for WSNs. Hence, lack of security mechanisms would cause intrusions towards those networks. These intrusions need to be detected and mitigation methods should be applied.

There have been important innovations in securing wireless sensor networks. Most wireless embedded networks use omni-directional  antennas and therefore neighbors can overhear communication in and out of nodes. This was used this to develop a primitive called "*local monitoring*" which was used for detection  of sophisticated attacks, like blackhole or wormhole, which degrade the  throughput of large networks to close-to-zero. This primitive has since been  used by many researchers and commercial wireless packet sniffers. This was subsequently refined for more sophisticated attacks such as with  collusion, mobility,  and multi-antenna, multi-channel devices.

### Distributed sensor network

If a centralized architecture is used in a sensor network and the central node fails, then the entire network will collapse, however the reliability of the sensor network can be increased by using a distributed control architecture. Distributed control is used in WSNs for the following reasons:

1. Sensor nodes are prone to failure,
2. For better collection of data,
3. To provide nodes with backup in case of failure of the central node.

There is also no centralised body to allocate the resources and they have to be self organized.

As for the distributed filtering over distributed sensor network. the general setup is to observe the underlying process through a group of sensors organized according to a given network topology, which renders the individual observer estimates the system state based not only on its own measurement but also on its neighbors'.

### Data integration and sensor web

The data gathered from wireless sensor networks is usually saved in the form of numerical data in a central base station. Additionally, the Open Geospatial Consortium (OGC) is specifying standards for interoperability interfaces and metadata encodings that enable real time integration of heterogeneous sensor webs into the Internet, allowing any individual to monitor or control wireless sensor networks through a web browser.

### In-network processing

To reduce communication costs some algorithms remove or reduce nodes' redundant sensor information and avoid forwarding data that is of no use. This technique has been used, for instance, for distributed anomaly detection or distributed optimization. As nodes can inspect the data they forward, they can measure averages or directionality for example of readings from other nodes. For example, in sensing and monitoring applications, it is generally the case that neighboring sensor nodes monitoring an environmental feature typically register similar values. This kind of data redundancy due to the spatial correlation between sensor observations inspires techniques for in-network data aggregation and mining. Aggregation reduces the amount of network traffic which helps to reduce energy consumption on sensor nodes. Recently, it has been found that network gateways also play an important role in improving energy efficiency of sensor nodes by scheduling more resources for the nodes with more critical energy efficiency need and advanced energy efficient scheduling algorithms need to be implemented at network gateways for the improvement of the overall network energy efficiency.

### Secure data aggregation

This is a form of in-network processing where sensor nodes are assumed to be unsecured with limited available energy, while the base station is assumed to be secure with unlimited available energy. Aggregation complicates the already existing security challenges for wireless sensor networks and requires new security techniques tailored specifically for these scenarios. Providing security to aggregate data in wireless sensor networks is known as *secure data aggregation in WSN*. were the first few works discussing techniques for secure  data aggregation in wireless sensor networks.

Two main security challenges in secure data aggregation are confidentiality and integrity of data. While encryption is traditionally used to provide end to end confidentiality in wireless sensor network, the aggregators in a secure data aggregation scenario need to decrypt the encrypted data to perform aggregation. This exposes the plaintext at the aggregators, making the data vulnerable to attacks from an adversary. Similarly an aggregator can inject false data into the aggregate and make the base station accept false data. Thus, while data aggregation improves energy efficiency of a network, it complicates the existing security challenges.
