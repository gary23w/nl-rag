---
title: "Deep content inspection"
source: https://en.wikipedia.org/wiki/Deep_content_inspection
domain: snort-ids
license: CC-BY-SA-4.0
tags: snort ids, network intrusion detection, packet analyzer, signature based detection, intrusion prevention system
fetched: 2026-07-02
---

# Deep content inspection

**Deep content inspection** (**DCI**) is a form of network filtering that examines an entire file or MIME object as it passes an inspection point, searching for viruses, spam, data loss, key words or other content level criteria. Deep Content Inspection is considered the evolution of deep packet inspection with the ability to look at what the actual content contains instead of focusing on individual or multiple packets. Deep content inspection allows services to keep track of content across multiple packets so that the signatures they may be searching for can cross packet boundaries and yet they will still be found. An exhaustive form of network traffic inspection in which Internet traffic is examined across all the seven OSI ISO layers, and most importantly, the application layer.

## Background

Traditional inspection technologies are unable to keep up with the recent outbreaks of widespread attacks. Unlike inspection methods such as deep packet inspection (DPI), where only the data part (and possibly also the header) of a packet are inspected, deep content inspection (DCI)-based systems are exhaustive, such that network traffic packets are reassembled into their constituting objects, un-encoded and/or decompressed as required, and presented to be inspected for malware, right-of-use, compliance, and understanding of the traffic's intent. If this reconstruction and comprehension can be done in real-time, then real-time policies can be applied to traffic, preventing the propagation of malware, spam and valuable data loss. Further, with DCI, the correlation and comprehension of the digital objects transmitted in many communication sessions leads to new ways of network performance optimization and intelligence regardless of protocol or blended communication sessions.

Historically, DPI was developed to detect and prevent intrusion. It was then used to provide Quality of Service where the flow of network traffic can be prioritized such that latency-sensitive traffic types (e.g., Voice over IP) can be utilized to provide higher flow priority.

New generation of Network Content Security devices such as Unified Threat Management or Next Generation Firewalls (Garner RAS Core Research Note G00174908) use DPI to prevent attacks from a small percentage of viruses and worms; the signatures of these malware fit within the payload of a DPI's inspection scope. However, the detection and prevention of a new generation of malware such as Conficker and Stuxnet is only possible through the exhaustive analysis provided by DCI.

### The evolution of DPI systems

Computer networks send information across a network from one point to another; the data (sometimes referred to as the payload) is ‘encapsulated’ within an IP packet, which looks as follows:

*The IP Header provides address information - the sender and destination addresses, while the TCP/UDP Header provided other pertinent information such as the port number, etc.

As networks evolve, inspection techniques evolve; all attempting to understand the payload. Throughout the last decade there have been vast improvements including:

### Packet filtering

Historically, inspection technology examined only the IP Header and the TCP/UDP Header. Dubbed as ‘Packet Filtering’, these devices would drop sequence packets, or packets that are not allowed on a network. This scheme of network traffic inspection was first used by firewalls to protect against packet attacks.

### Stateful packet inspection

Stateful packet inspection was developed to examine header information and the packet content to increase source and destination understanding. Instead of letting the packets through as a result of their addresses and ports, packets stayed on the network if the context was appropriate to the networks’ current ‘state’. This scheme was first used by Check Point firewalls and eventually Intrusion Prevention/Detection Systems.

### Deep packet inspection

Deep packet inspection is the predominant inspection tool used to analyze data packets passing through the network, including the headers and the data protocol structures. These technologies scan packet streams and look for offending patterns.

To be effective, Deep Packet Inspection Systems must ‘string’ match Packet Payloads to malware signatures and specification signatures (which dictate what the request/response should be like) at wire speeds. To do so, FPGAs, or Field Programmable Gate Arrays, Network Processors, or even Graphics Processing Units (GPUs) are programmed to be hardwired with these signatures and, as a result, traffic that passes through such circuitry is quickly matched.

While using hardware allows for quick and inline matches, DPI systems have the following limitations including;

**Hardware limitations:** Since DPI systems implement their pattern matching (or searches for ‘offending’ patterns) through hardware, these systems are typically limited by:

- The number of circuits a high-end DPI chip can have; as of 2011, this of a high end DPI system can, optimally, process around 512 request/response per session.
- The memory available for pattern matches; as of 2011, high-end DPI systems are capable of matches of up to 60,000 unique signatures

**Payload limitations:** Web applications communicate content using binary-to-text encoding, compression (zipped, archived, etc.), obfuscation and even encryption. As such payload structure is becoming more complex such that straight ‘string’ matching of the signatures is no longer sufficient. The common workaround is to have signatures be similarly ‘encoded’ or zipped which, given the above ‘search limitations’, cannot scale to support every application type, or nested zipped or archived files.

## Deep content inspection

Parallel to the development of Deep Packet Inspection, the beginnings of Deep Content Inspection can be traced back as early as 1995 with the introduction of proxies that stopped malware or spam. Deep Content Inspection, can be seen as the third generation of Network Content Inspection, where network content is exhaustively examined,

### First generation – secure web gateway or proxy-based network content inspection

Proxies have been deployed to provide internet caching services to retrieve objects and then forward them. Consequently, all network traffic is intercepted, and potentially stored. These graduated to what is now known as secure web gateways, proxy-based inspections retrieve and scans object, script, and images.

