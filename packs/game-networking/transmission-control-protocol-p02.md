---
title: "Transmission Control Protocol (part 2/2)"
source: https://en.wikipedia.org/wiki/Transmission_Control_Protocol
domain: game-networking
license: CC-BY-SA-4.0
tags: game networking, netcode, multiplayer networking, network game architecture
fetched: 2026-07-02
part: 2/2
---

## Development

TCP is a complex protocol. However, while significant enhancements have been made and proposed over the years, its most basic operation has not changed significantly since its first specification RFC 675 in 1974, and the v4 specification RFC 793, published in September 1981. RFC 1122, published in October 1989, clarified a number of TCP protocol implementation requirements. A list of the 8 required specifications and over 20 strongly encouraged enhancements is available in RFC 7414. Among this list is RFC 2581, TCP Congestion Control, one of the most important TCP-related RFCs in recent years, describes updated algorithms that avoid undue congestion. In 2001, RFC 3168 was written to describe Explicit Congestion Notification (ECN), a congestion avoidance signaling mechanism.

The original TCP congestion avoidance algorithm was known as *TCP Tahoe*, but many alternative algorithms have since been proposed (including TCP Reno, TCP Vegas, FAST TCP, TCP New Reno, and TCP Hybla).

Multipath TCP (MPTCP) is an ongoing effort within the IETF that aims at allowing a TCP connection to use multiple paths to maximize resource usage and increase redundancy. The redundancy offered by Multipath TCP in the context of wireless networks enables the simultaneous use of different networks, which brings higher throughput and better handover capabilities. Multipath TCP also brings performance benefits in datacenter environments. The reference implementation of Multipath TCP was developed in the Linux kernel. Multipath TCP is used to support the Siri voice recognition application on iPhones, iPads and Macs.

tcpcrypt is an extension proposed in July 2010 to provide transport-level encryption directly in TCP itself. It is designed to work transparently and not require any configuration. Unlike TLS (SSL), tcpcrypt itself does not provide authentication, but provides simple primitives down to the application to do that. The tcpcrypt RFC was published by the IETF in May 2019.

TCP Fast Open is an extension to speed up the opening of successive TCP connections between two endpoints. It works by skipping the three-way handshake using a cryptographic *cookie*. It is similar to an earlier proposal called T/TCP, which was not widely adopted due to security issues. TCP Fast Open was published as RFC 7413 in 2014.

Proposed in May 2013, Proportional Rate Reduction (PRR) is a TCP extension developed by Google engineers. PRR ensures that the TCP window size after recovery is as close to the slow start threshold as possible. The algorithm is designed to improve the speed of recovery and is the default congestion control algorithm in Linux 3.2+ kernels.

### Deprecated proposals

TCP Cookie Transactions (TCPCT) is an extension proposed in December 2009 to secure servers against denial-of-service attacks. Unlike SYN cookies, TCPCT does not conflict with other TCP extensions such as window scaling. TCPCT was designed due to necessities of DNSSEC, where servers have to handle large numbers of short-lived TCP connections. In 2016, TCPCT was deprecated in favor of TCP Fast Open. The status of the original RFC was changed to *historic*.


## Hardware implementations

One way to overcome the processing power requirements of TCP is to build hardware implementations of it, widely known as TCP offload engines (TOE). The main problem of TOEs is that they are hard to integrate into computing systems, requiring extensive changes in the operating system of the computer or device.

TCP low power (*TCPlp*) has been demonstrated to work in resource constrained environments where otherwise UDP-based CoAP is preferred.


## Wire image and ossification

The wire data of TCP provides significant information-gathering and modification opportunities to on-path observers, as the protocol metadata is transmitted in cleartext. While this transparency is useful to network operators and researchers, information gathered from protocol metadata may reduce the end-user's privacy. This visibility and malleability of metadata has led to TCP being difficult to extend—a case of protocol ossification—as any intermediate node (a 'middlebox') can make decisions based on that metadata or even modify it, breaking the end-to-end principle. One measurement found that a third of paths across the Internet encounter at least one intermediary that modifies TCP metadata, and 6.5% of paths encounter harmful ossifying effects from intermediaries. Avoiding extensibility hazards from intermediaries placed significant constraints on the design of MPTCP, and difficulties caused by intermediaries have hindered the deployment of TCP Fast Open in web browsers. Another source of ossification is the difficulty of modification of TCP functions at the endpoints, typically in the operating system kernel or in hardware with a TCP offload engine.


