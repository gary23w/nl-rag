---
title: "Constrained Application Protocol"
source: https://en.wikipedia.org/wiki/Constrained_Application_Protocol
domain: thread-network-deep
license: CC-BY-SA-4.0
tags: thread protocol, 6lowpan mesh, low-power ipv6, border router
fetched: 2026-07-02
---

# Constrained Application Protocol

**Constrained Application Protocol** (**CoAP**) is a specialized UDP-based Internet application protocol for constrained devices, as defined in RFC 7252 (published in 2014). It enables those constrained devices called "nodes" to communicate with the wider Internet using similar protocols. CoAP is designed for use between devices on the same constrained network (e.g., low-power, lossy networks), between devices and general nodes on the Internet, and between devices on different constrained networks both joined by an internet. CoAP is also being used via other mechanisms, such as SMS on mobile communication networks.

CoAP is an application-layer protocol that is intended for use in resource-constrained Internet devices, such as wireless sensor network nodes. CoAP is designed to easily translate to HTTP for simplified integration with the web, while also meeting specialized requirements such as multicast support, very low overhead, and simplicity. Multicast, low overhead, and simplicity are important for Internet of things (IoT) and machine-to-machine (M2M) communication, which tend to be embedded and have much less memory and power supply than traditional Internet devices have. Therefore, efficiency is very important. CoAP can run on most devices that support UDP or a UDP analogue.

The Internet Engineering Task Force (IETF) Constrained RESTful Environments Working Group (CoRE) has done the major standardization work for this protocol. In order to make the protocol suitable to IoT and M2M applications, various new functions have been added.

## Specification

The core of the protocol is specified in RFC 7252. Various extensions have been proposed, particularly:

- RFC 7641 (2015) Observing Resources in the Constrained Application Protocol
- RFC 7959 (2016) Block-Wise Transfers in the Constrained Application Protocol (CoAP)
- RFC 8323 (2018) CoAP (Constrained Application Protocol) over TCP, TLS, and WebSockets
- RFC 8974 (2021) Extended Tokens and Stateless Clients in the Constrained Application Protocol (CoAP)

## Message formats

CoAP makes use of two message types, requests and responses, using a simple, binary header format. CoAP is by default bound to UDP and optionally to DTLS, providing a high level of communications security. When bound to UDP, the entire message *must* fit within a single datagram. When used with 6LoWPAN as defined in RFC 4944, messages *should* fit into a single IEEE 802.15.4 frame to minimize fragmentation.

The smallest CoAP message is 4 bytes in length, if the token, options and payload fields are omitted, i.e. if it only consists of the CoAP header. The header is followed by the token value (0 to 8 bytes) which may be followed by a list of options in an optimized type–length–value format. Any bytes after the header, token and options (if any) are considered the message payload, which is prefixed by the one-byte "payload marker" (0xFF). The length of the payload is implied by the datagram length.

CoAP Message

Octet

offset

0

1

2

3

Bit

offset

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

4

32

ver

type

token length

request/response code

message ID

8

64

token (0–8 bytes)

12

96

16

128

options (if available)

20

160

1

1

1

1

1

1

1

1

payload (if available)

### CoAP fixed-size header

The first 4 bytes are mandatory in all CoAP datagrams, they constitute the fixed-size header.

These fields can be extracted from these 4 bytes in C via these macros:

```mw
#define COAP_HEADER_VERSION(data)  ( (0xC0 & (data)[0]) >> 6      )
#define COAP_HEADER_TYPE(data)     ( (0x30 & (data)[0]) >> 4      )
#define COAP_HEADER_TKL(data)      ( (0x0F & (data)[0]) >> 0      )
#define COAP_HEADER_CLASS(data)    ( ((data)[1] >> 5) & 0x07      )
#define COAP_HEADER_CODE(data)     ( ((data)[1] >> 0) & 0x1F      )
#define COAP_HEADER_MID(data)      ( ((data)[2] << 8) | (data)[3] )
```

#### Version (ver) (2 bits)

Indicates the CoAP version number.

#### Type (2 bits)

This describes the datagram's message type for the two message type context of Request and Response.

- Request
  - 0 : Confirmable : This message expects a corresponding acknowledgement message.
  - 1 : Non-confirmable : This message does not expect a confirmation message.
- Response
  - 2 : Acknowledgement : This message is a response that acknowledges a confirmable message.
  - 3 : Reset : This message indicates that it had received a message but could not process it.

