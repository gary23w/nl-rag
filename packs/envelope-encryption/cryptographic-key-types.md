---
title: "Cryptographic key types"
source: https://en.wikipedia.org/wiki/Cryptographic_key_types
domain: envelope-encryption
license: CC-BY-SA-4.0
tags: envelope encryption, data encryption key wrapping, key encryption key, key hierarchy management
fetched: 2026-07-02
---

# Cryptographic key types

A cryptographic key is a string of data that is used to lock or unlock cryptographic functions, including authentication, authorization and encryption. Cryptographic keys are grouped into **cryptographic key types** according to the functions they perform.

## Description

Consider a keyring that contains a variety of keys. These keys might be various shapes and sizes, but one thing is certain, each will generally serve a separate purpose. One key might be used to start an automobile, while another might be used to open a safe deposit box. The automobile key will not work to open the safe deposit box and vice versa. This analogy provides some insight on how cryptographic key types work. These keys are categorized in respect to how they are used and what properties they possess.

A cryptographic key is categorized according to how it will be used and what properties it has. For example, a key might have one of the following properties: Symmetric, Public or Private. Keys may also be grouped into pairs that have one private and one public key, which is referred to as an Asymmetric key pair.

### Asymmetric versus symmetric keys

Asymmetric keys differ from symmetric keys in that the algorithms use separate keys for encryption and decryption, while a symmetric key’s algorithm uses a single key for both processes. Because multiple keys are used with an asymmetric algorithm, the process takes longer to produce than a symmetric key algorithm would. However, the benefits lay in the fact that an asymmetric algorithm is much more secure than a symmetric key algorithm is.

With a symmetric key, the key needs to be transmitted to the receiver, where there is always the possibility that the key could be intercepted or tampered with. With an asymmetric key, the message and/or accompanying data can be sent or received by using a public key; however, the receiver or sender would use his or her personal private key to access the message and/or accompanying data. Thus, asymmetric keys are suited for use for transmitting confidential messages and data and when authentication is required for assurance that the message has not been tampered with. Only the receiver, who is in possession of the private key corresponding to the public key(encryption only key), has the ability to decode the message. A public key can be sent back and forth between recipients, but a private key remains fixed to one location and is not sent back and forth, which keeps it safe from being intercepted during transmission.

### Long term versus single use

Cryptographic keys may also have keys that designate they can be used for long-term (static, archived) use or used for a single session (ephemeral). The latter generally applies to the use of an Ephemeral Key Agreement Key. Most other key types are designed to last for long crypto-periods, from about one to two years. When a shorter crypto-period is designed different key types may be used, such as Data Encryption keys, Symmetric Authentication keys, Private Key-Transport keys, Key-Wrapping keys, Authorization keys or RNG keys.

## Key types

This page shows the classification of key types from the point of view of key management. In a key management system, each key should be labeled with one such type and that key should never be used for a different purpose.

According to NIST SP 800-57 (Revision 4) the following types of keys exist:

**Private signature key**

Private signature keys are the private keys of asymmetric (

public

) key pairs that are used by public key algorithms to generate digital signatures with possible long-term implications. When properly handled, private signature keys can be used to provide

authentication

,

integrity

and

non-repudiation

.

**Public signature verification key**

A public signature verification key is the public key of an asymmetric key pair that is used by a public key algorithm to verify digital signatures, either to authenticate a user's identity, to determine the integrity of the data, for non-repudiation, or a combination thereof.

**Symmetric authentication key**

Symmetric

authentication keys are used with symmetric key algorithms to provide assurance of the integrity and source of messages, communication sessions, or stored data.

**Private authentication key**

A private authentication key is the private key of an asymmetric key pair that is used with a public key algorithm to provide assurance as to the integrity of information, and the identity of the originating entity or the source of messages, communication sessions, or stored data.

**Public authentication key**

A public authentication key is the public key of an asymmetric key pair that is used with a public key algorithm to determine the integrity of information and to authenticate the identity of entities, or the source of messages, communication sessions, or stored data.

**Symmetric data encryption key**

These keys are used with symmetric key algorithms to apply confidentiality protection to information.

**Symmetric key wrapping key**

Symmetric key wrapping keys are used to encrypt other keys using symmetric key algorithms. Key wrapping keys are also known as key encrypting keys.

**Symmetric and asymmetric random number generation keys**

These are keys used to

generate random numbers

.

**Symmetric master key**

A symmetric master key is used to derive other symmetric keys (e.g., data encryption keys, key wrapping keys, or authentication keys) using symmetric cryptographic methods.

**Private key transport key**

Private key transport keys are the private keys of asymmetric key pairs that are used to decrypt keys that have been encrypted with the associated public key using a public key algorithm. Key transport keys are usually used to establish keys (e.g., key wrapping keys, data encryption keys or

MAC

keys) and, optionally, other keying material (e.g.,

initialization vectors

).

**Public key transport key**

Public key transport keys are the public keys of asymmetric key pairs that are used to encrypt keys using a public key algorithm. These keys are used to establish keys (e.g., key wrapping keys, data encryption keys or MAC keys) and, optionally, other keying material (e.g., Initialization Vectors).

**Symmetric key agreement key**

These symmetric keys are used to establish keys (e.g., key wrapping keys, data encryption keys, or MAC keys) and, optionally, other keying material (e.g., Initialization Vectors) using a symmetric key agreement algorithm.

**Private static key agreement key**

Private

static key

agreement keys are the private keys of asymmetric key pairs that are used to establish keys (e.g., key wrapping keys, data encryption keys, or MAC keys) and, optionally, other keying material (e.g., Initialization Vectors).

**Public static key agreement key**

Public static key agreement keys are the public keys of asymmetric key pairs that are used to establish keys (e.g., key wrapping keys, data encryption keys, or MAC keys) and, optionally, other keying material (e.g., Initialization Vectors).

**Private ephemeral key agreement key**

Private

ephemeral key

agreement keys are the private keys of asymmetric key pairs that are used only once to establish one or more keys (e.g., key wrapping keys, data encryption keys, or MAC keys) and, optionally, other keying material (e.g., Initialization Vectors).

**Public ephemeral key agreement key**

Public ephemeral key agreement keys are the public keys of asymmetric key pairs that are used in a single key establishment transaction to establish one or more keys (e.g., key wrapping keys, data encryption keys, or MAC keys) and, optionally, other keying material (e.g., Initialization Vectors).

**Symmetric authorization key**

Symmetric

authorization

keys are used to provide privileges to an entity using a symmetric cryptographic method. The authorization key is known by the entity responsible for monitoring and granting access privileges for authorized entities and by the entity seeking access to resources.

**Private authorization key**

A private authorization key is the private key of an asymmetric key pair that is used to provide privileges to an entity.

**Public authorization key**

A public authorization key is the public key of an asymmetric key pair that is used to verify privileges for an entity that knows the associated private authorization key.
