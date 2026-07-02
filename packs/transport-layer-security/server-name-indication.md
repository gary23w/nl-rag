---
title: "Server Name Indication"
source: https://en.wikipedia.org/wiki/Server_Name_Indication
domain: transport-layer-security
license: CC-BY-SA-4.0
tags: transport layer security, https protocol, http strict transport security, perfect forward secrecy, server name indication
fetched: 2026-07-02
---

# Server Name Indication

**Server Name Indication** (**SNI**) is an extension to Transport Layer Security (TLS) where a client indicates which hostname it is attempting to connect to at the start of the handshaking process. The extension allows a server to present one of multiple possible certificates on the same IP address and port number, allowing for multiple services (including HTTPS websites) to be served by the same IP address without using a single certificate. For HTTPS, it is the conceptual equivalent to HTTP/1.1 virtual hosting. In the original specification, the hostname is not encrypted; the later Encrypted Client Hello specification rectifies this. The SNI extension was specified in 2003 in RFC 3546.

## Background of the problem

Prior to SNI, when making a TLS connection, the client had no way to specify which site it was trying to connect to. Hence, if one server hosts multiple sites on a single listener, the server has no way to know which certificate to use in the TLS protocol. In more detail, when making a TLS connection, the client requests a digital certificate from the web server. Once the server sends the certificate, the client examines it and compares the name it was trying to connect to with the name(s) included in the certificate. If a match occurs, the connection proceeds as normal. If a match is not found, the user may be warned of the discrepancy and the connection may abort as the mismatch may indicate an attempted man-in-the-middle attack. However, some applications allow the user to bypass the warning to proceed with the connection, with the user taking on the responsibility of trusting the certificate and, by extension, the connection.

However, it may be hard – or even impossible due to lack of a full list of all names in advance – to obtain a single certificate that covers all names a server will be responsible for. A server that is responsible for multiple hostnames is likely to need to present a different certificate for each name (or small group of names). It is possible to use *subjectAltName* to contain multiple domains controlled by one person in a single certificate. Such "unified communications certificates" must be reissued every time the list of domains changes.

Name-based virtual hosting allows multiple DNS hostnames to be hosted by a single server (usually a web server) on the same IP address. To achieve this, the server uses a hostname presented by the client as part of the protocol (for HTTP the name is presented in the host header). However, when using HTTPS, the TLS handshake happens before the server sees any HTTP headers. Therefore, it was not possible for the server to use the information in the HTTP host header to decide which certificate to present and as such only names covered by the same certificate could be served from the same IP address.

In practice, this meant that an HTTPS server could only serve one domain (or small group of domains) per IP address for secured and efficient browsing. Assigning a separate IP address for each site increases the cost of hosting, since requests for IP addresses must be justified to the regional Internet registry and IPv4 addresses are now exhausted. For IPv6, it increases the administrative overhead by having multiple IPs on a single machine, even though the address space is not exhausted. The result was that many websites were effectively constrained from using secure communications.

## Technical principles

SNI addresses this issue by having the client send the name of the virtual domain as part of the TLS negotiation's *ClientHello* message. This enables the server to select the correct virtual domain early and present the browser with the certificate containing the correct name. Therefore, with clients and servers that implement SNI, a server with a single IP address can serve a group of domain names for which it is impractical to get a common certificate.

SNI was added to the IETF's Internet RFCs in June 2003 through RFC 3546, *Transport Layer Security (TLS) Extensions*. The latest version of the standard is RFC 6066.

## Security implications

Server Name Indication payload is not encrypted, thus the hostname of the server the client tries to connect to is visible to a passive eavesdropper. This protocol weakness was exploited by security software for network filtering and monitoring and governments to implement censorship.

Presently, there are multiple technologies attempting to hide Server Name Indication:

### Domain fronting

