---
title: "Rabin fingerprint"
source: https://en.wikipedia.org/wiki/Rabin_fingerprint
domain: rabin-karp-algorithm
license: CC-BY-SA-4.0
tags: rabin karp algorithm, rolling hash, string searching algorithm, rabin fingerprint
fetched: 2026-07-02
---

# Rabin fingerprint

The **Rabin fingerprinting scheme** (a.k.a. **Polynomial fingerprinting**) is a method for implementing fingerprints using polynomials over a finite field. It was proposed by Michael O. Rabin.

## Scheme

Given an *n*-bit message *m*0,...,*m**n*-1, we view it as a polynomial of degree *n*-1 over the finite field GF(2).

$f(x)=m_{0}+m_{1}x+\ldots +m_{n-1}x^{n-1}$

We then pick a random irreducible polynomial ⁠ $p(x)$ ⁠ of degree *k* over GF(2), and we define the fingerprint of the message *m* to be the remainder $r(x)$ after division of $f(x)$ by $p(x)$ over GF(2) which can be viewed as a polynomial of degree *k* − 1 or as a *k*-bit number.

## Applications

Many implementations of the Rabin–Karp algorithm internally use Rabin fingerprints.

The *Low Bandwidth Network Filesystem* (LBFS) from MIT uses Rabin fingerprints to implement variable size shift-resistant blocks. The basic idea is that the filesystem computes the cryptographic hash of each block in a file. To save on transfers between the client and server, they compare their checksums and only transfer blocks whose checksums differ. But one problem with this scheme is that a single insertion at the beginning of the file will cause every checksum to change if fixed-sized (e.g. 4 KB) blocks are used. So the idea is to select blocks not based on a specific offset but rather by some property of the block contents. LBFS does this by sliding a 48 byte window over the file and computing the Rabin fingerprint of each window. When the low 13 bits of the fingerprint are zero LBFS calls those 48 bytes a breakpoint and ends the current block and begins a new one. Since the output of Rabin fingerprints are pseudo-random the probability of any given 48 bytes being a breakpoint is $2^{-13}$ (1 in 8192). This has the effect of shift-resistant variable size blocks. *Any* hash function could be used to divide a long file into blocks (as long as a cryptographic hash function is then used to find the checksum of each block): but the Rabin fingerprint is an efficient rolling hash, since the computation of the Rabin fingerprint of region *B* can reuse some of the computation of the Rabin fingerprint of region *A* when regions *A* and *B* overlap.

Note that this is a problem similar to that faced by rsync.
