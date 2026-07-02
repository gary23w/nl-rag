---
title: "Software-defined perimeter"
source: https://en.wikipedia.org/wiki/Software-defined_perimeter
domain: zero-trust
license: CC-BY-SA-4.0
tags: zero trust, zero trust architecture, never trust always verify, principle of least privilege, software defined perimeter
fetched: 2026-07-02
---

# Software-defined perimeter

A **software-defined perimeter** (**SDP**), sometimes referred to as a **black cloud**, is a network architecture used to implement zero-trust principles. The SDP specification was developed by the Cloud Security Alliance (CSA) to control resource access based on identity.

In an SDP, connectivity follows a need-to-know model, requiring both entity authentication and device posture validation before granting access to internal assets. The application infrastructure is effectively "black", a term used by the United States Department of Defense to describe undetectable infrastructure, as it lacks visible DNS information or IP addresses.

The SDP architecture mitigates many common network-based attacks, including but not limited to:

- Server scanning
- Denial-of-service (DoS)
- SQL injection
- Operating system and application vulnerability exploits
- Man-in-the-middle attacks
- Pass-the-hash (also known as pass-the-ticket)
- Other unauthorized user attacks

## Background

Traditional enterprise network architecture is based on the premise of an internal network isolated by a fixed perimeter, typically consisting of firewalls. These firewalls block external entities from accessing internal assets while allowing the internal users to connect to external resources.

However, the proliferation of user-managed devices, remote connectivity, SaaS, PaaS, and IaaS has extended the perimeter and broadened the attack surface. Software-Defined Perimeters (SDPs) address these issues by allowing application owners to deploy perimeters that maintain the traditional model's invisibility and inaccessibility. Unlike static firewalls, SDPs can be deployed anywhere—on the internet, in the cloud, at a hosting center, on a private corporate network, or across some or all of these locations.

## Authorization techniques

There are several techniques for delivering a software-defined perimeter. These include:

- Single Packet Authorization (SPA) uses cryptographic techniques to make internet-facing servers invisible to unauthorized users. Only devices that have been seeded with the cryptographic secret can generate a valid SPA packet and, as a result, establish a network connection.
- First Packet Authentication involves a single-use, cryptographically generated identity token inserted at both ends of a TCP/IP session for authentication. If the request is allowed, the gateway applies a security policy that forwards, redirects, or discards based on the identity.
- Authenticate Before Connect provisions endpoints with unique, cryptographically generated identities (commonly using X.509 certificates and JSON Web Tokens). These endpoints establish outbound connectivity into a mesh overlay that listens for authenticated and authorized endpoints. This eliminates the need for inbound connectivity at both the source and destination.

## Architecture

In its simplest form, the SDP architecture consists of two components: SDP Hosts and SDP Controllers. SDP Hosts can either initiate or accept connections. Interactions with the SDP Controllers manage these actions through a control channel (see Figure 1). As a result, the control plane is separated from the data plane in an SDP, enabling greater scalability. Additionally, all components can be made redundant for higher availability.

The SDP framework has the following workflow (see Figure 2):

1. One or more SDP Controllers are brought online and connected to the appropriate authentication and authorization services (e.g., PKI, device fingerprinting, geolocation, SAML, OpenID, OAuth, LDAP, Kerberos, multi-factor authentication, and other similar services).
2. One or more accepting SDP Hosts are brought online. These hosts connect to and authenticate with the controllers. However, they do not acknowledge communication from any other host and will not respond to any non-provisioned requests.
3. Each Initiating SDP Host that comes online connects to and authenticates with the SDP Controllers.
4. After authenticating the Initiating SDP Host, the SDP Controllers determine a list of Accepting SDP Hosts with which the initiating host is authorized to communicate.
5. The SDP Controller instructs the Accepting SDP Hosts to accept communication from the Initiating SDP Host and applies any optional policies required for encrypted communications.
6. The SDP Controller provides the Initiating SDP Host with the list of Accepting SDP Hosts and any optional policies required for encrypted communications.
7. The Initiating SDP Host establishes a mutual VPN connection with all authorized Accepting SDP Hosts.

## SDP deployment models

While the general workflow remains the same for all implementations, the application of SDPs can favour certain implementations over others.

### Client-to-Gateway

In the client-to-gateway implementation, one or more servers are protected behind an Accepting SDP Host, which acts as a gateway between the clients and the protected servers. This implementation can be used within an enterprise network to mitigate common lateral movement attacks, such as server scanning, OS and application vulnerability exploits, password cracking, man-in-the-middle attacks, pass-the-hash (PtH) and others. Alternatively, it can be implemented on the internet to isolate protected servers from unauthorized users and mitigate attacks.

### Client-to-Server

The client-to-server implementation offers features and benefits similar to the client-to-gateway implementation. However, in a client-to-server scenario, the protected server runs the Accepting SDP Host software rather than using a gateway in front of the server running that software. The choice between the client-to-gateway and client-to-server implementations is typically based on factors such as the number of servers being protected, load balancing methods, server elasticity, and other topological considerations.

### Server-to-Server

In the server-to-server implementation, servers offering a Representational State Transfer (REST) service, a Simple Object Access Protocol (SOAP) service, a remote procedure call (RPC), or any kind of application programming interface (API) over the internet can be protected from unauthorized hosts on the network. For example, the server initiating the REST call would be the Initiating SDP Host, and the server offering the REST service would be the Accepting SDP Host. Implementing an SDP for this use case can reduce the load on these services and mitigate attacks similar to those mitigated by the client-to-gateway implementation.

### Client-to-Server-to-Client

The client-to-server-to-client implementation creates a peer-to-peer relationship between the two clients and can be used for applications such as IP telephony, chat and video conferencing. In these cases, the SDP obfuscates the IP addresses of the connecting clients. Alternatively, a client-to-gateway-to-client configuration can hide the application server as well.

## SDP applications

### Enterprise application isolation

In the context of data breaches involving intellectual property, financial records, and human resources data, attackers typically gain initial entry by compromising a single endpoint. Following the initial breach, they exploit the network's flat architecture to move laterally, seeking access to high-value information assets.

To counter this threat, organizations can deploy a Software-Defined Perimeter (SDP) within the data center to partition the network and isolate sensitive applications. By enforcing access controls, the SDP restricts unauthorized access to protected resources. This prevents the lateral movement necessary for large-scale data exfiltration, localizing the breach and securing the enterprise's most critical data.

### Private cloud and hybrid cloud

The application of SDP varies across cloud service models to address specific security requirements:

- Software-as-a-Service (SaaS): Implementations may designate the SaaS application as an **Accepting Host** and authenticated users as **Initiating Hosts**. This configuration significantly reduces the vendor’s attack surface while maintaining seamless outbound internet connectivity.
- Infrastructure-as-a-Service (IaaS): Providers can offer **SDP-as-a-Service** to secure administrative and user access to customers' virtualized cloud infrastructure.
- Platform-as-a-Service (PaaS): Providers may integrate SDP architecture as an embedded security layer, effectively mitigating network-based exploits against the development and deployment environment.

As the proliferation of interconnected devices increases, the back-end applications responsible for managing these devices and processing sensitive data have become mission-critical. SDPs enhance the security and availability of these systems by concealing servers and their communication from the public internet. This "dark" infrastructure approach prevents unauthorized discovery and targeted external attacks.
