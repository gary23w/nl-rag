---
title: "Transport Layer Security (part 1/3)"
source: https://en.wikipedia.org/wiki/Transport_Layer_Security
domain: security
license: CC-BY-SA-4.0 (OWASP) / CC-BY-SA-4.0 (Wikipedia)
tags: security, authentication, password hashing, session token, tls, owasp
fetched: 2026-07-02
part: 1/3
---

# Transport Layer Security

**Transport Layer Security** (**TLS**) is a cryptographic protocol designed to provide communications security over a computer network, such as the Internet. The protocol is widely used in applications such as email, instant messaging, and voice over IP, but its use in securing HTTPS remains the most publicly visible.

The TLS protocol aims primarily to provide security, including privacy (confidentiality), integrity, and authenticity through the use of cryptography, such as the use of certificates, between two or more communicating computer applications. It runs in the presentation layer and is itself composed of two layers: the TLS record and the TLS handshake protocols.

The closely-related Datagram Transport Layer Security (DTLS) is a communications protocol that provides security to datagram-based applications. In technical writing, references to "(D)TLS" are often seen when it applies to both versions.

TLS is a proposed Internet Engineering Task Force (IETF) standard, first defined in 1999, and the current version is TLS 1.3, defined in August 2018. TLS builds on the now-deprecated **SSL** (**Secure Sockets Layer**) specifications (1994, 1995, 1996) developed by Netscape Communications for adding the HTTPS protocol to their Netscape Navigator web browser.


## Description

Client–server applications use the TLS protocol to communicate across a network in a way designed to prevent eavesdropping and tampering.

Since applications can communicate either with or without TLS (or SSL), it is necessary for the client to request that the server set up a TLS connection. One of the main ways of achieving this is to use a different port number for TLS connections. Port 80 is typically used for unencrypted HTTP traffic while port 443 is the common port used for encrypted HTTPS traffic. Another mechanism is to make a protocol-specific STARTTLS request to the server to switch the connection to TLS – for example, when using some mail and news protocols.

Once the client and server have agreed to use TLS, they negotiate a stateful connection by using a handshaking procedure (see § TLS handshake). The protocols use a handshake with an asymmetric cipher to establish not only cipher settings but also a session-specific shared key with which further communication is encrypted using a symmetric cipher. During this handshake, the client and server agree on various parameters used to establish the connection's security:

- The handshake begins when a client connects to a TLS-enabled server requesting a secure connection and the client presents a list of supported cipher suites (ciphers and hash functions).
- From this list, the server picks a cipher and hash function that it also supports and notifies the client of the decision.
- The server usually then provides identification in the form of a digital certificate. The certificate contains the server name, the trusted certificate authority (CA) that vouches for the authenticity of the certificate, and the server's public encryption key.
- The client confirms the validity of the certificate before proceeding.
- To generate the session keys used for the secure connection, the client either:
  - encrypts a random number (*PreMasterSecret*) with the server's public key and sends the result to the server (which only the server should be able to decrypt with its private key); both parties then use the random number to generate a unique session key for subsequent encryption and decryption of data during the session, or
  - uses Diffie–Hellman key exchange (or its variant elliptic-curve DH) to securely generate a random and unique session key for encryption and decryption that has the additional property of forward secrecy: if the server's private key is disclosed in the future, it cannot be used to decrypt the current session, even if the session is intercepted and recorded by a third party.

This concludes the handshake and begins the secured connection, which is encrypted and decrypted with the session key until the connection closes. If any one of the above steps fails, then the TLS handshake fails and the connection is not created.

Note that TLS 1.3 only allows key exchange algorithms providing forward secrecy. Consequently, establishing a PreMasterSecret using the server's public and private key is only available in TLS 1.2 and below.

TLS and SSL do not fit neatly into any single layer of the OSI model or the TCP/IP model. TLS runs "on top of some reliable transport protocol (e.g., TCP)", which would imply that it is above the transport layer. It serves encryption to higher layers, which is normally the function of the presentation layer. However, applications generally use TLS as if it were a transport layer, even though applications using TLS must actively control initiating TLS handshakes and handling of exchanged authentication certificates.

When secured by TLS, connections between a client (e.g., a web browser) and a server (e.g., wikipedia.org) will have all of the following properties:

