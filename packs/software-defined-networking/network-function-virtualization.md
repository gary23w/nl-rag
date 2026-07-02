---
title: "Network function virtualization"
source: https://en.wikipedia.org/wiki/Network_function_virtualization
domain: software-defined-networking
license: CC-BY-SA-4.0
tags: software-defined networking, sdn, openflow, network function virtualization
fetched: 2026-07-02
---

# Network function virtualization

**Network function virtualization** (**NFV**) is a network architecture concept that leverages IT virtualization technologies to virtualize entire classes of network node functions into building blocks that may connect, or chain together, to create and deliver communication services.

NFV relies upon traditional server-virtualization techniques, such as those used in enterprise IT. A **virtualized network function**, or **VNF**, is implemented within one or more virtual machines or containers running different software and processes, on top of commercial off the shelf (COTS) high-volume servers, switches and storage devices, or even cloud computing infrastructure, instead of having custom hardware appliances for each network function thereby avoiding vendor lock-in.

For example, a virtual session border controller could be deployed to protect a network without the typical cost and complexity of obtaining and installing physical network protection units. Other examples of NFV include virtualized load balancers, firewalls, intrusion detection devices and WAN accelerators to name a few.

Decoupling the network function software from the customized hardware platform creates a flexible network architecture that enables agile network management, faster new service roll outs with significant reduction in CAPEX and OPEX.

## Background

Product development within the telecommunication industry has traditionally followed rigorous standards for stability, protocol adherence and quality, reflected by the use of the term carrier grade to designate equipment demonstrating this high reliability and performance factor. While this model worked well in the past, it inevitably led to long product cycles, a slow pace of development and reliance on proprietary or specific hardware, e.g., bespoke application-specific integrated circuits (ASICs). This development model resulted in significant delays when rolling out new services, posed complex interoperability challenges and significant increase in CAPEX/OPEX when scaling network systems & infrastructure and enhancing network service capabilities to meet increasing network load and performance demands. Moreover, the rise of significant competition in communication service offerings from agile organizations operating at large scale on the public Internet (such as Google Talk, Skype, Netflix) has spurred service providers to look for innovative ways to disrupt the status quo and increase revenue streams.

## History

In October 2012, a group of telecom operators published a white paper at a conference in Darmstadt, Germany, on software-defined networking (SDN) and OpenFlow. The Call for Action concluding the White Paper led to the creation of the Network Functions Virtualization (NFV) Industry Specification Group (ISG) within the European Telecommunications Standards Institute (ETSI). The ISG was made up of representatives from the telecommunication industry from Europe and beyond. ETSI ISG NFV addresses many aspects, including functional architecture, information model, data model, protocols, APIs, testing, reliability, security, future evolutions, etc.

The ETSI ISG NFV has announced the Release 5 of its specifications since May 2021 aiming to produce new specifications and extend the already published specifications based on new features and enhancements.

Since the publication of the white paper, the group has produced over 100 publications, which have gained wider acceptance in the industry and are being implemented in prominent open source projects like OpenStack, ONAP, Open Source MANO (OSM) to name a few. Due to active cross-liaison activities, the ETSI NFV specifications are also being referenced in other SDOs like 3GPP, IETF, ETSI MEC etc.

## Framework

The NFV framework consists of three main components:

1. Virtualized network functions (VNFs) are software implementations of network functions that can be deployed on a network functions virtualization infrastructure (NFVI).
2. Network functions virtualization infrastructure (NFVI) is the totality of all hardware and software components that build the environment where NFVs are deployed. The NFV infrastructure can span several locations. The network providing connectivity between these locations is considered as part of the NFV infrastructure.
3. Network functions virtualization management and orchestration architectural framework (NFV-MANO Architectural Framework) is the collection of all functional blocks, data repositories used by these blocks, and reference points and interfaces through which these functional blocks exchange information for the purpose of managing and orchestrating NFVI and VNFs.

The building block for both the NFVI and the NFV-MANO is the NFV platform. In the NFVI role, it consists of both virtual and physical processing and storage resources, and virtualization software. In its NFV-MANO role it consists of VNF and NFVI managers and virtualization software operating on a hardware controller. The NFV platform implements carrier-grade features used to manage and monitor the platform components, recover from failures and provide effective security – all required for the public carrier network.

## Practical aspects

A service provider that follows the NFV design implements one or more virtualized network functions, or *VNFs*. A VNF by itself does not automatically provide a usable product or service to the provider's customers. To build more complex services, the notion of *service chaining* is used, where multiple VNFs are used in sequence to deliver a service.

