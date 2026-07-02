---
title: "Transport Layer Security (part 2/2)"
source: https://en.wikipedia.org/wiki/Transport_Layer_Security
domain: reqwest-rust
license: CC-BY-SA-4.0
tags: reqwest client, rust http client, reqwest requests, reqwest async client
fetched: 2026-07-02
part: 2/2
---

## Security

### Attacks against TLS/SSL

Significant attacks against TLS/SSL are listed below.

In February 2015, IETF issued an informational RFC summarizing the various known attacks against TLS/SSL.

#### Renegotiation attack

A vulnerability of the renegotiation procedure was discovered in August 2009 that can lead to plaintext injection attacks against SSL 3.0 and all current versions of TLS. For example, it allows an attacker who can hijack an https connection to splice their own requests into the beginning of the conversation the client has with the web server. The attacker cannot actually decrypt the client–server communication, so it is different from a typical man-in-the-middle attack. A short-term fix is for web servers to stop allowing renegotiation, which typically will not require other changes unless client certificate authentication is used. To fix the vulnerability, a renegotiation indication extension was proposed for TLS. It will require the client and server to include and verify information about previous handshakes in any renegotiation handshakes. This extension has been implemented by several libraries.

#### Downgrade attacks: FREAK attack and Logjam attack

A protocol downgrade attack (also called a version rollback attack) tricks a web server into negotiating connections with previous versions of TLS (such as SSLv2) that have long since been abandoned as insecure.

Previous modifications to the original protocols, like **False Start** (adopted and enabled by Google Chrome) or **Snap Start**, reportedly introduced limited TLS protocol downgrade attacks or allowed modifications to the cipher suite list sent by the client to the server. In doing so, an attacker might succeed in influencing the cipher suite selection in an attempt to downgrade the cipher suite negotiated to use either a weaker symmetric encryption algorithm or a weaker key exchange. A paper presented at an ACM conference on computer and communications security in 2012 demonstrated that the False Start extension was at risk: in certain circumstances it could allow an attacker to recover the encryption keys offline and to access the encrypted data.

Encryption downgrade attacks can force servers and clients to negotiate a connection using cryptographically weak keys. In 2014, a man-in-the-middle attack called FREAK was discovered affecting the OpenSSL stack, the default Android web browser, and some Safari browsers. The attack involved tricking servers into negotiating a TLS connection using cryptographically weak 512 bit encryption keys.

Logjam is a security exploit discovered in May 2015 that exploits the option of using legacy "export-grade" 512-bit Diffie–Hellman groups dating back to the 1990s. It forces susceptible servers to downgrade to cryptographically weak 512-bit Diffie–Hellman groups. An attacker can then deduce the keys the client and server determine using the Diffie–Hellman key exchange.

#### Cross-protocol attacks: DROWN

The DROWN attack is an exploit that attacks servers supporting contemporary SSL/TLS protocol suites by exploiting their support for the obsolete, insecure, SSLv2 protocol to leverage an attack on connections using up-to-date protocols that would otherwise be secure. DROWN exploits a vulnerability in the protocols used and the configuration of the server, rather than any specific implementation error. Full details of DROWN were announced in March 2016, together with a patch for the exploit. At that time, more than 81,000 of the top 1 million most popular websites were among the TLS protected websites that were vulnerable to the DROWN attack.

#### BEAST attack

On September 23, 2011, researchers Thai Duong and Juliano Rizzo demonstrated a proof of concept called **BEAST** (**Browser Exploit Against SSL/TLS**) using a Java applet to violate same origin policy constraints, for a long-known cipher block chaining (CBC) vulnerability in TLS 1.0: an attacker observing 2 consecutive ciphertext blocks C0, C1 can test if the plaintext block P1 is equal to x by choosing the next plaintext block P2 = x ⊕ C0 ⊕ C1; as per CBC operation, C2 = E(C1 ⊕ P2) = E(C1 ⊕ x ⊕ C0 ⊕ C1) = E(C0 ⊕ x), which will be equal to C1 if x = P1. Practical exploits had not been previously demonstrated for this vulnerability, which was originally discovered by Phillip Rogaway in 2002. The vulnerability of the attack had been fixed with TLS 1.1 in 2006, but TLS 1.1 had not seen wide adoption prior to this attack demonstration.

RC4 as a stream cipher is immune to BEAST attack. Therefore, RC4 was widely used as a way to mitigate BEAST attack on the server side. However, in 2013, researchers found more weaknesses in RC4. Thereafter enabling RC4 on server side was no longer recommended.

Chrome and Firefox themselves are not vulnerable to BEAST attack, however, Mozilla updated their NSS libraries to mitigate BEAST-like attacks. NSS is used by Mozilla Firefox and Google Chrome to implement SSL. Some web servers that have a broken implementation of the SSL specification may stop working as a result.

Microsoft released Security Bulletin MS12-006 on January 10, 2012, which fixed the BEAST vulnerability by changing the way that the Windows Secure Channel (Schannel) component transmits encrypted network packets from the server end. Users of Internet Explorer (prior to version 11) that run on older versions of Windows (Windows 7, Windows 8 and Windows Server 2008 R2) can restrict use of TLS to 1.1 or higher.

Apple mitigated the BEAST vulnerability by implementing a 1/n-1 split and turning it on by default in OS X Mavericks, released on October 22, 2013.