Domain fronting is a technique of replacing the desired host name in SNI with another one hosted by the same server or, more frequently, network of servers known as a content delivery network. When a client uses domain fronting, it replaces the server domain in SNI (unencrypted), but leaves it in the HTTP host header (which is encrypted by TLS) so that server can serve the right content. Domain fronting violates the standard defining SNI itself, so its compatibility is limited (many services check that SNI host matches the HTTP header host and reject connections with domain-fronted SNI as invalid). While domain fronting was used in the past to avoid government censorship, its popularity dwindled because major cloud providers (Google, Amazon's AWS and CloudFront) explicitly prohibit it in their TOS and have technical restrictions against it.

### Encrypted Client Hello

**Encrypted Client Hello** (**ECH**) is a TLS 1.3 protocol extension defined in RFC 9849 in March 2026 that enables encryption of the whole Client Hello message, which is sent during the early stage of TLS 1.3 negotiation. ECH encrypts the payload with a public key that the relying party (a web browser) needs to know in advance, which means ECH is most effective with large CDNs. Transmission of the public keys and configuration information via HTTPS and SVCB DNS records is defined in RFC 9848.

The initial 2018 version of this extension was called Encrypted SNI (ESNI). In March 2020, ESNI was reworked into the ECH extension, after analysis demonstrated that encrypting only the SNI is insufficient. For example, specifications permit the Pre-Shared Key extension to contain any data to facilitate session resumption, even transmission of a cleartext copy of exactly the same server name that is encrypted by ESNI. Also, encrypting extensions one-by-one would require an encrypted variant of every extension, each with potential privacy implications, and even that exposes the set of extensions advertised. Lastly, real-world deployment of ESNI has exposed interoperability limitations. The short name was *ECHO* in March 2020 and changed to *ECH* in May 2020. In July 2023, in the IETF117 meeting, members working on ECH informed Chrome and Firefox were doing a 1% sample trial, and the team expects the final draft to be submitted to the IESG evaluation by January 2024.

In September 2023, Cloudflare started to support ECH for hosted domains.

In September 2023, Chromium version 117 (used in Google Chrome, Microsoft Edge, Samsung Internet, and Opera) enabled ECH by default, also requiring keys to be deployed in HTTPS resource records in DNS. ECH is enabled in Firefox by default since version 119 released in October 2023, and is recommended by Mozilla to be used along with DNS over HTTPS.

In April 2026, OpenSSL 4.0 included support for ECH. Since its December 2025 release, NGINX supports ECH with OpenSSL 4.0.

#### ESNI (2018–2020)

The initial 2018 version of this extension was called Encrypted SNI (ESNI) and its implementations were rolled out in an "experimental" fashion to address this risk of domain eavesdropping. In contrast to ECH, Encrypted SNI encrypted just the SNI rather than the whole Client Hello. Opt-in support for this version was incorporated into Firefox in October 2018 and required enabling DNS over HTTPS (DoH). But it was removed in January 2021 with the release of Firefox 85.

Both ESNI and ECH are compatible only with TLS 1.3 because they rely on KeyShareEntry which was first defined in TLS 1.3.

In August 2020, the Great Firewall of China started blocking ESNI traffic, while still allowing ECH traffic.

In October 2020, Russian ISP Rostelecom and its mobile operator Tele2 started blocking ESNI traffic. In September of the same year, Russian censorship ministry Roscomnadzor planned to ban a range of encryption protocols, among which were TLS 1.3 and ESNI, which hindered web site access censorship.

## Implementation

In 2004, a patch for adding TLS/SNI into OpenSSL was created by the EdelKey project. In 2006, this patch was then ported to the development branch of OpenSSL, and in 2007 it was back-ported to OpenSSL 0.9.8 (first released in 0.9.8f). First web browsers with SNI support appeared in 2006 (Mozilla Firefox 2.0, Internet Explorer 7), web servers later (Apache HTTP Server in 2009, Microsoft IIS in 2012).

For an application program to implement SNI, the TLS library it uses must implement it and the application must pass the hostname to the TLS library. Further complicating matters, the TLS library may either be included in the application program or be a component of the underlying operating system. Because of this, some browsers implement SNI when running on any operating system, while others implement it only when running on certain operating systems.

## Support

|   | SNI Support | ECH Support |   |   |   |   |
|---|---|---|---|---|---|---|
| Software | Type | Supported | Notes | Since | Supported | Notes |
| Alpine (email client) | IMAP email client | Yes | Since version 2.22 | 2019-02-18 |   |   |
| Internet Explorer | Web browser | Yes | Since version 7 on Vista (not supported on XP) | 2006 | No |   |
| Edge | Web browser | Yes | All versions |   | Yes | Since v105 behind flag |
| Mozilla Firefox | Web browser | Yes | Since version 2.0 | 2006 | Yes | Introduced in v85 behind flag. Enabled by default in v118 when DoH is enabled. |
| cURL | Command-line tool and library | Yes | Since version 7.18.1 | 2008 | Partial |   |
| Safari | Web browser | Yes | Not supported on Windows XP |   | No |   |
| Google Chrome | Web browser | Yes |   | 2010 | Yes | Since v105 behind flag. |
| BlackBerry 10 | Web browser | Yes | Supported in all BB10 releases | 2013 | No |   |
| BlackBerry OS |   |   |   |   | No |   |
| Barracuda WAF | Reverse Proxy | Yes | Supported since version 7.8 | 2013 |   |   |
| Barracuda ADC | Load balancer | Yes | Frontend support since version 4.0 and backend support from v5.2 | Frontend 2013 / Backend 2015 |   |   |
| Windows Mobile | Web browser |   | Some time after 6.5 |   | No |   |
| Android browser (discontinued in Android 4.2) | Web browser | Yes | Honeycomb (3.x) for tablets and Ice Cream Sandwich (4.x) for phones | 2011 | No |   |
| Firefox for Android | Web browser | Yes | Supported for browsing. Sync and other services support SNI only since version 86. |   | Yes | Introduced in Nightly behind a flag, available by default since v143 |
| wget | Command-line tool | Yes | Since version 1.14 | 2012 |   |   |
| Nokia Browser for Symbian | Web browser | No |   |   | No |   |
| Opera Mobile for Symbian | Web browser | No | Not supported on Series60 |   | No |   |
| Dillo | Web browser | Yes | Since version 3.1 | 2016 |   |   |
| IBM HTTP Server | Web server | Yes | Since version 9.0.0 |   |   |   |
| Apache Tomcat | Web server | Yes | Not supported before 8.5 (backport from 9) |   |   |   |
| Apache HTTP Server | Web server | Yes | Since version 2.2.12 | 2009 |   |   |
| Microsoft IIS | Web server | Yes | Since version 8 (part of Windows Server 2012) | 2012 |   |   |
| nginx | Web server | Yes | Since version 0.5.23 | 2007 | Yes | Since v1.29.4 |
| Caddy (web server) | Web server | Yes |   |   | Yes |   |
| Jetty | Web server | Yes | Since version 9.3.0 | 2015 |   |   |
| HCL Domino | Web server | Yes | Since version 11.0.1 | 2020 |   |   |
| HCL Notes | Workflow client | Yes | Since version 14.0 | 2023 |   |   |
| H2O | Web server | Yes |   |   | Yes |   |
| BoringSSL | Library | Yes |   |   | Yes |   |
| BSAFE Micro Edition Suite | Library | Yes |   | Version 5.0 |   |   |
| GnuTLS | Library | Yes |   |   | No | Work in progress as July 2023. |
| LibreSSL | Library | Yes |   |   | No |   |
| Mbed TLS | Library | Yes |   |   | No |   |
| Mozilla NSS client side | Library | Yes | Since version 3.11.1 | 2006 | Yes |   |
| Mozilla NSS server side | Library | No |   |   | No |   |
| OpenSSL | Library | Yes |   |   | Yes | Since v4.0.0 |
| Picotls | Library | Yes |   |   | Yes |   |
| Rustls | Library | Yes |   |   | No | Supports client-side ECH; server-side ECH still todo as of August 2024 |
| SwiftNIO SSL | Library | Yes |   |   | No |   |
| wolfSSL | Library | Yes |   |   | Yes | Since v5.6.3 |
| 4th Dimension | Standard library | No | Not supported in 15.2 or earlier |   | No |   |
| ColdFusion / Lucee | Standard library | Yes | ColdFusion since Version 10 Update 18, 11 Update 7, Lucee since Version 4.5.1.019, Version 5.0.0.50 | 2015 |   |   |
| Erlang | Standard library | Yes | Since version r17 | 2013 |   |   |
| Go | Standard library | Yes | Since version 1.4 | 2011 |   | Cloudflare/go fork provides support |
| Java | Standard library | Yes | Since version 1.7 | 2011 |   |   |
| Perl | Standard library | Yes | Since `Net::SSLeay` version 1.50 and `IO::Socket::SSL` version 1.56 | 2012 |   |   |
| PHP | Standard library | Yes | Since version 5.3 | 2014 |   |   |
| Python | Standard library | Yes | Supported in 2.x from 2.7.9 and 3.x from 3.2 (in `ssl`, `urllib[2]` and `httplib` modules) | 2011 for Python 3.x and 2014 for Python 2.x |   |   |
| Qt | Standard library | Yes | Since version 4.8 | 2011 |   |   |
| Ruby | Standard library | Yes | Since version 2.0 (in `net/http`) | 2011 |   |   |
| Hiawatha | Web server | Yes | Since version 8.6 | 2012 | No | Depends on Mbed TLS. |
| lighttpd | Web server | Yes | Since version 1.4.24 | 2009 | Yes | Since version 1.4.77 |
| HAProxy | Load balancer | Yes | Since version 1.5-dev12 | 2012 | Yes |   |
| OpenBSD httpd | Web server | Yes | Since OpenBSD version 6.1 | 2017-04-11 | No | Depends on OpenSSL. |