Proxies, which relies on a fetch the content first if it were not cached, then forwarding the content to the recipient introduced some form of file inspection as early as 1995 when MAILsweeper was released by Content Technologies (now Clearswift), which was then replaced by MIMEsweeper in 2005. 2006 saw the release of the open-source, cross-platform antivirus software ClamAV provided support for caching proxies, Squid and NetCache. Using the Internet Content Adaptation Protocol (ICAP), a proxy will pass the downloaded content for scanning to an ICAP server running an anti-virus software. Since complete files or ‘objects’ were passed for scanning, proxy-based anti-virus solutions are considered the first generation of network content inspection.

BlueCoat, WebWasher and Secure Computing Inc. (now McAfee, now a division of Intel), provided commercial implementations of proxies, eventually becoming a standard network element in most enterprise networks.

Limitations: While proxies (or secure web gateways) provide in-depth network traffic inspection, their use is limited as they:

- require network reconfiguration which is accomplished through – a) end-devices to get their browsers to point to these proxies; or b) on the network routers to get traffic routed through these devices
- are limited to web (http) and ftp protocols; cannot scan other protocols such as e-mail
- and finally, proxy architectures which are typically built around Squid, which cannot scale with concurrent sessions, limiting their deployment to enterprises.

### Second generation – gateway/firewall-based network traffic proxy-assisted deep packet inspection

The Second generation of Network Traffic Inspection solutions were implemented in firewalls and/or UTMs. Given that network traffic is choked through these devices, in addition to DPI inspection, proxy-like inspection is possible. This approach was first pioneered by NetScreen Technologies Inc. (acquired by Juniper Networks Inc). However, given the expensive cost of such operation, this feature was applied in tandem with a DPI system and was only activated on a-per-need basis, or when content failed to be qualified through the DPI system.

### Third generation – transparent, application-aware network content inspection, or deep content inspection

The third, and current, generation of network content inspection, known as deep content inspection solutions, are implemented as fully transparent devices that perform full application level content inspection at wire speed. In order to understand the communication session's intent —in its entirety—, a Deep Content Inspection System must scan both the handshake and payload. Once the digital objects (executables, images, JavaScript's, .pdfs, etc. also referred to as Data-In-Motion) carried within the payload are constructed, usability, compliance and threat analysis of this session and its payload can be achieved. Given that the handshake sequence and complete payload of the session is available to the DCI system, unlike DPI systems where simple pattern matching and reputation search are only possible, exhaustive object analysis is possible. The inspection provided by DCI systems can include signature matching, behavioral analysis, regulatory and compliance analysis, and correlation of the session under inspection to the history of previous sessions. Because of the availability of the complete payload's objects, and these schemes of inspection, deep content inspection systems are typically deployed where high-grade security and compliance is required or where end-point security solutions are not possible such as in bring your own device, or Cloud installations.

This third generation approach of deep content inspection was developed within the defence and intelligence community, first appearing in guard products such as SyBard, and later by Wedge Networks Inc.. Key-implementation highlights of this company's approach can be deduced from their patent USPTO# 7,630,379

The main differentiators of deep content inspection are:

#### Content

Deep content inspection is content-focused instead of analyzing packets or classifying traffic based on application types such as in Next Generation Firewalls. "Understanding" content and its intent is the highest level of intelligence to be gained from network traffic. This is important as information flow is moving away from packet, towards application, and ultimately to content.

Example inspection levels:

- Packet: Random Sample to get larger picture
- Application: Group or application profiling. Certain applications, or areas of applications, are allowed / not allowed or scanned further.
- Content: Look at everything. Scan everything. Subject the content to rules of inspection (such as Compliance/Data Loss Prevention rules). Understand the intent.

#### Multi-services inspection

Because of the availability of the complete objects of that payload to a Deep Content Inspection system, some of the services/inspection examples can include:

- Anti Malware
- Anti-spam
- Data Loss for Data In Motion
- Zero-Day or Unknown Threats
- Network Traffic Visualization and Analytics
- Code Attacks/Injection
- Content Manipulation

## Applications of deep content inspection

DCI is currently being adopted by enterprises, service providers and governments as a reaction to increasingly complex internet traffic with the benefits of understanding complete file types and their intent. Typically, these organizations have mission-critical applications with rigid requirements.

## Obstacles to deep content inspection

### Network throughput

This type of inspection deals with real time protocols that only continue to increase in complexity and size. One of the key barriers for providing this level of inspection, that is looking at all content, is dealing with network throughput. Solutions must overcome this issue while not introducing latency into the network environment. They must also be able to effectively scale up to meet tomorrow's demands and the demands envisioned by the growing Cloud Computing trend. One approach is to use selective scanning; however, to avoid compromising accuracy, the selection criteria should be based on recurrence. The following patent USPTO# 7,630,379 provides a scheme as to how deep content inspection can be carried out effectively using a recurrence selection scheme. The novelty introduced by this patent is that it addresses issues such as content (E.g., an mp3 file) that could have been renamed before transmission.

### Accuracy of services

Dealing with the amount of traffic and information and then applying services requires very high speed look ups to be able to be effective. Need to compare against full services platforms or else having all traffic is not being utilized effectively. An example is often found in dealing with Viruses and Malicious content where solutions only compare content against a small virus database instead of a full and complete one.
