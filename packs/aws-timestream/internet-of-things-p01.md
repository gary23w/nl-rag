---
title: "Internet of things (part 1/2)"
source: https://en.wikipedia.org/wiki/Internet_of_things
domain: aws-timestream
license: CC-BY-SA-4.0
tags: aws timestream, amazon timestream, time series database, iot time series store
fetched: 2026-07-02
part: 1/2
---

# Internet of things

**Internet of things** (**IoT**) describes physical objects that are embedded with sensors, processing ability, software, and other technologies that connect and exchange data with other devices and systems over the Internet or other communication networks. The field of IoT encompasses electronics, communication, and computer science engineering. "Internet of things" has been considered a misnomer because most devices do not need to be connected to the public Internet; they only need to be connected to a network and be individually addressable.

The field has evolved due to the convergence of multiple technologies, including ubiquitous computing, sensors, embedded systems, and machine learning. Traditional fields of embedded systems, wireless sensor networks, control systems, and automation independently and collectively enable the Internet of things.

While in the consumer market, IoT technology is most commonly as smart home products—including devices and appliances like thermostats and smart speakers—the technology's largest applications are in the business and industrial sectors. Commercial asset tracking and fleet management represent the largest single application of IoT, accounting for 22% of the total market, driven by the need to monitor mobile assets like vehicles and shipping containers. The largest asset tracking sub-segments in transport & logistics are trailer and intermodal container tracking, reaching 5.8 million and 5.3 million active devices globally at the end of 2024 respectively. Other major applications include industrial monitoring, smart metering in utilities, and connected healthcare.

There are a number of concerns about the risks in the growth of IoT technologies and products, especially in the areas of privacy and security, and consequently there have been industry and government moves to address these concerns adequately and minimize safety risks, including the development and implementation of international and local standards, guidelines, and regulatory frameworks. Due to their interconnected nature, IoT devices are vulnerable to security breaches and privacy concerns. At the same time, the way these devices communicate wirelessly creates regulatory ambiguities, complicating jurisdictional boundaries of the data transfer.


## Background

Around 1972, for its remote site use, the Stanford Artificial Intelligence Laboratory developed a computer-controlled vending machine, adapted from a machine rented from Canteen Vending, which sold for cash or, through a computer terminal (Teletype Model 33 KSR), on credit. Amongst its products were beer, yogurt, and milk. It was named *Prancing Pony*, after the name of the room, which was named after an inn in J. R. R. Tolkien's epic fantasy novel The Lord of the Rings. A successor version still operates in the Computer Science Department at Stanford, with updated hardware and software.


## History

In 1982, an early concept of a network connected smart device was constructed as an Internet interface for sensors installed in the Carnegie Mellon University *Computer Science Department*'s departmental Coca-Cola vending machine, supplied by graduate student volunteers, provided a temperature model and an inventory status, inspired by the computer controlled vending machine in the *Prancing Pony* room at Stanford Artificial Intelligence Laboratory. While it was initially accessible only on the CMU campus, it gained prominence as the first ARPANET-connected appliance.

Mark Weiser's 1991 paper on ubiquitous computing, "The Computer of the 21st Century", as well as academic venues such as UbiComp and PerCom, produced the contemporary vision of the IoT. In 1994, Reza Raji described the concept in *IEEE Spectrum* as "[moving] small packets of data to a large set of nodes, so as to integrate and automate everything from home appliances to entire factories." Between 1993 and 1997, several companies proposed solutions, such as Microsoft's at Work or Novell's NEST. The field gained momentum when Bill Joy envisioned device-to-device communication as part of his "Six Webs" framework, which was presented at the World Economic Forum in Davos in 1999.

The concept of the "Internet of things" and the term itself first appeared in a speech by Peter T. Lewis to the Congressional Black Caucus Foundation 15th Annual Legislative Weekend in Washington, D.C., published in September 1985. According to Lewis, "The Internet of Things, or IoT, is the integration of people, processes, and technology with connectable devices and sensors to enable remote monitoring, status, manipulation, and evaluation of trends of such devices."

