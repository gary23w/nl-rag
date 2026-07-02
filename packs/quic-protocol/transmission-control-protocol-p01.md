---
title: "Transmission Control Protocol (part 1/2)"
source: https://en.wikipedia.org/wiki/Transmission_Control_Protocol
domain: quic-protocol
license: CC-BY-SA-4.0
tags: quic protocol, quic transport, udp transport
fetched: 2026-07-02
part: 1/2
---

# Transmission Control Protocol

The **Transmission Control Protocol** (**TCP**) is one of the main protocols of the Internet protocol suite, providing reliable, ordered, and error-checked delivery of a stream of octets (bytes) between applications running on hosts communicating via an IP network. It originated in the initial network implementation in which it complemented the Internet Protocol (IP). Therefore, the entire suite is commonly referred to as TCP/IP.

Major internet applications such as the World Wide Web, email, remote administration, file transfer and streaming media rely on TCP, which is part of the transport layer of the TCP/IP suite. SSL/TLS often runs on top of TCP. Today, TCP remains a core protocol for most Internet communication, ensuring reliable data transfer across diverse networks.

TCP is connection-oriented, meaning that sender and receiver first need to establish a connection based on agreed parameters; they do this through a three-way handshake procedure. The server must be listening (passive open) for connection requests from clients before a connection is established. The three-way handshake (active open), retransmission, and error detection add to reliability but lengthen latency. Applications that do not require reliable data stream service may use the User Datagram Protocol (UDP) instead, which provides a connectionless datagram service that prioritizes time over reliability. TCP employs network congestion avoidance. However, there are vulnerabilities in TCP, including denial of service, connection hijacking, TCP veto, and reset attack.


## Historical origin

In May 1974, Vint Cerf and Bob Kahn described an internetworking protocol for sharing resources using packet switching among network nodes. The authors had been working with Gérard Le Lann to incorporate concepts from the French CYCLADES project into the new network. The specification of the resulting protocol, RFC 675 (*Specification of Internet Transmission Control Program*), was written by Vint Cerf, Yogen Dalal, and Carl Sunshine, and published in December 1974. It contains the first attested use of the term *internet*, as a shorthand for *internetwork*.

The Transmission Control Program incorporated both connection-oriented links and datagram services between hosts. In version 4, the monolithic Transmission Control Program was divided into a modular architecture consisting of the *Transmission Control Protocol* and the *Internet Protocol*. This resulted in a networking model that became known informally as *TCP/IP*, although formally it was variously referred to as the *DoD internet architecture model* (*DoD model* for short) or *DARPA model*. Later, it became part of, and synonymous with, the *Internet Protocol Suite*. TCP continues to evolve, with incremental updates and best practices formalized in RFCs such as RFC 9293 (2022).

The following Internet Experiment Note (IEN) documents describe the evolution of TCP into the modern version:

- IEN #5 *Specification of Internet Transmission Control Program TCP Version 2* (March 1977)
- IEN #21 *Specification of Internetwork Transmission Control Program TCP Version 3* (January 1978)
- IEN #27 *A Proposal for TCP Version 3.1 Header Format* (February 1978)
- IEN #40 *Transmission Control Protocol Draft Version 4* (June 1978)
- IEN #44 *Latest Header Formats* (June 1978)
- IEN #55 *Specification of Internetwork Transmission Control Protocol Version 4* (September 1978)
- IEN #81 *Transmission Control Protocol Version 4* (February 1979)
- IEN #112 *Transmission Control Protocol* (August 1979)
- IEN #124 *DOD STANDARD TRANSMISSION CONTROL PROTOCOL* (December 1979)

TCP was standardized in January 1980 as RFC 761.

In 2004, Vint Cerf and Bob Kahn received the Turing Award for their foundational work on TCP/IP.


## Network function

The Transmission Control Protocol provides a communication service at an intermediate level between an application program and the Internet Protocol. It provides host-to-host connectivity at the transport layer of the Internet model. An application does not need to know the particular mechanisms for sending data via a link to another host, such as the required IP fragmentation to accommodate the maximum transmission unit of the transmission medium. At the transport layer, TCP handles all handshaking and transmission details and presents an abstraction of the network connection to the application typically through a network socket interface.

At the lower levels of the protocol stack, due to network congestion, traffic load balancing, or unpredictable network behavior, IP packets may be lost, duplicated, or delivered out of order. TCP detects these problems, requests re-transmission of lost data, rearranges out-of-order data and even helps minimize network congestion to reduce the occurrence of the other problems. If the data still remains undelivered, the source is notified of this failure. Once the TCP receiver has reassembled the sequence of octets originally transmitted, it passes them to the receiving application. Thus, TCP abstracts the application's communication from the underlying networking details.

