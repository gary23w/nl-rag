---
title: "DNS over HTTPS"
source: https://en.wikipedia.org/wiki/DNS_over_HTTPS
domain: dns-filtering
license: CC-BY-SA-4.0
tags: dns filtering, dns sinkhole, content filtering, protective dns
fetched: 2026-07-02
---

# DNS over HTTPS

**DNS over HTTPS** (**DoH**) is a protocol for performing remote Domain Name System (DNS) resolution via the HTTPS protocol. A goal of the method is to increase user privacy and security by preventing eavesdropping and manipulation of DNS data by man-in-the-middle attacks by using the HTTPS protocol to encrypt the data between the DoH client and the DoH-based DNS resolver. By March 2018, Google and the Mozilla Foundation had started testing versions of DNS over HTTPS. In February 2020, Firefox switched to DNS over HTTPS by default for users in the United States. In May 2020, Chrome switched to DNS over HTTPS by default.

An alternative to DoH is the DNS over TLS (DoT) protocol, a similar standard for encrypting DNS queries, differing only in the methods used for encryption and delivery. Based on privacy and security, whether either protocol is superior is a matter of debate, while others argue that the merits of either depend on the specific use case.

## Technical details

DoH is a proposed standard, published as RFC 8484 (October 2018) by the IETF. It uses HTTPS, and supports the *wire format* DNS response data, as returned in existing UDP responses, in an HTTPS payload with the MIME type *application/dns-message*. The underlying HTTP layer can be any version of HTTP, though HTTP/2 is the *recommended* minimum. If HTTP/2 is used, the server may also use HTTP/2 server push to send values that it anticipates the client may find useful in advance.

DoH is a work in progress. Even though the IETF has published RFC 8484 as a proposed standard and companies are experimenting with it, the IETF has yet to determine how it should best be implemented. The IETF is evaluating a number of approaches for how best to deploy DoH and has established a working group, Adaptive DNS Discovery (ADD), to do this work and develop a consensus.

Since DoH cannot be used under some circumstances, like captive portals, web browsers like Firefox can be configured to fall back to insecure DNS.

The de facto DoH URL is *https://host_name/dns-query*.

## Oblivious DNS over HTTPS

Oblivious DNS over HTTPS (ODoH) is an experimental standard, published as RFC 9230 (June 2022) by the IETF, proposing a protocol extension to ensure no single DoH server is aware of both the client's IP address and the content of their DNS queries and responses. This is an application of a security principle called decoupling or privacy partitioning. A different protocol with the same name (Oblivious DoH) was originally developed as Oblivious DNS (ODNS) by researchers at Princeton University and the University of Chicago as an extension to unencrypted DNS, before DoH itself was standardized and widely deployed. Apple and Cloudflare subsequently deployed the technology in the context of DoH, as Oblivious DoH (ODoH).

In ODoH and ODNS, all DNS requests and responses are routed via a proxy, hiding the client's address from the resolver. Requests and responses are encrypted to hide their contents from the proxy, and only the resolver can decrypt the requests, and the client the responses. Thus, the proxy knows the client address and resolver but not the request, and the resolver knows the proxy and request but not the client address, preventing the client address being linked to the query, unless both the proxy and resolver servers collude. Another protocol, Oblivious HTTP, uses similar architectural principles for HTTP requests.

## Deployment scenarios

DoH is used for recursive DNS resolution by DNS resolvers. Resolvers (*DoH clients*) must have access to a DoH server hosting a query endpoint.

Three usage scenarios are common:

- Using a DoH implementation within an application: Some browsers have a built-in DoH implementation and can thus perform queries by bypassing the operating system's DNS functionality. A drawback is that an application may not inform the user if it skips DoH querying, either by misconfiguration or lack of support for DoH.
- Installing a DoH proxy on the name server in the local network: In this scenario client systems continue to use traditional (port 53 or 853) DNS to query the name server in the local network, which will then gather the necessary replies via DoH by reaching DoH-servers in the Internet. This method is transparent to the end user.
- Installing a DoH proxy on a local system: In this scenario, operating systems are configured to query a locally running DoH proxy. In contrast to the previously mentioned method, the proxy needs to be installed on each system wishing to use DoH, which might require a lot of effort in larger environments.

## Software support

### Operating systems

#### Apple

Apple's iOS 14 and macOS 11 released in late 2020 support both DoH and DoT protocols. In iOS, the protocols can be used via configuration profiles.

#### Windows

In November 2019, Microsoft announced plans to implement support for encrypted DNS protocols in Microsoft Windows, beginning with DoH. In May 2020, Microsoft released Windows 10 Insider Preview Build 19628 that included initial support for DoH along with instructions on how to enable it via registry and command line interface. Windows 10 Insider Preview Build 20185 added a graphical user interface for specifying a DoH resolver. DoH support is not included in Windows 10 21H2.

