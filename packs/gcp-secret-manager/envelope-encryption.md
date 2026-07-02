---
title: "Hybrid cryptosystem"
source: https://en.wikipedia.org/wiki/Envelope_encryption
domain: gcp-secret-manager
license: CC-BY-SA-4.0
tags: gcp secret manager, secret storage gcp, credential management gcp, api key management
fetched: 2026-07-02
---

# Hybrid cryptosystem

(Redirected from

Envelope encryption

)

In cryptography, a **hybrid cryptosystem** is one which combines the convenience of a public-key cryptosystem with the efficiency of a symmetric-key cryptosystem. Public-key cryptosystems are convenient in that they do not require the sender and receiver to share a common secret in order to communicate securely. However, they often rely on complicated mathematical computations and are thus generally much more inefficient than comparable symmetric-key cryptosystems. In many applications, the high cost of encrypting long messages in a public-key cryptosystem can be prohibitive. This is addressed by hybrid systems by using a combination of both.

A hybrid cryptosystem can be constructed using any two separate cryptosystems:

- a key encapsulation mechanism, which is a public-key cryptosystem
- a data encapsulation scheme, which is a symmetric-key cryptosystem

The hybrid cryptosystem is itself a public-key system, whose public and private keys are the same as in the key encapsulation scheme.

Note that for very long messages the bulk of the work in encryption/decryption is done by the more efficient symmetric-key scheme, while the inefficient public-key scheme is used only to encrypt/decrypt a short key value.

## Implementations and standards

All practical implementations of public key cryptography today employ a hybrid system. Examples include the TLS protocol and the SSH protocol, that use a public-key mechanism for key exchange (such as Diffie-Hellman) and a symmetric-key mechanism for data encapsulation (such as AES). The OpenPGP file format and the PKCS#7 file format are other examples.

Hybrid Public Key Encryption (HPKE, published as RFC 9180) is a modern standard for generic hybrid encryption. HPKE is used within multiple IETF protocols, including Messaging Layer Security (MLS), Oblivious DNS over HTTPS, Oblivious HTTP, Privacy Preserving Measurement, and TLS Encrypted Client Hello.

Envelope encryption is an example of a usage of hybrid cryptosystems in cloud computing. In a cloud context, hybrid cryptosystems also enable centralized key management.

## Example

To encrypt a message addressed to Alice in a hybrid cryptosystem, Bob does the following:

1. Obtains Alice's public key.
2. Generates a fresh symmetric key for the data encapsulation scheme.
3. Encrypts the message under the data encapsulation scheme, using the symmetric key just generated.
4. Encrypts the symmetric key under the key encapsulation scheme, using Alice's public key.
5. Sends both of these ciphertexts to Alice.

To decrypt this hybrid ciphertext, Alice does the following:

1. Uses her private key to decrypt the symmetric key contained in the key encapsulation segment.
2. Uses this symmetric key to decrypt the message contained in the data encapsulation segment.

## Security

If both the key encapsulation and data encapsulation schemes in a hybrid cryptosystem are secure against adaptive chosen ciphertext attacks, then the hybrid scheme inherits that property as well. However, it is possible to construct a hybrid scheme secure against adaptive chosen ciphertext attacks even if the key encapsulation has a slightly weakened security definition (though the security of the data encapsulation must be slightly stronger).

## Envelope encryption

Envelope encryption is term used for encrypting with a hybrid cryptosystem used by all major cloud service providers, often as part of a centralized key management system in cloud computing.

Envelope encryption gives names to the keys used in hybrid encryption: Data Encryption Keys (abbreviated DEK, and used to encrypt data) and Key Encryption Keys (abbreviated KEK, and used to encrypt the DEKs). In a cloud environment, encryption with envelope encryption involves generating a DEK locally, encrypting one's data using the DEK, and then issuing a request to wrap (encrypt) the DEK with a KEK stored in a potentially more secure service. Then, this wrapped DEK and encrypted message constitute a ciphertext for the scheme. To decrypt a ciphertext, the wrapped DEK is unwrapped (decrypted) via a call to a service, and then the unwrapped DEK is used to decrypt the encrypted message. In addition to the normal advantages of a hybrid cryptosystem, using asymmetric encryption for the KEK in a cloud context provides easier key management and separation of roles, but can be slower.

In cloud systems, such as Google Cloud Platform and Amazon Web Services, a key management system (KMS) can be available as a service. In some cases, the key management system will store keys in hardware security modules, which are hardware systems that protect keys with hardware features like intrusion resistance. This means that KEKs can also be more secure because they are stored on secure specialized hardware. Envelope encryption makes centralized key management easier because a centralized key management system only needs to store KEKs, which occupy less space, and requests to the KMS only involve sending wrapped and unwrapped DEKs, which use less bandwidth than transmitting entire messages. Since one KEK can be used to encrypt many DEKs, this also allows for less storage space to be used in the KMS. This also allows for centralized auditing and access control at one point of access.
