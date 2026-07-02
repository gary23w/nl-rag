---
title: "Cipher suite"
source: https://en.wikipedia.org/wiki/Cipher_suite
domain: x509-certificates
license: CC-BY-SA-4.0
tags: x.509 certificate, public key certificate, certificate revocation list, cipher suite
fetched: 2026-07-02
---

# Cipher suite

A **cipher suite** is a set of algorithms that help secure a network connection. Suites typically use Transport Layer Security (TLS) or its deprecated predecessor Secure Socket Layer (SSL) as their protocol. The set of algorithms that cipher suites usually contain include: a key exchange algorithm, a bulk encryption algorithm, and a message authentication code (MAC) algorithm.

The key exchange algorithm is used to exchange a key between two devices. This key is used to encrypt and decrypt the messages being sent between two machines. The bulk encryption algorithm is used to encrypt the data being sent. The MAC algorithm provides data integrity checks to ensure that the data sent does not change in transit. In addition, cipher suites can include signatures and an authentication algorithm to help authenticate the server and or client.

Overall, there are hundreds of different cipher suites that contain different combinations of these algorithms. Some cipher suites offer better security than others. But with the adoption of TLS 1.3, only 5 cipher suites have been officially supported and defined.

The structure and use of the cipher suite concept are defined in the TLS standard document. TLS 1.2 is the most prevalent version of TLS. The newest version of TLS (TLS 1.3) includes additional requirements to cipher suites. Cipher suites defined for TLS 1.2 cannot be used in TLS 1.3, and vice versa, unless otherwise stated in their definition.

A reference list of named cipher suites is provided in the TLS Cipher Suite Registry.

## History

The use of ciphers has been a part of the Secure Socket Layer (SSL) transit protocol since its creation. SSL has been succeeded by TLS for most uses. However, the name *Cipher Suite* was not used in the original draft of SSL. Instead the ability for a client and a server to choose from a small set of ciphers to secure their connection was called *Cipher-Choice.* It was not until SSL v3 (the last version of SSL) that the name *Cipher Suite* was used. Every version of TLS since has used *Cipher Suite* in its standardization. The concept and purpose of a *Cipher Suite* has not changed since the term was first coined. It has and still is used as a structure describing the algorithms that a machine supports in order for two machines to decide which algorithms to use to secure their connection. What has changed is the versions of the algorithms that are supported in the cipher suites. Each version of TLS has added support for stronger versions of the algorithms and removed support for versions of the algorithms that have been identified as insecure.

TLS 1.3 marks a change in how cipher suites are coordinated between machines. The cipher suite chosen for two communicating machines to use is determined by the handshake process. Modifications were done in TLS 1.3 to the handshake process to cut down on the number of messages needed to be sent. This allows for less processing, less packet traffic and more efficiency compared to previous versions of TLS.

## Naming scheme

Each cipher suite has a unique name that is used to identify it and to describe the algorithmic contents of it. Each segment in a cipher suite name stands for a different algorithm or protocol. An example of a cipher suite name: **TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256**

The meaning of this name is:

**TLS**

defines the protocol that this cipher suite is for; it will usually be TLS.

**ECDHE**

indicates the

key exchange algorithm

being used.

**RSA**

authentication mechanism during the handshake.

**AES**

session cipher.

**128**

session encryption

key size

(bits) for cipher.

**GCM**

type of encryption (cipher-block dependency and additional options).

**SHA**

(SHA2)hash function. For a digest of 256 and higher. Signature mechanism. Indicates the

message authentication algorithm

which is used to authenticate a message.

**256**

Digest size (bits).

As of TLS 1.3 cipher suite names no longer include a certificate type (RSA) or key exchange mechanism (ECDHE), as these are negotiated separately in the new version.

## Full handshake: coordinating cipher suites

