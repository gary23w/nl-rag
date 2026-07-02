---
title: "Key management"
source: https://en.wikipedia.org/wiki/Key_management
domain: envelope-encryption-deep
license: CC-BY-SA-4.0
tags: envelope encryption, key wrapping scheme, data encryption key, disk encryption at rest, symmetric key algorithm
fetched: 2026-07-02
---

# Key management

**Key management** is the management of cryptographic keys in a cryptosystem. This includes the lifecycle management of keys, such as the generation, exchange, storage, use, crypto-shredding (destruction) and replacement of keys. It includes cryptographic protocol design, key servers, user procedures, and other relevant protocols.

Key management concerns keys at the user level, either between users or systems. This is in contrast to key scheduling, which typically refers to the internal handling of keys within the operation of a cipher.

Successful key management is critical to the security of a cryptosystem. It is the more challenging side of cryptography in a sense that it involves aspects of social engineering such as system policy, user training, organizational and departmental interactions, and coordination between all of these elements, in contrast to pure mathematical practices that can be automated.

## Types of keys

Cryptographic systems may use different types of keys, with some systems using more than one. These may include symmetric keys or asymmetric keys. In a symmetric key algorithm the keys involved are identical for both encrypting and decrypting a message. Keys must be chosen carefully, and distributed and stored securely. Asymmetric keys, also known as public keys, in contrast are two distinct keys that are mathematically linked. They are typically used together to communicate. Public key infrastructure (PKI), the implementation of public key cryptography, requires an organization to establish an infrastructure to create and manage public and private key pairs along with digital certificates.

## Inventory

The starting point in any certificate and private key management strategy is to create a comprehensive inventory of all certificates, their locations and responsible parties. This is not a trivial matter because certificates from a variety of sources are deployed in a variety of locations by different individuals and teams - it's simply not possible to rely on a list from a single certificate authority. Certificates that are not renewed and replaced before they expire can cause serious downtime and outages. Some other considerations:

- Regulations and requirements, like PCI-DSS, demand stringent security and management of cryptographic keys and auditors are increasingly reviewing the management controls and processes in use.
- Private keys used with certificates must be kept secure or unauthorised individuals can intercept confidential communications or gain unauthorised access to critical systems. Failure to ensure proper segregation of duties means that admins who generate the encryption keys can use them to access sensitive, regulated data.
- If a certificate authority is compromised or an encryption algorithm is broken, organizations must be prepared to replace all of their certificates and keys in a matter of hours.

## Management steps

Once keys are inventoried, key management typically consists of three steps: exchange, storage and use.

### Key exchange

Prior to any secured communication, users must set up the details of the cryptography. In some instances this may require exchanging identical keys (in the case of a symmetric key system). In others it may require possessing the other party's public key. While public keys can be openly exchanged (their corresponding private key is kept secret), symmetric keys must be exchanged over a secure communication channel. Formerly, exchange of such a key was extremely troublesome, and was greatly eased by access to secure channels such as a diplomatic bag. Clear text exchange of symmetric keys would enable any interceptor to immediately learn the key, and any encrypted data.

The advance of public key cryptography in the 1970s has made the exchange of keys less troublesome. Since the Diffie-Hellman key exchange protocol was published in 1975, it has become possible to exchange a key over an insecure communications channel, which has substantially reduced the risk of key disclosure during distribution. It is possible, using something akin to a book code, to include key indicators as clear text attached to an encrypted message. The encryption technique used by Richard Sorge's code clerk was of this type, referring to a page in a statistical manual, though it was in fact a code. The German Army Enigma symmetric encryption key was a mixed type early in its use; the key was a combination of secretly distributed key schedules and a user chosen session key component for each message.

In more modern systems, such as OpenPGP compatible systems, a session key for a symmetric key algorithm is distributed encrypted by an asymmetric key algorithm. This approach avoids even the necessity for using a key exchange protocol like Diffie-Hellman key exchange.

Another method of key exchange involves encapsulating one key within another. Typically a master key is generated and exchanged using some secure method. This method is usually cumbersome or expensive (breaking a master key into multiple parts and sending each with a trusted courier for example) and not suitable for use on a larger scale. Once the master key has been securely exchanged, it can then be used to securely exchange subsequent keys with ease. This technique is usually termed key wrap. A common technique uses block ciphers and cryptographic hash functions.

