---
title: "/dev/random"
source: https://en.wikipedia.org/wiki//dev/random
domain: secure-random-generation
license: CC-BY-SA-4.0
tags: cryptographically secure random, random number generation, entropy source seeding, deterministic random bit generator
fetched: 2026-07-02
---

# /dev/random

In Unix-like operating systems, **/dev/random** and **/dev/urandom** are special files that provide random numbers from a cryptographically secure pseudorandom number generator (CSPRNG). The CSPRNG is seeded with entropy (a value that provides randomness) from environmental noise, collected from device drivers and other sources. Users can obtain random numbers from the CSPRNG simply by reading the file. Not all operating systems implement the same methods for /dev/random and /dev/urandom.

When entropy available is low, /dev/random will block; on newer systems, this typically happens at program startup until entropy is sufficient, before permanently unblocking. The /dev/urandom device typically was never a blocking device, even if the pseudorandom number generator seed was not fully initialized with entropy since boot.

This special file originated in Linux in 1994. It was quickly adopted by other Unix-like operating systems.

## Linux

The Linux kernel provides the separate device files /dev/random and /dev/urandom. Since kernel version 5.6 of 2020, /dev/random only blocks when the CSPRNG hasn't initialized. Once initialized, /dev/random and /dev/urandom behave the same.

In October 2016, with the release of Linux kernel version 4.8, the kernel's /dev/urandom was switched over to a ChaCha20-based cryptographic pseudorandom number generator (CPRNG) implementation by Theodore Ts'o, based on Bernstein's well-regarded stream cipher ChaCha20.

Since version 5.17 of the Linux kernel, the random number generator switched from using the SHA-1 cryptographic hash function in the entropy collector to BLAKE2s, a newer, faster and more secure hash function.

### Original implementation

Random number generation in kernel space was implemented for the first time for Linux in 1994 by Theodore Ts'o. The implementation used secure hashes rather than ciphers, to avoid cryptography export restrictions that were in place when the generator was originally designed. The implementation was also designed with the assumption that any given hash or cipher might eventually be found to be weak, and so the design is durable in the face of any such weaknesses. Fast recovery from pool compromise is not considered a requirement, because the requirements for pool compromise are sufficient for much easier and more direct attacks on unrelated parts of the operating system.

In Ts'o's implementation, the generator keeps an estimate of the number of bits of noise in the entropy pool. From this entropy pool random numbers are created. When read, the /dev/random device will only return random bytes within the estimated number of bits of noise in the entropy pool. When the entropy pool is empty, reads from /dev/random will block until additional environmental noise is gathered. The intent is to serve as a cryptographically secure pseudorandom number generator, delivering output with entropy as large as possible. This is suggested by the authors for use in generating cryptographic keys for high-value or long-term protection.

A counterpart to /dev/random is /dev/urandom ("unlimited"/non-blocking random source) which reuses the internal pool to produce more pseudo-random bits. This means that the call will not block, but the output may contain less entropy than the corresponding read from /dev/random. While /dev/urandom is still intended as a pseudorandom number generator suitable for most cryptographic purposes, the authors of the corresponding man page note that, theoretically, there may exist an as-yet-unpublished attack on the algorithm used by /dev/urandom, and that users concerned about such an attack should use /dev/random instead. However such an attack is unlikely to come into existence, because once the entropy pool is unpredictable it doesn't leak security by a reduced number of bits.

It is also possible to write to /dev/random. This allows any user to mix random data into the pool. Non-random data is harmless, because only a privileged user can issue the ioctl needed to increase the entropy estimate. The current amount of entropy and the size of the Linux kernel entropy pool, both measured in bits, are available in /proc/sys/kernel/random/ and can be displayed by the command `cat /proc/sys/kernel/random/entropy_avail` and `cat /proc/sys/kernel/random/poolsize` respectively.

### Entropy injection

Gutterman, Pinkas, & Reinman in March 2006 published a detailed cryptographic analysis of the Linux random number generator in which they describe several weaknesses. Perhaps the most severe issue they report is with embedded or Live CD systems, such as routers and diskless clients, for which the bootup state is predictable and the available supply of entropy from the environment may be limited. For a system with non-volatile memory, they recommend saving some state from the RNG at shutdown so that it can be included in the RNG state on the next reboot. In the case of a router for which network traffic represents the primary available source of entropy, they note that saving state across reboots "would require potential attackers to either eavesdrop on all network traffic" from when the router is first put into service, or obtain direct access to the router's internal state. This issue, they note, is particularly critical in the case of a wireless router whose network traffic can be captured from a distance, and which may be using the RNG to generate keys for data encryption.

