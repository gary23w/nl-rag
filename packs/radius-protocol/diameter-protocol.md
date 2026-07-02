---
title: "Diameter (protocol)"
source: https://en.wikipedia.org/wiki/Diameter_(protocol)
domain: radius-protocol
license: CC-BY-SA-4.0
tags: radius protocol, aaa authentication, diameter protocol, access accounting
fetched: 2026-07-02
---

# Diameter (protocol)

**Diameter** is an authentication, authorization, and accounting (AAA) protocol for computer networks. It evolved from the earlier RADIUS protocol. It belongs to the application layer protocols in the Internet protocol suite.

*Diameter Applications* extend the base protocol by adding new commands and/or attributes, such as those for use with the Extensible Authentication Protocol (EAP).

## Comparison with RADIUS

The name is a play on words, derived from the RADIUS protocol, which is the predecessor (a diameter is twice the radius). Diameter is not directly backward compatible but provides an upgrade path for RADIUS. The main features provided by Diameter but lacking in RADIUS are:

- Support for SCTP
- Capability negotiation
- Application layer acknowledgements; Diameter defines failover methods and state machines (RFC 3539)
- Extensibility; new commands can be defined
- Aligned on 32 bit boundaries

Also: Like RADIUS, it is intended to work in both local and roaming AAA situations. It uses TCP or SCTP, unlike RADIUS which uses UDP. Unlike RADIUS it includes no encryption but can be protected by transport-level security (IPSEC or TLS). The base size of the AV identifier is 32 bit unlike RADIUS which uses 8 bit as the base AV identifier size. Like RADIUS, it supports stateless as well as stateful modes. Like RADIUS, it supports application-layer acknowledgment and defines failover. Diameter is used for many different interfaces defined by the 3GPP standards, with each interface typically defining new commands and attributes.

## Applications

A *Diameter Application* is not a software application but is a protocol based on the Diameter base protocol defined in RFC 6733 (obsoletes RFC 3588) and RFC 7075. Each application is defined by an application identifier and can add new command codes and/or new mandatory AVPs (Attribute-Value Pair). Adding a new optional AVP does not require a new application.

Examples of Diameter applications:

- Diameter Mobile IPv4 Application (MobileIP, RFC 4004)
- Diameter Network Access Server Application (NASREQ, RFC 7155)(Obsoletes: RFC 4005)
- Diameter Extensible Authentication Protocol Application (RFC 4072)
- Diameter Credit-Control Application (DCCA, RFC 8506])(Obsoletes: RFC 4006)
- Diameter Session Initiation Protocol Application (RFC 4740)
- Various applications in the 3GPP IP Multimedia Subsystem

Both the

HSS

and the

SLF

communicate using the Diameter protocol.

(Generic Bootstrapping Architecture): Bootstrapping Server Function

## History

The Diameter protocol was initially developed by Pat R. Calhoun, Glen Zorn, and Ping Pan in 1998 to provide a framework for authentication, authorization, and accounting (AAA) that could overcome the limitations of RADIUS. At the time Diameter was designed, RADIUS was believed to have issues with reliability, scalability, security, and flexibility. RADIUS also did not support large policies which were needed for telephony applications. The Diameter protocol defines a policy protocol used by clients to perform Policy, AAA, and resource control. This allows a single server to handle policies for many services.

Like RADIUS, Diameter provides AAA functionality, but uses TCP and SCTP instead of UDP, therefore delegating detection and handling of communication problems to those protocols. The Diameter protocol is enhanced further by the development of the 3rd Generation Partnership Project (3GPP) IP Multimedia Subsystem (IMS). The S6a, S6b, Gx, Gy, Sy, Rx, Cx, Dh, Dx, Rf, Ro, Sh and Zh interfaces are supported by Diameter applications. Through the use of extensions, the protocol was designed to be extensible to support proxies, brokers, strong security, mobile IP, network-access servers (NASREQ), accounting and resource management.

## Protocol description