The term "Internet of things" was coined independently by Kevin Ashton of Procter & Gamble, later of Massachusetts Institute of Technology's Auto-ID Center, in 1999, despite preferring the phrase "Internet *for* things." At that point, he considered radio-frequency identification (RFID) an essential component of the Internet of things, as it would effectively enable computers to manage all individual things. The primary defining characteristic of the Internet of things has been considered its ability to embed short-range mobile transceivers in various gadgets and daily necessities, enabling new forms of communication between people and things, as well as between things themselves.

In 2004, Cornelius "Pete" Peterson, CEO of NetSilicon, predicted that "The next era of information technology will be dominated by [IoT] devices, and networked devices will ultimately gain in popularity and significance to the extent that they will far exceed the number of networked computers and workstations." Peterson believed that medical devices and industrial controls would become dominant applications of the technology.

Defining the Internet of things as "simply the point in time when more 'things or objects' were connected to the Internet than people", Cisco Systems estimated that the IoT was "born" between 2008 and 2009, with the things/people ratio growing from 0.08 in 2003 to 1.84 in 2010.


## Applications

The extensive set of applications for IoT devices is often divided into consumer, commercial, industrial, and infrastructure spaces.

### Consumers

A growing portion of IoT devices is created for consumer use, including connected vehicles, home automation, wearable technology, connected health, and appliances with remote monitoring capabilities.

#### Home automation

IoT devices are part of the broader concept of home automation, which generally includes lighting, heating and air conditioning, media and security systems, and camera systems. Moreover, long-term benefits could include energy savings by automatically ensuring lights and electronics are turned off or by making the residents in the home aware of usage.

A smart home, also known as an automated home, could be based on a platform or hubs that control smart devices and appliances. For instance, using Apple's HomeKit, manufacturers can have their home products and accessories controlled by an application in iOS devices such as the iPhone and the Apple Watch. This could be a dedicated app or iOS native applications such as Siri. This can be demonstrated in the case of Lenovo's Smart Home Essentials, which is a line of smart home devices that are controlled through Apple's Home app or Siri without the need for a Wi-Fi bridge. There are also dedicated smart home hubs that are offered as standalone platforms to connect different smart home products. These include the Amazon Echo, Google Home, Apple's HomePod, and Samsung's SmartThings Hub. In addition to the commercial systems, there are many non-proprietary, open source ecosystems, including Home Assistant, OpenHAB, and Domoticz.

#### Elder care

One key application of a smart home is to assist the elderly and individuals with disabilities. These home systems use assistive technology to accommodate an owner's specific disabilities. Voice control can assist users with sight and mobility limitations while alert systems can be connected directly to cochlear implants worn by individuals with hearing impairments. They can also be equipped with additional safety features, including sensors that monitor for medical emergencies such as falls or seizures. Smart home technology applied in this way can provide users with more freedom and a higher quality of life.

### Organizations

The term "Enterprise IoT" refers to devices used in business and corporate settings.

#### Medical and healthcare

The **Internet of Medical Things** (**IoMT**) is an application of the IoT for medical and health-related purposes, data collection and analysis for research, and monitoring. The IoMT has been referenced as "Smart Healthcare", as the technology for creating a digitized healthcare system, connecting available medical resources and healthcare services.

IoT devices can be used to enable remote health monitoring and emergency notification systems. These health monitoring devices can range from blood pressure and heart rate monitors to advanced devices capable of monitoring specialized implants, such as pacemakers, Fitbit electronic wristbands, or advanced hearing aids. Some hospitals have begun implementing "smart beds" that can detect when they are occupied and when a patient is attempting to get up. It can also adjust itself to ensure appropriate pressure and support are applied to the patient without the manual interaction of nurses. A 2015 Goldman Sachs report indicated that healthcare IoT devices "can save the United States more than $300 billion in annual healthcare expenditures by increasing revenue and decreasing cost." Moreover, the use of mobile devices to support medical follow-up led to the creation of 'm-health', which is used to analyze health statistics.

