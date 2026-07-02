---
title: "Network Time Protocol"
source: https://en.wikipedia.org/wiki/Network_Time_Protocol
domain: ntp-protocol
license: CC-BY-SA-4.0
tags: ntp, network time protocol, precision time protocol, clock synchronization
fetched: 2026-07-02
---

# Network Time Protocol

The **Network Time Protocol** (**NTP**) is a networking protocol for clock synchronization between computer systems over packet-switched, variable-latency data networks. In operation since before 1985, NTP is one of the oldest Internet protocols in current use. NTP was designed by David L. Mills of the University of Delaware.

NTP is intended to synchronize participating computers to within a few milliseconds of Coordinated Universal Time (UTC). It uses the intersection algorithm, a modified version of Marzullo's algorithm, to select accurate time servers and is designed to mitigate the effects of variable network latency. NTP can usually maintain time to within tens of milliseconds over the public Internet, and can achieve better than one millisecond accuracy in local area networks under ideal conditions. Asymmetric routes and network congestion can cause errors of 100 ms or more.

The protocol is usually described in terms of a client–server model, but can as easily be used in peer-to-peer relationships where both peers consider the other to be a potential time source. Implementations send and receive timestamps using the User Datagram Protocol (UDP); the service is normally on port number 123, and in some modes both sides use this port number. They can also use broadcasting or multicasting, where clients passively listen to time updates after an initial round-trip calibrating exchange. NTP supplies a warning of any impending leap second adjustment, but no information about local time zones or daylight saving time is transmitted.

The current protocol is version 4 (NTPv4), which is backward compatible with version 3.

## Clock synchronization algorithm

A typical NTP client regularly polls one or more NTP servers. The client must compute its time offset and round-trip delay. Time offset *θ* is the positive or negative (client time > server time) difference in absolute time between the two clocks. It is defined by

$\theta ={\frac {(t_{1}-t_{0})+(t_{2}-t_{3})}{2}},$ and the round-trip delay *δ* by $\delta ={(t_{3}-t_{0})-(t_{2}-t_{1})},$ where

- *t*0 is the client's timestamp of the request packet transmission,
- *t*1 is the server's timestamp of the request packet reception,
- *t*2 is the server's timestamp of the response packet transmission and
- *t*3 is the client's timestamp of the response packet reception.

To derive the expression for the offset, note that for the request packet, $t_{0}+\theta +\delta /2=t_{1}$ and for the response packet, $t_{3}+\theta -\delta /2=t_{2}$ Solving for *θ* yields the definition of the time offset.

The values for *θ* and *δ* are passed through filters and subjected to statistical analysis ("mitigation"). Outliers are discarded and an estimate of time offset is derived from the best three remaining candidates. The clock frequency is then adjusted to reduce the offset gradually ("discipline"), creating a feedback loop.

Accurate synchronization is achieved when both the incoming and outgoing routes between the client and the server have symmetrical nominal delay. If the routes do not have a common nominal delay, a systematic bias exists of half the difference between the forward and backward travel times. A number of approaches have been proposed to measure asymmetry, but among practical implementations only chrony seems to have one included.

## History

| RFC evolution for NTP |   |   |
|---|---|---|
| 1980 —–1985 —–1990 —–1995 —–2000 —–2005 —–2010 —–2015 —–2020 —– | v0, RFC 958v1, RFC 1059v2, RFC 1119v3, RFC 1305v4, RFC 5905v3, RFC 1361v3, RFC 1769v4, RFC 2030v4, RFC 4330 | ←DCNET Internet Clock Service←SNTP←SNTP merged←Ext. fields←MAC change←Port randomization |
|   |   |   |

In 1979, network time synchronization technology was used in what was possibly the first public demonstration of Internet services running over a trans-Atlantic satellite network, at the National Computer Conference in New York. The technology was later described in the 1981 Internet Engineering Note (IEN) 173 and a public protocol was developed from it that was documented in RFC 778. The technology was first deployed in a local area network as part of the Hello routing protocol and implemented in the Fuzzball router, an experimental operating system used in network prototyping, where it ran for many years.