The Diameter base protocol is defined by RFC 6733 (Obsoletes: RFC 3588 and RFC 5719) and defines the minimum requirements for an AAA protocol. *Diameter Applications* can extend the base protocol by adding new commands, attributes, or both. Diameter security is provided by IPsec or TLS. The IANA has assigned TCP and SCTP port number 3868 to Diameter, as stated in section 11.4 of RFC 6733.

### Packet format

The packet consists of a Diameter header and a variable number of Attribute–Value Pairs, or AVPs, for encapsulating information relevant to the Diameter message.

Diameter Header

Bit offset

0

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

0

version

message length

32

R

P

E

T

command code

64

application ID

96

hop-by-hop ID

128

end-to-end ID

160

...

AVPs

...

### Version

This field indicates the version of the Diameter Base Protocol. As of 2014, the only value supported is 1.

### Message length

The Message Length field indicates the length of the Diameter message in bytes, including the header fields and the padded AVPs.

### Command flags

The "**R**" (Request) bit – If set, the message is a request. If cleared, the message is an answer.

The "**P**" (Proxiable) bit – If set, the message MAY be proxied, relayed or redirected. If cleared, the message MUST be locally processed.

The "**E**" (Error) bit – If set, the message contains a protocol error, and the message will not conform to the CCF described for this command. Messages with the "E" bit set are commonly referred to as error messages. This bit MUST NOT be set in request messages.

The "**T**" (Potentially re-transmitted message) bit – This flag is set after a link failover procedure, to aid the removal of duplicate requests. It is set when resending requests not yet acknowledged as an indication of a possible duplicate due to a link failure.

### Commands

Each command Request/Answer pair is assigned a command code. Whether it is the request or answer is identified via the 'R' bit in the Command Flags field of the header.

The values 0-255 are reserved for RADIUS backward compatibility. The values 256-16777213 are for permanent, standard commands allocated by IANA. The values 16777214 and 16777215 (hex 0xFFFFFE and 0xFFFFFF) are reserved for experimental and testing purposes.

A Command Code is used to determine the action that is to be taken for a particular message. Some common Diameter commands defined in the protocol (base and applications) are:

