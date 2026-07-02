---
title: "Learning with errors"
source: https://en.wikipedia.org/wiki/Learning_with_errors
domain: homomorphic-encryption-applied
license: CC-BY-SA-4.0
tags: homomorphic encryption, fully homomorphic encryption, paillier cryptosystem, learning with errors, lattice based cryptography
fetched: 2026-07-02
---

# Learning with errors

In cryptography, **learning with errors** (**LWE**) is a mathematical problem that is widely used to create secure encryption algorithms. It is based on the idea of representing secret information as a set of equations with errors. In other words, LWE is a way to hide the value of a secret by introducing noise to it. In more technical terms, it refers to the computational problem of inferring a linear n -ary function f over a finite ring from given samples $y_{i}=f(\mathbf {x} _{i})$ some of which may be erroneous. The LWE problem is conjectured to be hard to solve, and thus to be useful in cryptography.

More precisely, the LWE problem is defined as follows. Let $\mathbb {Z} _{q}$ denote the ring of integers modulo q and let $\mathbb {Z} _{q}^{n}$ denote the set of n -vectors over $\mathbb {Z} _{q}$ . There exists a certain unknown linear function $f:\mathbb {Z} _{q}^{n}\rightarrow \mathbb {Z} _{q}$ , and the input to the LWE problem is a sample of pairs $(\mathbf {x} ,y)$ , where $\mathbf {x} \in \mathbb {Z} _{q}^{n}$ and $y\in \mathbb {Z} _{q}$ , so that with high probability $y=f(\mathbf {x} )$ . Furthermore, the deviation from the equality is according to some known noise model. The problem calls for finding the function f , or some close approximation thereof, with high probability.

The LWE problem was introduced by Oded Regev in 2005 (who won the 2018 Gödel Prize for this work); it is a generalization of the parity learning problem. Regev showed that the LWE problem is as hard to solve as several worst-case lattice problems. Subsequently, the LWE problem has been used as a hardness assumption to create public-key cryptosystems, such as the ring learning with errors key exchange by Peikert.

## Definition

Denote by $\mathbb {T} =\mathbb {R} /\mathbb {Z}$ the additive group on reals modulo one. Let $\mathbf {s} \in \mathbb {Z} _{q}^{n}$ be a fixed vector. Let $\phi$ be a fixed probability distribution over $\mathbb {T}$ . Denote by $A_{\mathbf {s} ,\phi }$ the distribution on $\mathbb {Z} _{q}^{n}\times \mathbb {T}$ obtained as follows.

1. Pick a vector $\mathbf {a} \in \mathbb {Z} _{q}^{n}$ from the uniform distribution over $\mathbb {Z} _{q}^{n}$ ,
2. Pick a number $e\in \mathbb {T}$ from the distribution $\phi$ ,
3. Evaluate $t=\langle \mathbf {a} ,\mathbf {s} \rangle /q+e$ , where $\textstyle \langle \mathbf {a} ,\mathbf {s} \rangle =\sum _{i=1}^{n}a_{i}s_{i}$ is the standard inner product in $\mathbb {Z} _{q}^{n}$ , the division is done in the field of reals (or more formally, this "division by q " is notation for the group homomorphism $\mathbb {Z} _{q}\longrightarrow \mathbb {T}$ mapping $1\in \mathbb {Z} _{q}$ to $1/q+\mathbb {Z} \in \mathbb {T}$ ), and the final addition is in $\mathbb {T}$ .
4. Output the pair $(\mathbf {a} ,t)$ .

The **learning with errors problem** $\mathrm {LWE} _{q,\phi }$ is to find $\mathbf {s} \in \mathbb {Z} _{q}^{n}$ , given access to polynomially many samples of choice from $A_{\mathbf {s} ,\phi }$ .