#### CRIME and BREACH attacks

The authors of the BEAST attack are also the creators of the later CRIME attack, which can allow an attacker to recover the content of web cookies when data compression is used along with TLS. When used to recover the content of secret authentication cookies, it allows an attacker to perform session hijacking on an authenticated web session.

While the CRIME attack was presented as a general attack that could work effectively against a large number of protocols, including but not limited to TLS, and application-layer protocols such as SPDY or HTTP, only exploits against TLS and SPDY were demonstrated and largely mitigated in browsers and servers. The CRIME exploit against HTTP compression has not been mitigated at all, even though the authors of CRIME have warned that this vulnerability might be even more widespread than SPDY and TLS compression combined. In 2013 a new instance of the CRIME attack against HTTP compression, dubbed BREACH, was announced. Based on the CRIME attack a BREACH attack can extract login tokens, email addresses or other sensitive information from TLS encrypted web traffic in as little as 30 seconds (depending on the number of bytes to be extracted), provided the attacker tricks the victim into visiting a malicious web link or is able to inject content into valid pages the user is visiting (ex: a wireless network under the control of the attacker). All versions of TLS and SSL are at risk from BREACH regardless of the encryption algorithm or cipher used. Unlike previous instances of CRIME, which can be successfully defended against by turning off TLS compression or SPDY header compression, BREACH exploits HTTP compression which cannot realistically be turned off, as virtually all web servers rely upon it to improve data transmission speeds for users. This is a known limitation of TLS as it is susceptible to chosen-plaintext attack against the application-layer data it was meant to protect.

#### Timing attacks on padding

Earlier TLS versions were vulnerable against the padding oracle attack discovered in 2002. A novel variant, called the Lucky Thirteen attack, was published in 2013.

Some experts also recommended avoiding triple DES CBC. Since the last supported ciphers developed to support any program using Windows XP's SSL/TLS library like Internet Explorer on Windows XP are RC4 and Triple-DES, and since RC4 is now deprecated (see discussion of RC4 attacks), this makes it difficult to support any version of SSL for any program using this library on XP.

A fix was released in 2014 as the Encrypt-then-MAC extension to the TLS specification. The Lucky Thirteen attack can be mitigated in TLS 1.2 by using only AES_GCM ciphers; AES_CBC remains vulnerable. SSL may safeguard email, VoIP, and other types of communications over insecure networks in addition to its primary use case of secure data transmission between a client and the server.

#### POODLE attack

On October 14, 2014, Google researchers published a vulnerability in the design of SSL 3.0, which makes CBC mode of operation with SSL 3.0 vulnerable to a padding attack (CVE-2014-3566). They named this attack **POODLE** (**Padding Oracle On Downgraded Legacy Encryption**). On average, attackers only need to make 256 SSL 3.0 requests to reveal one byte of encrypted messages.

Although this vulnerability only exists in SSL 3.0 and most clients and servers support TLS 1.0 and above, all major browsers voluntarily downgrade to SSL 3.0 if the handshakes with newer versions of TLS fail unless they provide the option for a user or administrator to disable SSL 3.0 and the user or administrator does so. Therefore, the man-in-the-middle can first conduct a version rollback attack and then exploit this vulnerability.

On December 8, 2014, a variant of POODLE was announced that impacts TLS implementations that do not properly enforce padding byte requirements.

#### RC4 attacks

Despite the existence of attacks on RC4 that broke its security, cipher suites in SSL and TLS that were based on RC4 were still considered secure prior to 2013 based on the way in which they were used in SSL and TLS. In 2011, the RC4 suite was actually recommended as a workaround for the BEAST attack. New forms of attack disclosed in March 2013 conclusively demonstrated the feasibility of breaking RC4 in TLS, suggesting it was not a good workaround for BEAST. An attack scenario was proposed by AlFardan, Bernstein, Paterson, Poettering and Schuldt that used newly discovered statistical biases in the RC4 key table to recover parts of the plaintext with a large number of TLS encryptions. An attack on RC4 in TLS and SSL that requires 13 × 220 encryptions to break RC4 was unveiled on 8 July 2013 and later described as "feasible" in the accompanying presentation at a USENIX Security Symposium in August 2013. In July 2015, subsequent improvements in the attack make it increasingly practical to defeat the security of RC4-encrypted TLS.

As many modern browsers have been designed to defeat BEAST attacks (except Safari for Mac OS X 10.7 or earlier, for iOS 6 or earlier, and for Windows; see § Web browsers), RC4 is no longer a good choice for TLS 1.0. The CBC ciphers which were affected by the BEAST attack in the past have become a more popular choice for protection. Mozilla and Microsoft recommend disabling RC4 where possible. In February 2015, the use of RC4 cipher suites was officially prohibited in all versions of TLS.

On September 1, 2015, Microsoft, Google, and Mozilla announced that RC4 cipher suites would be disabled by default in their browsers (Microsoft Edge [Legacy], Internet Explorer 11 on Windows 7/8.1/10, Firefox, and Chrome) in early 2016.

#### Truncation attack

A TLS (logout) truncation attack blocks a victim's account logout requests so that the user unknowingly remains logged into a web service. When the request to sign out is sent, the attacker injects an unencrypted TCP FIN message (no more data from sender) to close the connection. The server therefore does not receive the logout request and is unaware of the abnormal termination.