Specialized sensors can also be equipped within living spaces to monitor the health and general well-being of senior citizens, while ensuring that proper treatment is administered and assisting people in regaining lost mobility via therapy as well. These sensors create a network of intelligent sensors that are able to collect, process, transfer, and analyze valuable information in different environments, such as connecting in-home monitoring devices to hospital-based systems. Other consumer devices to encourage healthy living, such as connected scales or wearable heart monitors, are also a possibility with the IoT. End-to-end health monitoring IoT platforms are also available for antenatal and chronic patients, helping one manage health vitals and recurring medication requirements.

Advances in plastic and fabric electronics fabrication methods have enabled ultra-low-cost, use-and-throw IoMT sensors. These sensors, along with the required radio-frequency identification electronics, can be fabricated on paper or e-textiles for wireless powered disposable sensing devices. Applications have been established for point-of-care medical diagnostics, where portability and low system complexity are considered essential.

As of 2018, IoMT was being applied in the clinical laboratory industry.

IoMT in the insurance industry provides access to better and new types of dynamic information. This includes sensor-based solutions such as biosensors, wearables, connected health devices, and mobile apps to track customer behavior. This can lead to more accurate underwriting and new pricing models.

The application of the IoT in healthcare plays a fundamental role in managing chronic diseases and in disease prevention and control. Remote monitoring is made possible through the connection of wireless solutions. The connectivity enables health practitioners to capture patients' data and apply algorithms in health data analysis.

#### Transportation

The IoT can assist in the integration of communications, control, and information processing across various transportation systems. Application of the IoT extends to all aspects of transportation systems (i.e., the vehicle, the infrastructure, and the driver or user). Dynamic interaction between these components of a transport system enables inter- and intra-vehicular communication, smart traffic control, smart parking, electronic toll collection systems, logistics and fleet management, vehicle control, safety, and road assistance. In vehicle security applications, IoT-connected GPS trackers can operate for months or years on internal batteries, using low-power wide-area network protocols such as LTE-M to transmit location data to owners via smartphone applications when unauthorized movement is detected.

#### V2X communications

In vehicular communication systems, vehicle-to-everything communication (V2X), consists of three main components: vehicle-to-vehicle communication (V2V), vehicle-to-infrastructure communication (V2I), and vehicle-to-pedestrian communication (V2P). Eventually, V2X is the first step to autonomous driving and connected road infrastructure.

#### Home automation

IoT devices can be used to monitor and control the mechanical, electrical, and electronic systems used in various types of buildings (e.g., public and private, industrial, institutions, or residential) in home automation and building automation systems. In this context, three main areas are being covered in the literature:

- The integration of the Internet with building energy management systems to create energy-efficient and IOT-driven "smart buildings".
- The possible means of real-time monitoring for reducing energy consumption and monitoring occupant behaviors.
- The integration of smart devices in the built environment and how they might be used in future applications.

### Industrial

Also known as IIoT, industrial IoT devices acquire and analyze data from connected equipment, operational technology (OT), locations, and people. Combined with operational technology (OT) monitoring devices, IIoT helps regulate and monitor industrial systems. Additionally, the same implementation can be carried out for automated record updates of asset placement in industrial storage units as the size of the assets can vary from a small screw to the whole motor spare part, and misplacement of such assets can cause a loss of manpower time and money.

#### Manufacturing

The IoT can connect various manufacturing devices equipped with sensing, identification, processing, communication, actuation, and networking capabilities. Network control and management of manufacturing equipment, asset and situation management, or manufacturing process control enable IoT to be utilized for industrial applications and smart manufacturing. IoT intelligent systems enable rapid manufacturing and optimization of new products and rapid response to product demands.

Digital control systems, which aim to automate process controls, operator tools, and service information systems, alongside optimizing plant safety and security, fall within the purview of the IIoT. Furthermore, IoT can also be applied to asset management via predictive maintenance, statistical evaluation, and measurements to maximize reliability. Industrial management systems can be integrated with smart grids, enabling energy optimization. Measurements, automated controls, plant optimization, health and safety management, and other functions are provided by networked sensors.

