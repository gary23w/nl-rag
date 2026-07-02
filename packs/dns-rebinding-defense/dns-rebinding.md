---
title: "DNS rebinding"
source: https://en.wikipedia.org/wiki/DNS_rebinding
domain: dns-rebinding-defense
license: CC-BY-SA-4.0
tags: dns rebinding defense, same-origin policy bypass, dns pinning mitigation, internal network exposure
fetched: 2026-07-02
---

# DNS rebinding

**DNS rebinding** is a method of manipulating resolution of domain names that is commonly used as a form of computer attack. In this attack, a malicious web page causes visitors to run a client-side script that attacks machines elsewhere on the network. In theory, the same-origin policy prevents this from happening: client-side scripts are only allowed to access content on the same host that served the script. Comparing domain names is an essential part of enforcing this policy, so DNS rebinding circumvents this protection by abusing the Domain Name System (DNS).

This attack can be used to breach a private network by causing the victim's web browser to access computers at private IP addresses and return the results to the attacker. It can also be employed to use the victim machine for spamming, distributed denial-of-service attacks, or other malicious activities.

## How DNS rebinding works

The attacker registers a domain (such as attacker.com) and delegates it to a DNS server that is under the attacker's control. The server is configured to respond with a very short time to live (TTL) record, preventing the DNS response from being cached. When the victim browses to the malicious domain, the attacker's DNS server first responds with the IP address of a server hosting the malicious client-side code. For instance, they could point the victim's browser to a website that contains malicious JavaScript or Flash scripts that are intended to execute on the victim's computer.

The malicious client-side code makes additional accesses to the original domain name (such as attacker.com). These are permitted by the same-origin policy. However, when the victim's browser runs the script it makes a new DNS request for the domain, and the attacker replies with a new IP address. For instance, they could reply with an internal IP address or the IP address of a target somewhere else on the Internet.

## Protection

Techniques attempting to prevent DNS rebinding attacks can broadly be divided in two categories:

### DNS Based

- DNS servers in the chain can filter out private IP addresses and loopback IP addresses:
  - External public DNS servers (e.g. OpenDNS) can implement DNS filtering.
  - Local system administrators can configure the organization's local nameserver(s) to block the resolution of external names into internal IP addresses. (This has the downside of allowing an attacker to map the internal address ranges in use.)
- A firewall (e.g. dnswall), in the gateway or in the local pc, can filter DNS replies that pass through it, discarding local addresses.

Note that DNS filtering conflicts with Domain Name System blocklist. RFC 5782 standardizes the use of IP addresses beginning with 127, like 127.0.0.2, for such use. Normally, mail servers perform various queries of this kind, either according to local configuration or following external directives, such as the SPF's EXISTS mechanism. It is crucial for correctness, that mail servers don't utilize DNS servers that perform the above kind of filtering.

### Web Based

- Web browsers can resist DNS rebinding:
  - Web browsers can implement DNS pinning: the IP address is locked to the value received in the first DNS response. This technique may block some legitimate uses of Dynamic DNS, and may not work against all attacks. However, it is important to fail-safe (stop rendering) if the IP address does change, because using an IP address past the TTL expiration can open the opposite vulnerability when the IP address has legitimately changed and the expired IP address may now be controlled by an attacker.
  - The NoScript extension for Firefox includes ABE, a firewall-like feature inside the browser which in its default configuration prevents attacks on the local network by preventing external webpages from accessing local IP addresses.
- Web servers can reject HTTP requests with an unrecognized Host header.
