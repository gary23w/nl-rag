---
title: "Internet of things (part 2/2)"
source: https://en.wikipedia.org/wiki/Internet_of_things
domain: matter-protocol-deep
license: CC-BY-SA-4.0
tags: matter protocol, connectivity standards alliance, smart home interoperability, thread ip transport
fetched: 2026-07-02
part: 2/2
---

## Enabling technologies

There are many technologies that enable the IoT. Crucial to the field is the network used to communicate between devices of an IoT installation, a role that several wireless or wired technologies may fulfill:

### Addressability

The original idea of the Auto-ID Center is based on RFID tags and distinct identification through the Electronic Product Code. This has evolved into objects having an IP address or URI. An alternative view, from the world of the Semantic Web focuses instead on making all things (not just those electronic, smart, or RFID-enabled) addressable by the existing naming protocols, such as URI. The objects themselves do not converse, but they may now be referred to by other agents, such as powerful centralised servers acting for their human owners. Integration with the Internet implies that devices will use an IP address as a distinct identifier. Due to the limited address space of IPv4 (which allows for 4.3 billion different addresses), objects in the IoT will have to use the next generation of the Internet protocol (IPv6) to scale to the extremely large address space required. Internet-of-things devices additionally will benefit from the stateless address auto-configuration present in IPv6, as it reduces the configuration overhead on the hosts, and the IETF 6LoWPAN header compression. To a large extent, the future of the Internet of things will not be possible without the support of IPv6; and consequently, the global adoption of IPv6 in the coming years will be critical for the successful development of the IoT in the future.

### Application layer

- ADRC defines an application layer protocol and supporting framework for implementing IoT applications.

### Short-range wireless

- Bluetooth mesh networking – Specification providing a mesh networking variant to Bluetooth Low Energy (BLE) with an increased number of nodes and standardized application layer (Models).
- Li-Fi (light fidelity) – Wireless communication technology similar to the Wi-Fi standard, but using visible-light communication for increased bandwidth.
- Near-field communication (NFC) – Communication protocols enabling two electronic devices to communicate within a 4 cm range.
- Radio-frequency identification (RFID) – Technology using electromagnetic fields to read data stored in tags embedded in other items.
- Wi-Fi – Technology for local area networking–based on the IEEE 802.11 standard, where devices may communicate through a shared access point or directly between individual devices.
- Zigbee – Communication protocols for personal area networking– based on the IEEE 802.15.4 standard, providing low power consumption, low data rate, low cost, and high throughput.
- Z-Wave – Wireless communications protocol used primarily for home automation and security applications

### Medium-range wireless

- LTE-Advanced – High-speed communication specification for mobile networks. Provides enhancements to the LTE standard with extended coverage, higher throughput, and lower latency.
- 5G – 5G wireless networks can be used to achieve the high communication requirements of the IoT and connect a large number of IoT devices, even when they are on the move. There are three features of 5G that are each considered to be useful for supporting particular elements of IoT: enhanced mobile broadband (eMBB), massive machine type communications (mMTC) and ultra-reliable low latency communications (URLLC).
- LoRa: Range up to 3 miles (4.8 km) in urban areas, and up to 10 miles (16 km) or more in rural areas (line of sight).
- DASH7: Range of up to 2 km.

### Long-range wireless

- Low-power wide-area networking (LPWAN) – Wireless networks designed to allow long-range communication at a low data rate, reducing power and cost for transmission. Available LPWAN technologies and protocols: LoRaWan, NB-IoT, Weightless, RPMA, MIoTy, IEEE 802.11ah
- Very-small-aperture terminal (VSAT) – Satellite communication technology using small dish antennas for narrowband and broadband data.

### Wired

- Ethernet – General purpose networking standard using twisted pair and fiber optic links in conjunction with hubs or switches.
- Power-line communication (PLC) – Communication technology using electrical wiring to carry power and data. Specifications such as HomePlug or G.hn utilize PLC for networking IoT devices.

### Comparison of technologies by layer

Different technologies have different roles in a protocol stack. Below is a simplified presentation of the roles of several popular communication technologies in IoT applications:

|   | Physical | Link / MAC | Network | Transport | Application |
|---|---|---|---|---|---|
| Bluetooth LE | (Yes) | (Yes) | (Yes) | (Yes) | (Yes) |
| Z-Wave | (No) | (No) | (Yes) | (Yes) | (Yes) |
| ITU-T G.9959 | (Yes) | (Yes) | (No) | (No) | (No) |
| Zigbee | (No) | (No) | (Yes) | (Yes) | (Yes) |
| Matter | (No) | (No) | (No) | (No) | (Yes) |
| TCP and UDP | (No) | (No) | (No) | (Yes) | (No) |
| Thread | (No) | (No) | (Yes) | (No) | (No) |
| IEEE 802.15.4 | (Yes) | (Yes) | (No) | (No) | (No) |
| IPv6 | (No) | (No) | (Yes) | (No) | (No) |
| Ethernet | (Yes) | (Yes) | (No) | (No) | (No) |
| Wi-Fi | (Yes) | (Yes) | (No) | (No) | (No) |

### Standards and standards organizations

This is a list of technical standards for the IoT, most of which are open standards, and the standards organizations that aspire to successfully setting them.

| Short name | Long name | Standards under development | Other notes |
|---|---|---|---|
| Auto-ID Labs | Auto Identification Center | Networked RFID (radiofrequency identification) and emerging sensing technologies |   |
| Connected Home over IP | Project Connected Home over IP | Connected Home over IP (or Project Connected Home over IP) is an open-sourced, royalty-free home automation connectivity standard project which features compatibility among different smart home and Internet of things (IoT) products and software | The Connected Home over IP project group was launched and introduced by Amazon, Apple, Google, Comcast and the Zigbee Alliance on 18 December 2019. The project is backed by big companies and by being based on proven Internet design principles and protocols it aims to unify the currently fragmented systems. |
| EPCglobal | Electronic Product code Technology | Standards for adoption of EPC (Electronic Product Code) technology |   |
| FDA | U.S. Food and Drug Administration | UDI (Unique Device Identification) system for distinct identifiers for medical devices |   |
| GS1 | Global Standards One | Standards for UIDs ("unique" identifiers) and RFID of fast-moving consumer goods (consumer packaged goods), health care supplies, and other things The GS1 digital link standard, first released in August 2018, allows the use QR Codes, GS1 Datamatrix, RFID and NFC to enable various types of business-to-business, as well as business-to-consumer interactions. | Parent organization comprises member organizations such as GS1 US |
| IEEE | Institute of Electrical and Electronics Engineers | Underlying communication technology standards such as IEEE 802.15.4, IEEE P1451-99 (IoT Harmonization), and IEEE P1931.1 (ROOF Computing). |   |
| IETF | Internet Engineering Task Force | Standards that comprise TCP/IP (the Internet protocol suite) |   |
| MTConnect Institute | — | MTConnect is a manufacturing industry standard for data exchange with machine tools and related industrial equipment. It is important to the IIoT subset of the IoT. |   |
| O-DF | Open Data Format | O-DF is a standard published by the Internet of Things Work Group of The Open Group in 2014, which specifies a generic information model structure that is meant to be applicable for describing any "Thing", as well as for publishing, updating and querying information when used together with O-MI (Open Messaging Interface). |   |
| O-MI | Open Messaging Interface | O-MI is a standard published by the Internet of Things Work Group of The Open Group in 2014, which specifies a limited set of key operations needed in IoT systems, notably different kinds of subscription mechanisms based on the Observer pattern. |   |
| OCF | Open Connectivity Foundation | Standards for simple devices using CoAP (Constrained Application Protocol) | OCF (Open Connectivity Foundation) supersedes OIC (Open Interconnect Consortium) |
| OMA | Open Mobile Alliance | OMA DM and OMA LWM2M for IoT device management, as well as GotAPI, which provides a secure framework for IoT applications |   |
| XSF | XMPP Standards Foundation | Protocol extensions of XMPP (Extensible Messaging and Presence Protocol), the open standard of instant messaging |   |
| W3C | World Wide Web Consortium | Standards for bringing interoperability between different IoT protocols and platforms such as Thing Description, Discovery, Scripting API and Architecture that explains how they work together. | Homepage of the Web of Things activity at the W3C at https://www.w3.org/WoT/ |


