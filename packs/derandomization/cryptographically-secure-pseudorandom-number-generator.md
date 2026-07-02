---
title: "Cryptographically secure pseudorandom number generator"
source: https://en.wikipedia.org/wiki/Cryptographically_secure_pseudorandom_number_generator
domain: derandomization
license: CC-BY-SA-4.0
tags: derandomization technique, pseudorandom generator, method of conditional probabilities, small bias sample space
fetched: 2026-07-02
---

# Cryptographically secure pseudorandom number generator

A **cryptographically secure pseudorandom number generator** (**CSPRNG**) or **cryptographic pseudorandom number generator** (**CPRNG**) is a pseudorandom number generator (PRNG) with properties that make it suitable for use in cryptography. It is also referred to as a **cryptographic random number generator** (**CRNG**).

## Background

Most cryptographic applications require random numbers, for example:

- key generation
- initialization vectors
- nonces
- salts in certain signature schemes, including ECDSA and RSASSA-PSS
- token generation

The "quality" of the randomness required for these applications varies. For example, creating a nonce in some protocols needs only uniqueness. On the other hand, the generation of a master key requires a higher quality, such as more entropy. And in the case of one-time pads, the information-theoretic guarantee of perfect secrecy only holds if the key material comes from a true random source with high entropy, and thus just any kind of pseudorandom number generator is insufficient.

Ideally, the generation of random numbers in CSPRNGs uses entropy obtained from a high-quality source, generally the operating system's randomness API. However, unexpected correlations have been found in several such ostensibly independent processes. From an information-theoretic point of view, the amount of randomness, the entropy that can be generated, is equal to the entropy provided by the system. But sometimes, in practical situations, numbers are needed with more randomness than the available entropy can provide. Also, the processes to extract randomness from a running system are slow in actual practice. In such instances, a CSPRNG can sometimes be used. A CSPRNG can "stretch" the available entropy over more bits.

## Requirements

The requirements of an ordinary PRNG are also satisfied by a cryptographically secure PRNG, but the reverse is not true. CSPRNG requirements fall into two groups:

1. They pass statistical randomness tests:
  - Every CSPRNG should satisfy the next-bit test. That is, given the first *k* bits of a random sequence, there is no polynomial-time algorithm that can predict the (*k*+1)th bit with probability of success non-negligibly better than 50%.
  - Andrew Yao proved in 1982 that a generator passing the next-bit test will pass all other polynomial-time statistical tests for randomness. In other words, no polynomial-time algorithm would be able to distinguish the output of the RNG from true randomness.
  - Instead of polynomial-time complexity, another metric considered in practice is the absolute number of operations required for a *distinguisher* to tell the output from true randomness. From the number of operations one can also define a security level (bits of security) for a particular CSPRNG against distinguishing attacks.
2. They hold up well under serious attack, even when part of their initial or running state becomes available to an attacker:
  - Every CSPRNG should withstand "state compromise extension attacks". In the event that part or all of its state has been revealed (or guessed correctly), it should be impossible to reconstruct the stream of random numbers prior to the revelation. Additionally, if there is an entropy input while running, it should be infeasible to use knowledge of the input's state to predict future conditions of the CSPRNG state.
  - For instance, if the PRNG under consideration produces output by computing bits of pi in sequence, starting from some unknown point in the binary expansion, it may well satisfy the next-bit test and thus be statistically random, as pi is conjectured to be a normal number. However, this algorithm is not cryptographically secure; an attacker who determines which bit of pi is currently in use (i.e. the state of the algorithm) will be able to calculate all preceding bits as well.

Most PRNGs are not suitable for use as CSPRNGs and will fail on both counts:

1. While most PRNGs' outputs appear random to assorted statistical tests, they do not resist determined reverse engineering. Specialized statistical tests may be found specially tuned to such a PRNG that shows the random numbers not to be truly random. At the same time, because CSPRNGs are designed to resist all statistical tests (and are believed to be secure on this front until such a test has been found), a CSPRNG can replace any true random number generator in any non-cryptographic application as well.
2. For most PRNGs, when their state has been revealed, all past random numbers can be retrodicted, allowing an attacker to read all past messages, as well as future ones. CSPRNGs are designed explicitly to resist this type of cryptanalysis.

## Definitions

In the asymptotic setting, a family of deterministic polynomial time computable functions $G_{k}\colon \{{\texttt {0}},{\texttt {1}}\}^{k}\to \{{\texttt {0}},{\texttt {1}}\}^{p(k)}$ for some polynomial p, is a pseudorandom number generator (PRNG, or PRG in some references), if it stretches the length of its input ( $p(k)>k$ for any k), and if its output is computationally indistinguishable from true randomness, i.e. for any probabilistic polynomial time algorithm A, which outputs 1 or 0 as a distinguisher,

$\left|\Pr _{x\gets \{{\texttt {0}},{\texttt {1}}\}^{k}}[A(G(x))=1]-\Pr _{r\gets \{{\texttt {0}},{\texttt {1}}\}^{p(k)}}[A(r)=1]\right|<\mu (k)$

for some negligible function $\mu$ . (The notation $x\gets X$ means that x is chosen uniformly at random from the set X.)

There is an equivalent characterization: For any function family $G_{k}\colon \{{\texttt {0}},{\texttt {1}}\}^{k}\to \{{\texttt {0}},{\texttt {1}}\}^{p(k)}$ , G is a PRNG if and only if the next output bit of G cannot be predicted by a polynomial time algorithm.

A **forward-secure** PRNG with block length $t(k)$ is a PRNG $G_{k}\colon \{{\texttt {0}},{\texttt {1}}\}^{k}\to \{{\texttt {0}},{\texttt {1}}\}^{k}\times \{{\texttt {0}},{\texttt {1}}\}^{t(k)}$ , where the input string $s_{i}$ with length k is the current state at period i, and the output ( $s_{i+1}$ , $y_{i}$ ) consists of the next state $s_{i+1}$ and the pseudorandom output block $y_{i}$ of period i, that withstands state compromise extensions in the following sense. If the initial state $s_{1}$ is chosen uniformly at random from $\{{\texttt {0}},{\texttt {1}}\}^{k}$ , then for any i, the sequence $(y_{1},y_{2},\dots ,y_{i},s_{i+1})$ must be computationally indistinguishable from $(r_{1},r_{2},\dots ,r_{i},s_{i+1})$ , in which the $r_{i}$ are chosen uniformly at random from $\{{\texttt {0}},{\texttt {1}}\}^{t(k)}$ .

Any PRNG $G\colon \{{\texttt {0}},{\texttt {1}}\}^{k}\to \{{\texttt {0}},{\texttt {1}}\}^{p(k)}$ can be turned into a forward secure PRNG with block length $p(k)-k$ by splitting its output into the next state and the actual output. This is done by setting $G(s)=G_{\texttt {0}}(s)\Vert G_{\texttt {1}}(s)$ , in which $|G_{\texttt {0}}(s)|=|s|=k$ and $|G_{\texttt {1}}(s)|=p(k)-k$ ; then G is a forward secure PRNG with $G_{\texttt {0}}$ as the next state and $G_{\texttt {1}}$ as the pseudorandom output block of the current period.

## Entropy extraction

Santha and Vazirani proved that several bit streams with weak randomness can be combined to produce a higher-quality, quasi-random bit stream. Even earlier, John von Neumann suggested a simple algorithm that can remove a considerable amount of the bias in any bit stream.

## Designs

CSPRNG designs are divided into two classes:

1. Designs based on cryptographic primitives such as ciphers and cryptographic hashes
2. Designs based on mathematical problems thought to be hard

### Designs based on cryptographic primitives

