---
title: "Decoding methods"
source: https://en.wikipedia.org/wiki/Decoding_methods
domain: self-consistency-decoding
license: CC-BY-SA-4.0
tags: self consistency decoding, majority vote reasoning, sampled reasoning paths, answer aggregation prompting, diverse reasoning sampling
fetched: 2026-07-02
---

# Decoding methods

In coding theory, **decoding** is the process of translating received messages into codewords of a given code. There have been many common methods of mapping messages to codewords. These are often used to recover messages sent over a noisy channel, such as a binary symmetric channel.

## Notation

$C\subset \mathbb {F} _{2}^{n}$ is considered a binary code with the length n ; $x,y$ shall be elements of $\mathbb {F} _{2}^{n}$ ; and $d(x,y)$ is the distance between those elements.

## Ideal observer decoding

One may be given the message $x\in \mathbb {F} _{2}^{n}$ , then **ideal observer decoding** generates the codeword $y\in C$ . The process results in this solution:

$\mathbb {P} (y{\mbox{ sent}}\mid x{\mbox{ received}})$

For example, a person can choose the codeword y that is most likely to be received as the message x after transmission.

### Decoding conventions

Each codeword does not have an expected possibility: there may be more than one codeword with an equal likelihood of mutating into the received message. In such a case, the sender and receiver(s) must agree ahead of time on a decoding convention. Popular conventions include:

1. Request that the codeword be resent – automatic repeat-request.
2. Choose any random codeword from the set of most likely codewords which is nearer to that.
3. If another code follows, mark the ambiguous bits of the codeword as erasures and hope that the outer code disambiguates them
4. Report a decoding failure to the system

## Maximum likelihood decoding

Given a received vector $x\in \mathbb {F} _{2}^{n}$ **maximum likelihood decoding** picks a codeword $y\in C$ that maximizes

$\mathbb {P} (x{\mbox{ received}}\mid y{\mbox{ sent}})$

,

that is, the codeword y that maximizes the probability that x was received, given that y was sent. If all codewords are equally likely to be sent then this scheme is equivalent to ideal observer decoding. In fact, by Bayes' theorem,

${\begin{aligned}\mathbb {P} (x{\mbox{ received}}\mid y{\mbox{ sent}})&{}={\frac {\mathbb {P} (x{\mbox{ received}},y{\mbox{ sent}})}{\mathbb {P} (y{\mbox{ sent}})}}\\&{}=\mathbb {P} (y{\mbox{ sent}}\mid x{\mbox{ received}})\cdot {\frac {\mathbb {P} (x{\mbox{ received}})}{\mathbb {P} (y{\mbox{ sent}})}}.\end{aligned}}$

Upon fixing $\mathbb {P} (x{\mbox{ received}})$ , x is restructured and $\mathbb {P} (y{\mbox{ sent}})$ is constant as all codewords are equally likely to be sent. Therefore, $\mathbb {P} (x{\mbox{ received}}\mid y{\mbox{ sent}})$ is maximised as a function of the variable y precisely when $\mathbb {P} (y{\mbox{ sent}}\mid x{\mbox{ received}})$ is maximised, and the claim follows.

As with ideal observer decoding, a convention must be agreed to for non-unique decoding.

The maximum likelihood decoding problem can also be modeled as an integer programming problem.

The maximum likelihood decoding algorithm is an instance of the "marginalize a product function" problem which is solved by applying the generalized distributive law.

## Minimum distance decoding

Given a received vector $x\in \mathbb {F} _{2}^{n}$ , **minimum distance decoding** picks a codeword $y\in C$ to minimise the Hamming distance:

$d(x,y)=|\{i:x_{i}\not =y_{i}\}|$

i.e. choose the codeword y that is as close as possible to x .

Note that if the probability of error on a discrete memoryless channel p is strictly less than one half, then *minimum distance decoding* is equivalent to *maximum likelihood decoding*, since if

$d(x,y)=d,\,$

then:

${\begin{aligned}\mathbb {P} (y{\mbox{ received}}\mid x{\mbox{ sent}})&{}=(1-p)^{n-d}\cdot p^{d}\\&{}=(1-p)^{n}\cdot \left({\frac {p}{1-p}}\right)^{d}\\\end{aligned}}$

which (since *p* is less than one half) is maximised by minimising *d*.

Minimum distance decoding is also known as *nearest neighbour decoding*. It can be assisted or automated by using a standard array. Minimum distance decoding is a reasonable decoding method when the following conditions are met:

1. The probability p that an error occurs is independent of the position of the symbol.
2. Errors are independent events – an error at one position in the message does not affect other positions.

These assumptions may be reasonable for transmissions over a binary symmetric channel. They may be unreasonable for other media, such as a DVD, where a single scratch on the disk can cause an error in many neighbouring symbols or codewords.

As with other decoding methods, a convention must be agreed to for non-unique decoding.

## Syndrome decoding

**Syndrome decoding** is a highly efficient method of decoding a linear code over a *noisy channel*, i.e. one on which errors are made. In essence, syndrome decoding is *minimum distance decoding* using a reduced lookup table. This is allowed by the linearity of the code.

Suppose that $C\subset \mathbb {F} _{2}^{n}$ is a linear code of length n and minimum distance d with parity-check matrix H . Then clearly C is capable of correcting up to

$t=\left\lfloor {\frac {d-1}{2}}\right\rfloor$

errors made by the channel (since if no more than t errors are made then minimum distance decoding will still correctly decode the incorrectly transmitted codeword).

Now suppose that a codeword $x\in \mathbb {F} _{2}^{n}$ is sent over the channel and the error pattern $e\in \mathbb {F} _{2}^{n}$ occurs. Then $z=x+e$ is received. Ordinary minimum distance decoding would lookup the vector z in a table of size $|C|$ for the nearest match - i.e. an element (not necessarily unique) $c\in C$ with

$d(c,z)\leq d(y,z)$

for all $y\in C$ . Syndrome decoding takes advantage of the property of the parity matrix that:

$Hx=0$

for all $x\in C$ . The *syndrome* of the received $z=x+e$ is defined to be:

$Hz=H(x+e)=Hx+He=0+He=He$

To perform ML decoding in a binary symmetric channel, one has to look-up a precomputed table of size $2^{n-k}$ , mapping $He$ to e .

Note that this is already of significantly less complexity than that of a standard array decoding.

However, under the assumption that no more than t errors were made during transmission, the receiver can look up the value $He$ in a further reduced table of size

${\begin{matrix}\sum _{i=0}^{t}{\binom {n}{i}}\\\end{matrix}}$

## List decoding

## Information set decoding

This is a family of Las Vegas-probabilistic methods all based on the observation that it is easier to guess enough error-free positions, than it is to guess all the error-positions.

The simplest form is due to Prange: Let G be the $k\times n$ generator matrix of C used for encoding. Select k columns of G at random, and denote by $G'$ the corresponding submatrix of G . With reasonable probability $G'$ will have full rank, which means that if we let $c'$ be the sub-vector for the corresponding positions of any codeword $c=mG$ of C for a message m , we can recover m as $m=c'G'^{-1}$ . Hence, if we were lucky that these k positions of the received word y contained no errors, and hence equalled the positions of the sent codeword, then we may decode.

If t errors occurred, the probability of such a fortunate selection of columns is given by $\textstyle {\binom {n-t}{k}}/{\binom {n}{k}}\approx \exp(-tk/n)$ .

This method has been improved in various ways, e.g. by Stern and Canteaut and Sendrier.

## Partial response maximum likelihood

Partial response maximum likelihood (PRML) is a method for converting the weak analog signal from the head of a magnetic disk or tape drive into a digital signal.

## Viterbi decoder

A Viterbi decoder uses the Viterbi algorithm for decoding a bitstream that has been encoded using forward error correction based on a convolutional code. The Hamming distance is used as a metric for hard decision Viterbi decoders. The *squared* Euclidean distance is used as a metric for soft decision decoders.

## Optimal decision decoding algorithm (ODDA)

Optimal decision decoding algorithm (ODDA) for an asymmetric TWRC system.
