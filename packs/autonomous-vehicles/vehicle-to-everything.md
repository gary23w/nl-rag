---
title: "Vehicle-to-everything"
source: https://en.wikipedia.org/wiki/Vehicle-to-everything
domain: autonomous-vehicles
license: CC-BY-SA-4.0
tags: autonomous vehicles, self-driving car, vehicular automation, automated driving
fetched: 2026-07-02
---

# Vehicle-to-everything

**Vehicle-to-everything** (**V2X**) describes wireless communication between a vehicle and any entity that may affect, or may be affected by, the vehicle. Sometimes called C-V2X, it is a vehicular communication system that is intended to improve road safety and traffic efficiency while reducing pollution and saving energy.

The automotive and communications industries, along with the U.S. government, European Union and South Korea are actively promoting V2X and C-V2X as potentially life-saving, pollution-reducing technologies. The U.S. Department of Transport has said V2X technologies offer significant transportation safety and mobility benefits. The U.S. NHTSA estimates a minimum of 13% reduction in traffic accidents if a V2V system were implemented, resulting in 439,000 fewer crashes per year. V2X technology is already being used in Europe and China.

There are two standards for dedicated V2X communications depending on the underlying wireless technology being used: (1) WLAN-based, and (2) cellular-based. V2X also incorporates various more specific types of communication including:

- Vehicle-to-device (V2D) - Bluetooth / WiFi-Direct, e.g. Apple's CarPlay and Google's Android Auto.
- Vehicle-to-grid (V2G) - information exchange with the smart grid to balance loads more efficiently.
  - Vehicle-to-building (V2B), also known as vehicle-to-home (V2H)
  - Vehicle-to-load (V2L)
- Vehicle-to-network (V2N) - communication between a vehicle and a wider network, such as a cellular network. This category includes telematics, where a vehicle communicates with a fleet management platform or a cloud server.
  - Vehicle-to-cloud (V2C) - e.g. OTA updates, remote vehicle diagnostics (DoIP).
  - Vehicle-to-infrastructure (V2I) - e.g. traffic lights, lane markers and parking meters.
  - Vehicle-to-pedestrian (V2P) - e.g. wheelchairs and bicycles, commonly also used to designate vulnerable road users (VRUs).
  - Vehicle-to-vehicle (V2V) - real-time data exchange with nearby vehicles.

## History

The history of working on vehicle-to-vehicle communication projects to increase safety, reduce accidents and driver assistance can be traced back to the 1970s with projects such as the US Electronic Road Guidance System (ERGS) and Japan's CACS. Most milestones in the history of vehicle networks originate from the United States, Europe, and Japan.

Standardization of WLAN-based V2X supersedes that of cellular-based V2X systems. IEEE first published the specification of WLAN-based V2X (IEEE 802.11p) in 2010. It supports direct communication between vehicles (V2V) and between vehicles and infrastructure (V2I). This technology is referred to as dedicated short-range communication (DSRC). DSRC uses the underlying radio communication provided by 802.11p.

In 2016, Toyota became the first automaker globally to introduce automobiles equipped with V2X. These vehicles use DSRC technology and are only for sale in Japan. In 2017, GM became the second automaker to introduce V2X. GM sells a Cadillac model in the United States that also is equipped with DSRC V2X.

In 2016, 3GPP published V2X specifications based on LTE as the underlying technology. It is generally referred to as "cellular V2X" (C-V2X) to differentiate itself from the 802.11p based V2X technology. In addition to the direct communication (V2V, V2I), C-V2X also supports wide area communication over a cellular network (V2N).

As of December 2017, a European automotive manufacturer has announced to deploy V2X technology based on 802.11p from 2019. While some studies and analysis in 2017 and 2018, all performed by the 5G Automotive Association (5GAA) – the industry organisation supporting and developing the C-V2X technology – indicate that cellular-based C-V2X technology in direct communication mode is superior to 802.11p in multiple aspects, such as performance, communication range, and reliability, many of these claims are disputed, e.g. in a whitepaper published by NXP, one of the companies active in the 802.11p based V2X technology, but also published by peer-reviewed journals.

This technology can be misused to remotely control the vehicle. The Police of the Czech Republic in cooperation with universities has developed a system for remote stopping of vehicles with reference to the fact that such a procedure is legal even under the current legislation.

## Technology overview

### 802.11p (DSRC)

The original V2X communication uses WLAN technology and works directly between vehicles (V2V) as well as vehicles and traffic infrastructure (V2I), which form a vehicular ad-hoc network as two V2X senders come within each other's range. Hence it does not require any communication infrastructure for vehicles to communicate, which is key to assure safety in remote or little-developed areas.

