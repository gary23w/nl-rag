---
title: "QUIC"
source: https://en.wikipedia.org/wiki/QUIC
domain: quic-protocol
license: CC-BY-SA-4.0
tags: quic protocol, quic transport, udp transport
fetched: 2026-07-02
---

# QUIC

**QUIC** (/kwɪk/) is a general-purpose transport layer network protocol initially designed by Jim Roskind at Google. It was first implemented and deployed in 2012 and was publicly announced in 2013 as experimentation broadened. It was also described at an IETF meeting. QUIC is supported by major web browsers, including Chrome, Edge, Firefox, and Safari. In Chrome, QUIC is used by more than half of all connections to Google's servers.

QUIC improves performance of connection-oriented web applications that previously relied on Transmission Control Protocol (TCP). It does this by establishing a number of multiplexed connections between two endpoints using User Datagram Protocol (UDP), and it is designed to obsolete TCP at the transport layer for many applications. Although its name was initially proposed as an acronym for *Quick UDP Internet Connections*, in IETF's use of the word *QUIC* is not an acronym; it is simply the name of the protocol.

QUIC works hand-in-hand with HTTP/3's multiplexed connections, allowing multiple streams of data to reach all the endpoints independently, and hence independent of packet losses involving other streams. In contrast, HTTP/2, which is carried over TCP, can suffer head-of-line-blocking delays if multiple streams are multiplexed on a TCP connection and any of the TCP packets on that connection are delayed or lost.

QUIC's secondary goals include reduced connection and transport latency, and bandwidth estimation in each direction to avoid congestion. It also moves congestion control algorithms into the user space at both endpoints, rather than the kernel space, which is claimed to allow these algorithms to improve more rapidly. Additionally, the protocol can be extended with forward error correction (FEC) to further improve performance when errors are expected. It is designed with the intention of avoiding protocol ossification.

In June 2015, an Internet Draft of a specification for QUIC was submitted to the IETF for standardization. A QUIC working group was established in 2016. In October 2018, the IETF's HTTP and QUIC Working Groups jointly decided to call the HTTP mapping over QUIC "HTTP/3" in advance of making it a worldwide standard. In May 2021, the IETF standardized QUIC in RFC 9000, supported by RFC 8999, 9001 and 9002. DNS-over-QUIC is another application.

## Background

Transmission Control Protocol, or TCP, aims to provide an interface for sending streams of data between two endpoints. Data is sent to the TCP system, which ensures it reaches the other end in the exact same form; if any discrepancies occur, the connection will signal an error condition.

To do this, TCP breaks up the data into network packets and adds small amounts of data to each packet. This additional data includes a sequence number that is used to detect packets that are lost or arrive out of order, and a checksum that allows the errors within packet data to be detected. When either problem occurs, TCP uses automatic repeat request (ARQ) to ask the sender to re-send the lost or damaged packet.

In most implementations, TCP will see any error on a connection as a blocking operation, stopping further transfers until the error is resolved or the connection is considered failed. If a single connection is being used to send multiple streams of data, as is the case in the HTTP/2 protocol, all of these streams are blocked although only one of them might have a problem. For instance, if a single error occurs while downloading a GIF image used for a favicon, the entire rest of the page will wait while that problem is resolved. This phenomenon is known as head-of-line blocking.

As the TCP system is designed to look like a "data pipe", or stream, it deliberately has little information regarding the data it transmits. If that data has additional requirements, like encryption using TLS, this must be set up by systems running on top of TCP, using TCP to communicate with similar software on the other end of the connection. Each of these sorts of setup tasks requires its own handshake process. This often requires several round-trips of requests and responses until the connection is established. Due to the inherent latency of long-distance communications, this can add significant delay to the overall transmission.

TCP has suffered from protocol ossification, due to its wire image being in cleartext and hence visible to and malleable by middleboxes. One measurement found that a third of paths across the Internet encounter at least one intermediary that modifies TCP metadata, and 6.5% of paths encounter harmful ossifying effects from intermediaries. Extensions to TCP have been affected: the design of Multipath TCP (MPTCP) was constrained by middlebox behaviour, and the deployment of TCP Fast Open has been likewise hindered.

## Characteristics

In the context of supporting encrypted HTTP traffic, QUIC serves a role similar to that of TCP, but with reduced latency during connection setup and more efficient loss recovery when multiple HTTP streams are multiplexed over a single connection. It does this primarily through two changes that rely on the understanding of the behaviour of HTTP traffic.

The first change is to greatly reduce overhead during connection setup. As most HTTP connections will demand TLS, QUIC makes the exchange of setup keys and listing of supported protocols part of the initial handshake process. When a client opens a connection, the response packet includes the data needed for future packets to use encryption. This eliminates the need to set up an unencrypted *pipe* and then negotiate the security protocol as separate steps. Other protocols can be serviced in the same way, combining multiple steps into a single request–response pair. This data can then be used both for following requests in the initial setup and future requests that would otherwise be negotiated as separate connections.

