---
title: "Computational hardness assumption"
source: https://en.wikipedia.org/wiki/Computational_hardness_assumption
domain: cryptographic-hardness
license: CC-BY-SA-4.0
tags: cryptographic hardness assumption, computational hardness, learning with errors, discrete logarithm assumption
fetched: 2026-07-02
---

# Computational hardness assumption

In computational complexity theory, a **computational hardness assumption** is the hypothesis that a particular problem cannot be solved efficiently (where *efficiently* typically means "in polynomial time"). It is not known how to prove (unconditional) hardness for essentially any useful problem. Instead, computer scientists rely on reductions to formally relate the hardness of a new or complicated problem to a computational hardness assumption about a problem that is better-understood.

Computational hardness assumptions are of particular importance in cryptography. A major goal in cryptography is to create cryptographic primitives with provable security. In some cases, cryptographic protocols are found to have information theoretic security; the one-time pad is a common example. However, information theoretic security cannot always be achieved; in such cases, cryptographers fall back to computational security. Roughly speaking, this means that these systems are secure *assuming that any adversaries are computationally limited*, as all adversaries are in practice.

Computational hardness assumptions are also useful for guiding algorithm designers: a simple algorithm is unlikely to refute a well-studied computational hardness assumption such as P ≠ NP.

## Comparing hardness assumptions

Computer scientists have different ways of assessing which hardness assumptions are more reliable.

### Strength of hardness assumptions

We say that assumption A is *stronger* than assumption B when A implies B (and the converse is false or not known). In other words, even if assumption A were false, assumption B may still be true, and cryptographic protocols based on assumption B may still be safe to use. Thus when devising cryptographic protocols, one hopes to be able to prove security using the *weakest* possible assumptions.

### Average-case vs. worst-case assumptions

An average-case assumption says that a specific problem is hard on most instances from some explicit distribution, whereas a worst-case assumption only says that the problem is hard on *some* instances. For a given problem, average-case hardness implies worst-case hardness, so an average-case hardness assumption is stronger than a worst-case hardness assumption for the same problem. Furthermore, even for incomparable problems, an assumption like the exponential time hypothesis is often considered preferable to an average-case assumption like the planted clique conjecture. However, for cryptographic applications, knowing that a problem has some hard instance (the problem is hard in the worst-case) is useless because it does not provide us with a way of generating hard instances. Fortunately, many average-case assumptions used in cryptography (including RSA, discrete log, and some lattice problems) can be based on worst-case assumptions via worst-case-to-average-case reductions.

### Falsifiability

A desired characteristic of a computational hardness assumption is falsifiability, i.e. that if the assumption were false, then it would be possible to prove it. In particular, Naor (2003) introduced a formal notion of cryptographic falsifiability. Roughly, a computational hardness assumption is said to be falsifiable if it can be formulated in terms of a challenge: an interactive protocol between an adversary and an efficient verifier, where an efficient adversary can convince the verifier to accept if and only if the assumption is false.

## Common cryptographic hardness assumptions

There are many cryptographic hardness assumptions in use. This is a list of some of the most common ones, and some cryptographic protocols that use them.

### Integer factorization

Given a composite integer n , and in particular one which is the product of two large primes $n=p\cdot q$ , the integer factorization problem is to find p and q (more generally, find primes $p_{1},\dots ,p_{k}$ such that $n=\prod _{i}p_{i}$ ). It is a major open problem to find an algorithm for integer factorization that runs in time polynomial in the size of representation ( $\log n$ ). The security of many cryptographic protocols rely on the assumption that integer factorization is hard (i.e. cannot be solved in polynomial time). Cryptosystems whose security is equivalent to this assumption include Rabin signature and the Okamoto–Uchiyama cryptosystem. Many more cryptosystems rely on stronger assumptions such as RSA, residuosity problems, and phi-hiding.

#### RSA problem

Given a composite number n , exponent e and number $c:=m^{e}(\mathrm {mod} \;n)$ , the RSA problem is to find m . The problem is conjectured to be hard, but becomes easy given the factorization of n . In the RSA cryptosystem, $(n,e)$ is the public key, c is the encryption of message m , and the factorization of n is the secret key used for decryption.

#### Residuosity problems

Given a composite number n and integers $y,d$ , the residuosity problem is to determine whether there exists (alternatively, find an) x such that

