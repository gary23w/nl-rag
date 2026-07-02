---
title: "Keepalive"
source: https://en.wikipedia.org/wiki/Keep-alive
domain: undici-client
license: CC-BY-SA-4.0
tags: undici client, node http client, connection pooling, keep-alive dispatcher
fetched: 2026-07-02
---

# Keepalive

(Redirected from

Keep-alive

)

A **keepalive** (**KA**) is a message sent by one device to another to check that the link between the two is operating, or to prevent the link from being broken.

## Description

Once a TCP connection has been established, that connection is defined to be valid until one side closes it. Once the connection has entered the connected state, can theoretically remain connected indefinitely. In reality, the connection will not last indefinitely. Many firewall or NAT systems will close a connection if there has been no activity in some time period. The Keep Alive signal can be used to trick intermediate hosts to not close the connection due to inactivity. It is also possible that one host is no longer listening (e.g. application or system crash). In this case, the connection is closed, but no `FIN` (short for 'finish') was ever sent. In this case, a KeepAlive packet can be used to interrogate a connection to check if it is still intact.

A keepalive signal is often sent at predefined intervals, and plays an important role on the Internet. After a signal is sent, if no reply is received, the link is assumed to be down and future data will be routed via another path until the link is up again. A keepalive signal can also be used to indicate to Internet infrastructure that the connection should be preserved. Without a keepalive signal, intermediate NAT-enabled routers can drop the connection after timeout.

Since the only purpose is to find links that do not work or to indicate connections that should be preserved, keepalive messages tend to be short and not take much bandwidth. However, their precise format and usage terms depend on the communication protocol.

## TCP keepalive

Transmission Control Protocol (TCP) keepalives are an optional feature, and if included must default to off.

### Probe TCP packets

A proper keepalive packet (sometimes called a *probe*) contains no data. It is exceptionally tolerated to optionally enable the use of 1 "garbage octet" in the keepalive packet but this is only to comply with erroneous TCP implementations. In an Ethernet network, keepalive packets result in frames of minimum size (64 bytes).

### Keepalive algorithm and configuration

Regarding TCP keepalive, RFC 1122 only describes conditions under which a keepalive packet can be sent, what the packet contains, how destination host must behave (ACK reply) when receiving it and that dataless ACK packet transmission is unreliable, even in TCP (which implies that a connection can actually still be operational but that an intermediary might be discarding ACK packets with no data). However, besides a configurable interval (or at least 2 hours by default) at which keepalive packets can be sent, no particular algorithm is prescribed. Consequentially, operating systems vary in how they implement TCP keepalive. For example, Windows Server 2008 and Windows Vista use a simple RFC-compliant implementation that sends a keepalive packet at a single configurable time interval; they make no time interval distinction between the first keepalive packet sent on the connection and those sent afterwards if no reply was received from the destination host. While under Linux, three parameters are used to configure TCP keepalive:

- A **keepalive delay** which tells after how much time the first keepalive packet will be sent on an apparently idle connection.
- A **keepalive interval** which is the duration between two successive keepalive retransmissions, if acknowledgement to the previous keepalive transmission is not received.
- A **keepalive probe count** which is the maximal number of consecutive unresponded keepalive packets before declaring that remote end is not available.

### General behavior

When two hosts are connected over a network via TCP/IP, TCP keepalive packets can be used to determine if the connection is still valid, and terminate it if needed.

Most hosts that support TCP also support TCP keepalive. Each host (or peer) periodically sends a TCP packet to its peer which solicits a response. If a certain number of keepalives are sent and no response (ACK) is received, the sending host will terminate the connection from its end. If a connection has been terminated due to a TCP keepalive time-out and the other host eventually sends a packet for the old connection, the host that terminated the connection will send a packet with the RST flag set to signal the other host that the old connection is no longer active. This will force the other host to terminate its end of the connection so a new connection can be established.

### Real world default behavior

Typically, TCP keepalives are sent every 45 or 60 seconds on an idle TCP connection, and the connection is dropped after 3 sequential ACKs are missed. This varies by host, e.g. by default, Windows PCs send the first TCP keepalive packet after 7200000ms (2 hours), then send 5 keepalives at 1000ms intervals, dropping the connection if there is no response to any of the keepalive packets. Linux hosts send the first TCP Keepalive packet after 2 hours (default since Linux 2.2), then send 9 keepalive probes (default since Linux 2.2) at 75 seconds (default since Linux 2.4) intervals, dropping the connection if there is no response to any of the Keepalive packets.

## Keepalive on higher layers

Since TCP keepalive is optional, various protocols (e.g. SMB and TLS) implement their own keep-alive feature on top of TCP. It is also common for protocols which maintain a session over a connectionless protocol, e.g. OpenVPN over UDP, to implement their own keep-alive.

## Similar concepts

### HTTP keepalive

The Hypertext Transfer Protocol (HTTP) uses the keyword `keep-alive` in the `Connection` header to signal that the connection should be kept open for further messages (this is the default in HTTP 1.1, but in HTTP 1.0 the default was to use a new connection for each request/reply pair). Despite the similar name, this function is entirely unrelated.
