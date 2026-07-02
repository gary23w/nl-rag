---
title: "VeraCrypt"
source: https://en.wikipedia.org/wiki/VeraCrypt
domain: encryption-at-rest
license: CC-BY-SA-4.0
tags: encryption at rest, full disk encryption, data at rest, linux unified key setup, database encryption
fetched: 2026-07-02
---

# VeraCrypt

**VeraCrypt** is a free and open-source utility for on-the-fly encryption (OTFE). The software can create a virtual encrypted disk that works just like a regular disk, but within a file. It can also encrypt a partition or (in Microsoft Windows) the entire storage device with pre-boot authentication.

VeraCrypt is a fork of the discontinued TrueCrypt project. It was initially released on 22 June 2013. Many security improvements have been implemented and concerns within the TrueCrypt code audits have been addressed. VeraCrypt includes optimizations to the original cryptographic hash functions and ciphers, which boost performance on modern central processing units.

## Encryption scheme

VeraCrypt employs AES, Serpent, Twofish, Camellia, and Kuznyechik as ciphers. Version 1.19 stopped using the Magma cipher in response to a security audit. For additional security, ten different combinations of cascaded algorithms are available:

- AES–Twofish
- AES–Twofish–Serpent
- Camellia–Kuznyechik
- Camellia–Serpent
- Kuznyechik–AES
- Kuznyechik–Serpent–Camellia
- Kuznyechik–Twofish
- Serpent–AES
- Serpent–Twofish–AES
- Twofish–Serpent

The cryptographic hash functions available for use in VeraCrypt are BLAKE2s-256, SHA-256, SHA-512, Streebog and Whirlpool. VeraCrypt used to have support for RIPEMD-160, but it has since been removed in version 1.26.

VeraCrypt's block cipher mode of operation is XTS. It generates the header key and the secondary header key (XTS mode) using PBKDF2 with a 512-bit salt. By default, they go through 200,000 or 500,000 iterations, depending on the underlying hash function used and whether it is system or non-system encryption. The user can customize it to lower these numbers to as low as 2,048 and 16,000, respectively.

## Security improvements

- The VeraCrypt development team considered the TrueCrypt storage format too vulnerable to a National Security Agency (NSA) attack, so it created a new format incompatible with that of TrueCrypt. Support for the older TrueCrypt format was dropped in October 2023 starting with VeraCrypt 1.26, but older versions of VeraCrypt are still capable of opening and converting volumes previously created in the TrueCrypt format.
- An independent security audit of TrueCrypt released 29 September 2015 found TrueCrypt includes two vulnerabilities in the Windows installation driver allowing an attacker arbitrary code execution and privilege escalation via DLL hijacking. This was fixed in VeraCrypt in January 2016.
- While TrueCrypt uses 1,000 iterations of the PBKDF2-RIPEMD-160 algorithm for system partitions, VeraCrypt uses either 200,000 iterations (SHA-256, BLAKE2s-256, Streebog) or 500,000 iterations (SHA-512, Whirlpool) by default (which is customizable by user to be as low as 2,048 and 16,000 respectively). For standard containers and non-system partitions, VeraCrypt uses 500,000 iterations by default regardless of the hashing algorithm chosen (which is customizable by user to be as low as 16,000). While these default settings make VeraCrypt slower at opening encrypted partitions, it also makes password-guessing attacks slower.
- Additionally, since version 1.12, a new feature called "Personal Iterations Multiplier" (PIM) provides a parameter whose value is used to control the number of iterations used by the header key derivation function, thereby making brute-force attacks potentially even more difficult. VeraCrypt out of the box uses a reasonable PIM value to improve security, but users can provide a higher value to enhance security. The primary downside of this feature is that it makes the process of opening encrypted archives even slower.
- A vulnerability in the bootloader was fixed on Windows and various optimizations were made as well. The developers added support for SHA-256 to the system boot encryption option and also fixed a ShellExecute security issue. Linux and macOS users benefit from support for hard drives with sector sizes larger than 512. Linux also received support for the NTFS formatting of volumes.
- Unicode passwords are supported on all operating systems since version 1.17 (except for system encryption on Windows).
- VeraCrypt added the capability to boot system partitions using UEFI in version 1.18a.
- Option to enable/disable support for the TRIM command for both system and non-system drives was added in version 1.22.
- Erasing the system encryption keys from RAM during shutdown/reboot helps mitigate some cold boot attacks, added in version 1.24.
- RAM encryption for keys and passwords on 64-bit systems was added in version 1.24.

### VeraCrypt audit

QuarksLab conducted an audit of version 1.18 on behalf of the Open Source Technology Improvement Fund (OSTIF), which took 32 man-days. The auditor published the results on 17 October 2016. On the same day, IDRIX released version 1.19, which resolved major vulnerabilities identified in the audit.

Fraunhofer Institute for Secure Information Technology (SIT) conducted another audit in 2020, following a request by Germany's Federal Office for Information Security (BSI), and published the results in October 2020.

## 2026 signing certificate revocation

In March 2026, VeraCrypt’s lead developer Mounir Idrassi disclosed that Microsoft had terminated the developer account used to digitally sign the software’s Windows drivers and UEFI bootloader. As a result, no new Windows releases could be published; Linux and macOS updates remained unaffected. The same issue affected other Windows applications, including WireGuard, MemTest86, and Windscribe.

Idrassi stated that he had attempted to sign Windows drivers for version 1.26.27 in January 2026, but his account was terminated with an automated message stating his company “did not meet verification requirements” – without specifics or any appeal mechanism.