The Linux kernel provides support for several hardware random number generators, should they be installed. The raw output of such a device may be obtained from /dev/hwrng.

With Linux kernel 3.16 and newer, the kernel itself mixes data from hardware random number generators into /dev/random on a sliding scale based on the definable entropy estimation quality of the HWRNG. This means that no userspace daemon, such as rngd from rng-tools, is needed to do that job.

The entropy pool can be improved by programs like timer_entropyd, haveged, randomsound etc. With rng-tools, hardware random number generators like *Entropy Key, etc.* can write to /dev/random. The diehard tests programs diehard, dieharder and ent can test these random number generators.

### Critique of entropy injection

In January 2014, Daniel J. Bernstein published a critique of how Linux mixes different sources of entropy. He outlines an attack in which one source of entropy capable of monitoring the other sources of entropy could modify its output to nullify the randomness of the other sources of entropy. Consider the function ⁠ $H(x,y,z)$ ⁠ where *H* is a hash function and *x*, *y*, and *z* are sources of entropy with *z* being the output of a CPU-based malicious HRNG Z:

1. *Z* generates a random value of *r*.
2. *Z* computes ⁠ $H(x,y,r)$ ⁠.
3. If the output of ⁠ $H(x,y,r)$ ⁠ is equal to the desired value, output *r* as *z*.
4. Else, repeat starting at 1.

Bernstein estimated that an attacker would need to repeat ⁠ $H(x,y,r)$ ⁠ 16 times to compromise DSA and ECDSA, by causing the first four bits of the RNG output to be 0. This is possible because Linux reseeds H on an ongoing basis instead of using a single high quality seed.

Bernstein also argues that entropy injection is pointless once the CSPRNG has been initialized.

In kernel 5.17 (backported to kernel 5.10.119), Jason A. Donenfeld offered a new design of the Linux entropy pool infrastructure. Donenfeld reported that the old pool, consisting of a single 4096-bit LFSR is vulnerable to two attacks: (1) an attacker can undo the effect of a known input; (2) if the whole pool's state is leaked, an attacker can set all bits in the pool to zero. His new design, which is faster and safer, uses the blake2s hash function for mixing a 256-bit pool.

## BSD systems

The FreeBSD operating system provides a /dev/urandom link to /dev/random. Both block only until properly seeded. FreeBSD's PRNG (Fortuna) reseeds regularly, and does not attempt to estimate entropy. On a system with small amount of network and disk activity, reseeding is done after a fraction of a second.

DragonFly BSD inherited FreeBSD's random device files when it was forked.

Since OpenBSD 5.1 (May 1, 2012) /dev/random and /dev/arandom uses arc4random, a CSPRNG function based on RC4. The function was changed to use the stronger ChaCha20 with OpenBSD 5.5 (May 1, 2014). The system automatically uses hardware random number generators (such as those provided on some Intel PCI hubs) if they are available, through the OpenBSD Cryptographic Framework. /dev/arandom was removed in OpenBSD 6.3 (April 15, 2018).

NetBSD's implementation of the legacy `arc4random()` API has been switched over to ChaCha20 as well.

## macOS, iOS and other Apple OSes

All Apple OSes have moved to Fortuna since at least December 2019, possibly earlier. It is based on SHA-256. Multiple entropy sources such as the secure enclave RNG, boot phase timing jitter, hardware interrupt (timing assumed) are used. RDSEED/RDRAND is used on Intel-based Macs that support it. Seed (entropy) data is also stored for subsequent reboots.

Prior to the change, macOS and iOS used 160-bit Yarrow based on SHA-1.

There is no difference between /dev/random and /dev/urandom; both behave identically.

## Other operating systems

/dev/random and /dev/urandom are also available on Solaris, NetBSD, Tru64 UNIX 5.1B, AIX 5.2 and HP-UX 11i v2. As with FreeBSD, AIX implements its own Yarrow-based design, however AIX uses considerably fewer entropy sources than the standard /dev/random implementation and stops refilling the pool when it thinks it contains enough entropy.

In Windows NT, similar functionality is delivered by ksecdd.sys, but reading the special file \Device\KsecDD does not work as in UNIX. The documented methods to generate cryptographically random bytes are CryptGenRandom and RtlGenRandom. Windows PowerShell provides access to a cryptographically secure pseudorandom number generator via the Get-SecureRandom cmdlet.
