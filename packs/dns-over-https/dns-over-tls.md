---
title: "DNS over TLS"
source: https://en.wikipedia.org/wiki/DNS_over_TLS
domain: dns-over-https
license: CC-BY-SA-4.0
tags: dns over https, encrypted dns resolution, doh protocol, private dns query
fetched: 2026-07-02
---

# DNS over TLS

**DNS over TLS** (**DoT**) is a network security protocol for encrypting and wrapping Domain Name System (DNS) queries and answers via the Transport Layer Security (TLS) protocol. The goal of the method is to increase user privacy and security by preventing eavesdropping and manipulation of DNS data via man-in-the-middle attacks. The well-known port number for DoT is 853.

While DNS over TLS is applicable to any DNS transaction, it was first standardized for use between stub or forwarding resolvers and recursive resolvers, in RFC 7858 in May of 2016. Subsequent IETF efforts specify the use of DoT between recursive and authoritative servers ("Authoritative DNS over TLS" or "ADoT") and a related implementation between authoritative servers (Zone Transfer-over-TLS or "xfr-over-TLS").

## Server software

BIND supports DoT connections as of version 9.17. Earlier versions offered DoT capability by proxying through stunnel. Unbound has supported DNS over TLS since 22 January 2023. Unwind has supported DoT since 29 January 2023. With Android Pie's support for DNS over TLS, some ad blockers now support using the encrypted protocol as a relatively easy way to access their services versus any of the various work-around methods typically used such as VPNs and proxy servers.

## Client software

Android clients running Android Pie or newer support DNS over TLS and will use it by default if the network infrastructure, for example the ISP, supports it.

In April 2018, Google announced that Android Pie will include support for DNS over TLS, allowing users to set a DNS server phone-wide on both Wi-Fi and mobile connections, an option that was historically only possible on rooted devices or by using VPNService API. DNSDist, from PowerDNS, also announced support for DNS over TLS in version 1.3.0.

Linux and Windows users can use DNS over TLS as a client through the NLnet Labs stubby daemon or Knot Resolver. Alternatively they may install getdns-utils to use DoT directly with the getdns_query tool. The unbound DNS resolver by NLnet Labs also supports DNS over TLS.

Apple's iOS 14 introduced OS-level support for DNS over TLS (and DNS over HTTPS). iOS does not allow manual configuration of DoT servers, and requires the use of a third-party application to make configuration changes.

systemd-resolved is a Linux-only implementation that can be configured to use DNS over TLS, by editing `/etc/systemd/resolved.conf` and enabling the setting `DNSOverTLS`. Most major Linux distributions have systemd installed by default.

## Public resolvers

DNS over TLS was first implemented in a public recursive resolver by Quad9 in 2017. Other recursive resolver operators such as Google and Cloudflare followed suit in subsequent years, and now it is a broadly-supported feature generally available in most large recursive resolvers.

## Criticisms and implementation considerations

DoT can impede analysis and monitoring of DNS traffic for cybersecurity purposes. DoT has been used to bypass parental controls which operate at the (unencrypted) standard DNS level; However, there are DNS providers that offer filtering and parental controls along with support for both DoT and DoH. In that scenario, DNS queries are checked against block lists once they are received by the provider rather than prior to leaving the user's router.

As with any communication, encryption of DNS requests by itself does not protect privacy. It protects against third-party observers, but does not guarantee what the endpoints do with the (then decrypted) data.

DoT clients do not necessarily directly query any authoritative name servers. The client may rely on the DoT server using traditional (port 53 or 853) queries to finally reach authoritative servers. Thus, DoT does not qualify as an end-to-end encrypted protocol, only hop-to-hop encrypted and only if DNS over TLS is used consistently.

## Alternatives

DNS over HTTPS (DoH) is a similar protocol standard for encrypting DNS queries, differing only in the methods used for encryption and delivery from DoT. On the basis of privacy and security, whether or not a superior protocol exists among the two is a matter of controversial debate, while others argue the merits of either depend on the specific use case.

DNSCrypt is another network protocol that authenticates and encrypts DNS traffic, although it was never proposed to the Internet Engineering Task Force (IETF) with a Request for Comments (RFC).
