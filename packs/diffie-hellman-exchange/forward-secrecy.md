---
title: "Forward secrecy"
source: https://en.wikipedia.org/wiki/Forward_secrecy
domain: diffie-hellman-exchange
license: CC-BY-SA-4.0
tags: diffie hellman key exchange, discrete logarithm, elliptic curve diffie hellman, forward secrecy
fetched: 2026-07-02
---

# Forward secrecy

In cryptography, **forward secrecy** (**FS**), also known as **perfect forward secrecy** (**PFS**), is a feature of specific key-agreement protocols that gives assurances that session keys will not be compromised even if long-term secrets used in the session key exchange are compromised, limiting damage. For TLS, the long-term secret is typically the private key of the server. Forward secrecy protects past sessions against future compromises of keys or passwords. By generating a unique session key for every session a user initiates, the compromise of a single session key will not affect any data other than that exchanged in the specific session protected by that particular key. This by itself is not sufficient for forward secrecy, which additionally requires that a long-term secret compromise does not affect the security of past session keys.

Forward secrecy protects data on the transport layer of a network that uses common transport layer security protocols, including OpenSSL, when its long-term secret keys are compromised, as with the Heartbleed security bug. If forward secrecy is used, encrypted communications and sessions recorded in the past cannot be retrieved and decrypted should long-term secret keys or passwords be compromised in the future, even if the adversary actively interfered, for example via a man-in-the-middle (MITM) attack.

The value of forward secrecy is that it protects past communication. This reduces the motivation for attackers to compromise keys. For instance, if an attacker learns a long-term key, but the compromise is detected and the long-term key is revoked and updated, relatively little information is leaked in a forward secure system.

The value of forward secrecy depends on the assumed capabilities of an adversary. Forward secrecy has value if an adversary is assumed to be able to obtain secret keys from a device (read access) but is either detected or unable to modify the way session keys are generated in the device (full compromise). In some cases an adversary who can read long-term keys from a device may also be able to modify the functioning of the session key generator, as in the backdoored Dual Elliptic Curve Deterministic Random Bit Generator. If an adversary can make the random number generator predictable, then past traffic will be protected but all future traffic will be compromised.

The value of forward secrecy is limited not only by the assumption that an adversary will attack a server by only stealing keys and not modifying the random number generator used by the server but it is also limited by the assumption that the adversary will only passively collect traffic on the communications link and not be active using a man-in-the-middle attack. Forward secrecy typically uses an ephemeral Diffie–Hellman key exchange to prevent reading past traffic. The ephemeral Diffie–Hellman key exchange is often signed by the server using a static signing key. If an adversary can steal (or obtain through a court order) this static (long term) signing key, the adversary can masquerade as the server to the client and as the client to the server and implement a classic man-in-the-middle attack.

## History

The term "perfect forward secrecy" was coined by C. G. Günther in 1990 and further discussed by Whitfield Diffie, Paul van Oorschot, and Michael James Wiener in 1992, where it was used to describe a property of the Station-to-Station protocol.

Forward secrecy has also been used to describe the analogous property of password-authenticated key agreement protocols where the long-term secret is a (shared) password.

In 2000 the IEEE first ratified IEEE 1363, which establishes the related one-party and two-party forward secrecy properties of various standard key agreement schemes.

## Definition

An encryption system has the property of forward secrecy if plain-text (decrypted) inspection of the data exchange that occurs during key agreement phase of session initiation does not reveal the key that was used to encrypt the remainder of the session.

## Example

The following is a hypothetical example of a simple instant messaging protocol that employs forward secrecy:

1. Alice and Bob each generate a pair of long-term, asymmetric public and private keys, then verify public-key fingerprints in person or over an already-authenticated channel. Verification establishes with confidence that the claimed owner of a public key is the actual owner.
2. Alice and Bob use a key exchange algorithm such as Diffie–Hellman, to securely agree on an ephemeral session key. They use the keys from step 1 only to authenticate one another during this process.
3. Alice sends Bob a message, encrypting it with a symmetric cipher using the session key negotiated in step 2.
4. Bob decrypts Alice's message using the key negotiated in step 2.
5. The process repeats for each new message sent, starting from step 2 (and switching Alice and Bob's roles as sender/receiver as appropriate). Step 1 is never repeated.

Forward secrecy (achieved by generating new session keys for each message) ensures that past communications cannot be decrypted if one of the keys generated in an iteration of step 2 is compromised, since such a key is only used to encrypt a single message. Forward secrecy also ensures that past communications cannot be decrypted if the long-term private keys from step 1 are compromised. However, masquerading as Alice or Bob would be possible going forward if this occurred, possibly compromising all future messages.

## Attacks

Forward secrecy is designed to prevent the compromise of a long-term secret key from affecting the confidentiality of past conversations. However, forward secrecy cannot defend against a successful cryptanalysis of the underlying ciphers being used, since a cryptanalysis consists of finding a way to decrypt an encrypted message without the key, and forward secrecy only protects keys, not the ciphers themselves. A patient attacker can capture a conversation whose confidentiality is protected through the use of public-key cryptography and wait until the underlying cipher is broken (e.g. large quantum computers could be created which allow the discrete logarithm problem to be computed quickly), a.k.a. harvest now, decrypt later attacks. This would allow the recovery of old plaintexts even in a system employing forward secrecy.

Non-interactive forward-secure key exchange protocols face additional threats that are not relevant to interactive protocols. In a *message suppression* attack, an attacker in control of the network may itself store messages while preventing them from reaching the intended recipient; as the messages are never received, the corresponding private keys may not be destroyed or punctured, so a compromise of the private key can lead to successful decryption. Proactively retiring private keys on a schedule mitigates, but does not eliminate, this attack. In a *malicious key exhaustion* attack, the attacker sends many messages to the recipient and exhausts the private key material, forcing a protocol to choose between failing closed (and enabling denial of service attacks) or failing open (and giving up some amount of forward secrecy).

## Non-interactive forward secrecy

Most key exchange protocols are *interactive*, requiring bidirectional communication between the parties. A protocol that permits the sender to transmit data without first needing to receive any replies from the recipient may be called *non-interactive*, or *asynchronous*, or *zero round-trip time* (0-RTT).

Interactivity is onerous for some applications—for example, in a secure messaging system, it may be desirable to have a store-and-forward implementation, rather than requiring sender and recipient to be online at the same time; loosening the bidirectionality requirement can also improve performance even where it is not a strict requirement, for example at connection establishment or resumption. These use cases have stimulated interest in non-interactive key exchange, and, as forward security is a desirable property in a key-exchange protocol, in non-interactive forward secrecy. This combination has been identified as desirable since at least 1996. However, combining forward secrecy and non-interactivity has proven challenging; it had been suspected that forward secrecy with protection against replay attacks was impossible non-interactively, but it has been shown to be possible to achieve all three desiderata.

Broadly, two approaches to non-interactive forward secrecy have been explored, *pre-computed keys* and *puncturable encryption*.

With pre-computed keys, many key pairs are created and the public keys shared, with the private keys destroyed after a message has been received using the corresponding public key. This approach has been deployed as part of the Signal protocol.

In puncturable encryption, the recipient modifies their private key after receiving a message in such a way that the new private key cannot read the message but the public key is unchanged. Ross J. Anderson informally described a puncturable encryption scheme for forward secure key exchange in 1997, and Green & Miers (2015) formally described such a system, building on the related scheme of Canetti, Halevi & Katz (2003), which modifies the private key according to a schedule so that messages sent in previous periods cannot be read with the private key from a later period. Green & Miers (2015) make use of hierarchical identity-based encryption and attribute-based encryption, while Günther et al. (2017) use a different construction that can be based on any hierarchical identity-based scheme. Dallmeier et al. (2020) experimentally found that modifying QUIC to use a 0-RTT forward secure and replay-resistant key exchange implemented with puncturable encryption incurred significantly increased resource usage, but not so much as to make practical use infeasible.

## Weak perfect forward secrecy

Weak perfect forward secrecy (Wpfs) is the weaker property whereby when agents' long-term keys are compromised, the secrecy of previously established session keys is guaranteed, but only for sessions in which the adversary did not actively interfere. This new notion, and the distinction between this and forward secrecy, was introduced by Hugo Krawczyk in 2005. This weaker definition implicitly requires that full (perfect) forward secrecy maintains the secrecy of previously established session keys even in sessions where the adversary *did* actively interfere or attempted to act as a man in the middle.

## Protocols

Forward secrecy is present in several protocol implementations, such as SSH and IPsec (RFC 2412), though it is optional in the latter. Off-the-Record Messaging, a cryptography protocol and library for many instant messaging clients, as well as OMEMO which provides additional features such as multi-user functionality in such clients, both provide forward secrecy as well as deniable encryption.

In Transport Layer Security (TLS), cipher suites based on Diffie–Hellman key exchange (DHE-RSA, DHE-DSA) and elliptic curve Diffie–Hellman key exchange (ECDHE-RSA, ECDHE-ECDSA) are available. In theory, TLS can use forward secrecy since SSLv3, but many implementations do not offer forward secrecy or provided it with lower-grade encryption. TLS 1.3 removed support for RSA for key exchange, leaving Diffie–Hellman (with forward secrecy) as the sole algorithm for key exchange.

OpenSSL supports forward secrecy using elliptic curve Diffie–Hellman since version 1.0, with a computational overhead of approximately 15% for the initial handshake.

The Signal Protocol uses the Double Ratchet Algorithm to provide forward secrecy.

On the other hand, among popular protocols currently in use, WPA Personal did not support forward secrecy before WPA3.

## Use

Since late 2011, Google provided forward secrecy with TLS by default to users of its Gmail service, Google Docs service, and encrypted search services. Since November 2013, Twitter provided forward secrecy with TLS to its users. Wikis hosted by the Wikimedia Foundation have all provided forward secrecy to users since July 2014, and have required the use of forward secrecy since August 2018.

Facebook reported as part of an investigation into email encryption that, as of May 2014, 74% of hosts that support STARTTLS also provide forward secrecy. TLS 1.3, published in August 2018, dropped support for ciphers without forward secrecy. As of February 2019, 96.6% of web servers surveyed support some form of forward secrecy, and 52.1% will use forward secrecy with most browsers.

At WWDC 2016, Apple announced that all iOS apps would need to use App Transport Security (ATS), a feature which enforces the use of HTTPS transmission. Specifically, ATS requires the use of an encryption cipher that provides forward secrecy. ATS became mandatory for apps on January 1, 2017.

The Signal messaging application employs forward secrecy in its protocol, notably differentiating it from messaging protocols based on PGP.

In one survey in June 2025, forward secrecy was supported by about 95% of popular websites when accessed with modern browsers, while 0.2% did not support it at all.