In addition to general manufacturing, IoT is also used for processes in the industrialization of construction.

#### Agriculture

There are numerous IoT applications in farming such as collecting data on temperature, rainfall, humidity, wind speed, pest infestation, and soil content. This data can be used to automate farming techniques, make informed decisions to improve quality and quantity, minimize risk and waste, and reduce the effort required to manage crops. For example, farmers can now monitor soil temperature and moisture from afar and even apply IoT-acquired data to precision fertilization programs. The overall goal is that data from sensors, coupled with the farmer's knowledge and intuition about his or her farm, can help increase farm productivity, and also help reduce costs.

In August 2018, Toyota Tsusho began a partnership with Microsoft to create fish farming tools using the Microsoft Azure application suite for IoT technologies related to water management. Developed in part by researchers from Kindai University, the water pump mechanisms use artificial intelligence to count the number of fish on a conveyor belt, analyze the number of fish, and deduce the effectiveness of water flow from the data the fish provide. The FarmBeats project from Microsoft Research that uses TV white space to connect farms is also a part of the Azure Marketplace now.

#### Maritime

IoT devices are in use to monitor the environments and systems of boats and yachts. Many pleasure boats are left unattended for days in summer, and months in winter so such devices provide valuable early alerts of boat flooding, fire, and deep discharge of batteries.

### Infrastructure

Monitoring and controlling operations of sustainable urban and rural infrastructures like bridges, railway tracks and on- and offshore wind farms is a key application of the IoT. The IoT infrastructure can be used for monitoring any events or changes in structural conditions that can compromise safety and increase risk. The IoT can benefit the construction industry by cost-saving, time reduction, better quality workday, paperless workflow and increase in productivity. It can help in making faster decisions and saving money in Real-Time Data Analytics. It can also be used for scheduling repair and maintenance activities efficiently, by coordinating tasks between different service providers and users of these facilities. IoT devices can also be used to control critical infrastructure, like bridges, to provide access to ships. The usage of IoT devices for monitoring and operating infrastructure is likely to significantly improve incident management and emergency response coordination, and quality of service, up-times and reduce costs of operation in all infrastructure-related areas. Even areas such as waste management can benefit.

#### Metropolitan scale deployments

There are several planned or ongoing large-scale deployments of the IoT to enable better management of cities and systems. For example, Songdo, South Korea, the first fully equipped and wired smart city, is gradually being built, with approximately 70 percent of the business district completed as of June 2018. A sizeable portion of the city, the first of its kind, is planned to be wired and automated to operate with little or no human intervention.

In 2014, another application was undergoing a project in Santander, Spain. For this deployment, two approaches have been adopted. This city of 180,000 inhabitants has already seen 18,000 downloads of its city smartphone app. The app is connected to 10,000 sensors that enable services like parking search and environmental monitoring. Additionally, city context information is used in this deployment, aiming to benefit merchants through a spark deals mechanism based on city behavior that aims at maximizing the impact of each notification.

Other examples of large-scale deployments underway include the Sino-Singapore Guangzhou Knowledge City; work on improving air and water quality, reducing noise pollution, and increasing transportation efficiency in San Jose, California; and smart traffic management in western Singapore. Using its RPMA (Random Phase Multiple Access) technology, San Diego–based Ingenu has built a nationwide public network for low-bandwidth data transmissions using the same unlicensed 2.4 gigahertz spectrum as Wi-Fi. Ingenu's "Machine Network" covers more than a third of the US population across 35 major cities including San Diego and Dallas. French company, Sigfox, commenced building an Ultra Narrowband wireless data network in the San Francisco Bay Area in 2014, the first business to achieve such a deployment in the U.S. It subsequently announced it would set up a total of 4000 base stations to cover a total of 30 cities in the U.S. by the end of 2016, making it the largest IoT network coverage provider in the country thus far. Cisco also participates in smart cities projects. Cisco has deployed technologies for Smart Wi-Fi, Smart Safety & Security, Smart Lighting, Smart Parking, Smart Transports, Smart Bus Stops, Smart Kiosks, Remote Expert for Government Services (REGS) and Smart Education in the five km area in the city of Vijayawada, India.