- The connection is *private* (or has *confidentiality*) because a symmetric-key algorithm is used to encrypt the data transmitted. The keys for this symmetric encryption are generated uniquely for each connection and are based on a shared secret that was negotiated at the start of the session. The server and client negotiate the details of which encryption algorithm and cryptographic keys to use before the first byte of data is transmitted (see below). The negotiation of a shared secret is both secure (the negotiated secret is unavailable to eavesdroppers and cannot be obtained, even by an attacker who places themselves in the middle of the connection) and reliable (no attacker can modify the communications during the negotiation without being detected).
- The identity of the communicating parties can be *authenticated* using public-key cryptography. This authentication is required for the server and optional for the client.
- The connection is *reliable* (or has *integrity*) because each message transmitted includes a message integrity check using a message authentication code to prevent undetected loss or alteration of the data during transmission.

TLS supports many different methods for exchanging keys, encrypting data, and authenticating message integrity. As a result, secure configuration of TLS involves many configurable parameters, and not all choices provide all of the privacy-related properties described in the list above (see the tables below § Key exchange, § Cipher security, and § Data integrity).

Attempts have been made to subvert aspects of the communications security that TLS seeks to provide, and the protocol has been revised several times to address these security threats. Developers of web browsers have repeatedly revised their products to defend against potential security weaknesses after these were discovered (see TLS/SSL support history of web browsers).

### Datagram Transport Layer Security

Datagram Transport Layer Security, abbreviated DTLS, is a related communications protocol providing security to datagram-based applications by allowing them to communicate in a way designed to prevent eavesdropping, tampering, or message forgery. The DTLS protocol is based on the stream-oriented Transport Layer Security (TLS) protocol and is intended to provide similar security guarantees. However, unlike TLS, it can be used with most datagram oriented protocols including User Datagram Protocol (UDP), Datagram Congestion Control Protocol (DCCP), Control And Provisioning of Wireless Access Points (CAPWAP), Stream Control Transmission Protocol (SCTP) encapsulation, and Secure Real-time Transport Protocol (SRTP).

As the DTLS protocol datagram preserves the semantics of the underlying transport, the application does not suffer from the delays associated with stream protocols. However, the application has to deal with packet reordering, loss of datagram and data larger than the size of a datagram network packet. Because DTLS uses UDP or SCTP rather than TCP, it avoids the TCP meltdown problem, when being used to create a VPN tunnel.

The original 2006 release of DTLS version 1.0 was not a standalone document. It was given as a series of deltas to TLS 1.1. Similarly the follow-up 2012 release of DTLS is a delta to TLS 1.2. It was given the version number of DTLS 1.2 to match its TLS version. Lastly, the 2022 DTLS 1.3 is a delta to TLS 1.3. Like the two previous versions, DTLS 1.3 is intended to provide "equivalent security guarantees [to TLS 1.3] with the exception of order protection/non-replayability".

Many VPN clients including Cisco AnyConnect & InterCloud Fabric, OpenConnect, ZScaler tunnel, F5 Networks Edge VPN Client, and Citrix Systems NetScaler use DTLS to secure UDP traffic. In addition all modern web browsers support DTLS-SRTP for WebRTC.


## History and development

| Protocol | Published | Status |
|---|---|---|
| Unsupported: SSL 1.0 | Unpublished | Unpublished |
| Unsupported: SSL 2.0 | 1995 | Deprecated in 2011 |
| Unsupported: SSL 3.0 | 1996 | Deprecated in 2015 |
| Unsupported: TLS 1.0 | 1999 | Deprecated in 2021 |
| Unsupported: TLS 1.1 | 2006 | Deprecated in 2021 |
| Supported: TLS 1.2 | 2008 | In use since 2008 |
| Latest version: TLS 1.3 | 2018 | In use since 2018 |
| **Legend:**UnsupportedSupported**Latest version**Preview versionFuture version |   |   |

### Early research projects

#### Secure Data Network System

In August 1986, the National Security Agency, the National Bureau of Standards, the Defense Communications Agency launched a project, called the Secure Data Network System (SDNS), with the intent of designing the next generation of secure computer communications network and product specifications to be implemented for applications on public and private internets. It was intended to complement the rapidly emerging new OSI internet standards moving forward both in the U.S. government's GOSIP Profiles and in the huge ITU-ISO JTC1 internet effort internationally.

As part of the project, researchers designed a protocol called SP4 (*security protocol* in layer 4 of the OSI system). This was later renamed the Transport Layer Security Protocol (TLSP) and subsequently published in 1995 as international standard ITU-T X.274|ISO/IEC 10736:1995. Despite the name similarity, this is distinct from today's TLS.

#### Secure Network Programming (SNP)

Other efforts towards transport layer security included the Secure Network Programming (SNP) application programming interface (API), which in 1993 explored the approach of having a secure transport layer API closely resembling Berkeley sockets, to facilitate retrofitting pre-existing network applications with security measures. SNP was published and presented in the 1994 USENIX Summer Technical Conference. The SNP project was funded by a grant from NSA to Professor Simon Lam at UT-Austin in 1991. Secure Network Programming won the 2004 ACM Software System Award. Simon Lam was inducted into the Internet Hall of Fame for "inventing secure sockets in 1991 and implementing the first secure sockets layer, named SNP, in 1993."

