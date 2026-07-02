---
title: "Golomb coding"
source: https://en.wikipedia.org/wiki/Rice_coding
domain: flac-lossless
license: CC-BY-SA-4.0
tags: flac lossless, linear predictive coding audio, rice coding, lossless audio
fetched: 2026-07-02
---

# Golomb coding

(Redirected from

Rice coding

)

**Golomb coding** is a lossless data compression method using a family of data compression codes invented by Solomon W. Golomb in the 1960s. Alphabets following a geometric distribution will have a Golomb code as an optimal prefix code, making Golomb coding highly suitable for situations in which the occurrence of small values in the input stream is significantly more likely than large values.

## Rice coding

**Rice coding** (invented by Robert F. Rice) denotes using a subset of the family of Golomb codes to produce a simpler (but possibly suboptimal) prefix code. Rice used this set of codes in an adaptive coding scheme; "Rice coding" can refer either to that adaptive scheme or to using that subset of Golomb codes. Whereas a Golomb code has a tunable parameter that can be any positive integer value, Rice codes are those in which the tunable parameter is a power of two. This makes Rice codes convenient for use on a computer, since multiplication and division by 2 can be implemented more efficiently in binary arithmetic.

Rice was motivated to propose this simpler subset due to the fact that geometric distributions are often varying with time, not precisely known, or both, so selecting the seemingly optimal code might not be very advantageous.

Rice coding is used as the entropy encoding stage in a number of lossless image compression and audio data compression methods.

## Overview

### Construction of codes

Golomb coding uses a tunable parameter M to divide an input value x into two parts: q, the result of a division by M, and r, the remainder. The quotient is sent in unary coding, followed by the remainder in truncated binary encoding. When $M=1$ , Golomb coding is equivalent to unary coding.

Golomb–Rice codes can be thought of as codes that indicate a number by the position of the *bin* (q), and the *offset* within the *bin* (r). The example figure shows the position q and offset r for the encoding of integer x using Golomb–Rice parameter *M* = 3, with source probabilities following a geometric distribution with *p*(0) = 0.2.

Formally, the two parts are given by the following expression, where x is the nonnegative integer being encoded:

$q=\left\lfloor {\frac {x}{M}}\right\rfloor$

and

$r=x-qM.$

Both q and r will be encoded using variable numbers of bits: q by a unary code, and r by b bits for Rice code, or a choice between b and *b*+1 bits for Golomb code (i.e. M is not a power of 2), with $b=\lfloor \log _{2}(M)\rfloor$ . If $r<2^{b+1}-M$ , then use b bits to encode r; otherwise, use b+1 bits to encode r. Clearly, $b=\log _{2}(M)$ if M is a power of 2 and we can encode all values of r with b bits.

The integer x treated by Golomb was the run length of a Bernoulli process, which has a geometric distribution starting at 0. The best choice of parameter M is a function of the corresponding Bernoulli process, which is parameterized by $p=P(x=0)$ the probability of success in a given Bernoulli trial. M is either the median of the distribution or the median ±1. It can be determined by these inequalities: $(1-p)^{M}+(1-p)^{M+1}\leq 1<(1-p)^{M-1}+(1-p)^{M},$ which are solved by $M=\left\lceil -{\frac {\log(2-p)}{\log(1-p)}}\right\rceil .$

For the example with *p*(0) = 0.2: $M=\left\lceil -{\frac {\log(1.8)}{\log(0.8)}}\right\rceil =\left\lceil 2.634\right\rceil =3.$

The Golomb code for this distribution is equivalent to the Huffman code for the same probabilities, if it were possible to compute the Huffman code for the infinite set of source values.

### Use with signed integers