Another aspect of implementing NFV is the *orchestration* process. To build highly reliable and scalable services, NFV requires that the network be able to instantiate VNF instances, monitor them, repair them, and (most important for a service provider business) bill for the services rendered. These attributes, referred to as carrier-grade features, are allocated to an orchestration layer in order to provide high availability and security, and low operation and maintenance costs. Importantly, the orchestration layer must be able to manage VNFs irrespective of the underlying technology within the VNF. For example, an orchestration layer must be able to manage an SBC VNF from vendor X running on VMware vSphere just as well as an IMS VNF from vendor Y running on KVM.

## Distributed NFV

The initial perception of NFV was that virtualized capability should be implemented in data centers. This approach works in many – but not all – cases. NFV presumes and emphasizes the widest possible flexibility as to the physical location of the virtualized functions.

Ideally, therefore, virtualized functions should be located where they are the most effective and least expensive. That means a service provider should be free to locate NFV in all possible locations, from the data center to the network node to the customer premises. This approach, known as distributed NFV, has been emphasized from the beginning as NFV was being developed and standardized, and is prominent in the recently released NFV ISG documents.

For some cases there are clear advantages for a service provider to locate this virtualized functionality at the customer premises. These advantages range from economics to performance to the feasibility of the functions being virtualized.

The first ETSI NFV ISG-approved public multi-vendor proof of concept (PoC) of D-NFV was conducted by Cyan, Inc., RAD, Fortinet and Certes Networks in Chicago in June, 2014, and was sponsored by CenturyLink. It was based on RAD's dedicated customer-edge D-NFV equipment running Fortinet's Next Generation Firewall (NGFW) and Certes Networks’ virtual encryption/decryption engine as Virtual Network Functions (VNFs) with Cyan's Blue Planet system orchestrating the entire ecosystem. RAD's D-NFV solution, a Layer 2/Layer 3 network termination unit (NTU) equipped with a D-NFV X86 server module that functions as a virtualization engine at the customer edge, became commercially available by the end of that month. During 2014 RAD also had organized a D-NFV Alliance, an ecosystem of vendors and international systems integrators specializing in new NFV applications.

## NFV modularity benefits

When designing and developing the software that provides the VNFs, vendors may structure that software into software components (implementation view of a software architecture) and package those components into one or more images (deployment view of a software architecture). These vendor-defined software components are called VNF Components (VNFCs). VNFs are implemented with one or more VNFCs and it is assumed, without loss of generality, that VNFC instances map 1:1 to VM Images.

VNFCs should in general be able to scale up and/or scale out. By being able to allocate flexible (virtual) CPUs to each of the VNFC instances, the network management layer can scale up (i.e., scale *vertically*) the VNFC to provide the throughput/performance and scalability expectations over a single system or a single platform. Similarly, the network management layer can scale out (i.e., *scale horizontally*) a VNFC by activating multiple instances of such VNFC over multiple platforms and therefore reach out to the performance and architecture specifications whilst not compromising the other VNFC function stabilities.

## Relationship to SDN

Network Functions Virtualisation is highly complementary to SDN. In essence, SDN is an approach to building data networking equipment and software that separates and abstracts elements of these systems. It does this by decoupling the control plane and data plane from each other, such that the control plane resides centrally and the forwarding components remain distributed. The control plane interacts with both northbound and southbound. In the northbound direction the control plane provides a common abstracted view of the network to higher-level applications and programs using high-level APIs and novel management paradigms, such as Intent-based networking. In the southbound direction the control plane programs the forwarding behavior of the data plane, using device level APIs of the physical network equipment distributed around the network.

Thus, NFV is not dependent on SDN or SDN concepts, but NFV and SDN can cooperate to enhance the management of a NFV infrastructure and to create a more dynamic network environment. It is entirely possible to implement a virtualized network function (VNF) as a standalone entity using existing networking and orchestration paradigms. However, there are inherent benefits in leveraging SDN concepts to implement and manage an NFV infrastructure, particularly when looking at the management and orchestration of Network Services (NS), composed of different type of Network Functions (NF), such as Physical Network Functions (PNF) and VNFs, and placed between different geo-located NFV infrastructures, and that's why multivendor platforms are being defined that incorporate SDN and NFV in concerted ecosystems.