$x^{d}\equiv y{\pmod {n}}.$

Important special cases include the quadratic residuosity problem and the decisional composite residuosity problem. As in the case of RSA, this problem (and its special cases) are conjectured to be hard, but become easy given the factorization of n . Some cryptosystems that rely on the hardness of residuousity problems include:

- Goldwasser–Micali cryptosystem (quadratic residuosity problem)
- Blum Blum Shub generator (quadratic residuosity problem)
- Paillier cryptosystem (decisional composite residuosity problem)
- Benaloh cryptosystem (higher residuosity problem)
- Naccache–Stern cryptosystem (higher residuosity problem)

#### Phi-hiding assumption

For a composite number m , it is not known how to efficiently compute its Euler's totient function $\phi (m)$ . The phi-hiding assumption postulates that it is hard to compute $\phi (m)$ , and furthermore even computing any prime factors of $\phi (m)$ is hard. This assumption is used in the Cachin–Micali–Stadler PIR protocol.

### Discrete log problem (DLP)

Given elements a and b from a group G , the discrete log problem asks for an integer k such that $a=b^{k}$ . The discrete log problem is not known to be comparable to integer factorization, but their computational complexities are closely related.

Most cryptographic protocols related to the discrete log problem actually rely on the stronger Diffie–Hellman assumption: given group elements $g,g^{a},g^{b}$ , where g is a generator and $a,b$ are random integers, it is hard to find $g^{a\cdot b}$ . Examples of protocols that use this assumption include the original Diffie–Hellman key exchange, as well as the ElGamal encryption (which relies on the yet stronger Decisional Diffie–Hellman (DDH) variant).

#### Multilinear maps

A multilinear map is a function $e:G_{1},\dots ,G_{n}\rightarrow G_{T}$ (where $G_{1},\dots ,G_{n},G_{T}$ are groups) such that for any $g_{1},\dots ,g_{n}\in G_{1},\dots G_{n}$ and $a_{1},\dots ,a_{n}$ ,

$e(g_{1}^{a_{1}},\dots ,g_{n}^{a_{n}})=e(g_{1},\dots ,g_{n})^{a_{1}\cdots a_{n}}$

.

For cryptographic applications, one would like to construct groups $G_{1},\dots ,G_{n},G_{T}$ and a map e such that the map and the group operations on $G_{1},\dots ,G_{n},G_{T}$ can be computed efficiently, but the discrete log problem on $G_{1},\dots ,G_{n}$ is still hard. Some applications require stronger assumptions, e.g. multilinear analogs of Diffie-Hellman assumptions.

For the special case of $n=2$ , bilinear maps with believable security have been constructed using Weil pairing and Tate pairing. For $n>2$ many constructions have been proposed in recent years, but many of them have also been broken, and currently there is no consensus about a safe candidate.

Some cryptosystems that rely on multilinear hardness assumptions include:

- Boneh-Franklin scheme (bilinear Diffie-Hellman)
- Boneh–Lynn–Shacham (bilinear Diffie-Hellman)
- Garg-Gentry-Halevi-Raykova-Sahai-Waters candidate for indistinguishability obfuscation and functional encryption (multilinear jigsaw puzzles)

### Lattice problems

The most fundamental computational problem on lattices is the shortest vector problem (SVP): given a lattice L , find the shortest non-zero vector $v\in L$ . Most cryptosystems require stronger assumptions on variants of SVP, such as shortest independent vectors problem (SIVP), GapSVP, or Unique-SVP.

The most useful lattice hardness assumption in cryptography is for the learning with errors (LWE) problem: Given samples to $(x,y)$ , where $y=f(x)$ for some linear function $f(\cdot )$ , it is easy to learn $f(\cdot )$ using linear algebra. In the LWE problem, the input to the algorithm has errors, i.e. for each pair $y\neq f(x)$ with some small probability. The errors are believed to make the problem intractable (for appropriate parameters); in particular, there are known worst-case to average-case reductions from variants of SVP.

For quantum computers, factoring and discrete log problems are easy, but lattice problems are conjectured to be hard. This makes some lattice-based cryptosystems candidates for post-quantum cryptography.

Some cryptosystems that rely on hardness of lattice problems include:

- NTRU (both NTRUEncrypt and NTRUSign)
- Most candidates for fully homomorphic encryption