### SSL 1.0, 2.0, and 3.0

Netscape developed the original SSL protocols, and Taher Elgamal, chief scientist at Netscape Communications from 1995 to 1998, has been described as the "father of SSL". SSL version 1.0 was never publicly released because of serious security flaws in the protocol. Version 2.0, after being released in February 1995 was quickly found to contain a number of security and usability flaws. It used the same cryptographic keys for message authentication and encryption. It had a weak MAC construction that used the MD5 hash function with a secret prefix, making it vulnerable to length extension attacks. It also provided no protection for either the opening handshake or an explicit message close, both of which meant man-in-the-middle attacks could go undetected. Moreover, SSL 2.0 assumed a single service and a fixed domain certificate, conflicting with the widely used feature of virtual hosting in Web servers, so most websites were effectively impaired from using SSL.

These flaws necessitated the complete redesign of the protocol to SSL version 3.0. Released in 1996, it was produced by Paul Kocher working with Netscape engineers Phil Karlton and Alan Freier, with a reference implementation by Christopher Allen and Tim Dierks of Certicom. Newer versions of SSL/TLS are based on SSL 3.0. The 1996 draft of SSL 3.0 was published by IETF as a historical document in RFC 6101.

SSL 2.0 was deprecated in 2011 by RFC 6176. In 2014, SSL 3.0 was found to be vulnerable to the POODLE attack that affects all block ciphers in SSL; RC4, the only non-block cipher supported by SSL 3.0, is also feasibly broken as used in SSL 3.0. SSL 3.0 was deprecated in June 2015 by RFC 7568.

### TLS 1.0

TLS 1.0 was first defined in RFC 2246 in January 1999 as an upgrade of SSL Version 3.0, and written by Christopher Allen and Tim Dierks of Certicom. As stated in the RFC, "the differences between this protocol and SSL 3.0 are not dramatic, but they are significant enough to preclude interoperability between TLS 1.0 and SSL 3.0". Tim Dierks later wrote that these changes, and the renaming from "SSL" to "TLS", were a face-saving gesture to Microsoft, "so it wouldn't look [like] the IETF was just rubberstamping Netscape's protocol".

The PCI Council suggested that organizations migrate from TLS 1.0 to TLS 1.1 or higher before June 30, 2018. In October 2018, Apple, Google, Microsoft, and Mozilla jointly announced they would deprecate TLS 1.0 and 1.1 in March 2020. TLS 1.0 and 1.1 were formally deprecated in RFC 8996 in March 2021.

### TLS 1.1

TLS 1.1 was defined in RFC 4346 in April 2006. It is an update from TLS version 1.0. Significant differences in this version include:

- Added protection against cipher-block chaining (CBC) attacks.
  - The implicit initialization vector (IV) was replaced with an explicit IV.
  - Change in handling of padding errors.
- Support for IANA registration of parameters.

Support for TLS versions 1.0 and 1.1 was widely deprecated by web sites around 2020, disabling access to Firefox versions before 24 and Chromium-based browsers before 29, though third-party fixes can be applied to Netscape Navigator and older versions of Firefox to add TLS 1.2 support.

### TLS 1.2

TLS 1.2 was defined in RFC 5246 in August 2008. It is based on the earlier TLS 1.1 specification. Major differences include:

- The MD5 and SHA-1 combination in the pseudorandom function (PRF) was replaced with SHA-256, with an option to use cipher suite specified PRFs.
- The MD5 and SHA-1 combination in the finished message hash was replaced with SHA-256, with an option to use cipher suite specific hash algorithms. However, the size of the hash in the finished message must still be at least 96 bits.
- The MD5 and SHA-1 combination in the digitally signed element was replaced with a single hash negotiated during handshake, which defaults to SHA-1.
- Enhancement in the client's and server's ability to specify which hashes and signature algorithms they accept.
- Expansion of support for authenticated encryption ciphers, used mainly for Galois/Counter Mode (GCM) and CCM mode of Advanced Encryption Standard (AES) encryption.
- TLS Extensions definition and AES cipher suites were added.

All TLS versions were further refined in RFC 6176 in March 2011, removing their backward compatibility with SSL such that TLS sessions never negotiate the use of Secure Sockets Layer (SSL) version 2.0. As of April 2025 there is no formal date for TLS 1.2 to be deprecated. The specifications for TLS 1.2 became redefined as well by the Standards Track Document RFC 8446 to keep it as secure as possible; it is to be seen as a failover protocol now, meant only to be negotiated with clients which are unable to use TLS 1.3 (The original RFC 5246 definition for TLS 1.2 is since then obsolete).

