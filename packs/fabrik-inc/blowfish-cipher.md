---
title: "Blowfish (cipher)"
source: https://en.wikipedia.org/wiki/Blowfish_(cipher)
domain: fabrik-inc
license: CC-BY-SA-4.0
tags: fabrik inc.
fetched: 2026-07-03
---

# Blowfish (cipher)

**Blowfish** is a symmetric-key block cipher, designed in 1993 by Bruce Schneier and included in many cipher suites and encryption products. Blowfish provides a good encryption rate in software, and no effective cryptanalysis of it has been found to date for smaller files. It is recommended Blowfish should not be used to encrypt files larger than 4GB in size, in which case Twofish should be used instead.

Blowfish has a 64-bit block size and therefore it could be vulnerable to Sweet32 birthday attacks.

Schneier designed Blowfish as a general-purpose algorithm, intended as an alternative to the aging DES and free of the problems and constraints associated with other algorithms. At the time Blowfish was released, many other designs were proprietary, encumbered by patents, or were commercial or government secrets. Schneier has stated that "Blowfish is unpatented, and will remain so in all countries. The algorithm is hereby placed in the public domain, and can be freely used by anyone."

Notable features of the design include key-dependent S-boxes and a highly complex key schedule.

## The algorithm

Blowfish has a 64-bit block size and a variable key length from 32 bits up to 448 bits. It is a 16-round Feistel cipher and uses large key-dependent S-boxes. In structure it resembles CAST-128, which uses fixed S-boxes.

The adjacent diagram shows Blowfish's encryption routine. Each line represents 32 bits. There are five subkey-arrays: one 18-entry P-array (denoted as K in the diagram, to avoid confusion with the Plaintext) and four 256-entry S-boxes (S0, S1, S2 and S3).

Every round *r* consists of 4 actions:

| **Action 1** | XOR the left half (L) of the data with the *r* th P-array entry |
|---|---|
| **Action 2** | Use the XORed data as input for Blowfish's F-function |
| **Action 3** | XOR the F-function's output with the right half (R) of the data |
| **Action 4** | Swap L and R |

The F-function splits the 32-bit input into four 8-bit quarters and uses the quarters as input to the S-boxes. The S-boxes accept 8-bit input and produce 32-bit output. The outputs are added modulo 232 and XORed to produce the final 32-bit output (see image in the upper right corner).

After the 16th round, undo the last swap, and XOR L with K18 and R with K17 (output whitening).

Decryption is exactly the same as encryption, except that P1, P2, ..., P18 are used in the reverse order. This is not so obvious because xor is commutative and associative. A common misconception is to use inverse order of encryption as decryption algorithm (i.e. first XORing P17 and P18 to the ciphertext block, then using the P-entries in reverse order).

Blowfish's key schedule starts by initializing the P-array and S-boxes with values derived from the hexadecimal digits of pi, which contain no obvious pattern (see nothing up my sleeve number). The secret key is then, byte by byte, cycling the key if necessary, XORed with all the P-entries in order. A 64-bit all-zero block is then encrypted with the algorithm as it stands. The resultant ciphertext replaces P1 and P2. The same ciphertext is then encrypted again with the new subkeys, and the new ciphertext replaces P3 and P4. This continues, replacing the entire P-array and all the S-box entries. In all, the Blowfish encryption algorithm will run 521 times to generate all the subkeys – about 4 KB of data is processed.

Because the P-array is 576 bits long, and the key bytes are XORed through all these 576 bits during the initialization, many implementations support key sizes up to 576 bits. The reason for that is a discrepancy between the original Blowfish description, which uses 448-bit keys, and its reference implementation, which uses 576-bit keys. The test vectors for verifying third-party implementations were also produced with 576-bit keys. When asked which Blowfish version is the correct one, Bruce Schneier answered: "The test vectors should be used to determine the one true Blowfish".

Another opinion is that the 448 bits limit is present to ensure that every bit of every subkey depends on every bit of the key, as the last four values of the P-array don't affect every bit of the ciphertext. This point should be taken in consideration for implementations with a different number of rounds, as even though it increases security against an exhaustive attack, it weakens the security guaranteed by the algorithm. And given the slow initialization of the cipher with each change of key, it is granted a natural protection against brute-force attacks, which doesn't really justify key sizes longer than 448 bits.