Other related network tools were available both then and now. They include the Daytime and Time protocols for recording the time of events, as well as the ICMP Timestamp messages and IP Timestamp option (RFC 781). More complete synchronization systems, although lacking NTP's data analysis and clock disciplining algorithms, include the Unix daemon *timed*, which uses an election algorithm to appoint a server for all the clients; and the **Digital Time Synchronization Service** (DTSS), which uses a hierarchy of servers similar to the NTP stratum model.

In 1985, NTP version 0 (NTPv0) was implemented in both Fuzzball and Unix, and the NTP packet header and round-trip delay and offset calculations, which have persisted into NTPv4, were documented in RFC 958. Despite the relatively slow computers and networks available at the time, accuracy of better than 100 milliseconds was usually obtained on Atlantic spanning links, with accuracy of tens of milliseconds on Ethernet networks.

In 1988, a much more complete specification of the NTPv1 protocol, with associated algorithms, was published in RFC 1059. It drew on the experimental results and clock filter algorithm documented in RFC 956 and was the first version to describe the client–server and peer-to-peer modes. In 1991, the NTPv1 architecture, protocol and algorithms were brought to the attention of a wider engineering community with the publication of an article by David L. Mills in the *IEEE Transactions on Communications*.

In 1989, RFC 1119 was published defining NTPv2 by means of a state machine, with pseudocode to describe its operation. It introduced a management protocol and cryptographic authentication scheme which have both survived into NTPv4, along with the bulk of the algorithm. However the design of NTPv2 was criticized for lacking formal correctness by the DTSS community, and the clock selection procedure was modified to incorporate Marzullo's algorithm for NTPv3 onwards.

In 1992, RFC 1305 defined NTPv3. The RFC included an analysis of all sources of error, from the reference clock down to the final client, which enabled the calculation of a metric that helps choose the best server where several candidates appear to disagree. Broadcast mode was introduced.

In subsequent years, as new features were added and algorithm improvements were made, it became apparent that a new protocol version was required. In 2010, RFC 5905 was published containing a proposed specification for NTPv4. Following the retirement of Mills from the University of Delaware, the reference implementation is currently maintained as an open source project led by Harlan Stenn. On the IANA side, a ntp (network time *protocols*) work group is in charge of reviewing proposed drafts.

The protocol has significantly progressed since NTPv4. As of 2022, three RFC documents describing updates to the protocol have been published, not counting the numerous peripheral standards such as Network Time Security. Mills had mentioned plans for a "NTPv5" on his page, but one was never published. An unrelated draft termed "NTPv5" by M. Lichvar of chrony was initiated in 2020 and includes security, accuracy, and scaling changes.

## SNTP

| Feature | Full NTP | SNTP | Notes |
|---|---|---|---|
| Mitigation algorithms | Mandatory | Optional | SNTP may be designed to bypass these entirely. |
| Header processing | Mandatory | Optional | SNTP can use a subset; some implementations only read the *Transmit Timestamp*. |
| Redundancy | Mandatory | Optional | SNTP is intended for a single upstream server with no failover logic. |
| State tracking | Mandatory | Optional | SNTP can operate in a stateless "Remote Procedure Call" (RPC) mode. |
| Root distance and dispersion | Mandatory | Optional | SNTP often ignores these fields or uses "canned" (pre-set) values. |
| Clock discipline | Mandatory | Optional | SNTP usually just forces the clock to match the server's time (stepping). |
| NTP network protocol | Mandatory | Mandatory | SNTP uses the same on-wire protocol |

As NTP replaced the old Time Protocol, some use cases nevertheless found the full protocol too complicated. In 1992, **Simple Network Time Protocol** (**SNTP**) was defined to fill this niche. The SNTPv3 standard describes a way to use NTPv3 such that no storage of state over an extended period is needed. The topology becomes essentially the same as with the Time Protocol, as only one server is used. In 1996, SNTP was updated to SNTPv4, with some features of the then-in-development NTPv4. SNTPv4 was merged into the main NTPv4 standard in 2010.