| Command-Name | Abbr. | Code | Application |
|---|---|---|---|
| AA-Request | AAR | 265 | Diameter NAS Application - RFC 7155 |
| AA-Answer | AAA | 265 | Diameter NAS Application - RFC 7155 |
| Diameter-EAP-Request | DER | 268 | Diameter EAP Application - RFC 4072 |
| Diameter-EAP-Answer | DEA | 268 | Diameter EAP Application - RFC 4072 |
| Abort-Session-Request | ASR | 274 | Diameter base |
| Abort-Session-Answer | ASA | 274 | Diameter base |
| Accounting-Request | ACR | 271 | Diameter base |
| Accounting-Answer | ACA | 271 | Diameter base |
| Credit-Control-Request | CCR | 272 | Diameter Credit-Control Application - RFC 8506 (Obsoletes RFC 4006) |
| Credit-Control-Answer | CCA | 272 | Diameter Credit-Control Application - RFC 8506 (Obsoletes RFC 4006) |
| Capabilities-Exchange-Request | CER | 257 | Diameter base |
| Capabilities-Exchange-Answer | CEA | 257 | Diameter base |
| Device-Watchdog-Request | DWR | 280 | Diameter base |
| Device-Watchdog-Answer | DWA | 280 | Diameter base |
| Disconnect-Peer-Request | DPR | 282 | Diameter base |
| Disconnect-Peer-Answer | DPA | 282 | Diameter base |
| Re-Auth-Request | RAR | 258 | Diameter base |
| Re-Auth-Answer | RAA | 258 | Diameter base |
| Session-Termination-Request | STR | 275 | Diameter base |
| Session-Termination-Answer | STA | 275 | Diameter base |
| User-Authorization-Request | UAR | 283 | Diameter SIP Application - RFC 4740 |
| User-Authorization-Answer | UAA | 283 | Diameter SIP Application - RFC 4740 |
| Server-Assignment-Request | SAR | 284 | Diameter SIP Application - RFC 4740 |
| Server-Assignment-Answer | SAA | 284 | Diameter SIP Application - RFC 4740 |
| Location-Info-Request | LIR | 285 | Diameter SIP Application - RFC 4740 |
| Location-Info-Answer | LIA | 285 | Diameter SIP Application - RFC 4740 |
| Multimedia-Auth-Request | MAR | 286 | Diameter SIP Application - RFC 4740 |
| Multimedia-Auth-Answer | MAA | 286 | Diameter SIP Application - RFC 4740 |
| Registration-Termination-Request | RTR | 287 | Diameter SIP Application - RFC 4740 |
| Registration-Termination-Answer | RTA | 287 | Diameter SIP Application - RFC 4740 |
| Push-Profile-Request | PPR | 288 | Diameter SIP Application - RFC 4740 |
| Push-Profile-Answer | PPA | 288 | Diameter SIP Application - RFC 4740 |
| User-Authorization-Request | UAR | 300 | Diameter base (3GPP) RFC 3589 |
| User-Authorization-Answer | UAA | 300 | Diameter base (3GPP) RFC 3589 |
| Server-Assignment-Request | SAR | 301 | Diameter base (3GPP) RFC 3589 |
| Server-Assignment-Answer | SAA | 301 | Diameter base (3GPP) RFC 3589 |
| Location-Info-Request | LIR | 302 | Diameter base (3GPP) RFC 3589 |
| Location-Info-Answer | LIA | 302 | Diameter base (3GPP) RFC 3589 |
| Multimedia-Auth-Request | MAR | 303 | Diameter base (3GPP) RFC 3589 |
| Multimedia-Auth-Answer | MAA | 303 | Diameter base (3GPP) RFC 3589 |
| Registration-Termination-Request | RTR | 304 | Diameter base (3GPP) RFC 3589 |
| Registration-Termination-Answer | RTA | 304 | Diameter base (3GPP) RFC 3589 |
| Push-Profile-Request | PPR | 305 | Diameter base (3GPP) RFC 3589 |
| Push-Profile-Answer | PPA | 305 | Diameter base (3GPP) RFC 3589 |
| User-Data-Request | UDR | 306 | Diameter base (3GPP) RFC 3589 |
| User-Data-Answer | UDA | 306 | Diameter base (3GPP) RFC 3589 |
| Profile-Update-Request | PUR | 307 | Diameter base (3GPP) RFC 3589 |
| Profile-Update-Answer | PUA | 307 | Diameter base (3GPP) RFC 3589 |
| Subscribe-Notifications-Request | SNR | 308 | Diameter base (3GPP) RFC 3589 |
| Subscribe-Notifications-Answer | SNA | 308 | Diameter base (3GPP) RFC 3589 |
| Push-Notification-Request | PNR | 309 | Diameter base (3GPP) RFC 3589 |
| Push-Notification-Answer | PNA | 309 | Diameter base (3GPP) RFC 3589 |
| Bootstrapping-Info-Request | BIR | 310 | Diameter base (3GPP) RFC 3589 |
| Bootstrapping-Info-Answer | BIA | 310 | Diameter base (3GPP) RFC 3589 |
| Message-Process-Request | MPR | 311 | Diameter base (3GPP) RFC 3589 |
| Message-Process-Answer | MPA | 311 | Diameter base (3GPP) RFC 3589 |
| Update-Location-Request | ULR | 316 | 3GPP TS 29.272 [RFC 5516] |
| Update-Location-Answer | ULA | 316 | 3GPP TS 29.272 [RFC 5516] |
| Cancel-Location-Request | CLR | 317 | 3GPP TS 29.272 [RFC 5516] |
| Cancel-Location-Answer | CLA | 317 | 3GPP TS 29.272 [RFC 5516] |
| Authentication-Information-Request | AIR | 318 | 3GPP TS 29.272 [RFC 5516] |
| Authentication-Information-Answer | AIA | 318 | 3GPP TS 29.272 [RFC 5516] |
| Insert-Subscriber-Data-Request | IDR | 319 | 3GPP TS 29.272 [RFC 5516] |
| Insert-Subscriber-Data-Answer | IDA | 319 | 3GPP TS 29.272 [RFC 5516] |
| Delete-Subscriber-Data-Request | DSR | 320 | 3GPP TS 29.272 [RFC 5516] |
| Delete-Subscriber-Data-Answer | DSA | 320 | 3GPP TS 29.272 [RFC 5516] |
| Purge-UE-Request | PER | 321 | 3GPP TS 29.272 [RFC 5516] |
| Purge-UE-Answer | PEA | 321 | 3GPP TS 29.272 [RFC 5516] |
| Notify-Request | NR | 323 | 3GPP TS 29.272 [RFC 5516] |
| Notify-Answer | NA | 323 | 3GPP TS 29.272 [RFC 5516] |
| Provide-Location-Request | PLR | 8388620 | 3GPP-LCS-SLg (Application-ID 16777255) |
| Provide-Location-Answer | PLA | 8388620 | 3GPP-LCS-SLg (Application-ID 16777255) |
| Routing-Info-Request | RIR | 8388622 | 3GPP-LCS-SLh (Application-ID 16777291) |
| Routing-Info-Answer | RIA | 8388622 | 3GPP-LCS-SLh (Application-ID 16777291) |
| AA-Mobile-Node-Request | AMR | 260 | Diameter Mobile IPv4 - RFC 4004 |
| AA-Mobile-Node-Answer | AMA | 260 | Diameter Mobile IPv4 - RFC 4004 |
| Home-Agent-MIP-Request | HAR | 262 | Diameter Mobile IPv4 - RFC 4004 |
| Home-Agent-MIP-Answer | HAA | 262 | Diameter Mobile IPv4 - RFC 4004 |
| Configuration-Information-Request | CIR | 8388718 | S6t per 3GPP TS 29.336 |
| Configuration-Information-Answer | CIA | 8388718 | S6t per 3GPP TS 29.336 |
| Reporting-Information-Request | RIR | 8388719 | S6t per 3GPP TS 29.336 |
| Reporting-Information-Answer | RIA | 8388719 | S6t per 3GPP TS 29.336 |
| NIDD-Information-Request | NIR | 8388726 | S6t per 3GPP TS 29.336 |
| NIDD-Information-Answer | NIA | 8388726 | S6t per 3GPP TS 29.336 |

