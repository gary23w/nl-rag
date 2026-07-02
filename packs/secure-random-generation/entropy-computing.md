---
title: "Entropy (computing)"
source: https://en.wikipedia.org/wiki/Entropy_(computing)
domain: secure-random-generation
license: CC-BY-SA-4.0
tags: cryptographically secure random, random number generation, entropy source seeding, deterministic random bit generator
fetched: 2026-07-02
---

# Entropy (computing)

In computing, **entropy** is the randomness collected by an operating system or application for use in cryptography or other uses that require random data. This randomness is often collected from hardware sources (variance in fan noise or HDD), either pre-existing ones such as mouse movements or specially provided randomness generators. A lack of entropy can have a negative impact on performance and security.

## Linux kernel

The Linux kernel generates entropy from keyboard timings, mouse movements, and integrated drive electronics (IDE) timings and makes the random character data available to other operating system processes through the special files /dev/random and /dev/urandom. This capability was introduced in Linux version 1.3.30.

There are some Linux kernel patches allowing one to use more entropy sources. The audio_entropyd project, which is included in some operating systems such as Fedora, allows audio data to be used as an entropy source. Also available are video_entropyd, which calculates random data from a video-source and entropybroker, which includes these three and can be used to distribute the entropy data to systems not capable of running any of these (e.g. virtual machines). Furthermore, one can use the HAVEGE algorithm through haveged to pool entropy. In some systems, network interrupts can be used as an entropy source as well.

## OpenBSD kernel

OpenBSD has integrated cryptography as one of its main goals and has always worked on increasing its entropy for encryption but also for randomising many parts of the OS, including various internal operations of its kernel. Around 2011, two of the random devices were dropped and linked into a single source as it could produce hundreds of megabytes per second of high quality random data on an average system. This significantly reduced the likelihood of depletion of random data by userland programs on OpenBSD once sufficient entropy had been gathered.

## Hurd kernel

A driver ported from the Linux kernel has been made available for the Hurd kernel.

## Solaris

/dev/random and /dev/urandom have been available as Sun packages or patches for Solaris since Solaris 2.6, and have been a standard feature since Solaris 9. As of Solaris 10, administrators can remove existing entropy sources or define new ones via the kernel-level cryptographic framework.

A 3rd-party kernel module implementing /dev/random is also available for releases dating back to Solaris 2.4.

## OS/2

There is a software package for OS/2 that allows software processes to retrieve random data.

## Windows

Microsoft Windows releases newer than Windows 95 use CryptoAPI to gather entropy in a manner similar to the Linux kernel's /dev/random.

Windows's CryptoAPI uses the binary registry key *HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Cryptography\RNG\Seed* to store a seeded value from all of its entropy sources.

Because CryptoAPI is closed-source, some free and open source software applications running on the Windows platform use other measures to get randomness. For example, GnuPG, as of version 1.06, uses a variety of sources such as the number of free bytes in memory that combined with a random seed generates desired randomness it needs.

Programmers using CAPI can get entropy by calling CAPI's CryptGenRandom(), after properly initializing it.

CryptoAPI was deprecated from Windows Vista and higher. New API is called Cryptography API: Next Generation (CNG). Windows's CNG uses the binary registry key *HKEY_LOCAL_MACHINE\SYSTEM\RNG\Seed* to store a seeded value.

Newer version of Windows are able to use a variety of entropy sources:

- TPM if available and enabled on motherboard
- Entropy from UEFI interface (if booted from UEFI)
- RDRAND CPU instruction if available
- Hardware system clock (RTC)
- OEM0 ACPI table content
- Interrupt timings
- Keyboard timings and Mouse movements

## Embedded systems

Embedded systems may have difficulty gathering sufficient entropy, as they are often simple devices with short boot times, and key generation operations that require sufficient entropy are often one of the first things a system may do. Common entropy sources may not exist on these devices, or may not have been active long enough during boot to generate sufficient entropy. Embedded devices often lack rotating disk drives, human interface devices, and even fans, and the network interface, if any, will not have been active for long enough to provide much entropy. Lacking easy access to entropy, some devices may use hard-coded keys to seed random generators, or seed random generators from easily guessed unique identifiers such as the device's MAC address. A simple study demonstrated the widespread use of weak keys by finding many embedded systems such as routers using the same keys. It was thought that the number of weak keys found would have been far higher if simple and often attacker determinable one-time unique identifiers had not been incorporated into the entropy of some of these systems.

## (De)centralized systems

A true random number generator (TRNG) can be a (de)central service. One example of a centralized system where a random number can be acquired is the *randomness beacon service* from the National Institute of Standards and Technology. The Cardano platform uses the participants of their decentralized proof-of-stake protocol to generate random numbers.

## Other systems

There are some software packages that allow one to use a userspace process to gather random characters, exactly what /dev/random does, such as EGD, the Entropy Gathering Daemon.

## Hardware-originated entropy

Modern CPUs and hardware often feature integrated generators that can provide high-quality and high-speed entropy to operating systems. On systems based on the Linux kernel, one can read the entropy generated from such a device through /dev/hw_random. However, sometimes /dev/hw_random may be slow;

There are some companies manufacturing entropy generation devices, and some of them are shipped with drivers for Linux.

On Linux system, one can install the rng-tools package that supports the true random number generators (TRNGs) found in CPUs supporting the RDRAND instruction, Trusted Platform Modules and in some Intel, AMD, or VIA chipsets, effectively increasing the entropy collected into /dev/random and potentially improving the cryptographic potential. This is especially useful on headless systems that have no other sources of entropy.

## Practical implications

System administrators, especially those supervising Internet servers, have to ensure that the server processes will not halt because of entropy depletion. Entropy on servers utilising the Linux kernel, or any other kernel or userspace process that generates entropy from the console and the storage subsystem, is often less than ideal because of the lack of a mouse and keyboard, thus servers have to generate their entropy from a limited set of resources such as IDE timings.

The entropy pool size in Linux is viewable through the file */proc/sys/kernel/random/entropy_avail* and should generally be at least 2000 bits (out of a maximum of 4096). Entropy changes frequently.

Administrators responsible for systems that have low or zero entropy should not attempt to use /dev/urandom as a substitute for /dev/random as this may cause SSL/TLS connections to have lower-grade encryption.

Some software systems change their Diffie-Hellman keys often, and this may in some cases help a server to continue functioning normally even with an entropy bottleneck.

On servers with low entropy, a process can appear hung when it is waiting for random characters to appear in /dev/random (on Linux-based systems). For example, there was a known problem in Debian that caused exim4 to hang in some cases because of this.

### Security

Entropy sources can be used for keyboard timing attacks.

Entropy can affect the cryptography (TLS/SSL) of a server: If a server fails to use a proper source of randomness, the keys generated by the server will be insecure. In some cases a cracker (malicious attacker) can guess some bits of entropy from the output of a pseudorandom number generator (PRNG), and this happens when not enough entropy is introduced into the PRNG.

## Potential sources

Commonly used entropy sources include the mouse, keyboard, and IDE timings, but there are other potential sources. For example, one could collect entropy from the computer's microphone, or by building a sensor to measure the air turbulence inside a disk drive.

For Unix/BSD derivatives there exists a USB based solution that utilizes an ARM Cortex CPU for filtering / securing the bit stream generated by two entropy generator sources in the system.

Cloudflare uses an image feed from a rack of 80 lava lamps as an additional source of entropy.