To use cipher suites, the client and the server must agree on the specific cipher suite that is going to be used in exchanging messages. Both the client and the server must support the agreed upon cipher suite. If the client and server do not agree on a cipher suite, no connection will be made. This selection process occurs during the TLS Handshake Protocol. TLS 1.3 includes a TLS Handshake Protocol that differs compared to past and the current version of TLS/SSL.

After coordinating which cipher suite to use, the server and the client still have the ability to change the coordinated ciphers by using the *ChangeCipherSpec* protocol in the current handshake or in a new handshake.

To test which TLS ciphers a server supports, an SSL/TLS Scanner may be used.

### TLS 1.0–1.2 handshake

This client starts the process by sending a *clientHello* message to the server that includes the version of TLS being used and a cipher suites list in the order of the client's preference. In response, the server sends a *serverHello* message that includes the chosen cipher suite and the session ID. Next the server sends a digital certificate to verify its identity to the client. The server may also request a client's digital certification if needed.

If the client and server are not using pre-shared keys, the client then sends an encrypted message to the server that enables the client and the server to compute which secret key will be used during exchanges.

If the *prefer server cipher* bit of *serverHello* message is set to true, the negotiated cipher suite is preferred on the cipher suites list of *serverHello* message; otherwise, the negotiated cipher suite is preferred on the cipher suites list of *clientHello* message.

After successfully verifying the authentication of the server and, if needed, exchanging the secret key, the client sends a *finished* message to signal that it is done with the handshake process. After receiving this message, the server sends a *finished* message that confirms that the handshake is complete. Now the client and the server are in agreement on which cipher suite to use to communicate with each other.

### TLS 1.3 handshake

If two machines are corresponding over TLS 1.3, they coordinate which cipher suite to use by using the TLS 1.3 Handshake Protocol. The handshake in TLS 1.3 was condensed to only one round trip compared to the two round trips required in previous versions of TLS/SSL.

First the client sends a *clientHello* message to the server that contains a list of supported ciphers in order of the client's preference and makes a guess on what key algorithm is being used so that it can send a secret key to share if needed.

By making a guess on what key algorithm that is being used it eliminates a round trip. After receiving the *clientHello*, the server sends a *serverHello* with its key, a certificate, the chosen cipher suite and the *finished* message.

If the *prefer server cipher* bit of *serverHello* message is set to true, the negotiated cipher suite is preferred on the cipher suites list of *serverHello* message; otherwise, the negotiated cipher suite is preferred on the cipher suites list of *clientHello* message.

After the client receives the server's *finished* message it now is coordinated with the server on which cipher suite to use.

## Supported algorithms

### In TLS 1.0–1.2

| Key exchange/agreement | Authentication | Block/stream ciphers | Message authentication |
|---|---|---|---|
| RSA | RSA | RC4 | Hash-based MD5 |
| Diffie–Hellman | DSA | Triple DES | SHA hash function (SHA-1 and SHA-2) |
| ECDH | ECDSA | AES (128-bits and 256-bits) |   |
| SRP |   | IDEA |   |
| PSK |   | DES |   |
|   |   | Camellia |   |
|   |   | ChaCha20 |   |

For more information about algorithms supported in TLS 1.0–1.2, see also: Transport Layer Security § Applications and adoption

### TLS 1.3

In TLS 1.3, many legacy algorithms that were supported in early versions of TLS have been dropped in an effort to make the protocol more secure. In addition, all encryption and authentication algorithms are combined in the authenticated encryption with associated data (AEAD) encryption algorithm. Also a hash algorithm must now be used in HMAC-based key derivation (HKDF). All non-AEAD ciphers have been removed due to possible weaknesses or vulnerabilities and ciphers must use an ephemeral key exchange algorithm so that new key pairs are generated for every exchange.

## DTLS with cipher suites

Datagram Transport Layer Security (DTLS) is based on TLS, but is specifically used for UDP connections instead of TCP connections. Since DTLS is based on TLS it is able to use a majority of the cipher suites described for TLS. There are special cases that must be considered when using TLS cipher suites with DTLS. DTLS does not support the stream cipher RC4 which means no TLS cipher suite using RC4 can be used with DTLS.