### Application-ID

Application-ID is used to identify for which Diameter application the message is applicable. The application can be an authentication application, an accounting application, or a vendor-specific application.

Diameter agents conforming to a certain Diameter extension publicize its support by including a specific value of in the Auth-Application-ID Attribute of the Capabilities-Exchange-Request (CER) and Capabilities-Exchange-Answer (CEA) command.

The value of the Application-ID field in the header is the same as any relevant Application-ID AVPs contained in the message. For instance, the value of the Application-ID and of the Auth-Application-ID Attribute in the Credit-Control-Request (CCR) and Credit-Control-Answer (CCA) Command for the Diameter Credit-Control Application is 4.

| Application-ID | Abbr. | Full name | Usage |
|---|---|---|---|
| 0 | Base | Diameter Common Messages | Diameter protocol association establishment/teardown/maintenance |
| 16777216 | Cx/Dx | 3GPP Cx/Dx | IMS I/S-CSCF to HSS interface |
| 16777217 | Sh | 3GPP Sh | VoIP/IMS SIP Application Server to HSS interface |
| 16777236 | Rx | 3GPP Rx | Policy and charging control |
| 16777238 | Gx | 3GPP Gx | Policy and charging control |
| 16777251 | S6a/S6d | 3GPP S6a/S6d | LTE Roaming signaling |
| 16777252 | S13 | 3GPP 13 | Interface between EIR and MME |
| 16777255 | SLg | 3GPP LCS SLg | Location services |
| 16777345 | S6t | 3GPP S6t | Interface between SCEF and HSS |

### Hop-by-Hop Identifier

The Hop-by-Hop Identifier is an unsigned 32-bit integer field (in network byte order) that is used to match the requests with their answers as the same value in the request is used in the response.