For every $\alpha >0$ , denote by $D_{\alpha }$ the one-dimensional Gaussian with zero mean and variance $\alpha ^{2}/(2\pi )$ , that is, the density function is $D_{\alpha }(x)=\rho _{\alpha }(x)/\alpha$ where $\rho _{\alpha }(x)=e^{-\pi (|x|/\alpha )^{2}}$ , and let $\Psi _{\alpha }$ be the distribution on $\mathbb {T}$ obtained by considering $D_{\alpha }$ modulo one. The version of LWE considered in most of the results would be $\mathrm {LWE} _{q,\Psi _{\alpha }}$

## Decision version

The **LWE** problem described above is the *search* version of the problem. In the *decision* version (**DLWE**), the goal is to distinguish between noisy inner products and uniformly random samples from $\mathbb {Z} _{q}^{n}\times \mathbb {T}$ (practically, some discretized version of it). Regev showed that the *decision* and *search* versions are equivalent when q is a prime bounded by some polynomial in n .

Intuitively, if we have a procedure for the search problem, the decision version can be solved easily: just feed the input samples for the decision problem to the solver for the search problem. Denote the given samples by $\{(\mathbf {a} _{i},\mathbf {b} _{i})\}\subset \mathbb {Z} _{q}^{n}\times \mathbb {T}$ . If the solver returns a candidate $\mathbf {s}$ , for all i , calculate $\{\langle \mathbf {a} _{i},\mathbf {s} \rangle -\mathbf {b} _{i}\}$ . If the samples are from an LWE distribution, then the results of this calculation will be distributed according $\chi$ , but if the samples are uniformly random, these quantities will be distributed uniformly as well.

For the other direction, given a solver for the decision problem, the search version can be solved as follows: Recover $\mathbf {s}$ one coordinate at a time. To obtain the first coordinate, $\mathbf {s} _{1}$ , make a guess $k\in \mathbb {Z} _{q}$ , and do the following. Choose a number $r\in \mathbb {Z} _{q}$ uniformly at random. Transform the given samples $\{(\mathbf {a} _{i},\mathbf {b} _{i})\}\subset \mathbb {Z} _{q}^{n}\times \mathbb {T}$ as follows. Calculate $\{(\mathbf {a} _{i}+(r,0,\ldots ,0),\mathbf {b} _{i}+(rk)/q)\}$ . Send the transformed samples to the decision solver.

If the guess k was correct, the transformation takes the distribution $A_{\mathbf {s} ,\chi }$ to itself, and otherwise, since q is prime, it takes it to the uniform distribution. So, given a polynomial-time solver for the decision problem that errs with very small probability, since q is bounded by some polynomial in n , it only takes polynomial time to guess every possible value for k and use the solver to see which one is correct.

After obtaining $\mathbf {s} _{1}$ , we follow an analogous procedure for each other coordinate $\mathbf {s} _{j}$ . Namely, we transform our $\mathbf {b} _{i}$ samples the same way, and transform our $\mathbf {a} _{i}$ samples by calculating $\mathbf {a} _{i}+(0,\ldots ,r,\ldots ,0)$ , where the r is in the $j^{\text{th}}$ coordinate.

Peikert showed that this reduction, with a small modification, works for any q that is a product of distinct, small (polynomial in n ) primes. The main idea is if $q=q_{1}q_{2}\cdots q_{t}$ , for each $q_{\ell }$ , guess and check to see if $\mathbf {s} _{j}$ is congruent to $0\mod q_{\ell }$ , and then use the Chinese remainder theorem to recover $\mathbf {s} _{j}$ .

### Average case hardness

Regev showed the random self-reducibility of the **LWE** and **DLWE** problems for arbitrary q and $\chi$ . Given samples $\{(\mathbf {a} _{i},\mathbf {b} _{i})\}$ from $A_{\mathbf {s} ,\chi }$ , it is easy to see that $\{(\mathbf {a} _{i},\mathbf {b} _{i}+\langle \mathbf {a} _{i},\mathbf {t} \rangle )/q\}$ are samples from $A_{\mathbf {s} +\mathbf {t} ,\chi }$ .