## Politics and civic engagement

Some scholars and activists argue that the IoT can be used to create new models of civic engagement if device networks can be open to user control and interoperable platforms. Philip N. Howard, a professor and author, writes that political life in both democracies and authoritarian regimes will be shaped by the way the IoT will be used for civic engagement. For that to happen, he argues that any connected device should be able to divulge a list of the "ultimate beneficiaries" of its sensor data and that individual citizens should be able to add new organisations to the beneficiary list. In addition, he argues that civil society groups need to start developing their IoT strategy for making use of data and engaging with the public.


## Government regulation

One of the key drivers of the IoT is data. The success of the idea of connecting devices to make them more efficient is dependent upon access to and storage & processing of data. For this purpose, companies working on the IoT collect data from multiple sources and store it in their cloud network for further processing. This leaves the door wide open for privacy and security dangers and single point vulnerability of multiple systems. The other issues pertain to consumer choice and ownership of data and how it is used. Though still in their infancy, regulations and governance regarding these issues of privacy, security, and data ownership continue to develop. IoT regulation depends on the country. Some examples of legislation that is relevant to privacy and data collection are: the US Privacy Act of 1974, OECD Guidelines on the Protection of Privacy and Transborder Flows of Personal Data of 1980, and the EU Directive 95/46/EC of 1995.

Current regulatory environment:

A report published by the Federal Trade Commission (FTC) in January 2015 made the following three recommendations:

- Data security – At the time of designing IoT companies should ensure that data collection, storage and processing would be secure at all times. Companies should adopt a "defense in depth" approach and encrypt data at each stage.
- Data consent – users should have a choice as to what data they share with IoT companies and the users must be informed if their data gets exposed.
- Data minimisation – IoT companies should collect only the data they need and retain the collected information only for a limited time.

However, the FTC stopped at just making recommendations for now. According to an FTC analysis, the existing framework, consisting of the FTC Act, the Fair Credit Reporting Act, and the Children's Online Privacy Protection Act, along with developing consumer education and business guidance, participation in multi-stakeholder efforts and advocacy to other agencies at the federal, state and local level, is sufficient to protect consumer rights.

A resolution passed by the Senate in March 2015, is already being considered by the Congress. This resolution recognized the need for formulating a National Policy on IoT and the matter of privacy, security and spectrum. Furthermore, to provide an impetus to the IoT ecosystem, in March 2016, a bipartisan group of four Senators proposed a bill, The Developing Innovation and Growing the Internet of Things (DIGIT) Act, to direct the Federal Communications Commission to assess the need for more spectrum to connect IoT devices.

Approved on 28 September 2018, California Senate Bill No. 327 goes into effect on 1 January 2020. The bill requires "*a manufacturer of a connected device, as those terms are defined, to equip the device with a reasonable security feature or features that are appropriate to the nature and function of the device, appropriate to the information it may collect, contain, or transmit, and designed to protect the device and any information contained therein from unauthorized access, destruction, use, modification, or disclosure,*"

Several standards for the IoT industry are actually being established relating to automobiles because most concerns arising from use of connected cars apply to healthcare devices as well. In fact, the National Highway Traffic Safety Administration (NHTSA) is preparing cybersecurity guidelines and a database of best practices to make automotive computer systems more secure.

A recent report from the World Bank examines the challenges and opportunities in government adoption of IoT. These include –

- Still early days for the IoT in government
- Underdeveloped policy and regulatory frameworks
- Unclear business models, despite a strong value proposition
- Clear institutional and capacity gap in government AND the private sector
- Inconsistent data valuation and management
- Infrastructure a major barrier
- Government as an enabler
- Most successful pilots share common characteristics (public-private partnership, local, leadership)

In early December 2021, the U.K. government introduced the Product Security and Telecommunications Infrastructure bill (PST), an effort to legislate IoT distributors, manufacturers, and importers to meet certain cybersecurity standards. The bill also seeks to improve the security credentials of consumer IoT devices.


## Criticism, problems and controversies

### Platform fragmentation