Golomb's scheme was designed to encode sequences of non-negative numbers. However, it is easily extended to accept sequences containing negative numbers using an *overlap and interleave* scheme, in which all values are reassigned to some positive number in a unique and reversible way. The sequence begins: 0, −1, 1, −2, 2, −3, 3, −4, 4, ... The *n*-th negative value (i.e., ⁠ $-n$ ⁠) is mapped to the *n*th odd number (⁠ $2n-1$ ⁠), and the *m*th positive value is mapped to the *m*-th even number (⁠ $2m$ ⁠). This may be expressed mathematically as follows: a positive value x is mapped to ( $x'=2|x|=2x,\ x\geq 0$ ), and a negative value y is mapped to ( $y'=2|y|-1=-2y-1,\ y<0$ ). Such a code may be used for simplicity, even if suboptimal. Truly optimal codes for two-sided geometric distributions include multiple variants of the Golomb code, depending on the distribution parameters, including this one.

## Simple algorithm

Below is the Rice–Golomb encoding, where the remainder code uses simple truncated binary encoding, also named "Rice coding" (other varying-length binary encodings, like arithmetic or Huffman encodings, are possible for the remainder codes, if the statistic distribution of remainder codes is not flat, and notably when not all possible remainders after the division are used). In this algorithm, if the *M* parameter is a power of 2, it becomes equivalent to the simpler Rice encoding:

1. Fix the parameter *M* to an integer value.
2. For *N*, the number to be encoded, find
  1. quotient = *q* = floor(*N*/*M*)
  2. remainder = *r* = *N* modulo *M*
3. Generate codeword
  1. The code format : <Quotient code><Remainder code>, where
  2. Quotient code (in unary coding)
    1. Write a *q*-length string of 1 bits (alternatively, of 0 bits)
    2. Write a 0 bit (respectively, a 1 bit)
  3. Remainder code (in truncated binary encoding)
    1. Let $b=\lfloor \log _{2}(M)\rfloor$
      1. If $r<2^{b+1}-M$ code *r* in binary representation using *b* bits.
      2. If $r\geq 2^{b+1}-M$ code the number $r+2^{b+1}-M$ in binary representation using *b* + 1 bits.

Decoding:

1. Decode the unary representation of *q* (count the number of 1 in the beginning of the code)
2. Skip the 0 delimiter
3. Let $b=\lfloor \log _{2}(M)\rfloor$
  1. Interpret next *b* bits as a binary number *r'*. If $r'<2^{b+1}-M$ holds, then the remainder $r=r'$
  2. Otherwise interpret *b + 1* bits as a binary number *r'*, the remainder is given by $r=r'-2^{b+1}+M$
4. Compute $N=q*M+r$

## Example

Set *M* = 10. Thus $b=\lfloor \log _{2}(10)\rfloor =3$ . The cutoff is $2^{b+1}-M=16-10=6$ .

| Encoding of quotient part q output bits 0 0 1 10 2 110 3 1110 4 11110 5 111110 6 1111110 $\vdots$ $\vdots$ N $\underbrace {111\cdots 111} _{N}0$ | Encoding of remainder part r offset binary output bits 0 0 0000 000 1 1 0001 001 2 2 0010 010 3 3 0011 011 4 4 0100 100 5 5 0101 101 6 12 1100 1100 7 13 1101 1101 8 14 1110 1110 9 15 1111 1111 |
|---|---|

For example, with a Rice–Golomb encoding using parameter *M* = 10, the decimal number 42 would first be split into q = 4 and r = 2, and would be encoded as qcode(q),rcode(r) = qcode(4),rcode(2) = 11110,010 (you don't need to encode the separating comma in the output stream, because the 0 at the end of the q code is enough to say when q ends and r begins; both the qcode and rcode are self-delimited).

## Use for run-length encoding

Note that

p

and

1 – p

are reversed in this section compared to the use in earlier sections.

Given an alphabet of two symbols, or a set of two events, *P* and *Q*, with probabilities *p* and (1 − *p*) respectively, where *p* ≥ 1/2, Golomb coding can be used to encode runs of zero or more *P*′s separated by single *Q*′s. In this application, the best setting of the parameter *M* is the nearest integer to $-{\frac {1}{\log _{2}p}}$ . When *p* = 1/2, *M* = 1, and the Golomb code corresponds to unary (*n* ≥ 0 *P*′s followed by a *Q* is encoded as *n* ones followed by a zero). If a simpler code is desired, one can assign Golomb–Rice parameter b (i.e., Golomb parameter $M=2^{b}$ ) to the integer nearest to $-\log _{2}(-\log _{2}p)$ ; although not always the best parameter, it is usually the best Rice parameter and its compression performance is quite close to the optimal Golomb code. (Rice himself proposed using various codes for the same data to figure out which was best. A later JPL researcher proposed various methods of optimizing or estimating the code parameter.)

Consider using a Rice code with a binary portion having b bits to run-length encode sequences where *P* has a probability p. If $\mathbb {P} [{\text{bit is part of }}k{\text{-run}}]$ is the probability that a bit will be part of an k-bit run ( $k-1$ *P*s and one *Q*) and $({\text{compression ratio of }}k{\text{-run}})$ is the compression ratio of that run, then the expected compression ratio is ${\begin{aligned}\mathbb {E} [{\text{compression ratio}}]&=\sum _{k=1}^{\infty }({\text{compression ratio of }}k{\text{-run}})\cdot \mathbb {P} [{\text{bit is part of }}k{\text{-run}}]\\&=\sum _{k=1}^{\infty }{\frac {b+1+\lfloor 2^{-b}(k-1)\rfloor }{k}}\cdot kp^{k-1}(1-p)^{2}\\&=(1-p)^{2}\sum _{j=0}^{\infty }(b+1+j)\cdot \sum _{i=j2^{b}+1}^{(j+1)2^{b}}p^{i-1}\\&=(1-p)^{2}\sum _{j=0}^{\infty }(b+1+j)\cdot \left(p^{2^{b}j}-p^{2^{b}(j+1)}\right)\\&=(1-p)\cdot \left(b+\sum _{m=0}^{\infty }p^{2^{b}m}\right)\\&=(1-p)\cdot \left(b+{\left(1-p^{2^{b}}\right)}^{-1}\right)\\\end{aligned}}$

Compression is often expressed in terms of $1-\mathbb {E} [{\text{compression ratio}}]$ , the proportion compressed. For $p\approx 1$ , the run-length coding approach results in compression ratios close to entropy. For example, using Rice code $b=6$ for $p=0.99$ yields 91.89% compression, while the entropy limit is 91.92%.

## Adaptive run-length Golomb–Rice encoding

When a probability distribution for integers is not known, the optimal parameter for a Golomb–Rice encoder cannot be determined. Thus, in many applications, a two-pass approach is used: first, the block of data is scanned to estimate a probability density function (PDF) for the data. The Golomb–Rice parameter is then determined from that estimated PDF. A simpler variation of that approach is to assume that the PDF belongs to a parametrized family, estimate the PDF parameters from the data, and then compute the optimal Golomb–Rice parameter. That is the approach used in most of the applications discussed below.

An alternative approach to efficiently encode integer data whose PDF is not known, or is varying, is to use a backwards-adaptive encoder. The RLGR encoder [1] achieves that using a very simple algorithm that adjusts the Golomb–Rice parameter up or down, depending on the last encoded symbol. A decoder can follow the same rule to track the variation of the encoding parameters, so no side information needs to be transmitted, just the encoded data. Assuming a generalized Gaussian PDF, which covers a wide range of statistics seen in data such as prediction errors or transform coefficients in multimedia codecs, the RLGR encoding algorithm can perform very well in such applications.

## Applications

Numerous signal codecs use a Rice code for prediction residues. In predictive algorithms, such residues tend to fall into a two-sided geometric distribution, with small residues being more frequent than large residues, and the Rice code closely approximates the Huffman code for such a distribution without the overhead of having to transmit the Huffman table. One signal that does not match a geometric distribution is a sine wave, because the differential residues create a sinusoidal signal whose values are not creating a geometric distribution (the highest and lowest residue values have similar high frequency of occurrences, only the median positive and negative residues occur less often).

Several lossless audio codecs, such as Shorten, FLAC, Apple Lossless, and MPEG-4 ALS, use a Rice code after the linear prediction step (called "adaptive FIR filter" in Apple Lossless). Rice coding is also used in the FELICS lossless image codec.

The Golomb–Rice coder is used in the entropy coding stage of Rice algorithm based *lossless image codecs*. One such experiment yields the compression ratio graph shown.

The JPEG-LS scheme uses Rice–Golomb to encode the prediction residuals.

The RLGR adaptive version of Golomb–Rice coding mentioned above [2] is used for encoding screen content in virtual machines in the RemoteFX component of the Microsoft Remote Desktop Protocol. It is also used in the recent G-PCC MPEG standard ISO/IEC 23090‑9 for point-cloud attribute compression.
