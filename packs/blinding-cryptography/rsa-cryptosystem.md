---
title: "RSA cryptosystem"
source: https://en.wikipedia.org/wiki/RSA_(cryptosystem)
domain: blinding-cryptography
license: CC-BY-SA-4.0
tags: cryptographic blinding, rsa blinding defense, message randomization countermeasure, side channel blinding
fetched: 2026-07-02
---

# RSA cryptosystem

(Redirected from

RSA (cryptosystem)

)

The **RSA** (**Rivest–Shamir–Adleman**) **cryptosystem** is a family of public-key cryptosystems (one of the oldest), widely used for secure data transmission. The initialism "RSA" comes from the surnames of Ron Rivest, Adi Shamir and Leonard Adleman, who publicly described the algorithm in 1977. An equivalent system was developed secretly in 1973 at Government Communications Headquarters (GCHQ), the British signals intelligence agency, by the English mathematician Clifford Cocks. That system was declassified in 1997.

RSA is used in digital signature such as RSASSA-PSS or RSA-FDH, public-key encryption of very short messages (almost always a single-use symmetric key in a hybrid cryptosystem) such as RSAES-OAEP, and public-key key encapsulation.

In RSA-based cryptography, a user's *private key*—which can be used to sign messages, or decrypt messages sent to that user—is a pair of large prime numbers chosen at random and kept secret. A user's *public key*—which can be used to verify messages from the user, or encrypt messages so that only that user can decrypt them—is the product of the prime numbers.

The security of RSA is related to the difficulty of factoring the product of two large prime numbers, the "factoring problem". Breaking RSA encryption is known as the RSA problem. Whether it is as difficult as the factoring problem is an open question. There are no published methods to defeat the system if a large enough key is used.

## History

The idea of an asymmetric public-private key cryptosystem is attributed to Whitfield Diffie and Martin Hellman, who published this concept in 1976. They also introduced digital signatures and attempted to apply number theory. Their formulation used a shared-secret-key created from exponentiation of some number, modulo a prime number. However, they left open the problem of realizing a one-way function, possibly because the difficulty of factoring was not well-studied at the time. Moreover, like Diffie-Hellman, RSA is based on modular exponentiation.

Ron Rivest, Adi Shamir, and Leonard Adleman at the Massachusetts Institute of Technology made several attempts over the course of a year to create a function that was hard to invert. Rivest and Shamir, as computer scientists, proposed many potential functions, while Adleman, as a mathematician, was responsible for finding their weaknesses. They tried many approaches, including "knapsack-based" and "permutation polynomials". For a time, they thought what they wanted to achieve was impossible due to contradictory requirements. In April 1977, they spent Passover at the house of a student and drank a good deal of wine before returning to their homes at around midnight. Rivest, unable to sleep, lay on the couch with a math textbook and started thinking about their one-way function. He spent the rest of the night formalizing his idea, and he had much of the paper ready by daybreak. The algorithm is now known as RSA – the initials of their surnames in same order as their paper.

Clifford Cocks, an English mathematician working for the British intelligence agency Government Communications Headquarters (GCHQ), described a similar system in an internal document in 1973. However, given the relatively expensive computers needed to implement it at the time, it was considered to be mostly a curiosity and, as far as is publicly known, was never deployed. His ideas and concepts were not revealed until 1997 due to its top-secret classification.

Kid-RSA (KRSA) is a simplified, insecure public-key cipher published in 1997, designed for educational purposes. Kid-RSA gives insight into RSA and other public-key ciphers, analogous to simplified DES.

## Patent

A patent describing the RSA algorithm was granted to MIT on 20 September 1983: U.S. patent 4,405,829 "Cryptographic communications system and method". From DWPI's abstract of the patent:

> The system includes a communications channel coupled to at least one terminal having an encoding device and to at least one terminal having a decoding device. A message-to-be-transferred is enciphered to ciphertext at the encoding terminal by encoding the message as a number M in a predetermined set. That number is then raised to a first predetermined power (associated with the intended receiver) and finally computed. The remainder or residue, C, is... computed when the exponentiated number is divided by the product of two predetermined prime numbers (associated with the intended receiver).

A detailed description of the algorithm was published in August 1977, in *Scientific American*'s Mathematical Games column. This preceded the patent's filing date of December 1977. Consequently, the patent had no legal standing outside the United States. Had Cocks' work been publicly known, a patent in the United States would not have been legal either.