TCP is optimized for accurate delivery rather than timely delivery and can incur relatively long delays (on the order of seconds) while waiting for out-of-order messages or re-transmissions of lost messages. Therefore, it is not particularly suitable for real-time applications such as voice over IP. For such applications, protocols like the Real-time Transport Protocol (RTP) operating over the User Datagram Protocol (UDP) are usually recommended instead.

TCP is a reliable byte stream delivery service that guarantees that all bytes received will be identical and in the same order as those sent. Since packet transfer by many networks is not reliable, TCP achieves this using a technique known as *positive acknowledgment with re-transmission*. This requires the receiver to respond with an acknowledgment message as it receives the data. The sender keeps a record of each packet it sends and maintains a timer from when the packet was sent. The sender re-transmits a packet if the timer expires before receiving the acknowledgment. The timer is needed in case a packet gets lost or corrupted.

While IP handles actual delivery of the data, TCP keeps track of *segments* – the individual units of data transmission that a message is divided into for efficient routing through the network. For example, when an HTML file is sent from a web server, the TCP software layer of that server divides the file into segments and forwards them individually to the internet layer in the network stack. The internet layer software encapsulates each TCP segment into an IP packet by adding a header that includes (among other data) the destination IP address. When the client program on the destination computer receives them, the TCP software in the transport layer re-assembles the segments and ensures they are correctly ordered and error-free as it streams the file contents to the receiving application.


## TCP segment structure

Transmission Control Protocol accepts data from a data stream, divides it into chunks, and adds a TCP header creating a TCP segment. The TCP segment is then encapsulated into an Internet Protocol (IP) datagram, and exchanged with peers.

The term *TCP packet* appears in both informal and formal usage, whereas in more precise terminology *segment* refers to the TCP protocol data unit (PDU), *datagram* to the IP PDU, and *frame* to the data link layer PDU:

> Processes transmit data by calling on the TCP and passing buffers of data as arguments. The TCP packages the data from these buffers into segments and calls on the internet module [e.g. IP] to transmit each segment to the destination TCP.

A TCP segment consists of a segment *header* and a *data* section. The segment header contains 10 mandatory fields, and an optional extension field (*Options*, octets 20 through 56 in table). The data section follows the header and is the payload data carried for the application. The length of the data section is not specified in the segment header; it can be calculated by subtracting the combined length of the segment header and IP header from the total IP datagram length specified in the IP header.

TCP header format

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

Source Port

Destination Port

4

32

Sequence Number

8

64

Acknowledgement Number (meaningful when ACK bit set)

12

96

Data Offset

Reserved

CWR

ECE

URG

ACK

PSH

RST

SYN

FIN

Window

16

128

Checksum

Urgent Pointer (meaningful when URG bit set)

20

160

(Options) If present, Data Offset will be greater than 5.

Padded with zeroes to a multiple of 32 bits, since Data Offset counts words of 4 octets.

⋮

⋮

56

448

60

480

Data

64

512

⋮

⋮

**Source Port: 16 bits**

Identifies the sending port.

**Destination Port: 16 bits**

Identifies the receiving port.

**Sequence Number: 32 bits**

Has a dual role:

- If the SYN flag is set (1), then this is the initial sequence number. The sequence number of the actual first data byte and the acknowledged number in the corresponding ACK are then this sequence number plus 1.
- If the SYN flag is unset (0), then this is the accumulated sequence number of the first data byte of this segment for the current session.

**Acknowledgment Number: 32 bits**

If the ACK flag is set then the value of this field is the next sequence number that the sender of the ACK is expecting. This acknowledges receipt of all prior bytes (if any).

The first ACK sent by each end acknowledges the other end's initial sequence number itself, but no data.

**Data Offset (DOffset): 4 bits**

Specifies the size of the TCP header in 32-bit

words

. The minimum size header is 5 words and the maximum is 15 words thus giving the minimum size of 20 bytes and maximum of 60 bytes, allowing for up to 40 bytes of options in the header. This field gets its name from the fact that it is also the offset from the start of the TCP segment to the actual data.

**Reserved (Rsrvd): 4 bits**

For future use and should be set to zero; senders should not set these and receivers should ignore them if set, in the absence of further specification and implementation.

From 2003 to 2017, the last bit (bit 103 of the header) was defined as the NS (Nonce Sum) flag by the experimental

RFC 3540

, ECN-nonce. ECN-nonce never gained widespread use and the RFC was moved to Historic status.

A RFC draft

proposes a new use for this bit. The bit is now used for negotiating the use of Accurate

ECN

.

**Flags: 8 bits**

Contains 8 1-bit flags (control bits) as follows. When using

tcpdump

, a set flag is indicated with the character in parentheses.

**CWR (W): 1 bit**

Congestion window reduced (CWR) flag is set by the sending host to indicate that it received a TCP segment with the ECE flag set and had responded in congestion control mechanism.