## Performance

As TCP provides applications with the abstraction of a reliable byte stream, it can suffer from head-of-line blocking: if packets are reordered or lost and need to be retransmitted (and thus are reordered), data from sequentially later parts of the stream may be received before sequentially earlier parts of the stream; however, the later data cannot typically be used until the earlier data has been received, incurring network latency. If multiple independent higher-level messages are encapsulated and multiplexed onto a single TCP connection, then head-of-line blocking can cause processing of a fully-received message that was sent later to wait for delivery of a message that was sent earlier. Web browsers attempt to mitigate head-of-line blocking by opening multiple parallel connections. This incurs the cost of connection establishment repeatedly, as well as multiplying the resources needed to track those connections at the endpoints. Parallel connections also have congestion control operating independently of each other, rather than being able to pool information together and respond more promptly to observed network conditions; TCP's aggressive initial sending patterns can cause congestion if multiple parallel connections are opened; and the per-connection fairness model leads to a monopolization of resources by applications that take this approach.

Connection establishment is a major contributor to latency as experienced by web users. TCP's three-way handshake introduces one RTT of latency during connection establishment before data can be sent. For short flows, these delays are very significant. Transport Layer Security (TLS) requires a handshake of its own for key exchange at connection establishment. Because of the layered design, the TCP handshake and the TLS handshake proceed serially; the TLS handshake cannot begin until the TCP handshake has concluded. Two RTTs are required for connection establishment with TLS 1.2 over TCP. TLS 1.3 allows for zero RTT connection resumption in some circumstances, but, when layered over TCP, one RTT is still required for the TCP handshake, and this cannot assist the initial connection; zero RTT handshakes also present cryptographic challenges, as efficient, replay-safe and forward secure non-interactive key exchange is an open research topic. TCP Fast Open allows the transmission of data in the initial (i.e., SYN and SYN-ACK) packets, removing one RTT of latency during connection establishment. However, TCP Fast Open has been difficult to deploy due to protocol ossification; as of 2020, no Web browsers used it by default.

TCP throughput is affected by packet reordering. Reordered packets can cause duplicate acknowledgments to be sent, which, if they cross a threshold, will then trigger a spurious retransmission and congestion control. Transmission behavior can also become bursty, as large ranges are acknowledged all at once when a reordered packet at the range's start is received (in a manner similar to how head-of-line blocking affects applications). Blanton & Allman (2002) found that throughput was inversely related to the amount of reordering, up to a threshold where all reordering triggers spurious retransmission. Mitigating reordering depends on a sender's ability to determine that it has sent a spurious retransmission, and hence on resolving retransmission ambiguity. Reducing reordering-induced spurious retransmissions may slow recovery from genuine loss.

Selective acknowledgment can provide a significant benefit to throughput; Bruyeron, Hemon & Zhang (1998) measured gains of up to 45%. An important factor in the improvement is that selective acknowledgment can more often avoid going into slow start after a loss and can hence better use available bandwidth. However, TCP can only selectively acknowledge a maximum of three blocks of sequence numbers. This can limit the retransmission rate and hence loss recovery or cause needless retransmissions, especially in high-loss environments.

TCP was originally designed for wired networks where packet loss is considered to be the result of network congestion and the congestion window size is reduced dramatically as a precaution. However, wireless links are known to experience sporadic and usually temporary losses due to fading, shadowing, hand off, interference, and other radio effects, that are not strictly congestion. After the (erroneous) back-off of the congestion window size, due to wireless packet loss, there may be a congestion avoidance phase with a conservative decrease in window size. This causes the radio link to be underused. Extensive research on combating these harmful effects has been conducted. Suggested solutions can be categorized as end-to-end solutions, which require modifications at the client or server, link layer solutions, such as Radio Link Protocol in cellular networks, or proxy-based solutions which require some changes in the network without modifying end nodes. A number of alternative congestion control algorithms, such as Vegas, Westwood, Veno, and Santa Cruz, have been proposed to help solve the wireless problem.