The Diameter protocol requires that relaying and proxying agents maintain transaction state, which is used for failover purposes. Transaction state implies that upon forwarding a request, its Hop-by-Hop Identifier is saved; the field is replaced with a locally unique identifier, which is restored to its original value when the corresponding answer is received. The request's state is released upon receipt of the answer. Received answers that do not match a known Hop-by-Hop Identifier are ignored by the Diameter agent.

In case of redirecting agents, the Hop-by-Hop Identifier is maintained in the header as the Diameter agent responds with an answer message.

### End-to-End Identifier

The End-to-End Identifier is an unsigned 32-bit integer field (in network byte order) that is used to detect duplicate messages along with the combination of the Origin-Host AVP.

When creating a request, the End-to-End Identifier is set to a locally unique value. The End-to-End Identifier is not modified by Diameter agents of any kind, and the same value in the corresponding request is used in the answer.

### Attribute–Value Pairs (AVP)

AVP Header

Bit offset

0

1

2

3

4

5

6

7

8

9

10

11

12

13

14

15

16

17

18

19

20

21

22

23

24

25

26

27

28

29

30

31

0

AVP code

32

V

M

P

AVP length

64

vendor ID (optional)

96

...

data

...

For simplicity, AVP Flag "**V**" bit Means **Vendor Specific**; "**M**" bit means **Mandatory**; "**P**" bit means **Protected**.

The "**V**" bit, known as the Vendor-Specific bit, indicates whether the optional **Vendor-ID** field is present in the AVP header. When set the AVP Code belongs to the specific vendor code address space.

The "**M**" bit, known as the Mandatory bit, indicates whether support of the AVP is required. If an AVP with the "**M**" bit set is received by a Diameter client, server, proxy, or translation agent and either the AVP or its value is unrecognized, the message *must* be rejected. Diameter Relay and redirect agents *must not* reject messages with unrecognized AVPs.

The "**P**" bit indicates the need for encryption for end-to-end security.

| Attribute-Name | Code | Data Type |
|---|---|---|
| Acct-Interim-Interval | 85 | Unsigned32 |
| Accounting-Realtime-Required | 483 | Enumerated |
| Acct-Multi-Session-Id | 50 | UTF8String |
| Accounting-Record-Number | 485 | Unsigned32 |
| Accounting-Record-Type | 480 | Enumerated |
| Accounting-Session-Id | 44 | OctetString |
| Accounting-Sub-Session-Id | 287 | Unsigned64 |
| Acct-Application-Id | 259 | Unsigned32 |
| Auth-Application-Id | 258 | Unsigned32 |
| Auth-Request-Type | 274 | Enumerated |
| Authorization-Lifetime | 291 | Unsigned32 |
| Auth-Grace-Period | 276 | Unsigned32 |
| Auth-Session-State | 277 | Enumerated |
| Re-Auth-Request-Type | 285 | Enumerated |
| Class | 25 | OctetString |
| Destination-Host | 293 | DiamIdent |
| Destination-Realm | 283 | DiamIdent |
| Disconnect-Cause | 273 | Enumerated |
| E2E-Sequence | 300 | Grouped |
| Error-Message | 281 | UTF8String |
| Error-Reporting-Host | 294 | DiamIdent |
| Event-Timestamp | 55 | Time |
| Experimental-Result | 297 | Grouped |
| Experimental-Result-Code | 298 | Unsigned32 |
| Failed-AVP | 279 | Grouped |
| Firmware-Revision | 267 | Unsigned32 |
| Host-IP-Address | 257 | Address |
| Inband-Security-Id | 299 | Unsigned32 |
| Multi-Round-Time-Out | 272 | Unsigned32 |
| Origin-Host | 264 | DiamIdent |
| Origin-Realm | 296 | DiamIdent |
| Origin-State-Id | 278 | Unsigned32 |
| Product-Name | 269 | UTF8String |
| Proxy-Host | 280 | DiamIdent |
| Proxy-Info | 284 | Grouped |
| Proxy-State | 33 | OctetString |
| Redirect-Host | 292 | DiamURI |
| Redirect-Host-Usage | 261 | Enumerated |
| Redirect-Max-Cache-Time | 262 | Unsigned32 |
| Result-Code | 268 | Unsigned32 |
| Route-Record | 282 | DiamIdent |
| Session-Id | 263 | UTF8String |
| Session-Timeout | 27 | Unsigned32 |
| Session-Binding | 270 | Unsigned32 |
| Session-Server-Failover | 271 | Enumerated |
| Supported-Vendor-Id | 265 | Unsigned32 |
| Termination-Cause | 295 | Enumerated |
| User-Name | 1 | UTF8String |
| Vendor-Id | 266 | Unsigned32 |
| Vendor-Specific-Application-Id | 260 | Grouped |