**ECE (E): 1 bit**

ECN-Echo has a dual role, depending on the value of the SYN flag. It indicates:

- If the SYN flag is set (1), the TCP peer is ECN capable.
- If the SYN flag is unset (0), a packet with the Congestion Experienced flag set (ECN=11) in its IP header was received during normal transmission. This serves as an indication of network congestion (or impending congestion) to the TCP sender.

**URG (U): 1 bit**

Indicates that the Urgent pointer field is significant.

**ACK (.): 1 bit**

Indicates that the Acknowledgment field is significant. All packets after the initial SYN packet sent by the client should have this flag set.

**PSH (P): 1 bit**

Push function. Asks to push the buffered data onto the wire (i.e. send) on the sender end and to the receiving application at the receiver end.

**RST (R): 1 bit**

Reset the connection

**SYN (S): 1 bit**

Synchronize sequence numbers. Only the first packet sent from each end should have this flag set. Some other flags and fields change meaning based on this flag, and some are only valid when it is set, and others when it is clear.

**FIN (F): 1 bit**

Last packet from sender

**Window: 16 bits**

The size of the

receive window

, which specifies the number of window size units

that the sender of this segment is currently willing to receive.

(See

§ Flow control

and

§ Window scaling

.)

**Checksum: 16 bits**

The 16-bit

checksum

field is used for error-checking of the TCP header, the payload and an IP pseudo-header. The pseudo-header consists of the

source IP address

, the

destination IP address

, the

protocol number

for the TCP protocol (6) and the length of the TCP headers and payload (in bytes).

**Urgent Pointer: 16 bits**

If the URG flag is set, then this 16-bit field is an offset from the sequence number indicating the last urgent data byte.

**Options (TCP Option): Variable length, up to 40 bytes (320 bits); `Options length (bytes) = (Data Offset − 5) × 4; equivalent bit formula per RFC 9293: (Data Offset − 5) × 32`**

The length of this field is determined by the

Data Offset

field. The TCP header padding is used to ensure that the TCP header ends, and data begins, on a 32-bit boundary. The padding is composed of zeros.

Options have up to three fields: Option-Kind (1 byte), Option-Length (1 byte), Option-Data (variable). The Option-Kind field indicates the type of option and is the only field that is not optional. Depending on Option-Kind value, the next two fields may be set. Option-Length indicates the total length of the option, and Option-Data contains data associated with the option, if applicable. For example, an Option-Kind byte of 1 indicates that this is a no operation option used only for padding, and does not have an Option-Length or Option-Data fields following it. An Option-Kind byte of 0 marks the end of options, and is also only one byte. An Option-Kind byte of 2 is used to indicate Maximum Segment Size option, and will be followed by an Option-Length byte specifying the length of the MSS field. Option-Length is the total length of the given options field, including Option-Kind and Option-Length fields. So while the MSS value is typically expressed in two bytes, Option-Length will be 4. As an example, an MSS option field with a value of

0x05B4

is coded as (

0x02 0x04 0x05B4

) in the TCP options section.

Some options may only be sent when SYN is set; they are indicated below as

[SYN]

. Option-Kind and standard lengths given as (Option-Kind, Option-Length).

| Option-Kind | Option-Length | Option-Data | Purpose | Notes |
|---|---|---|---|---|
| 0 | —N/a | —N/a | End of options list |   |
| 1 | —N/a | —N/a | No operation | This may be used to align option fields on 32-bit boundaries for better performance. |
| 2 | 4 | SS | Maximum segment size | See § Maximum segment size for details. `[SYN]` |
| 3 | 3 | S | Window scale | See § Window scaling for details. `[SYN]` |
| 4 | 2 | —N/a | Selective Acknowledgement permitted | See § Selective acknowledgments for details. `[SYN]` |
| 5 | N (10, 18, 26, or 34) | BBBB, EEEE, ... | Selective ACKnowledgement (SACK) | These first two bytes are followed by a list of 1–4 blocks being selectively acknowledged, specified as 32-bit begin/end pointers. |
| 8 | 10 | TTTT, EEEE | Timestamp and echo of previous timestamp | See § TCP timestamps for details. |
| 28 | 4 | —N/a | User Timeout Option | See RFC 5482. |
| 29 | N | —N/a | TCP Authentication Option (TCP-AO) | For message authentication, replacing MD5 authentication (option 19) originally designed to protect BGP sessions. See RFC 5925. |
| 30 | N | —N/a | Multipath TCP (MPTCP) | See Multipath TCP for details. |

The remaining Option-Kind values are historical, obsolete, experimental, not yet standardized, or unassigned. Option number assignments are maintained by the

Internet Assigned Numbers Authority

(IANA).

**Data: Variable**