### TLS 1.3

TLS 1.3 was defined in RFC 8446 in August 2018. It is based on the earlier TLS 1.2 specification. Major differences from TLS 1.2 include:

- Separating key agreement and authentication algorithms from the cipher suites
- Removing support for weak and less-used named elliptic curves
- Removing support for MD5 and SHA-224 cryptographic hash functions
- Requiring digital signatures even when a previous configuration is used
- Integrating HKDF and the semi-ephemeral DH proposal
- Replacing resumption with PSK and tickets
- Supporting 1-RTT handshakes and initial support for 0-RTT
- Mandating perfect forward secrecy, by means of using ephemeral keys during the (EC)DH key agreement
- Dropping support for many insecure or obsolete features including compression, renegotiation, non-AEAD ciphers, null ciphers, non-PFS key exchange (among which are static RSA and static DH key exchanges), custom DHE groups, EC point format negotiation, Change Cipher Spec protocol, Hello message UNIX time, and the length field AD input to AEAD ciphers
- Prohibiting SSL or RC4 negotiation for backwards compatibility
- Integrating use of session hash
- Deprecating use of the record layer version number and freezing the number for improved backwards compatibility
- Moving some security-related algorithm details from an appendix to the specification and relegating ClientKeyShare to an appendix
- Adding the ChaCha20 stream cipher with the Poly1305 message authentication code
- Adding the Ed25519 and Ed448 digital signature algorithms
- Adding the x25519 and x448 key exchange protocols
- Adding support for sending multiple OCSP responses
- Encrypting all handshake messages after the ServerHello, including server certificate

Network Security Services (NSS), the cryptography library developed by Mozilla and used by its web browser Firefox, enabled TLS 1.3 by default in February 2017. TLS 1.3 support was subsequently added — but due to compatibility issues for a small number of users, not automatically enabled — to Firefox 52.0, which was released in March 2017. TLS 1.3 was enabled by default in May 2018 with the release of Firefox 60.0.

Google Chrome set TLS 1.3 as the default version for a short time in 2017. It then removed it as the default, due to incompatible middleboxes such as Blue Coat web proxies.

The intolerance of the new version of TLS was protocol ossification; middleboxes had ossified the protocol's version parameter. As a result, version 1.3 mimics the wire image of version 1.2. This change occurred very late in the design process, only having been discovered during browser deployment. The discovery of this intolerance also led to the prior version negotiation strategy, where the highest matching version was picked, being abandoned due to unworkable levels of ossification. 'Greasing' an extension point, where one protocol participant claims support for non-existent extensions to ensure that unrecognised-but-actually-existent extensions are tolerated and so to resist ossification, was originally designed for TLS, but it has since been adopted elsewhere.

During the IETF 100 Hackathon, which took place in Singapore in 2017, the TLS Group worked on adapting open-source applications to use TLS 1.3. The TLS group was made up of individuals from Japan, United Kingdom, and Mauritius via the cyberstorm.mu team. This work was continued in the IETF 101 Hackathon in London, and the IETF 102 Hackathon in Montreal.

wolfSSL enabled the use of TLS 1.3 as of version 3.11.1, released in May 2017. As the first commercial TLS 1.3 implementation, wolfSSL 3.11.1 supported Draft 18 and now supports Draft 28, the final version, as well as many older versions. A series of blogs were published on the performance difference between TLS 1.2 and 1.3.

In September 2018, the popular OpenSSL project released version 1.1.1 of its library, in which support for TLS 1.3 was "the headline new feature".

Support for TLS 1.3 was added to Secure Channel (schannel) for the GA releases of Windows 11 and Windows Server 2022.

#### Enterprise Transport Security

The Electronic Frontier Foundation praised TLS 1.3 and expressed concern about the variant protocol Enterprise Transport Security (ETS) that intentionally disables important security measures in TLS 1.3. Originally called Enterprise TLS (eTLS), ETS is a published standard known as the 'ETSI TS103523-3', "Middlebox Security Protocol, Part3: Enterprise Transport Security". It is intended for use entirely within proprietary networks such as banking systems. ETS does not support forward secrecy so as to allow third-party organizations connected to the proprietary networks to be able to use their private key to monitor network traffic for the detection of malware and to make it easier to conduct audits. Despite the claimed benefits, the EFF warned that the loss of forward secrecy could make it easier for data to be exposed along with saying that there are better ways to analyze traffic.


## Digital certificates