Another example of a large deployment is the one completed by New York Waterways in New York City to connect all the city's vessels and be able to monitor them live 24/7. The network was designed and engineered by Fluidmesh Networks, a Chicago-based company developing wireless networks for critical applications. The NYWW network is currently providing coverage on the Hudson River, East River, and Upper New York Bay. With the wireless network in place, NY Waterway is able to take control of its fleet and passengers in a way that was not previously possible. New applications can include security, energy and fleet management, digital signage, public Wi-Fi, paperless ticketing and others.

#### Energy management

Significant numbers of energy-consuming devices (e.g., lamps, household appliances, motors, pumps, etc.) already integrate Internet connectivity, which can allow them to communicate with utilities not only to balance power generation but also helps optimize the energy consumption as a whole. These devices allow for remote control by users, or central management via a cloud-based interface, and enable functions like scheduling (e.g., remotely powering on or off heating systems, controlling ovens, changing lighting conditions etc.). The smart grid is a utility-side IoT application; systems gather and act on energy and power-related information to improve the efficiency of the production and distribution of electricity. Using advanced metering infrastructure (AMI) Internet-connected devices, electric utilities not only collect data from end-users, but also manage distribution automation devices like transformers.

#### Environmental monitoring

Environmental monitoring applications of the IoT typically use sensors to assist in environmental protection by monitoring air or water quality, atmospheric or soil conditions, and can even include areas like monitoring the movements of wildlife and their habitats. Development of resource-constrained devices connected to the Internet also means that other applications like earthquake or tsunami early-warning systems can also be used by emergency services to provide more effective aid. IoT devices in this application typically span a large geographic area and can also be mobile. It has been argued that the standardization that IoT brings to wireless sensing will revolutionize this area.

#### Living labs

Another example of integrating the IoT is the concept of a "living lab." Living labs integrate and combine research and innovation processes, establishing within a public-private-people-partnership. Between 2006 and January 2024, there were over 440 living labs (though not all are currently active) that use the IoT to collaborate and share knowledge between stakeholders to co-create innovative and technological products. When companies intend to implement and develop IoT services for smart cities, they need to have economic incentives. The US government plays a key role in smart city projects; changes in policies will help cities to implement the IoT, which provides effectiveness, efficiency, and accuracy of the resources that are being used. For instance, the US government provides tax incentives and affordable rent, improves public transport, and offers an environment where start-up companies, creative industries, and multinationals may co-create, share a common infrastructure and labor markets, and take advantage of locally embedded technologies, production processes, and transaction costs.

### Military

The Internet of Military Things (IoMT) is the application of IoT technologies in the military domain for the purposes of reconnaissance, surveillance, and other combat-related objectives. It is heavily influenced by the future prospects of warfare in an urban environment and involves the use of sensors, munitions, vehicles, robots, human-wearable biometrics, and other smart technology that is relevant on the battlefield.

One of the examples of IOT devices used in the military is the Xaver 1000 system. The Xaver 1000 was developed by Israel's Camero Tech, which is the latest in the company's line of "through-wall imaging systems." The Xaver line uses millimeter wave (MMW) radar, or radar in the range of 30-300 gigahertz. It is equipped with an AI-based life target tracking system as well as its own 3D 'sense-through-the-wall' technology.

#### Internet of Battlefield Things

The **Internet of Battlefield Things** (**IoBT**) is a project initiated and executed by the U.S. Army Research Laboratory (ARL) that focuses on the basic science related to the IoT that enhances the capabilities of Army soldiers. In 2017, ARL launched the Internet of Battlefield Things Collaborative Research Alliance (IoBT-CRA), establishing a working collaboration between industry, university, and Army researchers to advance the theoretical foundations of IoT technologies and their applications to Army operations.