SNTP is fully interoperable with NTP since it does not define a new protocol, as it utilizes the same packet format and port as NTP, ensuring compatibility with NTP servers. However, client/server will lack the complex algorithms required to filter network jitter, analyze clock drift, or cross-reference multiple time sources. This makes it suitable for IoT devices and basic hardware that require "good enough" time without the overhead of a full NTP application stack.

An SNTP client typically operates by querying a single server and applying the received time directly to the local clock. However, the simple algorithms provide times of reduced accuracy and thus it is inadvisable to sync time from an SNTP source. However, RFC 5905 notes that because the additional complexity of the full on-wire protocol is minimal, full implementation is encouraged even for simple clients.

## Clock strata

NTP uses a hierarchical, semi-layered system of time sources. Each level of this hierarchy is termed a *stratum* and is assigned a number starting with zero for the reference clock at the top. A server synchronized to a stratum *n* server runs at stratum *n* + 1. The number represents the distance from the reference clock and is used to prevent cyclical dependencies in the hierarchy. Stratum is not always an indication of quality or reliability; it is common to find stratum 3 time sources that are higher quality than some stratum 2 time sources. Brief descriptions of strata 0, 1, 2 and 3 are provided below.

**Stratum 0**

These are high-precision timekeeping devices such as

atomic clocks

,

GNSS

(including

GPS

) or other

radio clocks

, or

PTP

-synchronized clocks.

They generate a very accurate

pulse per second

signal that triggers an

interrupt

and timestamp on a connected computer. Stratum 0 devices are also known as

reference clocks

. NTP servers cannot advertise themselves as stratum 0; a stratum field set to 0 in an NTP message indicates an unspecified stratum.

**Stratum 1**

These are computers whose

system time

is synchronized to within a few microseconds of their attached stratum 0 devices. Stratum 1 servers may peer with other stratum 1 servers for

sanity check

and backup.

They are also referred to as primary time servers.

**Stratum 2**

These are computers that are synchronized over a network to stratum 1 servers. Often a stratum 2 computer queries several stratum 1 servers. Stratum 2 computers may also peer with other stratum 2 computers to provide more stable and robust time for all devices in the peer group.

**Stratum 3**

These are computers that are synchronized to stratum 2 servers. They employ the same algorithms for peering and data sampling as stratum 2, and can themselves act as servers for stratum 4 computers, and so on.

The upper limit for stratum is 15; stratum 16 is used to indicate that a device is unsynchronized. The NTP algorithms on each computer interact to construct a Bellman–Ford shortest-path spanning tree, to minimize the accumulated round-trip delay to the stratum 1 servers for all the clients.

In addition to stratum, the protocol is able to identify the synchronization source for each server in terms of a reference identifier (refid).

| Refid | Clock Source |
|---|---|
| GOES | Geostationary Operational Environmental Satellite (described as “Geosynchronous Orbit Environment Satellite” in RFC 5905) |
| GPS | Global Positioning System |
| GAL | Galileo Positioning System |
| PPS | Generic pulse-per-second |
| IRIG | Inter-Range Instrumentation Group |
| WWVB | LF Radio WWVB Fort Collins, Colorado 60 kHz |
| DCF/PZF | LF Radio DCF77 Mainflingen, DE 77.5 kHz |
| HBG | LF Radio HBG Prangins, HB 75 kHz (ceased operation) |
| MSF | LF Radio MSF Anthorn, UK 60 kHz |
| JJY | LF Radio JJY Fukushima, JP 40 kHz, Saga, JP 60 kHz |
| LORC | MF Radio Loran-C station, 100 kHz |
| TDF | MF Radio Allouis, FR 162 kHz |
| CHU | HF Radio CHU Ottawa, Ontario |
| WWV | HF Radio WWV Fort Collins, Colorado |
| WWVH | HF Radio WWVH Kauai, Hawaii |
| NIST | NIST telephone modem |
| ACTS | NIST telephone modem |
| USNO | USNO telephone modem |
| PTB | German PTB time standard telephone modem |
| MRS | (Informal) Multi Reference Sources |
| GOOG | (Unofficial) Google Refid used by Google NTP servers as time4.google.com |

