---
title: "OpenVPN"
source: https://en.wikipedia.org/wiki/OpenVPN
domain: cloud-vpn
license: CC-BY-SA-4.0
tags: cloud vpn, site-to-site vpn, ipsec tunnel, vpn gateway
fetched: 2026-07-02
---

# OpenVPN

**OpenVPN** is a virtual private network (VPN) system that implements techniques to create secure point-to-point or site-to-site connections in routed or bridged configurations and remote access facilities. It implements both client and server applications.

OpenVPN allows peers to authenticate each other using pre-shared secret keys, certificates or username/password. When used in a multiclient-server configuration, it allows the server to release an authentication certificate for every client, using signatures and certificate authority.

It uses the OpenSSL encryption library extensively, as well as the TLS protocol, and contains many security and control features. As it uses a custom security protocol that utilizes SSL/TLS for key exchange. It is capable of traversing network address translators (NATs) and firewalls.

OpenVPN has been ported and embedded on several systems. For example, DD-WRT has the OpenVPN server function. SoftEther VPN, a multi-protocol VPN server, also has an implementation of the OpenVPN protocol.

It was written by James Yonan and is free software, released under the terms of the GNU General Public License version 2 (GPLv2). Additionally, commercial licenses are available.

## Architecture

### Encryption

OpenVPN uses the OpenSSL library to provide encryption of both the data and control channels. It lets OpenSSL do all the encryption and authentication work, allowing OpenVPN to use all the ciphers available in the OpenSSL package. It can also use the HMAC packet authentication feature to add an additional layer of security to the connection (referred to as an "HMAC Firewall" by the creator). It can also use hardware acceleration to get better encryption performance. Support for mbed TLS is available starting from version 2.3.

### Authentication

OpenVPN has several ways to authenticate peers with each other. OpenVPN offers pre-shared keys, certificate-based, and username/password-based authentication. Preshared secret key is the easiest, and certificate-based is the most robust and feature-rich. In version 2.0, username/password authentications can be enabled, both with or without certificates. However, to make use of username/password authentications, OpenVPN depends on third-party modules.

### Networking

OpenVPN can run over User Datagram Protocol (UDP) or Transmission Control Protocol (TCP) transports, multiplexing created SSL tunnels on a single TCP/UDP port (RFC 3948 for UDP).

From 2.3.x series on, OpenVPN fully supports IPv6 as a protocol of the virtual network inside a tunnel and the OpenVPN applications can also establish connections via IPv6. It has the ability to work through most proxy servers (including HTTP) and is good at working through network address translation (NAT) and getting out through firewalls. The server configuration can "push" certain network configuration options to the clients. These include IP addresses, routing commands, and a few connection options. OpenVPN offers two types of interfaces for networking via the Universal TUN/TAP driver. It can create either a layer-3 based IP tunnel (TUN), or a layer-2 based Ethernet TAP that can carry any type of Ethernet traffic. OpenVPN can optionally use the LZO compression library to compress the data stream. Port 1194 is the official IANA assigned port number for OpenVPN. Newer versions of the program now default to that port. A feature in the 2.0 version allows for one process to manage several simultaneous tunnels, as opposed to the original "one tunnel per process" restriction on the 1.x series.

OpenVPN's use of common network protocols (TCP and UDP) makes it a desirable alternative to IPsec in situations where an ISP may block specific VPN protocols in order to force users to subscribe to a higher-priced, "business grade" service tier. For example, Comcast previously declared that their @Home product was, and had always been, designated as a residential service and did not allow the use of commercial applications. Their argument was that conducting remote work via a VPN can adversely affect the network performance of their regular residential subscribers. They offered an alternative, @Home Professional, which would cost more than the @Home product. So, anyone wishing to use a VPN would have to subscribe to a higher-priced, business-grade service tier.

When OpenVPN uses Transmission Control Protocol (TCP) transports to establish a tunnel, performance will be acceptable only as long as there is sufficient excess bandwidth on the un-tunneled network link to guarantee that the tunneled TCP timers do not expire. If this becomes untrue, performance falls off dramatically due to the TCP meltdown problem.

### Security

OpenVPN offers various internal security features. It has up to 256-bit encryption through the OpenSSL library, although some service providers may offer lower rates, effectively providing some of the fastest VPN available to consumers. OpenVPN also supports Perfect Forward Secrecy (PFS), which regenerates encryption keys at set intervals, ensuring that even if one key is compromised, previous and future data remains secure. Additionally, OpenVPN can be configured with various encryption ciphers, such as ChaCha20 and AES-256. It runs in userspace instead of requiring IP stack (therefore kernel) operation. OpenVPN has the ability to drop root privileges, use mlockall to prevent swapping sensitive data to disk, enter a chroot jail after initialization, and apply a SELinux context after initialization.

