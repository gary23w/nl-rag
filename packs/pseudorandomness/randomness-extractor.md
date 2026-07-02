---
title: "Randomness extractor"
source: https://en.wikipedia.org/wiki/Randomness_extractor
domain: pseudorandomness
license: CC-BY-SA-4.0
tags: pseudorandomness theory, pseudorandom generator, randomness extractor, expander construction
fetched: 2026-07-02
---

# Randomness extractor

A **randomness extractor**, often simply called an "extractor", is a function, which being applied to output from a weak entropy source, together with a short, uniformly random seed, generates a highly random output that appears independent from the source and uniformly distributed. Examples of weakly random sources include radioactive decay or thermal noise; the only restriction on possible sources is that there is no way they can be fully controlled, calculated or predicted, and that a lower bound on their entropy rate can be established. For a given source, a randomness extractor can even be considered to be a true random number generator (TRNG); but there is no single extractor that has been proven to produce truly random output from any type of weakly random source.

Sometimes the term "bias" is used to denote a weakly random source's departure from uniformity, and in older literature, some extractors are called **unbiasing algorithms**, as they take the randomness from a so-called "biased" source and output a distribution that appears unbiased. The weakly random source will always be longer than the extractor's output, but an efficient extractor is one that lowers this ratio of lengths as much as possible, while simultaneously keeping the seed length low. Intuitively, this means that as much randomness as possible has been "extracted" from the source.

An extractor has some conceptual similarities with a pseudorandom generator (PRG), but the two concepts are not identical. Both are functions that take as input a small, uniformly random seed and produce a longer output that "looks" uniformly random. Some pseudorandom generators are, in fact, also extractors. (When a PRG is based on the existence of hard-core predicates, one can think of the weakly random source as a set of truth tables of such predicates and prove that the output is statistically close to uniform.) However, the general PRG definition does not specify that a weakly random source must be used, and while in the case of an extractor, the output should be statistically close to uniform, in a PRG it is only required to be computationally indistinguishable from uniform, a somewhat weaker concept.

## Formal definition of extractors

The min-entropy of a distribution X (denoted $H_{\infty }(X)$ ), is the largest real number k such that $\Pr[X=x]\leq 2^{-k}$ for every x in the range of X . In essence, this measures how likely X is to take its most likely value, giving a worst-case bound on how random X appears. Letting $U_{\ell }$ denote the uniform distribution over $\{{\texttt {0}},{\texttt {1}}\}^{\ell }$ , clearly $H_{\infty }(U_{\ell })=\ell$ .

For an *n*-bit distribution X with min-entropy *k*, we say that X is an $(n,k)$ distribution.

**Definition (Extractor):** **(*k*, *ε*)-extractor**

Let ${\text{Ext}}:\{{\texttt {0}},{\texttt {1}}\}^{n}\times \{{\texttt {0}},{\texttt {1}}\}^{d}\to \{{\texttt {0}},{\texttt {1}}\}^{m}$ be a function that takes as input a sample from an $(n,k)$ distribution X and a *d*-bit seed from $U_{d}$ , and outputs an *m*-bit string. ${\text{Ext}}$ is a **(*k*, *ε*)-extractor**, if for all $(n,k)$ distributions X , the output distribution of ${\text{Ext}}$ is *ε*-close to $U_{m}$ .

In the above definition, *ε*-close refers to statistical distance.

Intuitively, an extractor takes a weakly random *n*-bit input and a short, uniformly random seed and produces an *m*-bit output that looks uniformly random. The aim is to have a low d (i.e. to use as little uniform randomness as possible) and as high an m as possible (i.e. to get out as many close-to-random bits of output as we can).

### Strong extractors

An extractor is strong if concatenating the seed with the extractor's output yields a distribution that is still close to uniform.

**Definition (Strong Extractor):** A $(k,\epsilon )$ -strong extractor is a function

${\text{Ext}}:\{{\texttt {0}},{\texttt {1}}\}^{n}\times \{{\texttt {0}},{\texttt {1}}\}^{d}\rightarrow \{{\texttt {0}},{\texttt {1}}\}^{m}\,$

such that for every $(n,k)$ distribution X the distribution $U_{d}\circ {\text{Ext}}(X,U_{d})$ (the two copies of $U_{d}$ denote the same random variable) is $\epsilon$ -close to the uniform distribution on $U_{m+d}$ .

### Explicit extractors

Using the probabilistic method, it can be shown that there exists a (*k*, *ε*)-extractor, i.e. that the construction is possible. However, it is usually not enough merely to show that an extractor exists. An explicit construction is needed, which is given as follows:

**Definition (Explicit Extractor):** For functions *k*(*n*), *ε*(*n*), *d*(*n*), *m*(*n*) a family Ext = {Ext*n*} of functions

