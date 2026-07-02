---
title: "Open RAN"
source: https://en.wikipedia.org/wiki/Open_RAN
domain: network-slicing-5g
license: CC-BY-SA-4.0
tags: 5g network slicing, logical network partition, slice isolation, service-level networking
fetched: 2026-07-02
---

# Open RAN

**Open RAN**, or **Open Radio Access Network** architecture is based on 3GPP standards for Radio Access Networks (RAN) but contains many extensions, disaggregates RAN components and makes their interfaces open, aiming to improve flexibility and interoperability. RAN hardware and software are cloudified/virtualized, and it includes intelligent management (SMO).

Those open interfaces aim for mixing components from different vendors and quicker deployment of new services. Open RAN standardization is led by the O-RAN ALLIANCE.

*Cloudification* means disaggregating hardware and software, making RAN software cloud-native functions running on a general-purpose hardware.

*Intelligent open management* includes automated management and orchestration systems which can utilize Artificial Intelligence and Machine Learning for life cycle management of network functions.

*Open interfaces*: standardized open interfaces, such as the O-RAN ALLIANCE's specifications and 3GPP-defined interfaces, facilitate interoperability between disaggregated RAN components.

## Key components

In Open RAN, the RAN is split into three main blocks: the Radio Unit (RU), the Distributed Unit (DU), and the Centralised Unit (CU). The RU performs basic RF and low-PHY functions such as precoding and beamforming. The DU performs additional PHY functions such as scrambling and modulation, and handles MAC and RLC functions such as radio resource allocation. The CU handles functions such as SDAP and RRC.

*RAN Intelligent Controller* (RIC) is an optional virtualized optimization technology for 5G. It adds programmability to a new or existing RAN and allows SON-like (Self-Optimizing Networks) capabilities. The optimization in RIC is boosted by policy-driven closed loop automation and AI/ML. In O-RAN deployments, there are the *near real-time RIC* (near-RT RIC) which operates on sub-100 millisecond intervals, and the *non real-time RIC* (non-RT RIC) which operates on intervals longer than 1 second.

The near-RT RIC houses *xApps*, which are programs that optimize functions such as beamforming, traffic steering, and power control. The non-RT RIC houses *rApps*, which manage longer-term policies such as network slicing.

The fronthaul interface lies between radio Units (RU) and baseband units (Distributed Units (DU)). It is a focus area in Open RAN.

O-RAN has specified an eCPRI-based 7.2x open interface to be used in the fronthaul, allowing connections between radio units and baseband units of different vendors.

### Near-RT RIC

The near-RT RIC really houses multiple interworking components.

- *Internal messaging infrastructure* connects the xApps, platform services, and interface (O1, A1, E2) terminations to each other. O-RAN Alliance specifies not what technology the near-RT RIC must use, but there are certain functionalities that this internal messaging infrastructure must provide.
- The *subscription manager* allows xApps to listen to functions exposed over the E2 interface.
- The *security sub-system* prevents malicious xApps from leaking sensitive RAN data or negatively affecting RAN performance.
- The RAN *Network Information Base (NIB) Database* stores information from the E2 interface, typically KPMs from RANs and UEs. The UE-NIB contains information about UEs, specifically their identity key (UE-ID), which allows for xApps to control UEs. These NIBs may be queried through the *Shared Data Layer API*, usually by xApps.
- *Conflict mitigation* prevents RAN performance from being degraded by xApps making conflicting managing decisions on RANs. This is an emerging functionality and is not included in all near-RT RIC implementations.
- xApps are the meat and potatoes of the near-RT RIC, and the other components exist to support the xApps. xApps are typically realized as Kubernetes or Docker containers. The O-RAN alliance only stipulates that a few KPIs are exposed to the xApps.

## O-RAN ALLIANCE

O-RAN ALLIANCE (O-RAN) was founded in 2018 by AT&T, China Mobile, Deutsche Telekom, NTT DOCOMO and Orange to promote open mobile networks. O-RAN has over 30 operator members and almost 300 contributors.

O-RAN specifications define the parts of the O-RAN Architecture, which can be used to develop Open RAN solutions.

O-RAN ALLIANCE also handles the activities of the earlier xRAN and C-RAN forums.