Windows 11 has DoH support.

#### Android

Android 11 onwards supports DNS over HTTP/3 (DoH3) if a July 2022 system update is installed.

### Recursive DNS resolvers

#### BIND

BIND 9, an open source DNS resolver from Internet Systems Consortium added native support for DoH in version 9.17.10.

#### PowerDNS

DNSdist, an open source DNS proxy/load balancer from PowerDNS, added native support for DoH in version 1.4.0 in April 2019.

#### Unbound

Unbound, an open source DNS resolver created by NLnet Labs, has supported DoH since version 1.12.0, released in October 2020. It first implemented support for DNS encryption using the alternative DoT protocol much earlier, starting with version 1.4.14, released in December 2011. Unbound runs on most operating systems, including distributions of Linux, BSD, MacOS, and Windows.

### Web browsers

#### Google Chrome

DNS over HTTPS is available in Google Chrome 83 or later for Windows, Linux, and macOS, configurable via the settings page. When enabled, and the operating system is configured with a supported DNS server, Chrome will upgrade DNS queries to be encrypted. It is also possible to manually specify a preset or custom DoH server to use within the user interface.

In September 2020, Google Chrome for Android began staged rollout of DNS over HTTPS. Users can configure a custom resolver or disable DNS over HTTPS in settings.

Google Chrome has five DNS-over-HTTPS providers pre-configured, which are Google Public DNS, Cloudflare's 1.1.1.1, Quad9's 9.9.9.9, NextDNS, and CleanBrowsing.

#### Microsoft Edge

Microsoft Edge supports DNS over HTTPS, configurable via the settings page. When enabled, and the operating system is configured with a supported DNS server, Edge will upgrade DNS queries to be encrypted. It is also possible to manually specify a preset or custom DoH server to use within the user interface.

#### Mozilla Firefox

In 2018, Mozilla partnered with Cloudflare to deliver DoH for Firefox users that enable it (known as Trusted Recursive Resolver). On February 25, 2020, Firefox started enabling DNS over HTTPS for all US-based users, relying on Cloudflare's resolver by default.

#### Opera

Opera supports DoH, configurable via the browser settings page. By default, DNS queries are sent to Cloudflare servers.

#### Brave

Brave implemented DNS over HTTPS (DoH) by default for its desktop browser in version 1.4, released in April 2020, as part of its broader privacy-focused features to encrypt DNS queries and prevent third-party eavesdropping or manipulation.

### Public DNS servers

DNS over HTTPS server implementations are already available free of charge by some public DNS providers.

## Implementation considerations

Many issues with how to properly deploy DoH are still being resolved by the internet community including, but not limited to:

- Stopping third parties from analyzing DNS traffic for security purposes
- Disruption of DNS-level parental controls and content filters
- Split DNS in enterprise networks
- CDN localization

### Analysis of DNS traffic for security purposes

DoH can impede analysis and monitoring of DNS traffic for cybersecurity purposes; the 2019 DDoS worm Godlua used DoH to mask connections to its command-and-control server.

In January 2021, NSA warned enterprises against using external DoH resolvers because they prevent DNS query filtering, inspection, and audit. Instead, NSA recommends configuring enterprise-owned DoH resolvers and blocking all known external DoH resolvers.

### Disruption of content filters

DoH has been used to bypass parental controls which operate at the (unencrypted) standard DNS level; However, there are DNS providers that offer filtering and parental controls along with support for DoH by operating DoH servers.

The Internet Service Providers Association (ISPA)—a trade association representing British ISPs—and the also British body Internet Watch Foundation have criticized Mozilla, developer of the Firefox web browser, for supporting DoH, as they believe that it will undermine web blocking programs in the country, including ISP default filtering of adult content, and mandatory court-ordered filtering of copyright violations. The ISPA nominated Mozilla for its "Internet Villain" award for 2019 (alongside the EU Directive on Copyright in the Digital Single Market, and Donald Trump), "for their proposed approach to introduce DNS-over-HTTPS in such a way as to bypass UK filtering obligations and parental controls, undermining internet safety standards in the UK." Mozilla responded to the allegations by the ISPA, arguing that it would not prevent filtering, and that they were "surprised and disappointed that an industry association for ISPs decided to misrepresent an improvement to decades-old internet infrastructure". In response to the criticism, the ISPA apologized and withdrew the nomination. Mozilla subsequently stated that DoH will not be used by default in the British market until further discussion with relevant stakeholders, but stated that it "would offer real security benefits to UK citizens".

### Censorship by Chinese government

In July 2020, iYouPort, the University of Maryland, and the Great Firewall Report, reported that the Great Firewall (GFW) by the Chinese government blocks TLS connections using the encrypted SNI extension in China.