The second change is to use UDP rather than TCP as its basis, which does not include loss recovery. Instead, each QUIC stream is separately flow-controlled, and lost data is retransmitted at the level of QUIC, not UDP. This means that if an error occurs in one stream, like the favicon example above, the protocol stack can continue servicing other streams independently. This can be very useful in improving performance on error-prone links, as in most cases considerable additional data may be received before TCP notices a packet is missing or broken, and all of this data is blocked or even flushed while the error is corrected. In QUIC, this data is free to be processed while the single multiplexed stream is repaired.

QUIC includes a number of other changes that improve overall latency and throughput. For instance, the packets are encrypted individually, so that they do not result in the encrypted data waiting for partial packets. This is not generally possible under TCP, where the encryption records are in a bytestream and the protocol stack is unaware of higher-layer boundaries within this stream. These can be negotiated by the layers running on top, but QUIC aims to do all of this in a single handshake process.

Another goal of the QUIC system was to improve performance during network-switching events, like what happens when a user of a mobile device moves from a local Wi-Fi hotspot to a mobile network. When this occurs on TCP, a lengthy process starts where every existing connection times out one-by-one and is then re-established on demand. To solve this problem, QUIC includes a connection identifier to uniquely identify the connection to the server regardless of source. This allows the connection to be re-established simply by sending a packet, which always contains this ID, as the original connection ID will still be valid even if the user's IP address changes.

QUIC can be implemented in the application space, as opposed to being in the operating system kernel. This generally invokes additional overhead due to context switches as data is moved between applications. However, in the case of QUIC, the protocol stack is intended to be used by a single application, with each application using QUIC having its own connections hosted on UDP. Ultimately the difference could be very small because much of the overall HTTP/2 stack is already in the applications (or their libraries, more commonly). Placing the remaining parts in those libraries, essentially the error correction, has little effect on the HTTP/2 stack's size or overall complexity.

This organization allows future changes to be made more easily as it does not require changes to the kernel for updates. One of QUIC's longer-term goals is to add new systems for forward error correction (FEC) and improved congestion control.

One concern about the move from TCP to UDP is that TCP is widely adopted and many of the "middleboxes" in the Internet infrastructure are tuned for TCP and rate-limit or even block UDP. Google carried out a number of exploratory experiments to characterize this and found that only a small number of connections were blocked in this manner. This led to the use of a system for rapid fallback to TCP; Chromium's network stack starts both a QUIC and a conventional TCP connection at the same time, which allows it to fall back with negligible latency.

QUIC has been specifically designed to be deployable and evolvable and to have anti-ossification properties; it is the first IETF transport protocol to deliberately minimise its wire image for these ends. Beyond encrypted headers, it is 'greased' and it has protocol invariants explicitly specified.

The security layer of QUIC is based on TLS 1.2 or TLS 1.3. Earlier insecure protocols such as TLS 1.0 are not allowed in a QUIC stack.

### Google QUIC (gQUIC)

The protocol originally developed by Google, known as gQUIC, was first deployed around 2012 and later brought to the IETF. However, the version of QUIC standardized by the IETF is significantly different from the earlier Google implementation. Google's QUIC was initially designed as a general-purpose web protocol and was deployed mainly to support HTTP and HTTPS in Chromium, using its own encryption and transport mechanisms. In contrast, the IETF QUIC protocol has been redeveloped as a general-purpose transport protocol that uses standard TLS 1.3 for its cryptographic handshake and incorporates a modular packet and connection design intended for broader interoperability. Chromium developers have continued to follow the progress of IETF QUIC standardization and have worked to adopt and comply with the evolving Internet standards for QUIC within Chromium. The transition to IETF QUIC in Chrome began progressing publicly around 2020.

## Applications

QUIC was developed with HTTP in mind, and HTTP/3 was its first application. DNS-over-QUIC is an application of QUIC to name resolution, providing security for data transferred between resolvers similar to DNS-over-TLS. The IETF is developing applications of QUIC for secure network tunnelling and streaming media delivery. XMPP has experimentally been adapted to use QUIC. Another application is SMB over QUIC, which, according to Microsoft, can offer an "SMB VPN" without affecting the user experience. SMB clients use TCP by default and will attempt QUIC if the TCP attempt fails or if intentionally requiring QUIC.

## Adoption

### Browser support

The QUIC code was experimentally developed in Google Chrome starting in 2012, and was announced as part of Chromium version 29 (released on August 20, 2013). It is currently enabled by default in Chromium and Chrome.

Support in Firefox arrived in May 2021.

Apple added experimental support in the WebKit engine through the Safari Technology Preview 104 in April 2020. Official support was added in Safari 14, included in macOS Big Sur and iOS 14, but the feature needed to be turned on manually. It was later enabled by default in Safari 16.

### Client support

The cronet library for QUIC and other protocols is available to Android applications as a module loadable via Google Play Services.

cURL 7.66, released 11 September 2019, supports HTTP/3 (and thus QUIC).