When the patent was issued, terms of patent were 17 years. The patent was about to expire on 21 September 2000, but RSA Security released the algorithm to the public domain on 6 September 2000.

## Operation

The RSA algorithm involves four steps: key generation, key distribution, public-key operation (used for encryption or verifying a signature), and private key operation (used for decryption or signing a message).

A basic principle behind RSA is the observation that it is practical to find three very large positive integers e, d, and n, such that for all integers x (0 ≤ *x* < *n*), both (*x**e*)*d* and x have the same remainder when divided by n (they are congruent modulo n): $(x^{e})^{d}\equiv x{\pmod {n}}.$ However, when given only e and n, it is infeasible to compute eth roots modulo n; that is, for uniform random y (0 ≤ *y* < *n*), it is extremely difficult to find x such that *x**e* ≡ *y* (mod *n*).

The integers n and e form the public key and d is the private key. The modular exponentiation to the power of e is used in encryption and in verifying signatures, and exponentiation to the power of d is used in decryption and in signing messages.

### Key generation

The keys for the RSA algorithm are generated in the following way:

1. Choose two distinct large prime numbers p and q.
  - To make factoring infeasible, p and q must be chosen at random from a large space of possibilities, such as all prime numbers between 21023 and 21024 (corresponding to a 2,048-bit key). Many different algorithms for prime selection are used in practice.
  - p and q are kept secret.
2. Compute *n* = *pq*.
  - n is used as the modulus for both the public and private keys. Its length, usually expressed in bits, is the key length.
  - n is released as part of the public key.
3. Compute *λ*(*n*), where λ is Carmichael's totient function. Since *n* = *pq*, *λ*(*n*) = lcm(*λ*(*p*), *λ*(*q*)), and since p and q are prime, *λ*(*p*) = *φ*(*p*) = *p* − 1, and likewise *λ*(*q*) = *q* − 1. Hence *λ*(*n*) = lcm(*p* − 1, *q* − 1).
  - The lcm may be calculated through the Euclidean algorithm, since lcm(*a*, *b*) = ⁠|*ab*|/gcd(*a*, *b*)⁠.
  - *λ*(*n*) is kept secret.
4. Choose an integer e such that 1 < *e* < *λ*(*n*) and gcd(*e*, *λ*(*n*)) = 1; that is, e and *λ*(*n*) are coprime.
  - e having a short bit-length and small Hamming weight results in more efficient encryption – the most commonly chosen value for e is 216 + 1 = 65537. The smallest (and fastest) possible value for e is 3, but such a small value for e may expose vulnerabilities in insecure padding schemes.
  - e is released as part of the public key.
5. Determine d as *d* ≡ *e*−1 (mod *λ*(*n*)); that is, d is the modular multiplicative inverse of e modulo *λ*(*n*).
  - This means: solve for d the equation *de* ≡ 1 (mod *λ*(*n*)); d can be computed efficiently by using the extended Euclidean algorithm, since, thanks to e and *λ*(*n*) being coprime, said equation is a form of Bézout's identity, where d is one of the coefficients.
  - d is kept secret as the *private key exponent*.

The *public key* consists of the modulus n and the public exponent e. The *private key* consists of the private exponent d, which must be kept secret. p, q, and *λ*(*n*) must also be kept secret because they can be used to calculate d. In fact, they can all be discarded after d has been computed.

In the original RSA paper, the Euler totient function *φ*(*n*) = (*p* − 1)(*q* − 1) is used instead of *λ*(*n*) for calculating the private exponent d. Since *φ*(*n*) is always divisible by *λ*(*n*), the algorithm works as well. The possibility of using Euler totient function results also from Lagrange's theorem applied to the multiplicative group of integers modulo *pq*. Thus any d satisfying *d*⋅*e* ≡ 1 (mod *φ*(*n*)) also satisfies *d*⋅*e* ≡ 1 (mod *λ*(*n*)). However, computing d modulo *φ*(*n*) will sometimes yield a result that is larger than necessary (i.e. *d* > *λ*(*n*)). Most of the implementations of RSA will accept exponents generated using either method (if they use the private exponent d at all, rather than using the optimized decryption method based on the Chinese remainder theorem described below), but some standards such as FIPS 186-4 (Section B.3.1) may require that *d* < *λ*(*n*). Any "oversized" private exponents not meeting this criterion may always be reduced modulo *λ*(*n*) to obtain a smaller equivalent exponent.