The IoT suffers from platform fragmentation, lack of interoperability and common technical standards a situation where the variety of IoT devices, in terms of both hardware variations and differences in the software running on them, makes the task of developing applications that work consistently between different inconsistent technology ecosystems hard. For example, wireless connectivity for IoT devices can be done using Bluetooth, Wi-Fi, Wi-Fi HaLow, Zigbee, Z-Wave, LoRa, NB-IoT, Cat M1 as well as completely custom proprietary radios – each with its own advantages and disadvantages; and unique support ecosystem.

The IoT's amorphous computing nature is also a problem for security, since patches to bugs found in the core operating system often do not reach users of older and lower-price devices. One set of researchers says that the failure of vendors to support older devices with patches and updates leaves more than 87% of active Android devices vulnerable.

### Privacy, autonomy, and control

Philip N. Howard, a professor and author, writes that the Internet of things offers immense potential for empowering citizens, making government transparent, and broadening information access. Howard cautions, however, that privacy threats are enormous, as is the potential for social control and political manipulation.

Concerns about privacy have led many to consider the possibility that big data infrastructures such as the Internet of things and data mining are inherently incompatible with privacy. Key challenges of increased digitalization in the water, transport or energy sector are related to privacy and cybersecurity which necessitate an adequate response from research and policymakers alike.

Writer Adam Greenfield claims that IoT technologies are not only an invasion of public space but are also being used to perpetuate normative behavior, citing an instance of billboards with hidden cameras that tracked the demographics of passersby who stopped to read the advertisement.

The Internet of Things Council compared the increased prevalence of digital surveillance due to the Internet of things to the concept of the panopticon described by Jeremy Bentham in the 18th century. The assertion is supported by the works of French philosophers Michel Foucault and Gilles Deleuze. In *Discipline and Punish: The Birth of the Prison*, Foucault asserts that the panopticon was a central element of the discipline society developed during the Industrial Era. Foucault also argued that the discipline systems established in factories and school reflected Bentham's vision of panopticism. In his 1992 paper "Postscripts on the Societies of Control", Deleuze wrote that the discipline society had transitioned into a control society, with the computer replacing the panopticon as an instrument of discipline and control while still maintaining the qualities similar to that of panopticism.

Peter-Paul Verbeek, a professor of philosophy of technology at the University of Twente, Netherlands, writes that technology already influences our moral decision making, which in turn affects human agency, privacy and autonomy. He cautions against viewing technology merely as a human tool and advocates instead to consider it as an active agent.

Justin Brookman, of the Center for Democracy and Technology, expressed concern regarding the impact of the IoT on consumer privacy, saying that "There are some people in the commercial space who say, 'Oh, big data – well, let's collect everything, keep it around forever, we'll pay for somebody to think about security later.' The question is whether we want to have some sort of policy framework in place to limit that."

Tim O'Reilly believes that the way companies sell IoT devices to consumers is misplaced, disputing the notion that the IoT is about gaining efficiency from putting all kinds of devices online and postulating that, "IoT is really about human augmentation. The applications are profoundly different when you have sensors and data driving the decision-making."

Editorials at WIRED have also expressed concern, one stating, "What you're about to lose is your privacy. Actually, it's worse than that. You aren't just going to lose your privacy, you're going to have to watch the very concept of privacy be rewritten under your nose."

The American Civil Liberties Union (ACLU) expressed concern regarding the ability of IoT to erode people's control over their own lives. The ACLU wrote that "There's simply no way to forecast how these immense powers – disproportionately accumulating in the hands of corporations seeking financial advantage and governments craving ever more control – will be used. Chances are big data and the Internet of Things will make it harder for us to control our own lives, as we grow increasingly transparent to powerful corporations and government institutions that are becoming more opaque to us."

In response to rising concerns about privacy and smart technology, in 2007, the British Government stated it would follow formal Privacy by Design principles when implementing its smart metering program. The program would lead to the replacement of traditional power meters with smart power meters, which could track and manage energy usage more accurately. However the British Computer Society is doubtful these principles were ever actually implemented. In 2009, the Dutch Parliament rejected a similar smart metering program, basing their decision on privacy concerns. The Dutch program later revised and passed in 2011.