Published in July 2013, the attack causes web services such as Gmail and Hotmail to display a page that informs the user that they have successfully signed-out, while ensuring that the user's browser maintains authorization with the service, allowing an attacker with subsequent access to the browser to access and take over control of the user's logged-in account. The attack does not rely on installing malware on the victim's computer; attackers need only place themselves between the victim and the web server (e.g., by setting up a rogue wireless hotspot). This vulnerability also requires access to the victim's computer. Another possibility is when using FTP the data connection can have a false FIN in the data stream, and if the protocol rules for exchanging close_notify alerts is not adhered to a file can be truncated.

#### Plaintext attack against DTLS

In February 2013 two researchers from Royal Holloway, University of London discovered a timing attack which allowed them to recover (parts of the) plaintext from a DTLS connection using the OpenSSL or GnuTLS implementation of DTLS when Cipher Block Chaining mode encryption was used.

#### Unholy PAC attack

This attack, discovered in mid-2016, exploits weaknesses in the Web Proxy Autodiscovery Protocol (WPAD) to expose the URL that a web user is attempting to reach via a TLS-enabled web link. Disclosure of a URL can violate a user's privacy, not only because of the website accessed, but also because URLs are sometimes used to authenticate users. Document sharing services, such as those offered by Google and Dropbox, also work by sending a user a security token that is included in the URL. An attacker who obtains such URLs may be able to gain full access to a victim's account or data.

The exploit works against almost all browsers and operating systems.

#### Sweet32 attack

The Sweet32 attack breaks all 64-bit block ciphers used in CBC mode as used in TLS by exploiting a birthday attack and either a man-in-the-middle attack or injection of a malicious JavaScript into a web page. The purpose of the man-in-the-middle attack or the JavaScript injection is to allow the attacker to capture enough traffic to mount a birthday attack.

#### Implementation errors: Heartbleed bug, BERserk attack, Cloudflare bug

The Heartbleed bug is a serious vulnerability specific to the implementation of SSL/TLS in the popular OpenSSL cryptographic software library, affecting versions 1.0.1 to 1.0.1f. This weakness, reported in April 2014, allows attackers to extract private keys from servers that should normally be protected. The Heartbleed bug allows anyone on the Internet to read the memory of the systems protected by the vulnerable versions of the OpenSSL software. This compromises the secret private keys associated with the public certificates used to identify the service providers and to encrypt the traffic, the names and passwords of the users and the actual content. This allows attackers to eavesdrop on communications, extract data directly from the services and users and to impersonate services and users. The vulnerability is caused by a buffer over-read bug in the OpenSSL software, rather than a defect in the SSL or TLS protocol specification.

In September 2014, a variant of Daniel Bleichenbacher's PKCS#1 v1.5 RSA Signature Forgery vulnerability was announced by Intel Security Advanced Threat Research. This attack, dubbed BERserk, is a result of incomplete ASN.1 length decoding of public key signatures in some SSL implementations, and allows a man-in-the-middle attack by forging a public key signature.

In February 2015, after media reported the hidden pre-installation of superfish adware on some Lenovo notebooks, a researcher found a trusted root certificate on affected Lenovo machines to be insecure, as the keys could easily be accessed using the company name, Komodia, as a passphrase. The Komodia library was designed to intercept client-side TLS/SSL traffic for parental control and surveillance, but it was also used in numerous adware programs, including Superfish, that were often surreptitiously installed unbeknownst to the computer user. In turn, these potentially unwanted programs installed the corrupt root certificate, allowing attackers to completely control web traffic and confirm false websites as authentic.

In May 2016, it was reported that dozens of Danish HTTPS-protected websites belonging to Visa Inc. were vulnerable to attacks allowing hackers to inject malicious code and forged content into the browsers of visitors. The attacks worked because the TLS implementation used on the affected servers incorrectly reused random numbers (nonces) that are intended to be used only once, ensuring that each TLS handshake is unique.

In February 2017, an implementation error caused by a single mistyped character in code used to parse HTML created a buffer overflow error on Cloudflare servers. Similar in its effects to the Heartbleed bug discovered in 2014, this overflow error, widely known as Cloudbleed, allowed unauthorized third parties to read data in the memory of programs running on the servers—data that should otherwise have been protected by TLS.

As of June 2025, the Trustworthy Internet Movement estimated the ratio of websites that are vulnerable to TLS attacks.

| Attacks | Security |   |   |   |
|---|---|---|---|---|
| Insecure | Depends | Secure | Other |   |
| Renegotiation attack | < 0.1% support insecure renegotiation | < 0.1% support both | 99.8% support secure renegotiation | 0.1% no support |
| RC4 attacks | 0.1% support RC4 suites used with modern browsers | 2.1% support some RC4 suites | 97.8% no support | —N/a |
| TLS Compression (CRIME attack) | 0% vulnerable | —N/a | —N/a | —N/a |
| Heartbleed | 0% vulnerable | —N/a | —N/a | —N/a |
| ChangeCipherSpec injection attack | < 0.1% vulnerable and exploitable | < 0.1% vulnerable, not exploitable | 99.6% not vulnerable | 0.3% unknown |
| POODLE attack against TLS (Original POODLE against SSL 3.0 is not included) | < 0.1% vulnerable and exploitable | —N/a | 99.9% not vulnerable | 0.1% unknown |
| Protocol downgrade | 3.5% Downgrade defence not supported | —N/a | 82.3% Downgrade defence supported | 14.2% unknown |