A related method is to exchange a master key (sometimes termed a root key) and derive subsidiary keys as needed from that key and some other data (often referred to as diversification data). The most common use for this method is probably in smartcard-based cryptosystems, such as those found in banking cards. The bank or credit network embeds their secret key into the card's secure key storage during card production at a secured production facility. Then at the point of sale the card and card reader are both able to derive a common set of session keys based on the shared secret key and card-specific data (such as the card serial number). This method can also be used when keys must be related to each other (i.e., departmental keys are tied to divisional keys, and individual keys tied to departmental keys). However, tying keys to each other in this way increases the damage which may result from a security breach as attackers will learn something about more than one key. This reduces entropy, with regard to an attacker, for each key involved.

A recent method uses an oblivious pseudorandom function to issue keys without the key management system ever being in a position to see the keys.

### Key storage

However distributed, keys must be stored securely to maintain communications security. Security is a big concern and hence there are various techniques in use to do so. Likely the most common is that an encryption application manages keys for the user and depends on an access password to control use of the key. Likewise, in the case of smartphone keyless access platforms, they keep all identifying door information off mobile phones and servers and encrypt all data, where just like low-tech keys, users give codes only to those they trust.

In terms of regulation, there are few that address key storage in depth. "Some contain minimal guidance like 'don’t store keys with encrypted data' or suggest that 'keys should be kept securely.'" The notable exceptions to that are PCI DSS 3.2.1, NIST 800-53 and NIST 800–57.

For optimal security, keys may be stored in a Hardware Security Module (HSM) or protected using technologies such as Trusted Execution Environment (TEE, e.g. Intel SGX) or Multi-Party Computation (MPC). Additional alternatives include utilizing Trusted Platform Modules (TPM), virtual HSMs, aka "Poor Man's Hardware Security Modules" (pmHSM), or non-volatile Field-Programmable-Gate-Arrays (FPGA) with supporting System-on-Chip configurations. In order to verify the integrity of a key stored without compromising its actual value a KCV algorithm can be used.

### Key encryption use

The major issue is length of time a key is to be used, and therefore frequency of replacement. Because it increases any attacker's required effort, keys should be frequently changed. This also limits loss of information, as the number of stored encrypted messages which will become readable when a key is found will decrease as the frequency of key change increases. Historically, symmetric keys have been used for long periods in situations in which key exchange was very difficult or only possible intermittently. Ideally, the symmetric key should change with each message or interaction, so that only that message will become readable if the key is learned (*e.g.*, stolen, cryptanalyzed, or social engineered).

## Challenges

Several challenges IT organizations face when trying to control and manage their encryption keys are:

1. Scalability: Managing a large number of encryption keys.
2. Security: Vulnerability of keys from outside hackers, malicious insiders.
3. Availability: Ensuring data accessibility for authorized users.
4. Heterogeneity: Supporting multiple databases, applications and standards.
5. Governance: Defining policy-driven access control and protection for data. Governance includes compliance with data protection requirements.

## Compliance

Key management compliance refers to the oversight, assurance, and capability of being able to demonstrate that keys are securely managed. This includes the following individual compliance domains:

- *Physical security* – the most visible form of compliance, which may include locked doors to secure system equipment and surveillance cameras. These safeguards can prevent unauthorized access to printed copies of key material and computer systems that run key management software.
- *Logical security* – protects the organization against the theft or unauthorized access of information. This is where the use of cryptographic keys comes in by encrypting data, which is then rendered useless to those who do not have the key to decrypt it.
- *Personnel security* – this involves assigning specific roles or privileges to personnel to access information on a strict need-to-know basis. Background checks should be performed on new employees along with periodic role changes to ensure security.

Compliance can be achieved with respect to national and international data protection standards and regulations, such as Payment Card Industry Data Security Standard, Health Insurance Portability and Accountability Act, Sarbanes–Oxley Act, or General Data Protection Regulation.

## Management and compliance systems

### Key management system

A *key management system* (KMS), also known as a *cryptographic key management system* (CKMS) or *enterprise key management system* (EKMS), is an integrated approach for generating, distributing and managing cryptographic keys for devices and applications. They may cover all aspects of security - from the secure generation of keys over the secure exchange of keys up to secure key handling and storage on the client. Thus, a KMS includes the backend functionality for key generation, distribution, and replacement as well as the client functionality for injecting keys, storing and managing keys on devices.

### Standards-based key management

Many specific applications have developed their own key management systems with home grown protocols. However, as systems become more interconnected keys need to be shared between those different systems. To facilitate this, key management standards have evolved to define the protocols used to manage and exchange cryptographic keys and related information.