In October 2020, Facebook announced that it has successfully migrated its apps, including Instagram, and server infrastructure to QUIC, with already 75% of its Internet traffic using QUIC. All mobile apps from Google support QUIC, including YouTube and Gmail. Uber's mobile app also uses QUIC.

### Server support

As of 2017, there are several actively maintained implementations. Google servers support QUIC and Google has published a prototype server. Akamai Technologies has supported QUIC since July 2016. A Go implementation called quic-go is also available, and powers experimental QUIC support in the Caddy server. On July 11, 2017, LiteSpeed Technologies officially began supporting QUIC in their load balancer (WebADC) and LiteSpeed Web Server products. As of October 2019, 88.6% of QUIC websites used LiteSpeed and 10.8% used Nginx. Although at first only Google servers supported HTTP-over-QUIC connections, Facebook also launched the technology in 2018, and Cloudflare has been offering QUIC support on a beta basis since 2018. The HAProxy load balancer added experimental support for QUIC in March 2022 and declared it production-ready in March 2023. As of April 2023, 8.9% of all websites use QUIC, up from 5% in March 2021. Microsoft Windows Server 2022 supports both HTTP/3 and SMB over QUIC protocols via MsQuic. The Application Delivery Controller of Citrix (Citrix ADC, NetScaler) can function as a QUIC proxy since version 13.

In addition, there are several stale community projects: libquic was created by extracting the Chromium implementation of QUIC and modifying it to minimize dependency requirements, and goquic provides Go bindings of libquic. Finally, quic-reverse-proxy is a Docker image that acts as a reverse proxy server, translating QUIC requests into plain HTTP that can be understood by the origin server.

.NET 5 introduces experimental support for QUIC using the MsQuic library.

## Source code

| Implementation | License | Language | Description |
|---|---|---|---|
| Chromium | BSD-3-Clause License | C++ | This is the source code of the Chrome web browser and the reference gQUIC implementation. It contains a standalone gQUIC and QUIC client and server programs that can be used for testing. Browsable source code. This version is also the basis of LINE's stellite and Google's cronet. |
| MsQuic | MIT License | C | A cross platform QUIC implementation from Microsoft designed to be a general purpose QUIC library. Used in Windows and cross platform by .NET. Rust and C# interop layers available are available, as well as convenience C++ wrapper classes. |
| QUIC Library (mvfst) | MIT License | C++ | mvfst (Pronounced move fast) is a client and server implementation of IETF QUIC protocol in C++ by Facebook. |
| LiteSpeed QUIC Library (lsquic) | MIT License | C | This is the QUIC and HTTP/3 implementation used by LiteSpeed Web Server and OpenLiteSpeed. |
| ngtcp2 | MIT License | C | This is a QUIC library that's crypto library agnostic and works with OpenSSL or GnuTLS. For HTTP/3, it needs a separate library like nghttp3. |
| Quiche | BSD-2-Clause License | Rust | Socket-agnostic and exposes a C API for use in C/C++ applications. |
| quicly | MIT License | C | This library is the QUIC implementation for the H2O web server. |
| quic-go | MIT License | Go | This library provides QUIC support for Go. |
| Quinn | Apache License 2.0 MIT License | Rust | An async-friendly QUIC implementation in Rust |
| Neqo | Apache License 2.0 MIT License | Rust | This implementation from Mozilla is planned to be integrated in Necko, a network library used in the Firefox web browser |
| aioquic | BSD-3-Clause License | Python | This library features an I/O-free API suitable for embedding in both clients and servers. |
| picoquic | MIT License | C | A minimal implementation of QUIC aligned with the IETF specifications |
| pquic | MIT License | C | An extensible QUIC implementation that includes an eBPF virtual machine that is able to dynamically load extensions as plugins |
| quic | BSD-3-Clause License | Haskell | This package implements QUIC based on Haskell lightweight threads. |
| netty-incubator-codec-quic | Apache License 2.0 | Java | This package implements QUIC in netty based on the Quiche implementation. |
| nodejs-quic | MIT License | NodeJs | This experimental package implements QUIC for Nodejs. |
| s2n-quic | Apache License 2.0 | Rust | Open-source Rust implementation from Amazon Web Services |
| swift-quic | Apache License 2.0 | Swift | Swift implementation pitched for incubation at the Swift Server Workgroup. |
| TQUIC | Apache License 2.0 | Rust | A high-performance, lightweight, and cross-platform QUIC library |
| nginx | BSD-2-Clause License | C | Open-source QUIC server implementation |
| HAProxy | GNU General Public License version 2 | C | Open-source QUIC server implementation |
| kwik | GNU Lesser General Public License version 3 | Java | Client and server implementations of the QUIC protocol in 100% Java. Supports HTTP3 with "Flupke" add-on. |
| OpenSSL | Apache License | C | OpenSSL has added QUIC support since version 3.2. |
| GnuTLS | GNU Lesser General Public License version 2.1 | C | GnuTLS has added QUIC support since version 3.7. |
| Linux QUIC | GNU General Public License version 2 | C | An in‑kernel QUIC implementation for Linux, offering standard POSIX socket APIs to kernel subsystems and userspace applications. |
