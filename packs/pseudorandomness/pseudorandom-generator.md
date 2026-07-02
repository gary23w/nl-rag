---
title: "Pseudorandom generator"
source: https://en.wikipedia.org/wiki/Pseudorandom_generator
domain: pseudorandomness
license: CC-BY-SA-4.0
tags: pseudorandomness theory, pseudorandom generator, randomness extractor, expander construction
fetched: 2026-07-02
---

# Pseudorandom generator

In theoretical computer science and cryptography, a **pseudorandom generator (PRG)** for a class of statistical tests is a deterministic procedure that maps a random seed to a longer pseudorandom string such that no statistical test in the class can distinguish between the output of the generator and the uniform distribution. The random seed itself is typically a short binary string drawn from the uniform distribution.

Many different classes of statistical tests have been considered in the literature, among them the class of all Boolean circuits of a given size. It is not known whether good pseudorandom generators for this class exist, but it is known that their existence is in a certain sense equivalent to (unproven) circuit lower bounds in computational complexity theory. Hence the construction of pseudorandom generators for the class of Boolean circuits of a given size rests on currently unproven hardness assumptions.

## Definition

Let ${\mathcal {A}}=\{A:\{0,1\}^{n}\to \{0,1\}^{*}\}$ be a class of functions. These functions are the *statistical tests* that the pseudorandom generator will try to fool, and they are usually algorithms. Sometimes the statistical tests are also called *adversaries* or *distinguishers*. The notation in the codomain of the functions is the Kleene star.

A function $G:\{0,1\}^{\ell }\to \{0,1\}^{n}$ with $\ell <n$ is a *pseudorandom generator* against ${\mathcal {A}}$ with *bias* $\varepsilon$ if, for every A in ${\mathcal {A}}$ , the statistical distance between the distributions $A(G(U_{\ell }))$ and $A(U_{n})$ is at most $\varepsilon$ , where $U_{k}$ is the uniform distribution on $\{0,1\}^{k}$ .

The quantity $\ell$ is called the *seed length* and the quantity $n-\ell$ is called the *stretch* of the pseudorandom generator.

A pseudorandom generator against a family of adversaries $({\mathcal {A}}_{n})_{n\in \mathbb {N} }$ with bias $\varepsilon (n)$ is a family of pseudorandom generators $(G_{n})_{n\in \mathbb {N} }$ , where $G_{n}:\{0,1\}^{\ell (n)}\to \{0,1\}^{n}$ is a pseudorandom generator against ${\mathcal {A}}_{n}$ with bias $\varepsilon (n)$ and seed length $\ell (n)$ .

In most applications, the family ${\mathcal {A}}$ represents some model of computation or some set of algorithms, and one is interested in designing a pseudorandom generator with small seed length and bias, and such that the output of the generator can be computed by the same sort of algorithm.

## In cryptography

In cryptography, the class ${\mathcal {A}}$ usually consists of all circuits of size polynomial in the input and with a single bit output, and one is interested in designing pseudorandom generators that are computable by a polynomial-time algorithm and whose bias is negligible in the circuit size. These pseudorandom generators are sometimes called **cryptographically secure pseudorandom generators (CSPRGs)**.

It is not known if cryptographically secure pseudorandom generators exist. Proving that they exist is difficult since their existence implies P ≠ NP, which is widely believed but a famously open problem. The existence of cryptographically secure pseudorandom generators is widely believed. This is because it has been proven that pseudorandom generators can be constructed from any one-way function which are believed to exist. Pseudorandom generators are necessary for many applications in cryptography.

The pseudorandom generator theorem shows that cryptographically secure pseudorandom generators exist if and only if one-way functions exist.

### Uses

Pseudorandom generators have numerous applications in cryptography. For instance, pseudorandom generators provide an efficient analog of one-time pads. It is well known that in order to encrypt a message *m* in a way that the cipher text provides no information on the plaintext, the key *k* used must be random over strings of length |m|. Perfectly secure encryption is very costly in terms of key length. Key length can be significantly reduced using a pseudorandom generator if perfect security is replaced by semantic security. Common constructions of stream ciphers are based on pseudorandom generators.

Pseudorandom generators may also be used to construct symmetric key cryptosystems, where a large number of messages can be safely encrypted under the same key. Such a construction can be based on a pseudorandom function family, which generalizes the notion of a pseudorandom generator.