- A secure block cipher can be converted into a CSPRNG by running it in counter mode using, for example, a special construct that the NIST in SP 800-90A calls CTR DRBG. CTR_DBRG typically uses Advanced Encryption Standard (AES).
  - AES-CTR_DRBG is often used as a random number generator in systems that use AES encryption.
  - The NIST CTR_DRBG scheme erases the key *after* the requested randomness is output by running additional cycles. This is wasteful from a performance perspective, but does not immediately cause issues with forward secrecy. However, realizing the performance implications, the NIST recommends an "extended AES-CTR-DRBG interface" for its Post-Quantum Cryptography Project submissions. This interface allows multiple sets of randomness to be generated without intervening erasure, only erasing when the user explicitly signals the end of requests. As a result, the key could remain in memory for an extended time if the "extended interface" is misused. Newer "fast-key-erasure" RNGs erase the key with randomness as soon as randomness is requested.
- A stream cipher can be converted into a CSPRNG. This has been done with RC4, ISAAC, and ChaCha20, to name a few.
- A cryptographically secure hash might also be a base of a good CSPRNG, using, for example, a construct that NIST calls Hash DRBG.
- An HMAC primitive can be used as a base of a CSPRNG, for example, as part of the construct that NIST calls HMAC DRBG.

### Number-theoretic designs

- The Blum Blum Shub algorithm has a security proof based on the difficulty of the quadratic residuosity problem. Since the only known way to solve that problem is to factor the modulus, it is generally regarded that the difficulty of integer factorization provides a conditional security proof for the Blum Blum Shub algorithm. However the algorithm is very inefficient and therefore impractical unless extreme security is needed.
- The Blum–Micali algorithm has a security proof based on the difficulty of the discrete logarithm problem but is also very inefficient.
- Daniel Brown of Certicom wrote a 2006 security proof for Dual EC DRBG, based on the assumed hardness of the *Decisional Diffie–Hellman assumption*, the *x-logarithm problem*, and the *truncated point problem*. The 2006 proof explicitly assumes a lower *outlen* (amount of bits provided per iteration) than in the Dual_EC_DRBG standard, and that the *P* and *Q* in the Dual_EC_DRBG standard (which were revealed in 2013 to be probably backdoored by NSA) are replaced with non-backdoored values.

### Practical schemes

"Practical" CSPRNG schemes not only include an CSPRNG algorithm, but also a way to initialize ("seed") it while keeping the seed secret. A number of such schemes have been defined, including:

- Implementations of /dev/random in Unix-like systems.
  - Yarrow, which attempts to evaluate the entropic quality of its seeding inputs, and uses SHA-1 and 3DES internally. Yarrow was used in macOS and other Apple OS' up until about December 2019, after which it switched to Fortuna.
  - Fortuna, the successor to Yarrow, which does not attempt to evaluate the entropic quality of its inputs; it uses SHA-256 and "any good block cipher". Fortuna is used in FreeBSD. Apple changed to Fortuna for most or all Apple OSs beginning around Dec. 2019.
  - The Linux kernel CSPRNG, which uses ChaCha20 to generate data, and BLAKE2s to ingest entropy.
- *arc4random*, a CSPRNG in Unix-like systems that seeds from /dev/random. It originally is based on RC4, but all main implementations now use ChaCha20.
- *CryptGenRandom*, part of Microsoft's CryptoAPI, offered on Windows. Different versions of Windows use different implementations.
- ANSI X9.17 standard (*Financial Institution Key Management (wholesale)*), which has been adopted as a FIPS standard as well. It takes as input a TDEA (keying option 2) key bundle *k* and (the initial value of) a 64-bit random seed *s*. Each time a random number is required, it executes the following steps:Obtain the current date/time *D* to the maximum resolution possible.Compute a temporary value *t* = TDEA*k*(*D*).Compute the random value *x* = TDEA*k*(*s* ⊕ *t*), where ⊕ denotes bitwise exclusive or.Update the seed *s* = TDEA*k*(*x* ⊕ *t*).