${\text{Ext}}_{n}:\{{\texttt {0}},{\texttt {1}}\}^{n}\times \{{\texttt {0}},{\texttt {1}}\}^{d(n)}\rightarrow \{{\texttt {0}},{\texttt {1}}\}^{m(n)}$

is an explicit (*k*, *ε*)-extractor, if Ext(*x*, *y*) can be computed in polynomial time (in its input length) and for every *n*, Ext*n* is a (*k*(*n*), *ε*(*n*))-extractor.

By the probabilistic method, it can be shown that there exists a (*k*, *ε*)-extractor with seed length

$d=\log {(n-k)}+2\log \left({\frac {1}{\varepsilon }}\right)+O(1)$

and output length

$m=k+d-2\log \left({\frac {1}{\varepsilon }}\right)-O(1)$

.

### Dispersers

A variant of the randomness extractor with weaker properties is the disperser.

## Randomness extractors in cryptography

One of the most important aspects of cryptography is random key generation. It is often necessary to generate secret and random keys from sources that are semi-secret or which may be compromised to some degree. By taking a single, short (and secret) random key as a source, an extractor can be used to generate a longer pseudo-random key, which then can be used for public key encryption. More specifically, when a strong extractor is used its output will appear be uniformly random, even to someone who sees part (but not all) of the source. For example, if the source is known but the seed is not known (or vice versa). This property of extractors is particularly useful in what is commonly called **Exposure-Resilient** cryptography in which the desired extractor is used as an **Exposure-Resilient Function** (ERF). Exposure-Resilient cryptography takes into account that the fact that it is difficult to keep secret the initial exchange of data which often takes place during the initialization of an encryption application e.g., the sender of encrypted information has to provide the receivers with information which is required for decryption.

The following paragraphs define and establish an important relationship between two kinds of ERF--***k*-ERF** and ***k*-APRF**--which are useful in Exposure-Resilient cryptography.

**Definition (*k*-ERF):** *An adaptive k-ERF is a function* f *where, for a random input* r *, when a computationally unbounded adversary* A *can adaptively read all of* r *except for* k *bits,* $|\Pr\{A^{r}(f(r))=1\}-\Pr\{A^{r}(R)=1\}|\leq \epsilon (n)$ *for some negligible function* $\epsilon (n)$ (defined below).

The goal is to construct an adaptive ERF whose output is highly random and uniformly distributed. But a stronger condition is often needed in which every output occurs with almost uniform probability. For this purpose **Almost-Perfect Resilient Functions** (APRF) are used. The definition of an APRF is as follows:

**Definition (k-APRF):** *A* $k=k(n)$ *APRF is a function* f *where, for any setting of* $n-k$ *bits of the input* r *to any fixed values, the probability vector* p *of the output* $f(r)$ *over the random choices for the* k *remaining bits satisfies* $|p_{i}-2^{-m}|<2^{-m}\epsilon (n)$ *for all* i *and for some negligible function* $\epsilon (n)$ .

Kamp and Zuckerman have proved a theorem stating that if a function f is a *k*-APRF, then f is also a *k*-ERF. More specifically, *any* extractor having sufficiently small error and taking as input an *oblivious*, bit-fixing source is also an APRF and therefore also a *k*-ERF. A more specific extractor is expressed in this lemma:

**Lemma:** *Any* $2^{-m}\epsilon (n)$ *-extractor* $f:\{{\texttt {0}},{\texttt {1}}\}^{n}\rightarrow \{{\texttt {0}},{\texttt {1}}\}^{m}$ *for the set of* $(n,k)$ *oblivious bit-fixing sources, where* $\epsilon (n)$ *is negligible, is also a k-APRF.*

This lemma is proved by Kamp and Zuckerman. The lemma is proved by examining the distance from uniform of the output, which in a $2^{-m}\epsilon (n)$ -extractor obviously is at most $2^{-m}\epsilon (n)$ , which satisfies the condition of the APRF.

The lemma leads to the following theorem, stating that there in fact exists a *k*-APRF function as described:

**Theorem (existence):** *For any positive constant* $\gamma \leq {\frac {1}{2}}$ *, there exists an explicit k-APRF* $f:\{{\texttt {0}},{\texttt {1}}\}^{n}\rightarrow \{{\texttt {0}},{\texttt {1}}\}^{m}$ *, computable in a linear number of arithmetic operations on* m *-bit strings, with* $m=\Omega (n^{2\gamma })$ *and* $k=n^{{\frac {1}{2}}+\gamma }$ .

**Definition (negligible function):** In the proof of this theorem, we need a definition of a negligible function. A function $\epsilon (n)$ is defined as being negligible if $\epsilon (n)=O\left({\frac {1}{n^{c}}}\right)$ for all constants c .

