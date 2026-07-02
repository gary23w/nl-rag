---
title: "traceroute"
source: https://en.wikipedia.org/wiki/Traceroute
domain: icmp
license: CC-BY-SA-4.0
tags: icmp, icmpv6, internet control message protocol, traceroute
fetched: 2026-07-02
---

# traceroute

In computing, **`traceroute`** and **`tracert`** are diagnostic command-line interface commands for displaying possible routes (paths) and transit delays of packets across an Internet Protocol (IP) network.

The ping utility only computes the final round-trip times from the destination point, while route-tracing utilities can show more detail, such as the round-trip times of the packets received from each successive host (remote node) along the route to a destination and the sum of the mean times in each hop as a measure of the total time spent to establish the connection.

For Internet Protocol Version 6 (IPv6), the tool sometimes has the name **`traceroute6`** and **`tracert6`**.

## Implementations

A command is available in many modern operating systems, generally named `traceroute` in Unix-like systems such as FreeBSD, macOS, and Linux and named `tracert` in Windows and ReactOS.

On Linux, *tracepath* is a utility similar to traceroute, with the primary difference of not requiring superuser privileges. Tracepath is part of the *iputils* group that contains the package *ping*.

The functionality was available graphically in macOS, but has been deprecated since the release of macOS Big Sur.

Windows NT-based operating systems also provide PathPing, which combines the functionality of ping with that of tracert.

On Unix-like operating systems, traceroute sends, by default, a sequence of User Datagram Protocol (UDP) packets, with destination port numbers ranging from 33434 to 33534; the implementations of traceroute shipped with Linux, FreeBSD, NetBSD, OpenBSD, DragonFly BSD, and macOS include an option to use ICMP Echo Request packets (*-I*), or any arbitrary protocol (*-P*) such as UDP, TCP using TCP SYN packets, or ICMP.

On Windows, tracert sends ICMP Echo Request packets, rather than the UDP packets traceroute sends by default.

The time-to-live (TTL) value, also known as *hop limit*, is used in determining the intermediate routers being traversed towards the destination. Traceroute sends packets with TTL values that gradually increase from packet to packet, starting with TTL value of one. Routers decrement TTL values of packets by one when routing and discard packets whose TTL value has reached zero, returning the ICMP error message ICMP Time Exceeded. For the first set of packets, the first router receives the packet, decrements the TTL value and drops the packet because it then has TTL value zero. The router sends an ICMP Time Exceeded message back to the source. The next set of packets are given a TTL value of two, so the first router forwards the packets, but the second router drops them and replies with ICMP Time Exceeded. Proceeding in this way, traceroute uses the returned ICMP Time Exceeded messages to build a list of routers that packets traverse, until the destination is reached and returns an ICMP Destination Unreachable message if UDP packets are being used or an ICMP Echo Reply message if ICMP Echo messages are being used.

The timestamp values returned for each router along the path are the delay (latency) values, typically measured in milliseconds for each packet.

The sender expects a reply within a configured number of seconds. If a packet is not acknowledged within the expected interval, an asterisk is displayed.

The Internet Protocol does not require packets to take the same route towards a particular destination, thus hosts listed might be hosts that other packets have traversed. If the host at hop #N does not reply, the hop is skipped in the output.

If a network has a firewall and operates both Windows and Unix-like systems, more than one protocol must be enabled inbound through the firewall for traceroute to work and receive replies.

Some traceroute implementations use TCP packets, such as *tcptraceroute* and layer four traceroute (lft). PathPing is a utility introduced with Windows NT that combines ping and traceroute functionality. MTR is an enhanced version of ICMP traceroute available for Unix-like and Windows systems. The various implementations of traceroute all rely on ICMP Time Exceeded (type 11) packets being sent to the source.

Cisco's implementation of traceroute also uses a sequence of UDP datagrams, each with incrementing TTL values, to an invalid port number at the remote host; by default, UDP port 33434 is used. An extended version of this command (known as the *extended traceroute* command) can change the destination port number used by the UDP probe messages.

## Usage

Most implementations include options to specify the number of queries to send per hop, time to wait for a response, the hop limit and port to use. Invoking traceroute with no options displays the list of available options

For Linux, *man traceroute* presents more details, including the displayed error flags.

For example:

```mw
$ traceroute -w 3 -q 1 -m 16 example.com
traceroute to example.com (93.184.216.34), 16 hops max, 52 byte packets
 1  192.x.x.x (192.x.x.x)  5.152 ms
 2  10.x.x.x (10.x.x.x)  12.767 ms
 3  172.x.x.x (172.x.x.x)  11.638 ms
 4  172.x.x.x (172.x.x.x)  13.193 ms
 5  xxx.x.x.x.cox.net (68.x.x.x)  20.624 ms
 6  xxx.xxx.xxx.edgecastcdn.net (192.x.x.x)  56.205 ms
 7  xxx.xxx.xxx.edgecastcdn.net (192.x.x.x)  24.573 ms
 8  *
 9  *
10  93.x.x.x (93.x.x.x)  22.810 ms
11  93.x.x.x (93.x.x.x)  20.235 ms
```

In the example above, selected options are to wait for three seconds (instead of five), send out only one query to each hop (instead of three), limit the maximum number of hops to 16 before giving up (instead of 30), with *example.com* as the final host. On line 8 and 9 (TTLs 8 and 9) it shows asterisks where the router did not respond within the timeout.

## Value

Traceroute can help identify incorrect routing table definitions or firewalls that may be blocking ICMP traffic, or high port UDP in Unix ping, to a site. A correct traceroute response does not guarantee connectivity for applications as a firewall may permit ICMP packets but not permit packets of other protocols.

Traceroute is used by penetration testers to gather information about network infrastructure and IP address ranges around a given host.

Traceroute can be used to optimize data download. If there are multiple mirrors available for the same resource, each mirror can be traced to find the fastest.

## Origins

The traceroute manual page states that the original traceroute program was written by Van Jacobson in 1987 from a suggestion by Steve Deering, and that Guy Almes and Matt Mathis also had the idea concurrent with Deering. The author of the ping program, Mike Muuss, states on his website that traceroute was written using kernel ICMP support that he had earlier coded to enable raw ICMP sockets when he first wrote the ping program.

## Limitations

Traceroute has multiple limitations. Traceroute does not discover paths at the router level, but at the interface level. Another limitation appears when routers do not respond to probes or when routers have a limit for ICMP responses. In the presence of traffic load balancing, traceroute may indicate a path that does not actually exist; to minimize this problem there is a traceroute modification called Paris-traceroute, which maintains the flow identifier of the probes to avoid load balancing.