### Key Management Interoperability Protocol (KMIP)

KMIP is an extensible key management protocol that has been developed by many organizations working within the OASIS standards body. The first version was released in 2010, and it has been further developed by an active technical committee.

The protocol allows for the creation of keys and their distribution among disparate software systems that need to utilize them. It covers the full key life cycle of both symmetric and asymmetric keys in a variety of formats, the wrapping of keys, provisioning schemes, and cryptographic operations as well as meta data associated with the keys.

The protocol is backed by an extensive series of test cases, and interoperability testing is performed between compliant systems each year.

- (Individual interoperability tests performed by each server/client vendor combination since 2012) Individual interoperability tests performed by each server/client vendor combination since 2012
- (Results of 2017 OASIS KMIP interoperability testing) Results of 2017 OASIS KMIP interoperability testing

A list of some 80 products that conform to the KMIP standard can be found on the OASIS website.

#### Closed source

- Bloombase KeyCastle
- Cryptsoft KMIP C and Java Servers
- Fornetix Key Orchestration
- Fortanix Data Security Manager
- Gazzang zTrustee
- HP Enterprise Secure Key Manager
- IBM Distributed Key Management System (DKMS)
- IBM Enterprise Key Management Foundation
- IBM Security Key Lifecycle Manager
- IBM Cloud Hyper Protect Crypto Services
- Oracle Key Vault
- Oracle Key Manager
- P6R KMIP Client SDK
- QuintessenceLabs qCrypt Key and Policy Manager
- RSA Data Protection Manager
- Gemalto’s SafeNet KeySecure
- Thales Key Management
- Townsend Security Alliance Key Manager
- Venafi Trust Protection Platform
- Vormetric Data Security Platform

### Non-KMIP-compliant key management

#### Open source

- Barbican, the OpenStack security API.
- KeyBox - web-based SSH access and key management.
- EPKS - Echo Public Key Share, system to share encryption keys online in a p2p community.
- Kmc-Subset137 - key management system implementing UNISIG Subset-137 for ERTMS/ETCS railway application.
- privacyIDEA - two factor management with support for managing SSH keys.
- StrongKey - open source, last updated on SourceForge in 2016. There is no more maintenance on this project according to its home page.
- Vault - secret server from HashiCorp.
- NuCypher Archived 2018-05-07 at the Wayback Machine
- SecretHub Archived 2020-01-02 at the Wayback Machine - end-to-end encrypted SaaS key management
- Infisical - end-to-end open-source secret management platform.

#### Closed source

- Amazon Web Service (AWS) Key Management Service (KMS)
- Bell ID Key Manager
- Bloombase KeyCastle
- Cryptomathic CKMS
- Doppler SecretOps Platform
- Encryptionizer Key Manager (Windows only)
- Google Cloud Key Management
- IBM Cloud Key Protect
- Microsoft Azure Key Vault
- Porticor Virtual Private Data
- SSH Communications Security Universal SSH Key Manager
- CipherTrust Manager
- Akeyless Vault

#### KMS security policy

The security policy of a key management system provides the rules that are to be used to protect keys and metadata that the key management system supports. As defined by the National Institute of Standards and Technology NIST, the policy shall establish and specify rules for this information that will protect its:

- Confidentiality
- Integrity
- Availability
- Authentication of source

This protection covers the complete key life-cycle from the time the key becomes operational to its elimination.

#### Bring your own encryption / key

*Bring your own encryption* (BYOE)—also called *bring your own key* (BYOK)—refers to a cloud-computing security model to allow public-cloud customers to use their own encryption software and manage their own encryption keys. This security model is usually considered a marketing stunt, as critical keys are being handed over to third parties (cloud providers) and key owners are still left with the operational burden of generating, rotating and sharing their keys.

### Public-key infrastructure (PKI)

A public-key infrastructure is a type of key management system that uses hierarchical digital certificates to provide authentication, and public keys to provide encryption. PKIs are used in World Wide Web traffic, commonly in the form of SSL and TLS.

### Multicast group key management

Group key management means managing the keys in a group communication. Most of the group communications use multicast communication so that if the message is sent once by the sender, it will be received by all the users. The main problem in multicast group communication is its security. In order to improve the security, various keys are given to the users. Using the keys, the users can encrypt their messages and send them secretly. IETF.org released RFC 4046, entitled Multicast Security (MSEC) Group Key Management Architecture, which discusses the challenges of group key management.