A digital certificate certifies the ownership of a public key by the named subject of the certificate, and indicates certain expected usages of that key. This allows others (relying parties) to rely upon signatures or on assertions made by the private key that corresponds to the certified public key. Keystores and trust stores can be in various formats, such as .pem, .crt, .pfx, and .jks.

### Certificate authorities

TLS typically relies on a set of trusted third-party certificate authorities to establish the authenticity of certificates. Trust is usually anchored in a list of certificates distributed with user agent software, and can be modified by the relying party.

According to Netcraft, who monitors active TLS certificates, the market-leading certificate authority (CA) has been Symantec since the beginning of their survey (or VeriSign before the authentication services business unit was purchased by Symantec). As of 2015, Symantec accounted for just under a third of all certificates and 44% of the valid certificates used by the 1 million busiest websites, as counted by Netcraft. In 2017, Symantec sold its TLS/SSL business to DigiCert. In an updated report, it was shown that IdenTrust, DigiCert, and Sectigo are the top 3 certificate authorities in terms of market share since May 2019.

As a consequence of choosing X.509 certificates, certificate authorities and a public key infrastructure are necessary to verify the relation between a certificate and its owner, as well as to generate, sign, and administer the validity of certificates. While this can be more convenient than verifying the identities via a web of trust, the 2013 mass surveillance disclosures made it more widely known that certificate authorities are a weak point from a security standpoint, allowing man-in-the-middle attacks (MITM) if the certificate authority cooperates (or is compromised).

On April 11, 2025, the CA/Browser Forum approved a ballot that will require all public TLS certificate lifespans to gradually reduce to 47 days by 2029. The ballot was proposed by Apple.


## Algorithms

### Key exchange or key agreement

Before a client and server can begin to exchange information protected by TLS, they must securely exchange or agree upon an encryption key and a cipher to use when encrypting data (see § Cipher). Among the methods used for key exchange/agreement are: public and private keys generated with RSA (denoted TLS_RSA in the TLS handshake protocol), Diffie–Hellman (TLS_DH), ephemeral Diffie–Hellman (TLS_DHE), elliptic-curve Diffie–Hellman (TLS_ECDH), ephemeral elliptic-curve Diffie–Hellman (TLS_ECDHE), anonymous Diffie–Hellman (TLS_DH_anon), pre-shared key (TLS_PSK) and Secure Remote Password (TLS_SRP).

The TLS_DH_anon and TLS_ECDH_anon key agreement methods do not authenticate the server or the user and hence are rarely used because those are vulnerable to man-in-the-middle attacks. Only TLS_DHE and TLS_ECDHE provide forward secrecy.

Public key certificates used during exchange/agreement also vary in the size of the public/private encryption keys used during the exchange and hence the robustness of the security provided. In July 2013, Google announced that it would no longer use 1024-bit public keys and would switch instead to 2048-bit keys to increase the security of the TLS encryption it provides to its users because the encryption strength is directly related to the key size.

| Algorithm | SSL 2.0 | SSL 3.0 | TLS 1.0 | TLS 1.1 | TLS 1.2 | TLS 1.3 | Status |
|---|---|---|---|---|---|---|---|
| RSA | Yes | Yes | Yes | Yes | Yes | No | Defined for TLS 1.2 in RFCs |
| DH-RSA | No | Yes | Yes | Yes | Yes | No |   |
| DHE-RSA (forward secrecy) | No | Yes | Yes | Yes | Yes | Yes |   |
| ECDH-RSA | No | No | Yes | Yes | Yes | No |   |
| ECDHE-RSA (forward secrecy) | No | No | Yes | Yes | Yes | Yes |   |
| DH-DSS | No | Yes | Yes | Yes | Yes | No |   |
| DHE-DSS (forward secrecy) | No | Yes | Yes | Yes | Yes | No |   |
| DHE-ECDSA (forward secrecy) | No | No | No | No | No | Yes |   |
| ECDH-ECDSA | No | No | Yes | Yes | Yes | No |   |
| ECDHE-ECDSA (forward secrecy) | No | No | Yes | Yes | Yes | Yes |   |
| DHE-EdDSA (forward secrecy) | No | No | No | No | No | Yes |   |
| ECDH-EdDSA | No | No | Yes | Yes | Yes | No |   |
| ECDHE-EdDSA (forward secrecy) | No | No | Yes | Yes | Yes | Yes |   |
| PSK | No | No | Yes | Yes | Yes | Yes |   |
| RSA-PSK | No | No | Yes | Yes | Yes | No |   |
| DHE-PSK (forward secrecy) | No | No | Yes | Yes | Yes | Yes |   |
| ECDHE-PSK (forward secrecy) | No | No | Yes | Yes | Yes | Yes |   |
| SRP | No | No | Yes | Yes | Yes | No |   |
| SRP-DSS | No | No | Yes | Yes | Yes | No |   |
| SRP-RSA | No | No | Yes | Yes | Yes | No |   |
| Kerberos | No | No | Yes | Yes | Yes | ? |   |
| DH-ANON (insecure) | No | Yes | Yes | Yes | Yes | No |   |
| ECDH-ANON (insecure) | No | No | Yes | Yes | Yes | No |   |
| GOST R 34.10-2012 | No | No | No | No | Yes | Yes | Defined for TLS 1.2 and for TLS 1.3. |

