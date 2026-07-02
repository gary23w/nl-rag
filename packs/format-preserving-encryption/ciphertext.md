---
title: "Ciphertext"
source: https://en.wikipedia.org/wiki/Ciphertext
domain: format-preserving-encryption
license: CC-BY-SA-4.0
tags: format preserving encryption, feistel network cipher, fpe ff1 ff3, ciphertext format retention, aes based fpe
fetched: 2026-07-02
---

# Ciphertext

In cryptography, **ciphertext** or **cyphertext** is the result of encryption performed on plaintext using an algorithm, called a cipher. Ciphertext is also known as encrypted or encoded information because it contains a form of the original plaintext that is unreadable by a human or computer without the proper cipher to decrypt it. This process prevents the loss of sensitive information via hacking. Decryption, the inverse of encryption, is the process of turning ciphertext into readable plaintext. Ciphertext is not to be confused with codetext, because the latter is a result of a code, not a cipher.

## Conceptual underpinnings

Let $m\!$ be the plaintext message that Alice wants to secretly transmit to Bob and let $E_{k}\!$ be the encryption cipher, where $_{k}\!$ is a cryptographic key. Alice must first transform the plaintext into ciphertext, $c\!$ , in order to securely send the message to Bob, as follows:

$c=E_{k}(m).\!$

In a symmetric-key system, Bob knows Alice's encryption key. Once the message is encrypted, Alice can safely transmit it to Bob (assuming no one else knows the key). In order to read Alice's message, Bob must decrypt the ciphertext using ${E_{k}}^{-1}\!$ which is known as the decryption cipher, $D_{k}:\!$

$D_{k}(c)=D_{k}(E_{k}(m))=m.\!$

Alternatively, in a non-symmetric key system, everyone, not just Alice and Bob, knows the encryption key; but the decryption key cannot be inferred from the encryption key. Only Bob knows the decryption key $D_{k},$ and decryption proceeds as

$D_{k}(c)=m.$

## Types of ciphers

The history of cryptography began thousands of years ago. Cryptography uses a variety of different types of encryption. Earlier algorithms were performed by hand and are substantially different from modern algorithms, which are generally executed by a machine.

### Historical ciphers

Historical pen and paper ciphers used in the past are sometimes known as classical ciphers. They include:

- Substitution cipher: the units of plaintext are replaced with ciphertext (e.g., Caesar cipher and one-time pad)
  - Polyalphabetic substitution cipher: a substitution cipher using multiple substitution alphabets (e.g., Vigenère cipher and Enigma machine)
  - Polygraphic substitution cipher: the unit of substitution is a sequence of two or more letters rather than just one (e.g., Playfair cipher)
- Transposition cipher: the ciphertext is a permutation of the plaintext (e.g., rail fence cipher)

Historical ciphers are not generally used as a standalone encryption technique because they are quite easy to crack. Many of the classical ciphers, with the exception of the one-time pad, can be cracked using brute force.

### Modern ciphers

Modern ciphers are more secure than classical ciphers and are designed to withstand a wide range of attacks. An attacker should not be able to find the key used in a modern cipher, even if they know any specifics about the plaintext and its corresponding ciphertext. Modern encryption methods can be divided into the following categories:

- Private-key cryptography (symmetric key algorithm): one shared key is used for encryption and decryption
- Public-key cryptography (asymmetric key algorithm): two different keys are used for encryption and decryption

In a symmetric key algorithm (e.g., DES, AES), the sender and receiver have a shared key established in advance: the sender uses the shared key to perform encryption; the receiver uses the shared key to perform decryption. Symmetric key algorithms can either be block ciphers or stream ciphers. Block ciphers operate on fixed-length groups of bits, called blocks, with an unvarying transformation. Stream ciphers encrypt plaintext digits one at a time on a continuous stream of data, with the transformation of successive digits varying during the encryption process.

In an asymmetric key algorithm (e.g., RSA), there are two different keys: a *public key* and a *private key.* The *public key* is published, thereby allowing any sender to perform encryption. The *private key* is kept secret by the receiver, thereby allowing only the receiver to correctly perform decryption.

## Cryptanalysis

Cryptanalysis (also referred to as codebreaking or cracking the code) is the study of applying various methodologies to obtain the meaning of encrypted information, without having access to the cipher required to correctly decrypt the information. This typically involves gaining an understanding of the system design and determining the cipher.

Cryptanalysts can follow one or more attack models to crack a cipher, depending upon what information is available and the type of cipher being analyzed. Ciphertext is generally the most easily obtained part of a cryptosystem and therefore is an important part of cryptanalysis.

### Attack models

- Ciphertext-only: the cryptanalyst has access only to a collection of ciphertexts or code texts. This is the weakest attack model because the cryptanalyst has limited information. Modern ciphers rarely fail under this attack.
- Known-plaintext: the attacker has a set of ciphertexts to which they know the corresponding plaintext
- Chosen-plaintext attack: the attacker can obtain the ciphertexts corresponding to an arbitrary set of plaintexts of their own choosing
  - Batch chosen-plaintext attack: where the cryptanalyst chooses all plaintexts before any of them are encrypted. This is often the meaning of an unqualified use of "chosen-plaintext attack".
  - Adaptive chosen-plaintext attack: where the cryptanalyst makes a series of interactive queries, choosing subsequent plaintexts based on the information from the previous encryptions.
- Chosen-ciphertext attack: the attacker can obtain the plaintexts corresponding to an arbitrary set of ciphertexts of their own choosing
  - Adaptive chosen-ciphertext attack
  - Indifferent chosen-ciphertext attack
- Related-key attack: similar to a chosen-plaintext attack, except the attacker can obtain ciphertexts encrypted under two different keys. The keys are unknown, but the relationship between them is known (e.g., two keys that differ in the one bit).

## Famous ciphertexts

- The Babington Plot ciphers
- The Shugborough inscription
- The Zimmermann Telegram
- The Magic Words are Squeamish Ossifrage
- The cryptogram in "The Gold-Bug"
- Beale ciphers
- Kryptos
- Zodiac Killer ciphers