The payload of the TCP packet


## Protocol operation

TCP protocol operations may be divided into three phases. *Connection establishment* is a multi-step handshake process that establishes a connection before entering the *data transfer* phase. After data transfer is completed, the *connection termination* closes the connection and releases all allocated resources.

A TCP connection is managed by an operating system through a resource that represents the local end-point for communications, the *Internet socket*. During the lifetime of a TCP connection, the local end-point undergoes a series of state changes:

| State | Endpoint | Description |
|---|---|---|
| LISTEN | Server | Waiting for a connection request from any remote TCP end-point. |
| SYN-SENT | Client | Waiting for a matching connection request after having sent a connection request. |
| SYN-RECEIVED | Server | Waiting for a confirming connection request acknowledgment after having both received and sent a connection request. |
| ESTABLISHED | Server and client | An open connection, data received can be delivered to the user. The normal state for the data transfer phase of the connection. |
| FIN-WAIT-1 | Server and client | Waiting for a connection termination request from the remote TCP, or an acknowledgment of the connection termination request previously sent. |
| FIN-WAIT-2 | Server and client | Waiting for a connection termination request from the remote TCP. |
| CLOSE-WAIT | Server and client | Waiting for a connection termination request from the local user. |
| CLOSING | Server and client | Waiting for a connection termination request acknowledgment from the remote TCP. |
| LAST-ACK | Server and client | Waiting for an acknowledgment of the connection termination request previously sent to the remote TCP (which includes an acknowledgment of its connection termination request). |
| TIME-WAIT | Server or client | Waiting for enough time to pass to be sure that all remaining packets on the connection have expired. |
| CLOSED | Server and client | No connection state at all. |

### Connection establishment

Before a client attempts to connect with a server, the server must first bind to and listen at a port to open it up for connections: this is called a passive open. Once the passive open is established, a client may establish a connection by initiating an active open using the three-way (or 3-step) handshake:

1. **SYN**: The active open is performed by the client sending a SYN to the server. The client sets the segment's sequence number to a random value x.
2. **SYN-ACK**: In response, the server replies with a SYN-ACK. The acknowledgment number is set to one more than the received sequence number i.e. x+1, and the sequence number that the server chooses for the packet is another random number, y.
3. **ACK**: Finally, the client sends an ACK back to the server. The sequence number is set to the received acknowledgment value i.e. x+1, and the acknowledgment number is set to one more than the received sequence number i.e. y+1.

Steps 1 and 2 establish and acknowledge the sequence number for one direction (client to server). Steps 2 and 3 establish and acknowledge the sequence number for the other direction (server to client). Following the completion of these steps, both the client and server have received acknowledgments and a full-duplex communication is established.

### Connection termination

The connection termination phase uses a four-way handshake, with each side of the connection terminating independently. When an endpoint wishes to stop its half of the connection, it transmits a FIN packet, which the other end acknowledges with an ACK. Therefore, a typical tear-down requires a pair of FIN and ACK segments from each TCP endpoint. After the side that sent the first FIN has responded with the final ACK, it waits for a timeout before finally closing the connection, during which time the local port is unavailable for new connections; this state lets the TCP client resend the final acknowledgment to the server in case the ACK is lost in transit. The time duration is implementation-dependent, but some common values are 30 seconds, 1 minute, and 2 minutes. After the timeout, the client enters the CLOSED state and the local port becomes available for new connections.

It is also possible to terminate the connection by a 3-way handshake, when host A sends a FIN and host B replies with a FIN & ACK (combining two steps into one) and host A replies with an ACK.

Some operating systems, such as Linux implement a half-duplex close sequence. If the host actively closes a connection, while still having unread incoming data available, the host sends the signal RST (losing any received data) instead of FIN. This assures that a TCP application is aware there was a data loss.

A connection can be in a half-open state, in which case one side has terminated the connection, but the other has not. The side that has terminated can no longer send any data into the connection, but the other side can. The terminating side should continue reading the data until the other side terminates as well.

### Resource usage

Most implementations allocate an entry in a table that maps a session to a running operating system process. Because TCP packets do not include a session identifier, both endpoints identify the session using the client's address and port. Whenever a packet is received, the TCP implementation must perform a lookup on this table to find the destination process. Each entry in the table is known as a Transmission Control Block or TCB. It contains information about the endpoints (IP and port), status of the connection, running data about the packets that are being exchanged and buffers for sending and receiving data.

The number of sessions in the server side is limited only by memory and can grow as new connections arrive, but the client must allocate an ephemeral port before sending the first SYN to the server. This port remains allocated during the whole conversation and effectively limits the number of outgoing connections from each of the client's IP addresses. If an application fails to properly close unrequired connections, a client can run out of resources and become unable to establish new TCP connections, even from other applications.