### Data storage

A challenge for producers of IoT applications is to clean, process and interpret the vast amount of data that is gathered by the sensors. There is a solution proposed for the analytics of the information referred to as Wireless Sensor Networks. These networks share data among sensor nodes that are sent to a distributed system for the analytics of the sensory data.

Another challenge is the storage of this bulk data. Depending on the application, there could be high data acquisition requirements, which in turn lead to high storage requirements. In 2013, the Internet was estimated to be responsible for consuming 5% of the total energy produced, and a "daunting challenge to power" IoT devices to collect and even store data still remains.

Data silos, although a common challenge of legacy systems, still commonly occur with the implementation of IoT devices, particularly within manufacturing. As there are a lot of benefits to be gained from IoT and IIoT devices, the means in which the data is stored can present serious challenges without the principles of autonomy, transparency, and interoperability being considered. The challenges do not occur by the device itself, but the means in which databases and data warehouses are set up. These challenges were commonly identified in manufacturers and enterprises that have begun digital transformation, and are part of the digital foundation, indicating that in order to receive the optimal benefits from IoT devices and for decision making, enterprises will have to first re-align their data storage methods. These challenges were identified by Keller (2021) when investigating the IT and application landscape of I4.0 implementation within German M&E manufacturers.

### Security

Security is the biggest concern in adopting Internet of things technology, with concerns that rapid development is happening without appropriate consideration of the profound security challenges involved and the regulatory changes that might be necessary. The rapid development of the Internet of Things (IoT) has allowed billions of devices to connect to the network. Due to too many connected devices and the limitation of communication security technology, various security issues gradually appear in the IoT.

Most of the technical security concerns are similar to those of conventional servers, workstations and smartphones. These concerns include using weak authentication, forgetting to change default credentials, unencrypted messages sent between devices, SQL injections, man-in-the-middle attacks, and poor handling of security updates. However, many IoT devices have severe operational limitations on the computational power available to them. These constraints often make them unable to directly use basic security measures such as implementing firewalls or using strong cryptosystems to encrypt their communications with other devices - and the low price and consumer focus of many devices makes a robust security patching system uncommon.

Rather than conventional security vulnerabilities, fault injection attacks are on the rise and targeting IoT devices. A fault injection attack is a physical attack on a device to purposefully introduce faults in the system to change the intended behavior. Faults might happen unintentionally due to environmental noises and electromagnetic fields. There are ideas stemming from control-flow integrity (CFI) to prevent fault injection attacks and system recovery to a healthy state before the fault.

Internet of things devices also have access to new areas of data, and can often control physical devices, so that even by 2014 it was possible to say that many Internet-connected appliances could already "spy on people in their own homes" including televisions, kitchen appliances, cameras, and thermostats. Computer-controlled devices in automobiles such as brakes, engine, locks, hood and trunk releases, horn, heat, and dashboard have been shown to be vulnerable to attackers who have access to the on-board network. In some cases, vehicle computer systems are Internet-connected, allowing them to be exploited remotely. By 2008, security researchers had shown the ability to remotely control pacemakers without authority. Later, hackers demonstrated remote control of insulin pumps and implantable cardioverter defibrillators.

Poorly secured Internet-accessible IoT devices can also be subverted to attack others. In 2016, a distributed denial of service attack powered by Internet of things devices running the Mirai malware took down a DNS provider and major web sites. The Mirai Botnet had infected roughly 65,000 IoT devices within the first 20 hours. Eventually, the infections increased to around 200,000 to 300,000 infections. Brazil, Colombia and Vietnam made up of 41.5% of the infections. The Mirai Botnet had singled out specific IoT devices that consisted of DVRs, IP cameras, routers and printers. Top vendors that contained the most infected devices were identified as Dahua, Huawei, ZTE, Cisco, ZyXEL and MikroTik**.** In May 2017, Junade Ali, a computer scientist at Cloudflare noted that native DDoS vulnerabilities exist in IoT devices due to a poor implementation of the Publish–subscribe pattern. These sorts of attacks have caused security experts to view IoT as a real threat to Internet services.