## Blowfish in pseudocode

```
P[18]            // P-array of 18 elements
S[4][256]        // S-boxes: 4 arrays of 256 elements

function f(x):
    // Calculates a function f on a 32-bit input x, using S-boxes and bit manipulation
    high_byte := (x shifted right by 24 bits)
    second_byte := (x shifted right by 16 bits) AND 0xff
    third_byte := (x shifted right by 8 bits) AND 0xff
    low_byte := x AND 0xff

    h := S[0][high_byte] + S[1][second_byte]
    return (h XOR S[2][third_byte]) + S[3][low_byte]

procedure blowfish_encrypt(L, R):
    // Encrypts two 32-bit halves L and R using the P-array and function f over 16 rounds
    for round := 0 to 15:
        L := L XOR P[round]
        R := f(L) XOR R
        swap values of L and R
    swap values of L and R
    R := R XOR P[16]
    L := L XOR P[17]

procedure blowfish_decrypt(L, R):
    // Decrypts two 32-bit halves L and R using the P-array and function f over 16 rounds in reverse
    for round := 17 down to 2:
        L := L XOR P[round]
        R := f(L) XOR R
        swap values of L and R
    swap values of L and R
    R := R XOR P[1]
    L := L XOR P[0]
 
// Initializes the P-array and S-boxes using the provided key, followed by key expansion
// Initialize P-array with the key values
key_position := 0
for i := 0 to 17:
    k := 0
    for j := 0 to 3:
        k := (k shifted left by 8 bits) OR key[key_position]
        key_position := (key_position + 1) mod key_length
    P[i] := P[i] XOR k

// Blowfish key expansion (521 iterations)
L := 0, R := 0
for i := 0 to 17 by 2:
    blowfish_encrypt(L, R)
    P[i] := L
    P[i + 1] := R

// Fill S-boxes by encrypting L and R
for i := 0 to 3:
    for j := 0 to 255 by 2:
        blowfish_encrypt(L, R)
        S[i][j] := L
        S[i][j + 1] := R
```

## Blowfish in practice

Blowfish is a fast block cipher, except when changing keys. Each new key requires the pre-processing equivalent of encrypting about 4 kilobytes of text, which is very slow compared to other block ciphers. This prevents its use in certain applications, but is not a problem in others.

Blowfish must be initialized with a key. It is good practice to have this key hashed with a hash function before use.

In one application Blowfish's slow key changing is actually a benefit: the password-hashing method (crypt $2, i.e. bcrypt) used in OpenBSD uses an algorithm derived from Blowfish that makes use of the slow key schedule; the idea is that the extra computational effort required gives protection against dictionary attacks. *See* key stretching.

Blowfish has a memory footprint of just over 4 kilobytes of RAM. This constraint is not a problem even for older desktop and laptop computers, though it does prevent use in the smallest embedded systems such as early smartcards.

Blowfish was one of the first secure block ciphers not subject to any patents and therefore freely available for anyone to use. This benefit has contributed to its popularity in cryptographic software.

bcrypt is a password hashing function which, combined with a variable number of iterations (work "cost"), exploits the expensive key setup phase of Blowfish to increase the workload and duration of hash calculations, further reducing threats from brute force attacks.

bcrypt is also the name of a cross-platform file encryption utility developed in 2002 that implements Blowfish.

## Weakness and successors

Blowfish's use of a 64-bit block size (as opposed to e.g. AES's 128-bit block size) makes it vulnerable to birthday attacks, particularly in contexts like HTTPS. In 2016, the SWEET32 attack demonstrated how to leverage birthday attacks to perform plaintext recovery (i.e. decrypting ciphertext) against ciphers with a 64-bit block size. The GnuPG project recommends that Blowfish not be used to encrypt files larger than 4 GB due to its small block size.

A reduced-round variant of Blowfish is known to be susceptible to known-plaintext attacks on reflectively weak keys. Blowfish implementations use 16 rounds of encryption, and are not susceptible to this attack.

Bruce Schneier has recommended migrating to his Blowfish successor, Twofish.

Blowfish2 was released in 2005, developed by Alexander Pukall. It has exactly the same design but has twice as many S tables and uses 64-bit integers instead of 32-bit integers. It no longer works on 64-bit blocks but on 128-bit blocks like AES. Blowfish2 is used for example, in FreePascal.