Both endpoints must also allocate space for unacknowledged packets and received (but unread) data.

### Data transfer

The Transmission Control Protocol differs in several key features compared to the User Datagram Protocol:

- Ordered data transfer: the destination host rearranges segments according to a sequence number
- Retransmission of lost packets: any cumulative stream not acknowledged is retransmitted
- Error-free data transfer: corrupted packets are treated as lost and are retransmitted
- Flow control: limits the rate a sender transfers data to guarantee reliable delivery. The receiver continually hints the sender on how much data can be received. When the receiving host's buffer fills, the next acknowledgment suspends the transfer and allows the data in the buffer to be processed.
- Congestion control: lost packets (presumed due to congestion) trigger a reduction in data delivery rate

#### Reliable transmission

TCP uses a *sequence number* to identify each byte of data. The sequence number identifies the order of the bytes sent from each computer so that the data can be reconstructed in order, regardless of any out-of-order delivery that may occur. The sequence number of the first byte is chosen by the transmitter for the first packet, which is flagged SYN. This number can be arbitrary, and should, in fact, be unpredictable to defend against TCP sequence prediction attacks.

Acknowledgments (ACKs) are sent with a sequence number by the receiver of data to tell the sender that data has been received to the specified byte. ACKs do not imply that the data has been delivered to the application, they merely signify that it is now the receiver's responsibility to deliver the data.

Reliability is achieved by the sender detecting lost data and retransmitting it. TCP uses two primary techniques to identify loss. Retransmission timeout (RTO) and duplicate cumulative acknowledgments (DupAcks).

When a TCP segment is retransmitted, it retains the same sequence number as the original delivery attempt. This conflation of delivery and logical data ordering means that, when acknowledgment is received after a retransmission, the sender cannot tell whether the original transmission or the retransmission is being acknowledged, the so-called *retransmission ambiguity*. TCP incurs complexity due to retransmission ambiguity.

##### Duplicate-ACK-based retransmission

If a single segment (say segment number 100) in a stream is lost, then the receiver cannot acknowledge packets above that segment number (100) because it uses cumulative ACKs. Hence the receiver acknowledges packet 99 again on the receipt of another data packet. This duplicate acknowledgement is used as a signal for packet loss. That is, if the sender receives three duplicate acknowledgments, it retransmits the last unacknowledged packet. A threshold of three is used because the network may reorder segments causing duplicate acknowledgements. This threshold has been demonstrated to avoid spurious retransmissions due to reordering. Some TCP implementations use selective acknowledgements (SACKs) to provide explicit feedback about the segments that have been received. This greatly improves TCP's ability to retransmit the right segments.

Retransmission ambiguity can cause spurious fast retransmissions and congestion avoidance if there is reordering beyond the duplicate acknowledgment threshold. In the last two decades more packet reordering has been observed over the Internet which led TCP implementations, such as the one in the Linux Kernel to adopt heuristic methods to scale the duplicate acknowledgment threshold. Recently, there have been efforts to completely phase out duplicate-ACK-based fast-retransmissions and replace them with timer based ones. (Not to be confused with the classic RTO discussed below). The time based loss detection algorithm called Recent Acknowledgment (RACK) has been adopted as the default algorithm in Linux and Windows.

##### Timeout-based retransmission

When a sender transmits a segment, it initializes a timer with a conservative estimate of the arrival time of the acknowledgment. The segment is retransmitted if the timer expires, with a new timeout threshold of twice the previous value, resulting in exponential backoff behavior. Typically, the initial timer value is smoothed RTT + max(*G*, 4 × RTT variation), where G is the clock granularity. This guards against excessive transmission traffic due to faulty or malicious actors, such as man-in-the-middle denial of service attackers.

Accurate RTT estimates are important for loss recovery, as it allows a sender to assume an unacknowledged packet to be lost after sufficient time elapses (i.e., determining the RTO time). Retransmission ambiguity can lead a sender's estimate of RTT to be imprecise. In an environment with variable RTTs, spurious timeouts can occur: if the RTT is under-estimated, then the RTO fires and triggers a needless retransmit and slow-start. After a spurious retransmission, when the acknowledgments for the original transmissions arrive, the sender may believe them to be acknowledging the retransmission and conclude, incorrectly, that segments sent between the original transmission and retransmission have been lost, causing further needless retransmissions to the extent that the link truly becomes congested; selective acknowledgement can reduce this effect. RFC 6298 specifies that implementations must not use retransmitted segments when estimating RTT. Karn's algorithm ensures that a good RTT estimate will be produced—eventually—by waiting until there is an unambiguous acknowledgment before adjusting the RTO. After spurious retransmissions, however, it may take significant time before such an unambiguous acknowledgment arrives, degrading performance in the interim. TCP timestamps also resolve the retransmission ambiguity problem in setting the RTO, though they do not necessarily improve the RTT estimate.

