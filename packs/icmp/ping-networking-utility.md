---
title: "Ping (networking utility)"
source: https://en.wikipedia.org/wiki/Ping_(networking_utility)
domain: icmp
license: CC-BY-SA-4.0
tags: icmp, icmpv6, internet control message protocol, traceroute
fetched: 2026-07-02
---

# Ping (networking utility)

**Ping** is a network management software utility used to test the reachability of a host on an Internet Protocol (IP) network. It is available in a wide range of operating systems.

Ping measures the round-trip time for messages sent from the originating host to a destination computer that are echoed back to the source. The name comes from active sonar terminology that sends a pulse of sound and listens for the echo to detect objects under water.

Ping operates by means of Internet Control Message Protocol (ICMP) packets. *Pinging* involves sending an **ICMP echo request** to the target host and waiting for an **ICMP echo reply**. The program reports errors, packet loss, and a statistical summary of the results, typically including the minimum, maximum, the mean round-trip times, and standard deviation of the mean.

Command-line options and terminal output vary by implementation. Options may include the size of the payload, count of tests, limits for the number of network hops (TTL) that probes traverse, interval between the requests and time to wait for a response. Many systems provide a companion utility ping6, for testing on Internet Protocol version 6 (IPv6) networks, which uses ICMPv6.

## History

The ping utility was written by Mike Muuss in December 1983 during his employment at the Ballistic Research Laboratory, now the US Army Research Laboratory. A remark by David Mills on using ICMP echo packets for IP network diagnosis and measurements prompted Muuss to create the utility to troubleshoot network problems. The author named it after the sound that sonar makes since its methodology is analogous to sonar's echolocation. The backronym *Packet Internet Groper* for ping has been used for over 30 years. Muuss says that, from his point of view, *ping* was not intended as an acronym but he has acknowledged Mills's expansion of the name. The first released version was public domain software; all subsequent versions have been licensed under the BSD license. Ping was first included in 4.3BSD. The FreeDOS version was developed by Erick Engelke and is licensed under the GPL. Tim Crawford developed the ReactOS version. It is licensed under the MIT License.

Any host must process ICMP echo requests and issue echo replies in return.

## Invocation example

The following is the output of running ping on Linux for sending five probes (1-second interval by default, configurable via -i option) to the target host *www.example.com*:

```mw
$ ping -c 5 www.example.com

PING www.example.com (93.184.216.34): 56 data bytes
64 bytes from 93.184.216.34: icmp_seq=0 ttl=56 time=11.632 ms
64 bytes from 93.184.216.34: icmp_seq=1 ttl=56 time=11.726 ms
64 bytes from 93.184.216.34: icmp_seq=2 ttl=56 time=10.683 ms
64 bytes from 93.184.216.34: icmp_seq=3 ttl=56 time=9.674 ms
64 bytes from 93.184.216.34: icmp_seq=4 ttl=56 time=11.127 ms

--- www.example.com ping statistics ---
5 packets transmitted, 5 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 9.674/10.968/11.726/0.748 ms
```

The output lists each probe message and the results obtained. Finally, it lists the statistics of the entire test. In this example, the shortest round-trip time was 9.674 ms, the average was 10.968 ms, and the maximum value was 11.726 ms. The measurement had a standard deviation of 0.748 ms.

## Error indications

In cases of no response from the target host, most implementations display either nothing or periodically print notifications about timing out. Possible ping results indicating a problem include the following:

- H, !N or !P – host, network or protocol unreachable
- S – source route failed
- F – fragmentation needed
- U or !W – destination network/host unknown
- I – source host is isolated
- A – communication with destination network administratively prohibited
- Z – communication with destination host administratively prohibited
- Q – for this ToS the destination network is unreachable
- T – for this ToS the destination host is unreachable
- X – communication administratively prohibited
- V – host precedence violation
- C – precedence cutoff in effect

In case of error, the target host or an intermediate router sends back an ICMP error message, for example *host unreachable* or *TTL exceeded in transit*. In addition, these messages include the first eight bytes of the original message (in this case, the header of the ICMP echo request, including the quench value), so the ping utility can match responses to originating queries.

## Message format

### ICMP packet transported with IPv4

An ICMP packet transported with IPv4 looks like this.

IPv4 datagram

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

Version

(4)

IHL

(5)

DSCP

(0)

ECN

(0)

Total length

4

32

Identification

Flags

Fragment offset

8

64

Time to live

Protocol

(1)

Header checksum

12

96

Source address

16

128

Destination address

ICMP

Echo Request

packet

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

20

160

Type

(8)

Code

(0)

Checksum

24

192

Identifier

Sequence number

28

224

(Payload)

32

256

⋮

⋮

**Type: 8 bits**

Set to 8 to indicate 'Echo Request'.

**Checksum: 16 bits**

Checksum is the 16-bit

ones' complement

of the ones' complement sum of the ICMP packet, starting with the

Type

field,

including the

Payload

. The

IP header

is not included.

**Identifier: 16 bits**

Can be used by the client to match the reply with the request that caused the reply.