In the 1980s, simulations in physics began to use pseudorandom generators to produce sequences with billions of elements, and by the late 1980s, evidence had developed that a few common generators gave incorrect results in such cases as phase transition properties of the 3D Ising model and shapes of diffusion-limited aggregates. Then in the 1990s, various idealizations of physics simulations—based on random walks, correlation functions, localization of eigenstates, etc., were used as tests of pseudorandom generators.

### Testing

NIST announced SP800-22 Randomness tests to test whether a pseudorandom generator produces high quality random bits. Yongge Wang showed that NIST testing is not enough to detect weak pseudorandom generators and developed statistical distance based testing technique LILtest.

## For derandomization

A main application of pseudorandom generators lies in the derandomization of computation that relies on randomness, without corrupting the result of the computation. Physical computers are deterministic machines, and obtaining true randomness can be a challenge. Pseudorandom generators can be used to efficiently simulate randomized algorithms with using little or no randomness. In such applications, the class ${\mathcal {A}}$ describes the randomized algorithm or class of randomized algorithms that one wants to simulate, and the goal is to design an "efficiently computable" pseudorandom generator against ${\mathcal {A}}$ whose seed length is as short as possible. If a full derandomization is desired, a completely deterministic simulation proceeds by replacing the random input to the randomized algorithm with the pseudorandom string produced by the pseudorandom generator. The simulation does this for all possible seeds and averages the output of the various runs of the randomized algorithm in a suitable way.

### Constructions

#### For polynomial time

A fundamental question in computational complexity theory is whether all polynomial time randomized algorithms for decision problems can be deterministically simulated in polynomial time. The existence of such a simulation would imply that **BPP** = **P**. To perform such a simulation, it is sufficient to construct pseudorandom generators against the family **F** of all circuits of size *s*(*n*) whose inputs have length *n* and output a single bit, where *s*(*n*) is an arbitrary polynomial, the seed length of the pseudorandom generator is O(log *n*) and its bias is ⅓.

In 1991, Noam Nisan and Avi Wigderson provided a candidate pseudorandom generator with these properties. In 1997 Russell Impagliazzo and Avi Wigderson proved that the construction of Nisan and Wigderson is a pseudorandom generator assuming that there exists a decision problem that can be computed in time 2O(*n*) on inputs of length *n* but requires circuits of size 2Ω(*n*).

#### For logarithmic space

While unproven assumption about circuit complexity are needed to prove that the Nisan–Wigderson generator works for time-bounded machines, it is natural to restrict the class of statistical tests further such that we need not rely on such unproven assumptions. One class for which this has been done is the class of machines whose work space is bounded by $O(\log n)$ . Using a repeated squaring trick known as Savitch's theorem, it is easy to show that every probabilistic log-space computation can be simulated in space $O(\log ^{2}n)$ . Noam Nisan (1992) showed that this derandomization can actually be achieved with a pseudorandom generator of seed length $O(\log ^{2}n)$ that fools all $O(\log n)$ -space machines. Nisan's generator has been used by Saks and Zhou (1999) to show that probabilistic log-space computation can be simulated deterministically in space $O(\log ^{1.5}n)$ . This result was improved by William Hoza in 2021 to space $O(\log ^{1.5}n/{\sqrt {\log \log n}})$ .

#### For linear functions

When the statistical tests consist of all multivariate linear functions over some finite field $\mathbb {F}$ , one speaks of epsilon-biased generators. The construction of Naor & Naor (1990) achieves a seed length of $\ell =\log n+O(\log(\epsilon ^{-1}))$ , which is optimal up to constant factors. Pseudorandom generators for linear functions often serve as a building block for more complicated pseudorandom generators.

#### For polynomials

Viola (2008) proves that taking the sum of d small-bias generators fools polynomials of degree d . The seed length is $\ell =d\cdot \log n+O(2^{d}\cdot \log(\epsilon ^{-1}))$ .

#### For constant-depth circuits

Constant depth circuits that produce a single output bit.

## Limitations on probability

The pseudorandom generators used in cryptography and universal algorithmic derandomization have not been proven to exist, although their existence is widely believed. Proofs for their existence would imply proofs of lower bounds on the circuit complexity of certain explicit functions. Such circuit lower bounds cannot be proved in the framework of natural proofs assuming the existence of stronger variants of cryptographic pseudorandom generators.