#### Error detection

Sequence numbers allow receivers to discard duplicate packets and properly sequence out-of-order packets. Acknowledgments allow senders to determine when to retransmit lost packets.

To assure correctness a checksum field is included; see § Checksum computation for details. The TCP checksum is a weak check by modern standards and is normally paired with a CRC integrity check at layer 2, below both TCP and IP, such as is used in PPP or the Ethernet frame. However, introduction of errors in packets between CRC-protected hops is common and the 16-bit TCP checksum catches most of these.

#### Flow control

TCP uses an end-to-end flow control protocol to avoid having the sender send data too fast for the TCP receiver to receive and process it reliably. Having a mechanism for flow control is essential in an environment where machines of diverse network speeds communicate. For example, if a PC sends data to a smartphone that is slowly processing received data, the smartphone must be able to regulate the data flow so as not to be overwhelmed.

TCP uses a sliding window flow control protocol. In each TCP segment, the receiver specifies in the *receive window* field the amount of additionally received data (in bytes) that it is willing to buffer for the connection. The sending host can send only up to that amount of data before it must wait for an acknowledgment and receive window update from the receiving host.

When a receiver advertises a window size of 0, the sender stops sending data and starts its *persist timer*. The persist timer is used to protect TCP from a deadlock situation that could arise if a subsequent window size update from the receiver is lost, and the sender cannot send more data until receiving a new window size update from the receiver. When the persist timer expires, the TCP sender attempts recovery by sending a small packet so that the receiver responds by sending another acknowledgment containing the new window size.

If a receiver is processing incoming data in small increments, it may repeatedly advertise a small receive window. This is referred to as the silly window syndrome, since it is inefficient to send only a few bytes of data in a TCP segment, given the relatively large overhead of the TCP header.

#### Congestion control

The final main aspect of TCP is congestion control. TCP uses a number of mechanisms to achieve high performance and avoid congestive collapse, a gridlock situation where network performance is severely degraded. These mechanisms control the rate of data entering the network, keeping the data flow below a rate that would trigger collapse. They also yield an approximately max-min fair allocation between flows.

Acknowledgments for data sent, or the lack of acknowledgments, are used by senders to infer network conditions between the TCP sender and receiver. Coupled with timers, TCP senders and receivers can alter the behavior of the flow of data. This is more generally referred to as congestion control or congestion avoidance.

Modern implementations of TCP contain four intertwined algorithms: slow start, congestion avoidance, fast retransmit, and fast recovery.

In addition, senders employ a *retransmission timeout* (RTO) that is based on the estimated round-trip time (RTT) between the sender and receiver, as well as the variance in this round-trip time. There are subtleties in the estimation of RTT. For example, senders must be careful when calculating RTT samples for retransmitted packets; typically they use Karn's Algorithm or TCP timestamps. These individual RTT samples are then averaged over time to create a smoothed round trip time (SRTT) using Jacobson's algorithm. This SRTT value is what is used as the round-trip time estimate.

Enhancing TCP to reliably handle loss, minimize errors, manage congestion and go fast in very high-speed environments are ongoing areas of research and standards development. As a result, there are a number of TCP congestion avoidance algorithm variations.

### Maximum segment size

The maximum segment size (MSS) is the largest amount of data, specified in bytes, that TCP is willing to receive in a single segment. For best performance, the MSS should be set small enough to avoid IP fragmentation, which can lead to packet loss and excessive retransmissions. To accomplish this, typically the MSS is announced by each side using the MSS option when the TCP connection is established. The option value is derived from the maximum transmission unit (MTU) size of the data link layer of the networks to which the sender and receiver are directly attached. TCP senders can use path MTU discovery to infer the minimum MTU along the network path between the sender and receiver, and use this to dynamically adjust the MSS to avoid IP fragmentation within the network.

MSS announcement may also be called *MSS negotiation* but, strictly speaking, the MSS is not *negotiated*. Two completely independent values of MSS are permitted for the two directions of data flow in a TCP connection, so there is no need to agree on a common MSS configuration for a bidirectional connection.

### Selective acknowledgments

Relying purely on the cumulative acknowledgment scheme employed by the original TCP can lead to inefficiencies when packets are lost. For example, suppose bytes with sequence number 1,000 to 10,999 are sent in 10 different TCP segments of equal size, and the second segment (sequence numbers 2,000 to 2,999) is lost during transmission. In a pure cumulative acknowledgment protocol, the receiver can only send a cumulative ACK value of 2,000 (the sequence number immediately following the last sequence number of the received data) and cannot say that it received bytes 3,000 to 10,999 successfully. Thus the sender may then have to resend all data starting with sequence number 2,000.