#### Ocean of Things

The **Ocean of Things** project is a DARPA-led program designed to establish an Internet of things across large ocean areas for the purposes of collecting, monitoring, and analyzing environmental and vessel activity data. The project entails the deployment of about 50,000 floats that house a passive sensor suite that autonomously detects and tracks military and commercial vessels as part of a cloud-based network.

### Product digitalization

There are several applications of smart or active packaging in which a QR code or NFC tag is affixed to a product or its packaging. The tag itself is passive; however, it contains a unique identifier (typically a URL) which enables a user to access digital content about the product via a smartphone. Strictly speaking, such passive items are not part of the Internet of things, but they can be seen as enablers of digital interactions. The term "Internet of Packaging" has been coined to describe applications in which unique identifiers are used, to automate supply chains, and are scanned on large scale by consumers to access digital content. Authentication of the unique identifiers, and thereby of the product itself, is possible via a copy-sensitive digital watermark or copy detection pattern for scanning when scanning a QR code, while NFC tags can encrypt communication.


## Trends and characteristics

In the Internet of Things (IoT), As of April 2026, the number of devices connected and controlled via the Internet has increased. Applications of IoT technology vary across devices, but many share common characteristics.

The IoT creates opportunities for more direct integration of the physical world into computer-based systems, resulting in efficiency improvements, economic benefits, and reduced human exertions.

IoT Analytics reported there were 16.6 billion IoT devices connected in 2023. In 2020, the same firm projected there would be 30 billion devices connected by 2025. As of October, 2024, there are around 17 billion.

### Intelligence

Ambient intelligence and autonomous control are not part of the original concept of the Internet of things. Ambient intelligence and autonomous control do not necessarily require Internet structures, either. However, there is a shift in research (by companies such as Intel) to integrate the concepts of the IoT and autonomous control, with initial outcomes towards this direction considering objects as the driving force for autonomous IoT. An approach in this context is deep reinforcement learning where most of IoT systems provide a dynamic and interactive environment. Training an agent (i.e., IoT device) to behave smartly in such an environment cannot be addressed by conventional machine learning algorithms such as supervised learning. Through a reinforcement learning approach, a learning agent can sense the environment's state (e.g., sensing home temperature), perform actions (e.g., turn HVAC on or off) and learn by maximizing accumulated rewards it receives.

IoT intelligence can be offered at three levels: IoT devices, Edge/Fog nodes, and cloud computing. The need for intelligent control and decision at each level depends on the time sensitiveness of the IoT application. For example, an autonomous vehicle's camera needs to make real-time obstacle detection to avoid an accident. This fast decision making would not be possible if it is necessary to transfer data from the vehicle to cloud instances and return the predictions back to the vehicle. Instead, the operation should be performed locally in the vehicle. Integrating advanced machine learning algorithms, including deep learning, into IoT devices is an active research area to make smart objects closer to reality. Moreover, it is possible to get the most value out of IoT deployments through analyzing IoT data, extracting hidden information, and predicting control decisions. A wide variety of machine learning techniques have been used in IoT domain ranging from traditional methods such as regression, support vector machine, and random forest to advanced ones such as convolutional neural networks, LSTM, and variational autoencoder.

In the future, the Internet of things may be a non-deterministic and open network in which auto-organized or intelligent entities (web services, SOA components) and virtual objects (avatars) will be interoperable and able to act independently (pursuing their own objectives or shared ones) depending on the context, circumstances or environments. Autonomous behavior through the collection and reasoning of context information, as well as the object's ability to detect changes in the environment (faults affecting sensors) and introduce suitable mitigation measures, constitutes a major research trend, clearly needed to provide credibility to the IoT technology. Modern IoT products and solutions in the marketplace use a variety of different technologies to support such context-aware automation, but more sophisticated forms of intelligence are requested to permit sensor units and intelligent cyber-physical systems to be deployed in real environments.

