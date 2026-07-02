---
title: "Pseudorandom number generator"
source: https://en.wikipedia.org/wiki/Pseudorandom_number_generator
domain: particle-systems
license: CC-BY-SA-4.0
tags: particle system, particle emitter, gpu particles, particle effect
fetched: 2026-07-02
---

# Pseudorandom number generator

A **pseudorandom number generator** (**PRNG**), also known as a **deterministic random bit generator** (**DRBG**), is an algorithm for generating a sequence of numbers whose properties approximate the properties of sequences of random numbers. The PRNG-generated sequence is not truly random, because it is completely determined by an initial value, called the PRNG's *seed* (which may include truly random values). Although sequences that are closer to truly random can be generated using hardware random number generators, ***pseudorandom number generators*** are important in practice for their speed in number generation and their reproducibility.

PRNGs are central in applications such as simulations (e.g. for the Monte Carlo method), electronic games (e.g. for procedural generation), and cryptography. Cryptographic applications require the output not to be predictable from earlier outputs, and more elaborate algorithms, which do not inherit the linearity of simpler PRNGs, are needed.

Good statistical properties are a central requirement for the output of a PRNG. In general, careful mathematical analysis is required to have any confidence that a PRNG generates numbers that are sufficiently close to random to suit the intended use. John von Neumann cautioned about the misinterpretation of a PRNG as a truly random generator, joking that "Anyone who considers arithmetical methods of producing random digits is, of course, in a state of sin."

## Potential issues

In practice, the output from many common PRNGs exhibit artifacts that cause them to fail statistical pattern-detection tests. These include:

- Shorter-than-expected periods for some seed states (such seed states may be called "weak" in this context);
- Lack of uniformity of distribution for large quantities of generated numbers;
- Correlation of successive values;
- Poor dimensional distribution of the output sequence;
- Distances between where certain values occur are distributed differently from those in a random sequence distribution.

Defects exhibited by flawed PRNGs range from unnoticeable (and unknown) to very obvious. An example was the RANDU random number algorithm used for decades on mainframe computers. It was seriously flawed, but its inadequacy went undetected for a very long time.

In many fields, research work prior to the 21st century that relied on random selection or on Monte Carlo simulations, or in other ways relied on PRNGs, were much less reliable than ideal as a result of using poor-quality PRNGs. Even today, caution is sometimes required, as illustrated by the following warning in the *International Encyclopedia of Statistical Science* (2010).

> The list of widely used generators that should be discarded is much longer [than the list of good generators]. Do not trust blindly the software vendors. Check the default RNG of your favorite software and be ready to replace it if needed. This last recommendation has been made over and over again over the past 40 years. Perhaps amazingly, it remains as relevant today as it was 40 years ago.

As an illustration, consider the widely used programming language Java. Up until 2020, Java still relied on a linear congruential generator (LCG) for its PRNG, which is of low quality (see further below). Java support was upgraded with Java 17.

One well-known PRNG to avoid major problems and still run fairly quickly is the Mersenne Twister (discussed below), which was published in 1998. Other higher-quality PRNGs, both in terms of computational and statistical performance, were developed before and after this date; these can be identified in the List of pseudorandom number generators.

## Generators based on linear recurrences

In the second half of the 20th century, the standard class of algorithms used for PRNGs comprised linear congruential generators. The quality of LCGs was known to be inadequate, but better methods were unavailable. Press et al. (2007) described the result thus: "If all scientific papers whose results are in doubt because of [LCGs and related] were to disappear from library shelves, there would be a gap on each shelf about as big as your fist."

A major advance in the construction of pseudorandom generators was the introduction of techniques based on linear recurrences on the two-element field; such generators are related to linear-feedback shift registers.

The 1997 invention of the Mersenne Twister, in particular, avoided many of the problems with earlier generators. The Mersenne Twister has a period of 219 937 − 1 iterations (≈ 4.3×106001), is proven to be equidistributed in (up to) 623 dimensions (for 32-bit values), and at the time of its introduction was running faster than other statistically reasonable generators.

In 2003, George Marsaglia introduced the family of xorshift generators, again based on a linear recurrence. Such generators are extremely fast and, combined with a nonlinear operation, they pass strong statistical tests.

In 2006, the WELL family of generators was developed. The WELL generators in some ways improves on the quality of the Mersenne Twister, which has a too-large state space and a very slow recovery from state spaces with a large number of zeros.

## Counter-based RNGs

A counter-based random number generation (CBRNG, also known as a counter-based pseudo-random number generator, or CBPRNG) is a kind of PRNG that uses only an integer counter as its internal state:

${\text{ output }}=f(n,{\text{ key}})$

They are generally used for generating pseudorandom numbers for large parallel computations, such as over GPU or CPU clusters. They have certain advantages:

- The only "state" needed is the counter value and the key. For a given counter and key, the output is always the same. This property makes CBRNGs reproducible.
- Because each random number is computed independently of any previous outputs, they can be generated in parallel. For example, in a massively parallel application, each thread or GPU core can be assigned a range of counter values and compute random numbers without synchronization or shared state.
- Since the generator does not require stepping through every intermediate state, it can "jump" to any point in the sequence in constant time. This is particularly useful in applications like Monte Carlo simulations where independent streams are needed.

Examples include:

- Philox: Uses multiplication-based mixing to combine the counter and key.
- Threefry: Based on a reduced-strength version of the Threefish block cipher.

## Cryptographic PRNGs

A PRNG suitable for cryptographic applications is called a *cryptographically-secure PRNG* (CSPRNG). A requirement for a CSPRNG is that an adversary not knowing the seed has only negligible advantage in distinguishing the generator's output sequence from a random sequence. In other words, while a PRNG is only required to pass certain statistical tests, a CSPRNG must pass all statistical tests that are restricted to polynomial time in the size of the seed. Though a proof of this property is beyond the current state of the art of computational complexity theory, strong evidence may be provided by reducing to the CSPRNG from a problem that is assumed to be hard, such as integer factorization. In general, years of review may be required before an algorithm can be certified as a CSPRNG.

Some classes of CSPRNGs include the following:

- stream ciphers
- block ciphers running in counter or output feedback mode
- PRNGs that have been designed specifically to be cryptographically secure, such as Microsoft's Cryptographic Application Programming Interface function CryptGenRandom, the Yarrow algorithm (incorporated in Mac OS X and FreeBSD), and Fortuna
- combination PRNGs which attempt to combine several PRNG primitive algorithms with the goal of removing any detectable non-randomness
- special designs based on mathematical hardness assumptions: examples include the *Micali–Schnorr generator*, Naor-Reingold pseudorandom function and the Blum Blum Shub algorithm, which provide a strong security proof (such algorithms are rather slow compared to traditional constructions, and impractical for many applications)
- generic PRNGs: while it has been shown that a (cryptographically) secure PRNG can be constructed generically from any one-way function, this generic construction is extremely slow in practice, so is mainly of theoretical interest.

It has been shown to be likely that the NSA has inserted an asymmetric backdoor into the NIST-certified pseudorandom number generator Dual_EC_DRBG.

Most PRNG algorithms produce sequences that are uniformly distributed by any of several tests. It is an open question, and one central to the theory and practice of cryptography, whether there is any way to distinguish the output of a high-quality PRNG from a truly random sequence. In this setting, the distinguisher knows that either the known PRNG algorithm was used (but not the state with which it was initialized) or a truly random algorithm was used, and has to distinguish between the two. The security of most cryptographic algorithms and protocols using PRNGs is based on the assumption that it is infeasible to distinguish use of a suitable PRNG from use of a truly random sequence. The simplest examples of this dependency are stream ciphers, which (most often) work by exclusive or-ing the plaintext of a message with the output of a PRNG, producing ciphertext. The design of cryptographically adequate PRNGs is extremely difficult because they must meet additional criteria. The size of its period is an important factor in the cryptographic suitability of a PRNG, but not the only one.

## BSI evaluation criteria

The German Federal Office for Information Security (German: *Bundesamt für Sicherheit in der Informationstechnik*, BSI) has established four criteria for quality of deterministic random number generators. They are summarized here:

- K1 – There should be a high probability that generated sequences of random numbers are different from each other.
- K2 – A sequence of numbers is indistinguishable from "truly random" numbers according to specified statistical tests. The tests are the *monobit* test (equal numbers of ones and zeros in the sequence), *poker* test (a special instance of the chi-squared test), *runs* test (counts the frequency of runs of various lengths), *longruns* test (checks whether there exists any run of length 34 or greater in 20 000 bits of the sequence)—both from BSI and NIST, and the *autocorrelation* test. In essence, these requirements are a test of how well a bit sequence: has zeros and ones equally often; after a sequence of *n* zeros (or ones), the next bit a one (or zero) with probability one-half; and any selected subsequence contains no information about the next element(s) in the sequence.
- K3 – It should be impossible for an attacker (for all practical purposes) to calculate, or otherwise guess, from any given subsequence, any previous or future values in the sequence, nor any inner state of the generator.
- K4 – It should be impossible, for all practical purposes, for an attacker to calculate, or guess from an inner state of the generator, any previous numbers in the sequence or any previous inner generator states.

For cryptographic applications, only generators meeting the K3 or K4 standards are acceptable.

## Mathematical definition

Given:

- P – a probability distribution on $\left(\mathbb {R} ,{\mathfrak {B}}\right)$ (where ${\mathfrak {B}}$ is the sigma-algebra of all Borel subsets of the real line)
- ${\mathfrak {F}}$ – a non-empty collection of Borel sets ${\mathfrak {F}}\subseteq {\mathfrak {B}}$ , e.g. ${\mathfrak {F}}=\left\{\left(-\infty ,t\right]:t\in \mathbb {R} \right\}$ . If ${\mathfrak {F}}$ is not specified, it may be either ${\mathfrak {B}}$ or $\left\{\left(-\infty ,t\right]:t\in \mathbb {R} \right\}$ , depending on context.
- $A\subseteq \mathbb {R}$ – a non-empty set (not necessarily a Borel set). Often A is a set between P 's support and its interior; for instance, if P is the uniform distribution on the interval $\left(0,1\right]$ , A might be $\left(0,1\right]$ . If A is not specified, it is assumed to be some set contained in the support of P and containing its interior, depending on context.

We call a function $f:\mathbb {N} _{1}\rightarrow \mathbb {R}$ (where $\mathbb {N} _{1}=\left\{1,2,3,\dots \right\}$ is the set of positive integers) a **pseudo-random number generator for P given ${\mathfrak {F}}$ taking values in A** if and only if:

- $f\left(\mathbb {N} _{1}\right)\subseteq A$
- $\forall E\in {\mathfrak {F}}\quad \forall \varepsilon >0\quad \exists N\in \mathbb {N} _{1}\quad \forall n\geq N,\quad \left|{\frac {\#\left\{i\in \left\{1,2,\dots ,n\right\}:f(i)\in E\right\}}{n}}-P(E)\right|<\varepsilon$

( $\#S$ denotes the number of elements in the finite set S .)

It can be shown that if f is a pseudo-random number generator for the uniform distribution on $\left(0,1\right)$ and if F is the CDF of some given probability distribution P , then $F^{*}\circ f$ is a pseudo-random number generator for P , where $F^{*}:\left(0,1\right)\rightarrow \mathbb {R}$ is the percentile of P , i.e. $F^{*}(x):=\inf \left\{t\in \mathbb {R} :x\leq F(t)\right\}$ . Intuitively, an arbitrary distribution can be simulated from a simulation of the standard uniform distribution.

## Early approaches

An early computer-based PRNG, suggested by John von Neumann in 1946, is known as the middle-square method. The algorithm is as follows: take any number, square it, remove the middle digits of the resulting number as the "random number", then use that number as the seed for the next iteration. For example, squaring the number "1111" yields "1234321", which can be written as "01234321", an 8-digit number being the square of a 4-digit number. This gives "2343" as the "random" number. Repeating this procedure gives "4896" as the next result, and so on. Von Neumann used 10 digit numbers, but the process was the same.

A problem with the "middle square" method is that all sequences eventually repeat themselves, some very quickly, such as "0000". Von Neumann was aware of this, but he found the approach sufficient for his purposes and was worried that mathematical "fixes" would simply hide errors rather than remove them.

Von Neumann judged hardware random number generators unsuitable, for, if they did not record the output generated, they could not later be tested for errors. If they did record their output, they would exhaust the limited computer memories then available, and so the computer's ability to read and write numbers. If the numbers were written to cards, they would take very much longer to write and read. On the ENIAC computer he was using, the "middle square" method generated numbers at a rate some hundred times faster than reading numbers in from punched cards.

The middle-square method has since been supplanted by more elaborate generators.

A recent innovation is to combine the middle square with a Weyl sequence. This method produces high-quality output through a long period (see middle-square method).

## Non-uniform generators

Numbers selected from a non-uniform probability distribution can be generated using a uniform distribution PRNG and a function that relates the two distributions.

First, one needs the cumulative distribution function $F(b)$ of the target distribution $f(b)$ :

$F(b)=\int _{-\infty }^{b}f(b')\,db'$

Note that $0=F(-\infty )\leq F(b)\leq F(\infty )=1$ . Using a random number *c* from a uniform distribution as the probability density to "pass by", we get

$F(b)=c$

so that

$b=F^{-1}(c)$

is a number randomly selected from distribution $f(b)$ . This is based on the inverse transform sampling.

For example, the inverse of cumulative Gaussian distribution $\operatorname {erf} ^{-1}(x)$ with an ideal uniform PRNG with range (0, 1) as input x would produce a sequence of (positive only) values with a Gaussian distribution; however

- When using practical number representations, the infinite "tails" of the distribution have to be truncated to finite values.
- Repetitive recalculation of $\operatorname {erf} ^{-1}(x)$ should be reduced by means such as ziggurat algorithm for faster generation.

Similar considerations apply to generating other non-uniform distributions such as Rayleigh and Poisson.