**Sequence number: 16 bits**

Can be used by the client to match the reply with the request that caused the reply.

**Payload: variable length**

Optional. Payload for the different kind of answers; can be an arbitrary length, left to implementation detail.

Most Linux systems use a unique *Identifier* for every ping process, and *Sequence number* is an increasing number within that process. Windows uses a fixed *Identifier*, which varies between Windows versions, and a *Sequence number* that is only reset at boot time.

The *Echo Reply* is returned as:

ICMP

Echo Reply

packet

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

20

160

Type

(0)

Code

(0)

Checksum

24

192

Identifier

Sequence number

28

224

(Payload)

32

256

⋮

⋮

**Type: 8 bits**

Set to 0 to indicate 'Echo Reply'.

**Identifier: 16 bits**

Copied from the

Echo Request

and returned.

**Sequence number: 16 bits**

Copied from the

Echo Request

and returned.

**Payload: variable length**

Optional. Payload is copied from the

Echo Request

and returned.

### ICMPv6 packet transported with IPv6

An ICMP packet transported with IPv6 looks like this.

IPv6 datagram

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

Version

(6)

Traffic class

Flow label

4

32

Payload length

Next header

(58)

Hop limit

8

64

Source address

12

96

16

128

20

160

24

192

Destination address

28

224

32

256

36

288

ICMPv6

Echo Request

packet

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

40

320

Type

(128)

Code

(0)

Checksum

44

352

Identifier

Sequence number

48

384

(Payload)

52

416

⋮

⋮

**Type: 8 bits**

Set to 128 to indicate 'Echo Request'.

**Identifier: 16 bits**

Can be used by the client to match the reply with the request that caused the reply.

**Sequence number: 16 bits**

Can be used by the client to match the reply with the request that caused the reply.

**Checksum: 16 bits**

The checksum is calculated from the ICMP message (starting with the

Type

field), prepended with an IPv6

pseudo-header

.

**Payload: variable length**

Optional. Payload for the different kind of answers; can be an arbitrary length, left to implementation detail.

Most Linux systems use a unique *Identifier* for every ping process, and *Sequence number* is an increasing number within that process. Windows uses a fixed *Identifier*, which varies between Windows versions, and a *Sequence number* that is only reset at boot time.

The *Echo Reply* is returned as:

ICMPv6

Echo Reply

packet

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

40

320

Type

(129)

Code

(0)

Checksum

44

352

Identifier

Sequence number

48

384

(Payload)

52

416

⋮

⋮

**Type: 8 bits**

Set to 129 to indicate 'Echo Reply'.

**Identifier: 16 bits**

Copied from the

Echo Request

and returned.

**Sequence number: 16 bits**

Copied from the

Echo Request

and returned.

**Payload: variable length**

Optional. Payload is copied from the

Echo Request

and returned.

### Payload

The payload of the packet is generally filled with ASCII characters, as the output of the tcpdump utility shows in the last 32 bytes of the following example (after the eight-byte ICMP header starting with 0x0800):

```mw
16:24:47.966461 IP (tos 0x0, ttl 128, id 15103, offset 0, flags [none],
proto: ICMP (1), length: 60) 192.168.146.22 > 192.168.144.5: ICMP echo request,
id 1, seq 38, length 40
       0x0000:  4500 003c 3aff 0000 8001 5c55 c0a8 9216  E..<:.....\U....
       0x0010:  c0a8 9005 0800 4d35 0001 0026 6162 6364  ......M5...&abcd
       0x0020:  6566 6768 696a 6b6c 6d6e 6f70 7172 7374  efghijklmnopqrst
       0x0030:  7576 7761 6263 6465 6667 6869            uvwabcdefghi
```

The payload may include a timestamp indicating the time of transmission and a sequence number, which are not found in this example. This allows ping to compute the round-trip time in a stateless manner without needing to record the time of transmission of each packet.

The payload may also include a *magic packet* for the Wake-on-LAN protocol, but the minimum payload, in that case, is longer than shown. The *Echo Request* typically does not receive any reply if the host was sleeping in hibernation state, but the host still wakes up from sleep state if its interface is configured to accept wakeup requests. If the host is already active and configured to allow replies to incoming ICMP *Echo Request* packets, the returned reply should include the same payload. This may be used to detect that the remote host was effectively woken up by repeating a new request after some delay to allow the host to resume its network services. If the host was just sleeping in a low-power active state, a single request wakes up that host just enough to allow its *Echo Reply* service to reply instantly if that service was enabled. The host does not need to wake up all devices completely and may return to low-power mode after a short delay. Such a configuration may be used to avoid a host entering hibernation state, with much longer wake-up delay, after some time passed in low power active mode.

A packet including IP and ICMP headers must not be greater than the maximum transmission unit of the network, or risk being fragmented.

## Security loopholes

To conduct a denial-of-service attack, an attacker may send ping requests as fast as possible, possibly overwhelming the victim with ICMP echo requests. This technique is called a ping flood.

Ping requests to multiple addresses, ping sweeps, may be used to obtain a list of all hosts on a network.