Note: The authors of the original RSA paper carry out the key generation by choosing d and then computing e as the modular multiplicative inverse of d modulo *φ*(*n*), whereas most current implementations of RSA, such as those following PKCS#1, do the reverse—choose e and compute d from it. Since e can safely be small and fixed, whereas d must be chosen from a large enough space to resist attack, the modern approach can reduce the cost of the public-key operation without loss of security.

### Key distribution

Suppose that Bob wants to send secret messages to Alice, or verify messages from Alice. If they decide to use RSA, Bob must know Alice's public key to encrypt his secret messages or verify Alice's messages, and Alice must use her private key to decrypt Bob's secret messages or sign her own messages.

To enable Bob to send his encrypted messages or verify her future messages, Alice transmits her public key (*n*, *e*) to Bob via a reliable, but not necessarily secret, route. Alice's private key (*d*) is never distributed.

### Encryption

After Bob obtains Alice's public key, he can send a message M to Alice.

To do it, he first turns M into an integer m, the padded plaintext, such that 0 ≤ *m* < *n*, by using an agreed-upon reversible protocol known as a padding scheme. He then computes the ciphertext c, using Alice's public key e, by:

$c\equiv m^{e}{\pmod {n}}.$

This can be done reasonably quickly, even for very large numbers, using modular exponentiation. Bob then transmits c to Alice. Note that at least nine values of m will yield a ciphertext c equal to m, but this is very unlikely to occur in practice.

### Decryption

Alice can recover m from c by using her private key exponent d by computing

$c^{d}\equiv (m^{e})^{d}\equiv m{\pmod {n}}.$

Given m, she can recover the original message M by reversing the padding scheme, or discard it as corrupted if the padding is invalid.

Alice **must** discard m if the padding is invalid: if she reveals any information about m when it has invalid padding, an adversary could exploit this to decrypt (or sign) messages without knowing the private key, by sending her random or maliciously crafted ciphertexts and observing how she responds.

### Example

Here is an example of RSA encryption and decryption, ignoring the details of padding:

1. Choose two distinct prime numbers, such as $p=61$ and $q=53$ .
2. Compute *n* = *pq* giving $n=61\times 53=3233.$
3. Compute the Carmichael's totient function of the product as *λ*(*n*) = lcm(*p* − 1, *q* − 1) giving $\lambda (3233)=\operatorname {lcm} (60,52)=780.$
4. Choose any number 1 < *e* < 780 that is coprime to 780. Choosing a prime number for e leaves us only to check that e is not a divisor of 780. Let $e=17$ .
5. Compute d, the modular multiplicative inverse of *e* (mod *λ*(*n*)), yielding $d=413,$ as $1=(17\times 413){\bmod {7}}80.$

The **public key** is (*n* = 3233, *e* = 17). For a padded plaintext message m, the encryption function is ${\begin{aligned}c(m)&=m^{e}{\bmod {n}}\\&=m^{17}{\bmod {3}}233.\end{aligned}}$

The **private key** is (*n* = 3233, *d* = 413). For an encrypted ciphertext c, the decryption function is ${\begin{aligned}m(c)&=c^{d}{\bmod {n}}\\&=c^{413}{\bmod {3}}233.\end{aligned}}$

For instance, in order to encrypt *m* = 65, one calculates $c=65^{17}{\bmod {3}}233=2790.$

To decrypt *c* = 2790, one calculates $m=2790^{413}{\bmod {3}}233=65.$

Both of these calculations can be computed efficiently using the square-and-multiply algorithm for modular exponentiation. In real-life situations the primes selected would be much larger; in our example it would be trivial to factor *n* = 3233 (obtained from the freely available public key) back to the primes p and q. e, also from the public key, is then inverted to get d, thus acquiring the private key.

Practical implementations use the Chinese remainder theorem to speed up the calculation using modulus of factors (mod *pq* using mod *p* and mod *q*).

The values d*p*, d*q* and qinv, which are part of the private key are computed as follows: ${\begin{aligned}d_{p}&=d{\bmod {(}}p-1)=413{\bmod {(}}61-1)=53,\\d_{q}&=d{\bmod {(}}q-1)=413{\bmod {(}}53-1)=49,\\q_{\text{inv}}&=q^{-1}{\bmod {p}}=53^{-1}{\bmod {6}}1=38\\&\Rightarrow (q_{\text{inv}}\times q){\bmod {p}}=38\times 53{\bmod {6}}1=1.\end{aligned}}$