The certificate authority (CA) used for existing signatures was set to be revoked in late June 2026. Idrassi warned that Windows systems with Secure Boot enabled might then fail to load VeraCrypt’s bootloader, which may have rendered encrypted drives unbootable unless the CA issue was resolved.

As of April 10 2026, Microsoft restored Idrassi's access to his Microsoft Partner Center account, allowing him to sign new versions. Idrassi then released a VeraCrypt 1.26.28 maintenance release with newly Microsoft-signed EFI bootloader components for current 1.26.x users, so people do not have to wait for VeraCrypt 1.27. The old VeraCrypt bootloader will still work even after the certificate expires, but future Windows configurations may require bootloaders signed with the new certificate.

## Security precautions

There are several kinds of attacks to which all software-based disk encryption is vulnerable. As with TrueCrypt, the VeraCrypt documentation instructs users to follow various security precautions to mitigate these attacks, several of which are detailed below.

### Encryption keys stored in memory

VeraCrypt stores its keys in random-access memory (RAM); on some personal computers dynamic random-access memory (DRAM) will maintain its contents for several seconds after power is cut, or longer if the temperature is lowered. Even if there is some degradation in the memory contents, various algorithms may be able to recover the keys. This method, known as a cold boot attack, which would apply in particular to a notebook computer obtained while in power-on, suspended, or screen-locked mode, was successfully used to attack a file system protected by TrueCrypt versions 4.3a and 5.0a in 2008. With version 1.24, VeraCrypt added the option of encrypting the in-RAM keys and passwords on x86-64 editions of Microsoft Windows, with a CPU overhead of less than 10%, and the option of erasing all encryption keys from memory when a new device is connected.

### Tampered hardware

VeraCrypt documentation states that VeraCrypt is unable to secure data on a computer if an attacker physically accessed it and VeraCrypt is then used on the compromised computer by the user again. This does not affect the common case of a stolen, lost, or confiscated computer. The attacker having physical access to a computer can, for example, install a hardware or a software keylogger, a bus-mastering device capturing memory or install any other malicious hardware or software, allowing the attacker to capture unencrypted data (including encryption keys and passwords) or to decrypt encrypted data using captured passwords or encryption keys. Therefore, physical security is a basic premise of a secure system.

Some kinds of malware are designed to log keystrokes, including typed passwords, that may then be sent to the attacker over the Internet or saved to an unencrypted local drive from which the attacker might be able to read it later, when they gain physical access to the computer.

### Trusted Platform Module

VeraCrypt does not take advantage of Trusted Platform Module (TPM). VeraCrypt FAQ repeats the negative opinion of the original TrueCrypt developers verbatim. The TrueCrypt developers were of the opinion that the exclusive purpose of the TPM is "to protect against attacks that require the attacker to have administrator privileges, or physical access to the computer". The attacker who has physical or administrative access to a computer can circumvent TPM, e.g., by installing a hardware keystroke logger, by resetting TPM, or by capturing memory contents and retrieving TPM-issued keys. The condemning text goes so far as to claim that TPM is entirely redundant.

It is true that after achieving either unrestricted physical access or administrative privileges, it is only a matter of time before other security measures in place are bypassed. However, stopping an attacker in possession of administrative privileges has never been one of the goals of TPM. (See Trusted Platform Module § Uses for details.) TPM might, however, reduce the success rate of the cold boot attack described above. TPM is also known to be susceptible to SPI attacks.

## Plausible deniability

As with its predecessor TrueCrypt, VeraCrypt supports plausible deniability by allowing a single "hidden volume" to be created within another volume. The Windows versions of VeraCrypt can create and run a hidden encrypted operating system whose existence may be denied. The VeraCrypt documentation lists ways in which the hidden volume deniability features may be compromised (e.g., by third-party software which may leak information through temporary files or via thumbnails) and possible ways to avoid this.

## Performance

VeraCrypt supports parallelized encryption for multi-core systems. On Microsoft Windows, pipelined read and write operations (a form of asynchronous processing) to reduce the performance hit of encryption and decryption. On processors supporting the AES-NI instruction set, VeraCrypt supports hardware-accelerated AES to further improve performance. On 64-bit CPUs VeraCrypt uses optimized assembly implementation of Twofish, Serpent, and Camellia.

## License and source model

VeraCrypt was forked from the since-discontinued TrueCrypt project in 2013, and originally contained mostly TrueCrypt code released under the TrueCrypt License 3.0. In the years since, more and more of VeraCrypt's code has been rewritten and released under the permissive Apache License 2.0.

The TrueCrypt license is generally considered to be source-available but not free and open source. The Apache license is universally considered to be free and open source. The mixed VeraCrypt license is widely but not universally considered to be free and open source.

On 28 May 2014 TrueCrypt ceased development under unusual circumstances, and there exists no way to contact the former developers.

VeraCrypt is considered to be free and open source by:

- PC World
- Techspot
- DuckDuckGo's Open Source Technology Improvement Fund
- SourceForge
- Open Tech Fund
- Fosshub
- opensource.com
- fossmint
- The current VeraCrypt development team

VeraCrypt is not considered free and open source by:

- Debian Debian considers all software that does not meet the guidelines of its DFSG to be non-free.

The original TrueCrypt license (but not necessarily the current combined VeraCrypt license) is not considered free and open source by:

- The Free Software Foundation
- At least one member of the Open Source Initiative (OSI). The director expressed concern about an older version of the TrueCrypt license, but the OSI has not published a determination regarding either TrueCrypt or VeraCrypt.

## Use for criminal purposes

VeraCrypt has been used by consumers of child pornography to conceal illicit materials, with the FBI being unable to decrypt the encrypted content, leading to requests by prosecutors to force the defendants to hand over their passwords under the *foregone conclusion* doctrine of the All Writs Act.
