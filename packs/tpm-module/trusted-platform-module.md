---
title: "Trusted Platform Module"
source: https://en.wikipedia.org/wiki/Trusted_Platform_Module
domain: tpm-module
license: CC-BY-SA-4.0
tags: trusted platform module, hardware root of trust, platform integrity measurement, remote attestation protocol, secure cryptoprocessor
fetched: 2026-07-02
---

# Trusted Platform Module

A **Trusted Platform Module** (**TPM**) is a secure cryptoprocessor that implements the **ISO/IEC 11889** standard. Common uses are verifying that the boot process starts from a trusted combination of hardware and software and storing disk encryption keys.

A TPM 2.0 implementation is part of the Windows 11 system requirements.

## History

The first TPM version that was deployed was 1.1b in 2003.

Trusted Platform Module (TPM) was conceived by a computer industry consortium called Trusted Computing Group (TCG). It evolved into *TPM Main Specification Version 1.2* which was standardized by International Organization for Standardization (ISO) and International Electrotechnical Commission (IEC) in 2009 as ISO/IEC 11889:2009. *TPM Main Specification Version 1.2* was finalized on 3 March 2011 completing its revision.

On April 9, 2014, the Trusted Computing Group announced a major upgrade to their specification entitled *TPM Library Specification 2.0*. The group continues work on the standard incorporating errata, algorithmic additions and new commands, with its most recent edition published as 2.0 in November 2019. This version became ISO/IEC 11889:2015.

When a new revision is released, it is divided into multiple parts by the Trusted Computing Group. Each part consists of a document that makes up the whole of the new TPM specification.

- Part 1 Architecture (renamed from Design Principles)
- Part 2 Structures of the TPM
- Part 3 Commands
- Part 4 Supporting Routines (added in TPM 2.0)

### Version differences

While TPM 2.0 addresses many of the same use cases and has similar features, the details are different. TPM 2.0 is not backward compatible with TPM 1.2.

| Specification | TPM 1.2 | TPM 2.0 |
|---|---|---|
| Architecture | A complete specification is intended to consist of a platform-specific protection profile which references a common three part TPM 1.2 library. In practice, only a PC Client protection profile was created for TPM 1.2. Protection profiles for PDA and cellular were intended to be defined, but were never published. | A complete specification consists of a platform-specific specification which references a common four-part TPM 2.0 library. Platform-specific specifications define what parts of the library are mandatory, optional, or banned for that platform; and detail other requirements for that platform. Platform-specific specifications include PC Client, mobile, and Automotive-Thin. |
| Algorithms | SHA-1 and RSA are required. AES is optional. Triple DES was once an optional algorithm in earlier versions of TPM 1.2, but has been removed from TPM 1.2 version 103. The MGF1 hash-based mask generation function that is defined in PKCS#1 is required. | The PC Client Platform TPM Profile (PTP) Specification requires SHA-1 and SHA-256 for hashes; RSA, ECC using the NIST P-256 curve for public-key cryptography and asymmetric digital signature generation and verification; HMAC for symmetric digital signature generation and verification; 128-bit AES for symmetric-key algorithm; and the MGF1 hash-based mask generation function that is defined in PKCS#1. Many other algorithms are also defined but are optional. Note that Triple DES was added into the TPM 2.0 library, but with restrictions to reject weak keys. Also, elliptic cryptography Direct Anonymous Attestation (ECDAA) using Barreto-Naehrig ECC curves which was mandatory in earlier versions has been made optional in the PC Client profile version 1.59. |
| Crypto Primitives | A random number generator, a public-key cryptographic algorithm, a cryptographic hash function, a mask generation function, digital signature generation and verification, and Direct Anonymous Attestation are required. Symmetric-key algorithms and exclusive or are optional. Key generation is also required. | A random number generator, public-key cryptographic algorithms, cryptographic hash functions, symmetric-key algorithms, digital signature generation and verification, mask generation functions, and exclusive or are required by the TCG PC Client Platform TPM Profile (PTP) Specification. ECC-based Direct Anonymous Attestation using the Barreto–Naehrig 256-bit curve is optional for the TCG PC Client Platform TPM Profile (PTP) Specification. The TPM 2.0 common library specification also requires key generation and key derivation functions. |
| Hierarchy | One (storage) | Three (platform, storage and endorsement) |
| Root keys | One (SRK RSA-2048) | Multiple keys and algorithms per hierarchy |
| Authorization | HMAC, PCR, locality, physical presence | Password, HMAC, and policy (which covers HMAC, PCR, locality, and physical presence). |
| NVRAM | Unstructured data | Unstructured data, counter, bitmap, extend, PIN pass and fail |

