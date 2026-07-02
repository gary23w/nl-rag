---
title: "Direct Anonymous Attestation"
source: https://en.wikipedia.org/wiki/Direct_Anonymous_Attestation
domain: remote-attestation
license: CC-BY-SA-4.0
tags: remote attestation protocol, platform integrity attestation, attestation evidence verification, trusted computing attestation
fetched: 2026-07-02
---

# Direct Anonymous Attestation

**Direct Anonymous Attestation** (**DAA**) is a cryptographic primitive which enables remote authentication of a trusted computer whilst preserving privacy of the platform's user. The protocol has been adopted by the Trusted Computing Group (TCG) in the latest version of its Trusted Platform Module (TPM) specification to address privacy concerns (see also Loss of Internet anonymity). ISO/IEC 20008 specifies DAA, as well, and Intel's Enhanced Privacy ID (EPID) 2.0 implementation for microprocessors is available for licensing RAND-Z along with an open source SDK.

## Historical perspective

In principle the privacy issue could be resolved using any standard signature scheme (or public key encryption) and a single key pair. Manufacturers would embed the private key into every TPM produced and the public key would be published as a certificate. Signatures produced by the TPM must have originated from the private key, by the nature of the technology, and since all TPMs use the same private key they are indistinguishable ensuring the user's privacy. This rather naive solution relies upon the assumption that there exists a *global secret*. One only needs to look at the precedent of Content Scramble System (CSS), an encryption system for DVDs, to see that this assumption is fundamentally flawed. Furthermore, this approach fails to realize a secondary goal: the ability to detect rogue TPMs. A rogue TPM is a TPM that has been compromised and had its secrets extracted.

The solution first adopted by the TCG (TPM specification v1.1) required a trusted third-party, namely a *privacy certificate authority* (privacy CA). Each TPM has an embedded RSA key pair called an Endorsement Key (EK) which the privacy CA is assumed to know. In order to attest the TPM generates a second RSA key pair called an Attestation Identity Key (AIK). It sends the public AIK, signed by EK, to the privacy CA who checks its validity and issues a certificate for the AIK. (For this to work, either a) the privacy CA must know the TPM's public EK *a priori*, or b) the TPM's manufacturer must have provided an *endorsement certificate*.) The host/TPM is now able to authenticate itself with respect to the certificate. This approach permits two possibilities to detecting rogue TPMs: firstly the privacy CA should maintain a list of TPMs identified by their EK known to be rogue and reject requests from them, secondly if a privacy CA receives too many requests from a particular TPM it may reject them and blocklist the TPMs EK. The number of permitted requests should be subject to a risk management exercise. This solution is problematic since the privacy CA must take part in every transaction and thus must provide high availability whilst remaining secure. Furthermore, privacy requirements may be violated if the privacy CA and verifier collude. Although the latter issue can probably be resolved using blind signatures, the first remains.

The EPID 2.0 solution embeds the private key in the microprocessor when it is manufactured, inherently distributes the key with the physical device shipment, and has the key provisioned and ready for use with 1st power-on.

## Overview

The DAA protocol is based on three entities and two different steps. The entities are the DAA Member (TPM platform or EPID-enabled microprocessor), the DAA Issuer and the DAA Verifier. The issuer is charged to verify the TPM platform during the Join step and to issue DAA credential to the platform. The platform (Member) uses the DAA credential with the Verifier during the Sign step. Through a zero-knowledge proof the Verifier can verify the credential without attempting to violate the platform's privacy. The protocol also supports a blocklisting capability so that Verifiers can identify attestations from TPMs that have been compromised.

## Privacy properties

The protocol allows differing degrees of privacy. Interactions are always anonymous, but the Member/Verifier may negotiate as to whether the Verifier is able to link transactions. This would allow user profiling and/or the rejection of requests originating from a host which has made too many requests. The Member and Verifier can also elect to reveal additional information to accomplish non-anonymous interactions (just as you can choose to tell a stranger your full name, or not). Thus, known identity can be built on top of an anonymous start. (Contrast this with: if you start with known identity, you can never prove you un-know that identity to regress to anonymity.)

## Implementations and attacks

The first Direct Anonymous Attestation scheme was due to Brickell, Camenisch, and Chen; that scheme proved insecure and required a fix. Brickell, Chen, and Li improved efficiency of that first scheme using symmetric pairings, rather than RSA. And Chen, Morrissey, and Smart attempted to further improve efficiency by switching from a symmetric to an asymmetric setting; unfortunately, the asymmetric scheme was also insecure. Chen, Page, and Smart proposed a new elliptic curve cryptography scheme using Barreto–Naehrig curves. This scheme is implemented by both EPID 2.0 and the TPM 2.0 standard. It is recommended for TPMs in general and required for TPMs that conform to the PC client profile. In addition, the Intel EPID 2.0 implementation of ISO/IEC 20008 DAA and the available open source SDK can be used for members and verifiers to do attestation. Since one of the DAA attestation methods in TPM 2.0 is identical to EPID 2.0, work is underway to make ISO/IEC 20008 DAA and TPM 2.0 DAA attestation read consistently with each other at the spec level.
