---
title: "Padding oracle attack"
source: https://en.wikipedia.org/wiki/Padding_oracle_attack
domain: authenticated-encryption
license: CC-BY-SA-4.0
tags: authenticated encryption, aead cipher mode, galois counter mode, encrypt then mac
fetched: 2026-07-02
---

# Padding oracle attack

In cryptography, a **padding oracle attack** is an attack which uses the padding validation of a cryptographic message to decrypt the ciphertext. In cryptography, variable-length plaintext messages often have to be padded (expanded) to be compatible with the underlying cryptographic primitive. The attack relies on having a "padding oracle" which freely responds to queries about whether a message is correctly padded or not. The information could be directly given, or leaked through a side-channel.

The earliest well-known attack that uses a padding oracle is Bleichenbacher's attack of 1998, which attacks RSA with PKCS #1 v1.5 padding. The term "padding oracle" appeared in literature in 2002, after Serge Vaudenay's attack on the CBC mode decryption used within symmetric block ciphers. Variants of both attacks continue to find success more than one decade after their original publication.

## Asymmetric cryptography

In 1998, Daniel Bleichenbacher published a seminal paper on what became known as Bleichenbacher's attack (also known as "million message attack"). The attack uses a padding oracle against RSA with PKCS #1 v1.5 padding, but it does not include the term. Later authors have classified his attack as a padding oracle attack.

Manger (2001) reports an attack on the replacement for PKCS #1 v1.5 padding, PKCS #1 v2.0 "OAEP".

## Symmetric cryptography

In symmetric cryptography, the padding oracle attack can be applied to the CBC mode of operation. Leaked data on padding validity can allow attackers to decrypt (and sometimes encrypt) messages through the oracle using the oracle's key, without knowing the encryption key.

Compared to Bleichenbacher's attack on RSA with PKCS #1 v1.5, Vaudenay's attack on CBC is much more efficient. Both attacks target crypto systems commonly used for the time: CBC is the original mode used in Secure Sockets Layer (SSL) and had continued to be supported in TLS.

A number of mitigations have been performed to prevent the decryption software from acting as an oracle, but newer attacks based on timing have repeatedly revived this oracle. TLS 1.2 introduces a number of authenticated encryption with additional data modes that do not rely on CBC.

### Padding oracle attack on CBC encryption

The standard implementation of CBC decryption in block ciphers is to decrypt all ciphertext blocks, validate the padding, remove the PKCS7 padding, and return the message's plaintext. If the server allows an attacker to hand over arbitrary data, the attacker can use the server as a padding oracle to decrypt (and sometimes encrypt) messages. The only way to prevent this attack is to make sure that the attacker cannot manipulate the data handed over to the algorithm, e.g. by only accepting messages which are secured with a digital signature or message authentication code which the attacker cannot forge.

The mathematical formula for CBC decryption is

$P_{i}=D_{K}(C_{i})\oplus C_{i-1},{\text{ if }}i\in \{1,N\}$

$P_{0}=IV\oplus D_{K}(C_{0}).$

As depicted above, CBC decryption XORs each plaintext block with the previous block. As a result, a single-byte modification in block $C_{1}$ will make a corresponding change to a single byte in $P_{2}$ .

Suppose the attacker has two ciphertext blocks $C_{1},C_{2}$ and wants to decrypt the second block to get plaintext $P_{2}$ . The attacker changes the last byte of $C_{1}$ (creating $C_{1}'$ ) and sends $(IV,C_{1}',C_{2})$ to the server. The server then returns whether or not the padding of the last decrypted block ( $P_{2}'$ ) is correct (a valid PKCS#7 padding). If the padding is correct, the attacker now knows that the last byte of $D_{K}(C_{2})\oplus C_{1}'$ is $\mathrm {0x01}$ , the last two bytes are 0x02, the last three bytes are 0x03, …, or the last eight bytes are 0x08. The attacker can modify the second-last byte (flip any bit) to ensure that the last byte is 0x01. (Alternatively, the attacker can flip earlier bytes and binary search for the position to identify the padding. For example, if modifying the third-last byte is correct, but modifying the second-last byte is incorrect, then the last two bytes are known to be 0x02, allowing both of them to be decrypted.) Therefore, the last byte of $D_{K}(C_{2})$ equals $C_{1}'\oplus \mathrm {0x01}$ . If the padding is incorrect, the attacker can change the last byte of $C_{1}'$ to the next possible value. At most, the attacker will need to make 256 attempts to find the last byte of $P_{2}$ , 255 attempts for every possible byte (256 possible, minus one by pigeonhole principle), plus one additional attempt to eliminate an ambiguous padding.

After determining the last byte of $P_{2}$ , the attacker can use the same technique to obtain the second-to-last byte of $P_{2}$ . The attacker sets the last byte of $P_{2}$ to $\mathrm {0x02}$ by setting the last byte of $C_{1}$ to $D_{K}(C_{2})\oplus \mathrm {0x02}$ . The attacker then uses the same approach described above, this time modifying the second-to-last byte until the padding is correct (0x02, 0x02).

If a block consists of 128 bits (AES, for example), which is 16 bytes, the attacker will obtain plaintext $P_{2}$ in no more than 256⋅16 = 4096 attempts. This is significantly faster than the $2^{128}$ attempts required to bruteforce a 128-bit key.

### Encrypting messages with Padding oracle attack (CBC-R)

CBC-R turns a decryption oracle into an encryption oracle, and is primarily demonstrated against padding oracles.

Using padding oracle attack CBC-R can craft an initialization vector and ciphertext block for any plaintext:

- decrypt any ciphertext *Pi* = PODecrypt( *Ci* ) ⊕ *C**i*−1,
- select previous cipherblock *C**x*−1 freely,
- produce valid ciphertext/plaintext pair *C**x*-1 = *Px* ⊕ PODecrypt( *Ci* ).

To generate a ciphertext that is N blocks long, attacker must perform N numbers of padding oracle attacks. These attacks are chained together so that proper plaintext is constructed in reverse order, from end of message (CN) to beginning message (*C*0, IV). In each step, padding oracle attack is used to construct the IV to the previous chosen ciphertext.

The CBC-R attack will not work against an encryption scheme that authenticates ciphertext (using a message authentication code or similar) before decrypting.

## Attacks using padding oracles

The original attack against CBC was published in 2002 by Serge Vaudenay. Concrete instantiations of the attack were later realised against SSL and IPSec. It was also applied to several web frameworks, including JavaServer Faces, Ruby on Rails and ASP.NET as well as other software, such as the Steam gaming client. In 2012 it was shown to be effective against PKCS 11 cryptographic tokens.

While these earlier attacks were fixed by most TLS implementors following its public announcement, a new variant, the Lucky Thirteen attack, published in 2013, used a timing side-channel to re-open the vulnerability even in implementations that had previously been fixed. As of early 2014, the attack is no longer considered a threat in real-life operation, though it is still workable in theory (see signal-to-noise ratio) against a certain class of machines. As of 2015, the most active area of development for attacks upon cryptographic protocols used to secure Internet traffic are downgrade attack, such as Logjam and Export RSA/FREAK attacks, which trick clients into using less-secure cryptographic operations provided for compatibility with legacy clients when more secure ones are available. An attack called POODLE (late 2014) combines both a downgrade attack (to SSL 3.0) with a padding oracle attack on the older, insecure protocol to enable compromise of the transmitted data. In May 2016 it has been revealed in CVE-2016-2107 that the fix against Lucky Thirteen in OpenSSL introduced another timing-based padding oracle.
