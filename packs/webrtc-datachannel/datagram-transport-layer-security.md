---
title: "Datagram Transport Layer Security"
source: https://en.wikipedia.org/wiki/Datagram_Transport_Layer_Security
domain: webrtc-datachannel
license: CC-BY-SA-4.0
tags: webrtc datachannel, peer-to-peer data channel, browser peer connection, webrtc data transfer
fetched: 2026-07-02
---

# Datagram Transport Layer Security

**Datagram Transport Layer Security** (**DTLS**) is a communications protocol providing security to datagram-based applications by allowing them to communicate in a way designed to prevent eavesdropping, tampering, or message forgery. The DTLS protocol is based on the stream-oriented Transport Layer Security (TLS) protocol and is intended to provide similar security guarantees. The DTLS protocol datagram preserves the semantics of the underlying transport—the application does not suffer from the delays associated with stream protocols, but because it uses User Datagram Protocol (UDP) or Stream Control Transmission Protocol (SCTP), the application has to deal with packet reordering, loss of datagram and data larger than the size of a datagram network packet. Because DTLS uses UDP or SCTP rather than TCP it avoids the TCP meltdown problem when being used to create a VPN tunnel.

## Definition

The following documents define DTLS:

- RFC 5238 from May 2008 for use with Datagram Congestion Control Protocol (DCCP)
- RFC 5415 from March 2009 for use with Control And Provisioning of Wireless Access Points (CAPWAP)
- RFC 5764 from May 2010 for use with Secure Real-time Transport Protocol (SRTP) subsequently called **DTLS-SRTP** in a draft with Secure Real-Time Transport Control Protocol (SRTCP)
- RFC 6083 from January 2011 for use with Stream Control Transmission Protocol (SCTP) encapsulation
- RFC 6347 from January 2012 defining DTLS 1.2
- RFC 9147 from April 2022 defining DTLS 1.3

DTLS 1.0 is based on TLS 1.1, DTLS 1.2 is based on TLS 1.2, and DTLS 1.3 is based on TLS 1.3. There is no DTLS 1.1 because this version-number was skipped in order to harmonize version numbers with TLS. Like previous DTLS versions, DTLS 1.3 is intended to provide "equivalent security guarantees [to TLS 1.3] with the exception of order protection/non-replayability".

## Implementations

### Libraries

| Implementation | DTLS 1.0 | DTLS 1.2 | DTLS 1.3 |
|---|---|---|---|
| Botan | Yes | Yes |   |
| cryptlib | No | No |   |
| GnuTLS | Yes | Yes |   |
| Java Secure Socket Extension | Yes | Yes |   |
| LibreSSL | Yes | Yes |   |
| libsystools | Yes | No |   |
| MatrixSSL | Yes | Yes |   |
| mbed TLS (previously PolarSSL) | Yes | Yes |   |
| Network Security Services | Yes | Yes |   |
| OpenSSL | Yes | Yes |   |
| PyDTLS | Yes | Yes |   |
| Python3-dtls | Yes | Yes |   |
| RSA BSAFE | No | No |   |
| s2n | No | No |   |
| Schannel XP/2003, Vista/2008 | No | No |   |
| Schannel 7/2008R2, 8/2012, 8.1/2012R2, 10 | Yes | No |   |
| Schannel 10 (1607), 2016 | Yes | Yes |   |
| Secure Transport OS X 10.2–10.7 / iOS 1–4 | No | No |   |
| Secure Transport OS X 10.8–10.10 / iOS 5–8 | Yes | No |   |
| SharkSSL | No | No |   |
| tinydtls | No | Yes |   |
| Waher.Security.DTLS | No | Yes |   |
| wolfSSL (previously CyaSSL) | Yes | Yes | Yes |
| @nodertc/dtls | No | Yes |   |
| java-dtls | Yes | Yes |   |
| pion/dtls (Go) | No | Yes |   |
| californium/scandium (Java) | No | Yes |   |
| SNF4J (Java) | Yes | Yes |   |
| Implementation | DTLS 1.0 | DTLS 1.2 | DTLS 1.3 |

### Applications

- Cisco AnyConnect VPN Client uses TLS and invented DTLS-based VPN.
- OpenConnect is an open source AnyConnect-compatible client and ocserv server that supports (D)TLS.
- Cisco InterCloud Fabric uses DTLS to form a tunnel between private and public/provider compute environments.
- Cato Networks utilizes DTLS v1.2 for the underlay tunnel used by both the Cato Socket and Cato ZTNA (formerly SDP) client when forming tunnels to the Cato POPs and when forming off-cloud tunnels between Cato sockets.
- ZScaler tunnel 2.0 for ZScaler Internet Access (ZIA) uses DTLS for tunneling. ZScaler Private Access (ZPA) does not support DTLS
- F5 Networks Edge VPN Client uses TLS and DTLS.
- Fortinet's SSL VPN and Array Networks SSL VPN also use DTLS for VPN tunneling.
- Citrix Systems NetScaler uses DTLS to secure UDP.
- Web browsers: Google Chrome, Opera and Firefox support DTLS-SRTP for WebRTC. Firefox 86 and onward does not support DTLS 1.0.
- Remote Desktop Protocol 8.0 and onwards.

## Vulnerabilities

In February 2013 two researchers from Royal Holloway, University of London discovered a timing attack which allowed them to recover (parts of the) plaintext from a DTLS connection using the OpenSSL or GnuTLS implementation of DTLS when Cipher Block Chaining mode encryption was used.