#### Token length (4 bits)

Indicates the length of the variable-length Token field, which may be 0–8 bytes in length.

#### Request/response code (8 bits)

| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| Class | Code |   |   |   |   |   |   |

The three most significant bits form a number known as the "class", which is analogous to the class of HTTP status codes. The five least significant bits form a code that communicates further detail about the request or response. The entire code is typically communicated in the form `class.code` .

You can find the latest CoAP request/response codes at , though the below list gives some examples:

- Method: 0.XX EMPTYGETPOSTPUTDELETEFETCHPATCHiPATCH
- Success: 2.XX CreatedDeletedValidChangedContentContinue
- Client Error: 4.XX Bad RequestUnauthorizedBad OptionForbiddenNot FoundMethod Not AllowedNot AcceptableRequest Entity IncompleteConflictPrecondition FailedRequest Entity Too LargeUnsupported Content-Format
- Server error: 5.XX Internal server errorNot implementedBad gatewayService unavailableGateway timeoutProxying not supported
- Signaling Codes: 7.XX UnassignedCSMPingPongReleaseAbort

#### Message ID (16 bits)

Used to detect message duplication and to match messages of type acknowledgement/reset to messages of type confirmable/non-confirmable.

### Token

Every request carries a token (but it may be zero length) whose value was generated by the client. The server must echo every token value without any modification back to the client in the corresponding response. It is intended for use as a client-local identifier to match requests and responses, especially for concurrent requests.

Matching requests and responses is not done with the message ID because a response may be sent in a different message than the acknowledgement (which uses the message ID for matching). For example, this could be done to prevent retransmissions if obtaining the result takes some time. Such a detached response is called "separate response". In contrast, transmitting the response directly in the acknowledgement is called "piggybacked response" which is expected to be preferred for efficiency reasons.

### Option

| Bit position |   |   |   |   |   |   |   |
|---|---|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| Option delta | Option length |   |   |   |   |   |   |
| Option delta extended (none, 8 bits, 16 bits) |   |   |   |   |   |   |   |
| Option length extended (none, 8 bits, 16 bits) |   |   |   |   |   |   |   |
| Option value |   |   |   |   |   |   |   |

Option delta:

- 0 to 12: For delta between 0 and 12: Represents the exact delta value between the last option ID and the desired option ID, with no option delta extended value
- 13: For delta from 13 to 268: Option delta extended is an 8-bit value that represents the option delta value minus 13
- 14: For delta from 269 to 65,804: Option delta extended is a 16-bit value that represents the option delta value minus 269
- 15: Reserved for payload marker, where the option delta and option length are set together as 0xFF.

Option length:

- 0 to 12: For option length between 0 and 12: Represents the exact length value, with no option length extended value
- 13: For option length from 13 to 268: Option length extended is an 8-bit value that represents the option length value minus 13
- 14: For option length from 269 to 65,804: Option length extended is a 16-bit value that represents the option length value minus 269
- 15: Reserved for future use. It is an error for the option length field to be set to 0xFF.

Option value:

- Size of option value field is defined by option length value in bytes.
- Semantic and format this field depends on the respective option.

## Active protocol implementations