For servers on stratum 2 and below, the refid is an encoded form of the upstream time server's IP address. For IPv4, this is simply the 32-bit address; for IPv6, it would be the first 32 bits of the MD5 hash of the source address. Refids serve to detect and prevent timing loops to the first degree.

The refid field is filled with status words in the case of kiss-o'-death (KoD) packets, which tell the client to stop sending requests so that the server can rest. Some examples are INIT (initialization), STEP (step time change), and RATE (client requesting too fast). The program output may additionally use codes not transmitted in the packet to indicate error, such as XFAC to indicate a network disconnection.

The IANA maintains a registry for refid source names and KoD codes. Informal assignments can still appear.

## Software implementations

### Reference implementation

The NTP reference implementation, along with the protocol, has been continuously developed for over 20 years. Backwards compatibility has been maintained as new features have been added. It contains several sensitive algorithms, especially to discipline the clock, that can misbehave when synchronized to servers that use different algorithms. The software has been ported to almost every computing platform, including personal computers. It runs as a daemon called ntpd under Unix or as a service under Windows. Reference clocks are supported and their offsets are filtered and analysed in the same way as remote servers, although they are usually polled more frequently. This implementation was audited in 2017, finding 14 potential security issues.

### Windows Time

All Microsoft Windows versions since Windows 2000 include the Windows Time service (W32Time), which has the ability to synchronize the computer clock to an NTP server.

W32Time was originally implemented for the purpose of the Kerberos version 5 authentication protocol, which required time to be within 5 minutes of the correct value to prevent replay attacks. The network time server in Windows 2000 Server (and Windows XP) does not implement NTP disciplined synchronization, only locally disciplined synchronization with NTP/SNTP correction.

Beginning with Windows Server 2003 and Windows Vista, the NTP provider for W32Time became compatible with a significant subset of NTPv3. Microsoft states that W32Time cannot reliably maintain time synchronization with one second accuracy. If higher accuracy is desired, Microsoft recommends using a newer version of Windows or different NTP implementation.

Beginning with Windows 10 version 1607 and Windows Server 2016, W32Time can be configured to reach time accuracy of 1 s, 50 ms or 1 ms under certain specified operating conditions.

### OpenNTPD

In 2004, Henning Brauer of OpenBSD presented OpenNTPD, an NTPv3/SNTPv4 implementation with a focus on security and encompassing a privilege separated design. Whilst it is aimed more closely at the simpler generic needs of OpenBSD users, it also includes some protocol security improvements while still being compatible with existing NTP servers. The simpler code base sacrifices accuracy, deemed unnecessary in this use case. A portable version is available in Linux package repositories.

### NTPsec

NTPsec is a fork of the reference implementation that has been systematically security-hardened. The fork point was in June 2015 and was in response to a series of compromises in 2014. The first production release shipped in October 2017. Between removal of unsafe features, removal of support for obsolete hardware, and removal of support for obsolete Unix variants, NTPsec has been able to pare away 75% of the original codebase, making the remainder easier to audit. A 2017 audit of the code showed eight security issues, including two that were not present in the original reference implementation, but NTPsec did not suffer from eight other issues that remained in the reference implementation.

### chrony

chrony is an independent NTP implementation mainly sponsored by Red Hat, who uses it as the default time program in their distributions. Being written from scratch, chrony has a simpler codebase allowing for better security and lower resource consumption. It does not however compromise on accuracy, instead syncing faster and better than the reference ntpd in many circumstances. It is versatile enough for ordinary computers, which are unstable, go into sleep mode or have intermittent connection to the Internet. It is also designed for virtual machines, a more unstable environment.

