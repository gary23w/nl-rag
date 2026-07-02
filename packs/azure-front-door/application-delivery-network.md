---
title: "Application delivery network"
source: https://en.wikipedia.org/wiki/Application_delivery_network
domain: azure-front-door
license: CC-BY-SA-4.0
tags: azure front door, global load balancer azure, application delivery azure, edge routing azure
fetched: 2026-07-02
---

# Application delivery network

An **application delivery network** (**ADN**) is a suite of technologies that, when deployed together, provide availability, security, visibility, and acceleration for Internet applications such as websites. ADN components provide supporting functionality that enables website content to be delivered to visitors and other users of that website, in a fast, secure, and reliable way.

Gartner defines application delivery networking as the combination of WAN optimization controllers (WOCs) and application delivery controllers (ADCs). At the data center end of an ADN is the ADC, an advanced traffic management device that is often also referred to as a web switch, content switch, or multilayer switch, the purpose of which is to distribute traffic among a number of servers or geographically dislocated sites based on application specific criteria. In the branch office portion of an ADN is the WAN optimization controller, which works to reduce the number of bits that flow over the network using caching and compression, and shapes TCP traffic using prioritization and other optimization techniques. Some WOC components are installed on PCs or mobile clients, and there is typically a portion of the WOC installed in the data center. Application delivery networks are also offered by some CDN vendors.

The ADC, one component of an ADN, evolved from layer 4-7 switches in the late 1990s when it became apparent that traditional load balancing techniques were not robust enough to handle the increasingly complex mix of application traffic being delivered over a wider variety of network connectivity options.

## Application delivery techniques

The Internet was designed according to the end-to-end principle. This principle keeps the core network relatively simple and moves the intelligence as much as possible to the network end-points: the hosts and clients. An Application Delivery Network (ADN) enhances the delivery of applications across the Internet by employing a number of optimization techniques. Many of these techniques are based on established best-practices employed to efficiently route traffic at the network layer including redundancy and load balancing

In theory, an Application Delivery Network (ADN) is closely related to a content delivery network. The difference between the two delivery networks lies in the intelligence of the ADN to understand and optimize applications, usually referred to as application fluency. Application Fluent Network (AFN) is based on the concept of Application Fluency to refer to WAN optimization techniques applied at Layer Four to Layer Seven of the OSI model for networks. Application Fluency implies that the network is fluent or intelligent in understanding and being able to optimize delivery of each application. Application Fluent Network is an addition of SDN capabilities. The acronym 'AFN' is used by Alcatel-Lucent Enterprise to refer to an Application Fluent Network.

Application delivery uses one or more layer 4–7 switches, also known as a web switch, content switch, or multilayer switch to intelligently distribute traffic to a pool, also known as a cluster or farm, of servers. The application delivery controller (ADC) is assigned a single virtual IP address (VIP) that represents the pool of servers. Traffic arriving at the ADC is then directed to one of the servers in the pool (cluster, farm) based on a number of factors including application specific data values, application transport protocol, availability of servers, current performance metrics, and client-specific parameters. An ADN provides the advantages of load distribution, increase in capacity of servers, improved scalability, security, and increased reliability through application specific health checks.

Increasingly the ADN comprises a redundant pair of ADC on which is integrated a number of different feature sets designed to provide security, availability, reliability, and acceleration functions. In some cases these devices are still separate entities, deployed together as a network of devices through which application traffic is delivered, each providing specific functionality that enhances the delivery of the application.

## ADN optimization techniques

### TCP multiplexing

TCP Multiplexing is loosely based on established connection pooling techniques utilized by application server platforms to optimize the execution of database queries from within applications. An ADC establishes a number of connections to the servers in its pool and keeps the connections open. When a request is received by the ADC from the client, the request is evaluated and then directed to a server over an existing connection. This has the effect of reducing the overhead imposed by establishing and tearing down the TCP connection with the server, improving the responsiveness of the application.

Some ADN implementations take this technique one step further and also multiplex HTTP and application requests. This has the benefit of executing requests in parallel, which enhances the performance of the application.

### TCP optimization

There are a number of Request for Comments (RFCs) which describe mechanisms for improving the performance of TCP. Many ADN implement these RFCs in order to provide enhanced delivery of applications through more efficient use of TCP.

The RFCs most commonly implemented are:

- Delayed Acknowledgements
- Nagle Algorithm
- Selective Acknowledgements
- Explicit Congestion Notification ECN
- Limited and Fast Retransmits
- Adaptive Initial Congestion Windows

### Data compression and caching

ADNs also provide optimization of application data through caching and compression techniques. There are two types of compression used by ADNs today: industry standard HTTP compression and proprietary data reduction algorithms. It is important to note that the cost in CPU cycles to compress data when traversing a LAN can result in a negative performance impact and therefore best practices are to only utilize compression when delivering applications via a WAN or particularly congested high-speed data link.

HTTP compression is asymmetric and transparent to the client. Support for HTTP compression is built into web servers and web browsers. All commercial ADN products currently support HTTP compression.

A second compression technique is achieved through data reduction algorithms. Because these algorithms are proprietary and modify the application traffic, they are symmetric and require a device to reassemble the application traffic before the client can receive it. A separate class of devices known as WAN Optimization Controllers (WOC) provide this functionality, but the technology has been slowly added to the ADN portfolio over the past few years as this class of device continues to become more application aware, providing additional features for specific applications such as CIFS and SMB.