To alleviate this issue TCP employs the *selective acknowledgment (SACK)* option, defined in 1996 in RFC 2018, which allows the receiver to acknowledge discontinuous blocks of packets that were received correctly, in addition to the sequence number immediately following the last sequence number of the last contiguous byte received successively, as in the basic TCP acknowledgment. The acknowledgment can include a number of *SACK blocks*, where each SACK block is conveyed by the *Left Edge of Block* (the first sequence number of the block) and the *Right Edge of Block* (the sequence number immediately following the last sequence number of the block), with a *Block* being a contiguous range that the receiver correctly received. In the example above, the receiver would send an ACK segment with a cumulative ACK value of 2,000 and a SACK option header with sequence numbers 3,000 and 11,000. The sender would accordingly retransmit only the second segment with sequence numbers 2,000 to 2,999.

A TCP sender may interpret an out-of-order segment delivery as a lost segment. If it does so, the TCP sender will retransmit the segment previous to the out-of-order packet and slow its data delivery rate for that connection. The duplicate-SACK option, an extension to the SACK option that was defined in May 2000 in RFC 2883, solves this problem. Once the TCP receiver detects a second duplicate packet, it sends a D-ACK to indicate that no segments were lost, allowing the TCP sender to reinstate the higher transmission rate.

The SACK option is not mandatory and comes into operation only if both parties support it. This is negotiated when a connection is established. SACK uses a TCP header option (see § TCP segment structure for details). The use of SACK has become widespread—all popular TCP stacks support it. Selective acknowledgment is also used in Stream Control Transmission Protocol (SCTP).

Selective acknowledgements can be 'reneged', where the receiver unilaterally discards the selectively acknowledged data. RFC 2018 discouraged such behavior, but did not prohibit it to allow receivers the option of reneging if they, for example, ran out of buffer space. The possibility of reneging leads to implementation complexity for both senders and receivers, and also imposes memory costs on the sender.

### Window scaling

For more efficient use of high-bandwidth networks, a larger TCP window size may be used. A 16-bit TCP window size field controls the flow of data and its value is limited to 65,535 bytes. Since the size field cannot be expanded beyond this limit, a scaling factor is used. The TCP window scale option, as defined in RFC 1323, is an option used to increase the maximum window size to 1 gigabyte. Scaling up to these larger window sizes is necessary for TCP tuning.

The window scale option is used only during the TCP 3-way handshake. The window scale value represents the number of bits to left-shift the 16-bit window size field when interpreting it. The window scale value can be set from 0 (no shift) to 14 for each direction independently. Both sides must send the option in their SYN segments to enable window scaling in either direction.

Some routers and packet firewalls rewrite the window scaling factor during a transmission. This causes sending and receiving sides to assume different TCP window sizes. The result is non-stable traffic that may be very slow. The problem is visible on some sites behind a defective router.

### TCP timestamps

TCP timestamps, defined in RFC 1323 in 1992, can help TCP determine in which order packets were sent. TCP timestamps are not normally aligned to the system clock and start at some random value. Many operating systems will increment the timestamp for every elapsed millisecond; however, the RFC only states that the ticks should be proportional.

There are two timestamp fields:

- a 4-byte sender timestamp value (my timestamp)
- a 4-byte echo reply timestamp value (the most recent timestamp received from you).

TCP timestamps are used in an algorithm known as *Protection Against Wrapped Sequence* numbers, or *PAWS*. PAWS is used when the receive window crosses the sequence number wraparound boundary. In the case where a packet was potentially retransmitted, it answers the question: "Is this sequence number in the first 4 GB or the second?" And the timestamp is used to break the tie.

Also, the Eifel detection algorithm uses TCP timestamps to determine if retransmissions are occurring because packets are lost or simply out of order.

TCP timestamps are enabled by default in Linux, and disabled by default in Windows Server 2008, 2012 and 2016.

Recent Statistics show that the level of TCP timestamp adoption has stagnated, at ~40%, owing to Windows Server dropping support since Windows Server 2008.

### Out-of-band data

It is possible to interrupt or abort the queued stream instead of waiting for the stream to finish. This is done by specifying the data as *urgent*. This marks the transmission as out-of-band data (OOB) and tells the receiving program to process it immediately. When finished, TCP informs the application and resumes the stream queue. An example is when TCP is used for a remote login session where the user can send a keyboard sequence that interrupts or aborts the remotely running program without waiting for the program to finish its current transfer.

The *urgent* pointer only alters the processing on the remote host and doesn't expedite any processing on the network itself. The capability is implemented differently or poorly on different systems or may not be supported. Where it is available, it is prudent to assume only single bytes of OOB data will be reliably handled. Since the feature is not frequently used, it is not well tested on some platforms and has been associated with vulnerabilities, WinNuke for instance.

### Forcing data delivery