The TPM 2.0 policy authorization includes the 1.2 HMAC, locality, physical presence, and PCR. It adds authorization based on an asymmetric digital signature, indirection to another authorization secret, counters and time limits, NVRAM values, a particular command or command parameters, and physical presence. It permits the ANDing and ORing of these authorization primitives to construct complex authorization policies.

## Overview

The Trusted Platform Module (TPM) provides:

- A hardware random number generator
- Facilities for the secure generation of cryptographic keys for limited uses.
- Remote attestation: Creates a nearly unforgeable hash key summary of the hardware and software configuration. One could use the hash to verify that the hardware and software have not been changed. The software in charge of hashing the setup determines the extent of the summary.
- Binding: Data is encrypted using the TPM bind key, a unique RSA key descended from a storage key. Computers that incorporate a TPM can create cryptographic keys and encrypt them so that they can only be decrypted by the TPM. This process, often called wrapping or binding a key, can help protect the key from disclosure. Each TPM has a master wrapping key, called the storage root key, which is stored within the TPM itself. User-level RSA key containers are stored with the Windows user profile for a particular user and can be used to encrypt and decrypt information for applications that run under that specific user identity.
- Sealed storage: Specifies the TPM state for the data to be decrypted (unsealed).
- Other Trusted Computing functions for the data to be decrypted (unsealed).

Computer programs can use a TPM for the authentication of hardware devices, since each TPM chip has a unique and secret Endorsement Key (EK) burned in as it is produced. Security embedded in hardware provides more protection than a software-only solution. Its use is restricted in some countries.

## Uses

### Platform integrity

The primary scope of TPM is to ensure the integrity of a platform during boot time. In this context, "integrity" means "behaves as intended", and a "platform" is any computer device regardless of its operating system. This is to ensure that the boot process starts from a trusted combination of hardware and software, and continues until the operating system has fully booted and applications are running.

When TPM is used, the firmware and the operating system are responsible for ensuring integrity.

For example, the Unified Extensible Firmware Interface (UEFI) can use TPM to form a root of trust: The TPM contains several Platform Configuration Registers (PCRs) that allow secure storage and reporting of security-relevant metrics. These metrics can be used to detect changes to previous configurations and decide how to proceed. Examples of such use can be found in Linux Unified Key Setup (LUKS), BitLocker and PrivateCore vCage memory encryption. (See below.)

Another example of platform integrity via TPM is in the use of Microsoft Office 365 licensing and Outlook Exchange.

Another example of TPM use for platform integrity is the Trusted Execution Technology (TXT), which creates a chain of trust. It could remotely attest that a computer is using the specified hardware and software.

### Disk encryption

Full disk encryption utilities, such as dm-crypt, can use this technology to protect the keys used to encrypt the computer's storage devices and provide integrity authentication for a trusted boot pathway that includes firmware and the boot sector.

## Implementations

### Laptops and notebooks

In 2006, new laptops began being sold with a built-in TPM chip. In the future, this concept could be co-located on an existing motherboard chip in computers, or any other device where the TPM facilities could be employed, such as a cellphone. On a PC, either the Low Pin Count (LPC) bus or the Serial Peripheral Interface (SPI) bus is used to connect to the TPM chip.