WLAN is particularly well-suited for V2X communication, due to its low latency. It transmits messages known as Cooperative Awareness Messages (CAM) or Basic Safety Message (BSM), and Decentralised Environmental Notification Messages (DENM).

Other roadside infrastructure related messages are Signal Phase and Timing Message (SPaT), In Vehicle Information Message (IVI), and Service Request Message (SRM). The data volume of these messages is very low. The radio technology is part of the WLAN IEEE 802.11 family of standards and known in the US as Wireless Access in Vehicular Environments (WAVE) and in Europe as ITS-G5. To complement the direct communication mode, vehicles can be equipped with traditional cellular communication technologies, supporting V2N based services. This extension with V2N was achieved in Europe under the C-ITS platform umbrella with cellular systems and broadcast systems (TMC/DAB+).

### 3GPP (C-V2X)

More recent V2X communication uses cellular networks and is called cellular V2X (or C-V2X) to differentiate it from the WLAN-based V2X. There have been multiple industry organizations, such as the 5G Automotive Association (5GAA) promoting C-V2X due to its advantages over WLAN based V2X (without considering disadvantages at the same time). C-V2X is initially defined as LTE in 3GPP Release 14 and is designed to operate in several modes:

1. Device-to-device (V2V or V2I), and
2. Device-to-network (V2N).

In 3GPP Release 15, the V2X functionalities are expanded to support 5G. C-V2X includes support of both direct communication between vehicles (V2V) and traditional cellular-network based communication. Also, C-V2X provides a migration path to 5G based systems and services, which implies incompatibility and higher costs compared to 4G based solutions.

The direct communication between vehicle and other devices (V2V, V2I) uses so-called PC5 interface. PC5 refers to a reference point where the User Equipment (UE), i.e. mobile handset, directly communicates with another UE over the direct channel. In this case, the communication with the base station is not required. In system architectural level, proximity service (ProSe) is the feature that specifies the architecture of the direct communication between UEs. In 3GPP RAN specifications, "sidelink" is the terminology to refer to the direct communication over PC5. PC5 interface was originally defined to address the needs of mission-critical communication for public safety community (Public Safety-LTE, or PS-LTE) in release 13. The motivation of the mission-critical communication was to allow law enforcement agencies or emergency rescue to use the LTE communication even when the infrastructure is not available, such as natural disaster scenario. In release 14 onwards, the use of PC5 interface has been expanded to meet various market needs, such as communication involving wearable devices such as smartwatch. In C-V2X, PC5 interface is re-applied to the direct communication in V2V and V2I.

The Cellular V2X mode 4 communication relies on a distributed resource allocation scheme, namely sensing-based semipersistent scheduling which schedules radio resources in a stand-alone fashion in each user equipment (UE).

In addition to the direct communication over PC5, C-V2X also allows the C-V2X device to use the cellular network connection in the traditional manner over Uu interface. Uu refers to the logical interface between the UE and the base station. This is generally referred to as vehicle-to-network (V2N), the mechanism that enables conventional **telematics** services. V2N is a unique use case to C-V2X and does not exist in 802.11p based V2X given that the latter supports direct communication only. However, similar to WLAN based V2X also in case of C-V2X, two communication radios are required to be able to communicate simultaneously via a PC5 interface with nearby stations and via the UU interface with the network.

While 3GPP defines the data transport features that enable V2X, it does not include V2X semantic content but proposes usage of ITS-G5 standards like CAM, DENM, BSM, etc. over 3GPP V2X data transport features.

## Use cases

Through its instant communication, V2X enables road safety applications such as (non-exhaustive list):

- Forward collision warning
- Lane change warning/blind spot warning
- Emergency electric brake light warning
- Optimal speed advisory (through traffic lights)
- Emergency vehicle approaching
- Roadworks warning
- Platooning
- **Fleet management**: Utilizing V2N communication for telematics applications such as remote vehicle diagnostics, fleet management software, track and trace of assets, and communication with a central dispatch platform.
- Energy efficient intersection control
- Prevention of red light running

In June 2024 the U.S. Department of Transportation announced that it is awarding $60 million in grants to advance connected and interoperable vehicle technologies under a program called "Saving Lives with Connectivity: Accelerating V2X Deployment program". It said the grants to recipients in Arizona, Texas and Utah would serve as national models to accelerate and spur new deployments of V2X technologies. European standardisation body ETSI and SAE published standards on what they see as use cases. Early use cases focus on road safety and efficiency. Organizations such as 3GPP and 5GAA continuously introduce and test new cases. The 5GAA has published several roadmaps which highlight the technical potential and challenges of new use cases. Some use cases address high levels of automation.