### Architecture

IoT system architecture, in its simplistic view, consists of three tiers: Tier 1: Devices, Tier 2: the Edge Gateway, and Tier 3: the Cloud. Devices include networked things, such as the sensors and actuators found in IoT equipment, particularly those that use protocols such as Modbus, Bluetooth, Zigbee, or proprietary protocols, to connect to an Edge Gateway. The Edge Gateway layer consists of sensor data aggregation systems called Edge Gateways that provide functionality, such as pre-processing of the data, securing connectivity to cloud, using systems such as WebSockets, the event hub, and, even in some cases, edge analytics or fog computing. Edge Gateway layer is also required to give a common view of the devices to the upper layers to facilitate in easier management. The final tier includes the cloud application built for IoT using the microservices architecture, which are usually polyglot and inherently secure in nature using HTTPS/OAuth. It includes various database systems that store sensor data, such as time series databases or asset stores using backend data storage systems (e.g. Cassandra, PostgreSQL). The cloud tier in most cloud-based IoT system features event queuing and messaging system that handles communication that transpires in all tiers. Some experts classified the three-tiers in the IoT system as edge, platform, and enterprise and these are connected by proximity network, access network, and service network, respectively.

#### Network architecture

IoT requires huge scalability in the network space to handle the surge of devices. IETF 6LoWPAN can be used to connect devices to IP networks. With billions of devices being added to the Internet space, IPv6 may play an important role in handling the network layer scalability. IETF's Constrained Application Protocol, ZeroMQ, and MQTT can provide lightweight data transport. In practice, many groups of IoT devices are hidden behind gateway nodes and may not have unique addresses. Also, the vision of everything being interconnected is not needed for most applications as it is mainly the data that needs interconnecting at a higher layer.

Fog computing is a viable alternative to prevent such a large burst of data flow through the Internet. The edge devices' computation power to analyze and process data is extremely limited. Limited processing power is a key attribute of IoT devices as their purpose is to supply data about physical objects while remaining autonomous. Heavy processing requirements use more battery power, harming IoT's ability to operate. Scalability is easy because IoT devices simply supply data through the Internet to a server with sufficient processing power.

##### Decentralized IoT

Decentralized Internet of things, or decentralized IoT, is a modified IoT that utilizes fog computing to handle and balance requests of connected IoT devices in order to reduce loading on the cloud servers and improve responsiveness for latency-sensitive IoT applications like vital signs monitoring of patients, vehicle-to-vehicle communication of autonomous driving, and critical failure detection of industrial devices. Performance is improved, especially for huge IoT systems with millions of nodes.

Conventional IoT is connected via a mesh network and led by a major head node (centralized controller). The head node decides how a data is created, stored, and transmitted. In contrast, decentralized IoT attempts to divide IoT systems into smaller divisions. The head node authorizes partial decision-making power to lower level sub-nodes under mutual agreed policy.

Some approaches to decentralized IoT attempt to address the limited bandwidth and hashing capacity of battery-powered or wireless IoT devices via blockchain.

### Complexity

In semi-open or closed loops (i.e., value chains, whenever a global finality can be settled) the IoT is often analyzed as a complex system due to the large number of different interactions between autonomous actors, and its capacity to integrate new actors. At the overall stage (full open loop) it will likely be seen as a chaotic environment (since systems always have finality).

As a practical approach, not all elements on the Internet of things run in a global, public space. Subsystems are often implemented to mitigate the risks of privacy, control and reliability. For example, domestic robotics (domotics) running inside a smart home might only share data within and be available via a local network. Managing and controlling a high dynamic ad hoc IoT things/devices network is a complex task within traditional network architecture, software-defined networking (SDN) provides a dynamic approach that better fits the special requirements of IoT applications.

### Size considerations

The exact scale of the Internet of things is unknown, with quotes of billions or trillions often quoted at the beginning of IoT articles. In 2015, there were 83 million smart devices in people's homes. This number is expected to grow to 193 million devices by 2020. In 2023, the number of connected IoT devices will reach 16.6 billion.