The Trusted Computing Group (TCG) has certified TPM chips manufactured by Infineon Technologies, Nuvoton, and STMicroelectronics, having assigned TPM vendor IDs to Advanced Micro Devices, Atmel, Broadcom, IBM, Infineon, Intel, Lenovo, National Semiconductor, Nationz Technologies, Nuvoton, Qualcomm, Rockchip, Standard Microsystems Corporation, STMicroelectronics, Samsung, Sinosun, Texas Instruments, and Winbond.

### TPM 2.0

There are five different types of TPM 2.0 implementations (listed in order from most to least secure):

- Discrete TPMs (dTPMs) are dedicated chips that implement TPM functionality in their own tamper resistant semiconductor package. They are the most secure, certified to FIPS-140 with level 3 physical security resistance to attack versus routines implemented in software, and their packages are required to implement some tamper resistance. For example, the TPM for the brake controller in a car is protected from hacking by sophisticated methods.
- Integrated TPMs (iTPMs) are part of another chip. While they use hardware that resists software bugs, they are not required to implement tamper resistance. Intel has integrated TPMs in some of its chipsets.
- Firmware TPMs (fTPMs) are firmware-based (e.g. UEFI) solutions that run in a CPU's trusted execution environment. Intel, AMD and Qualcomm have implemented firmware TPMs.
- Virtual TPMs (vTPMs) are provided by and rely on hypervisors in isolated execution environments that are hidden from the software running inside virtual machines to secure their code from the software in the virtual machines. They can provide a security level comparable to a firmware TPM. Google Cloud Platform has implemented vTPM.
- Software TPMs are software emulators of TPMs that run with no more protection than a regular program gets within an operating system. They depend entirely on the environment that they run in, so they provide no more security than what can be provided by the normal execution environment. They are useful for development purposes.

### Open source

The official TCG reference implementation of the TPM 2.0 Specification has been developed by Microsoft. It is licensed under BSD License and the source code is available on GitHub.

In 2018, Intel open-sourced its Trusted Platform Module 2.0 (TPM2) software stack with support for Linux and Microsoft Windows. The source code is hosted on GitHub and licensed under BSD License.

Infineon funded the development of an open source TPM middleware that complies with the Software Stack (TSS) Enhanced System API (ESAPI) specification of the TCG. It was developed by Fraunhofer Institute for Secure Information Technology (SIT).

IBM's Software TPM 2.0 is an implementation of the TCG TPM 2.0 specification. It is based on the TPM specification Parts 3 and 4 and source code donated by Microsoft. It contains additional files to complete the implementation. The source code is hosted on SourceForge and GitHub and licensed under BSD License.

In 2022, AMD announced that under certain circumstances their fTPM implementation causes performance problems. A fix is available in form of a BIOS-Update.

## Criticism

The Trusted Computing Group (TCG) has faced resistance to the deployment of this technology in some areas, where some authors see possible uses not specifically related to Trusted Computing, which may raise privacy concerns. The concerns include the abuse of remote validation of software to decide what software is allowed to run, and possible ways to follow actions taken by the user and record them in a database in a manner that is completely undetectable to the user.

The TrueCrypt disk encryption utility, as well as its derivative VeraCrypt, do not support TPM. The original TrueCrypt developers were of the opinion that the exclusive purpose of the TPM is "to protect against attacks that require the attacker to have administrator privileges, or physical access to the computer". The attacker who has physical or administrative access to a computer can circumvent TPM, e.g., by installing a hardware keystroke logger, by resetting TPM, or by capturing memory contents and retrieving TPM-issued keys. The condemning text goes so far as to claim that TPM is entirely redundant. The VeraCrypt publisher has reproduced the original allegation with no changes other than replacing "TrueCrypt" with "VeraCrypt". The author is right that, after achieving either unrestricted physical access or administrative privileges, it is only a matter of time before other security measures in place are bypassed. However, stopping an attacker in possession of administrative privileges has never been one of the goals of TPM (see § Uses for details), and TPM can stop some physical tampering.

In 2015, Richard Stallman suggested replacing the term "trusted computing" with the term "treacherous computing" due to the danger that the computer can be made to systematically disobey its owner if the cryptographical keys are kept secret from them. He also considers that TPMs available for PCs in 2015 are not currently dangerous and that there is no reason not to include one in a computer or support it in software due to failed attempts from the industry to use that technology for DRM, but that the TPM2 released in 2022 is precisely the "treacherous computing" threat he had warned of.