The U.S. National Intelligence Council in an unclassified report maintains that it would be hard to deny "access to networks of sensors and remotely-controlled objects by enemies of the United States, criminals, and mischief makers... An open market for aggregated sensor data could serve the interests of commerce and security no less than it helps criminals and spies identify vulnerable targets. Thus, massively parallel sensor fusion may undermine social cohesion, if it proves to be fundamentally incompatible with Fourth-Amendment guarantees against unreasonable search." In general, the intelligence community views the Internet of things as a rich source of data.

On 31 January 2019, *The Washington Post* wrote an article regarding the security and ethical challenges that can occur with IoT doorbells and cameras: "Last month, Ring got caught allowing its team in Ukraine to view and annotate certain user videos; the company says it only looks at publicly shared videos and those from Ring owners who provide consent. Just last week, a California family's Nest camera let a hacker take over and broadcast fake audio warnings about a missile attack, not to mention peer in on them, when they used a weak password."

There have been a range of responses to concerns over security. The Internet of Things Security Foundation (IoTSF) was launched on 23 September 2015 with a mission to secure the Internet of things by promoting knowledge and best practices. Its founding board is made up of technology providers and telecommunications companies. In addition, large IT companies are continually developing innovative solutions to ensure the security of IoT devices. In 2017, Mozilla launched Project Things, which allows to route IoT devices through a safe Web of Things gateway. As per the estimates from KBV Research, the overall IoT security market would grow at 27.9% rate during 2016–2022 as a result of growing infrastructural concerns and diversified usage of Internet of things.

Governmental regulation is argued by some to be necessary to secure IoT devices and the wider Internet – as market incentives to secure IoT devices is insufficient. It was found that due to the nature of most of the IoT development boards, they generate predictable and weak keys which make it easy to be utilized by man-in-the-middle attack. However, various hardening approaches were proposed by many researchers to resolve the issue of SSH weak implementation and weak keys.

IoT security within the field of manufacturing presents different challenges and varying perspectives. Within the EU and Germany, data protection is constantly referenced throughout manufacturing and digital policy, particularly that of I4.0. However, the attitude towards data security differs from the enterprise perspective, whereas there is an emphasis on less data protection in the form of GDPR, as the data being collected from IoT devices in the manufacturing sector does not display personal details. Yet, research has indicated that manufacturing experts are concerned about "data security for protecting machine technology from international competitors with the ever-greater push for interconnectivity".

### Safety

IoT systems are typically controlled by event-driven smart apps that take as input either sensed data, user inputs, or other external triggers (from the Internet) and command one or more actuators towards providing different forms of automation. Examples of sensors include smoke detectors, motion sensors, and contact sensors. Examples of actuators include smart locks, smart power outlets, and door controls. Popular control platforms on which third-party developers can build smart apps that interact wirelessly with these sensors and actuators include Samsung's SmartThings, Apple's HomeKit, and Amazon's Alexa, among others.

A problem specific to IoT systems is that buggy apps, unforeseen bad app interactions, or device/communication failures, can cause unsafe and dangerous physical states, e.g., "unlock the entrance door when no one is at home" or "turn off the heater when the temperature is below 0 degrees Celsius and people are sleeping at night". Detecting flaws that lead to such states, requires a holistic view of installed apps, component devices, their configurations, and more importantly, how they interact. Recently, researchers from the University of California Riverside have proposed IotSan, a novel practical system that uses model checking as a building block to reveal "interaction-level" flaws by identifying events that can lead the system to unsafe states. They have evaluated IotSan on the Samsung SmartThings platform. From 76 manually configured systems, IotSan detects 147 vulnerabilities (i.e., violations of safe physical states/properties).

### Design

Given widespread recognition of the evolving nature of the design and management of the Internet of things, sustainable and secure deployment of IoT solutions must design for "anarchic scalability". Application of the concept of anarchic scalability can be extended to physical systems (i.e. controlled real-world objects), by virtue of those systems being designed to account for uncertain management futures. This hard anarchic scalability thus provides a pathway forward to fully realize the potential of Internet-of-things solutions by selectively constraining physical systems to allow for all management regimes without risking physical failure.