C-V2X offers further use cases including slippery road, roadworks and road hazard information to cars and trucks over hills, around curves and over longer distances than is possible with direct communications. Volvo, for example, has sold new cars that warn other Volvos of slippery roads ahead using C-V2X communications since 2016 in Denmark, and has announced plans to complement that with general accident-ahead warnings and offer the same functionality in other European markets over time.

In the medium term, V2X is perceived as a key enabler for autonomous driving, assuming it would be allowed to intervene into the actual driving. In that case, vehicles would be able to join platoons the way HGVs do. With the advent of connected and autonomous mobility, V2X discussions are seen to play an important role, especially in the context of teleoperations for autonomous vehicles and platooning

Hobbyists have documented open source projects capturing V2X packets or plotting passing vehicle speeds.

## Standardisation history

### IEEE 802.11p

WLAN-based V2X communication is based on a set of standards drafted by the American Society for Testing and Materials (ASTM). The ASTM E 2213 series of standards looks at wireless communication for high-speed information exchange between vehicles themselves as well as road infrastructure. The first standard of this series was published 2002. Here the acronym Wireless Access in Vehicular Environments (WAVE) was first used for V2X communication.

From 2004 onwards the Institute of Electrical and Electronics Engineers (IEEE) started to work on wireless access for vehicles under the umbrella of their standards family IEEE 802.11 for Wireless Local Area Networks (WLAN). Their initial standard for wireless communication for vehicles is known as IEEE 802.11p and is based on the work done by the ASTM. Later on in 2012 IEEE 802.11p was incorporated in IEEE 802.11.

Around 2007 when IEEE 802.11p got stable, IEEE started to develop the 1609.x standards family standardising applications and a security framework (IEEE uses the term WAVE), and soon after SAE started to specify standards for V2V communication applications. SAE uses the term DSRC for this technology (this is how the term was coined in the US). In parallel at ETSI the technical committee for Intelligent transportation system (ITS) was founded and started to produce standards for protocols and applications (ETSI coined the term ITS-G5). All these standards are based on IEEE 802.11p technology.

Between 2012 and 2013, the Japanese Association of Radio Industries and Businesses (ARIB) specified, also based on IEEE 802.11, a V2V and V2I communication system in the 700 MHz frequency band.

In 2015 ITU published as summary of all V2V and V2I standards that are worldwide in use, comprising the systems specified by ETSI, IEEE, ARIB, and TTA (Republic of Korea, Telecommunication Technology Association).

### 3GPP

3GPP started standardization work of cellular V2X (C-V2X) in Release 14 in 2014. It is based on LTE as the underlying technology. Specifications were published in 2017. Because this C-V2X functionalities are based on LTE, it is often referred to as LTE-V2X. The scope of functionalities supported by C-V2X includes both direct communication (V2V, V2I) as well as wide area cellular network communication (V2N).

In Release 15, 3GPP continued its C-V2X standardization to be based on 5G. Specifications are published in 2018 as Release 15 comes to completion. To indicate the underlying technology, the term 5G-V2X is often used in contrast to LTE-based V2X (LTE-V2X). Either case, C-V2X is the generic terminology that refers to the V2X technology using the cellular technology irrespective of the specific generation of technology.

In Release 16, 3GPP further enhances the C-V2X functionality. The work is currently in progress. In this way, C-V2X is inherently future-proof by supporting migration path to 5G.

Study and analysis were done to compare the effectiveness of direct communication technologies between LTE-V2X PC5 and 802.11p from the perspective of accident avoided and reduction in fatal and serious injuries. The study shows that LTE-V2X achieves higher level of accident avoidance and reduction in injury. It also indicates LTE-V2X performs higher percentage of successful packet delivery and communication range. Another link-level and system-level simulation result indicates that, to achieve the same link performance for both line-of-sight (LOS) and non-line-of-sight (NLOS) scenarios, lower signal-to-noise-ratio (SNR) are achievable by LTE-V2X PC5 interface compared to IEEE 802.11p.

Cellular-based V2X solution also leads to the possibility of further protecting other types of road users (e.g. pedestrian, cyclist) by having PC5 interface to be integrated into smartphones, effectively integrating those road users into the overall C-ITS solution. Vehicle-to-person (V2P) includes Vulnerable Road User (VRU) scenarios to detect pedestrians and cyclists to avoid accident and injuries involving those road users.

As both direct communication and wide area cellular network communication are defined in the same standard (3GPP), both modes of communication will likely be integrated into a single chipset. Commercialization of those chipsets further enhances economy of scale and leads to possibilities to wider range of business models and services using both types of communications.

## Regulatory history

### United States

In 1999 the US Federal Communications Commission (FCC) allocated 75 MHz in the spectrum of 5.850-5.925 GHz for intelligent transport systems.