In August 2023, Linus Torvalds, who was frustrated with AMD fTPM's stuttering bugs, opined, "Let's just disable the stupid fTPM `hwrnd` thing." He said the CPU-based random number generation, `rdrand`, was equally suitable, despite having its share of bugs.

## Security issues

In 2010, Christopher Tarnovsky presented an attack against TPMs at Black Hat Briefings, where he claimed to be able to extract secrets from a single TPM. He was able to do this after 6 months of work by inserting a probe and spying on an internal bus for the Infineon SLE 66 CL PC.

In case of physical access, computers with TPM 1.2 are vulnerable to cold boot attacks as long as the system is on or can be booted without a passphrase from shutdown, sleep or hibernation, which is the default setup for Windows computers with BitLocker full disk encryption. A fix was proposed, which has been adopted in the specifications for TPM 2.0.

In 2009, the concept of shared authorisation data in TPM 1.2 was found to be flawed. An adversary given access to the data could spoof responses from the TPM. A fix was proposed, which has been adopted in the specifications for TPM 2.0.

In 2015, as part of the Snowden revelations, it was revealed that in 2010 a US CIA team claimed at an internal conference to have carried out a differential power analysis attack against TPMs that was able to extract secrets.

Main Trusted Boot (tboot) distributions before November 2017 are affected by a dynamic root of trust for measurement (DRTM) attack CVE-2017-16837, which affects computers running on Intel's Trusted eXecution Technology (TXT) for the boot-up routine.

In October 2017, it was reported that a code library developed by Infineon, which had been in widespread use in its TPMs, contained a vulnerability, known as ROCA, which generated weak RSA key pairs that allowed private keys to be inferred from public keys. As a result, all systems depending upon the privacy of such weak keys are vulnerable to compromise, such as identity theft or spoofing. Cryptosystems that store encryption keys directly in the TPM without blinding could be at particular risk to these types of attacks, as passwords and other factors would be meaningless if the attacks can extract encryption secrets. Infineon has released firmware updates for its TPMs to manufacturers who have used them.

In 2018, a design flaw in the TPM 2.0 specification for the static root of trust for measurement (SRTM) was reported (CVE-2018-6622). It allows an adversary to reset and forge platform configuration registers which are designed to securely hold measurements of software that are used for bootstrapping a computer. Fixing it requires hardware-specific firmware patches. An attacker abuses power interrupts and TPM state restores to trick TPM into thinking that it is running on non-tampered components.

In 2021, the Dolos Group showed an attack on a discrete TPM, where the TPM chip itself had some tamper resistance, but the other endpoints of its communication bus did not. They read a full-disk-encryption key as it was transmitted across the motherboard, and used it to decrypt the laptop's SSD.

## Availability

As of 2025, a TPM is provided by nearly all PC and notebook manufacturers in their products.

Vendors include:

- Infineon provides both TPM chips and TPM software, which are delivered as OEM versions with new computers as well as separately by Infineon for products with TPM technology which comply with TCG standards. For example, Infineon licensed TPM management software to Broadcom Corp. in 2004.
- Microchip (formerly Atmel) manufactured TPM devices that it claims to be compliant to the Trusted Platform Module specification version 1.2 revision 116 and offered with several interfaces (LPC, SPI, and I2C), modes (FIPS 140-2 certified and standard mode), temperature grades (commercial and industrial), and packages (TSSOP and QFN). Its TPMs support PCs and embedded devices. It also provides TPM development kits to support integration of its TPM devices into various embedded designs.
- Nuvoton Technology Corporation provides TPM devices for PC applications. Nuvoton also provides TPM devices for embedded systems and Internet of Things (IoT) applications via I2C and SPI host interfaces. Nuvoton's TPM complies with Common Criteria (CC) with assurance level EAL 4 augmented with ALC_FLR.1, AVA_VAN.4 and ALC_DVS.2, FIPS 140-2 level 2 with Physical Security and EMI/EMC level 3 and Trusted Computing Group Compliance requirements, all supported within a single device. TPMs produced by Winbond are now part of Nuvoton.
- STMicroelectronics has provided TPMs for PC platforms and embedded systems since 2005. The product offering includes discrete devices with several interfaces supporting Serial Peripheral Interface (SPI) and I2C and different qualification grades (consumer, industrial and automotive). The TPM products are Common Criteria (CC) certified EAL4+ augmented with ALC_FLR.1 and AVA_VAN.5, FIPS 140-2 level 2 certified with physical security level 3 and also Trusted Computing Group (TCG) certified.