chrony has been evaluated as "trustworthy", with only a few incidents. It is able to achieve improved precision on LAN connections, using hardware timestamping on the network adapter. Support for Network Time Security (NTS) was added on version 4.0. chrony is available under GNU General Public License version 2, was created by Richard Curnow in 1997 and is currently maintained by Miroslav Lichvar.

### ntpd-rs

ntpd-rs is a security-focused implementation of the NTP protocol, founded by the Internet Security Research Group as part of their Prossimo initiative for the creation of memory safe Internet infrastructure. ntpd-rs is implemented in Rust programming language which offers memory safety guarantees in addition to the real-time computing capabilities which are required for an NTP implementation. ntpd-rs is used in security-sensitive environments such as the Let's Encrypt non-profit Certificate Authority. Support for NTS is available. ntpd-rs is part of the "Pendulum" project which also includes a Precision Time Protocol implementation "statime". Both projects are available under Apache and MIT software licenses.

### Others

- Ntimed was started by Poul-Henning Kamp of FreeBSD in 2014 and abandoned in 2015. The implementation was sponsored by the Linux Foundation.
- systemd-timesyncd is the SNTP client built into systemd. It is used by Debian since version "bookworm" and the downstream Ubuntu.
- ntpdate was started by Stenn and deprecated in 2012. The implementation was sponsored by the Network Time Foundation.

## Leap seconds

On the day of a leap second event, ntpd receives notification from either a configuration file, an attached reference clock, or a remote server. Although the NTP clock is actually halted during the event, because of the requirement that time must appear to be strictly increasing, any processes that query the system time cause it to increase by a tiny amount, preserving the order of events. If a negative leap second should ever become necessary, it would be deleted with the sequence 23:59:58, 00:00:00, skipping 23:59:59.

An alternative implementation, called leap smearing, consists in introducing the leap second incrementally during a period of 24 hours, from noon to noon in UTC time. This implementation is used by Google (both internally and on their public NTP servers), Amazon AWS, and Facebook. chrony supports leap smear in smoothtime and leapsecmode configurations, but such use is not to be mixed with a public NTP pool as leap smear is non-standard and will throw off client calculation in a mix.

## Security concerns

Because adjusting system time is generally a privileged operation, part or all of NTP code has to be run with some privileges in order to support its core functionality. Only a few other security problems have been identified in the reference implementation of the NTP codebase, but those that appeared in 2009, such as arbitrary code execution and denial-of-service attacks, were cause for significant concern. The protocol has been undergoing revision and review throughout its history. The codebase for the reference implementation has undergone security audits from several sources for several years.

A stack buffer overflow exploit was discovered and patched in 2014. Apple was concerned enough about this vulnerability that it used its auto-update capability for the first time. On systems using the reference implementation, which is running with root user's credential, this could allow unlimited access. Some other implementations, such as OpenNTPD, have smaller code base and adopted other mitigation measures like privilege separation, are not subject to this flaw.

A 2017 security audit of three NTP implementations, conducted on behalf of the Linux Foundation's Core Infrastructure Initiative, suggested that both NTP and NTPsec were more problematic than chrony from a security standpoint.

NTP servers can be susceptible to man-in-the-middle attacks unless packets are cryptographically signed for authentication. The computational overhead involved can make this impractical on busy servers, particularly during denial of service attacks. NTP message spoofing from a man-in-the-middle attack can be used to alter clocks on client computers and allow a number of attacks based on bypassing of cryptographic key expiration. Some of the services affected by fake NTP messages identified are TLS, DNSSEC, various caching schemes (such as DNS cache), Border Gateway Protocol (BGP), Bitcoin and a number of persistent login schemes.

NTP has been used in distributed denial of service attacks. A small query is sent to an NTP server with the return IP address spoofed to be the target address. Similar to the DNS amplification attack, the server responds with a much larger reply that allows an attacker to substantially increase the amount of data being sent to the target. To avoid participating in an attack, NTP server software can be upgraded or servers can be configured to ignore external queries.

