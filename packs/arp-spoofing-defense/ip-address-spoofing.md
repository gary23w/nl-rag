---
title: "IP address spoofing"
source: https://en.wikipedia.org/wiki/IP_address_spoofing
domain: arp-spoofing-defense
license: CC-BY-SA-4.0
tags: arp spoofing defense, dynamic arp inspection, address resolution, man-in-the-middle prevention
fetched: 2026-07-02
---

# IP address spoofing

In computer networking, **IP address spoofing** or **IP spoofing** is the creation of Internet Protocol (IP) packets with a false source IP address, for the purpose of impersonating another computing system.

## Background

The basic protocol for sending data over the Internet and many other computer networks is the Internet Protocol (IP). The protocol specifies that each IP packet must have a header which contains (among other things) the IP address of the sender of the packet. The source IP address is normally the address that the packet was sent from, but the sender's address in the header can be altered, so that to the recipient it appears that the packet came from another source.

The protocol requires the receiving computer to send back a response to the source IP address; therefore, spoofing is mainly used when the sender can anticipate the network response or does not care about the response.

The source IP address provides only limited information about the sender. It may provide general information on the region, city and town from which the packet was sent. It does not provide information on the identity of the sender or the computer being used.

## Applications

IP address spoofing involving the use of a trusted IP address can be used by network intruders to overcome network security measures, such as authentication based on IP addresses. This type of attack is most effective where trust relationships exist between machines. For example, it is common on some corporate networks to have internal systems trust each other, so that users can log in without a username or password, provided they are connecting from another machine on the internal network, which would require them to be already logged in. By spoofing a connection from a trusted machine, an attacker on the same network may be able to access the target machine without authentication.

IP address spoofing is most frequently used in denial-of-service attacks, where the objective is to flood the target with an overwhelming volume of traffic, and the attacker does not care about receiving responses to the attack packets. Packets with spoofed IP addresses are more difficult to filter since each spoofed packet appears to come from a different address, and they hide the true source of the attack. Denial-of-service attacks that use spoofing typically randomly choose addresses from the entire IP address space, though more sophisticated spoofing mechanisms might avoid non-routable addresses or unused portions of the IP address space. The proliferation of large botnets makes spoofing less important in denial-of-service attacks, but attackers typically have spoofing available as a tool, if they want to use it, so defenses against denial-of-service attacks that rely on the validity of the source IP address in attack packets might have trouble with spoofed packets.

In DDoS attacks, the attacker may decide to spoof the IP source address to randomly generated addresses, so the victim machine cannot distinguish between the spoofed packets and legitimate packets. The replies would then be sent to random addresses that do not end up anywhere in particular. Such packages-to-nowhere are called the backscatter, and there are network telescopes monitoring backscatter to measure the statistical intensity of DDoS attacks on the internet over time.

### Reflection and amplification attacks

IP address spoofing is a prerequisite for *reflection* attacks, in which the attacker sends requests with the victim's IP address as the spoofed source to third-party servers, which then send responses to the victim. When the response is substantially larger than the request, the technique is known as an *amplification* attack. Protocols historically abused for amplification include DNS, NTP, SSDP, and memcached.

## Legitimate uses

The use of packets with a false source IP address is not always evidence of malicious intent. For example, in performance testing of websites, hundreds or even thousands of "vusers" (virtual users) may be created, each executing a test script against the website under test, in order to simulate what will happen when the system goes "live" and a large number of users log in simultaneously.

Since each user will normally have its own IP address, commercial testing products (such as HP LoadRunner, WebLOAD, and others) can use IP spoofing, allowing each user its own "return address" as well.

IP spoofing is also used in some server-side load balancing. It lets the load balancer spray incoming traffic, but not need to be in the return path from the servers to the client. This saves a networking hop through switches and the load balancer as well as outbound message processing load on the load balancer. Output usually has more packets and bytes, so the savings are significant.

## Services vulnerable to IP spoofing

Network services that authenticate clients solely by source IP address are inherently vulnerable to spoofing. Historical examples include the Berkeley r-commands suite (rlogin, rsh, rcp), which are now largely deprecated in favour of SSH. Some remote procedure call implementations and any application relying on IP-based access control lists without cryptographic authentication remain susceptible.

## Defense against spoofing attacks

Packet filtering is one defense against IP spoofing attacks. Ingress filtering, standardized as BCP 38 (RFC 2827), is performed at the gateway to a network and blocks incoming packets whose source address is inside the network. This prevents an outside attacker from spoofing the address of an internal machine. Ideally, the gateway would also perform egress filtering on outgoing packets, which is the blocking of packets from inside the network with a source address that is not inside. This prevents an attacker within the network performing filtering from launching IP spoofing attacks against external machines. An intrusion detection system (IDS) is a common use of packet filtering, which has been used to secure the environments for sharing data over network and host-based IDS approaches.

It is also recommended to design network protocols and services so that they do not rely on the source IP address for authentication.

The CAIDA Spoofer project measures the prevalence of networks that fail to deploy source address validation by inviting volunteers to run a client that attempts to send spoofed packets from their network.

### Upper layers

Some upper layer protocols have their own defense against IP spoofing attacks. For example, Transmission Control Protocol (TCP) uses sequence numbers negotiated with the remote machine to ensure that arriving packets are part of an established connection. Since the attacker normally cannot see any reply packets, the sequence number must be guessed in order to hijack the connection. The poor implementation in many older operating systems and network devices, however, means that TCP sequence numbers can be predicted.

## Other definitions

The term ***spoofing*** is also sometimes used to refer to *header forgery*, the insertion of false or misleading information in e-mail or netnews headers. Falsified headers are used to mislead the recipient or network applications as to the origin of a message. This is a common technique of spammers and sporgers, who wish to conceal the origin of their messages to avoid being tracked.