### Cipher

Cipher

security against publicly known feasible attacks

Cipher

Protocol version

Status

Type

Algorithm

Nominal strength (bits)

SSL 2.0

SSL 3.0

TLS 1.0

TLS 1.1

TLS 1.2

TLS 1.3

Block cipher

with

mode of operation

AES

GCM

256, 128

—

N/a

—

N/a

—

N/a

—

N/a

Secure

Secure

Defined for TLS 1.2 in RFCs

AES

CCM

—

N/a

—

N/a

—

N/a

—

N/a

Secure

Secure

AES

CBC

—

N/a

Insecure

Depends on mitigations

Depends on mitigations

Depends on mitigations

—

N/a

Camellia

GCM

256, 128

—

N/a

—

N/a

—

N/a

—

N/a

Secure

—

N/a

Camellia

CBC

—

N/a

Insecure

Depends on mitigations

Depends on mitigations

Depends on mitigations

—

N/a

ARIA

GCM

256, 128

—

N/a

—

N/a

—

N/a

—

N/a

Secure

—

N/a

ARIA

CBC

—

N/a

—

N/a

Depends on mitigations

Depends on mitigations

Depends on mitigations

—

N/a

SEED

CBC

128

—

N/a

Insecure

Depends on mitigations

Depends on mitigations

Depends on mitigations

—

N/a

3DES EDE

CBC

112

Insecure

Insecure

Insecure

Insecure

Insecure

—

N/a

GOST R 34.12-2015 Magma

CTR

256

—

N/a

—

N/a

Insecure

Insecure

Insecure

—

N/a

Defined in

RFC

4357

,

9189

GOST R 34.12-2015 Kuznyechik

CTR

256

—

N/a

—

N/a

—

N/a

—

N/a

Secure

—

N/a

Defined in

RFC

9189

GOST R 34.12-2015 Magma

MGM

256

—

N/a

—

N/a

—

N/a

—

N/a

—

N/a

Insecure

Defined in

RFC

9367

GOST R 34.12-2015 Kuznyechik

MGM

256

—

N/a

—

N/a

—

N/a

—

N/a

—

N/a

Secure

Defined in

RFC

9367

IDEA

CBC

128

Insecure

Insecure

Insecure

Insecure

—

N/a

—

N/a

Removed from TLS 1.2

DES

CBC

0

56

Insecure

Insecure

Insecure

Insecure

—

N/a

—

N/a

0

40

Insecure

Insecure

Insecure

—

N/a

—

N/a

—

N/a

Forbidden in TLS 1.1 and later

RC2

CBC

0

40

Insecure

Insecure

Insecure

—

N/a

—

N/a

—

N/a

Stream cipher

ChaCha20

-

Poly1305

256

—

N/a

—

N/a

—

N/a

—

N/a

Secure

Secure

Defined for TLS 1.2 in RFCs

RC4

128

Insecure

Insecure

Insecure

Insecure

Insecure

—

N/a

Prohibited in all versions of TLS

0

40

Insecure

Insecure

Insecure

—

N/a

—

N/a

—

N/a

None

Null

–

Insecure

Insecure

Insecure

Insecure

Insecure

—

N/a

Defined for TLS 1.2 in RFCs

**Notes**