OpenVPN runs a custom security protocol based on SSL and TLS, rather than supporting IKE, IPsec, L2TP or PPTP.

OpenVPN supports the use of smart cards via PKCS#11-based cryptographic tokens.

### Extensibility

OpenVPN can be extended with third-party plug-ins or scripts, which can be called at defined entry points. The purpose of this is often to extend OpenVPN with more advanced logging, enhanced authentication with username and passwords, dynamic firewall updates, RADIUS integration and so on. The plug-ins are dynamically loadable modules, usually written in C, while the scripts interface can execute any scripts or binaries available to OpenVPN. In the OpenVPN source code there are some examples of such plug-ins, including a PAM authentication plug-in. Several third-party plug-ins also exist to authenticate against LDAP or SQL databases such as SQLite and MySQL.

### Header

This is an example for an OpenVPN control channel packet when HMAC based auth is enabled (tls-auth option in OpenVPN). Data channel packets, which carry IP traffic, have a different format.

OpenVPN header format

Offsets

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

Opcode

KeyID

Session ID

4

32

Session ID

8

64

Session ID

HMAC

12

96

HMAC

⋮

⋮

24

192

28

224

HMAC

Packet ID

32

256

Packet ID

Net Time

36

288

Net Time

Msg Array Len

Message Packet ID #

⋮

⋮

## Platforms

It is available on Solaris, Linux, OpenBSD, FreeBSD, NetBSD, QNX, macOS and Windows XP and later. OpenVPN is available for mobile operating systems including Maemo, Windows Mobile 6.5 and below, iOS 3GS+ devices, jailbroken iOS 3.1.2+ devices, Android 4.0+ devices, and Android devices that have had the Cyanogenmod aftermarket firmware flashed or have the correct kernel module installed. It is not compatible with some mobile phone OSes, including Palm OS. It is not a "web-based" VPN shown as a web page such as Citrix or Terminal Services Web access; the program is installed independently and configured by editing text files manually, rather than through a GUI-based wizard. OpenVPN is not compatible with VPN clients that use the IPsec over L2TP or PPTP protocols. The entire package consists of one binary for both client and server connections, an optional configuration file, and one or more key files depending on the authentication method used.

### Firmware implementations

OpenVPN has been integrated into several router firmware packages allowing users to run OpenVPN in client or server mode from their network routers. A router running OpenVPN in client mode, for example, allows any device on a network to access a VPN without needing the capability to install OpenVPN.

Notable firmware packages with OpenVPN integration include:

| Firmware package | Cost | Developer | References |
|---|---|---|---|
| DD-WRT | Free | NewMedia-NET GmbH |   |
| Gargoyle | Free | Eric Bishop |   |
| IPFire | Free | IPFire Project |   |
| OpenWrt | Free | Community driven development |   |
| OPNsense | Free | Deciso BV |   |
| pfSense | Free | Rubicon Communications, LLC (Netgate) |   |
| Tomato | Free | Keith Moyer |   |

OpenVPN has also been implemented in some manufacturer router firmware.

### Software implementations

OpenVPN has been integrated into SoftEther VPN, an open-source multi-protocol VPN server, to allow users to connect to the VPN server from existing OpenVPN clients.

OpenVPN is also integrated into Vyos, an open-source routing operating system forked from the Vyatta software router.

## Licensing

OpenVPN is available in two versions:

- OpenVPN Community Edition, which is a free and open-source version
- OpenVPN Access Server (OpenVPN-AS) is based on the Community Edition, but provides additional paid and proprietary features like LDAP integration, SMB server, Web UI management and provides a set of installation and configuration tools that are reported to simplify the rapid deployment of a VPN remote-access solution. The Access Server edition relies heavily on iptables for load balancing and it has never been available on Windows for this reason. This version is also able to dynamically create client ("OpenVPN Connect") installers, which include a client profile for connecting to a particular Access Server instance. However, the user does not need to have an Access Server client in order to connect to the Access Server instance; the client from the OpenVPN Community Edition can be used.

## Detectability

OpenVPN connections can be easily detected using deep packet inspection, based on known header data of the transmitted packets, regardless of the protocol or port used. While deep packet inspection does not allow determining the contents of the encrypted tunnel, it can be used to block the connection, identify communication participants, and log related data. This is particularly important when the use of VPN connections is prohibited in certain environments, for example, in countries where encrypted connections are banned, or under civil legislation when circumventing network blocks in corporate networks.