## Non-cryptographic hardness assumptions

As well as their cryptographic applications, hardness assumptions are used in computational complexity theory to provide evidence for mathematical statements that are difficult to prove unconditionally. In these applications, one proves that the hardness assumption implies some desired complexity-theoretic statement, instead of proving that the statement is itself true. The best-known assumption of this type is the assumption that P ≠ NP, but others include the exponential time hypothesis, the planted clique conjecture, and the unique games conjecture.

### *C*-hard problems

Many worst-case computational problems are known to be hard or even complete for some complexity class C , in particular NP-hard (but often also PSPACE-hard, PPAD-hard, etc.). This means that they are at least as hard as any problem in the class C . If a problem is C -hard (with respect to polynomial time reductions), then it cannot be solved by a polynomial-time algorithm unless the computational hardness assumption $P\neq C$ is false.

### Exponential time hypothesis (ETH) and variants

The exponential time hypothesis (ETH) is a strengthening of $P\neq NP$ hardness assumption, which conjectures that not only does the Boolean satisfiability problem (SAT) not have a polynomial time algorithm, it furthermore requires exponential time ( $2^{\Omega (n)}$ ). An even stronger assumption, known as the strong exponential time hypothesis (SETH) conjectures that k -SAT requires $2^{(1-\varepsilon _{k})n}$ time, where $\lim _{k\rightarrow \infty }\varepsilon _{k}=0$ . ETH, SETH, and related computational hardness assumptions allow for deducing fine-grained complexity results, e.g. results that distinguish polynomial time and quasi-polynomial time, or even $n^{1.99}$ versus $n^{2}$ . Such assumptions are also useful in parametrized complexity.

### Average-case hardness assumptions

Some computational problems are assumed to be hard on average over a particular distribution of instances. For example, in the planted clique problem, the input is a random graph sampled, by sampling an Erdős–Rényi random graph and then "planting" a random k -clique, i.e. connecting k uniformly random nodes (where $2\log _{2}n\ll k\ll {\sqrt {n}}$ ), and the goal is to find the planted k -clique (which is unique w.h.p.). Another important example is Feige's Hypothesis, which is a computational hardness assumption about random instances of 3-SAT (sampled to maintain a specific ratio of clauses to variables). Average-case computational hardness assumptions are useful for proving average-case hardness in applications like statistics, where there is a natural distribution over inputs. Additionally, the planted clique hardness assumption has also been used to distinguish between polynomial and quasi-polynomial worst-case time complexity of other problems, similarly to the exponential time hypothesis.

### Unique games

The unique label cover problem is a constraint satisfaction problem, where each constraint C involves two variables $x,y$ , and for each value of x there is a *unique* value of y that satisfies C . Determining whether all the constraints can be satisfied is easy, but the **unique game conjecture** (UGC) postulates that determining whether almost all the constraints ( $(1-\varepsilon )$ -fraction, for any constant $\varepsilon >0$ ) can be satisfied or almost none of them ( $\varepsilon$ -fraction) can be satisfied is NP-hard. Approximation problems are often known to be NP-hard assuming UGC; such problems are referred to as UG-hard. In particular, assuming UGC there is a semidefinite programming algorithm that achieves optimal approximation guarantees for many important problems.

#### Small set expansion

Closely related to the unique label cover problem is the **small set expansion (SSE)** problem: Given a graph $G=(V,E)$ , find a small set of vertices (of size $n/\log(n)$ ) whose edge expansion is minimal. It is known that if SSE is hard to approximate, then so is unique label cover. Hence, the *small set expansion hypothesis*, which postulates that SSE is hard to approximate, is a stronger (but closely related) assumption than the unique game conjecture. Some approximation problems are known to be SSE-hard (i.e. at least as hard as approximating SSE).

### The 3SUM conjecture

Given a set of n numbers, the 3SUM problem asks whether there is a triplet of numbers whose sum is zero. There is a quadratic-time algorithm for 3SUM, and it has been conjectured that no algorithm can solve 3SUM in "truly sub-quadratic time": the **3SUM conjecture** is the computational hardness assumption that there are no $O(n^{2-\varepsilon })$ -time algorithms for 3SUM (for any constant $\varepsilon >0$ ). This conjecture is useful for proving near-quadratic lower bounds for several problems, mostly from computational geometry.