1. RFC 5746 must be implemented to fix a renegotiation flaw that would otherwise break this protocol.
2. If libraries implement fixes listed in RFC 5746, this violates the SSL 3.0 specification, which the IETF cannot change unlike TLS. Most current libraries implement the fix and disregard the violation that this causes.
3. The BEAST attack breaks all block ciphers (CBC ciphers) used in SSL 3.0 and TLS 1.0 unless mitigated by the client or the server. See § Web browsers.
4. The POODLE attack breaks all block ciphers (CBC ciphers) used in SSL 3.0 unless mitigated by the client or the server. See § Web browsers.
5. AEAD ciphers (such as GCM and CCM) can only be used in TLS 1.2 or later.
6. CBC ciphers can be attacked with the Lucky Thirteen attack if the library is not written carefully to eliminate timing side channels.
7. The Sweet32 attack breaks block ciphers with a block size of 64 bits.
8. Although the key length of 3DES is 168 bits, effective security strength of 3DES is only 112 bits, which is below the recommended minimum of 128 bits.
9. IDEA and DES have been removed from TLS 1.2.
10. 40-bit strength cipher suites were intentionally designed with reduced key lengths to comply with since-rescinded US regulations forbidding the export of cryptographic software containing certain strong encryption algorithms (see Export of cryptography from the United States). These weak suites are forbidden in TLS 1.1 and later.
11. Use of RC4 in all versions of TLS is prohibited because RC4 attacks weaken or break RC4 used in SSL/TLS.
12. Authentication only, no encryption.

### Data integrity

A message authentication code (MAC) is used for data integrity. HMAC is used for CBC mode of block ciphers. Authenticated encryption (AEAD) such as GCM and CCM mode uses AEAD-integrated MAC and does not use HMAC. HMAC-based PRF, or HKDF is used for TLS handshake.

| Algorithm | SSL 2.0 | SSL 3.0 | TLS 1.0 | TLS 1.1 | TLS 1.2 | TLS 1.3 | Status |
|---|---|---|---|---|---|---|---|
| HMAC-MD5 | Yes | Yes | Yes | Yes | Yes | No | Defined for TLS 1.2 in RFCs |
| HMAC-SHA1 | No | Yes | Yes | Yes | Yes | No |   |
| HMAC-SHA256/384 | No | No | No | No | Yes | No |   |
| AEAD | No | No | No | No | Yes | Yes |   |
| GOST 28147-89 IMIT | No | No | No | No | Yes | No | Defined for TLS 1.2 in RFC 9189. |
| GOST R 34.12-2015 AEAD | No | No | No | No | No | Yes | Defined for TLS 1.3 in RFC 9367. |


## Applications and adoption

In applications design, TLS is usually implemented on top of Transport Layer protocols, encrypting all of the protocol-related data of protocols such as HTTP, FTP, SMTP, NNTP and XMPP.

Historically, TLS has been used primarily with reliable transport protocols such as the Transmission Control Protocol (TCP). However, it has also been implemented with datagram-oriented transport protocols, such as the User Datagram Protocol (UDP) and the Datagram Congestion Control Protocol (DCCP), usage of which has been standardized independently using the term *Datagram Transport Layer Security* (*DTLS*).

### Websites

A primary use of TLS is to secure World Wide Web traffic between a website and a web browser encoded with the HTTP protocol. This use of TLS to secure HTTP traffic constitutes the HTTPS protocol.

| Protocol version | selected Web­sites' support | Security |
|---|---|---|
| Unsupported: SSL 2.0 | 0.1% | Insecure |
| Unsupported: SSL 3.0 | 1.0% | Insecure |
| Unsupported: TLS 1.0 | 23.5% | Deprecated |
| Unsupported: TLS 1.1 | 25.2% | Deprecated |
| Supported: TLS 1.2 | 100% | Depends on cipher and client mitigations |
| Latest version: TLS 1.3 | 75.3% | Secure |

**Notes**

1. see § Cipher table above
2. see § Web browsers and § Attacks against TLS/SSL sections

### Web browsers

As of March 2025, the latest versions of all major web browsers support TLS 1.2 and 1.3 and have them enabled by default, with the exception of IE 11. TLS 1.0 and 1.1 are disabled by default on the latest versions of all major browsers.

Mitigations against known attacks are not enough yet:

- Mitigations against POODLE attack: some browsers already prevent fallback to SSL 3.0; however, this mitigation needs to be supported by not only clients but also servers. Disabling SSL 3.0 itself, implementation of "anti-POODLE record splitting", or denying CBC ciphers in SSL 3.0 is required.
  - Google Chrome: complete (TLS_FALLBACK_SCSV is implemented since version 33, fallback to SSL 3.0 is disabled since version 39, SSL 3.0 itself is disabled by default since version 40. Support of SSL 3.0 itself was dropped since version 44.)
  - Mozilla Firefox: complete (support of SSL 3.0 itself is dropped since version 39. SSL 3.0 itself is disabled by default and fallback to SSL 3.0 are disabled since version 34, TLS_FALLBACK_SCSV is implemented since version 35. In ESR, SSL 3.0 itself is disabled by default and TLS_FALLBACK_SCSV is implemented since ESR 31.3.0.)
  - Internet Explorer: partial (only in version 11, SSL 3.0 is disabled by default since April 2015. Version 10 and older are still vulnerable against POODLE.)
  - Opera: complete (TLS_FALLBACK_SCSV is implemented since version 20, "anti-POODLE record splitting", which is effective only with client-side implementation, is implemented since version 25, SSL 3.0 itself is disabled by default since version 27. Support of SSL 3.0 itself will be dropped since version 31.)
  - Safari: complete (only on OS X 10.8 and later and iOS 8, CBC ciphers during fallback to SSL 3.0 is denied, but this means it will use RC4, which is not recommended as well. Support of SSL 3.0 itself is dropped on OS X 10.11 and later and iOS 9.)
