---
title: "Rolling hash"
source: https://en.wikipedia.org/wiki/Rolling_hash
domain: rabin-karp-algorithm
license: CC-BY-SA-4.0
tags: rabin karp algorithm, rolling hash, string searching algorithm, rabin fingerprint
fetched: 2026-07-02
---

# Rolling hash

A **rolling hash** (also known as recursive hashing or rolling checksum) is a hash function where the input is hashed in a window that moves through the input.

A few hash functions allow a rolling hash to be computed very quickly—the new hash value is rapidly calculated given only the old hash value, the old value removed from the window, and the new value added to the window—similar to the way a moving average function can be computed much more quickly than other low-pass filters; and similar to the way a Zobrist hash can be rapidly updated from the old hash value.

One of the main applications is the Rabin–Karp string search algorithm, which uses the rolling hash described below. Another popular application is the rsync program, which uses a checksum based on Mark Adler's adler-32 as its rolling hash. Low Bandwidth Network Filesystem (LBFS) uses a Rabin fingerprint as its rolling hash. FastCDC (Fast Content-Defined Chunking) uses a compute-efficient Gear fingerprint as its rolling hash.

At best, rolling hash values are pairwise independent or strongly universal. They cannot be 3-wise independent, for example.

## Polynomial rolling hash

The Rabin–Karp string search algorithm is often explained using a rolling hash function that only uses multiplications and additions:

$H=c_{1}a^{k-1}+c_{2}a^{k-2}+c_{3}a^{k-3}+...+c_{k}a^{0}$

,

where a is a constant, and $c_{1},...,c_{k}$ are the input characters (but this function is not a Rabin fingerprint, see below).

In order to avoid manipulating huge H values, all math is done modulo n . The choice of a and n is critical to get good hashing; in particular, the modulus n is typically a prime number. See linear congruential generator for more discussion.

Removing and adding characters simply involves adding or subtracting the first or last term. Shifting all characters by one position to the left requires multiplying the entire sum H by a . Shifting all characters by one position to the right requires dividing the entire sum H by a . Note that in modulo arithmetic, a can be chosen to have a multiplicative inverse $a^{-1}$ by which H can be multiplied to get the result of the division without actually performing a division.

## Rabin fingerprint

The Rabin fingerprint is another hash, which also interprets the input as a polynomial, but over the Galois field GF(2). Instead of seeing the input as a polynomial of bytes, it is seen as a polynomial of bits, and all arithmetic is done in GF(2) (similarly to CRC-32). The hash is the remainder after the division of that polynomial by an irreducible polynomial over GF(2). It is possible to update a Rabin fingerprint using only the entering and the leaving byte, making it effectively a rolling hash.

Because it shares the same author as the Rabin–Karp string search algorithm, which is often explained with another, simpler rolling hash, and because this simpler rolling hash is also a polynomial, both rolling hashes are often mistaken for each other.

## Cyclic polynomial

Hashing by cyclic polynomial—sometimes called Buzhash—is also simple and it has the benefit of avoiding multiplications, using circular shift instead. It is a form of tabulation hashing: it presumes that there is some substitution function s from characters to integers in the interval $[0,2^{L})$ , essentially a lookup table (each of the 32 bit-positions of the values of *s* should be balanced, i.e. have as many 1s as there are 0s). Let the function $\operatorname {rol}$ be bitwise rotation. E.g., $\operatorname {rol} (101)=011$ . Let $\oplus$ be the bitwise exclusive or. Let $c_{i}$ be the i-th byte in a stream, and w be the window size in use.

We precalculate $s'$ for removing the contribution of a byte that is out of the window:

$s'[i]=\operatorname {rol} (s[i],w)$

The hash values is defined as the following recurrence relation:

$H_{i}={\begin{cases}0&{\text{if }}i=0\\\operatorname {rol} (H_{i-1},1)\oplus s[c_{i}]&{\text{if }}i\leq w\\\operatorname {rol} (H_{i-1},1)\oplus s[c_{i}]\oplus s'[c_{i-w}]&{\text{if }}i>w\end{cases}}$

All values of *H* are within the interval $[0,2^{L})$ . This recurrence relation describes the way to compute the hash in a rolling fashion:

- Hash is initialized at 0.
- When the window is being filled, adding a character involves left-rotating the old hash by one position and XORing the new $s[c_{i}]$ .
- When the window is full, the same procedure is used to add a character, followed by removal of the contribution of the out-of-window character by XORing $s'[c_{i-w}]$ .

The value of *H* is neither formally uniform nor 2-universal, despite its empirical uniformity. However, it can be made formally uniform and pairwise independent if only a consecutive $L-w+1$ bits are taken from the hash. In practice, this can be a bitwise AND (masking) operation: $H'_{i}=H_{i}\mathbin {\&} (1\ll (w-1)-1)$ , where $\mathbin {\&}$ is a bitwise AND and $\ll$ is a left-shift.

In addition, the authors of borg note that *w* should not be a multiple of 2 *L* if a *seed* is used to modify *s[]* by XORing each value with the seed.

## Gear hashing

Gear chunking is another type of tabulation hashing. Let *s* be an unchanging table of 256 random unsigned 32-bit integers, *H* be the hash accumulator (unsigned integer, at least 32 bits), and *f* be the file represented as an array of bytes (8-bit integers, 1-based subscript). Let $\ll$ be the left-shift operator. The recurrence relation is:

$H_{0}=0$

$H_{i}=(H_{i-1}\ll 1)+s[f[i]]$

Compared to the cyclic polynomial hash, the left-rotate operation is replaced by left-shift, which removes the need to remove the contribution of an out-of-window byte. Xor is also replaced by addition. Chunking is done based on the top bits of *H*. This type of chunking generates results comparable with the Rabin fingerprint in one-third of the time. However, in practice the distribution of split-sizes were wider than Rabin, making deduplication results about 1% poorer for the typical cases and 6% poor for the worst case.

Using the bottom bits is also acceptable but reduces the effective sliding-window size. The largest effective size appears when the mask samples a number of non-consecutive bits from a relatively wide "span" of *H*.

## Content-based slicing using a rolling hash

One of the interesting use cases of the rolling hash function is that it can create dynamic, content-based chunks of a stream or file. This is especially useful when it is required to send only the changed chunks of a large file over a network: a simple byte addition at the front of the file would normally cause all fixed size windows to become updated, while in reality, only the first "chunk" has been modified.

A simple approach to making dynamic chunks is to calculate a rolling hash, and if the hash value matches an arbitrary pattern (e.g. all zeroes) in the lower *N* bits (with a probability of ${\textstyle {1 \over 2^{n}}}$ , given the hash has a uniform probability distribution) then it’s chosen to be a chunk boundary. Each chunk will thus have an average size of ${\textstyle 2^{n}}$ bytes. This approach ensures that unmodified data (more than a window size away from the changes) will have the same boundaries. Once the boundaries are known, the chunks need to be compared by cryptographic hash value to detect changes.

Such content-defined chunking (CDC) or content-based chunking (CBC) is often used for data deduplication. The hash function used can be any rolling-hash algorithm. Some examples are:

- Chunking on the least-significant bits
  - An unweighted sum (rsyncrypto)
  - Rabin-Karp polynomial rolling hash
- Rabin fingerprint, as used in the backup software restic (with blob size varying between 512KiB and 8MiB and 64-byte window).
- Chunking on any consecutive bits
  - Cyclic polynomial (buzhash), as used in the backup software Borg. Borg provides a customizable chunk size range for splitting file streams, based on varying the *N*, by default between 512KiB and 8MiB). It uses a 4095-byte window and non-balanced substitution function.
- Chunking on any collection of bits
  - A gear hash. Gear-based CDC has been successively optimized, yielding FastCDC, RapidCDC, and QuickCDC.

Content-based chunking has the advantage that in *most* cases, local changes to a file only affects the chunk it is in and possibly the next chunk, but no other chunk. Different choices of algorithms and hashes offer different strengths of this guarantee.

### Content-based slicing using moving sum

Several programs, including gzip (with the `--rsyncable` option) and rsyncrypto, do content-based slicing based on this specific (unweighted) moving sum:

$H(n)=\sum _{i=n-8195}^{n}c_{i}\mod 4096$

where

- $c_{i}$ is byte i of the file,
- $H(n)$ is a "hash value" consisting of the bottom 12 bits of the sum of 8196 consecutive bytes ending with byte n .

Shifting the window by one byte simply involves adding the new character to the sum and subtracting the oldest character (no longer in the window) from the sum. Because of the properties of modulo arithmetic, the storage required is only 12 bits.

For every n where $H(n)==0$ , these programs cut the file between n and $n+1$ .

### FastCDC

FastCDC optimizes Gear-based CDC mainly by adding a "kickstart" loop for bytes before the desired minimal size. By skipping the check for cutting, performance is improved while also adding a feature that allows for controlling the minimum size. The new scheme approximately doubles the speed over the olg Gear-based algorithm and is 10× as fast as the Rabin-based CDC approach.

The basic version pseudocode is provided as follows:

```
algorithm FastCDC
    input: data buffer src, 
           data length n, 
    output: cut point i
    
    MinSize ← 2KB     // split minimum chunk size is 2 KB
    MaxSize ← 64KB    // split maximum chunk size is 64 KB
    Mask ← 0x0000d93003530000 // 13 bits set -> desired average size is 2^13 bytes = 8 KB
    fp ← 0        // uint64
    i ← 0
    
    // buffer size is less than minimum chunk size
    if n ≤ MinSize then
        return n
    if n ≥ MaxSize then
        n ← MaxSize
    
    // Skip the first MinSize bytes, and kickstart the hash
    while i < MinSize do
        fp ← (fp << 1 ) + Gear[src[i]]
        i ← i + 1
     
    while i < n do
        fp ← (fp << 1 ) + Gear[src[i]]
        if !(fp & Mask) then
            return i
        i ← i + 1
   
    return i
```

Where the *Gear* array is equivalent to the *s* table above.

An advanced version uses two different masks derived from the above *Mask*, one with 15 set bits and the other with 11 set bits. The former is used when *i* < 8 KB; afterwards the latter takes over. This tightens the chunk-size distribution around the desired average and improves deduplication.

## Computational complexity

All rolling hash functions can be computed in linear time for the number of characters and updated in constant time when characters are shifted by one position. In particular, computing the Rabin–Karp rolling hash of a string of length k requires $O(k)$ modular arithmetic operations, and hashing by cyclic polynomials requires $O(k)$ bitwise exclusive ors and circular shifts.