There are also hybrid types; for example, TPM can be integrated into an Ethernet controller, thus eliminating the need for a separate motherboard component.

### Field upgrade

Field upgrade is the TCG term for updating the TPM firmware. The update can be between TPM 1.2 and TPM 2.0, or between firmware versions. Some vendors limit the number of transitions between 1.2 and 2.0, and some restrict rollback to previous versions. Platform OEMs such as HP supply an upgrade tool.

Since July 28, 2016, all new Microsoft device models, lines, or series (or updating the hardware configuration of an existing model, line, or series with a major update, such as CPU, graphic cards) implement, and enable by default TPM 2.0.

While TPM 1.2 parts are discrete silicon components, which are typically soldered on the motherboard, TPM 2.0 is available as a discrete (dTPM) silicon component in a single semiconductor package, an integrated component incorporated in one or more semiconductor packages - alongside other logic units in the same package(s), and as a firmware (fTPM) based component running in a trusted execution environment (TEE) on a general purpose System-on-a-chip (SoC).

### Virtual TPM

- Google Compute Engine was the first major cloud provider offering virtualized TPMs (vTPMs) as part of Google Cloud's Shielded VMs product. Amazon Web Services followed in 2022, naming its vTPM offering "Nitro TPM".
- The libtpms library provides software emulation of a Trusted Platform Module (TPM 1.2 and TPM 2.0). It targets the integration of TPM functionality into hypervisors, primarily into Qemu.

### Operating systems

- Windows 11 requires TPM 2.0 support as a minimum system requirement. On many systems TPM is disabled by default which requires changing settings in the computer's UEFI to enable it.
- Windows 8 and later have native support for TPM 2.0.
- Windows 7 can install an official patch to add TPM 2.0 support.
- Windows Vista through Windows 10 have native support for TPM 1.2.
- The Linux kernel supports the Trusted Platform Module 2.0 (TPM 2.0) since version 4.0 (2015).

### Platforms

- Google includes TPMs in Chromebooks as part of their security model.
- Oracle ships TPMs in their X- and T-Series Systems such as T3 or T4 series of servers. Support is included in Solaris 11.
- In 2006, with the introduction of first Macintosh models with Intel processors, Apple started to ship Macs with TPM. Apple never provided an official driver, but there was a port under GPL available. Apple has not shipped a computer with TPM since 2006. Starting in 2016, Apple products began adopting Apple's own trusted hardware component called "Secure Enclave", originally as a separate chip and later as an integrated part of Apple silicon CPUs. Apple Secure Enclave is not TPM-compatible.
- In 2011, Taiwanese manufacturer MSI launched its Windpad 110W tablet featuring an AMD CPU and Infineon Security Platform TPM, which ships with controlling software version 3.7. The chip is disabled by default but can be enabled with the included, pre-installed software.

### Virtualization

- VMware ESXi hypervisor has supported TPM since 4.x, and from 5.0 it is enabled by default.
- Xen hypervisor has support of virtualized TPMs. Each guest gets its own unique, emulated, software TPM.
- KVM, combined with QEMU, has support for virtualized TPMs. As of 2012, it supports passing through the physical TPM chip to a single dedicated guest. QEMU 2.11 released in December 2017 also provides emulated TPMs to guests.
- VirtualBox has support for virtual TPM 1.2 and 2.0 devices starting with version 7.0 released in October 2022.

### Software