Normally, TCP waits for 200 ms for a full packet of data to send (Nagle's Algorithm tries to group small messages into a single packet). This wait creates small, but potentially serious delays if repeated constantly during a file transfer. For example, a typical send block would be 4 KB, a typical MSS is 1460, so 2 packets go out on a 10 Mbit/s Ethernet taking ~1.2 ms each followed by a third carrying the remaining 1176 after a 197 ms pause because TCP is waiting for a full buffer. In the case of telnet, each user keystroke is echoed back by the server before the user can see it on the screen. This delay would become very annoying.

Setting the socket option `TCP_NODELAY` overrides the default 200 ms send delay. Application programs use this socket option to force output to be sent after writing a character or line of characters.

The RFC 793 defines the `PSH` push bit as "a message to the receiving TCP stack to send this data immediately up to the receiving application". There is no way to indicate or control it in user space using Berkeley sockets; it is controlled by the protocol stack only.


## Vulnerabilities

TCP may be attacked in a variety of ways. The results of a thorough security assessment of TCP, along with possible mitigations for the identified issues, were published in 2009, and was pursued within the IETF through 2012. Notable vulnerabilities include denial of service, connection hijacking, TCP veto and TCP reset attack.

### Denial of service

By using a spoofed IP address and repeatedly sending purposely assembled SYN packets, followed by many ACK packets, attackers can cause the server to consume large amounts of resources keeping track of the bogus connections. This is known as a SYN flood attack. Proposed solutions to this problem include SYN cookies and cryptographic puzzles, though SYN cookies come with their own set of vulnerabilities. Sockstress is a similar attack, that might be mitigated with system resource management. An advanced DoS attack involving the exploitation of the TCP *persist timer* was analyzed in Phrack No. 66. PUSH and ACK floods are other variants.

### Connection hijacking

An attacker who is able to eavesdrop on a TCP session and redirect packets can hijack a TCP connection. To do so, the attacker learns the sequence number from the ongoing communication and forges a false segment that looks like the next segment in the stream. A simple hijack can result in one packet being erroneously accepted at one end. When the receiving host acknowledges the false segment, synchronization is lost. Hijacking may be combined with ARP spoofing or other routing attacks that allow an attacker to take permanent control of the TCP connection.

Impersonating a different IP address was not difficult prior to RFC 1948 when the initial *sequence number* was easily guessable. The earlier implementations allowed an attacker to blindly send a sequence of packets that the receiver would believe came from a different IP address, without the need to intercept communication through ARP or routing attacks: it is enough to ensure that the legitimate host of the impersonated IP address is down, or bring it to that condition using denial-of-service attacks. This is why the initial sequence number is now chosen at random.

### TCP veto

An attacker who can eavesdrop and predict the size of the next packet to be sent can cause the receiver to accept a malicious payload without disrupting the existing connection. The attacker injects a malicious packet with the sequence number and a payload size of the next expected packet. When the legitimate packet is ultimately received, it is found to have the same sequence number and length as a packet already received and is silently dropped as a normal duplicate packet—the legitimate packet is *vetoed* by the malicious packet. Unlike in connection hijacking, the connection is never desynchronized and communication continues as normal after the malicious payload is accepted. TCP veto gives the attacker less control over the communication but makes the attack particularly resistant to detection. The only evidence to the receiver that something is amiss is a single duplicate packet, a normal occurrence in an IP network. The sender of the vetoed packet never sees any evidence of an attack.


## TCP ports

A TCP connection is identified by a four-tuple of the source address, source port, destination address, and destination port. Port numbers are used to identify different services, and to allow multiple connections between hosts. TCP uses 16-bit port numbers, providing 65,536 possible values for each of the source and destination ports. The dependency of connection identity on addresses means that TCP connections are bound to a single network path; TCP cannot use other routes that multihomed hosts have available, and connections break if an endpoint's address changes.

Port numbers are categorized into three basic categories: well-known, registered, and dynamic or private. The well-known ports are assigned by the Internet Assigned Numbers Authority (IANA) and are typically used by system-level processes. Well-known applications running as servers and passively listening for connections typically use these ports. Some examples include: FTP (20 and 21), SSH (22), TELNET (23), SMTP (25), HTTP over SSL/TLS (443), and HTTP (80). Registered ports (1024–49151) may be assigned to specific services by third-party developers, but some operating systems also allocate ephemeral client ports from this range. Dynamic or private ports (49152–65535) are not associated with any registered services and are commonly used exclusively as ephemeral ports for temporary client connections.

Network Address Translation (NAT), typically uses dynamic port numbers, on the public-facing side, to disambiguate the flow of traffic that is passing between a public network and a private subnetwork, thereby allowing many IP addresses (and their ports) on the subnet to be serviced by a single public-facing address.
