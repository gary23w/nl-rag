---
title: "Key exchange"
source: https://en.wikipedia.org/wiki/Key_exchange
domain: diffie-hellman-exchange
license: CC-BY-SA-4.0
tags: diffie hellman key exchange, discrete logarithm, elliptic curve diffie hellman, forward secrecy
fetched: 2026-07-02
---

# Key exchange

**Key exchange** (also **key establishment**) is a method in cryptography by which cryptographic keys are exchanged between two parties, allowing use of a cryptographic algorithm.

If the sender and receiver wish to exchange encrypted messages, each must be equipped to encrypt messages to be sent and decrypt messages received. The nature of the equipping they require depends on the encryption technique they might use. If they use a code, both will require a copy of the same codebook. If they use a cipher, they will need appropriate keys. If the cipher is a symmetric key cipher, both will need a copy of the same key. If it is an asymmetric key cipher with the public/private key property, both will need the other's public key.

## Channel of exchange

Key exchange is done either in-band or out-of-band.

## The key exchange problem

The key exchange problem describes ways to exchange whatever keys or other information are needed for establishing a secure communication channel so that no one else can obtain a copy. Historically, before the invention of public-key cryptography (asymmetrical cryptography), symmetric-key cryptography utilized a single key to encrypt and decrypt messages. For two parties to communicate confidentially, they must first exchange the secret key so that each party is able to encrypt messages before sending, and decrypt received ones. This process is known as the key exchange.

The overarching problem with symmetrical cryptography, or single-key cryptography, is that it requires a secret key to be communicated through trusted couriers, diplomatic bags, or any other secure communication channel. If two parties cannot establish a secure initial key exchange, they won't be able to communicate securely without the risk of messages being intercepted and decrypted by a third party who acquired the key during the initial key exchange.

Public-key cryptography uses a two-key system, consisting of the public and the private keys, where messages are encrypted with one key and decrypted with another. It depends on the selected cryptographic algorithm which key—public or private—is used for encrypting messages, and which for decrypting. For example, in RSA, the private key is used for decrypting messages, while in the Digital Signature Algorithm (DSA), the private key is used for authenticating them. The public key can be sent over non-secure channels or shared in public; the private key is only available to its owner.

Known as the Diffie-Hellman key exchange, the encryption key can be openly communicated as it poses no risk to the confidentiality of encrypted messages. One party exchanges the keys to another party where they can then encrypt messages using the key and send back the cipher text. Only the decryption key—in this case, it's the private key—can decrypt that message. At no time during the Diffie-Hellman key exchange is any sensitive information at risk of compromise, as opposed to symmetrical key exchange.

### Identification

In principle, the only remaining problem was to be sure (or at least confident) that a public key actually belonged to its supposed owner. Because it is possible to 'spoof' another's identity in any of several ways, this is not a trivial or easily solved problem, particularly when the two users involved have never met and know nothing about each other.

### Diffie–Hellman key exchange

In 1976, Whitfield Diffie and Martin Hellman published a cryptographic protocol called the Diffie–Hellman key exchange (D–H) based on concepts developed by Hellman's PhD student Ralph Merkle. The protocol enables users to securely exchange secret keys even if an opponent is monitoring that communication channel. The D–H key exchange protocol, however, does not by itself address authentication (i.e. the problem of being sure of the actual identity of the person or 'entity' at the other end of the communication channel). Authentication is crucial when an opponent can both monitor *and alter* messages within the communication channel (AKA man-in-the-middle or MITM attacks) and was addressed in the fourth section of the paper.

### Public key infrastructure

Public key infrastructures (PKIs) have been proposed as a workaround for the problem of identity authentication. In their most usual implementation, each user applies to a “certificate authority” (CA), trusted by all parties, for a digital certificate which serves for other users as a non-tamperable authentication of identity. The infrastructure is safe, unless the CA itself is compromised. In case it is, though, many PKIs provide a way to revoke certificates so other users will not trust them. Revoked certificates are usually put in certificate revocation lists which any certificate can be matched against.

Several countries and other jurisdictions have passed legislation or issued regulations encouraging PKIs by giving (more or less) legal effect to these digital certificates (see digital signature). Many commercial firms, as well as a few government departments, have established such certificate authorities.

This does nothing to solve the problem though, as the trustworthiness of the CA itself is still not guaranteed for any particular individual. It is a form of argument from authority fallacy. For actual trustworthiness, personal verification that the certificate belongs to the CA and establishment of trust in the CA are required. This is usually not possible.

There are known cases where authoritarian governments proposed establishing so-called “national CAs” whose certificates would be mandatory to install on citizens’ devices and, once installed and trusted, could be used for monitoring, intercepting, modifying, or blocking the encrypted internet traffic.

For those new to such things, these arrangements are best thought of as electronic notary endorsements that “this public key belongs to this user”. As with notary endorsements, there can be mistakes or misunderstandings in such vouchings. Additionally, the notary itself can be untrusted. There have been several high-profile public failures by assorted certificate authorities.

### Web of trust

At the other end of the conceptual range is the web of trust system, which avoids central Certificate Authorities entirely. Each user is responsible for getting a certificate from another user before using that certificate to communicate with the user. PGP and GPG (an implementation of the OpenPGP Internet Standard) employ just such a web of trust mechanism.

### Password-authenticated key agreement

Password-authenticated key agreement algorithms can perform a cryptographic key exchange utilizing knowledge of a user's password.

### Quantum key exchange

Quantum key distribution exploits certain properties of quantum physics to ensure its security. It relies on the fact that observations (or measurements) of a quantum state introduces perturbations in that state. Over many systems, these perturbations are detectable as noise by the receiver, making it possible to detect man-in-the-middle attacks. Beside the correctness and completeness of quantum mechanics, the protocol assumes the availability of an authenticated channel between Alice and Bob.