- Microsoft operating systems Windows Vista and later use the chip in conjunction with the included disk encryption component named BitLocker. Microsoft had announced that from January 1, 2015, all computers will have to be equipped with a TPM 2.0 module in order to pass Windows 8.1 hardware certification. However, in a December 2014 review of the Windows Certification Program this was instead made an optional requirement. However, TPM 2.0 is required for connected standby systems. Virtual machines running on Hyper-V can have their own virtual TPM module starting with Windows 10 1511 and Windows Server 2016. Microsoft Windows includes two TPM related commands: tpmtool, a utility that can be used to retrieve information about the TPM, and tpmvscmgr, a command-line tool that allows creating and deleting TPM virtual smart cards on a computer.

## Endorsement keys

TPM endorsement keys (EKs) are asymmetric key pairs unique to each TPM. They use the RSA and ECC algorithms. The TPM manufacturer usually provisions endorsement key certificates in TPM non-volatile memory. The certificates assert that the TPM is authentic. Starting with TPM 2.0, the certificates are in X.509 DER format. After the TPM was manufactured, the EKs cannot be changed. For fTPM, the EKs are stored on CPU / chipset when it was manufactured.

These manufacturers typically provide their certificate authority root (and sometimes intermediate) certificates on their web sites.

- AMD
- Infineon
- Intel
- NationZ
- Nuvoton
- ST Micro

## Software libraries

To utilize a TPM, the user needs a software library that communicates with the TPM and provides a friendlier API than the raw TPM communication. Currently, there are several such open-source TPM 2.0 libraries. Some of them also support TPM 1.2, but mostly TPM 1.2 chips are now deprecated and modern development is focused on TPM 2.0.

Typically, a TPM library provides an API with one-to-one mappings to TPM commands. The TCG specification calls this layer the System API (SAPI). This way, the user has more control over the TPM operations, but the complexity is high. To hide some of the complexity, most libraries also offer simpler ways to invoke complex TPM operations. The TCG specification call these two layers Enhanced System API (ESAPI) and Feature API (FAPI).

There is currently only one stack that follows the TCG specification. All the other available open-source TPM libraries use their own form of richer API.

| TPM Libraries | API | TPM 2.0 | TPM 1.2 | Attestation server or example | Microsoft Windows | Linux | Bare metal |
|---|---|---|---|---|---|---|---|
| tpm2-tss | SAPI, ESAPI and FAPI from the TCG specification | Yes | No | No, but there is a separate project | Yes | Yes | Maybe |
| ibmtss | 1:1 mapping to TPM commands + rich API (mild layer on top) | Yes | Partial | Yes, "IBM ACS" | Yes | Yes | No |
| go-tpm | 1:1 mapping to TPM commands + rich API (mild layer on top) | Yes | Partial | Yes, "Go-attestation" | Yes | Yes | No |
| wolfTPM | 1:1 mapping to TPM commands + rich API (wrappers) | Yes | No | Yes, examples are inside the library | Yes | Yes | Yes |
| TSS.MSR | 1:1 mapping to TPM commands + rich API (wrappers) | Yes | No | Yes, examples are inside the library | Yes | Yes | No |

1. There is a separate project called "CHARRA" by Fraunhofer that uses the tpm2-tss library for Remote Attestation. The other stacks have accompanying attestation servers or directly include examples for attestation. IBM offer their open-source Remote Attestation Server called "IBM ACS" on SourceForge and Google have "Go-Attestation" available on GitHub, while "wolfTPM" offers time and local attestation examples directly in its open-source code, also on GitHub.
2. There is an application note about an example project for the AURIX 32-bit SoC using the tpm2-tss library.
3. Requires additional libraries (dotnet) to run on Linux.

These TPM libraries are sometimes also called TPM stacks, because they provide the interface for the developer or user to interact with the TPM. As seen from the table, the TPM stacks abstract the operating system and transport layer, so the user could migrate one application between platforms. For example, by using TPM stack API the user would interact the same way with a TPM, regardless if the physical chip is connected over SPI, I2C or LPC interface to the Host system.