## Acceleration

The idea of a TCP accelerator is to terminate TCP connections inside the network processor and then relay the data to a second connection toward the end system. The data packets that originate from the sender are buffered at the accelerator node, which is responsible for performing local retransmissions in the event of packet loss. Thus, in case of losses, the feedback loop between the sender and the receiver is shortened to the one between the acceleration node and the receiver which guarantees a faster delivery of data to the receiver.

Since TCP is a rate-adaptive protocol, the rate at which the TCP sender injects packets into the network is directly proportional to the prevailing load condition within the network as well as the processing capacity of the receiver. The prevalent conditions within the network are judged by the sender on the basis of the acknowledgments received by it. The acceleration node splits the feedback loop between the sender and the receiver and thus guarantees a shorter round trip time (RTT) per packet. A shorter RTT is beneficial as it ensures a quicker response time to any changes in the network and a faster adaptation by the sender to combat these changes.

Disadvantages of the method include the fact that the TCP session has to be directed through the accelerator; this means that if routing changes so that the accelerator is no longer in the path, the connection will be broken. It also destroys the end-to-end property of the TCP ACK mechanism; when the ACK is received by the sender, the packet has been stored by the accelerator, not delivered to the receiver.


## Debugging

A packet sniffer, which taps TCP traffic on a network link, can be useful in debugging networks, network stacks, and applications that use TCP by showing an engineer what packets are passing through a link. Some networking stacks support the SO_DEBUG socket option, which can be enabled on the socket using setsockopt. That option dumps all the packets, TCP states, and events on that socket, which is helpful in debugging. Netstat is another utility that can be used for debugging.


## Alternatives

For many applications TCP is not appropriate. The application cannot normally access the packets coming after a lost packet until the retransmitted copy of the lost packet is received. This causes problems for real-time applications such as streaming media, real-time multiplayer games and voice over IP (VoIP) where it is generally more useful to get most of the data in a timely fashion than it is to get all of the data in order.

For historical and performance reasons, most storage area networks (SANs) use Fibre Channel Protocol (FCP) over Fibre Channel connections. For embedded systems, network booting, and servers that serve simple requests from huge numbers of clients (e.g. DNS servers) the complexity of TCP can be a problem. Tricks such as transmitting data between two hosts that are both behind NAT (using STUN or similar systems) are far simpler without a relatively complex protocol like TCP in the way.

Generally, where TCP is unsuitable, the User Datagram Protocol (UDP) is used. This provides the same application multiplexing and checksums that TCP does, but does not handle streams or retransmission, giving the application developer the ability to code them in a way suitable for the situation, or to replace them with other methods such as forward error correction or error concealment.

Stream Control Transmission Protocol (SCTP) is another protocol that provides reliable stream-oriented services similar to TCP. It is newer and considerably more complex than TCP, and has not yet seen widespread deployment. However, it is especially designed to be used in situations where reliability and near-real-time considerations are important.

Venturi Transport Protocol (VTP) is a patented proprietary protocol that is designed to replace TCP transparently to overcome perceived inefficiencies related to wireless data transport. Especially in mobile communications and wireless networks, data transmission may become unstable due to high latency and signal interference.

The TCP congestion avoidance algorithm works very well for ad-hoc environments where the data sender is not known in advance. If the environment is predictable, a timing-based protocol such as Asynchronous Transfer Mode (ATM) can avoid TCP's retransmission overhead.

UDP-based Data Transfer Protocol (UDT) is designed for high-bandwidth, high-latency network environments, particularly for large-scale data transfers such as file or media streaming. In networks with a high bandwidth-delay product, UDT offers advantages over TCP, providing better efficiency and fairness.

Multipurpose Transaction Protocol (MTP/IP) is patented proprietary software that is designed to adaptively achieve high throughput and transaction performance in a wide variety of network conditions, particularly those where TCP is perceived to be inefficient.


## Checksum computation

### TCP checksum for IPv4