**Proof:** Consider the following $\epsilon$ -extractor: The function f is an extractor for the set of $(n,\delta n)$ oblivious bit-fixing source: $f:\{{\texttt {0}},{\texttt {1}}\}^{n}\rightarrow \{{\texttt {0}},{\texttt {1}}\}^{m}$ . f has $m=\Omega (\delta ^{2}n)$ , $\epsilon =2^{-cm}$ and $c>1$ .

The proof of this extractor's existence with $\delta \leq 1$ , as well as the fact that it is computable in linear computing time on the length of m can be found in the paper by Jesse Kamp and David Zuckerman (p. 1240).

That this extractor fulfills the criteria of the lemma is trivially true as $\epsilon =2^{-cm}$ is a negligible function.

The size of m is:

$m=\Omega (\delta ^{2}n)=\Omega (n)\geq \Omega (n^{2\gamma })$

Since we know $\delta \leq 1$ then the lower bound on m is dominated by n . In the last step we use the fact that $\gamma \leq {\frac {1}{2}}$ which means that the power of n is at most 1 . And since n is a positive integer we know that $n^{2\gamma }$ is at most n .

The value of k is calculated by using the definition of the extractor, where we know:

$(n,k)=(n,\delta n)\Rightarrow k=\delta n$

and by using the value of m we have:

$m=\delta ^{2}n=n^{2\gamma }$

Using this value of m we account for the worst case, where k is on its lower bound. Now by algebraic calculations we get:

$\delta ^{2}n=n^{2\gamma }$

$\Rightarrow \delta ^{2}=n^{2\gamma -1}$

$\Rightarrow \delta =n^{\gamma -{\frac {1}{2}}}$

Which inserted in the value of k gives

$k=\delta n=n^{\gamma -{\frac {1}{2}}}n=n^{\gamma +{\frac {1}{2}}}$

,

which proves that there exists an explicit k-APRF extractor with the given properties. $\Box$

## Examples

### Von Neumann extractor

Perhaps the earliest example is due to John von Neumann. From the input stream, his extractor took bits, two at a time (first and second, then third and fourth, and so on). If the two bits matched, no output was generated. If the bits differed, the value of the first bit was output. The Von Neumann extractor can be shown to produce a uniform output even if the distribution of input bits is not uniform so long as each bit has the same probability of being one and there is no correlation between successive bits.

Thus, it takes as input a Bernoulli sequence with p not necessarily equal to 1/2, and outputs a Bernoulli sequence with $p=1/2.$ More generally, it applies to any exchangeable sequence—it only relies on the fact that for any pair, 01 and 10 are *equally* likely: for independent trials, these have probabilities $p\cdot (1-p)=(1-p)\cdot p$ , while for an exchangeable sequence the probability may be more complicated, but both are equally likely. To put it simply, because the bits are statistically independent and due to the commutative property of multiplication, it would follow that $P(A\cap B)=P(A)P(B)=P(B)P(A)=P(B\cap A)$ . Hence, if pairs of 01 and 10 are mapped onto bits 0 and 1 and pairs 00 and 11 are discarded, then the output will be a uniform distribution.

Iterations upon the Von Neumann extractor include the Elias and Peres extractor, the latter of which reuses bits in order to produce larger output streams than the Von Neumann extractor given the same size input stream.

### Chaos machine

Another approach is to use the output of a chaos machine applied to the input stream. This approach generally relies on properties of chaotic systems. Input bits are pushed to the machine, evolving orbits and trajectories in multiple dynamical systems. Thus, small differences in the input produce very different outputs. Such a machine has a uniform output even if the distribution of input bits is not uniform or has serious flaws, and can therefore use weak entropy sources. Additionally, this scheme allows for increased complexity, quality, and security of the output stream, controlled by specifying three parameters: *time cost*, *memory required*, and *secret key*.

Note that while true chaotic systems are mathematically sound for 'amplifying' entropy, this is predicated on the availability of real numbers with an infinite precision. When implemented in digital computers with finite precision number representation, as in chaos machines using IEEE 754 Floating-Point, the periodicity has been shown to fall far short of the full space for a given bit length.

### Cryptographic hash function

It is also possible to use a cryptographic hash function as a randomness extractor. However, not every hashing algorithm is suitable for this purpose.

## Applications

Randomness extractors are used widely in cryptographic applications, whereby a cryptographic hash function is applied to a high-entropy, but non-uniform source, such as disk drive timing information or keyboard delays, to yield a uniformly random result.

Randomness extractors have played a major role in recent quantum cryptography developments, for example, distilling the raw output from a quantum random number generators into a shorter, secure and uniformly random output.

Strong extractors have proved useful in the generation of provable random numbers in commercial systems. Recently, they have made it possible for the (near-perfect) randomness output from a quantum computer to be used to enhance the quality of randomness in remote systems which do not have access to a quantum computer. The ability to deliver randomness proven using quantum physics entirely in software would not be possible without the use of strong extractors.

Randomness extraction is also used in some branches of computational complexity theory and in the construction of list-decodable error correcting codes.