- Mitigation against RC4 attacks:
  - Google Chrome disabled RC4 except as a fallback since version 43. RC4 is disabled since Chrome 48.
  - Firefox disabled RC4 except as a fallback since version 36. Firefox 44 disabled RC4 by default.
  - Opera disabled RC4 except as a fallback since version 30. RC4 is disabled since Opera 35.
  - Internet Explorer for Windows 7/Server 2008 R2 and for Windows 8/Server 2012 have set the priority of RC4 to lowest and can also disable RC4 except as a fallback through registry settings. Internet Explorer 11 Mobile 11 for Windows Phone 8.1 disable RC4 except as a fallback if no other enabled algorithm works. Edge [Legacy] and IE 11 disable RC4 completely in August 2016.
- Mitigation against FREAK attack:
  - The Android Browser included with Android 4.0 and older is still vulnerable to the FREAK attack.
  - Internet Explorer 11 Mobile is still vulnerable to the FREAK attack.
  - Google Chrome, Internet Explorer (desktop), Safari (desktop & mobile), and Opera (mobile) have FREAK mitigations in place.
  - Mozilla Firefox on all platforms and Google Chrome on Windows were not affected by FREAK.

### Libraries

Most SSL and TLS programming libraries are free and open-source software.

- BoringSSL, a fork of OpenSSL for Chrome/Chromium and Android as well as other Google applications.
- Botan, a BSD-licensed cryptographic library written in C++.
- BSAFE Micro Edition Suite: a multi-platform implementation of TLS written in C using a FIPS-validated cryptographic module
- BSAFE SSL-J: a TLS library providing both a proprietary API and JSSE API, using FIPS-validated cryptographic module
- cryptlib: a portable open source cryptography library (includes TLS/SSL implementation)
- Delphi programmers may use a library called Indy which utilizes OpenSSL or alternatively ICS which supports TLS 1.3 now.
- GnuTLS: a free implementation (LGPL licensed)
- Java Secure Socket Extension (JSSE): the Java API and provider implementation (named SunJSSE)
- LibreSSL: a fork of OpenSSL by OpenBSD project.
- MatrixSSL: a dual licensed implementation
- Mbed TLS (previously PolarSSL): A tiny SSL library implementation for embedded devices that is designed for ease of use
- Network Security Services: FIPS 140 validated open source library
- OpenSSL: a free implementation (BSD license with some extensions)
- Rustls, An implementation of TLS 1.3 written in the Rust programming language to ensure memory safety.
- Schannel: an implementation of SSL and TLS Microsoft Windows as part of its package.
- Secure Transport: an implementation of SSL and TLS used in OS X and iOS as part of their packages.
- wolfSSL (previously CyaSSL): Embedded SSL/TLS Library with a strong focus on speed and size.

A paper presented at the 2012 ACM conference on computer and communications security showed that many applications used some of these SSL libraries incorrectly, leading to vulnerabilities. According to the authors:

> "The root cause of most of these vulnerabilities is the terrible design of the APIs to the underlying SSL libraries. Instead of expressing high-level security properties of network tunnels such as confidentiality and authentication, these APIs expose low-level details of the SSL protocol to application developers. As a consequence, developers often use SSL APIs incorrectly, misinterpreting and misunderstanding their manifold parameters, options, side effects, and return values."

### Other uses

The Simple Mail Transfer Protocol (SMTP) can also be protected by TLS. These applications use public key certificates to verify the identity of endpoints.

TLS can also be used for tunneling an entire network stack to create a VPN, which is the case with OpenVPN and OpenConnect. Many vendors have by now married TLS's encryption and authentication capabilities with authorization. There has also been substantial development since the late 1990s in creating client technology outside of Web-browsers, in order to enable support for client/server applications. Compared to traditional IPsec VPN technologies, TLS has some inherent advantages in firewall and NAT traversal that make it easier to administer for large remote-access populations.

TLS is also a standard method for protecting Session Initiation Protocol (SIP) application signaling. TLS can be used for providing authentication and encryption of the SIP signaling associated with VoIP and other SIP-based applications.
