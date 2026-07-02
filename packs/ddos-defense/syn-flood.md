---
title: "SYN flood"
source: https://en.wikipedia.org/wiki/SYN_flood
domain: ddos-defense
license: CC-BY-SA-4.0
tags: ddos mitigation, denial of service attack, distributed denial of service, rate limiting, syn flood defense
fetched: 2026-07-02
---

# SYN flood

**SYN flooding** (or TCP **SYN flood**) is a form of denial-of-service attack against systems that provide services over the Transmission Control Protocol (TCP). It exploits the way many TCP implementations handle incoming connection requests by causing a server to retain state for large numbers of incomplete (or “half-open”) connections, leaving insufficient resources to accept new legitimate connections.

The attack typically targets a TCP service in the LISTEN state (such as a web or mail server). An attacker sends a rapid stream of TCP SYN packets—often using spoofed source IP addresses—so that the server replies with SYN-ACK packets and allocates resources for each pending connection, but does not receive the final ACK needed to complete the TCP three-way handshake. If enough such requests are received, the server's backlog of pending connections can be exhausted, causing legitimate connection attempts to be delayed or rejected.

SYN flooding was publicly described in 1996, although some sources claim it was documented in 1994 and became a widely recognised network attack in the same period. A range of mitigations have since been developed, including ingress filtering, increasing backlog limits, reducing timeouts for half-open connections, SYN caches, SYN cookies, and firewall or proxy-based defences. RFC 4987 (2007) describes the attack and surveys common countermeasures and their trade-offs, but does not define standards-level recommendations.

Modern operational reporting indicates that SYN floods remain a significant DDoS vector, even alongside larger volumetric attacks such as DNS and UDP floods. In 2025, Cloudflare reported that SYN floods were the second most common Layer 3/4 DDoS attack vector, accounting for 27% of attacks.

## Technical details

When a client attempts to start a TCP connection to a server, the client and server exchange a series of messages which normally runs like this:

1. The client requests a connection by sending a `SYN` (*synchronize*) message to the server.
2. The server *acknowledges* this request by sending `SYN-ACK` back to the client.
3. The client responds with an `ACK`, and the connection is established.

This is called the TCP three-way handshake, and is the foundation for every connection established using the TCP protocol.

A SYN flood attack works by not responding to the server with the expected `ACK` code. The malicious client can either simply not send the expected `ACK`, or by spoofing the source IP address in the `SYN`, cause the server to send the `SYN-ACK` to a falsified IP address – which will not send an `ACK` because it "knows" that it never sent a `SYN`.

The server will wait for the acknowledgement for some time, as simple network congestion could also be the cause of the missing `ACK`. However, in an attack, the *half-open connections* created by the malicious client bind resources on the server and may eventually exceed the resources available on the server. At that point, the server cannot connect to any clients, whether legitimate or otherwise. This effectively denies service to legitimate clients. Some systems may also malfunction or crash when other operating system functions are starved of resources in this way.

## Countermeasures

RFC 4987 describes several broad classes of mitigation for SYN flooding. These include ingress/source-address filtering (to reduce spoofed traffic), increasing backlog limits and shortening SYN-RECEIVED timeouts (simple but limited measures), and more robust end-host techniques such as SYN caches (which defer full state allocation) and SYN cookies (which avoid allocating state for half-open connections by encoding connection information into the SYN-ACK sequence number), which are included in most major operating systems.