Since then the US Department of Transportation (USDOT) has been working with a range of stakeholders on V2X. In 2012 a pre-deployment project was implemented in Ann Arbor, Michigan. 2800 vehicles covering cars, motorcycles, buses and HGV of different brands took part using equipment by different manufacturers. The US National Highway Traffic Safety Administration (NHTSA) saw this model deployment as proof that road safety could be improved and that WAVE standard technology was interoperable. In August 2014 NHTSA published a report arguing vehicle-to-vehicle technology was technically proven as ready for deployment. On 20 August 2014 the NHTSA published an Advance Notice of Proposed Rulemaking (ANPRM) in the Federal Register, arguing that the safety benefits of V2X communication could only be achieved if a significant part of the vehicles fleet was equipped. Because of the lack of an immediate benefit for early adopters, the NHTSA proposed a mandatory introduction. On 25 June 2015 the US House of Representatives held a hearing on the matter, where again the NHTSA, as well as other stakeholders argued the case for V2X.

On November 18, 2020, the FCC reallocated 45 MHz in the 5.850–5.895 GHz range to Wi-Fi, and the rest of the V2X band to C-V2X, citing the failure of DSRC to take off. The advocacy organizations ITS America and American Association of State Highway and Transportation Officials sued the FCC, arguing that the decision harms users of DSRC; on August 12, 2022, a federal court permitted the reassignment to go ahead.

### Europe

To acquire EU-wide spectrum, radio applications require a harmonised standard, in case of ITS-G5 ETSI EN 302 571, first published in 2008. A harmonised standard in turn requires an ETSI System Reference Document, here ETSI TR 101 788. Commission Decision 2008/671/EC harmonises the use of the 5875 to 5905 MHz frequency band for transport safety ITS applications. In 2010 the ITS Directive 2010/40/EU was adopted. It aims to assure that ITS applications are interoperable and can operate across national borders, it defines priority areas for secondary legislation, which cover V2X and requires technologies to be mature. In 2014 the European Commission's industry stakeholder “C-ITS Deployment Platform” started working on a regulatory framework for V2X in the EU. It identified key approaches to an EU-wide V2X security Public Key infrastructure (PKI) and data protection, as well as facilitating a mitigation standard to prevent radio interference between ITS-G5 based V2X and road charging systems. The European Commission recognised ITS-G5 as the initial communication technology in its 5G Action Plan and the accompanying explanatory document, to form a communication environment consisting of ITS-G5 and cellular communication as envisioned by EU Member States. Various pre-deployment projects exist at EU or EU Member State level, such as SCOOP@F, the Testfeld Telematik, the digital testbed Autobahn, the Rotterdam-Vienna ITS Corridor, Nordic Way, COMPASS4D or C-ROADS. There exist real scenarios of implementation V2X standard as well. The first commercial project where V2X standard is used for Intersection movement assist use-case. It has been realized in Brno City / Czech Republic where 80 pcs of cross intersections are controlled by V2X communication standard from public transport vehicles of municipality Brno.

## Spectrum allocation

Spectrum allocation for C-ITS in various countries is shown in the following table. Due to the standardization of V2X in 802.11p preceding C-V2X standardization in 3GPP, spectrum allocation was originally intended for the 802.11p based system. However, the regulations are technology neutral so that the deployment of C-V2X is not excluded.

In 2022, US Federal Courts told the FCC that it could reallocate 45 MHz of V2X spectrum to wireless and cellular carriers, citing years of no use by V2X constituents.

| Country | Spectrum (MHz) | Allocated bandwidth (MHz) |
|---|---|---|
| Australia | 5855 – 5925 | 70 |
| China | 5905 – 5925 | 20 |
| Europe | 5875 – 5905 | 30 |
| Japan | 755.5 – 764.5 and 5770 – 5850 | 9 and 80 |
| Korea | 5855 – 5925 | 70 |
| Singapore | 5875 – 5925 | 50 |
| USA | 5895 – 5925 | 30 |

## Consideration in the transition period

The deployment of V2X technology (either C-V2X or 802.11p based products) will occur gradually over time. New cars will be equipped with either of the two technologies starting around 2020 and its proportion on the road is expected to increase gradually. The Volkswagen Golf 8th generation was the first passenger car to be fitted with V2X technology powered by NXP technology. In the meantime, existing (legacy) vehicles will continue to exist on the road. This implies that the V2X capable vehicles will need to co-exist with non-V2X (legacy) vehicles or with V2X vehicles of incompatible technology.

The main obstacles to its adoption are legal issues and the fact that, unless almost all vehicles adopt it, its effectiveness is limited. British weekly *The Economist* argued in 2016 that autonomous driving is more driven by regulations than by technology.

However, a 2017 study indicated that there are benefits in reducing traffic accidents even during the transitional period in which the technology is being adopted in the market.