## ADN reliability and availability techniques

### Advanced health checking

Advanced health checking is the ability of an ADN to determine not only the state of the server on which an application is hosted, but the status of the application it is delivering. Advanced health checking techniques allow the ADC to intelligently determine whether or not the content being returned by the server is correct and should be delivered to the client.

This feature enables other reliability features in the ADN, such as resending a request to a different server if the content returned by the original server is found to be erroneous.

### Load balancing algorithms

The load balancing algorithms found in today's ADN are far more advanced than the simplistic round-robin and least connections algorithms used in the early 1990s. These algorithms were originally loosely based on operating systems' scheduling algorithms, but have since evolved to factor in conditions peculiar to networking and application environments. It is more accurate to describe today's "load balancing" algorithms as application routing algorithms, as most ADN employ application awareness to determine whether an application is available to respond to a request. This includes the ability of the ADN to determine not only whether the application is available, but whether or not the application can respond to the request within specified parameters, often referred to as a service level agreement.

Typical industry standard load balancing algorithms available today include:

- Round Robin
- Least Connections
- Fastest Response Time
- Weighted Round Robin
- Weighted Least Connections
- Custom values assigned to individual servers in a pool based on SNMP or other communication mechanism

### Fault tolerance

The ADN provides fault tolerance at the server level, within pools or farms. This is accomplished by designating specific servers as a 'backup' that is activated automatically by the ADN in the event that the primary server(s) in the pool fail.

The ADN also ensures application availability and reliability through its ability to seamlessly "failover" to a secondary device in the event of a hardware or software failure. This ensures that traffic continues to flow in the event of a failure in one device, thereby providing fault tolerance for the applications. Fault tolerance is implemented in ADNs through either a network or serial based connection.

#### Network based failover

The Virtual IP Address (VIP) is shared between two devices. A heartbeat daemon on the secondary device verifies that the primary device is active. In the event that the heartbeat is lost, the secondary device assumes the shared VIP and begins servicing requests. This process is not immediate, and though most ADN replicate sessions from the primary to the secondary, there is no way to guarantee that sessions initiated during the time it takes for the secondary to assume the VIP and begin managing traffic will be maintained.

#### Serial based failover

In a serial connection based failover configuration two ADN devices communicate via a standard RS-232 connection instead of the network, and all sharing of session information and status is exchanged over this connection. Failover is nearly instantaneous, though it suffers from the same constraints regarding sessions initiated while the primary device is failing as network based failover.

## ADN security

### Transport layer security

Although often erroneously assigned to the application layer, SSL is the most common method of securing application traffic through an ADN today. SSL uses PKI to establish a secure connection between the client and the ADN, making it difficult for attackers to decrypt the data in transit or hijack the session.

### Application layer security

#### Resource cloaking

The use of a virtual IP address (VIP) and position of the ADN in the network provides the means through which certain resources can be cloaked, or hidden, from the client. Because the ADN is designed to understand applications and application protocols, such as HTTP, it can manipulate certain aspects of the protocol to cloak the servers in the pool and prevent potentially useful information regarding the software and hardware infrastructure from being exposed.

A typical use of this functionality is to hide the operating system and server software used to host the application. This is usually accomplished by rewriting the Server field in an HTTP response.

A second typical use of this functionality is the exploitation of the ADN's ability to rewrite the URI portion of an HTTP request. The client is presented with a URI and VIP that are known only to the ADN, and upon receiving the request the ADN may either (a) rewrite the URI and send a 302 redirect or (b) transparently translates the URI and responds to the client as if the URI were the right one in the first place.

#### Application firewall

In recent years commercial ADNs have begun to include application firewall functionality to further secure applications during the delivery process. This is a hotly debated subject with many security professionals arguing that the functionality included in an application firewall are unnecessary and should be handled by the application while others consider employing as much security as possible, regardless of position in the delivery network, to be the best practice. Many commercial ADN companies have acquired and integrated these functions and present such features as part of a defense in depth strategy often cited by security professionals.

### Network layer security

The ADN is most often deployed in the DMZ at the edge of the network. This results in exposure to potential network layer attacks including Denial of Service (DoS) from ICMP and SYN floods. As a result, the ADN must necessarily protect not only itself but the applications it is delivering from succumbing to such attacks. The ADN generally employs a number of protections against typical network layer attacks though it does not implement the full security offered by an IPS. Some of the Network Layer Security technologies that may be employed by ADN devices include:

#### Delayed binding

Delayed binding, also called TCP splicing, is the postponement of the connection between the client and the server in order to obtain sufficient information to make a routing decision. Some application switches and routers delay binding the client session to the server until the proper handshakes are complete so as to prevent Denial of Service attacks.

#### IP filtering

ADNs often have the ability to filter traffic based on Access Control Lists (ACLs), Bogus IP ranges (Bogon filtering) and deep packet inspection pattern matching. In some cases, thresholds or rate limiting of IP addresses or ranges of IP addresses may be employed.

## Traffic management

ADNs are increasingly adding advanced traffic management functionality. The deep packet inspection capabilities of some of these products can identify traffic by application type and can be used to analyze, block, shape and prioritize traffic.