### Secure extensions

NTP itself includes support for authenticating servers to clients. NTPv3 supports a symmetric key mode, which is not useful against MITM. The public key system known as "autokey" in NTPv4 adapted from IPSec offers useful authentication, but is not practical for a busy server. Autokey was also later found to suffer from several design flaws, with no correction published, save for a change in the message authentication code. Autokey should no longer be used.

**Network Time Security** (NTS) is a secure version of NTPv4 with TLS and AEAD. The main improvement over previous attempts is that a separate "key establishment" server handles the heavy asymmetric cryptography, which needs to be done only once. If the server goes down, previous users would still be able to fetch time without fear of MITM. NTS is supported by several NTP servers including Cloudflare and Netnod. It can be enabled on chrony, NTPsec, and ntpd-rs.

Microsoft also has an approach to authenticate NTPv3/SNTPv4 packets using a Windows domain identity, known as MS-SNTP. This system is implemented in the reference ntpd and chrony, using samba for the domain connection.

## NTP packet header format

NTP packet header format

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

LI

VN

Mode

Stratum

Poll

Precision

4

32

Root Delay

8

64

Root Dispersion

12

96

Reference ID

16

128

Reference Timestamp (64-bits)

20

160

24

192

Origin Timestamp (64-bits)

28

224

32

256

Receive Timestamp (64-bits)

36

288

40

320

Transmit Timestamp (64-bits)

44

352

48

384

Optional: Extension Field(s) (n * 32 bits)

52

416

Optional: Key Identifier (If a MAC is present)

56

448

Optional: Message Digest (dgst) (If a MAC is present)

60

480

64

512

68

544

**LI (Leap Indicator): 2 bits**

Warning of leap second insertion or deletion:

- 0 = no warning
- 1 = last minute has 61 seconds
- 2 = last minute has 59 seconds
- 3 = unknown (clock unsynchronized)

**VN (Version Number): 3 bits**

NTP version number, typically 4.

**Mode: 3 bits**

Association mode:

- 0 = reserved
- 1 = symmetric active
- 2 = symmetric passive
- 3 = client
- 4 = server
- 5 = broadcast
- 6 = control
- 7 = private

**Stratum: 8 bits**

Indicates the distance from the reference clock.

- 0 = invalid
- 1 = primary server
- 2–15 = secondary
- 16 = unsynchronized

**Poll: 8 bits**

Maximum interval between successive messages, in log₂(seconds). Typical range is 6 to 10.

**Precision: 8 bits**

Signed log₂(seconds) of system clock precision (e.g., –18 ≈ 1 microsecond).

**Root Delay: 32 bits**

Total round-trip delay to the reference clock, in NTP short format.

**Root Dispersion: 32 bits**

Total dispersion to the reference clock, in NTP short format.

**Reference ID: 32 bits**

Identifies the specific server or reference clock; interpretation depends on Stratum.

**Reference Timestamp: 64 bits**

Time when the system clock was last set or corrected, in NTP timestamp format.

**Origin Timestamp (org): 64 bits**

Time at the client when the request departed, in NTP timestamp format.

**Receive Timestamp (rec): 64 bits**

The local time, in timestamp format, when the latest NTP message arrived.

**Transmit Timestamp (xmt): 64 bits**

Time at the server when the response left, in NTP timestamp format.

**Extension Field: variable**

Optional field(s) for NTP extensions (see

, Section 7.5).

**Key Identifier: 32 bits**

Unsigned integer designating an MD5 key shared by the client and server.

**Message Digest (MD5): 128 bits**

MD5 hash covering the packet header and extension fields, used for authentication.

### Timestamps

The 64-bit binary fixed-point timestamps used by NTP consist of a 32-bit part for seconds and a 32-bit part for fractional second, giving a time scale that rolls over every 232 seconds (136 years) and a theoretical resolution of 2−32 seconds (233 picoseconds). NTP uses an epoch of January 1, 1900. Therefore, the first rollover occurs on February 7, 2036.