| Name | Programming Language | Implemented CoAP version | Client/Server | Implemented CoAP features | License | Link |
|---|---|---|---|---|---|---|
| coap | Dart | RFC 7252 | Client | Blockwise Transfers, Observe, Multicast, Proxying (partial) | MIT | https://github.com/shamblett/coap |
| aiocoap | Python 3 | RFC 7252, RFC 7641, RFC 7959, RFC 8323, RFC 7967, RFC 8132, RFC 9176, RFC 8613, RFC 9528 | Client + Server | Blockwise Transfers, Observe (partial) | MIT | pypi.python.org/pypi/aiocoap |
| Californium | Java | RFC 7252, RFC 7641, RFC 7959 | Client + Server | Observe, Blockwise Transfers, Multicast (since 2.x), DTLS (+ DTLS 1.2 Connection ID) | EPL+EDL | www.eclipse.org/californium github.com/eclipse/californium |
| CoAPSharp | C#, .NET | RFC 7252 | Client + Server | Core, Observe, Block, RD | MIT | github.com/FemtomaxInc/coapsharp |
| FreeCoAP | C | RFC 7252 | Client + Server + HTTP/CoAP Proxy | Core, DTLS, Blockwise Transfers | BSD | github.com/keith-cullen/FreeCoAP |
| Go-CoAP | Go | RFC 7252, RFC 8232, RFC 7641, RFC 7959 | Client + Server | Core, Observe, Blockwise, Multicast, TCP/TLS | Apache License 2.0 | github.com/plgd-dev/go-coap |
| java-coap | Java | RFC 7252, RFC 7641, RFC 7959, RFC 8323 | Client + Server |   | Apache License 2.0 | github.com/PelionIoT/java-coap |
| libcoap | C | RFC 7252, RFC 7390, RFC 7641, RFC 7959, RFC 7967, RFC 8132, RFC 8323, RFC 8516, RFC 8613, RFC 8768, RFC 8974, RFC 9175, RFC 9177 | Client + Server | Core, Observe, Multicast, Blockwise Transfers, Patch/Fetch, OSCORE, (D)TLS | BSD/GPL | https://github.com/obgm/libcoap |
| libcoapy | Python | same support as libcoap | MIT | github.com/anyc/libcoapy |   |   |
| lobaro-coap | C | RFC 7252 | Client + Server | Observe, Blockwise Transfers | MIT | www.lobaro.com/lobaro-coap |
| microCoAPy | MicroPython | RFC 7252 | Client + Server | Core | Apache License 2.0 | github.com/insighio/microCoAPy |
| nanoCoAP | C | RFC 7252 | Client + Server | Core, Blockwise Transfers, DTLS | LGPL | api.riot-os.org/group__net__nanocoap.html |
| node-coap | JavaScript | RFC 7252, RFC 7641, RFC 7959 | Client + Server | Core, Observe, Block | MIT | github.com/mcollina/node-coap |
| Qt CoAP | C++ | RFC 7252 | Client | Core, Observe, Blockwise Transfers | GPL, Commercial | https://doc.qt.io/qt-6/qtcoap-index.html |
| coap-rs | Rust | RFC 7252 | Client + Server | Core, Multicast, Observe option, *Too Many Requests* Response Code | MIT | github.com/Covertness/coap-rs docs.rs/coap/ |

## Proxy implementations

There exist proxy implementations which provide forward or reverse proxy functionality for the CoAP protocol and also implementations which translate between protocols like HTTP and CoAP.

The following projects provide proxy functionality:

- Squid 3.1.9 with transparent HTTP-CoAP mapping module
- jcoap Proxy
- Californium cf-proxy2
- CoAPthon
- FreeCoAP
- libcoap

## Projects using CoAP

| Name | Programming Language | Implemented CoAP version | Client/Server | Implemented CoAP features | License | Link |
|---|---|---|---|---|---|---|
| CoAP Shell | Java | RFC 7252 | Client | Observe, Blockwise Transfers, DTLS | Apache License 2.0 | https://github.com/tzolov/coap-shell |
| Copper | JavaScript (browser plugin) | RFC 7252 | Client | Observe, Blockwise Transfers | 3-clause BSD | https://github.com/mkovatsc/Copper https://addons.mozilla.org/firefox/addon/copper-270430/ |

## Inactive protocol implementations

