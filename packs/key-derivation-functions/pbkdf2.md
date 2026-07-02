---
title: "PBKDF2"
source: https://en.wikipedia.org/wiki/PBKDF2
domain: key-derivation-functions
license: CC-BY-SA-4.0
tags: key derivation function, password based key derivation, kdf salt stretching, hkdf extract expand
fetched: 2026-07-02
---

# PBKDF2

In cryptography, **PBKDF1** and **PBKDF2** (**Password-Based Key Derivation Function 1** and **2**) are key derivation functions with a sliding computational cost, used to reduce vulnerability to brute-force attacks.

PBKDF2 is part of RSA Laboratories' Public-Key Cryptography Standards (PKCS) series, specifically PKCS #5 v2.0, also published as Internet Engineering Task Force's RFC 2898. It supersedes PBKDF1, which could only produce derived keys up to 160 bits long. RFC 8018 (PKCS #5 v2.1), published in 2017, recommends PBKDF2 for password hashing.

## Purpose and operation

PBKDF2 applies a pseudorandom function, such as hash-based message authentication code (HMAC), to the input password or passphrase along with a salt value and repeats the process many times to produce a *derived key*, which can then be used as a cryptographic key in subsequent operations. The added computational work makes password cracking much more difficult, and is known as key stretching.

While the recommended minimum number of iterations was 1,000 when the standard was written in the year 2000, the parameter is intended to be increased over time as CPU speeds increase. A Kerberos standard in 2005 recommended 4,096 iterations; Apple reportedly used 2,000 for iOS 3, and 10,000 for iOS 4; while LastPass in 2011 used 5,000 iterations for JavaScript clients and 100,000 iterations for server-side hashing. In 2023, OWASP recommended to use 600,000 iterations for PBKDF2-HMAC-SHA256 and 220,000 for PBKDF2-HMAC-SHA512.

Having a salt added to the password reduces the ability to use precomputed hashes (rainbow tables) for attacks, and means that multiple passwords have to be tested individually, not all at once. The public key cryptography standard recommends a salt length of at least 64 bits. The US National Institute of Standards and Technology recommends a salt length of at least 128 bits.

## Key derivation process

PBKDF2 has five input parameters:

DK = PBKDF2(PRF,

Password

,

Salt

,

c

,

dkLen

)

where:

- PRF is a pseudorandom function of two parameters with output length *hLen* (e.g., a keyed HMAC)
- *Password* is the master password from which a derived key is generated
- *Salt* is a sequence of bits, known as a cryptographic salt
- *c* is the number of iterations desired
- *dkLen* is the desired bit-length of the derived key
- *DK* is the generated derived key

Each *hLen*-bit block T*i* of derived key *DK*, is computed as follows (with + marking string concatenation):

DK

= T

1

+ T

2

+ ⋯ + T

dkLen

/

hLen

T

i

= F(

Password

,

Salt

,

c

,

i

)

The function F is the xor (^) of *c* iterations of chained PRFs. The first iteration of PRF uses *Password* as the PRF key and *Salt* concatenated with *i* encoded as a big-endian 32-bit integer as the input. (Note that *i* is a 1-based index.) Subsequent iterations of PRF use *Password* as the PRF key and the output of the previous PRF computation as the input:

F(

Password

,

Salt

,

c

,

i

) = U

1

^ U

2

^ ⋯ ^ U

c

where:

U

1

= PRF(

Password

,

Salt

+ INT_32_BE(

i

))

U

2

= PRF(

Password

, U

1

)

⋮

U

c

= PRF(

Password

, U

c

-1

)

For example, WPA2 uses:

DK = PBKDF2(HMAC-SHA1,

passphrase

,

ssid

, 4096, 256)

PBKDF1 had a simpler process: the initial *U* (called *T* in this version) is created by PRF(*Password* + *Salt*), and the following ones are simply PRF(*U*previous). The key is extracted as the first *dkLen* bits of the final hash, which is why there is a size limit.

## HMAC collisions

PBKDF2 has an interesting property when using HMAC as its pseudo-random function. It is possible to trivially construct any number of different password pairs with collisions within each pair. If a supplied password is longer than the block size of the underlying HMAC hash function, the password is first pre-hashed into a digest, and that digest is instead used as the password. For example, the following password is too long:

- **Password:** `plnlrtfpijpuhqylxbgqiiyipieyxvfsavzgxbbcfusqkozwpngsyejqlmjsytrmd`

therefore, when using HMAC-SHA1, it is pre-hashed using SHA-1 into:

- **SHA1** (hex): `65426b585154667542717027635463617226672a`

Which can be represented in ASCII as:

- **SHA1** (ASCII): `eBkXQTfuBqp'cTcar&g*`

This means regardless of the salt or iterations, PBKDF2-HMAC-SHA1 will generate the same key bytes for the passwords:

- "plnlrtfpijpuhqylxbgqiiyipieyxvfsavzgxbbcfusqkozwpngsyejqlmjsytrmd"
- "eBkXQTfuBqp'cTcar&g*"

For example, using:

- **PRF**: HMAC-SHA1
- **Salt:** A009C1A485912C6AE630D3E744240B04
- **Iterations:** 1,000
- **Derived key length:** 16 bytes

The following two function calls:

```mw
PBKDF2-HMAC-SHA1("plnlrtfpijpuhqylxbgqiiyipieyxvfsavzgxbbcfusqkozwpngsyejqlmjsytrmd", ...)
PBKDF2-HMAC-SHA1("eBkXQTfuBqp'cTcar&g*", ...)
```

will generate the same derived key bytes (`17EB4014C8C461C300E9B61518B9A18B`). These derived key collisions do not represent a security vulnerability – as one still must know the original password in order to generate the *hash* of the password.

## Alternatives to PBKDF2

One weakness of PBKDF2 is that while its number of iterations can be adjusted to make it take an arbitrarily large amount of computing time, it can be implemented with a small circuit and very little RAM, which makes brute-force attacks using application-specific integrated circuits or graphics processing units relatively cheap. The bcrypt password hashing function requires a larger amount of RAM (but still not tunable separately, i.e. fixed for a given amount of CPU time) and is significantly stronger against such attacks, while the more modern scrypt key derivation function can use arbitrarily large amounts of memory and is therefore more resistant to ASIC and GPU attacks.

In 2013, the Password Hashing Competition (PHC) was held to develop a more resistant approach. On 20 July 2015 Argon2 was selected as the final PHC winner, with special recognition given to four other password hashing schemes: Catena, Lyra2, yescrypt and Makwa. Another alternative is Balloon hashing, which is recommended in NIST password guidelines.

To limit a brute-force attack, it is possible to make each password attempt require an online interaction, without harming the confidentiality of the password. This can be done using an oblivious pseudorandom function to perform password hardening. This can be done as alternative to, or as an additional step in, a PBKDF.