To determine if a TLS cipher suite is compatible with DTLS looking at its name will not help. Each TLS cipher suite will still include the TLS identifier space in its name. e.g.: *TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256*. Instead, all TLS parameter registries now include the flag DTLS-OK to signal if a cipher suite supports DTLS.

## Vulnerabilities

A cipher suite is as secure as the algorithms that it contains. If the version of encryption or authentication algorithm in a cipher suite have known vulnerabilities the cipher suite and TLS connection may then be vulnerable. Therefore, a common attack against TLS and cipher suites is known as a downgrade attack. A downgrade in TLS occurs when a modern client connects to legacy servers that are using older versions of TLS or SSL.

When initiating a handshake, the modern client will offer the highest protocol that it supports. If the connection fails, it will automatically retry again with a lower protocol such as TLS 1.0 or SSL 3.0 until the handshake is successful with the server. The purpose of downgrading is so that new versions of TLS are compatible with older versions. However, it is possible for an adversary to take advantage of this feature and make it so that a client will automatically downgrade to a version of TLS or SSL that supports cipher suites with algorithms that are known for weak security and vulnerabilities. This has resulted in attacks such as POODLE.

One way to avoid this security flaw is to disable the ability of a server or client to be able to downgrade to SSL 3.0. The shortcoming with this fix is that some legacy hardware cannot be accessed by newer hardware. If SSL 3.0 support is needed for legacy hardware, there is an approved TLS_FALLBACK_SCSV cipher suite which verifies that downgrades are not triggered for malicious intentions.

## Cipher suites for constrained devices

Encryption, key exchange and authentication algorithms usually require a large amount of processing power and memory. To provide security to constrained devices with limited processing power, memory, and battery life such as those powering the Internet of things there are specifically chosen cipher suites. Two examples include:

1. TLS_PSK_WITH_AES_128_CCM_8 (pre-shared key)
2. TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8 (**raw** public key)

Each of these cipher suites has been implemented to run on devices with constraints in processing power and memory. They are both implemented in the open-sourced project TinyDTLS. The reason that they are able to work on these constrained devices is because they can be implemented in a light-weight fashion. Implementations of the pre-shared key cipher suite used only 1889 bytes of RAM and 38266 of flash ROM which is very resource-conscious compared to most encryption and security algorithms. This low memory usage is due to these cipher suites using proven efficient algorithms that are secure, but maybe not as secure as more resource-required algorithms; exp: Using 128 bit encryption vs 256 bit encryption. In addition they use pre-shared key or **raw** public key which requires less memory space and processing power compared to using traditional public key infrastructure (PKIX).

## Programming references

In programming, a cipher suite is referred to in both plural and non-plural forms. Each one has different definitions:

**CipherSuite cipher_suites**

a list of the cryptographic options supported by the client.

An example of how

cipher_suites

is usually used during the handshake process:

```mw
   struct {
       ProtocolVersion client_version;
       Random random;
       SessionID session_id;
       CipherSuite cipher_suites<2..2^16-2>;
       CompressionMethod compression_methods<1..2^8-1>;
       select (extensions_present) {
           case false:
               struct {};
           case true:
               Extension extensions<0..2^16-1>;
       };
   } ClientHello;
```

**CipherSuite cipher_suite**

the cipher suite selected by the server from the client's

cipher_suites

.

An example of how

cipher_suite

is usually used during the handshake process:

```mw
      struct {
          ProtocolVersion server_version;
          Random random;
          SessionID session_id;
          CipherSuite cipher_suite;
          CompressionMethod compression_method;
          select (extensions_present) {
              case false:
                  struct {};
              case true:
                  Extension extensions<0..2^16-1>;
          };
      } ServerHello;
```