### State machines

The RFC 3588 defines a core state machine for maintaining connections between peers and processing messages. This is part of the basic protocol functionality and all stacks should support it and as such abstract from the connectivity related operations.

- (Peer State Machine Part 1)Peer State Machine Part 1
- (Peer State Machine Part 2)Peer State Machine Part 2

Additionally, application specific state machines can be introduced either later or at a higher abstraction layer. The RFC 3588 defines an authorization and an accounting state machine.

- (Diameter Authorization State Machines (Client))Diameter Authorization State Machines (Client)
- (Diameter Authorization State Machines (Server))Diameter Authorization State Machines (Server)
- (Diameter Accounting State Machines (Client))Diameter Accounting State Machines (Client)
- (Diameter Accounting State Machines (Server))Diameter Accounting State Machines (Server)

### Message flows

The communication between two diameter peers starts with the establishment of a transport connection (TCP or SCTP). The initiator then sends a Capabilities-Exchange-Request (CER) to the other peer, which responds with a Capabilities-Exchange-Answer (CEA). For RFC3588 compliant peers TLS (Transport Layer Security) may optionally be negotiated. For RFC6733 compliant peers TLS negotiation may optionally happen before the CER/CEA.

The connection is then ready for exchanging application messages.

If no messages have been exchanged for some time either side may send a Device-Watchdog-Request (DWR) and the other peer must respond with Device-Watchdog-Answer.

Either side may terminate the communication by sending a Disconnect-Peer-Request (DPR) which the other peer must respond to with Disconnect-Peer-Answer. After that the transport connection can be disconnected.

## RFCs

The Diameter protocol is currently defined in the following IETF RFCs: Obsolete RFCs are indicated with strikethrough text.

| # | Title | Date published | Obsoleted by |
|---|---|---|---|
| RFC 3588 | Diameter Base Protocol. | September 2003 | RFC 6733 |
| RFC 3589 | Diameter Command Codes for Third Generation Partnership Project (3GPP) Release 5. | September 2003 |   |
| RFC 4004 | Diameter Mobile IPv4 Application. | August 2005 |   |
| RFC 4005 | Diameter Network Access Server Application. | August 2005 | RFC 7155 |
| RFC 4006 | Diameter Credit-Control Application. | August 2005 | RFC 8506 |
| RFC 4072 | Diameter Extensible Authentication Protocol (EAP) Application. | August 2005 |   |
| RFC 4740 | Diameter Session Initiation Protocol (SIP) Application. M. | November 2006 |   |
| RFC 5224 | Diameter Policy Processing Application. | March 2008 |   |
| RFC 5431 | Diameter ITU-T Rw Policy Enforcement Interface Application. | March 2009 |   |
| RFC 5447 | Diameter Mobile IPv6: Support for Network Access Server to Diameter Server Interaction. | February 2009 |   |
| RFC 5516 | Diameter Command Code Registration for the Third Generation Partnership Project (3GPP) Evolved Packet System (EPS). | April 2009 |   |
| RFC 5624 | Quality of Service Parameters for Usage with Diameter. | August 2009 |   |
| RFC 5719 | Updated IANA Considerations for Diameter Command Code Allocations. | January 2010 | RFC 6733 |
| RFC 6733 | Diameter Base Protocol. | October 2012 |   |
| RFC 6737 | The Diameter Capabilities Update Application. | October 2012 |   |
| RFC 7155 | Diameter Network Access Server Application. | April 2014 |   |
| RFC 8506 | Diameter Credit-Control Application | March 2019 |   |