So, suppose there was some set ${\mathcal {S}}\subset \mathbb {Z} _{q}^{n}$ such that $|{\mathcal {S}}|/|\mathbb {Z} _{q}^{n}|=1/\operatorname {poly} (n)$ , and for distributions $A_{\mathbf {s} ',\chi }$ , with $\mathbf {s} '\leftarrow {\mathcal {S}}$ , **DLWE** was easy.

Then there would be some distinguisher ${\mathcal {A}}$ , who, given samples $\{(\mathbf {a} _{i},\mathbf {b} _{i})\}$ , could tell whether they were uniformly random or from $A_{\mathbf {s} ',\chi }$ . If we need to distinguish uniformly random samples from $A_{\mathbf {s} ,\chi }$ , where $\mathbf {s}$ is chosen uniformly at random from $\mathbb {Z} _{q}^{n}$ , we could simply try different values $\mathbf {t}$ sampled uniformly at random from $\mathbb {Z} _{q}^{n}$ , calculate $\{(\mathbf {a} _{i},\mathbf {b} _{i}+\langle \mathbf {a} _{i},\mathbf {t} \rangle )/q\}$ and feed these samples to ${\mathcal {A}}$ . Since ${\mathcal {S}}$ comprises a large fraction of $\mathbb {Z} _{q}^{n}$ , with high probability, if we choose a polynomial number of values for $\mathbf {t}$ , we will find one such that $\mathbf {s} +\mathbf {t} \in {\mathcal {S}}$ , and ${\mathcal {A}}$ will successfully distinguish the samples.

Thus, no such ${\mathcal {S}}$ can exist, meaning **LWE** and **DLWE** are (up to a polynomial factor) as hard in the average case as they are in the worst case.

## Hardness results

### Regev's result

For a *n*-dimensional lattice L , let *smoothing parameter* $\eta _{\varepsilon }(L)$ denote the smallest s such that $\rho _{1/s}(L^{*}\setminus \{\mathbf {0} \})\leq \varepsilon$ where $L^{*}$ is the dual of L and $\rho _{\alpha }(x)=e^{-\pi (|x|/\alpha )^{2}}$ is extended to sets by summing over function values at each element in the set. Let $D_{L,r}$ denote the discrete Gaussian distribution on L of width r for a lattice L and real $r>0$ . The probability of each $x\in L$ is proportional to $\rho _{r}(x)$ .

The *discrete Gaussian sampling problem* (DGS) is defined as follows: An instance of $DGS_{\phi }$ is given by an n -dimensional lattice L and a number $r\geq \phi (L)$ . The goal is to output a sample from $D_{L,r}$ . Regev shows that there is a reduction from $\operatorname {GapSVP} _{100{\sqrt {n}}\gamma (n)}$ to $DGS_{{\sqrt {n}}\gamma (n)/\lambda (L^{*})}$ for any function $\gamma (n)\geq 1$ .

Regev then shows that there exists an efficient quantum algorithm for $DGS_{{\sqrt {2n}}\eta _{\varepsilon }(L)/\alpha }$ given access to an oracle for $\mathrm {LWE} _{q,\Psi _{\alpha }}$ for integer q and $\alpha \in (0,1)$ such that $\alpha q>2{\sqrt {n}}$ . This implies the hardness for LWE. Although the proof of this assertion works for any q , for creating a cryptosystem, the modulus q has to be polynomial in n .

### Peikert's result

Peikert proves that there is a probabilistic polynomial time reduction from the $\operatorname {GapSVP} _{\zeta ,\gamma }$ problem in the worst case to solving $\mathrm {LWE} _{q,\Psi _{\alpha }}$ using $\operatorname {poly} (n)$ samples for parameters $\alpha \in (0,1)$ , $\gamma (n)\geq n/(\alpha {\sqrt {\log n}})$ , $\zeta (n)\geq \gamma (n)$ and $q\geq (\zeta /{\sqrt {n}})\omega {\sqrt {\log n}})$ .

## Use in cryptography

The **LWE** problem serves as a versatile problem used in construction of several cryptosystems. In 2005, Regev showed that the decision version of LWE is hard assuming quantum hardness of the lattice problems $\mathrm {GapSVP} _{\gamma }$ (for $\gamma$ as above) and $\mathrm {SIVP} _{t}$ with $t=O(n/\alpha )$ ). In 2009, Peikert proved a similar result assuming only the classical hardness of the related problem $\mathrm {GapSVP} _{\zeta ,\gamma }$ . The disadvantage of Peikert's result is that it bases itself on a non-standard version of an easier (when compared to SIVP) problem GapSVP.