Obviously, the technique is easily generalized to any block cipher; AES has been suggested. If the key *k* is leaked, the entire X9.17 stream can be predicted; this weakness is cited as a reason for creating Yarrow.

All these above-mentioned schemes, save for X9.17, also mix the state of a CSPRNG with an additional source of entropy. They are therefore not "pure" pseudorandom number generators, in the sense that the output is not completely determined by their initial state. This addition aims to prevent attacks even if the initial state is compromised.

## Standards

Several CSPRNGs have been standardized. For example:

- FIPS 186-4
- NIST SP 800-90A

This withdrawn standard has four PRNGs. Two of them are uncontroversial and proven: CSPRNGs named Hash_DRBG

and HMAC_DRBG.

The third PRNG in this standard, CTR DRBG, is based on a block cipher running in counter mode. It has an uncontroversial design but has been proven to be weaker in terms of distinguishing attack, than the security level of the underlying block cipher when the number of bits output from this PRNG is greater than two to the power of the underlying block cipher's block size in bits.

When the maximum number of bits output from this PRNG is equal to the 2blocksize, the resulting output delivers the mathematically expected security level that the key size would be expected to generate, but the output is shown to not be indistinguishable from a true random number generator. When the maximum number of bits output from this PRNG is less than it, the expected security level is delivered and the output appears to be indistinguishable from a true random number generator.

It is noted in the next revision that the claimed security strength for CTR_DRBG depends on limiting the total number of generate requests and the bits provided per generate request.

The fourth and final PRNG in this standard is named Dual EC DRBG. It has been shown to not be cryptographically secure and is believed to have a kleptographic NSA backdoor.

- NIST SP 800-90A Rev.1

This is essentially NIST SP 800-90A with Dual_EC_DRBG removed, and is the withdrawn standard's replacement.

- ANSI X9.17-1985 Appendix C
- ANSI X9.31-1998 Appendix A.2.4
- ANSI X9.62-1998 Annex A.4, obsoleted by ANSI X9.62-2005, Annex D (HMAC_DRBG)

A good reference is maintained by NIST.

There are also standards for statistical testing of new CSPRNG designs:

- *A Statistical Test Suite for Random and Pseudorandom Number Generators*, NIST Special Publication 800-22.

## Security flaws

### NSA kleptographic backdoor in the Dual_EC_DRBG PRNG

*The Guardian* and *The New York Times* reported in 2013 that the National Security Agency (NSA) inserted a backdoor into a pseudorandom number generator (PRNG) of NIST SP 800-90A, which allows the NSA to readily decrypt material that was encrypted with the aid of Dual EC DRBG. Both papers reported that, as independent security experts long suspected, the NSA had been introducing weaknesses into CSPRNG standard 800-90; this being confirmed for the first time by one of the top-secret documents leaked to *The Guardian* by Edward Snowden. The NSA worked covertly to get its own version of the NIST draft security standard approved for worldwide use in 2006. The leaked document states that "eventually, NSA became the sole editor". In spite of the known potential for a kleptographic backdoor and other known significant deficiencies with Dual_EC_DRBG, several companies such as RSA Security continued using Dual_EC_DRBG until the backdoor was confirmed in 2013. RSA Security received a $10 million payment from the NSA to do so.

### DUHK attack

On October 23, 2017, Shaanan Cohney, Matthew Green, and Nadia Heninger, cryptographers at the University of Pennsylvania and Johns Hopkins University, released details of the DUHK (Don't Use Hard-coded Keys) attack on WPA2 where hardware vendors use a hardcoded seed key for the ANSI X9.31 RNG algorithm, stating "an attacker can brute-force encrypted data to discover the rest of the encryption parameters and deduce the master encryption key used to encrypt web sessions or virtual private network (VPN) connections."

### Japanese PURPLE cipher machine

During World War II, Japan used a cipher machine for diplomatic communications; the United States was able to crack it and read its messages, mostly because the "key values" used were insufficiently random.