Brown University computer scientist Michael Littman has argued that successful execution of the Internet of things requires consideration of the interface's usability as well as the technology itself. These interfaces need to be not only more user-friendly but also better integrated: "If users need to learn different interfaces for their vacuums, their locks, their sprinklers, their lights, and their coffeemakers, it's tough to say that their lives have been made any easier."

### Environmental sustainability impact

A concern regarding Internet-of-things technologies pertains to the environmental impacts of the manufacture, use, and eventual disposal of all these semiconductor-rich devices. Modern electronics are replete with a wide variety of heavy metals and rare-earth metals, as well as highly toxic synthetic chemicals. This makes them extremely difficult to properly recycle. Electronic components are often incinerated or placed in regular landfills. Furthermore, the human and environmental cost of mining the rare-earth metals that are integral to modern electronic components continues to grow. This leads to societal questions concerning the environmental impacts of IoT devices over their lifetime.

### Intentional obsolescence of devices

The Electronic Frontier Foundation has raised concerns that companies can use the technologies necessary to support connected devices to intentionally disable or "brick" their customers' devices via a remote software update or by disabling a service necessary to the operation of the device. In one example, home automation devices sold with the promise of a "Lifetime Subscription" were rendered useless after Nest Labs acquired Revolv and made the decision to shut down the central servers the Revolv devices had used to operate. As Nest is a company owned by Alphabet (Google's parent company), the EFF argues this sets a "terrible precedent for a company with ambitions to sell self-driving cars, medical devices, and other high-end gadgets that may be essential to a person's livelihood or physical safety."

Owners should be free to point their devices to a different server or collaborate on improved software. But such action violates the United States DMCA section 1201, which only has an exemption for "local use". This forces tinkerers who want to keep using their own equipment into a legal grey area. EFF thinks buyers should refuse electronics and software that prioritize the manufacturer's wishes above their own.

Examples of post-sale manipulations include Google Nest Revolv, disabled privacy settings on Android, Sony disabling Linux on PlayStation 3, and enforced EULA on Wii U.

### Confusing terminology

Kevin Lonergan at *Information Age*, a business technology magazine, has referred to the terms surrounding the IoT as a "terminology zoo". The lack of clear terminology is not "useful from a practical point of view" and a "source of confusion for the end user". A company operating in the IoT space could be working in anything related to sensor technology, networking, embedded systems, or analytics. According to Lonergan, the term IoT was coined before smart phones, tablets, and devices as we know them today existed, and there is a long list of terms with varying degrees of overlap and technological convergence: Internet of things, Internet of everything (IoE), Internet of goods (supply chain), industrial Internet, pervasive computing, pervasive sensing, ubiquitous computing, cyber-physical systems (CPS), wireless sensor networks (WSN), smart objects, digital twin, cyberobjects or avatars, cooperating objects, machine to machine (M2M), ambient intelligence (AmI), Operational technology (OT), and information technology (IT). Regarding IIoT, an industrial sub-field of IoT, the Industrial Internet Consortium's Vocabulary Task Group has created a "common and reusable vocabulary of terms" to ensure "consistent terminology" across publications issued by the Industrial Internet Consortium. IoT One has created an IoT Terms Database including a New Term Alert to be notified when a new term is published. As of March 2020, this database aggregates 807 IoT-related terms, while keeping material "transparent and comprehensive".


## Adoption barriers

### Lack of interoperability and unclear value propositions

Despite a shared belief in the potential of the IoT, industry leaders and consumers are facing barriers to adopting IoT technology more widely. Mike Farley argued in Forbes that while IoT solutions appeal to early adopters, they either lack interoperability or a clear use case for end-users. A study by Ericsson regarding the adoption of IoT among Danish companies suggests that many struggle "to pinpoint exactly where the value of IoT lies for them".

### Privacy and security concerns

As for IoT, especially in regard to consumer IoT, information about a user's daily routine is collected so that the "things" around the user can cooperate to provide better services that fulfill personal preferences. When the collected information which describes a user in detail travels through multiple hops in a network, due to a diverse integration of services, devices and network, the information stored on a device is vulnerable to privacy violation by compromising nodes existing in an IoT network.