### Public-key cryptosystem

Regev proposed a public-key cryptosystem based on the hardness of the **LWE** problem. The cryptosystem as well as the proof of security and correctness are completely classical. The system is characterized by $m,q$ and a probability distribution $\chi$ on $\mathbb {T}$ . The setting of the parameters used in proofs of correctness and security is

- $q\geq 2$ , usually a prime number between $n^{2}$ and $2n^{2}$ .
- $m=(1+\varepsilon )(n+1)\log q$ for an arbitrary constant $\varepsilon$
- $\chi =\Psi _{\alpha (n)}$ for $\alpha (n)\in o(1/{\sqrt {n}}\log n)$ , where $\Psi _{\beta }$ is a probability distribution obtained by sampling a normal variable with mean 0 and standard variation ${\frac {\beta }{\sqrt {2\pi }}}$ and reducing the result modulo 1 .

The cryptosystem is then defined by:

- *Private key*: Private key is an $\mathbf {s} \in \mathbb {Z} _{q}^{n}$ chosen uniformly at random.
- *Public key*: Choose m vectors $\mathbf {a} _{1},\ldots ,\mathbf {a} _{m}\in \mathbb {Z} _{q}^{n}$ uniformly and independently. Choose error offsets $e_{1},\ldots ,e_{m}\in \mathbb {T}$ independently according to $\chi$ . The public key consists of $(\mathbf {a} _{i},b_{i}=\langle \mathbf {a} _{i},\mathbf {s} \rangle /q+e_{i})_{i=1}^{m}$
- *Encryption*: The encryption of a bit $x\in \{0,1\}$ is done by choosing a random subset S of $[m]$ and then defining $\operatorname {Enc} (x)$ as

$\left(\sum _{i\in S}\mathbf {a} _{i},{\frac {x}{2}}+\sum _{i\in S}b_{i}\right)$

- *Decryption*: The decryption of $(\mathbf {a} ,b)$ is 0 if $b-\langle \mathbf {a} ,\mathbf {s} \rangle /q$ is closer to 0 than to ${\frac {1}{2}}$ , and 1 otherwise.

The proof of correctness follows from choice of parameters and some probability analysis. The proof of security is by reduction to the decision version of **LWE**: an algorithm for distinguishing between encryptions (with above parameters) of 0 and 1 can be used to distinguish between $A_{s,\chi }$ and the uniform distribution over $\mathbb {Z} _{q}^{n}\times \mathbb {T}$

### CCA-secure cryptosystem

Peikert proposed a system that is secure even against any chosen-ciphertext attack.

### Key exchange

The idea of using LWE and Ring LWE for key exchange was proposed and filed at the University of Cincinnati in 2011 by Jintai Ding. The idea comes from the associativity of matrix multiplications, and the errors are used to provide the security. The paper appeared in 2012 after a provisional patent application was filed in 2012.

The security of the protocol is proven based on the hardness of solving the LWE problem. In 2014, Peikert presented a key-transport scheme following the same basic idea of Ding's, where the new idea of sending an additional 1-bit signal for rounding in Ding's construction is also used. The "new hope" implementation selected for Google's post-quantum experiment, uses Peikert's scheme with variation in the error distribution.

### Ring learning with errors signature (RLWE-SIG)

A RLWE version of the classic Feige–Fiat–Shamir Identification protocol was created and converted to a digital signature in 2011 by Lyubashevsky. The details of this signature were extended in 2012 by Gunesyu, Lyubashevsky, and Popplemann in 2012 and published in their paper "Practical Lattice Based Cryptography – A Signature Scheme for Embedded Systems." These papers laid the groundwork for a variety of recent signature algorithms some based directly on the ring learning with errors problem and some which are not tied to the same hard RLWE problems.
