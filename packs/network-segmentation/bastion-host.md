---
title: "Bastion host"
source: https://en.wikipedia.org/wiki/Bastion_host
domain: network-segmentation
license: CC-BY-SA-4.0
tags: network segmentation, network microsegmentation, demilitarized zone network, air gap network, network access control
fetched: 2026-07-02
---

# Bastion host

A **bastion host** is a special-purpose computer on a network specifically designed and configured to withstand attacks, so named by analogy to the bastion, a military fortification. The computer generally hosts a single application or process, for example, a proxy server or load balancer, and all other services are removed or limited to reduce the threat to the computer. It is hardened in this manner primarily due to its location and purpose, which is either on the outside of a firewall or inside of a demilitarized zone (DMZ) and usually involves access from untrusted networks or computers. These computers are also equipped with special networking interfaces to withstand high-bandwidth attacks through the internet.

## Definitions

The term is generally attributed to a 1990 article discussing firewalls by Marcus J. Ranum, who defined a bastion host as "a system identified by the firewall administrator as a critical strong point in the network security. Generally, bastion hosts will have some degree of extra attention paid to their security, may undergo regular audits, and may have modified software".

It has also been described as "any computer that is fully exposed to attack by being on the public side of the DMZ, unprotected by a firewall or filtering router. Firewalls and routers, anything that provides perimeter access control security can be considered bastion hosts. Other types of bastion hosts can include web, mail, DNS, and FTP servers. Due to their exposure, a great deal of effort must be put into designing and configuring bastion hosts to minimize the chances of penetration".

## Placement

There are two common network configurations that include bastion hosts and their placement. The first requires two firewalls, with bastion hosts sitting between the first "outside world" firewall, and an inside firewall, in a DMZ. Often, smaller networks do not have multiple firewalls, so if only one firewall exists in a network, bastion hosts are commonly placed outside the firewall.

## Use cases

Though securing remote access is the main use case of a bastion server, there are a few more use cases of a bastion host such as:

- Authentication gateway
- VPN alternative
- Alternative to internal admin tools
- Alternative to file transfers
- Alternative way to share resource credentials
- Intrusion detection
- Software inventory management

## Examples

These are several examples of bastion host systems/services:

- DNS (Domain Name System) server
- Email server
- FTP (File Transfer Protocol) server
- Honeypot
- Proxy server
- VPN (virtual private network) server
- Web server