For example, on 21 October 2016, a multiple distributed denial of service (DDoS) attacks systems operated by domain name system provider Dyn, which caused the inaccessibility of several websites, such as GitHub, Twitter, and others. This attack is executed through a botnet consisting of a large number of IoT devices including IP cameras, gateways, and even baby monitors.

Fundamentally there are 4 security objectives that the IoT system requires: (1) data confidentiality: unauthorised parties cannot have access to the transmitted and stored data; (2) data integrity: intentional and unintentional corruption of transmitted and stored data must be detected; (3) non-repudiation: the sender cannot deny having sent a given message; (4) data availability: the transmitted and stored data should be available to authorised parties even with the denial-of-service (DOS) attacks.

Information privacy regulations also require organisations to practice "reasonable security". California's SB-327 Information privacy: connected devices "would require a manufacturer of a connected device, as those terms are defined, to equip the device with a reasonable security feature or features that are appropriate to the nature and function of the device, appropriate to the information it may collect, contain, or transmit, and designed to protect the device and any information contained therein from unauthorised access, destruction, use, modification, or disclosure, as specified". As each organisation's environment is unique, it can prove challenging to demonstrate what "reasonable security" is and what potential risks could be involved for the business. Oregon's HB2395 also "requires [a *person that manufactures, sells or offers to sell connected device*] **manufacturer** to equip connected device with reasonable security features that protect **connected device** and information that connected device [*collects, contains, stores or transmits*] **stores** from access, destruction, modification, use or disclosure that consumer does not authorise."

According to antivirus provider Kaspersky, there were 639 million data breaches of IoT devices in 2020 and 1.5 billion breaches in the first six months of 2021.

One method of overcoming the barrier of safety issues is the introduction of standards and certification of devices. In 2024, two voluntary and non-competing programs were proposed and launched in the United States: the US Cyber Trust Mark from The Federal Communications Commission and CSA's IoT Device Security Specification from the Connectivity Standards Alliance. The programs incorporate international expertise, with the CSA mark recognized by the Singapore Cybersecurity Agency. Compliance means that IoT devices can resist hacking, control hijacking and theft of confidential data.

### Traditional governance structure

A study issued by Ericsson regarding the adoption of Internet of things among Danish companies identified a "clash between IoT and companies' traditional governance structures, as IoT still presents both uncertainties and a lack of historical precedence." Among the respondents interviewed, 60 percent stated that they "do not believe they have the organizational capabilities, and three of four do not believe they have the processes needed, to capture the IoT opportunity." This has led to a need to understand organizational culture in order to facilitate organizational design processes and to test new innovation management practices. A lack of digital leadership in the age of digital transformation has also stifled innovation and IoT adoption to a degree that many companies, in the face of uncertainty, "were waiting for the market dynamics to play out", or further action in regards to IoT "was pending competitor moves, customer pull, or regulatory requirements". Some of these companies risk being "kodaked" – "Kodak was a market leader until digital disruption eclipsed film photography with digital photos" – failing to "see the disruptive forces affecting their industry" and "to truly embrace the new business models the disruptive change opens up". Scott Anthony has written in Harvard Business Review that Kodak "created a digital camera, invested in the technology, and even understood that photos would be shared online" but ultimately failed to realize that "online photo sharing *was* the new business, not just a way to expand the printing business."

### Business planning and project management

According to a 2018 study, 70–75% of IoT deployments were stuck in the pilot or prototype stage, unable to reach scale due in part to a lack of business planning.

Even though scientists, engineers, and managers across the world are continuously working to create and exploit the benefits of IoT products, there are some flaws in the governance, management and implementation of such projects. Despite tremendous forward momentum in the field of information and other underlying technologies, IoT still remains a complex area and the problem of how IoT projects are managed still needs to be addressed. IoT projects must be run differently than simple and traditional IT, manufacturing or construction projects. Because IoT projects have longer project timelines, a lack of skilled resources and several security/legal issues, there is a need for new and specifically designed project processes. The following management techniques should improve the success rate of IoT projects:

- A separate research and development phase
- A Proof-of-Concept/Prototype before the actual project begins
- Project managers with interdisciplinary technical knowledge
- Universally defined business and technical jargon
