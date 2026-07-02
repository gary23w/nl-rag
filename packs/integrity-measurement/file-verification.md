---
title: "File verification"
source: https://en.wikipedia.org/wiki/File_verification
domain: integrity-measurement
license: CC-BY-SA-4.0
tags: integrity measurement architecture, runtime file integrity attestation, linux ima appraisal, measured runtime integrity
fetched: 2026-07-02
---

# File verification

**File verification** is the process of using an algorithm for verifying the integrity of a computer file, usually by checksum. This can be done by comparing two files bit-by-bit, but requires two copies of the same file, and may miss systematic corruptions which might occur to both files. A more popular approach is to generate a hash of the copied file and comparing that to the hash of the original file.

## Integrity verification

File integrity can be compromised, usually referred to as the file becoming corrupted. A file can become corrupted by a variety of ways: faulty storage media, errors in transmission, write errors during copying or moving, software bugs, and so on.

Hash-based verification ensures that a file has not been corrupted by comparing the file's hash value to a previously calculated value. If these values match, the file is presumed to be unmodified. Due to the nature of hash functions, hash collisions may result in false positives, but the likelihood of collisions is often negligible with random corruption.

## Authenticity verification

It is often desirable to verify that a file hasn't been modified in transmission or storage by untrusted parties, for example, to include malicious code such as viruses or backdoors. To verify the authenticity, a classical hash function is not enough as they are not designed to be collision resistant; it is computationally trivial for an attacker to cause deliberate hash collisions, meaning that a malicious change in the file is not detected by a hash comparison. In cryptography, this attack is called a preimage attack.

For this purpose, cryptographic hash functions are employed often. As long as the hash sums cannot be tampered with — for example, if they are communicated over a secure channel — the files can be presumed to be intact. Alternatively, digital signatures can be employed to assure tamper resistance.

## File formats

A **checksum file** is a small file that contains the checksums of other files.

There are a few well-known checksum file formats.

Several utilities, such as md5deep, can use such checksum files to automatically verify an entire directory of files in one operation.

The particular hash algorithm used is often indicated by the file extension of the checksum file.

The ".sha1" file extension indicates a checksum file containing 160-bit SHA-1 hashes in sha1sum format.

The ".md5" file extension, or a file named "MD5SUMS", indicates a checksum file containing 128-bit MD5 hashes in md5sum format.

The ".sfv" file extension indicates a checksum file containing 32-bit CRC32 checksums in simple file verification format.

The "crc.list" file indicates a checksum file containing 32-bit CRC checksums in brik format.

As of 2012, best practice recommendations is to use SHA-2 or SHA-3 to generate new file integrity digests; and to accept MD5 and SHA-1 digests for backward compatibility if stronger digests are not available. The theoretically weaker SHA-1, the weaker MD5, or much weaker CRC were previously commonly used for file integrity checks.

CRC checksums cannot be used to verify the authenticity of files, as CRC32 is not a collision resistant hash function -- even if the hash sum file is not tampered with, it is computationally trivial for an attacker to replace a file with the same CRC digest as the original file, meaning that a malicious change in the file is not detected by a CRC comparison.