### Forward secrecy

Forward secrecy is a property of cryptographic systems which ensures that a session key derived from a set of public and private keys will not be compromised if one of the private keys is compromised in the future. Without forward secrecy, if the server's private key is compromised, not only will all future TLS-encrypted sessions using that server certificate be compromised, but also any past sessions that used it as well (provided that these past sessions were intercepted and stored at the time of transmission). An implementation of TLS can provide forward secrecy by requiring the use of ephemeral Diffie–Hellman key exchange to establish session keys, and some notable TLS implementations do so exclusively: e.g., Gmail and other Google HTTPS services that use OpenSSL. However, many clients and servers supporting TLS (including browsers and web servers) are not configured to implement such restrictions. In practice, unless a web service uses Diffie–Hellman key exchange to implement forward secrecy, all of the encrypted web traffic to and from that service can be decrypted by a third party if it obtains the server's master (private) key; e.g., by means of a court order.

Even where Diffie–Hellman key exchange is implemented, server-side session management mechanisms can impact forward secrecy. The use of TLS session tickets (a TLS extension) causes the session to be protected by AES128-CBC-SHA256 regardless of any other negotiated TLS parameters, including forward secrecy ciphersuites, and the long-lived TLS session ticket keys defeat the attempt to implement forward secrecy. Stanford University research in 2014 also found that of 473,802 TLS servers surveyed, 82.9% of the servers deploying ephemeral Diffie–Hellman (DHE) key exchange to support forward secrecy were using weak Diffie–Hellman parameters. These weak parameter choices could potentially compromise the effectiveness of the forward secrecy that the servers sought to provide.

Since late 2011, Google has provided forward secrecy with TLS by default to users of its Gmail service, along with Google Docs and encrypted search, among other services. Since November 2013, Twitter has provided forward secrecy with TLS to users of its service. As of August 2019, about 80% of TLS-enabled websites are configured to use cipher suites that provide forward secrecy to most web browsers.

### TLS interception

TLS interception (or HTTPS interception if applied particularly to that protocol) is the practice of intercepting an encrypted data stream in order to decrypt it, read and possibly manipulate it, and then re-encrypt it and send the data on its way again. This is done by way of a "transparent proxy": the interception software terminates the incoming TLS connection, inspects the HTTP plaintext, and then creates a new TLS connection to the destination.

TLS/HTTPS interception is used as an information security measure by network operators in order to be able to scan for and protect against the intrusion of malicious content into the network, such as computer viruses and other malware. Such content could otherwise not be detected as long as it is protected by encryption, which is increasingly the case as a result of the routine use of HTTPS and other secure protocols.

A significant drawback of TLS/HTTPS interception is that it introduces new security risks of its own. One notable limitation is that it provides a point where network traffic is available unencrypted thus giving attackers an incentive to attack this point in particular in order to gain access to otherwise secure content. The interception also allows the network operator, or persons who gain access to its interception system, to perform man-in-the-middle attacks against network users. A 2017 study found that "HTTPS interception has become startlingly widespread, and that interception products as a class have a dramatically negative impact on connection security".


## Protocol details

The TLS protocol exchanges *records*, which encapsulate the data to be exchanged in a specific format (see below). Each record can be compressed, padded, appended with a message authentication code (MAC), or encrypted, all depending on the state of the connection. Each record has a *content type* field that designates the type of data encapsulated, a length field and a TLS version field. The data encapsulated may be control or procedural messages of the TLS itself, or simply the application data needed to be transferred by TLS. The specifications (cipher suite, keys etc.) required to exchange application data by TLS, are agreed upon in the "TLS handshake" between the client requesting the data and the server responding to requests. The protocol therefore defines both the structure of payloads transferred in TLS and the procedure to establish and monitor the transfer.

### TLS handshake

When the connection starts, the record encapsulates a "control" protocol – the handshake messaging protocol (*content type* 22). This protocol is used to exchange all the information required by both sides for the exchange of the actual application data by TLS. It defines the format of messages and the order of their exchange. These may vary according to the demands of the client and server – i.e., there are several possible procedures to set up the connection. This initial exchange results in a successful TLS connection (both parties ready to transfer application data with TLS) or an alert message (as specified below).

#### Basic TLS handshake

A typical connection example follows, illustrating a handshake where the server (but not the client) is authenticated by its certificate:

1. Negotiation phase:
  - A client sends a **ClientHello** message specifying the highest TLS protocol version it supports, a random number, a list of suggested cipher suites and suggested compression methods. If the client is attempting to perform a resumed handshake, it may send a *session ID*. If the client can use Application-Layer Protocol Negotiation, it may include a list of supported application protocols, such as HTTP/2.
  - The server responds with a **ServerHello** message, containing the chosen protocol version, a random number, cipher suite and compression method from the choices offered by the client. To confirm or allow resumed handshakes the server may send a *session ID*. The chosen protocol version should be the highest that both the client and server support. For example, if the client supports TLS version 1.1 and the server supports version 1.2, version 1.1 should be selected; version 1.2 should not be selected.
  - The server sends its **Certificate** message (depending on the selected cipher suite, this may be omitted by the server).
  - The server sends its **ServerKeyExchange** message (depending on the selected cipher suite, this may be omitted by the server). This message is sent for all DHE, ECDHE and DH_anon cipher suites.
  - The server sends a **ServerHelloDone** message, indicating it is done with handshake negotiation.
  - The client responds with a **ClientKeyExchange** message, which may contain a *PreMasterSecret*, public key, or nothing. (Again, this depends on the selected cipher.) This *PreMasterSecret* is encrypted using the public key of the server certificate.
  - The client and server then use the random numbers and *PreMasterSecret* to compute a common secret, called the "master secret". All other key data (session keys such as IV, symmetric encryption key, MAC key) for this connection is derived from this master secret (and the client- and server-generated random values), which is passed through a carefully designed pseudorandom function.
2. The client now sends a **ChangeCipherSpec** record, essentially telling the server, "Everything I tell you from now on will be authenticated (and encrypted if encryption parameters were present in the server certificate)." The ChangeCipherSpec is itself a record-level protocol with content type of 20.
  - The client sends an authenticated and encrypted **Finished** message, containing a hash and MAC over the previous handshake messages.
  - The server will attempt to decrypt the client's *Finished* message and verify the hash and MAC. If the decryption or verification fails, the handshake is considered to have failed and the connection should be terminated.
3. Finally, the server sends a **ChangeCipherSpec**, telling the client, "Everything I tell you from now on will be authenticated (and encrypted, if encryption was negotiated)."
  - The server sends its authenticated and encrypted **Finished** message.
  - The client performs the same decryption and verification procedure as the server did in the previous step.
4. Application phase: at this point, the "handshake" is complete and the application protocol is enabled, with content type of 23. Application messages exchanged between client and server will also be authenticated and optionally encrypted exactly like in their *Finished* message. Otherwise, the content type will return 25 and the client will not authenticate.

#### Client-authenticated TLS handshake

The following *full* example shows a client being authenticated (in addition to the server as in the example above; see mutual authentication) via TLS using certificates exchanged between both peers.

1. Negotiation Phase:
  - A client sends a **ClientHello** message specifying the highest TLS protocol version it supports, a random number, a list of suggested cipher suites and compression methods.
  - The server responds with a **ServerHello** message, containing the chosen protocol version, a random number, cipher suite and compression method from the choices offered by the client. The server may also send a *session id* as part of the message to perform a resumed handshake.
  - The server sends its **Certificate** message (depending on the selected cipher suite, this may be omitted by the server).
  - The server sends its **ServerKeyExchange** message (depending on the selected cipher suite, this may be omitted by the server). This message is sent for all DHE, ECDHE and DH_anon ciphersuites.[1]
  - The server sends a **CertificateRequest** message, to request a certificate from the client.
  - The server sends a **ServerHelloDone** message, indicating it is done with handshake negotiation.
  - The client responds with a **Certificate** message, which contains the client's certificate, but not its private key.
  - The client sends a **ClientKeyExchange** message, which may contain a *PreMasterSecret*, public key, or nothing. (Again, this depends on the selected cipher.) This *PreMasterSecret* is encrypted using the public key of the server certificate.
  - The client sends a **CertificateVerify** message, which is a signature over the previous handshake messages using the client's certificate's private key. This signature can be verified by using the client's certificate's public key. This lets the server know that the client has access to the private key of the certificate and thus owns the certificate.
  - The client and server then use the random numbers and *PreMasterSecret* to compute a common secret, called the "master secret". All other key data ("session keys") for this connection is derived from this master secret (and the client- and server-generated random values), which is passed through a carefully designed pseudorandom function.
2. The client now sends a **ChangeCipherSpec** record, essentially telling the server, "Everything I tell you from now on will be authenticated (and encrypted if encryption was negotiated). "The ChangeCipherSpec is itself a record-level protocol and has type 20 and not 22.
  - Finally, the client sends an encrypted **Finished** message, containing a hash and MAC over the previous handshake messages.
  - The server will attempt to decrypt the client's *Finished* message and verify the hash and MAC. If the decryption or verification fails, the handshake is considered to have failed and the connection should be torn down.
3. Finally, the server sends a **ChangeCipherSpec**, telling the client, "Everything I tell you from now on will be authenticated (and encrypted if encryption was negotiated)."
  - The server sends its own encrypted **Finished** message.
  - The client performs the same decryption and verification procedure as the server did in the previous step.
4. Application phase: at this point, the "handshake" is complete and the application protocol is enabled, with content type of 23. Application messages exchanged between client and server will also be encrypted exactly like in their *Finished* message.

#### Resumed TLS handshake

Public key operations (e.g., RSA) are relatively expensive in terms of computational power. TLS provides a secure shortcut in the handshake mechanism to avoid these operations: resumed sessions. Resumed sessions are implemented using session IDs or session tickets.

Apart from the performance benefit, resumed sessions can also be used for single sign-on, as it guarantees that both the original session and any resumed session originate from the same client. This is of particular importance for the FTP over TLS/SSL protocol, which would otherwise suffer from a man-in-the-middle attack in which an attacker could intercept the contents of the secondary data connections.