When TCP runs over IPv4, the method used to compute the checksum is defined as follows:

> *The checksum field is the 16-bit ones' complement of the ones' complement sum of all 16-bit words in the header and text. The checksum computation needs to ensure the 16-bit alignment of the data being summed. If a segment contains an odd number of header and text octets, alignment can be achieved by padding the last octet with zeros on its right to form a 16-bit word for checksum purposes. The pad is not transmitted as part of the segment. While computing the checksum, the checksum field itself is replaced with zeros.*

In other words, after appropriate padding, all 16-bit words are added using ones' complement arithmetic. The sum is then bitwise complemented and inserted as the checksum field. A pseudo-header that mimics the IPv4 packet header used in the checksum computation is as follows:

TCP pseudo-header for checksum computation (IPv4)

Offset

Octet

0

1

2

3

Octet

Bit

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

0

Source address

4

32

Destination address

8

64

Zeroes

Protocol

(6)

TCP length

12

96

Source port

Destination port

16

128

Sequence number

20

160

Acknowledgement number

24

192

Data offset

Reserved

Flags

Window

28

224

Checksum

Urgent pointer

32

256

(Options)

36

288

Data

40

320

⋮

⋮

The checksum is computed over the following fields:

**Source address: 32 bits**

The source address in the IPv4 header

**Destination address: 32 bits**

The destination address in the IPv4 header

**Zeroes: 8 bits**

All zeroes

**Protocol: 8 bits**

The protocol value for TCP:

6

**TCP length: 16 bits**

The length of the TCP header and data (measured in octets). For example, let's say we have IPv4 packet with Total Length of

200 bytes

and IHL value of 5, which indicates a length of

5 bits × 32 bits

=

160 bits

=

20 bytes

. We can compute the TCP length as

(Total Length) − (IPv4 Header Length)

i.e.

200 − 20

, which results in

180 bytes

.

### TCP checksum for IPv6

When TCP runs over IPv6, the method used to compute the checksum is changed:

> *Any transport or other upper-layer protocol that includes the addresses from the IP header in its checksum computation must be modified for use over IPv6, to include the 128-bit IPv6 addresses instead of 32-bit IPv4 addresses.*

A pseudo-header that mimics the IPv6 header for computation of the checksum is shown below.

TCP pseudo-header for checksum computation (IPv6)

Offset

Octet

0

1

2

3

Octet

Bit

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

0

Source address

4

32

8

64

12

96

16

128

Destination address

20

160

24

192

28

224

32

256

TCP length

36

288

Zeroes

Next header

(6)

40

320

Source port

Destination port

44

352

Sequence number

48

384

Acknowledgement number

52

416

Data offset

Reserved

Flags

Window

56

448

Checksum

Urgent pointer

60

480

(Options)

64

512

Data

68

544

⋮

⋮

The checksum is computed over the following fields:

**Source address: 128 bits**

The address in the IPv6 header.

**Destination address: 128 bits**

The final destination; if the IPv6 packet doesn't contain a Routing header, TCP uses the destination address in the IPv6 header, otherwise, at the originating node, it uses the address in the last element of the Routing header, and, at the receiving node, it uses the destination address in the IPv6 header.

**TCP length: 32 bits**

The length of the TCP header and data (measured in octets).

**Zeroes: 24 bits; `Zeroes == 0`**

All zeroes.

**Next header: 8 bits**

The protocol value for TCP:

6

.

### Checksum offload

Many TCP/IP software stack implementations provide options to use hardware assistance to automatically compute the checksum in the network adapter prior to transmission onto the network or upon reception from the network for validation. This may reduce CPU load associated with calculating the checksum, potentially increasing overall network performance.

This feature may cause packet analyzers that are unaware or uncertain about the use of checksum offload to report invalid checksums in outbound packets that have not yet reached the network adapter. This will only occur for packets that are intercepted before being transmitted by the network adapter; all packets transmitted by the network adaptor on the wire will have valid checksums. This issue can also occur when monitoring packets being transmitted between virtual machines on the same host, where a virtual device driver may omit the checksum calculation (as an optimization), knowing that the checksum will be calculated later by the VM host kernel or its physical hardware.