Here is how d*p*, d*q* and qinv are used for efficient decryption (encryption is efficient by choice of a suitable d and e pair): ${\begin{aligned}m_{1}&=c^{d_{p}}{\bmod {p}}=2790^{53}{\bmod {6}}1=4,\\m_{2}&=c^{d_{q}}{\bmod {q}}=2790^{49}{\bmod {5}}3=12,\\h&=(q_{\text{inv}}\times (m_{1}-m_{2})){\bmod {p}}=(38\times -8){\bmod {6}}1=1,\\m&=m_{2}+h\times q=12+1\times 53=65.\end{aligned}}$

### Signing

Suppose Alice wishes to send a signed message m to Bob. She produces a hash value *h* = hash(*m*) of the message m, raises it to the power of d (modulo n), and attaches *s* = *h**d* mod *n* as a "signature" to the message.

### Verifying

When Bob receives the message m and signature s, he uses the same hash algorithm in conjunction with Alice's public key to compute *h* = hash(*m*). He raises the signature s to the power of e (modulo n), and compares the resulting hash value with the message's hash value: $s^{e}\mathrel {\stackrel {?}{\equiv }} h{\pmod {n}}$ If the two agree, he knows that the author of the message was in possession of Alice's private key and that the message has not been tampered with since being sent.

This equation is satisfied when *s* = *h**d* mod *n* because of exponentiation rules: $s^{e}=(h^{d})^{e}=h^{de}=h^{ed}=(h^{e})^{d}\equiv h{\pmod {n}}.$

The modular exponentiation for signing and verification is the same underlying mathematics as for decryption and encryption, but all the other details of padding scheme for secure public-key encryption and hashing for secure digital signature are different.

The use of a hash, first proposed in 1978 by Michael O. Rabin in the related Rabin signature algorithm, and the security of the hash, is essential for security of the signature: if Alice and Bob skipped the hash, and Bob checked for *s**e* ≡ *m* (mod *n*) instead, then anyone could forge the signature *s* = 1 on the message *m* = 1, or take two signed messages (*m*1, *s*1) and (*m*2, *s*2) from Alice and then forge a third by multiplication, (*m*1*m*2, *s*1*s*2), without knowledge of the private key.

## Proofs of correctness

### Proof using Fermat's little theorem

The proof of the correctness of RSA is based on Fermat's little theorem, stating that *a**p* − 1 ≡ 1 (mod *p*) for any integer a and prime p, not dividing a.

We want to show that $(m^{e})^{d}\equiv m{\pmod {pq}}$ for every integer m when p and q are distinct prime numbers and e and d are positive integers satisfying *ed* ≡ 1 (mod *λ*(*pq*)).

Since *λ*(*pq*) = lcm(*p* − 1, *q* − 1) is, by construction, divisible by both *p* − 1 and *q* − 1, we can write $ed-1=h(p-1)=k(q-1)$ for some nonnegative integers h and k.

To check whether two numbers, such as m*ed* and m, are congruent mod *pq*, it suffices (and in fact is equivalent) to check that they are congruent mod *p* and mod *q* separately.

To show *med* ≡ *m* (mod *p*), we consider two cases:

1. If *m* ≡ 0 (mod *p*), m is a multiple of p. Thus *med* is a multiple of p. So *med* ≡ 0 ≡ *m* (mod *p*).
2. If *m* ≢ 0 (mod *p*), $m^{ed}=m^{ed-1}m=m^{h(p-1)}m=(m^{p-1})^{h}m\equiv 1^{h}m\equiv m{\pmod {p}},$ where we used Fermat's little theorem to replace *m**p*−1 mod *p* with 1.

The verification that *med* ≡ *m* (mod *q*) proceeds in a completely analogous way:

1. If *m* ≡ 0 (mod *q*), *med* is a multiple of q. So *med* ≡ 0 ≡ *m* (mod *q*).
2. If *m* ≢ 0 (mod *q*), $m^{ed}=m^{ed-1}m=m^{k(q-1)}m=(m^{q-1})^{k}m\equiv 1^{k}m\equiv m{\pmod {q}}.$

This completes the proof that, for any integer m, and integers e, d such that *ed* ≡ 1 (mod *λ*(*pq*)), $(m^{e})^{d}\equiv m{\pmod {pq}}.$