#### TLS 1.3 handshake

The TLS 1.3 handshake was condensed to only one round trip compared to the two round trips required in previous versions of TLS/SSL.

To start the handshake, the client guesses which key exchange algorithm will be selected by the server and sends a **ClientHello** message to the server containing a list of supported ciphers (in order of the client's preference) and public keys for some or all of its key exchange guesses. If the client successfully guesses the key exchange algorithm, 1 round trip is eliminated from the handshake. After receiving the **ClientHello**, the server selects a cipher and sends back a **ServerHello** with its own public key, followed by server **Certificate** and **Finished** messages.

After the client receives the server's finished message, it now is coordinated with the server on which cipher suite to use.

##### Session IDs

In an ordinary *full* handshake, the server sends a *session id* as part of the **ServerHello** message. The client associates this *session id* with the server's IP address and TCP port, so that when the client connects again to that server, it can use the *session id* to shortcut the handshake. In the server, the *session id* maps to the cryptographic parameters previously negotiated, specifically the "master secret". Both sides must have the same "master secret" or the resumed handshake will fail (this prevents an eavesdropper from using a *session id*). The random data in the **ClientHello** and **ServerHello** messages virtually guarantee that the generated connection keys will be different from in the previous connection. In the RFCs, this type of handshake is called an *abbreviated* handshake. It is also described in the literature as a *restart* handshake.

1. Negotiation phase:
  - A client sends a **ClientHello** message specifying the highest TLS protocol version it supports, a random number, a list of suggested cipher suites and compression methods. Included in the message is the *session id* from the previous TLS connection.
  - The server responds with a **ServerHello** message, containing the chosen protocol version, a random number, cipher suite and compression method from the choices offered by the client. If the server recognizes the *session id* sent by the client, it responds with the same *session id*. The client uses this to recognize that a resumed handshake is being performed. If the server does not recognize the *session id* sent by the client, it sends a different value for its *session id*. This tells the client that a resumed handshake will not be performed. At this point, both the client and server have the "master secret" and random data to generate the key data to be used for this connection.
2. The server now sends a **ChangeCipherSpec** record, essentially telling the client, "Everything I tell you from now on will be encrypted." The ChangeCipherSpec is itself a record-level protocol and has type 20 and not 22.
  - Finally, the server sends an encrypted **Finished** message, containing a hash and MAC over the previous handshake messages.
  - The client will attempt to decrypt the server's *Finished* message and verify the hash and MAC. If the decryption or verification fails, the handshake is considered to have failed and the connection should be torn down.
3. Finally, the client sends a **ChangeCipherSpec**, telling the server, "Everything I tell you from now on will be encrypted."
  - The client sends its own encrypted **Finished** message.
  - The server performs the same decryption and verification procedure as the client did in the previous step.
4. Application phase: at this point, the "handshake" is complete and the application protocol is enabled, with content type of 23. Application messages exchanged between client and server will also be encrypted exactly like in their *Finished* message.

##### Session tickets

Instead of session IDs, TLS can also be extended via use of session tickets. It defines a way to resume a TLS session without requiring that session-specific state is stored at the TLS server.

When using session tickets, the TLS server stores its session-specific state in a session ticket and sends the session ticket to the TLS client for storing. The client resumes a TLS session by sending the session ticket to the server, and the server resumes the TLS session according to the session-specific state in the ticket. The session ticket is encrypted and authenticated by the server, and the server verifies its validity before using its contents.

One particular weakness of this method with OpenSSL is that it always limits encryption and authentication security of the transmitted TLS session ticket to `AES128-CBC-SHA256`, no matter what other TLS parameters were negotiated for the actual TLS session. This means that the state information (the TLS session ticket) is not as well protected as the TLS session itself. Of particular concern is OpenSSL's storage of the keys in an application-wide context (`SSL_CTX`), i.e. for the life of the application, and not allowing for re-keying of the `AES128-CBC-SHA256` TLS session tickets without resetting the application-wide OpenSSL context (which is uncommon, error-prone and often requires manual administrative intervention).

### TLS record

This is the general format of all TLS records.

General TLS record format

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

Content Type

Legacy version (major/minor)

Length

↴

4

32

↪

Length (cont.)

8

64

Protocol message(s)

12

96

⋮

⋮

⁠

$5+m$

⁠

⁠

$40+m*8$

⁠

Message Authentication Code

(optional)

⋮

⋮

⋮

⋮

⁠

$5+m+q$

⁠

⁠

$40+(m+q)*8$

⁠

Padding (block ciphers only)

**Content Type: 8 bits**

This field identifies the Record Layer Protocol Type contained in this record.

| Hex | Dec | Type |
|---|---|---|
| 0x14 | 20 | ChangeCipherSpec |
| 0x15 | 21 | Alert |
| 0x16 | 22 | Handshake |
| 0x17 | 23 | Application |
| 0x18 | 24 | Heartbeat |

**Legacy version: 16 bits**

This field identifies the major and minor version of TLS prior to TLS 1.3 for the contained message. For a

ClientHello

message, this need not be the

highest

version supported by the client. For TLS 1.3 and later, this must be set to

0x0303

and application must send supported versions in an extra message extension block.

| Major version | Minor version | Version type |
|---|---|---|
| 3 | 0 | SSL 3.0 |
| 3 | 1 | TLS 1.0 |
| 3 | 2 | TLS 1.1 |
| 3 | 3 | TLS 1.2 |
| 3 | 4 | TLS 1.3 |

**Length: 16 bits; Length < 214**

The length of

Protocol message(s)

,

MAC

and

Padding

fields combined. The length should not exceed 2

14

bytes (16 KiB).

**Protocol message(s): variable**

One or more messages identified by the Protocol field. Note that this field may be encrypted depending on the state of the connection. The length (in bytes) of all messages is indicated by the letter

m

.

**Message Authentication Code (MAC): 16, 20, or 32 bytes (optional)**

A

message authentication code

computed over the

Protocol message(s)

field, with additional key material included. 32 bytes for the

SHA-256

-based HMAC, 20 bytes for the

SHA-1

-based HMAC, 16 bytes for the

MD5

-based HMAC. Note that this field may be encrypted, or not included entirely, depending on the state of the connection. The length (in bytes) of the MAC is indicated by the letter

q

.

**Padding: variable (optional)**

Padding is only added when needed.

No *MAC* or *Padding* fields can be present at end of TLS records before all cipher algorithms and parameters have been negotiated and handshaked and then confirmed by sending a **CipherStateChange** record (see below) for signalling that these parameters will take effect in all further records sent by the same peer.

#### Handshake protocol

Most messages exchanged during the setup of the TLS session are based on this record, unless an error or warning occurs and needs to be signaled by an Alert protocol record (see below), or the encryption mode of the session is modified by another record (see **ChangeCipherSpec** protocol below).

Handshake TLS record format

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

Content Type

(22)

Legacy version (major/minor)

Length

↴

4

32

↪

Length (cont.)

Message Type

Handshake Message Data Length

↴

8

64

↪

Handshake Length (cont.)

12

96

Handshake Message

16

128

⋮

⋮

⋮

⋮

Handshake Message Data Length

⋮

⋮

Handshake Message

⋮

⋮

⋮

⋮

**Content Type: 8 bits; == 22**

This field indicates the

Handshake

Protocol Type.

**Message Type: 8 bits**

This field identifies the handshake message type.

| Code | Description |
|---|---|
| 0 | HelloRequest |
| 1 | ClientHello |
| 2 | ServerHello |
| 4 | NewSessionTicket |
| 8 | EncryptedExtensions (TLS 1.3 only) |
| 11 | Certificate |
| 12 | ServerKeyExchange |
| 13 | CertificateRequest |
| 14 | ServerHelloDone |
| 15 | CertificateVerify |
| 16 | ClientKeyExchange |
| 20 | Finished |

**Handshake Message Data Length: 24 bits**

This is a 3-byte field indicating the length of the handshake data, not including the header.

**Handshake Message: variable**

Data of the handshake message itself.

Note that multiple handshake messages may be combined within one record.

#### Alert protocol

This record should normally not be sent during normal handshaking or application exchanges. However, this message can be sent at any time during the handshake and up to the closure of the session. If this is used to signal a fatal error, the session will be closed immediately after sending this record, so this record is used to give a reason for this closure. If the alert level is flagged as a warning, the remote can decide to close the session if it decides that the session is not reliable enough for its needs (before doing so, the remote may also send its own signal).

Alert TLS record format

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

Content Type

(21)

Legacy version (major/minor)

Length

(2)

↴

4

32

↪

Length (cont.)

Level

Description

8

64

MAC (optional)

12

96

⋮

⋮

⋮

⋮

Padding (block ciphers only)

**Content Type: 8 bits; == 21**

This field indicates the

Alert

Protocol Type.

**Length: 16 bits; == 2**

The length of the rest of fields, which is 2.

**Level: 8 bits**

This field identifies the level of alert. If the level is fatal, the sender should close the session immediately. Otherwise, the recipient may decide to terminate the session itself, by sending its own fatal alert and closing the session itself immediately after sending it. The use of Alert records is optional, however if it is missing before the session closure, the session may be resumed automatically (with its handshakes).

Normal closure of a session after termination of the transported application should preferably be alerted with at least the

Close notify

Alert type (with a simple warning level) to prevent such automatic resume of a new session. Signalling explicitly the normal closure of a secure session before effectively closing its transport layer is useful to prevent or detect attacks (like attempts to truncate the securely transported data, if it intrinsically does not have a predetermined length or duration that the recipient of the secured data may expect).

| Code | Level type | Connection state |
|---|---|---|
| 1 | **warning** | connection or security may be unstable. |
| 2 | **fatal** | connection or security may be compromised, or an unrecoverable error has occurred. |

**Description: 8 bits**

This field identifies which type of alert is being sent.

| Code | Description | Level types | Note |
|---|---|---|---|
| 0 | Close notify | **warning**/**fatal** |   |
| 10 | Unexpected message | **fatal** |   |
| 20 | Bad record MAC | **fatal** | Possibly a bad SSL implementation, or payload has been tampered with e.g. FTP firewall rule on FTPS server. |
| 21 | Decryption failed | **fatal** | TLS only, reserved |
| 22 | Record overflow | **fatal** | TLS only |
| 30 | Decompression failure | **fatal** |   |
| 40 | Handshake failure | **fatal** |   |
| 41 | No certificate | **warning**/**fatal** | SSL 3.0 only, reserved |
| 42 | Bad certificate | **warning**/**fatal** |   |
| 43 | Unsupported certificate | **warning**/**fatal** | e.g. certificate has only server authentication usage enabled and is presented as a client certificate |
| 44 | Certificate revoked | **warning**/**fatal** |   |
| 45 | Certificate expired | **warning**/**fatal** | Check server certificate expire also check no certificate in the chain presented has expired |
| 46 | Certificate unknown | **warning**/**fatal** |   |
| 47 | Illegal parameter | **fatal** |   |
| 48 | Unknown CA (Certificate authority) | **fatal** | TLS only |
| 49 | Access denied | **fatal** | TLS only – e.g. no client certificate has been presented (TLS: Blank certificate message or SSLv3: No Certificate alert), but server is configured to require one. |
| 50 | Decode error | **fatal** | TLS only |
| 51 | Decrypt error | **warning**/**fatal** | TLS only |
| 60 | Export restriction | **fatal** | TLS only, reserved |
| 70 | Protocol version | **fatal** | TLS only |
| 71 | Insufficient security | **fatal** | TLS only |
| 80 | Internal error | **fatal** | TLS only |
| 86 | Inappropriate fallback | **fatal** | TLS only |
| 90 | User canceled | **fatal** | TLS only |
| 100 | No renegotiation | **warning** | TLS only |
| 110 | Unsupported extension | **warning** | TLS only |
| 111 | Certificate unobtainable | **warning** | TLS only |
| 112 | Unrecognized name | **warning**/**fatal** | TLS only; client's Server Name Indicator specified a hostname not supported by the server |
| 113 | Bad certificate status response | **fatal** | TLS only |
| 114 | Bad certificate hash value | **fatal** | TLS only |
| 115 | Unknown PSK identity | **fatal** | TLS only. Used in TLS-PSK and TLS-SRP. |
| 116 | Certificate required | **fatal** | TLS version 1.3 only |
| 120 or 255 | No application protocol | **fatal** | TLS version 1.3 only |

#### ChangeCipherSpec protocol

ChangeCipherSpec TLS record format

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

Content Type

(20)

Legacy version (major/minor)

Length

(1)

↴

4

32

↪

Length (cont.)

CCS Protocol Type

**Content Type: 8 bits; == 20**

This field indicates the

ChangeCipherSpec

Protocol Type.

**Length: 16 bits; == 1**

The length of the rest of fields, which is 1.

**CCS Protocol Type: 8 bits**

This field identifies the CCS Protocol type. There is currently only one.

#### Application protocol

Application TLS record format

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

Content Type

(23)

Legacy version (major/minor)

Length

↴

4

32

↪

Length (cont.)

8

64

Application Data

12

96

⋮

⋮

⁠

$5+m$

⁠

⁠

$40+m*8$

⁠

Message Authentication Code

(optional)

⋮

⋮

⋮

⋮

⁠

$5+m+q$

⁠

⁠

$40+(m+q)*8$

⁠

Padding (block ciphers only)

**Content Type: 8 bits; == 23**

This field identifies the

Application

Protocol Type.

**Length: 16 bits; Length < 214**

The length of

Application Data

,

MAC

and

Padding

fields combined. The length should not exceed 2

14

bytes (16 KiB).

**Application Data: variable**

Data of the application. The length (in bytes) of the data is indicated by the letter

m

.

**Message Authentication Code (MAC): 16, 20, or 32 bytes (optional)**

A

message authentication code

computed over the

Application Data

field. 32 bytes for the

SHA-256

-based HMAC, 20 bytes for the

SHA-1

-based HMAC, 16 bytes for the

MD5

-based HMAC. The length (in bytes) of the MAC is indicated by the letter

q

.

**Padding: variable (optional)**

The last byte contains the padding length.

## Support for name-based virtual servers

From the application protocol point of view, TLS belongs to a lower layer, although the TCP/IP model is too coarse to show it. This means that the TLS handshake is usually (except in the STARTTLS case) performed before the application protocol can start. In the name-based virtual server feature being provided by the application layer, all co-hosted virtual servers share the same certificate because the server has to select and send a certificate immediately after the ClientHello message. This is a big problem in hosting environments because it means either sharing the same certificate among all customers or using a different IP address for each of them.

There are two known workarounds provided by X.509:

- If all virtual servers belong to the same domain, a wildcard certificate can be used. Besides the loose host name selection that might be a problem or not, there is no common agreement about how to match wildcard certificates. Different rules are applied depending on the application protocol or software used.
- Add every virtual host name in the subjectAltName extension. The major problem being that the certificate needs to be reissued whenever a new virtual server is added.

To provide the server name, Transport Layer Security (TLS) Extensions allow clients to include a Server Name Indication extension (SNI) in the extended ClientHello message. This extension hints to the server immediately which name the client wishes to connect to, so the server can select the appropriate certificate to send to the clients.

There is also a method to implement name-based virtual hosting by upgrading HTTP to TLS via an HTTP/1.1 Upgrade header. Normally this is to securely implement HTTP over TLS within the main "http" URI scheme instead of the commonly used "https" scheme. This would avoid forking the URI space and reduces the number of used ports, however, few implementations currently support this.
