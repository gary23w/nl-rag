---
title: "Public key fingerprint"
source: https://en.wikipedia.org/wiki/Public_key_fingerprint
domain: certificate-transparency
license: CC-BY-SA-4.0
tags: certificate transparency log, merkle tree audit log, public key certificate monitoring, certificate authority accountability, misissued certificate detection
fetched: 2026-07-02
---

# Public key fingerprint

In public-key cryptography, a **public key fingerprint** is a short sequence of bytes used to identify a longer public key. Fingerprints are created by applying a cryptographic hash function to a public key. Since fingerprints are shorter than the keys they refer to, they can be used to simplify certain key management tasks. In Microsoft software, "thumbprint" is used instead of "fingerprint."

## Creating public key fingerprints

A public key fingerprint is typically created through the following steps:

1. A public key (and optionally some additional data) is encoded into a sequence of bytes. To ensure that the same fingerprint can be recreated later, the encoding must be deterministic, and any additional data must be exchanged and stored alongside the public key. The additional data is typically information which anyone using the public key should be aware of. Examples of additional data include: which protocol versions the key should be used with (in the case of PGP fingerprints); and the name of the key holder (in the case of X.509 trust anchor fingerprints, where the additional data consists of an X.509 self-signed certificate).
2. The data produced in the previous step is hashed with a cryptographic hash function such as SHA-1 or SHA-2.
3. If desired, the hash function output can be truncated to provide a shorter, more convenient fingerprint.

This process produces a short fingerprint which can be used to authenticate a much larger public key. For example, whereas a typical RSA public key will be 2048 bits in length or longer, typical MD5 or SHA-1 fingerprints are only 128 or 160 bits in length.

When displayed for human inspection, fingerprints are usually encoded into hexadecimal strings. These strings are then formatted into groups of characters for readability. For example, a 128-bit MD5 fingerprint for SSH would be displayed as follows:

```
 43:51:43:a1:b5:fc:8b:b7:0a:3a:a9:b1:0f:66:73:a8
```

## Using public key fingerprints for key authentication

When a public key is received over an untrusted channel, such as the Internet, the recipient often wishes to authenticate the public key. Fingerprints can help accomplish this, since their small size allows them to be passed over trusted channels where public keys won't easily fit.

For example, if Alice wishes to authenticate a public key as belonging to Bob, she can contact Bob over the phone or in person and ask him to read his fingerprint to her, or give her a scrap of paper with the fingerprint written down. Alice can then check that this trusted fingerprint matches the fingerprint of the public key. Exchanging and comparing values like this is much easier if the values are short fingerprints instead of long public keys.

Fingerprints can also be useful when automating the exchange or storage of key authentication data. For example, if key authentication data needs to be transmitted through a protocol or stored in a database where the size of a full public key is a problem, then exchanging or storing fingerprints may be a more viable solution.

In addition, fingerprints can be queried with search engines in order to ensure that the public key that a user just downloaded can be seen by third party search engines. If the search engine returns hits referencing the fingerprint linked to the proper site(s), one can feel more confident that the key is not being injected by an attacker, such as a Man-in-the-middle attack.

PGP developed the PGP word list to facilitate the exchange of public key fingerprints over voice channels.

## Public key fingerprints in practice

In systems such as SSH, users can exchange and check fingerprints manually to perform key authentication. Once a user has accepted another user's fingerprint, that fingerprint (or the key it refers to) will be stored locally along with a record of the other user's name or address, so that future communications with that user can be automatically authenticated.

In systems such as X.509-based PKI, fingerprints are primarily used to authenticate root keys. These root keys issue certificates which can be used to authenticate user keys. This use of certificates eliminates the need for manual fingerprint verification between users.

In systems such as PGP or Groove, fingerprints can be used for either of the above approaches: they can be used to authenticate keys belonging to other users, or keys belonging to certificate-issuing authorities. In PGP, normal users can issue certificates to each other, forming a web of trust, and fingerprints are often used to assist in this process (e.g., at key-signing parties).

In systems such as CGA or SFS and most cryptographic peer-to-peer networks, fingerprints are embedded into pre-existing address and name formats (such as IPv6 addresses, file names or other identification strings). If addresses and names are already being exchanged through trusted channels, this approach allows fingerprints to piggyback on them.

In PGP, most keys are created in such a way that what is called the "key ID" is equal to the lower 32 or 64 bits respectively of a key fingerprint. PGP uses key IDs to refer to public keys for a variety of purposes. These are not, properly speaking, fingerprints, since their short length prevents them from being able to securely authenticate a public key. 32bit key ids should not be used as current hardware can generate a colliding 32bit key id in just 4 seconds.

## Security of public key fingerprints

The primary threat to the security of a fingerprint is a second-preimage attack, where an attacker constructs a key pair whose public key hashes to a fingerprint that matches the victim's fingerprint. The attacker could then present his public key in place of the victim's public key to masquerade as the victim.

A secondary threat to some systems is a collision attack, where an attacker constructs multiple key pairs which hash to his own fingerprint. This may allow an attacker to repudiate signatures he has created, or cause other confusion.

To prevent preimage attacks, the cryptographic hash function used for a fingerprint should possess the property of second preimage resistance. If collision attacks are a threat, the hash function should also possess the property of collision-resistance. While it is acceptable to truncate hash function output for the sake of shorter, more usable fingerprints, the truncated fingerprints must be long enough to preserve the relevant properties of the hash function against brute-force search attacks.

In practice, most fingerprints commonly used today are based on non-truncated MD5 or SHA-1 hashes. As of 2017, collisions but not preimages can be found in MD5 and SHA-1. The future is therefore likely to bring increasing use of newer hash functions such as SHA-256. However, fingerprints based on SHA-256 and other hash functions with long output lengths are more likely to be truncated than (relatively short) MD5 or SHA-1 fingerprints.

In situations where fingerprint length must be minimized at all costs, fingerprint security can be boosted by increasing the cost of calculating the fingerprint. For example, in the context of Cryptographically Generated Addresses, this is called "Hash Extension" and requires anyone calculating a fingerprint to search for a hashsum starting with a fixed number of zeroes, which is assumed to be an expensive operation.
