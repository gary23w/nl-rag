---
title: "Internet Key Exchange"
source: https://en.wikipedia.org/wiki/Internet_Key_Exchange
domain: ipsec
license: CC-BY-SA-4.0
tags: ipsec, internet key exchange, security association, encapsulating security payload
fetched: 2026-07-02
---

# Internet Key Exchange

In computing, **Internet Key Exchange** (**IKE**, versioned as **IKEv1** and **IKEv2**) is the protocol used to set up a security association (SA) in the IPsec protocol suite. IKE builds upon the Oakley protocol and ISAKMP. IKE uses X.509 certificates for authentication ‒ either pre-shared or distributed using DNS (preferably with DNSSEC) ‒ and a Diffie–Hellman key exchange to set up a shared session secret from which cryptographic keys are derived. A IETF draft is currently being written to provide a quantum-resistant key establishment using ML-KEM. In addition, a security policy for every peer which will connect must be manually maintained.

## History

The Internet Engineering Task Force (IETF) originally defined IKE in November 1998 in a series of publications (Request for Comments) known as RFC 2407, RFC 2408 and RFC 2409:

- RFC 2407 defined the Internet IP Security Domain of Interpretation for ISAKMP.
- RFC 2408 defined the Internet Security Association and Key Management Protocol (ISAKMP).
- RFC 2409 defined the Internet Key Exchange (IKE).

RFC 4306 updated IKE to version two (IKEv2) in December 2005. RFC 4718 clarified some open details in October 2006. RFC 5996 combined these two documents plus additional clarifications into the updated IKEv2, published in September 2010. A later update upgraded the document from Proposed Standard to Internet Standard, published as RFC 7296 in October 2014.

The parent organization of the IETF, the Internet Society (ISOC), has maintained the copyrights of these standards as freely available to the Internet community.

## Architecture

Most IPsec implementations consist of an IKE daemon that runs in user space and an IPsec stack in the kernel that processes the actual IP packets.

User-space daemons have easy access to mass storage containing configuration information, such as the IPsec endpoint addresses, keys and certificates, as required. Kernel modules, on the other hand, can process packets efficiently and with minimum overhead—which is important for performance reasons.

The IKE protocol uses UDP packets, usually on port 500, and generally requires 4–6 packets with 2–3 round trips to create an ISAKMP security association (SA) on both sides. The negotiated key material is then given to the IPsec stack. For instance, this could be an AES key, information identifying the IP endpoints and ports that are to be protected, as well as what type of IPsec tunnel has been created. The IPsec stack, in turn, intercepts the relevant IP packets if and where appropriate and performs encryption/decryption as required. Implementations vary on how the interception of the packets is done—for example, some use virtual devices, others take a slice out of the firewall, etc.

IKEv1 consists of two phases: phase 1 and phase 2.

### IKEv1 phases

IKE phase one's purpose is to establish a secure authenticated communication channel by using the Diffie–Hellman key exchange algorithm to generate a shared secret key to encrypt further IKE communications. This negotiation results in one single bi-directional ISAKMP security association. The authentication can be performed using either pre-shared key (shared secret), signatures, or public key encryption. Phase 1 operates in either Main Mode or Aggressive Mode. Main Mode protects the identity of the peers and the hash of the shared key by encrypting them; Aggressive Mode does not.

During IKE phase two, the IKE peers use the secure channel established in Phase 1 to negotiate Security Associations on behalf of other services like IPsec. The negotiation results in a minimum of two unidirectional security associations (one inbound and one outbound). Phase 2 operates only in Quick Mode.

### Problems with IKE

Originally, IKE had numerous configuration options but lacked a general facility for automatic negotiation of a universally supported default case. As a result, both endpoints needed to exactly agree on every parameter of the security association—such as encryption algorithms, key exchange methods, and lifetimes—or the connection would fail. This led to frequent interoperability issues between different vendors' implementations. Troubleshooting was further complicated by limited or cryptic debug output in many implementations.

The IKEv1 specifications also permitted a significant degree of interpretation, sometimes bordering on design flaws. One example is Dead Peer Detection (DPD), which was implemented inconsistently across vendors. Even with correctly matched configurations, this could result in negotiation failures or dropped tunnels.

### Improvements with IKEv2

The IKEv2 protocol was described in Appendix A of RFC 4306 in 2005. The following issues were addressed:

- Fewer Requests for Comments (RFCs): The specifications for IKE were covered in at least three RFCs, more if one takes into account NAT traversal and other extensions that are in common use. IKEv2 combines these in one RFC as well as making improvements to support for NAT traversal (Network Address Translation (NAT)) and firewall traversal in general.
- Standard Mobility support: There is a standard extension for IKEv2 named [rfc:4555 Mobility and Multihoming Protocol] (MOBIKE) (see also, IPsec) used to support mobility and multihoming for it and Encapsulating Security Payload (ESP). By use of this extension IKEv2 and IPsec can be used by mobile and multihomed users.
- NAT traversal: The encapsulation of IKE and ESP in User Datagram Protocol (UDP port 4500) enables these protocols to pass through a device or firewall performing NAT.
- Stream Control Transmission Protocol (SCTP) support: IKEv2 allows for the SCTP protocol as used in Internet telephony protocol, Voice over IP (VoIP).
- Simple message exchange: IKEv2 has one four-message initial exchange mechanism where IKE provided eight distinctly different initial exchange mechanisms, each one of which had slight advantages and disadvantages.
- Fewer cryptographic mechanisms: IKEv2 uses cryptographic mechanisms to protect its packets that are very similar to what IPsec ESP uses to protect the IPsec packets. This led to simpler implementations and certifications for Common Criteria and FIPS 140-2 (Federal Information Processing Standard (FIPS), which require each cryptographic implementation to be separately validated.
- Reliability and State management: IKEv2 uses sequence numbers and acknowledgments to provide reliability and mandates some error processing logistics and shared state management. IKE could end up in a dead state due to the lack of such reliability measures, where both parties were expecting the other to initiate an action - which never eventuated. Work arounds (such as Dead-Peer-Detection) were developed but not standardized. This meant that different implementations of work-arounds were not always compatible.
- Denial of Service (DoS) attack resilience: IKEv2 does not perform much processing until it determines if the requester actually exists. This addressed some of the DoS problems suffered by IKE which would perform a lot of expensive cryptographic processing from spoofed locations.

Supposing

HostA

has a

Security Parameter Index

(SPI) of

A

and

HostB

has an

SPI

of

B

, the scenario would look like this:

```
HostA -------------------------------------------------- HostB
     |HDR(A,0),sai1,kei,Ni-------------------------->   |
     |   <----------------------------HDR(A,0),N(cookie)|
     |HDR(A,0),N(cookie),sai1,kei,Ni---------------->   |
     |   <--------------------------HDR(A,B),SAr1,ker,Nr|
```

If

HostB

(the responder) is experiencing large amounts of half-open IKE connections, it will send an unencrypted reply message of

IKE_SA_INIT

to

HostA

(the initiator) with a notify message of type

COOKIE

, and will expect

HostA

to send an

IKE_SA_INIT

request with that cookie value in a notify payload to

HostB

. This is to ensure that the initiator is really capable of handling an IKE response from the responder.

## Protocol extensions

The IETF ipsecme working group has standardized a number of extensions, with the goal of modernizing the IKEv2 protocol and adapting it better to high volume, production environments. These extensions include:

- **IKE session resumption**: the ability to resume a failed IKE/IPsec "session" after a failure, without the need to go through the entire IKE setup process (RFC 5723).
- **IKE redirect**: redirection of incoming IKE requests, allowing for simple load-balancing between multiple IKE endpoints (RFC 5685).
- **IPsec traffic visibility**: special tagging of ESP packets that are authenticated but not encrypted, with the goal of making it easier for middleboxes (such as intrusion detection systems) to analyze the flow (RFC 5840).
- **Mutual EAP authentication**: support for EAP-only (i.e., certificate-less) authentication of both of the IKE peers; the goal is to allow for modern password-based authentication methods to be used (RFC 5998).
- **Quick crash detection**: minimizing the time until an IKE peer detects that its opposite peer has crashed (RFC 6290).
- **High availability extensions**: improving IKE/IPsec-level protocol synchronization between a cluster of IPsec endpoints and a peer, to reduce the probability of dropped connections after a failover event (RFC 6311).

## Implementations

IKE is supported as part of the IPsec implementation in Windows 2000, Windows XP, Windows Server 2003, Windows Vista and Windows Server 2008. The ISAKMP/IKE implementation was jointly developed by Cisco and Microsoft.

Microsoft Windows 7 and Windows Server 2008 R2 partially support IKEv2 (RFC 7296) as well as MOBIKE (RFC 4555) through the *VPN Reconnect* feature (also known as *Agile VPN*).

There are several open source implementations of IPsec with associated IKE capabilities. On Linux, Libreswan, Openswan and strongSwan implementations provide an IKE daemon which can configure (i.e., establish SAs) to the KLIPS or XFRM/NETKEY kernel-based IPsec stacks. XFRM/NETKEY is the Linux native IPsec implementation available as of version 2.6.

The Berkeley Software Distributions also implements IPsec, IKE daemon via the OpenBSD Cryptographic Framework (OCF), which makes supporting cryptographic accelerators much easier. OCF has recently been ported to Linux.

A number of network equipment vendors have created their own IKE daemons (and IPsec implementations), or license a stack from one another.

There are a number of implementations of IKEv2 and some of the companies dealing in IPsec certification and interoperability testing are starting to hold workshops for testing as well as updated certification requirements to deal with IKEv2 testing.

The following open source implementations of IKEv2 are available:

- OpenIKEv2,
- strongSwan,
- Libreswan,
- Openswan,
- Racoon from the KAME project,
- iked from the OpenBSD project.

## Vulnerabilities

Leaked NSA presentations released in 2014 by *Der Spiegel* indicate that IKE is being exploited in an unknown manner to decrypt IPsec traffic, as is ISAKMP. The researchers who discovered the Logjam attack state that breaking a 1024-bit Diffie–Hellman group would break 66% of VPN servers, 18% of the top million HTTPS domains, and 26% of SSH servers, which the researchers claim is consistent with the leaks. This claim was refuted in 2015 by both Eyal Ronen and Adi Shamir in their paper "Critical Review of Imperfect Forward Secrecy" and by Paul Wouters of Libreswan in a 2015 article "66% of VPN's [*sic*] are not in fact broken".

IPsec VPN configurations which allow for negotiation of multiple configurations are subject to MITM-based downgrade attacks between the offered configurations, with both IKEv1 and IKEv2. This can be avoided by careful segregation of client systems onto multiple service access points with stricter configurations.

Both versions of the IKE standard are susceptible to an offline dictionary attack when a low entropy password is used. For the IKEv1 this is true for main mode and aggressive mode.