An NFV system needs a central orchestration and management system that takes operator requests associated with an NS or a VNF, translates them into the appropriate processing, storage and network configuration needed to bring the NS or VNF into operation. Once in operation, the VNF and the networks it is connected to potentially must be monitored for capacity and utilization, and adapted if necessary.

All network control functions in an NFV infrastructure can be accomplished using SDN concepts and NFV could be considered one of the primary SDN use cases in service provider environments. For example, within each NFV infrastructure site, a VIM could rely upon an SDN controller to set up and configure the overlay networks interconnecting (e.g. VXLAN) the VNFs and PNFs composing an NS. The SDN controller would then configure the NFV infrastructure switches and routers, as well as the network gateways, as needed. Similarly, a Wide Area Infrastructure Manager (WIM) could rely upon an SDN controller to set up overlay networks to interconnect NSs that are deployed to different geo-located NFV infrastructures. It is also apparent that many SDN use-cases could incorporate concepts introduced in the NFV initiative. Examples include where the centralized controller is controlling a distributed forwarding function that could in fact be also virtualized on existing processing or routing equipment.

## Industry impact

NFV has proven a popular standard even in its infancy. Its immediate applications are numerous, such as virtualization of mobile base stations, platform as a service (PaaS), content delivery networks (CDN), fixed access and home environments. The potential benefits of NFV is anticipated to be significant. Virtualization of network functions deployed on general purpose standardized hardware is expected to reduce capital and operational expenditures, and service and product introduction times. Many major network equipment vendors have announced support for NFV. This has coincided with NFV announcements from major software suppliers who provide the NFV platforms used by equipment suppliers to build their NFV products.

However, to realize the anticipated benefits of virtualization, network equipment vendors are improving IT virtualization technology to incorporate carrier-grade attributes required to achieve high availability, scalability, performance, and effective network management capabilities. To minimize the total cost of ownership (TCO), carrier-grade features must be implemented as efficiently as possible. This requires that NFV solutions make efficient use of redundant resources to achieve five-nines availability (99.999%), and of computing resource without compromising performance predictability.

The NFV platform is the foundation for achieving efficient carrier-grade NFV solutions. It is a software platform running on standard multi-core hardware and built using open source software that incorporates carrier-grade features. The NFV platform software is responsible for dynamically reassigning VNFs due to failures and changes in traffic load, and therefore plays an important role in achieving high availability. There are numerous initiatives underway to specify, align and promote NFV carrier-grade capabilities such as ETSI NFV Proof of Concept, ATIS Open Platform for NFV Project, Carrier Network Virtualization Awards and various supplier ecosystems.

The vSwitch, a key component of NFV platforms, is responsible for providing connectivity both VM-to-VM (between VMs) and between VMs and the outside network. Its performance determines both the bandwidth of the VNFs and the cost-efficiency of NFV solutions. The standard Open vSwitch's (OVS) performance has shortcomings that must be resolved to meet the needs of NFVI solutions. Significant performance improvements are being reported by NFV suppliers for both OVS and Accelerated Open vSwitch (AVS) versions.

Virtualization is also changing the way availability is specified, measured and achieved in NFV solutions. As VNFs replace traditional function-dedicated equipment, there is a shift from equipment-based availability to a service-based, end-to-end, layered approach. Virtualizing network functions breaks the explicit coupling with specific equipment, therefore availability is defined by the availability of VNF services. Because NFV technology can virtualize a wide range of network function types, each with their own service availability expectations, NFV platforms should support a wide range of fault tolerance options. This flexibility enables CSPs to optimize their NFV solutions to meet any VNF availability requirement.

## Management and orchestration (MANO)

ETSI has already indicated that an important part of controlling the NFV environment be done through automated orchestration. NFV Management and Orchestration (NFV-MANO) refers to a set of functions within an NFV system to manage and orchestrate the allocation of virtual infrastructure resources to virtualized network functions (VNFs) and network services (NSs). They are the brains of the NFV system and a key automation enabler.

The main functional blocks within the NFV-MANO architectural framework (ETSI GS NFV-006 ) are:

- Network Functions Virtualisation Orchestrator (NFVO);
- Virtualised Network Function Manager (VNFM);
- Virtualised Infrastructure Manager (VIM).