NTPv4 introduces a 128-bit date format: 64 bits for the second and 64 bits for the fractional-second. However, the 128-bit format is never transmitted as the standard states that eras "cannot be produced by NTP directly, nor is there need to do so." The most-significant 32 bits of this format is the *Era Number* which would resolve rollover ambiguity in most cases. According to Mills, "The 64-bit value for the fraction is enough to resolve the amount of time it takes a photon to pass an electron at the speed of light. The 64-bit second value is enough to provide unambiguous time representation until the universe goes dim."

## NTP and Timezone configuration via DHCP

DHCPv4 allows clients to automatically obtain time sources as part of initial network configuration. It is commonly used in managed networks to ensure dynamic time synchronisation without manual configuration.

### NTP server discovery

RFC 2132 defines a dedicated DHCPv4 option for distributing NTP server addresses to clients.

The *Network Time Protocol Servers* option carries a list of IPv4 addresses identifying NTP servers available to the client. Servers should be listed in order of preference, allowing the client to select the most appropriate source.

| Code | Length | Address 1 | Address 1 |
|---|---|---|---|
| 42 | n | a1.a2.a3.a4 | b1.b2.b3.b4 |

- Option code: 42
- Minimum length: 4 octets
- Length: must be a multiple of 4
- Content: a sequence of 32-bit IPv4 addresses, each address represents one NTP server
- Examples: `42|2|192.0.2.1|192.0.2.2`

### Time zone configuration via DHCP

While the Network Time Protocol (NTP) is responsible for synchronising system clocks to Coordinated Universal Time (UTC), it does not distribute local time zone information. Time zone configuration is handled separately at the operating system level.

This is especially useful for networks where devices are moving in and out, like cellular network. Reduce the need to defined directly on device.

These options are defined in RFC 4833 and apply to both DHCP for IPv4 (DHCPv4) and IPv6 (DHCPv6).

#### DHCPv4 time zone options

The following DHCPv4 options are defined:

| Option code | Description |
|---|---|
| 100 | POSIX time zone string |
| 101 | IANA time zone database (tzdb) name |

Both options contain a variable-length string and are not null-terminated.

##### POSIX time zone string (option 100)

This option carries a time zone definition using the POSIX `TZ` environment variable format (as specified in IEEE 1003.1), except that the string must not begin with a colon (`:`).

| Code | Length | Content |
|---|---|---|
| 100 | n | (POSIX time zone string) |

Example:

```
EST5EDT4,M3.2.0/02:00,M11.1.0/02:00
```

This describes:

- Standard time: EST (UTC−5)
- Daylight saving time: EDT (UTC−4)
- DST starts: second Sunday in March at 02:00
- DST ends: first Sunday in November at 02:00

##### Time zone database name (option 101)

For this option to be useful, the client must already have a local copy of the time zone database. If the client recognizes the provided name, it should prefer this option over the POSIX string. If the name is unknown, the option must be ignored.

This option contains the name of a zone from the IANA Time Zone Database , such as:

| Code | Length | Content |
|---|---|---|
| 101 | n | (*IANA Time Zone Database* string) |

```
Europe/Oslo
```

#### DHCPv6 time zone options

RFC 4833 defines equivalent options for DHCPv6 with different option codes:

| Option code | Description |
|---|---|
| 41 | POSIX time zone string |
| 42 | Time zone database name |

The semantics and string formats are identical to those used in DHCPv4; only the binary encoding differs due to protocol differences between DHCPv4 and DHCPv6.

#### Relationship to NTP

NTP distributes only absolute time (UTC) and does not include any information about local time zones or daylight saving rules. DHCP time zone options complement NTP by allowing clients to automatically configure their local time representation after their clocks have been synchronised.

In typical deployments:

- DHCP provides IP configuration and time zone information.
- NTP synchronises the system clock to UTC.
- The operating system applies the configured time zone to present local time to users and applications.

This separation keeps NTP simple and avoids embedding region-specific political and legal time rules into the time synchronisation protocol.