The number of online-capable devices grew 31% from 2016 to 2017 to reach 8.4 billion.

### Space considerations

In the Internet of things, the precise geographic location of a thing—and also the precise geographic dimensions of a thing—can be critical. Therefore, facts about a thing, such as its location in time and space, have been less critical to track because the person processing the information can decide whether or not that information was important to the action being taken, and if so, add the missing information (or decide to not take the action). (Note that some things on the Internet of things will be sensors, and sensor location is usually important.) The GeoWeb and Digital Earth are applications that become possible when things can become organized and connected by location. However, the challenges that remain include the constraints of variable spatial scales, the need to handle massive amounts of data, and an indexing for fast search and neighbour operations. On the Internet of things, if things are able to take actions on their own initiative, this human-centric mediation role is eliminated. Thus, the time-space context that we as humans take for granted must be given a central role in this information ecosystem. Just as standards play a key role on the Internet and the Web, geo-spatial standards will play a key role on the Internet of things.

### A solution to "basket of remotes"

Many IoT devices have the potential to take a piece of this market. Jean-Louis Gassée (Apple initial alumni team, and BeOS co-founder) has addressed this topic in an article on *Monday Note*, where he predicts that the most likely problem will be what he calls the "basket of remotes" problem, where we'll have hundreds of applications to interface with hundreds of devices that don't share protocols for speaking with one another. For improved user interaction, some technology leaders are joining forces to create standards for communication between devices to solve this problem. Others are turning to the concept of predictive interaction of devices, "where collected data is used to predict and trigger actions on the specific devices" while making them work together.

Social Internet of things (SIoT) is a new kind of IoT that focuses on the importance of social interaction and relationships between IoT devices. SIoT is a pattern of how cross-domain IoT devices enabling application to application communication and collaboration without human intervention in order to serve their owners with autonomous services, and this only can be realized when gained low-level architecture support from both IoT software and hardware engineering.

IoT defines a device with an identity like a citizen in a community and connects them to the Internet to provide services to its users. SIoT defines a social network for IoT devices only to interact with each other for different goals that to serve human.

#### How is SIoT different from IoT?

SIoT is different from the original IoT in terms of the collaboration characteristics. IoT is passive; it was set to serve for dedicated purposes with existing IoT devices in a predetermined system. SIoT is active, it was programmed and managed by AI to serve for unplanned purposes with mix and match of potential IoT devices from different systems that benefit its users.

#### Function

IoT devices with built-in sociability are able to broadcast their abilities or functionality, which can be used to discover and share information with other IoT devices in the same or nearby network, realizing SIoT. Facilitating further functionality with these abilities could be helpful during emergencies.

#### Examples

1. IoT-based smart home technology monitors health data of patients or aging adults by analyzing their physiological parameters and prompts the nearby health facilities when emergency medical services are needed. In case emergency, automatically, ambulance of a nearest available hospital will be called with pickup location provided, ward assigned, patient's health data will be transmitted to the emergency department, and display on the doctor's computer immediately for further action.
2. IoT sensors on the vehicles, road and traffic lights monitor the conditions of the vehicles and drivers and alert when attention is needed, and also coordinate themselves automatically to ensure autonomous driving is working normally. If a crash happens, the IoT camera will inform the nearest hospital and police station for help.

#### Challenges

1. Internet of things is multifaceted and complicated. One of the main factors that hindering people from adopting and use Internet of things (IoT) based products and services is its complexity. Installation and setup is a challenge to people; therefore, there is a need for IoT devices to mix, match and configure themselves automatically to provide different services in different situations.
2. System security is always a concern for any technology, and it is more crucial for SIoT as not only the security of oneself needs to be considered, but also the mutual trust mechanism between collaborative IoT devices from time to time, from place to place.
3. Another critical challenge for SIoT is the accuracy and reliability of the sensors. In most circumstances, IoT sensors would need to respond quickly to avoid accidents, injury, and loss of life.