| Name | Programming Language | Implemented CoAP version | Client/Server | Implemented CoAP features | License | Link |
|---|---|---|---|---|---|---|
| cantcoap | C++/C | RFC 7252 | Client + Server |   | BSD | https://github.com/staropram/cantcoap |
| Canopus | Go | RFC 7252 | Client + Server | Core | Apache License 2.0 | https://github.com/zubairhamed/canopus |
| CoAP implementation for Go | Go | RFC 7252 | Client + Server | Core + Draft Subscribe | MIT | https://github.com/dustin/go-coap |
| CoAP.NET | C# | RFC 7252, coap-13, coap-08, coap-03 | Client + Server | Core, Observe, Blockwise Transfers | 3-clause BSD | https://github.com/smeshlink/CoAP.NET |
| CoAPthon | Python | RFC 7252 | Client + Server + Forward Proxy + Reverse Proxy | Observe, Multicast server discovery, CoRE Link Format parsing, Block-wise | MIT | https://github.com/Tanganelli/CoAPthon |
| eCoAP | C | RFC 7252 | Client + Server | Core | MIT | https://gitlab.com/jobol/ecoap |
| Erbium for Contiki | C | RFC 7252 | Client + Server | Observe, Blockwise Transfers | 3-clause BSD | http://www.contiki-os.org/ (er-rest-example) |
| guile-coap | Guile | RFC 7252, RFC 8323 | Client + Server |   | GPL-3.0-or-later | https://codeberg.org/eris/guile-coap |
| iCoAP | Objective-C | RFC 7252 | Client | Core, Observe, Blockwise Transfers | MIT | https://github.com/stuffrabbit/iCoAP |
| jCoAP | Java | RFC 7252 | Client + Server | Observe, Blockwise Transfers | Apache License 2.0 | https://code.google.com/p/jcoap/ |
| LibNyoci | C | RFC 7252 | Client + Server | Core, Observe, Block, DTLS | MIT | https://github.com/darconeous/libnyoci |
| microcoap | C | RFC 7252 | Client + Server |   | MIT | https://github.com/1248/microcoap |
| nCoap | Java | RFC 7252 | Client + Server | Observe, Blockwise Transfers, CoRE Link Format, Endpoint-ID-Draft | BSD | https://github.com/okleine/nCoAP |
| Ruby coap | Ruby | RFC 7252 | Client + Server (david) | Core, Observe, Block, RD | MIT, GPL | https://github.com/nning/coap https://github.com/nning/david |
| Sensinode C Device Library | C | RFC 7252 | Client + Server | Core, Observe, Block, RD | Commercial | https://silver.arm.com/browse/SEN00 |
| Sensinode Java Device Library | Java SE | RFC 7252 | Client + Server | Core, Observe, Block, RD | Commercial | https://silver.arm.com/browse/SEN00 |
| Sensinode NanoService Platform | Java SE | RFC 7252 | Cloud Server | Core, Observe, Block, RD | Commercial | https://silver.arm.com/browse/SEN00 |
| SwiftCoAP | Swift | RFC 7252 | Client + Server | Core, Observe, Blockwise Transfers | MIT | https://github.com/stuffrabbit/SwiftCoAP |
| TinyOS CoapBlip | nesC/C | coap-13 | Client + Server | Observe, Blockwise Transfers | BSD | https://web.archive.org/web/20130312140509/http://docs.tinyos.net/tinywiki/index.php/CoAP |
| txThings | Python (Twisted) | RFC 7252 | Client + Server | Blockwise Transfers, Observe (partial) | MIT | https://github.com/mwasilak/txThings/ |
| YaCoAP | C |   |   |   | MIT | https://github.com/RIOT-Makers/YaCoAP |

## CoAP group communication

In many CoAP application domains it is essential to have the ability to address several CoAP resources as a group, instead of addressing each resource individually (e.g. to turn on all the CoAP-enabled lights in a room with a single CoAP request triggered by toggling the light switch). To address this need, the IETF has developed an optional extension for CoAP in the form of an experimental RFC: Group Communication for CoAP - RFC 7390 This extension relies on IP multicast to deliver the CoAP request to all group members. The use of multicast has certain benefits such as reducing the number of packets needed to deliver the request to the members. However, multicast also has its limitations such as poor reliability and being cache-unfriendly. An alternative method for CoAP group communication that uses unicasts instead of multicasts relies on having an intermediary where the groups are created. Clients send their group requests to the intermediary, which in turn sends individual unicast requests to the group members, collects the replies from them, and sends back an aggregated reply to the client.

## Security

CoAP defines four security modes:

- NoSec, where DTLS is disabled
- PreSharedKey, where DTLS is enabled, there is a list of pre-shared keys, and each key includes a list of which nodes it can be used to communicate with. Devices must support the AES cipher suite.
- RawPublicKey, where DTLS is enabled and the device uses an asymmetric key pair without a certificate, which is validated out of band. Devices must support the AES cipher suite and Elliptic Curve algorithms for key exchange.
- Certificate, where DTLS is enabled and the device uses X.509 certificates for validation.

Research has been conducted on optimizing DTLS by implementing security associates as CoAP resources rather than using DTLS as a security wrapper for CoAP traffic. This research has indicated that improvements of up to 6.5 times none optimized implementations.

In addition to DTLS, RFC8613 defines the Object Security for Constrained RESTful Environments (OSCORE) protocol which provides security for CoAP at the application layer.

## Security issues

Although the protocol standard includes provisions for mitigating the threat of DDoS amplification attacks, these provisions are not implemented in practice, resulting in the presence of over 580,000 targets primarily located in China and attacks up to 320 Gbit/s.
