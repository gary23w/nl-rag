---
title: "Secure cryptoprocessor"
source: https://en.wikipedia.org/wiki/Secure_cryptoprocessor
domain: hardware-security-module
license: CC-BY-SA-4.0
tags: hardware security module, cryptographic key management, tamper resistant hardware, secure cryptoprocessor, fips validated cryptography
fetched: 2026-07-02
---

# Secure cryptoprocessor

A **secure cryptoprocessor** is a dedicated computer-on-a-chip or microprocessor for carrying out cryptographic operations, embedded in a packaging with multiple physical security measures, which give it a degree of tamper resistance. Unlike cryptographic processors that output decrypted data onto a bus in a secure environment, a secure cryptoprocessor does not output decrypted data or decrypted program instructions in an environment where security cannot always be maintained.

The purpose of a secure cryptoprocessor is to act as the keystone of a security subsystem, eliminating the need to protect the rest of the subsystem with physical security measures.

## Examples

A hardware security module (HSM) contains one or more secure cryptoprocessor chips. These devices are high grade secure cryptoprocessors used with enterprise servers. A hardware security module can have multiple levels of physical security with a single-chip cryptoprocessor as its most secure component. The cryptoprocessor does not reveal keys or executable instructions on a bus, except in encrypted form, and zeros keys by attempts at probing or scanning. The crypto chip(s) may also be potted in the hardware security module with other processors and memory chips that store and process encrypted data. Any attempt to remove the potting will cause the keys in the crypto chip to be zeroed. A hardware security module may also be part of a computer (for example an ATM) that operates inside a locked safe to deter theft, substitution, and tampering.

Modern smartcards are probably the most widely deployed form of secure cryptoprocessor, although more complex and versatile secure cryptoprocessors are widely deployed in systems such as Automated teller machines, TV set-top boxes, military applications, and high-security portable communication equipment. Some secure cryptoprocessors can even run general-purpose operating systems such as Linux inside their security boundary. Cryptoprocessors input program instructions in encrypted form and decrypt the instructions to plain instructions, which are then executed within the same cryptoprocessor chip where the decrypted instructions are inaccessibly stored. By never revealing the decrypted program instructions, the cryptoprocessor prevents tampering of programs by technicians who may have legitimate access to the sub-system data bus. This is known as bus encryption. Data processed by a cryptoprocessor is also frequently encrypted.

The Trusted Platform Module (TPM) is an implementation of a secure cryptoprocessor that brings the notion of trusted computing to ordinary PCs by enabling a secure environment. Present TPM implementations focus on providing a tamper-proof boot environment, and persistent and volatile storage encryption.

Security chips for embedded systems are also available that provide the same level of physical protection for keys and other secret material as a smartcard processor or TPM but in a smaller, less complex and less expensive package. They are often referred to as cryptographic authentication devices and are used to authenticate peripherals, accessories and/or consumables. Like TPMs, they are usually turnkey integrated circuits intended to be embedded in a system, usually soldered to a PC board.

## Features

Security measures used in secure cryptoprocessors:

- Tamper-detecting and tamper-evident containment.
- Conductive shield layers in the chip that prevent reading of internal signals.
- Controlled execution to prevent timing delays from revealing any secret information.
- Automatic zeroization of secrets in the event of tampering.
- Chain of trust boot-loader which authenticates the operating system before loading it.
- Chain of trust operating system which authenticates application software before loading it.
- Hardware-based capability registers, implementing a one-way privilege separation model.

## Degree of security

Secure cryptoprocessors, while useful, are not invulnerable to attack, particularly for well-equipped and determined opponents (e.g. a government intelligence agency) who are willing to expend enough resources on the project.

One attack on a secure cryptoprocessor targeted the IBM 4758. A team at the University of Cambridge reported the successful extraction of secret information from an IBM 4758, using a combination of mathematics, and special-purpose codebreaking hardware. However, this attack was not practical in real-world systems because it required the attacker to have full access to all API functions of the device. Normal and recommended practices use the integral access control system to split authority so that no one person could mount the attack.

While the vulnerability they exploited was a flaw in the software loaded on the 4758, and not the architecture of the 4758 itself, their attack serves as a reminder that a security system is only as secure as its weakest link: the strong link of the 4758 hardware was rendered useless by flaws in the design and specification of the software loaded on it.

Smartcards are significantly more vulnerable, as they are more open to physical attack. Additionally, hardware backdoors can undermine security in smartcards and other cryptoprocessors unless investment is made in anti-backdoor design methods.

In the case of full disk encryption applications, especially when implemented without a boot PIN, a cryptoprocessor would not be secure against a cold boot attack if data remanence could be exploited to dump memory contents after the operating system has retrieved the cryptographic keys from its TPM.

However, if all of the sensitive data is stored only in cryptoprocessor memory and not in external storage, and the cryptoprocessor is designed to be unable to reveal keys or decrypted or unencrypted data on chip bonding pads or solder bumps, then such protected data would be accessible only by probing the cryptoprocessor chip after removing any packaging and metal shielding layers from the cryptoprocessor chip. This would require both physical possession of the device as well as skills and equipment beyond that of most technical personnel.

Other attack methods involve carefully analyzing the timing of various operations that might vary depending on the secret value or mapping the current consumption versus time to identify differences in the way that '0' bits are handled internally vs. '1' bits. Or the attacker may apply temperature extremes, excessively high or low clock frequencies or supply voltage that exceeds the specifications in order to induce a fault. The internal design of the cryptoprocessor can be tailored to prevent these attacks.

Some secure cryptoprocessors contain dual processor cores and generate inaccessible encryption keys when needed so that even if the circuitry is reverse engineered, it will not reveal any keys that are necessary to securely decrypt software booted from encrypted flash memory or communicated between cores.

The first single-chip cryptoprocessor design was for copy protection of personal computer software (see US Patent 4,168,396, Sept 18, 1979) and was inspired by Bill Gates's Open Letter to Hobbyists.

## History

The hardware security module (HSM), a type of secure cryptoprocessor, was invented by Egyptian-American engineer Mohamed M. Atalla, in 1972. He invented a high security module dubbed the "Atalla Box" which encrypted PIN and ATM messages, and protected offline devices with an un-guessable PIN-generating key. In 1972, he filed a patent for the device. He founded Atalla Corporation (now Utimaco Atalla) that year, and commercialized the "Atalla Box" the following year, officially as the Identikey system. It was a card reader and customer identification system, consisting of a card reader console, two customer PIN pads, intelligent controller and built-in electronic interface package. It allowed the customer to type in a secret code, which is transformed by the device, using a microprocessor, into another code for the teller. During a transaction, the customer's account number was read by the card reader. It was a success, and led to the wide use of high security modules.

Fearful that Atalla would dominate the market, banks and credit card companies began working on an international standard in the 1970s. The IBM 3624, launched in the late 1970s, adopted a similar PIN verification process to the earlier Atalla system. Atalla was an early competitor to IBM in the banking security market.

At the National Association of Mutual Savings Banks (NAMSB) conference in January 1976, Atalla unveiled an upgrade to its Identikey system, called the Interchange Identikey. It added the capabilities of processing online transactions and dealing with network security. Designed with the focus of taking bank transactions online, the Identikey system was extended to shared-facility operations. It was consistent and compatible with various switching networks, and was capable of resetting itself electronically to any one of 64,000 irreversible nonlinear algorithms as directed by card data information. The Interchange Identikey device was released in March 1976. Later in 1979, Atalla introduced the first network security processor (NSP). Atalla's HSM products protect 250 million card transactions every day as of 2013, and secure the majority of the world's ATM transactions as of 2014.