The entry point in NFV-MANO for external operations support systems (OSS) and business support systems (BSS) is the NFVO, which is in charge of managing the lifecycle of NS instances. The management of the lifecycle of VNF instances constituting an NS instance is delegated by the NFVO to one more or VNFMs. Both the NFVO and the VNFMs uses the services exposed by one or more VIMs for allocating virtual infrastructure resources to the objects they manage. Additional functions are used for managing containerized VNFs: the Container Infrastructure Service Management (CISM) and the Container Image Registry (CIR) functions. The CISM is responsible for maintaining the containerized workloads while the CIR is responsible for storing and maintaining information of OS container software images The behavior of the NFVO and VNFM is driven by the contents of deployment templates (a.k.a. NFV descriptors) such as a Network Service Descriptor (NSD) and a VNF Descriptor (VNFD).

ETSI delivers a full set of standards **enabling an open ecosystem** where Virtualized Network Functions (VNFs) can be interoperable with independently developed management and orchestration systems, and where the components of a management and orchestration system are themselves interoperable. This includes a set of Restful API specifications as well as the specifications of a packaging format for delivering VNFs to service providers and of the deployment templates to be packaged with the software images to enable managing the lifecycle of VNFs. Deployment templates can be based on TOSCA or YANG.

An OpenAPI (a.k.a. Swagger) representation of the API specifications is available and maintained on the ETSI forge server, along with TOSCA and YANG definition files to be used when creating deployment templates.

The full set of published specifications is summarized in the table below.

| Specification | Title |
|---|---|
| ETSI GS NFV-SOL 001 | NFV descriptors based on TOSCA specification |
| ETSI GS NFV-SOL 002 | RESTful protocols specification for the Ve-Vnfm Reference Point |
| ETSI GS NFV-SOL 003 | RESTful protocols specification for the Or-Vnfm Reference Point |
| ETSI GS NFV-SOL 004 | VNF Package and PNFD Archive specification |
| ETSI GS NFV-SOL 005 | RESTful protocols specification for the Os-Ma-nfvo Reference Point |
| ETSI GS NFV-SOL 006 | NFV descriptors based on YANG Specification |
| ETSI GS NFV-SOL 007 | Network Service Descriptor file structure specification |
| ETSI GS NFV-SOL 009 | RESTful protocols specification for the management of NFV-MANO |
| ETSI GS NFV-SOL 010 | VNF Snapshot Package specification |
| ETSI GS NFV-SOL 011 | RESTful protocols specification for the Or-Or Reference Point |
| ETSI GS NFV-SOL 012 | RESTful protocols specification for the Policy Management interface |
| ETSI GS NFV-SOL 013 | Specification of common aspects for RESTful NFV MANO APIs |
| ETSI GS NFV-SOL 014 | YAML data model specification for descriptor-based virtualised resource management |
| ETSI GS NFV-SOL 015 | Specification of Patterns and Conventions for RESTful NFV-MANO APIs |
| ETSI GS NFV-SOL 016 | NFV-MANO procedures specification |
| ETSI GS NFV-SOL 018 | Profiling specification of protocol and data model solutions for OS Container management and orchestration |

An overview of the different versions of the OpenAPI representations of NFV-MANO APIs is available on the ETSI NFV wiki.

The OpenAPI files as well as the TOSCA YAML definition files and YANG modules applicable to NFV descriptors are available on the ETSI Forge.

Additional studies are ongoing within ETSI on possible enhancement to the NFV-MANO framework to improve its automation capabilities and introduce autonomous management mechanisms (see ETSI GR NFV-IFA 041 )

## Performance study

Recent performance study on NFV focused on the throughput, latency and jitter of virtualized network functions (VNFs), as well as NFV scalability in terms of the number of VNFs a single physical server can support. Open source NFV platforms are available, one representative is openNetVM. openNetVM is a high performance NFV platform based on DPDK and Docker containers. openNetVM provides a flexible framework for deploying network functions and interconnecting them to build service chains. openNetVM is an open source version of the NetVM platform described in NSDI 2014 and HotMiddlebox 2016 papers, released under the BSD license. The source code can be found at GitHub:openNetVM

## Cloud-native network functions

From 2018, many VNF providers began to migrate many of their VNFs to a container-based architecture. Such VNFs also known as Cloud-Native Network Functions (CNF) utilize many innovations deployed commonly on internet infrastructure. These include auto-scaling, supporting a continuous delivery / DevOps deployment model, and efficiency gains by sharing common services across platforms. Through service discovery and orchestration, a network based on CNFs will be more resilient to infrastructure resource failures. Utilizing containers, and thus dispensing with the overhead inherent in traditional virtualization through the elimination of the guest OS can greatly increase infrastructure resource efficiency.
